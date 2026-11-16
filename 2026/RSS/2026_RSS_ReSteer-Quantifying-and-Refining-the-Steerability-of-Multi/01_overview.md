# ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, instruction-switching, steerability
- Aliases: ReSteer
- Official paper: https://roboticsproceedings.org/rss22/p143.html
- Venue verification: https://roboticsproceedings.org/rss22/p143.html
- Code/Project: https://resteer-vla.github.io/
- Code: https://github.com/ChenZhenY/ReSteer
- Source audit: 2026-10-31 공식 서지/abstract·공개 project/code 소개를 재확인했다. 신규 노트는 abstract 기반이며 기존 연구 검토의 지정 본문/code 확인은 work/sources/instruction_revision_review_2026-10-31.json 및 pre_gpu_buildup_review_2026-10-31.json의 별도 범위다. 사용자 정독·native 실행을 뜻하지 않는다.

## Problem and Importance

표준 초기 상태에서는 각각 가능한 작업도 실행 중 지시를 바꾸면 전환되지 않을 수 있다.

## Core Idea and Contribution

상태별 task steerability를 측정하고, 전환이 어려운 상태의 추정·전환 구간 데이터 생성·정책 self-refinement를 연결한다.

## Observation–State–Action Interface

현재 관측과 새 언어 지시 → multitask policy의 행동. 중간 상태에서의 전환 능력과 초기 상태의 작업 능력을 구별한다.

## Evaluation Scope and Claim Boundary

LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p143.html) · [저자 project/code](https://resteer-vla.github.io/) · [공식 code](https://github.com/ChenZhenY/ReSteer). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

현재 부분 지시 수정 후보의 기본 switching 선행이자 최소 실행의 직접 prerequisite다. 단순 task switch나 행동 큐 교체를 신규 기여로 삼지 않도록 NEXT에 추가한다.

## Verification Boundary

steerability score의 분모·switch timing·초기 능력, estimator와 실제 성공의 관계, 데이터 생성 비용, 제약 유지·철회가 평가에 포함되는 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
