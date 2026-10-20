# Electronics safety and qualification boundary

Nothing in this repository has been electrically tested, and nothing is certified. These are the checks a future builder must perform; none was performed for this release.

## Bench sequence (propellers removed throughout)

1. **Inspect** every joint and connector; confirm polarity marks against the component datasheets, not against these drawings.
2. **Continuity and isolation** with the pack disconnected: pack positive to frame, positive to return, each ESC input.
3. **First power through a current-limited bench supply** set at the pack's nominal voltage and a low current limit, before ever connecting a LiPo.
4. **Measure regulated outputs** (UBEC, controller `POWER`, any servo supply) open-circuit and under a dummy load.
5. **Controller checks**: pre-arm checks pass, RC failsafe triggers as configured, safety switch inhibits arming.
6. **Motor direction** one at a time at low command, propellers off.
7. **Release servo on its own supply** (E-REF-SERVO arrangement), dummy load, hands clear. Confirm the release is inhibited by default and only moves on a deliberate command.

## Hazards

LiPo fire (charge in a fire-safe container; never puncture or over-discharge), arcing on connection, unintended arming, unexpected servo motion, RF exposure from telemetry and VTX, and regulator back-feed.

## Out of scope

No auto-arm, mission or release script is provided. No airspace permission, field operation or crowd-area release is implied. Flight with any configuration derived from these documents is a new, untested aircraft and is the builder's responsibility.
