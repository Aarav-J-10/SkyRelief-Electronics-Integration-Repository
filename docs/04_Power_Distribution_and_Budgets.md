# Power domains and budgets

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

| Domain | Documentary value | Limit |
|---|---|---|
| Delivery pack | 3S, 11.1 V, 2200 mAh, 40C label | 24.42 Wh nominal, no usable-energy measurement |
| ESCs | Four 30 A labels | No operating-current/thermal trace |
| Controller POWER | Power-module role | Exact output, path and calibration unknown |
| FPV UBEC | 5 V / 3 A label | Loaded setpoint, noise and camera demand unknown |
| Historical servo | Signal/supply/return unknown | Never infer from POWER or I2C proximity |
| Scout pack | About 1100 mAh | Cells/voltage/discharge spec unknown |
| New bench reference | External regulated 4.8 V role | Supply current/transients unqualified |

No measured profiles justify a complete current or energy budget. 40C x 2.2 Ah is not a measured sustainable current. No fuse, regulator, MOSFET or reverse-polarity device is inserted into the historical harness. Any protective redesign requires exact parts and its own qualification. See [domain map](../diagrams/delivery_power_domains.svg).
