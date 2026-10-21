# SPDX-FileCopyrightText: 2026 Aarav Jalan and Abhinav Patro
# SPDX-License-Identifier: MIT
"""Generate original native KiCad logical role schematics, not physical pin maps."""
import uuid,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def uid(s):return str(uuid.uuid5(uuid.NAMESPACE_URL,'SkyRelief/reference/'+s))
def q(s):return json.dumps(s,ensure_ascii=False)
DISC='Historical SkyRelief hardware dossier with modern engineering reconstruction.'
WARN='REFERENCE IMPLEMENTATION — NOT VERIFIED HISTORICAL SKYRELIEF WIRING.'
class Sheet:
 def __init__(self,name,title):
  self.name=name;self.title=title;self.root=uid(name);self.libs={};self.items=[];self.n=0
 def text(self,t,x,y,size=1.2):
  size=round(size*1.55,3)
  self.items.append(f'(text {q(t)} (at {x} {y} 0) (effects (font (size {size} {size})) (justify left)) (uuid "{uid(self.name+t+str(x)+str(y))}"))')
 def module(self,ref,value,x,y,left,right,types=None):
  x=round(x/1.27)*1.27;y=round(y/1.27)*1.27
  # logical IDs only. pins named by functional role; no physical board pin implication.
  lib=self.name+'_'+ref;count=max(len(left),len(right));hy=max(6.35,(count+1)*2.54/2)
  pins=[]
  positions={}
  idx=0
  for side,names in [('L',left),('R',right)]:
   for i,n in enumerate(names):
    idx+=1;py=((len(names)-1)/2-i)*2.54;px=-22.86 if side=='L' else 22.86;ang=0 if side=='L' else 180
    kind=(types or {}).get(n,'passive')
    pins.append(f'(pin {kind} line (at {px} {py} {ang}) (length 5.08) (name {q(n)} (effects (font (size 1.6 1.6)))) (number "{idx}" (effects (font (size 1.1 1.1)))))')
    positions[n]=(round(x+px,4),round(y-py,4),str(idx))
  self.libs[lib]=f'''(symbol {q('SkyRelief:'+lib)} (pin_names (offset 0.5)) (exclude_from_sim no) (in_bom yes) (on_board no)
   (property "Reference" "U" (at 0 {hy+2.54} 0) (effects (font (size 1.8 1.8))))
   (property "Value" {q(value)} (at 0 {-hy-2.54} 0) (effects (font (size 1.8 1.8))))
   (property "Footprint" "" (at 0 0 0) (effects (font (size 1.8 1.8)) hide))
   (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.8 1.8)) hide))
   (symbol "{lib}_0_1" (rectangle (start -17.78 {hy}) (end 17.78 {-hy}) (stroke (width 0.254) (type default)) (fill (type background))))
   (symbol "{lib}_1_1" {''.join(pins)}))'''
  self.items.append(f'''(symbol (lib_id {q('SkyRelief:'+lib)}) (at {x} {y} 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board no) (dnp no)
   (uuid "{uid(self.name+ref)}")
   (property "Reference" "{ref}" (at {x} {y-hy-3} 0) (effects (font (size 1.8 1.8))))
   (property "Value" {q(value)} (at {x} {y+hy+3} 0) (effects (font (size 1.8 1.8))))
   (property "Footprint" "" (at {x} {y} 0) (effects (font (size 1.8 1.8)) hide))
   (property "Datasheet" "" (at {x} {y} 0) (effects (font (size 1.8 1.8)) hide))
   {''.join('(pin "'+str(i)+'" (uuid "'+uid(self.name+ref+str(i))+'"))' for i in range(1,idx+1))}
   (instances (project "{self.name}" (path "/{self.root}" (reference "{ref}") (unit 1)))))''')
  return positions
 def wirelabel(self,p,net,side):
  x,y,_=p;xx=x+(-7.62 if side=='L' else 7.62);self.n+=1
  justify='right bottom' if side=='L' else 'left bottom'
  self.items.append(f'(wire (pts (xy {x} {y}) (xy {xx} {y})) (stroke (width 0) (type default)) (uuid "{uid(self.name+"w"+str(self.n))}"))')
  self.items.append(f'(label "{net}" (at {xx} {y} 0) (effects (font (size 1.6 1.6)) (justify {justify})) (uuid "{uid(self.name+"l"+str(self.n))}"))')
 def save(self):
  head=f'''(kicad_sch (version 20250114) (generator "skyrelief_reference_builder") (generator_version "0.1")
   (uuid "{self.root}") (paper "A4")
   (title_block (title {q(self.title)}) (date "2026-10-20") (rev "0.1.0-review") (company "SkyRelief engineering documentation")
   (comment 1 "Logical roles only; no historical physical pin map recovered.")
   (comment 2 "CERN-OHL-W-2.0, (c) 2026 Aarav Jalan and Abhinav Patro; no physical test performed."))
   (lib_symbols {''.join(self.libs.values())})
   {''.join(self.items)}
   (embedded_fonts no))'''
  out=R/'kicad';out.mkdir(exist_ok=True)
  (out/(self.name+'.kicad_sch')).write_text(head,encoding='utf8')
  pro={'meta':{'filename':self.name+'.kicad_pro','version':1},'schematic':{'meta':{'version':1}},'net_settings':{'classes':[{'name':'Default','clearance':0.2,'track_width':0.25,'via_diameter':0.8,'via_drill':0.4,'wire_width':6}],'meta':{'version':3}}}
  (out/(self.name+'.kicad_pro')).write_text(json.dumps(pro,indent=2))
  libs=out/'libs';libs.mkdir(exist_ok=True)
  (libs/(self.name+'.kicad_sym')).write_text('(kicad_symbol_lib (version 20241209) (generator "skyrelief_reference_builder") '+''.join(v.replace('SkyRelief:','') for v in self.libs.values())+')',encoding='utf8')
def top(s):
 s.text(DISC,12,14,1.35)
 s.text('Source-supported components and connectivity are distinguished from new reference implementations.',12,20,1.1)
 s.text('Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records',12,25,1.1)
 s.text('or electrically validated flight instructions.',12,30,1.1)
s=Sheet('delivery_historical_power','Layer 1 / Delivery historical power groups')
top(s)
s.text('SOURCE-DERIVED from authored pld_cd_1.jpg: C01-C03 only. Logical labels are not connector contacts.',12,40)
bat=s.module('BT1','3S / 11.1 V nominal',45,65,[],['POS','RET'])
pdb=s.module('U1','PDB role',145,65,['IN_POS','IN_RET'],['OUT_POS','OUT_RET'])
for p,n,side in [(bat['POS'],'H_BAT_POS','R'),(bat['RET'],'H_BAT_RET','R'),(pdb['IN_POS'],'H_BAT_POS','L'),(pdb['IN_RET'],'H_BAT_RET','L'),(pdb['OUT_POS'],'H_ESC_POS','R'),(pdb['OUT_RET'],'H_ESC_RET','R')]:s.wirelabel(p,n,side)
for i,(x,y) in enumerate([(95,100),(95,123),(95,146),(95,169)],1):
 esc=s.module('U'+str(i+1),f'ESC{i} / 30 A label',x,y,['DC_POS','DC_RET'],['PH_A','PH_B','PH_C'])
 for pn,net in [('DC_POS','H_ESC_POS'),('DC_RET','H_ESC_RET')]:s.wirelabel(esc[pn],net,'L')
 # phase groups are labelled; motor symbol contains 3 functional roles.
 motor=s.module('M'+str(i),f'Motor{i} / 920 KV',235,y,['A','B','C'],[])
 for a,b in zip(['PH_A','PH_B','PH_C'],['A','B','C']):
  net=f'H_M{i}_{b}';s.wirelabel(esc[a],net,'R');s.wirelabel(motor[b],net,'L')
s.text('C04-C13 NOT WIRED: controller outputs, power module insertion, peripherals, range and servo.',12,190,1.05)
s.text('No motor location/order/phase sequence, exact polarity mating view or measured current is recovered.',12,196,1.05)
s.save()
s=Sheet('delivery_reference','Layer 2 / NEW servo bench interface abstraction')
top(s)
s.text(WARN,12,39,1.35)
s.text('Do not connect a battery, power a servo rail, arm propulsion or fly an aircraft using this drawing',12,45,1.1)
s.text('without independent hardware-specific electrical and firmware verification.',12,50,1.1)
s.text('REFERENCE IMPLEMENTATION - NOT THE HISTORICAL SKYRELIEF AS-BUILT WIRING.',12,57,1.2)
ps=s.module('U1','External regulated 4.8 V',55,90,[],['SUPPLY','RETURN'],{'SUPPLY':'power_out','RETURN':'power_out'})
sig=s.module('U2','External PWM source',55,132,[],['COMMAND','RETURN'],{'COMMAND':'output','RETURN':'passive'})
sv=s.module('U3','Servo role / PIN_UNVERIFIED',220,108,['SUPPLY','COMMAND','RETURN'],[],{'SUPPLY':'power_in','COMMAND':'input','RETURN':'power_in'})
for p,n,side in [(ps['SUPPLY'],'REF_4V8','R'),(ps['RETURN'],'REF_RETURN','R'),(sig['COMMAND'],'REF_COMMAND','R'),(sig['RETURN'],'REF_RETURN','R'),(sv['SUPPLY'],'REF_4V8','L'),(sv['COMMAND'],'REF_COMMAND','L'),(sv['RETURN'],'REF_RETURN','L')]:s.wirelabel(p,n,side)
s.text('NEW chosen source domain; not historical UBEC or Pixhawk rail. No connection to Pixhawk POWER.',12,158)
s.text('Role terminal numbers are not servo lead order. Actual polarity, logic levels, supply current/transients,',12,165)
s.text('PWM endpoints, device authenticity and mechanical travel remain unverified. No physical-use approval.',12,172)
s.text('References: TowerPro MG90S operating-voltage entry; ArduPilot Pixhawk powering / servo gripper guidance.',12,181,1)
s.save()
s=Sheet('scout_reference','Layer 1 / Scout logical boundaries - PIN_UNVERIFIED')
top(s)
s.text('SOURCE-DERIVED logical block schematic. All open ports are intentional unresolved evidence boundaries.',12,40)
s.text('Generic JHEMCU vendor graphic is not the installed GHF411/R81 harness and is not reproduced.',12,47)
s.module('BT1','Battery / cells UNKNOWN',55,85,[],['POWER_UNVERIFIED','RETURN_UNVERIFIED'])
s.module('U1','GHF411 PRO-BMI family',150,110,['BATTERY','RC_INPUT'],['MOTOR_GROUPS','VIDEO_BOUNDARY'])
s.module('M1','4 x Gremlin 1104 5400 KV',243,85,['PHASES_UNVERIFIED'],[])
s.module('U2','R81 / protocol UNKNOWN',55,144,[],['OUTPUT_UNVERIFIED'])
s.module('U3','FPV / model UNKNOWN',243,144,['SUPPLY_UNVERIFIED'],[])
s.text('NO WIRES: C14-C18 roles are documented; no physical pins, voltage, pad order or protocol recovered.',12,176)
s.text('Native ERC open-port findings are retained. No power flags or no-connect markers conceal missing harness.',12,183,1.05)
s.save()
print('Created three native KiCad sources/projects')

out=R/'kicad';libparts=[]
for p in sorted((out/'libs').glob('*.kicad_sym')):
 if p.name=='SkyRelief.kicad_sym':continue
 t=p.read_text(encoding='utf8');libparts.append(t[t.index('(symbol '):].rsplit(')',1)[0])
 p.unlink()
(out/'libs/SkyRelief.kicad_sym').write_text('(kicad_symbol_lib (version 20241209) (generator "skyrelief_reference_builder") '+''.join(libparts)+')',encoding='utf8')
(out/'sym-lib-table').write_text('(sym_lib_table (version 7) (lib (name "SkyRelief")(type "KiCad")(uri "'+'$'+'{KIPRJMOD}/libs/SkyRelief.kicad_sym")(options "")(descr "Original logical role symbols; not physical pin maps")))',encoding='utf8')


