"""Offline compatibility review; never writes parameters or talks to hardware.
SPDX-License-Identifier: LicenseRef-Pending-Approval
"""
import argparse,json,sys
from pathlib import Path
REQUIRED=['board_revision','firmware_target','firmware_version','battery_cell_count','receiver_protocol','motor_order','servo_supply_source','servo_return_path','servo_output_assignment','servo_logic_levels','servo_endpoints_review','failsafe_review']
def evaluate(record):
 missing=[k for k in REQUIRED if record.get(k) in (None,'','UNKNOWN','PIN_UNVERIFIED')]
 return {'status':'INCOMPLETE - not suitable for hardware use' if missing else 'DECLARATION COMPLETE - hardware-specific independent review still required','missing_fields':missing,'physical_validation':False,'configuration_generated':False}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('record',type=Path);args=a.parse_args()
 r=evaluate(json.loads(args.record.read_text(encoding='utf8')));print(json.dumps(r,indent=2));sys.exit(2 if r['missing_fields'] else 0)

