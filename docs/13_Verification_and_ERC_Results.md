# Native and file verification

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

KiCad 9.0.7 genuinely loaded and exported all three native projects to SVG/PDF/netlist. The historical power grouping and new bench abstraction returned ERC 0 with zero violations. Scout returned ERC exit 5 with nine pin_not_connected errors, retained as unresolved logical boundaries. No no-connect markers or power flags hide them.

See [exact native commands/results](../verification/native_kicad_checks.json), [file checks](../verification/repository_checks.json) and per-project ERC JSON. Native sources use embedded original symbols plus a project-local library table. Module symbols carry logical role terminals and are excluded from PCB placement.

The file validator checks SHA-256, exact-case local links, UTF-8 CSVs/quote math, XML and exclusions. The offline compatibility check is run against an incomplete fixture and is expected to reject it. There was no physical electrical, servo or flight test.

## Re-run on 2026-10-20 (KiCad 9.0.9)

KiCad 9.0.9 (Ubuntu 24.04, official KiCad PPA) re-ran ERC and exports for all three projects. Results are unchanged: `delivery_historical_power` 0, `delivery_reference` 0, `scout_reference` 9 × `pin_not_connected` (exit code 5). Net-level connectivity in all three netlists is identical to the 9.0.7 exports (16, 3 and 9 nets); only tool version, date and path separators differ. `scripts/build_schematics.py` regenerates the three `.kicad_sch` files and the symbol library byte-identically apart from line endings. Per-pin dispositions are in the [scout ERC register](Scout_ERC_Unresolved_Register.md).
