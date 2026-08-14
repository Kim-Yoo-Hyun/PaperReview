# Method — Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring
- Official paper: https://www.roboticsproceedings.org/rss21/p073.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p073.pdf
- Code/Project: https://cxu-tri.github.io/FAIL-Detect-Website/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- Policy input/output을 failure와 상관된 scalar signal로 distill한다.
- Sequential OOD detection으로 failure onset을 찾는다.
- Conformal prediction으로 uncertainty를 calibration하고 learned flow-based density signal도 비교한다.

## Interface

기존 imitation policy를 바꾸지 않는 modular runtime monitor이며 출력은 시간별 failure score와 alarm이다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `Policy uncertainty / OOD detection → FAIL-Detect / SAFE → typed recovery`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
