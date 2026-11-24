# CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Bei Yu, Jiaya Jia
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, feedback, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2610.21453
- Full-text retrieval: https://arxiv.org/pdf/2610.21453v1
- Venue verification: https://arxiv.org/abs/2610.21453
- Code/Project: https://vincent2311.github.io/Projects/CarryOn/
- Code: project_only
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

CarryOn은 고정된 VLA에 사용자 선호를 기억하는 계획 루프와 위험 접촉·실패에 대응하는 실행 루프를 결합한다. [PDF 1쪽](https://arxiv.org/pdf/2610.21453v1#page=1)

## Core Idea and Contribution

- 관측과 대화로 사용자·장면 정보를 갱신하고 실행 중 위험을 감시하다가 필요할 때 재사용 가능한 제어 기술로 작업을 복구한다. [PDF 4쪽](https://arxiv.org/pdf/2610.21453v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.21453v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2610.21453v1#page=6)
- 시뮬레이션에서 개인화·안전·복구를 평가하고 실물 음식 제공 과제에서 구성 요소가 함께 동작하는지 확인했다. [PDF 7쪽](https://arxiv.org/pdf/2610.21453v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2610.21453v1#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2610.21453v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2610.21453v1#page=10)

## Observation–State–Action Interface

사용자·scene context → 계획 → VLA·shield·recovery.

## Evaluation Scope and Claim Boundary

Simulation과 실제 robot assistance 결과를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.21453) · [저자 project/code](https://vincent2311.github.io/Projects/CarryOn/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

D2/D3에서 persistent planning·shield 결합의 신규성 경계를 정한다.

## Verification Boundary

메모리 입력, failure detector, recovery 비용, 공개 구현 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
