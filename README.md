# SkyRelief — electronics and integration

Supplement **S2** to the manuscript *SkyRelief: A Human-Supervised Dual-UAV Delivery Prototype with Mission-Architecture Analysis* (A. Jalan, A. Patro; candidate for MDPI *Hardware*, not yet submitted). Mechanical hardware is in the companion repository, [Skyrelief-Hardware-Repo](https://github.com/Aarav-J-10/Skyrelief-Hardware-Repo) (S1).

**What this repository gives you.** Three native KiCad 9 projects describing the SkyRelief electrical architecture at the level the records support, with reproducible ERC, exports and netlists; a register tracing every drawn connection to its source; parts and cost records; and the original A. Patro wiring sketch.

**What it does not give you.** An installed harness, pin map, firmware configuration or release-command mapping. None survived. The KiCad sheets are **functional interface drawings** (role blocks), not buildable circuit schematics.

| Project | ID | Meaning | ERC (KiCad 9.0.9) |
|---|---|---|---|
| [`delivery_historical_power`](kicad/delivery_historical_power.kicad_sch) | E-HIST-PWR | Pack → PDB → 4 ESCs → 4 three-phase motors, from the historical sketch | 0 |
| [`delivery_reference`](kicad/delivery_reference.kicad_sch) | E-REF-SERVO | **New** bench servo interface: external 4.8 V, external PWM, common return | 0 |
| [`scout_reference`](kicad/scout_reference.kicad_sch) | E-REF-SCOUT | Scout blocks with nine deliberately open pins | 9 × `pin_not_connected` |

<img src="assets/original_wiring_reference/pld_cd_1.jpg" width="260" alt="Original delivery wiring sketch by Abhinav Patro"> &nbsp; Exports: [PDF](kicad/exports/) · [SVG](kicad/exports/) · [netlists](kicad/exports/)

## Reproduce in 5 minutes

```bash
git clone https://github.com/Aarav-J-10/SkyRelief-Electronics-Integration-Repository && cd SkyRelief-Electronics-Integration-Repository
python scripts/verify_electronics_repository.py      # Python 3.11+, standard library: files, hashes, links, quotes, ERC reports
python scripts/build_schematics.py                   # regenerates the three .kicad_sch byte-identically
python scripts/run_native_checks.py --cli kicad-cli  # needs KiCad 9: ERC JSON, PDF, SVG, netlist
python scripts/release_gate.py                       # rights screen of the tree and Git history
```

Expected ERC: 0 / 0 / 9. CI runs the same steps, including KiCad in the official `kicad/kicad:9.0` container ([workflow](.github/workflows/verify.yml)).

## Contents

| Area | Start here |
|---|---|
| Reading the schematics | [Schematic interpretation](docs/Schematic_Interpretation.md) · [Scout ERC register](docs/Scout_ERC_Unresolved_Register.md) |
| Connections | [Interface trace](docs/Scout_and_Delivery_Interface_Trace.md) · [`Pin_and_Connector_Register.csv`](docs/Pin_and_Connector_Register.csv) |
| Power | [Power domain analysis](docs/Power_Domain_Analysis.md) · [Servo rail and release](docs/07_Servo_Rail_and_Release_Control.md) |
| Firmware and software | [Configuration boundary](docs/Flight_Control_Configuration_Boundary.md) · [`Configuration_Matrix.csv`](docs/Configuration_Matrix.csv) · [Software provenance](docs/Software_and_Algorithm_Provenance.md) |
| Safety | [Electronics safety and qualification](docs/Electronics_Safety_and_Qualification.md) |
| Parts and cost | [`bom/`](bom/) (delivery and scout BOMs, 34-entry crosswalk, 20 dated quotes) |
| Verification | [Native and file verification](docs/13_Verification_and_ERC_Results.md) · [`verification/`](verification/) |
| Rights and release | [`LICENSE_MATRIX.csv`](LICENSE_MATRIX.csv) · [Publication gate](PUBLICATION_GATE.md) · [Release lock](PUBLICATION_RELEASE_LOCK.json) · [Release notes](RELEASE_NOTES.md) |

## Status and licence

Release candidate **0.2.0-rc1**, untagged. **No reuse licence has been granted yet** ([decision sheet](AUTHORS_LICENSING_APPROVAL_REQUIRED.md), [LICENSES.md](LICENSES.md)). No electrical, servo or flight test was performed for this release. Do not power or fly anything from these drawings without independent, hardware-specific verification.

Cite with [CITATION.cff](CITATION.cff). Historical source archive: [Shadowfax0707/project-ap-DDPDS_2024_1729-0707](https://github.com/Shadowfax0707/project-ap-DDPDS_2024_1729-0707) at `42f9a44600351ec6d0a57fb20756c547acf38cad`.
