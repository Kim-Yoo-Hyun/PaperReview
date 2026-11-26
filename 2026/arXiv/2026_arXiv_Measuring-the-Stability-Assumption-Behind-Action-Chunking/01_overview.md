# Measuring the Stability Assumption Behind Action Chunking

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Aryan Goyal
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: VLA, action-chunking, feedback, diffusion policy, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2610.01626
- Full-text retrieval: https://arxiv.org/pdf/2610.01626v1
- Venue verification: https://arxiv.org/abs/2610.01626
- Code/Project: https://aryangoyal7.github.io/publication/2026-stability-action-chunking
- Code: project_only
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

이 연구는 모방 정책의 행동에 작은 교란을 넣고 계획된 행동을 계속 실행하거나 다시 계획할 때 오차가 증폭·감쇠하는 속도를 상태별로 측정한다. [PDF 1쪽](https://arxiv.org/pdf/2610.01626v1#page=1)

## Core Idea and Contribution

- 두 실행 조건에서 관측된 궤적 편차로 국소 전파율을 적합하고 불확실한 추정에 별도 판정을 부여한다. [PDF 3쪽](https://arxiv.org/pdf/2610.01626v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.01626v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.01626v1#page=5)
- 세 벤치마크의 조작 과제에서 상태별 안정성 및 두 실행 방식의 판정 차이를 비교하고 측정 설정에 대한 민감도를 조사했다. [PDF 8쪽](https://arxiv.org/pdf/2610.01626v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2610.01626v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2610.01626v1#page=10) · [PDF 11쪽](https://arxiv.org/pdf/2610.01626v1#page=11)

## Observation–State–Action Interface

같은 초기 상태·action perturbation → rollout → divergence slope.

## Evaluation Scope and Claim Boundary

GR00T manipulation task에서 chunk 안정성 가정의 차이를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.01626) · [저자 project/code](https://aryangoyal7.github.io/publication/2026-stability-action-chunking). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

같은 시뮬레이터 상태에서 행동을 교란한 뒤 고정 행동열 재생과 정책 재호출에서 궤적 편차를 측정한다. robomimic 등에서는 과제별 확산 정책을, RoboCasa에서는 공개 GR00T N1.5 정책을 조사했다. VLA는 여러 평가 대상 중 하나다. [원문 4쪽](https://arxiv.org/pdf/2610.01626v1#page=4) · [원문 6쪽](https://arxiv.org/pdf/2610.01626v1#page=6)

## Why This Paper Is Here — Researcher Interpretation

E2 진단에서도 state-dependent 안정성을 새 발견으로 주장하지 않도록 하는 REFERENCE다.

## Verification Boundary

norm 단위, perturbation 크기, branch 동치, 전역 안정성과의 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
