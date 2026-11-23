# ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Jingyi Xiang, Yixuan Wang, Jeannette Bohg, Wenzhen Yuan
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Benchmark, tactile, contact, robot-data
- Aliases: ContactBench 1.0
- Official paper: https://arxiv.org/abs/2610.24512
- Venue verification: https://arxiv.org/abs/2610.24512
- Code/Project: https://jingyi-xiang.github.io/contactbench/
- Code: https://github.com/Michaelwyx/contactbench-sim
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v2 abstract/project·simulation repository 공개 확인. Asset 공개를 완성된 RL environment 또는 학습 성공 증거로 간주하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ContactBench 1.0은 일상적인 접촉 조작을 여덟 기술로 나누고 여러 기관이 같은 물리 과제를 재현할 수 있는 평가 자원을 제공한다. [PDF 1쪽](https://arxiv.org/pdf/2610.24512v2#page=1)

## Core Idea and Contribution

- 36개 과제를 정의하고 3D 프린터로 제작할 수 있는 물체와 대응 시뮬레이션 모델을 제공해 기하와 접촉 조건을 통제할 수 있게 했다. [PDF 2쪽](https://arxiv.org/pdf/2610.24512v2#page=2) · [PDF 5쪽](https://arxiv.org/pdf/2610.24512v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2610.24512v2#page=6)
- 선정한 여섯 과제에서 시각 전용 정책과 시각·촉각 정책을 비교했으며 시험한 정책에서는 촉각 입력만으로 일관된 성능 향상을 얻지 못했다. [PDF 9쪽](https://arxiv.org/pdf/2610.24512v2#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2610.24512v2#page=10)

## Observation–State–Action Interface

물체·task variation → 실제/시뮬레이션 접촉 과제.

## Evaluation Scope and Claim Boundary

36개 reference task 중 6개에서 vision-only와 visual-tactile 정책을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.24512) · [저자 project/code](https://jingyi-xiang.github.io/contactbench/) · [공식 code](https://github.com/Michaelwyx/contactbench-sim). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

접촉 일반화 질문을 구체적인 물리 변화와 재현 자산으로 정의할 benchmark다.

## Verification Boundary

task별 success 판정, asset version, 정책용 reset/step와 scripted helper 분리을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
