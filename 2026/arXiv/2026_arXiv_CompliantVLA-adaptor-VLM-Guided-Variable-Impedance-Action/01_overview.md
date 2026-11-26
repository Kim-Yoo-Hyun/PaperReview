# CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / arXiv
- Authors: Heng Zhang, Wei-Hsing Huang, Qiyi Tong, Gokhan Solak, Puze Liu, Kaidi Zhang, Sheng Liu, Jan Peters, Yu She, Arash Ajoudani
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, VLM, variable-impedance, force-feedback, multi-rate control
- Aliases: CompliantVLA-adaptor
- Official paper: https://arxiv.org/abs/2601.15541
- Venue verification: https://arxiv.org/abs/2601.15541
- Code/Project: https://sites.google.com/view/compliantvla
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2601.15541v2
- Source audit: 2026-11-24에 요약과 기여를 대조했다. 2026-11-26에 III-B 식 (6)–(7)에 따라 강성과 감쇠의 계산 절차를 교정했다.

## Problem and Importance

CompliantVLA-adaptor는 VLA가 생성한 위치 명령을 작업 맥락과 힘·토크 피드백에 따라 가변 임피던스 제어로 실행한다. [PDF 1쪽](https://arxiv.org/pdf/2601.15541v2#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2601.15541v2#page=3)

## Core Idea and Contribution

- VLM이 제안한 강성을 측정 힘에 따라 조절하고, 조절된 강성·유효 질량·감쇠비로 제어기에 적용할 감쇠를 계산한다. [PDF 3쪽](https://arxiv.org/pdf/2601.15541v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2601.15541v2#page=4)
- 시뮬레이션 접촉 과제와 실물 상자 밀기·화이트보드 닦기에서 어댑터 유무에 따른 과제 성공과 접촉력을 측정했다. [PDF 5쪽](https://arxiv.org/pdf/2601.15541v2#page=5) · [PDF 7쪽](https://arxiv.org/pdf/2601.15541v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2601.15541v2#page=8)

## Observation–State–Action Interface

VLA가 목표 동작을 내고, VLM이 영상·지시·힘을 바탕으로 강성을 제안한다. 제어기는 측정 힘으로 강성을 조절하고 적용 감쇠를 계산한다.

## Evaluation Scope and Claim Boundary

Simulation과 실제 접촉 과제에서 성공률·force violation을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.15541) · [저자 project/code](https://sites.google.com/view/compliantvla).

## 검색 태그 근거

VLM 질의와 힘 피드백에는 서로 다른 주기가 있다. 실험에서는 매 두 행동 스텝마다 VLM을 호출했고, 그 사이에도 제어기는 측정 힘에 따라 강성을 조절했다. [실행 제어식](https://arxiv.org/pdf/2601.15541v2#page=4) · [실험의 질의 주기](https://arxiv.org/pdf/2601.15541v2#page=6)

## Why This Paper Is Here — Researcher Interpretation

단일 VLA RL 이전에 비교할 학습 없는 context/force 기반 controller 대안이다.

## Verification Boundary

Prompt와 controller 설정 비용, force threshold, release 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
