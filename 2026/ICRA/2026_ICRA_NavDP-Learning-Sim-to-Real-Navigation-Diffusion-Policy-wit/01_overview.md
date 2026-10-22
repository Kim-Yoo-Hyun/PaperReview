# NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICRA
- Category: Embodied Navigation and Mapping
- Primary track: Planning and control
- Tier: NEXT
- Tags: Navigation, diffusion-policy, privileged-training
- Aliases: NavDP
- Official paper: https://arxiv.org/abs/2505.08712
- Venue verification: https://github.com/InternRobotics/NavDP
- Code/Project: https://github.com/InternRobotics/NavDP
- Code: https://github.com/InternRobotics/NavDP
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ICRA 2026 status는 저자 공식 자료 확인; IEEE proceedings 직접 검증 미완료.

## Problem and Importance

Simulation에서 학습한 navigation diffusion policy를 실제 환경과 다른 robot embodiment로 옮기는 문제다.

## Core Idea and Contribution

Privileged information guidance를 이용한 simulation training과 end-to-end local navigation diffusion policy를 제안한다.

## Observation–State–Action Interface

Local visual observation + point/image goal 또는 no-goal setting → trajectory/action proposal; privileged 정보의 train/test 경계 확인 필요.

## Evaluation Scope and Claim Boundary

저자 project는 no-goal exploration, point-goal/image-goal navigation과 cross-embodiment real-world transfer를 설명한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2505.08712) · [저자 project/code](https://github.com/InternRobotics/NavDP). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Simulation training에서 real-world cross-embodiment local navigation으로 이어지는 경로를 보충한다. NoMaD/ViNT의 local policy와 비교할 대상이며, 논문 자체를 language-conditioned VLA RL로 부르지는 않는다.

## Verification Boundary

Training oracle, depth/pose 입력, trajectory selector, robot footprint와 controller 한계을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
