# Problem — Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

- Year/Venue: 2025 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, Diffusion, tactile sensing, contact-rich manipulation, slow-fast control, Imitation Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p052.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p052.pdf
- Code/Project: https://reactive-diffusion-policy.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Visual imitation policy의 긴 action chunk는 complex trajectory를 표현하지만 chunk 실행 중 contact 변화에 즉시 반응하기 어렵다.

## Core Assumptions

- 느린 visual latent plan과 빠른 tactile correction을 계층적으로 분리할 수 있다.
- Teleoperation tactile feedback으로 reactive behavior에 필요한 demonstration을 수집할 수 있다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `Diffusion Policy → Reactive Diffusion Policy → tactile/force-aware VLA executor` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

Task와 sensor 수가 제한적이며 safety guarantee를 직접 제공하지 않는다.
