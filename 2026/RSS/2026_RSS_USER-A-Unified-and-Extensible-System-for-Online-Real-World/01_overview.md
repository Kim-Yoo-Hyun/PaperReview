# USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hongzhi Zang, Shu'ang Yu, Hao Lin, Tianxing Zhou, Zefang Huang, Zhen Guo, Xin Xu, Yuze Sheng, Jiakai Zhou, Shizhe Zhang, Feng Gao, Wenhao Tang, Yufeng Yue, Quanlu Zhang, Xinlei Chen, Chao Yu, Yu Wang
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: real-robot-learning, asynchronous, distributed-system
- Aliases: USER, RLinf-USER
- Official paper: https://roboticsproceedings.org/rss22/p037.html
- Venue verification: https://roboticsproceedings.org/rss22/p037.html
- Code/Project: https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst
- Code: https://github.com/RLinf/RLinf
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

USER는 실제 로봇의 데이터 수집과 온라인 정책 학습을 비동기로 운영하는 시스템이다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p037.pdf#page=1)

## Core Idea and Contribution

- 기종별 장비 인터페이스와 학습 통신을 분리하고, 경험을 영속적으로 보존하면서 자주 읽는 데이터를 캐시하는 재생 버퍼를 설계했다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p037.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p037.pdf#page=4)
- 서로 다른 조작기와 여러 로봇을 이용한 학습을 검증하고, 장기 실행에서는 버퍼 재사용이 학습에 미치는 영향을 측정했다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p037.pdf#page=7) · [PDF 9쪽](https://roboticsproceedings.org/rss22/p037.pdf#page=9)

## Observation–State–Action Interface

Robot observation/action/reward stream ↔ edge/cloud rollout·training workers ↔ policy weight synchronization.

## Evaluation Scope and Claim Boundary

RSS abstract는 simulation과 실제 multi-robot·heterogeneous manipulator·edge-cloud·장기 비동기 학습 사례를 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p037.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLux-VLA와 역할이 다르다.

## Verification Boundary

Weight version tagging, replay consistency, crash recovery와 실제 robot 시간 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
