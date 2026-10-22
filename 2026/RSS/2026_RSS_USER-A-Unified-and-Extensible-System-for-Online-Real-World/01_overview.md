# USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: real-robot-learning, asynchronous, distributed-system
- Aliases: USER, RLinf-USER
- Official paper: https://roboticsproceedings.org/rss22/p037.html
- Venue verification: https://roboticsproceedings.org/rss22/p037.html
- Code/Project: https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst
- Code: https://github.com/RLinf/RLinf
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

실제 robot online learning은 cheap reset·대규모 병렬화가 불가능하고 이기종 장비·통신·장기 학습 관리가 필요하다.

## Core Idea and Contribution

Robot/GPU 추상화, adaptive communication 및 persistent buffer를 갖춘 asynchronous learning system을 제안한다.

## Observation–State–Action Interface

Robot observation/action/reward stream ↔ edge/cloud rollout·training workers ↔ policy weight synchronization.

## Evaluation Scope and Claim Boundary

RSS abstract는 simulation과 실제 multi-robot·heterogeneous manipulator·edge-cloud·장기 비동기 학습 사례를 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p037.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLux-VLA와 역할이 다르다.

## Verification Boundary

Weight version tagging, replay consistency, crash recovery와 실제 robot 시간 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
