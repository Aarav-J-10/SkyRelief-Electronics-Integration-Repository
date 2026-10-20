# Electrical evidence layers

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

Layer 1 is source-derived historical function: the authored sketch supports module roles and propulsion groups. Layer 2 is a new external-supply servo bench abstraction. Layer 3 records missing physical pins/configuration. Logical terminal identifiers are never connector contact numbers.

Native projects are delivery_historical_power, delivery_reference and scout_reference. They are schematic-only sources excluded from PCB placement. ERC checks drawn connectivity and pin types; it cannot identify the installed board or validate omitted harness details. [Connection ledger](../data/documented_connections.csv) and [interface register](../bom/interface_and_connector_register.csv) define the evidence scope.
