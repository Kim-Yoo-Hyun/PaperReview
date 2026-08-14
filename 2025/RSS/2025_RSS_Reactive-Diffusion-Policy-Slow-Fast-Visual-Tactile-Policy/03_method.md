# Method — Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

- Year/Venue: 2025 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, Diffusion, tactile sensing, contact-rich manipulation, slow-fast control, Imitation Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p052.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p052.pdf
- Code/Project: https://reactive-diffusion-policy.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- TactAR teleoperation으로 실시간 tactile feedback이 포함된 demonstration을 수집한다.
- 저주파 latent diffusion policy가 high-level action chunk를 예측한다.
- 고주파 asymmetric tokenizer가 tactile feedback을 이용해 chunk 내부 action을 수정한다.

## Interface

Vision은 느린 latent plan에, tactile signal은 빠른 closed-loop correction에 들어가는 dual-rate policy다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `Diffusion Policy → Reactive Diffusion Policy → tactile/force-aware VLA executor`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
