# DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IROS
- Authors: Jeonghwan Choi, Hyunwoo Kim, Ilsung Jin, Donghan Kim
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, bimanual, reasoning, mixture-of-experts
- Aliases:
- Official paper: https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf
- Full-text retrieval: https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf
- Venue verification: https://2026.ieee-iros.org/program/paper-index/
- Code/Project: https://jjjenghi.github.io/dialogvla/
- Code: not_released
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

DialogVLA는 양팔 조작의 단계와 각 팔이 맡을 역할을 명시적으로 추론하고 그 결과에 따라 연속 행동을 생성한다. [PDF 1쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=1)

## Core Idea and Contribution

- 역할 추론 결과로 전문가 라우팅을 조건화하고 흐름 정합 행동 생성기를 단계적으로 학습한다. [PDF 2쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=2) · [PDF 3쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=3) · [PDF 4쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=4)
- 시뮬레이션의 양팔 집기·놓기와 실물 조작에서 성공률을 비교하고 추론 및 라우팅 요소의 효과를 조사했다. [PDF 5쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=5) · [PDF 6쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=6) · [PDF 7쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=7)

## Observation–State–Action Interface

Multi-view·언어·proprioception → 양팔 action.

## Evaluation Scope and Claim Boundary

저자 project는 RoboTwin, RoboCasa GR1 및 실제 양팔 평가를 제시한다.

근거: [공식 paper/abstract](https://jjjenghi.github.io/dialogvla/) · [저자 project/code](https://jjjenghi.github.io/dialogvla/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

기술 단계와 양팔의 역할을 나타낸 대화로 병렬 전문가를 조건화하고, 고유수용 상태를 받는 행동 전문가가 행동열을 복원한다. RoboTwin·RoboCasa와 실물 양팔에서 평가했다. [원문 3쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=3) · [원문 6쪽](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

D3 양팔 role reasoning의 중복을 피할 REFERENCE다. IROS 2026은 저자 표기이며 공식 채택 미확인이다.

## Verification Boundary

공식 proceedings, 원문 공개, source version, code release을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
