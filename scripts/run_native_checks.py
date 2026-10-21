"""Native KiCad checks.
SPDX-FileCopyrightText: 2026 Aarav Jalan and Abhinav Patro
SPDX-License-Identifier: MIT
"""
import argparse,json,subprocess,collections
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--cli',default='kicad-cli');args=a.parse_args()
root=Path(__file__).resolve().parents[1];out=root/'verification';out.mkdir(exist_ok=True)
def call(cmd):
 r=subprocess.run([args.cli]+cmd,cwd=root,encoding='utf8',errors='replace',capture_output=True)
 return {'command':['kicad-cli']+cmd,'exit_code':r.returncode,'stdout':r.stdout.replace(str(root),'.'),'stderr':r.stderr.replace(str(root),'.')}
version=call(['version']);report={'tool_version':version['stdout'].strip(),'tool_version_exit':version['exit_code'],'physical_test':False,'projects':[]}
for source in sorted((root/'kicad').glob('*.kicad_sch')):
 name=source.stem;f=source.relative_to(root).as_posix()
 erc=call(['sch','erc','--format','json','--units','mm','--exit-code-violations','-o','verification/'+name+'_erc.json',f])
 svg=call(['sch','export','svg','--black-and-white','--exclude-drawing-sheet','-o','kicad/exports/'+name+'/',f])
 pdf=call(['sch','export','pdf','--black-and-white','--exclude-drawing-sheet','--exclude-pdf-metadata','-o','kicad/exports/'+name+'.pdf',f])
 net=call(['sch','export','netlist','--format','kicadxml','-o','kicad/exports/'+name+'.net',f])
 netpath=root/'kicad/exports'/(name+'.net')
 if netpath.exists():
  text=netpath.read_text(encoding='utf8').replace(str(root),'.').replace(root.as_posix(),'.')
  netpath.write_text(text,encoding='utf8')
 ercfile=out/(name+'_erc.json')
 if ercfile.exists():
  data=json.loads(ercfile.read_text());viol=[v for sheet in data['sheets'] for v in sheet['violations']]
  counts=dict(collections.Counter(v['type'] for v in viol));severities=dict(collections.Counter(v['severity'] for v in viol))
 else:counts={'REPORT_MISSING':1};severities={}
 report['projects'].append(dict(project=name,erc=erc,violations_by_type=counts,severities=severities,svg=svg,pdf=pdf,netlist=net))
(out/'native_kicad_checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if any(x[k]['exit_code'] for x in report['projects'] for k in ['svg','pdf','netlist']):raise SystemExit(1)

