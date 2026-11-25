# ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Zhenyang Chen, Alan Tian, Liquan Wang, Benjamin Joffe, Yingyan Celine Lin, Yuxiao Chen, Siddharth Karamcheti, Danfei Xu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: multitask-policy, VLA, instruction-switching, steerability
- Aliases: ReSteer
- Official paper: https://roboticsproceedings.org/rss22/p143.html
- Venue verification: https://roboticsproceedings.org/rss22/p143.html
- Code/Project: https://resteer-vla.github.io/
- Code: https://github.com/ChenZhenY/ReSteer
- Source audit: 2026-10-31 공식 서지/abstract·공개 project/code 소개를 재확인했다. 신규 노트는 abstract 기반이며 기존 연구 검토의 지정 본문/code 확인은 work/sources/instruction_revision_review_2026-10-31.json 및 pre_gpu_buildup_review_2026-10-31.json의 별도 범위다. 사용자 정독·native 실행을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ReSteer는 로봇이 작업을 수행하는 도중 지시가 바뀌면 이미 진행한 상태에서 새 목표로 전환하도록 정책을 학습한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p143.pdf#page=1)

## Core Idea and Contribution

- 두 지시의 훈련 궤적이 겹치는 정도와 전환 가능성의 관계를 조사하고 가능한 전환 동작을 생성·개선하는 학습 절차를 제안했다. [PDF 4쪽](https://roboticsproceedings.org/rss22/p143.pdf#page=4) · [PDF 6쪽](https://roboticsproceedings.org/rss22/p143.pdf#page=6)
- LIBERO와 실물 조작에서 지시 변경 뒤 새 목표에 도달하는지를 평가하고 전환 자료가 없는 정책과 비교했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p143.pdf#page=6) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p143.pdf#page=8)

## Observation–State–Action Interface

현재 관측과 새 언어 지시 → multitask policy의 행동. 중간 상태에서의 전환 능력과 초기 상태의 작업 능력을 구별한다.

## Evaluation Scope and Claim Boundary

LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p143.html) · [저자 project/code](https://resteer-vla.github.io/) · [공식 code](https://github.com/ChenZhenY/ReSteer). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 부분 지시 수정 후보의 기본 switching 선행이자 최소 실행의 직접 prerequisite다. 단순 task switch나 행동 큐 교체를 신규 기여로 삼지 않도록 NEXT에 추가한다.

## Verification Boundary

steerability score의 분모·switch timing·초기 능력, estimator와 실제 성공의 관계, 데이터 생성 비용, 제약 유지·철회가 평가에 포함되는 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 지시 전환 가능성 평가 · resteer/eval/steerability.py [배포 파일](https://raw.githubusercontent.com/ChenZhenY/ReSteer/7329c159319a346b7245a69c128e5d4940c0763b/resteer/eval/steerability.py)
- 가중치·학습 파라미터 — 배포 표에서 ReSteer π0.5의 SteerGen·SRBC 체크포인트가 공개 예정으로 표시되어 있다. [저자 공개 안내](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/README.md)
- 데이터 — 배포 표에서 SteerGen·SRBC 시연과 전환 상태 뱅크가 공개 예정으로 표시되어 있다. [저자 공개 안내](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/README.md)
