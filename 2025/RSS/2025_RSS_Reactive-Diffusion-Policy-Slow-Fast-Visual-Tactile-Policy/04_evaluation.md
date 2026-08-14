# Evaluation — Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

- Year/Venue: 2025 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, Diffusion, tactile sensing, contact-rich manipulation, slow-fast control, Imitation Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p052.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p052.pdf
- Code/Project: https://reactive-diffusion-policy.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 공식 RSS abstract는 3개 contact-rich task와 서로 다른 tactile/force sensor 적용을 보고한다.
- Success 외에 reaction time, contact force와 sensor transfer를 확인해야 한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

한 개 insertion task에서 visual-only chunk, tactile concatenation, slow-fast residual을 동일 demonstration으로 비교한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
