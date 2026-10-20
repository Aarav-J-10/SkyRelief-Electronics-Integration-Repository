# Assumptions and unknowns

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

Historical motor order, ESC protocol, target/version, receiver interface, compass axes, UART settings, monitor calibration, servo rail/output/return, ranging interface and perception deployment remain absent. Native files cannot recover these facts.

New bench supply/command roles are explicit design assumptions. The historical 5 V UBEC is not assigned to the servo. Scout pack voltage remains unknown. Every physical connector entry is PIN_UNVERIFIED. The [unresolved-net register](../data/unresolved_nets.csv) records consequence and required evidence. Zero ERC in a restricted role abstraction does not make it a hardware-ready replica.
