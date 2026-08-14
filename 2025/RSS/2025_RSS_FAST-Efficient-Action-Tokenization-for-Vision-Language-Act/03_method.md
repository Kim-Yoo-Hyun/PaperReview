# Method — FAST: Efficient Action Tokenization for Vision-Language-Action Models

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p012.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p012.pdf
- Code/Project: https://www.pi.website/research/fast
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- Discrete cosine transform으로 action sequence를 frequency-space에 압축한다.
- 압축된 계수를 token sequence로 만들고 FAST+ universal tokenizer를 대규모 robot trajectory에 학습한다.
- Autoregressive VLA가 high-frequency action chunk를 효율적으로 예측하도록 한다.

## Interface

Continuous action sequence를 compressed discrete token으로 encode하고 autoregressive decoder output을 다시 continuous trajectory로 복원한다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `RT-1/OpenVLA tokenization → FAST → high-frequency autoregressive VLA`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
