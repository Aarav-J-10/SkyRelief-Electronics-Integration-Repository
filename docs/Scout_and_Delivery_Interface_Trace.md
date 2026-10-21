# Interface trace: every drawn connection to its source

Each connection in the diagrams and KiCad projects is traced to the record it comes from. Status vocabulary: **VERIFIED** (physically confirmed; none qualify), **DOCUMENTED LOGICAL** (stated in a historical record, no pin-level detail), **UNVERIFIED** (role plausible, detail missing), **REFERENCE ONLY** (new design). Full table: [`Pin_and_Connector_Register.csv`](Pin_and_Connector_Register.csv).

| ID | Connection | Drawn in | Primary source | Status |
|---|---|---|---|---|
| C01 | Pack → PDB | E-HIST-PWR `H_BAT_*` | Sketch `pld_cd_1.jpg` upper-left; component list | DOCUMENTED LOGICAL |
| C02 | PDB → 4 ESCs | E-HIST-PWR `H_ESC_*` | Sketch; Vivo Ignite step 1 | DOCUMENTED LOGICAL |
| C03 | ESC → motor phases | E-HIST-PWR `H_Mn_A/B/C` | Sketch; Vivo Ignite step 8 | DOCUMENTED LOGICAL |
| C04 | ESC signal → Pixhawk OUT1–OUT4 | Functional diagram | Vivo Ignite step 8 (new evidence in this revision) | DOCUMENTED LOGICAL; order unknown |
| C05 | Power module → `POWER` | Functional diagram | Sketch label; Vivo Ignite step 6 | DOCUMENTED LOGICAL |
| C06 | GPS/compass → Pixhawk | Functional diagram | Sketch GPS/I2C; photo `pld10` | DOCUMENTED LOGICAL |
| C07 | Telemetry → `TELEM` | Functional diagram | Sketch; photo `pld13` | DOCUMENTED LOGICAL |
| C08 | FS-iA6B → `RC IN` | Functional diagram | Sketch; photo `pld2` | DOCUMENTED LOGICAL |
| C09–C10 | Safety switch, buzzer | Functional diagram | Sketch; Vivo Ignite step 4 | DOCUMENTED LOGICAL |
| C11 | UBEC → FPV | Functional diagram | Sketch; Vivo Ignite step 5 | DOCUMENTED LOGICAL |
| C12 | Release servo signal/supply/return | Dashed (unresolved) | Sketch shows three lines near an I2C label; photo `pld20` | UNVERIFIED |
| C13 | Range/LiDAR → Pixhawk `TELEM` | Functional diagram | Vivo Ignite step 9 (new evidence in this revision) | DOCUMENTED LOGICAL; model unknown |
| C14 | Scout pack → AIO | E-REF-SCOUT open pins | Vivo Ignite scout step 9 (XT30, 2–4S); methodology (1100 mAh) | DOCUMENTED LOGICAL; cells unknown |
| C15 | AIO → motors | E-REF-SCOUT open pins | Vivo Ignite scout step 3 | DOCUMENTED LOGICAL |
| C16 | R81 → AIO | E-REF-SCOUT open pins | Vivo Ignite scout step 4 | UNVERIFIED |
| C17 | Scout FPV supply | E-REF-SCOUT open pins | Vivo Ignite scout step 6 | UNVERIFIED |
| C18 | Detection/ranging → decision | Not drawn as a wire | Author clarification; algorithm prose | UNVERIFIED |
| R1–R3 | Bench servo supply, command, return | E-REF-SERVO | New design | REFERENCE ONLY |

The JHEMCU illustration in the archive is a generic manufacturer guide, not the installed scout harness; it is excluded and not traced.
