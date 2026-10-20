# Reference review and bring-up guide

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

Open delivery_reference.kicad_pro in KiCad 9.0.7. It is a native editable role schematic: external supply -> servo supply, external PWM -> command, shared return. Terminal identifiers are logical roles excluded from PCB design, never actual servo lead order.

Before physical construction, identify the exact device/datasheet and polarity in mating view; select supply for verified stall/transient demand; establish logic levels; review positive-rail isolation and returns; choose suitable protection from real component specifications. No complete supply or PCB is selected here.

For any later independent bench work remove propellers, isolate batteries, restrain the mechanism, use an appropriate current-limited initial supply and inspect connector polarity/return before power. Check mechanical clearance, unintended motion, power loss, EMI and failsafe responsibility. Record results in new documentation. These are future recommended checks, not tests claimed completed. No arm, flight or servo-sweep script is supplied.
