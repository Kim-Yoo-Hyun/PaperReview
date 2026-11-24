# CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / arXiv
- Authors: Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, VLM, variable-impedance, force-feedback
- Aliases: CompliantVLA-adaptor
- Official paper: https://arxiv.org/abs/2601.15541
- Venue verification: https://arxiv.org/abs/2601.15541
- Code/Project: https://sites.google.com/view/compliantvla
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2601.15541v2
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

CompliantVLA-adaptor는 VLA가 생성한 위치 명령을 작업 맥락과 힘·토크 피드백에 따라 가변 임피던스 제어로 실행한다. [PDF 1쪽](https://arxiv.org/pdf/2601.15541v2#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2601.15541v2#page=3)

## Core Idea and Contribution

- 시각·언어 모델이 장면과 지시에서 강성·감쇠를 정하고, 접촉 중 측정한 힘·토크에 따라 제어 파라미터를 다시 조절한다. [PDF 3쪽](https://arxiv.org/pdf/2601.15541v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2601.15541v2#page=4)
- 시뮬레이션 접촉 과제와 실물 상자 밀기·화이트보드 닦기에서 어댑터 유무에 따른 과제 성공과 접촉력을 측정했다. [PDF 5쪽](https://arxiv.org/pdf/2601.15541v2#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2601.15541v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2601.15541v2#page=8)

## Observation–State–Action Interface

이미지·언어 → stiffness/damping; force feedback → controller 보정.

## Evaluation Scope and Claim Boundary

Simulation과 실제 접촉 과제에서 성공률·force violation을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.15541) · [저자 project/code](https://sites.google.com/view/compliantvla).

## Why This Paper Is Here — Researcher Interpretation

단일 VLA RL 이전에 비교할 학습 없는 context/force 기반 controller 대안이다.

## Verification Boundary

Prompt와 controller 설정 비용, force threshold, release 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
