# Method — π0: A Vision-Language-Action Flow Model for General Robot Control

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Flow Matching, generalist policy, cross-embodiment, dexterous manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p010.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p010.pdf
- Code/Project: https://www.pi.website/research/pi0
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- Pretrained VLM 위에 flow-matching action expert를 결합한다.
- Single-arm, dual-arm, mobile manipulator의 다양한 data로 공동 학습한다.
- 직접 prompting, high-level VLM instruction, downstream fine-tuning을 하나의 generalist policy setting에서 다룬다.

## Interface

이미지·language·proprioception을 받아 연속 action chunk를 flow-matching 과정으로 생성한다. 실제 controller의 action convention과 rate는 embodiment별 adapter가 담당한다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `Flow Matching + pretrained VLM → π0 → FAST / π0.5`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
