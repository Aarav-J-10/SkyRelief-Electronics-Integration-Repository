# Flight-control configuration boundary

**No historical configuration was recovered.** There is no ArduPilot parameter file, Mission Planner mission, Betaflight `diff`/`dump`, flight log or release-trigger definition in the 49-file archive or the author-supplied reports. This repository does not provide a substitute, because a plausible-looking parameter file would be read as the 2024–2025 settings.

## Known

| Aircraft | Controller | Firmware family | Tooling | Source |
|---|---|---|---|---|
| Delivery UAV | Pixhawk 2.4.8 | ArduPilot (Copter) | Mission Planner: accelerometer, compass, radio and telemetry calibration; "updated firmware" installed | Vivo Ignite build step 7; component list |
| Scout UAV | GHF411 PRO-BMI 40 A F4 AIO | Betaflight | Betaflight Configurator: receiver channels, LiDAR telemetry, OSD; gyro/accelerometer calibration | Vivo Ignite scout steps 10–11 |

## Unknown (each is needed to reproduce operation)

Firmware versions and board targets; frame class and motor order; ESC protocol; receiver protocol and channel map; flight modes and switch assignments; failsafe actions for RC, telemetry, GPS and battery; battery monitor calibration; geofence; mission files; the servo output and the command that released the payload (RC switch, mission item or other); the range sensor's driver and avoidance settings.

The full role-by-role list is in [`Configuration_Matrix.csv`](Configuration_Matrix.csv); every field the records do not supply reads `UNKNOWN`.

## If you configure a new aircraft from these documents

You are building a new aircraft, not reproducing SkyRelief. Identify the exact board revision first, use the current official setup guides ([ArduPilot Copter](https://ardupilot.org/copter/), [Betaflight](https://betaflight.com/docs/wiki)), record your own parameter export and version, and treat every safety function (pre-arm checks, failsafes, release inhibit) as untested until you test it.
