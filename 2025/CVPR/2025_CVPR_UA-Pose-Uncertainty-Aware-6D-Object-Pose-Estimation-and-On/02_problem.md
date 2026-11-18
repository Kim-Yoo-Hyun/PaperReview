# UA-Pose: Uncertainty-Aware 6D Object Pose Estimation and Online Object Completion with Partial References

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

완전 CAD나 전체 표면 reference 없이 부분 관측만으로 미지 물체 pose를 추정해야 한다.

## Bottleneck and Changed Formulation

부분 3D 모델의 관측·미관측 영역 불확실성을 활용해 pose 신뢰도와 온라인 completion sampling을 다룬다.

## System and Robotics Loop

Known-pose RGB-D 소수 관측 또는 한 장의 reference 이미지에서 출발해 pose와 보완된 물체 표현을 출력한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Image-to-3D 전제·미관측 uncertainty의 calibration·실세계 control 평가.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

YCB-Video·YCBInEOAT·HO3D의 로봇/손 조작 RGB-D 시퀀스를 평가한다. 제어 정책 성공의 실증과 구별한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) · [저자 project/code](https://minfenli.github.io/UA-Pose/) · [공식 저장소(구현 공개 미확인)](https://github.com/minfenli/UA-Pose). Exact objective, constraints, success definition은 본문 수동 확인 필요.
