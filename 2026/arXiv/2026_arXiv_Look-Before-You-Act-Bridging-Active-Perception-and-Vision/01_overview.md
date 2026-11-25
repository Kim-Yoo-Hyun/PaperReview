# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> Evidence maturity: `ABSTRACT_CHECKED`. 아래의 요약·기여는 인용한 원문 쪽에서 추가 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yongchong Gu, Yanwei Fu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, active perception, manipulation, robustness
- Aliases: ActiveAlign
- Official paper: https://arxiv.org/abs/2610.23378
- Venue verification: https://arxiv.org/abs/2610.23378
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

ActiveAlign은 카메라를 움직인 직후의 관측·로봇 상태에서 시작할 수 있도록 조작 시연을 다시 구성해 VLA를 미세조정한다. [PDF 3쪽](https://arxiv.org/pdf/2610.23378v1#page=3)

## Core Idea and Contribution

- 시점 선택기의 종착 상태를 시연에 정렬하고 이후 구간을 재생해 성공한 연결 궤적으로 정책을 적응시킨다. [PDF 4쪽](https://arxiv.org/pdf/2610.23378v1#page=4)
- 시뮬레이션과 두 실물 작업대에서 고정 시점, 시점 이동만 적용, 시점 이동 후 적응을 분리해 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2610.23378v1#page=7)

## Observation–State–Action Interface

초기 영상·state → camera/관측 정렬 → VLA continuation.

## Evaluation Scope and Claim Boundary

LIBERO와 실제 robot manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.23378). 성공률과 비교 조건은 [평가 노트](./04_evaluation.md#조건별-성공률)에서 확인할 수 있다.

## Why This Paper Is Here — Researcher Interpretation

C1/D1의 능동 관측·관측 정렬 주장과 직접 충돌한다.

## Verification Boundary

camera 행동 비용, state change, 성공 continuation 선택, data budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

실물 시행의 분모와 비교 조건은 [조건별 성공률](./04_evaluation.md#조건별-성공률)에 기록했다.
