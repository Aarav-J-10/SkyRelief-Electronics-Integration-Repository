# SkyRelief / Electronics and integration

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

Version **0.1.0-review**, created 20 October 2026. Historical source: [project archive](https://github.com/Shadowfax0707/project-ap-DDPDS_2024_1729-0707), main at **42f9a44600351ec6d0a57fb20756c547acf38cad**. All 49 source files freshly fetched and Git-blob verified; **13 author-attributed originals included here**. See [source manifest](data/source_manifest.csv).

**Review package: specific public reuse licences pending.** Five historical STEP models and external artwork are excluded. Read [licences](LICENSES.md), [known limitations](Known_Limitations.md), [exclusions](docs/EXCLUDED_THIRD_PARTY_CAD.md) and [issue matrix](data/issue_matrix.csv).

## Quick start
1. Read the [overview](docs/01_Electrical_System_Overview.md), [source register](docs/Source_Document_Register.md), [photo map](docs/Photo_Map.md) and [BOM interpretation](bom/README.md).
2. Open kicad/delivery_reference.kicad_pro in KiCad 9.0.7. Historical power grouping and scout logical boundaries are separate native projects. Run: python scripts/run_native_checks.py --cli kicad-cli
3. Run **python scripts/verify_electronics_repository.py** from the repository root (Python 3.11+; standard library). Review [file results](verification/repository_checks.json).
4. Read [verification details](docs/13_Verification_and_ERC_Results.md) before using any result.

## Evidence and design scope
- Historical evidence: component lists, original photographs, entered ODS and illustrative estimate plus authored wiring sketch. They do not establish installed settings.
- Source-derived: functional diagrams, BOM/connection crosswalks and numerical audit facts.
- New reference: external 4.8 V / PWM / common-return servo abstraction, never a Pixhawk physical pin map.
- Missing: actual CAD permissions, complete latch/harness, firmware/parameters, logs and deployed perception source. No fully reproducible autonomous replica is supplied.

## Documents
- [Electrical evidence layers](docs/01_Electrical_System_Overview.md)
- [Delivery architecture](docs/02_Delivery_UAV_Architecture.md)
- [Scout architecture](docs/03_Scout_UAV_Architecture.md)
- [Power domains and budgets](docs/04_Power_Distribution_and_Budgets.md)
- [Pixhawk and peripherals](docs/05_Pixhawk_and_Peripheral_Interfaces.md)
- [Scout AIO and receiver](docs/06_Scout_AIO_and_Receiver_Interfaces.md)
- [Servo rail and release control](docs/07_Servo_Rail_and_Release_Control.md)
- [Ranging and vision boundaries](docs/08_Ranging_and_Vision_Boundaries.md)
- [Reference review and bring-up guide](docs/09_Reference_Implementation_Guide.md)
- [Firmware status](docs/10_Firmware_and_Configuration_Status.md)
- [Source provenance and rights](docs/11_Source_Provenance_and_Rights.md)
- [Assumptions and unknowns](docs/12_Design_Assumptions_and_Unknowns.md)
- [Native and file verification](docs/13_Verification_and_ERC_Results.md)
- [Manuscript artifact map](docs/14_Manuscript_Figure_and_Table_Map.md)

## Authors and citation
[CITATION.cff](CITATION.cff) identifies Aarav Jalan (Adani International School, Ahmedabad) and Abhinav Patro (SSRVM, Ahmedabad). This engineering reconstruction is for their review, not an already published release or DOI. See [contribution rules](CONTRIBUTING.md).

No new physical experiments, flight qualification, certification or journal submission-readiness determination is claimed.
