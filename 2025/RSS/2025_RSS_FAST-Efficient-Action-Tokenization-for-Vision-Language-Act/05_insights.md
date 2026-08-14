# Insights — FAST: Efficient Action Tokenization for Vision-Language-Action Models

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Paper-Supported Direction

Discrete token과 continuous diffusion/flow action을 비교하는 action-representation frontier.

## Researcher Interpretation

- Foundation/frontier connection: `RT-1/OpenVLA tokenization → FAST → high-frequency autoregressive VLA`
- 가장 먼저 반박할 가정: Action trajectory가 frequency-space에서 압축 가능하다.
- 현재 gap과 연결할 때 success만 보지 않고 downstream control 또는 evaluation protocol의 변화를 확인한다.

## Limitations / Failure Modes to Audit

- 압축이 급격한 contact correction이나 discontinuity를 지울 수 있다.
- Training efficiency와 runtime closed-loop latency는 별개의 문제다.

## Minimum Experiment

ALOHA 또는 LIBERO action sequence에서 uniform binning과 FAST의 reconstruction error, token length와 downstream BC success를 비교한다.

## Status

`UNREAD` — 이 노트는 official abstract 기반의 reading scaffold이며 정독 완료를 의미하지 않는다.
