# CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Tianhang Pan, Xuanhao Wang, Yiwen Pang, Bo Zhou, Jun Yang, Min-Ling Zhang, Shimin Di
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://arxiv.org/abs/2609.37150
- Venue verification: https://arxiv.org/abs/2609.37150
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

외부 카메라 이동으로 VLA의 global/wrist-view 협력이 깨지는 문제다.

## Core Idea and Contribution

Point-cloud reprojection과 render 복원, execution alignment로 training view를 복구한다.

## Observation–State–Action Interface

RGB-D·카메라 관계 → 복원 영상 → frozen VLA action.

## Evaluation Scope and Claim Boundary

5 real-robot task, LIBERO-100와 LIBERO-Plus를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.37150) · 저자 프로젝트·코드 주소 미확인. 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1 camera-shift 보정의 직접 NEXT baseline이다. Conditional Routing CoRE-VLA와 별도 identity다.

## Verification Boundary

intrinsic/extrinsic 접근, depth 정렬, asynchronous 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
