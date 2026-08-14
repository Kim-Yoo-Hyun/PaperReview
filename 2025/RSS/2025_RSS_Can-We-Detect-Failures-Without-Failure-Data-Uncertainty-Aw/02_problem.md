# Problem — Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring
- Official paper: https://www.roboticsproceedings.org/rss21/p073.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p073.pdf
- Code/Project: https://cxu-tri.github.io/FAIL-Detect-Website/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

실제 deployment failure는 다양하고 사전에 수집하기 어려워 failure-supervised detector의 확장성이 낮다.

## Core Assumptions

- 정상 training trajectory만으로 failure와 상관된 epistemic/OOD signal을 학습할 수 있다.
- Detector signal의 distribution이 calibration 이후 deployment task에서도 유지된다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `Policy uncertainty / OOD detection → FAIL-Detect / SAFE → typed recovery` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

Failure detection이 recovery action 선택까지 해결하지 않는다.
