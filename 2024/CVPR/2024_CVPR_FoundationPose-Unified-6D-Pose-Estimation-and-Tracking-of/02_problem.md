# FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

미지 물체의 pose 추정과 추적에서 완전 CAD와 소수 reference 관측의 서로 다른 전제를 통합한다.

## Bottleneck and Changed Formulation

Neural implicit 표현으로 두 입력 조건을 연결해 동일 pose 모듈을 재사용한다. 새 물체별 fine-tuning 없이 적용하는 설정이다.

## System and Robotics Loop

RGB-D와 CAD 또는 reference 관측에서 물체 6D pose·tracking 출력을 얻는다. 행동 정책 자체는 아니다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Model-free reference 요구·대칭 처리·ranking score와 보정 확률의 차이.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 project는 미지 물체 pose estimation/tracking의 일반화를 제시한다. 이번 등록에서는 세부 trial·로봇 성공률을 확정하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) · [저자 project/code](https://nvlabs.github.io/FoundationPose/) · [공식 code](https://github.com/NVlabs/FoundationPose). Exact objective, constraints, success definition은 본문 수동 확인 필요.
