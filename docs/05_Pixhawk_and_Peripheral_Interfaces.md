# Pixhawk and peripherals

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

The sketch labels POWER, TELEM, RC IN, GPS, I2C and MAIN OUT around a Pixhawk 2.4.8-family controller. Labels show intended roles, not mating-view contact numbers. Photographed cables do not prove continuity.

Identify the actual board revision before using a pinout; document connector, mating view, voltage, direction and return. The power-module role does not recover sensing calibration or battery insertion. GPS/compass C06 does not allocate a compass bus or orientation; telemetry C07 has no recovered baud; RC C08 has no established installed PPM/SBUS/iBUS harness. Safety/buzzer C09/C10 remain type/pinout unknown. The interface register therefore retains PIN_UNVERIFIED.

See the [peripheral role crosswalk](../diagrams/delivery_peripheral_interfaces.svg). Arrows are roles, never contact-level nets; the FPV power branch is isolated from the controller box.
