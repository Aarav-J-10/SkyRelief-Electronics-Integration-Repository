# Servo rail and release control

**Historical SkyRelief hardware dossier with modern engineering reconstruction.** Source-supported components and connectivity are distinguished from new reference implementations. Unrecovered pin assignments, firmware parameters and code must not be treated as as-built records or electrically validated flight instructions.

The historical servo signal, positive supply and return are unrecovered. Three conductors near an I2C label do not establish an I2C servo. MG90S photo marking versus Tower Pro 9g sketch wording does not prove the same exact authentic device.

Official Pixhawk guidance states POWER does not inherently supply the servo output rail. Separate supply/common-reference wiring is a possible architecture, not installed evidence.

The new delivery_reference sheet uses external regulated 4.8 V, external PWM source and common return roles. It selects no Pixhawk output and makes no positive connection to its POWER or rail. TowerPro's official operating-voltage entry does not establish stall current, lead order, logic amplitude or endpoints for the photographed device. These block physical use. No supply-current rating, fuse value, torque, pulse widths or linkage travel is guessed.
