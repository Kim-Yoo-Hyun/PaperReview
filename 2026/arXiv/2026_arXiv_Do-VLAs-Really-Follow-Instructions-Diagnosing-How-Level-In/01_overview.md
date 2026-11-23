# Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Sangwu Park, Wonjoong Kim, Yeonjun In, Chanyoung Park
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Benchmark, instruction-following
- Aliases: How-level instruction following, SIMPLER-IN
- Official paper: https://arxiv.org/abs/2610.21251
- Venue verification: https://arxiv.org/abs/2610.21251
- Code/Project: https://github.com/sangwu99/how-level-vla-Arxiv
- Code: https://github.com/sangwu99/how-level-vla-Arxiv
- Source audit: 2026-10-31 공식 서지/abstract·공개 project/code 소개를 재확인했다. 신규 노트는 abstract 기반이며 기존 연구 검토의 지정 본문/code 확인은 work/sources/instruction_revision_review_2026-10-31.json 및 pre_gpu_buildup_review_2026-10-31.json의 별도 범위다. 사용자 정독·native 실행을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 VLA가 무엇을 할지 지정하는 지시와 어떻게 수행할지 지정하는 세부 지시를 실제 행동에 반영하는지 구분해 시험한다. [PDF 1쪽](https://arxiv.org/pdf/2610.21251v2#page=1)

## Core Idea and Contribution

- 조작 궤적의 세부 구간에 언어를 붙여 학습하고 시각 관측만으로 알 수 없는 실행 제약을 지시에 넣은 SIMPLER-IN을 구축했다. [PDF 3쪽](https://arxiv.org/pdf/2610.21251v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.21251v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.21251v2#page=5)
- 세부 지시에 대한 행동 민감도가 높아져도 작업 성공이 일관되게 향상되지는 않으며 낯선 지시 조건에서 격차가 남음을 보고했다. [PDF 7쪽](https://arxiv.org/pdf/2610.21251v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2610.21251v2#page=8)

## Observation–State–Action Interface

영상·행동 맥락과 수행 방식 지시 → VLA 행동 → 목표 달성 및 지시 조건 준수 평가.

## Evaluation Scope and Claim Boundary

보강된 지시에 대한 행동 반응이 늘어도 작업 성공이 일관되게 높아지지는 않으며, 까다롭거나 분포 밖의 지시에 일반화가 제한된다고 보고한다. SIMPLER-IN의 상세 task·split·trial은 본문 확인 대상이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.21251) · [저자 project/code](https://github.com/sangwu99/how-level-vla-Arxiv). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 제약 유지·철회 후보에서 지시 반응, 목표 성공, 제약 준수를 분리할 직접 진단 선행이다. 평가 정의 자체를 새 기여로 과장하지 않기 위한 NEXT이며 preprint로 둔다.

## Verification Boundary

SIMPLER-IN 조건별 성공 정의와 중립 문장 대조, 지시 보강 학습의 정보·데이터 통제, OOD 범위, 평가 코드와 checkpoint 일치을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
