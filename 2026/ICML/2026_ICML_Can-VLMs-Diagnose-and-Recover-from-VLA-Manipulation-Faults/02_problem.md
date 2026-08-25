# Problem — Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Evidence maturity: `CURATION_ONLY`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2026 / ICML 2026 regular
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, failure diagnosis, recovery, Benchmark, LIBERO, real robot
- Official paper: https://kakigo.github.io/VLA-FixBench/
- Code/Project: https://kakigo.github.io/VLA-FixBench/
- Source audit: metadata registration only; full-text claims are UNVERIFIED.

## Target Problem and Assumptions

UNVERIFIED — 문제 formulation, bottleneck과 핵심 가정을 full text에서 확인한다.

## Closed-Loop Position

`observation → state/world model → task & motion decision → policy/control → contact → feedback/recovery` 중 위치를 정독 후 기록한다.
