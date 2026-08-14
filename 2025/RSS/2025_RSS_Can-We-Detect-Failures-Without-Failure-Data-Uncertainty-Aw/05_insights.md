# Insights — Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring
- Official paper: https://www.roboticsproceedings.org/rss21/p073.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p073.pdf
- Code/Project: https://cxu-tri.github.io/FAIL-Detect-Website/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Paper-Supported Direction

Known failure data 없이 runtime policy failure를 탐지하는 SAFE 이전/병렬의 직접 비교점.

## Researcher Interpretation

- Foundation/frontier connection: `Policy uncertainty / OOD detection → FAIL-Detect / SAFE → typed recovery`
- 가장 먼저 반박할 가정: 정상 training trajectory만으로 failure와 상관된 epistemic/OOD signal을 학습할 수 있다.
- 현재 gap과 연결할 때 success만 보지 않고 downstream control 또는 evaluation protocol의 변화를 확인한다.

## Limitations / Failure Modes to Audit

- Failure detection이 recovery action 선택까지 해결하지 않는다.
- Conformal guarantee가 sequential distribution shift와 closed-loop intervention 뒤에도 그대로 유지되는지 확인해야 한다.

## Minimum Experiment

성공 trajectory만으로 detector를 calibration한 뒤 occlusion, object displacement, wrong grasp를 삽입해 lead time과 false alarm을 측정한다.

## Status

`UNREAD` — 이 노트는 official abstract 기반의 reading scaffold이며 정독 완료를 의미하지 않는다.
