# PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

정밀 조작에서는 모든 context와 flow time의 오류를 동일하게 다루는 학습이 중요한 구간의 supervision을 충분히 배분하지 못할 수 있다.

## Bottleneck and Changed Formulation

시연의 proprioception으로 정밀도 요구를 점수화하고 flow supervision과 VLM 조건 표현 학습에 반영한다. 저자 project는 학습용 보조 head/label을 추론에서 제거한다고 설명한다.

## System and Robotics Loop

VLM condition과 flow action expert의 학습을 조정한다. 정밀도 점수는 학습 신호이며 별도 센서나 test-time oracle 입력으로 설명하지 않는다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

정밀도 proxy와 실제 공차의 차이·flow-time weighting·SNR gate·auxiliary loss·task별 trial·공개 구현의 논문 일치.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.14704) · [저자 project/code](https://seen-e.github.io/PRISM/) · [공식 code](https://github.com/seen-e/PRISM). Exact objective, constraints, success definition은 본문 수동 확인 필요.
