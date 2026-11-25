# Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Authors: Ningyu Yan, Shuai Wang, Xing Shen, Hui Wang, Hanqing Wang, Yang Xiang, Jiangmiao Pang
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: visuotactile, contact-rich, sim-to-real
- Aliases: Tac2Real
- Official paper: https://arxiv.org/abs/2603.28475
- Venue verification: https://api.crossref.org/works/10.1007/978-3-032-37550-6_13
- Code/Project: https://ningyurichard.github.io/tac2real-project-page/
- Code: not_released
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. ECCV 2026 accepted/video list의 공식 검색 색인과 저자 abstract 대조; proceedings page/DOI 미확인. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Tac2Real은 촉각 센서의 변형을 GPU로 모사해 접촉 조작 정책을 시뮬레이션에서 강화학습하고 실물에 전이한다. [PDF 1쪽](https://arxiv.org/pdf/2603.28475v1#page=1)

## Core Idea and Contribution

- 접촉 시뮬레이션으로 촉각 마커의 변위를 계산하고 TacAlign으로 시뮬레이션의 제어·센서 특성을 실물에 맞춘다. [PDF 4쪽](https://arxiv.org/pdf/2603.28475v1#page=4) · [PDF 7쪽](https://arxiv.org/pdf/2603.28475v1#page=7)
- 초기 방향이 달라지는 실제 핀 삽입에서 추가 실물 학습 없이 정책을 시험하고 보정 단계에 따른 차이를 측정했다. [PDF 12쪽](https://arxiv.org/pdf/2603.28475v1#page=12) · [PDF 13쪽](https://arxiv.org/pdf/2603.28475v1#page=13)

## Observation–State–Action Interface

Contact dynamics → tactile marker displacement/visual signal → RL policy → insertion action.

## Evaluation Scope and Claim Boundary

공식 abstract/project는 contact-rich peg insertion의 zero-shot real-world transfer 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.28475) · [저자 project/code](https://ningyurichard.github.io/tac2real-project-page/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / simulator. Tactile feedback을 이용하는 insertion·contact RL을 선택할 때 relevant하다. HIL-SERL 등 실제 interaction 학습과 simulation fidelity/transfer를 비교한다. Peg insertion 결과를 범용 dexterity로 확대하지 않는다.

## Verification Boundary

Tactile sensor calibration, contact parameter 분포, marker fidelity와 code 공개 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 저자 저장소가 구현 공개를 게재 이후로 예고한다. 확인한 리비전에는 구현 파일이 없다. [저자 공개 안내](https://github.com/InternRobotics/Tac2Real/blob/4ba3decc1430acbda62861dd8220589d2b07c7c8/README.md)
