# Software and algorithm provenance

| Item | What exists | Who | Status |
|---|---|---|---|
| Flight-control firmware | ArduPilot (delivery) and Betaflight (scout), upstream projects | Upstream communities | Used historically; versions and configurations **not recovered** |
| Object detection | YOLO-related development (reports name YOLOv8) | Aarav Jalan (author clarification, 19 Oct 2026) | Development activity reported; code, weights, labels and metrics **not recovered** |
| LiDAR / range sensing | Reported integration on both aircraft | Aarav Jalan (scout, LiDAR); Abhinav Patro (delivery hardware) | Sensor model and driver settings **not recovered** |
| Site-scoring algorithm | Prose: score S = w_f S_f + w_t S_t + w_p S_p, threshold ≈ 0.65, RANSAC ground plane, UDP to ground station | Project documents | **Proposal only**; no executable source; weights and normalisation unspecified |
| Endurance estimate | `evidence/original/Payload_and_Flight_Time_Analysis_Estimate(PLD).py` | Abhinav Patro | Original script; assumed constants (1100 g, 3400 g, 7 min, exponent 1.3); not a flight log |
| Schematic generator, validators | `scripts/*.py` in this repository | New (2026, AI-assisted) | Design automation; not operating software |
| Mission-architecture models | `SkyRelief_Reproducible_Computations.zip` (Supplement S3) | New (2026) | Separate supplement; event-tree, force/energy and trajectory models; **not flight code** |

The reports also mention reinforcement learning for path planning. Nothing executable survives, so it is not described as implemented.

Operationally, the decision to deliver was made by a human watching the scout's FPV feed. That baseline needs no software beyond the flight controllers; automatic terrain acceptance is not a demonstrated function.
