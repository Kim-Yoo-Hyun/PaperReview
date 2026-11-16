# Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

비정형 사람 영상에서 정확한 robot action supervision을 확보하기 어렵다.

## Bottleneck and Changed Formulation

역동역학과 실제 행동에 함께 정렬한 latent action을 학습한다.

## System and Robotics Loop

사람 영상 전이 → 행동 중심 embedding → VLA 사전학습.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

실제 action label 요구량, 인간 손과 robot action 대응, 비정형 영상 split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

사람 동작 및 simulation·실제 robot manipulation 전이를 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html) · [저자 project/code](https://research.beingbeyond.com/jala) · [공식 code](https://github.com/BeingBeyond/JALA). Exact objective, constraints, success definition은 본문 수동 확인 필요.
