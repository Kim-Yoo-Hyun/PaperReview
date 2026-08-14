# Problem — FAST: Efficient Action Tokenization for Vision-Language-Action Models

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Per-dimension·per-timestep discretization은 temporal correlation이 강한 high-frequency dexterous action을 비효율적으로 표현한다.

## Core Assumptions

- Action trajectory가 frequency-space에서 압축 가능하다.
- 공통 tokenizer가 서로 다른 action convention과 control rate의 핵심 구조를 보존한다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `RT-1/OpenVLA tokenization → FAST → high-frequency autoregressive VLA` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

압축이 급격한 contact correction이나 discontinuity를 지울 수 있다.
