# Release notes — v1.0.0

**Electronics and integration sources for SkyRelief, Supplement S2** of the manuscript *SkyRelief: A Human-Supervised Dual-UAV Delivery Prototype with Mission-Architecture Analysis* (A. Jalan, A. Patro; candidate for MDPI *Hardware*, not yet submitted). Paired with the same tag in [Skyrelief-Hardware-Repo](https://github.com/Aarav-J-10/Skyrelief-Hardware-Repo); both carry an identical `PUBLICATION_RELEASE_LOCK.json`.

## Licences
CERN-OHL-W-2.0 for hardware design sources, MIT for software, CC-BY-4.0 for documentation, photographs and data, approved by both authors on 21 October 2026. See `LICENSES.md` and `LICENSE_MATRIX.csv`.

## What you can reproduce
- **Three native KiCad 9 projects**: E-HIST-PWR (historical propulsion power topology, ERC 0), E-REF-SERVO (new bench servo interface, ERC 0), E-REF-SCOUT (scout blocks, ERC 9 unconnected pins kept as documented gaps). Schematic sources regenerate byte-identically; netlist connectivity unchanged since 0.1.0.
- File integrity, quote arithmetic, rights screening and cross-repository consistency checks (`scripts/`), all run in CI.

## Scope and limitations
- The KiCad sheets are functional interface drawings (role blocks), not buildable circuit schematics with footprints.
- The historical aircraft cannot be fully reproduced: frame CAD (D01–D05) is third-party and withheld; the latch and harness were never drawn; flight-controller configurations, mission files, the release command and perception code were not recovered.
- 19/20 is a retrospective composite count without a trial register. No new physical test of any kind was performed.

## Tagging (maintainer step)
The release is prepared on `main` but the tag could not be pushed from the preparation session (HTTP 403). From a clone with write access:

```bash
git fetch origin && git checkout main && git pull --ff-only
python scripts/release_gate.py && python scripts/check_release_lock.py --self-test
git tag -a v1.0.0 -m "SkyRelief v1.0.0" origin/main && git push origin v1.0.0
```

Pushing the tag runs `.github/workflows/release.yml`, which repeats the gates and publishes the GitHub release with the archive and SHA-256 files below.

## Integrity
The release workflow attaches `SkyRelief_Electronics_Source_Release_v1.0.0.zip` (built with `git archive` from the tagged commit) and its `.sha256`. Per-file SHA-256 values are in `verification/file_manifest.csv`.
