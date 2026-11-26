# WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Samuel Zhen, Siwon Jo, Yanze Zhang, Wenhao Luo
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation, control barrier function, safety filter, VLA
- Aliases:
- Official paper: https://arxiv.org/abs/2610.01083
- Full-text retrieval: https://arxiv.org/pdf/2610.01083v2
- Venue verification: https://arxiv.org/abs/2610.01083
- Code/Project: https://samuelzhen.com/projects/wbag
- Code: project_only
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

WBAG는 조작 중인 로봇의 전신과 손에 쥔 물체의 형상을 함께 모델링해 VLA의 명령을 충돌 회피에 맞게 수정한다. [PDF 1쪽](https://arxiv.org/pdf/2610.01083v2#page=1)

## Core Idea and Contribution

- 물체를 잡는 상태에 따라 안전 집합을 갱신하고 제어 장벽 함수의 제약 아래 원래의 6차원 동작 명령에 가까운 해를 선택한다. [PDF 3쪽](https://arxiv.org/pdf/2610.01083v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.01083v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.01083v2#page=5)
- 장애물이 추가된 SafeLIBERO에서 과제 성공과 충돌을 측정해 전신과 부착 물체를 보호하는 효과를 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2610.01083v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2610.01083v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2610.01083v2#page=8)

## Observation–State–Action Interface

Robot·attached object geometry와 VLA action → 수정 action.

## Evaluation Scope and Claim Boundary

SafeLIBERO 기반 안전성 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.01083) · [저자 project/code](https://samuelzhen.com/projects/wbag). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

WBAG는 RGB-D로 장면을 복원하고 팔 링크와 파지 물체의 기하를 제어 장벽 함수 제약에 넣어 VLA의 행동을 투영한다. SafeLIBERO 시뮬레이션에서 팔과 물체의 충돌을 평가한다. [원문 4쪽](https://arxiv.org/pdf/2610.01083v2#page=4) · [원문 6쪽](https://arxiv.org/pdf/2610.01083v2#page=6)

## Why This Paper Is Here — Researcher Interpretation

D2의 파지 후 geometry 고려라는 넓은 기여와 직접 충돌한다.

## Verification Boundary

geometry/oracle 접근, attachment 갱신, infeasible 제약, real-robot 여부을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
