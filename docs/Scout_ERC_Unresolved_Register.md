# Scout ERC: the nine unresolved pins

KiCad 9.0.9 reports nine `pin_not_connected` errors on `scout_reference.kicad_sch` (`verification/scout_reference_erc.json`). Each is a real gap in the historical record. None is suppressed.

| # | Symbol / pin | Interface | What the records say | Why no wire is drawn | Likely consequence of guessing | Resolves when |
|---|---|---|---|---|---|---|
| 1 | BT1 pin 1 `POWER_UNVERIFIED` | C14 | 1100 mAh pack (methodology); "2–4S via XT30" (build text) | Cell count never fixed; XT30 polarity not photographed | Wrong voltage on a 2–6S AIO is tolerated, but wrong polarity destroys it | A photo or record of the flown pack label and connector |
| 2 | BT1 pin 2 `RETURN_UNVERIFIED` | C14 | As above | As above | As above | As above |
| 3 | U1 pin 1 `BATTERY` | C14–C17 | GHF411 PRO-BMI is a 2–6S AIO family | Board revision and pad layout unconfirmed | Pad-level drawing could mislead a rebuild | Exact board revision (photo of silkscreen) |
| 4 | U1 pin 2 `RC_INPUT` | C16 | R81 receiver bound to Zorro | Which UART/pad, and the protocol, are unrecorded | Receiver on wrong UART: no control link | Photo of R81 solder joints or a Betaflight `resource` dump |
| 5 | U1 pin 3 `MOTOR_GROUPS` | C15 | Motor leads soldered to AIO ESC pads | Motor order and rotation unrecorded | Wrong order → unstable on arming | Betaflight motor remap or propeller-free test record |
| 6 | U1 pin 4 `VIDEO_BOUNDARY` | C17 | FPV camera/VTX on a 5 V output | Camera/VTX model and the 5 V source unknown | Over-voltage on the VTX | FPV model identification and its supply pad |
| 7 | M1 pin 1 `PHASES_UNVERIFIED` | C15 | Four FT Gremlin 1104 5400 KV | Same as #5; drawn as one grouped block | As #5 | As #5 |
| 8 | U2 pin 1 `OUTPUT_UNVERIFIED` | C16 | R81 receiver | Output protocol (SBUS / CRSF / other) unknown | Protocol mismatch, no link | Receiver firmware/protocol record |
| 9 | U3 pin 1 `SUPPLY_UNVERIFIED` | C17 | FPV assembly powered from 5 V BEC/UBEC | Source pad and current unknown | Brownout or over-voltage | As #6 |

Machine-readable form: [`data/erc_unresolved_crosswalk.csv`](../data/erc_unresolved_crosswalk.csv).
