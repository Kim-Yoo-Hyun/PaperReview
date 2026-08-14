# Insights — Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

- Year/Venue: 2025 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, Diffusion, tactile sensing, contact-rich manipulation, slow-fast control, Imitation Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p052.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p052.pdf
- Code/Project: https://reactive-diffusion-policy.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Paper-Supported Direction

Diffusion action chunk와 high-frequency tactile feedback을 직접 연결하는 G-01의 필수 baseline.

## Researcher Interpretation

- Foundation/frontier connection: `Diffusion Policy → Reactive Diffusion Policy → tactile/force-aware VLA executor`
- 가장 먼저 반박할 가정: 느린 visual latent plan과 빠른 tactile correction을 계층적으로 분리할 수 있다.
- 현재 gap과 연결할 때 success만 보지 않고 downstream control 또는 evaluation protocol의 변화를 확인한다.

## Limitations / Failure Modes to Audit

- Task와 sensor 수가 제한적이며 safety guarantee를 직접 제공하지 않는다.
- VLA semantic planner나 hybrid force-position controller와의 결합은 별도 문제다.

## Minimum Experiment

한 개 insertion task에서 visual-only chunk, tactile concatenation, slow-fast residual을 동일 demonstration으로 비교한다.

## Status

`UNREAD` — 이 노트는 official abstract 기반의 reading scaffold이며 정독 완료를 의미하지 않는다.
