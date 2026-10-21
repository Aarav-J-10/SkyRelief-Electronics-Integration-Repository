# Power domains

No current, voltage or ripple was measured on either aircraft, and none is claimed. This page separates the domains so that a rebuild knows what it must check.

## Delivery UAV

| Domain | Source → loads | Recorded labels | Open questions | Check before energising (propellers off) |
|---|---|---|---|---|
| Flight pack / high current | 3S LiPo → PDB → 4 ESCs | 11.1 V, 2200 mAh, 40C (24.42 Wh nominal = voltage × capacity, not usable energy) | Connector, wire gauge, fuse or none, inrush limiting | Polarity at PDB, continuity, insulation, no short pack-to-frame |
| ESC / motor | PDB → ESC → three-phase motor | 30 A ESC label, 920 KV motors | ESC firmware and rating under the fitted prop | Propeller-free direction test per motor |
| Flight-controller supply | Pack → power module → Pixhawk `POWER` | Power module listed (24 g) | Where the module sits in the high-current path; voltage/current sense calibration | Measured `POWER` voltage within the board's datasheet range |
| Servo rail | **Unrecorded** | — | Whether any supply reached the servo, from where | Do not infer from `POWER`; on Pixhawk-family boards `POWER` does not energise the servo rail ([ArduPilot](https://ardupilot.org/copter/docs/common-powering-the-pixhawk.html)) |
| FPV | PDB → UBEC → Caddx-labelled camera/VTX | UBEC 5 V / 3 A label | Camera/VTX model and current | UBEC output measured open-circuit and under a dummy load |
| Ground / return | Shared through PDB | — | Star point, return path for servo and FPV | Continuity between all intended returns |

## Scout UAV

| Domain | Source → loads | Recorded labels | Open questions |
|---|---|---|---|
| Flight pack | Pack → XT30 → GHF411 AIO | 1100 mAh; "2–4S" in build text | Cell count actually flown |
| ESC / motor | AIO ESC → 4 × 1104 5400 KV | 40 A AIO label | Motor order, rotation |
| FPV | AIO or separate 5 V regulator → camera/VTX | "5 V BEC or UBEC" | Which source, VTX model |

## E-REF-SERVO (new bench reference)

A separately regulated 4.8 V source powers the servo; a bench PWM source commands it; both share one return. The supply must be sized from the **selected** servo's datasheet stall current with margin, and current-limited on the bench. No value is given here because none was measured or verified for the photographed servo.

## Hazards to design for

LiPo short circuit and puncture, inrush sparking at connection, brownout of the controller when the servo stalls on a shared supply, back-feeding when two regulators are paralleled, and reversed polarity at XT30/XT60 adapters. None of these was characterised for SkyRelief.
