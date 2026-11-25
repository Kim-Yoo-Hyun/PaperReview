# CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Tianhang Pan, Xuanhao Wang, Yiwen Pang, Bo Zhou, Jun Yang, Min-Ling Zhang, Shimin Di
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, camera shift, RGB-D reprojection, asynchronous inference
- Aliases:
- Official paper: https://arxiv.org/abs/2609.37150
- Venue verification: https://arxiv.org/abs/2609.37150
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

카메라 이동을 다루는 CoRe-VLA는 장면을 정책이 학습한 시점으로 다시 렌더링해 외부 카메라와 손목 카메라 사이의 협응을 복원한다. [PDF 1쪽](https://arxiv.org/pdf/2609.37150v1#page=1)

## Core Idea and Contribution

- RGB-D 점군을 다시 투영한 영상의 결함을 복원하고, 이미 실행한 궤적에 맞춰 비동기 행동 출력을 정렬한다. [PDF 5쪽](https://arxiv.org/pdf/2609.37150v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.37150v1#page=6)
- 카메라 위치를 바꾼 실물 조작과 LIBERO 계열 과제에서 기존 VLA를 미세조정하지 않고 얻는 성공률 변화를 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2609.37150v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2609.37150v1#page=8)

## Observation–State–Action Interface

RGB-D·카메라 관계 → 복원 영상 → frozen VLA action.

## Evaluation Scope and Claim Boundary

5 real-robot task, LIBERO-100와 LIBERO-Plus를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.37150) · 저자 프로젝트·코드 주소 미확인. 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

D1 camera-shift 보정의 직접 NEXT baseline이다. Conditional Routing CoRE-VLA와 별도 identity다.

## Verification Boundary

intrinsic/extrinsic 접근, depth 정렬, asynchronous 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
