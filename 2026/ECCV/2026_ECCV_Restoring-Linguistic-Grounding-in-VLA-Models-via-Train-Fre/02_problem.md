# Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

지시가 장면과 모순되어도 VLA가 시각적으로 익숙한 행동을 계속할 수 있다.

## Bottleneck and Changed Formulation

ICBench로 같은 장면의 모순 지시를 진단하고 추론 시 attention을 재조정하여 언어 영향을 복원한다.

## System and Robotics Loop

고정 장면·변경 instruction → attention recalibration → VLA action; 재학습은 하지 않는다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

모순의 정답 정의, 무조건 정지 대조, 정상 지시 성능 trade-off.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

π0·π0.5·OpenVLA-OFT, LIBERO task와 실제 Franka에서 지시 모순에 따른 잘못된 실행을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3) · [저자 project/code](https://ray-nh.github.io/igar/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
