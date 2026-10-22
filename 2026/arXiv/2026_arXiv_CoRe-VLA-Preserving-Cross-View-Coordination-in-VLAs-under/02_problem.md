# CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

외부 카메라 이동으로 VLA의 global/wrist-view 협력이 깨지는 문제다.

## Bottleneck and Changed Formulation

Point-cloud reprojection과 render 복원, execution alignment로 training view를 복구한다.

## System and Robotics Loop

RGB-D·카메라 관계 → 복원 영상 → frozen VLA action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

intrinsic/extrinsic 접근, depth 정렬, asynchronous 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

5 real-robot task, LIBERO-100와 LIBERO-Plus를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.37150) · [저자 project/code](https://arxiv.org/abs/2609.37150). Exact objective, constraints, success definition은 본문 수동 확인 필요.
