# Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-10-31 공식 서지/abstract·공개 project/code 소개를 재확인했다. 신규 노트는 abstract 기반이며 기존 연구 검토의 지정 본문/code 확인은 work/sources/instruction_revision_review_2026-10-31.json 및 pre_gpu_buildup_review_2026-10-31.json의 별도 범위다. 사용자 정독·native 실행을 뜻하지 않는다.

## Problem and Importance

어떤 작업을 할지뿐 아니라 어떻게 수행할지를 지정하는 언어 조건의 준수는 일반 task success만으로 평가하기 어렵다.

## Core Idea and Contribution

How-level 지시의 효과를 진단하고 segment-level 지시 보강을 비교하며, 지시에만 주어진 조건을 성공 정의에 포함하는 SIMPLER-IN을 제안한다.

## Observation–State–Action Interface

영상·행동 맥락과 수행 방식 지시 → VLA 행동 → 목표 달성 및 지시 조건 준수 평가.

## Evaluation Scope and Claim Boundary

보강된 지시에 대한 행동 반응이 늘어도 작업 성공이 일관되게 높아지지는 않으며, 까다롭거나 분포 밖의 지시에 일반화가 제한된다고 보고한다. SIMPLER-IN의 상세 task·split·trial은 본문 확인 대상이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.21251) · [저자 project/code](https://github.com/sangwu99/how-level-vla-Arxiv). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 제약 유지·철회 후보에서 지시 반응, 목표 성공, 제약 준수를 분리할 직접 진단 선행이다. 평가 정의 자체를 새 기여로 과장하지 않기 위한 NEXT이며 preprint로 둔다.

## Verification Boundary

SIMPLER-IN 조건별 성공 정의와 중립 문장 대조, 지시 보강 학습의 정보·데이터 통제, OOD 범위, 평가 코드와 checkpoint 일치을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
