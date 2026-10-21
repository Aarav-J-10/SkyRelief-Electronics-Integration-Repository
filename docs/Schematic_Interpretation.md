# Reading the three KiCad projects

All three are native KiCad 9 projects (`.kicad_pro` + `.kicad_sch`) using project-local symbols in `kicad/libs/SkyRelief.kicad_sym`. They open on a clean KiCad 9 install with no external libraries. They are **functional interface drawings**, not buildable circuit schematics: each symbol is a rectangular role block whose pins name a function (for example `PH_A`, `DC_POS`, `COMMAND`), not a physical pad, connector pin or wire colour. No footprint or PCB is defined.

| ID | Project | What it is | Evidence class | ERC (KiCad 9.0.9) |
|---|---|---|---|---|
| E-HIST-PWR | `delivery_historical_power` | Delivery propulsion power: 3S pack → PDB → four ESCs → four three-phase motors | `H2` source-derived from the A. Patro wiring sketch (`assets/original_wiring_reference/pld_cd_1.jpg`) and component list | 0 violations |
| E-REF-SERVO | `delivery_reference` | New bench interface for a release servo: external 4.8 V supply, external PWM source, common return | `N` new reference; **not** the historical servo wiring | 0 violations |
| E-REF-SCOUT | `scout_reference` | Scout boundary blocks: pack, GHF411 AIO, motor group, R81, FPV | `H2` blocks with `U` connections | 9 × `pin_not_connected` (intentional) |

## E-HIST-PWR — what is known and what is not

Sixteen nets: pack positive and return to the PDB (`H_BAT_POS`, `H_BAT_RET`), a common ESC supply pair (`H_ESC_POS`, `H_ESC_RET`), and three phase nets per motor (`H_M1_A` … `H_M4_C`). The sketch shows exactly this topology, and the Vivo Ignite build text says the four ESCs and the power module were soldered to the PDB.

Not shown, on purpose: the power module's position in the high-current path (the sketch does not settle it), the UBEC/FPV branch, ESC signal leads to Pixhawk outputs, fuses, connectors and wire gauge. Phase letters A/B/C are labels, not wire colours: swapping any two reverses a motor, and the actual sequence was set by propeller-free testing that left no record.

## E-REF-SERVO — a new design, not a recovery

The historical servo's signal source, supply and return were never recorded. This sheet proposes a safe bench arrangement: a separately regulated 4.8 V supply, a PWM command from any bench source, and one shared return. It deliberately **does not** connect to a Pixhawk. On Pixhawk-family boards, powering the `POWER` port does not by itself energise the servo rail ([ArduPilot: Powering the Pixhawk](https://ardupilot.org/copter/docs/common-powering-the-pixhawk.html)). Terminal numbers 1–3 are role numbers, not servo lead order; the servo's own datasheet governs lead order, voltage range and current.

## E-REF-SCOUT — why nine errors stay

Every scout connection the records describe (pack to AIO, AIO to motors, R81 to AIO, FPV supply) lacks the pad, protocol, voltage or cell count needed to draw a wire honestly. Each open pin therefore stays open and KiCad reports it. See the per-pin [scout ERC register](Scout_ERC_Unresolved_Register.md) for what would resolve each one. Adding `no_connect` markers or guessed wires would make ERC pass and the drawing wrong.

## Regenerating and checking

```bash
python scripts/build_schematics.py               # regenerates the three .kicad_sch files from source tables
python scripts/run_native_checks.py --cli kicad-cli  # ERC JSON, SVG, PDF, netlist for each project
python scripts/verify_electronics_repository.py  # file, hash, link and report checks
```

On 2026-10-20 the native checks were re-run with KiCad 9.0.9 (Ubuntu 24.04, KiCad PPA). Net-level connectivity in all three netlists was identical to the committed 9.0.7 exports; only the tool version, date and path separators changed.
