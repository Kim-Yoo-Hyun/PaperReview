# MM-ACT: Learn from Multimodal Parallel Generation to Act

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

의미 이해와 예측을 행동 생성에 함께 활용하는 generalist policy 학습이 필요하다.

## Bottleneck and Changed Formulation

텍스트·영상·행동을 공유 token 공간과 context로 학습하고 modality별 병렬 decoding을 사용한다.

## System and Robotics Loop

공유 multimodal context → text/image/action generation; action은 one-step parallel decoding.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

modality별 loss·compute 균형, 생성 token이 action에 주는 영향, RL 미검증 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO, 실제 Franka, RoboTwin2.0의 in-domain·out-of-domain 조작을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) · [저자 project/code](https://github.com/HHYHRHY/MM-ACT). Exact objective, constraints, success definition은 본문 수동 확인 필요.
