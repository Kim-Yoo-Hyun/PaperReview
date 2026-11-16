# Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

ICBench로 같은 장면의 모순 지시를 진단하고 추론 시 attention을 재조정하여 언어 영향을 복원한다.

## Observation–State–Action Interface

고정 장면·변경 instruction → attention recalibration → VLA action; 재학습은 하지 않는다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 모순의 정답 정의, 무조건 정지 대조, 정상 지시 성능 trade-off.

Source가 명시한 evaluation 범위: π0·π0.5·OpenVLA-OFT, LIBERO task와 실제 Franka에서 지시 모순에 따른 잘못된 실행을 평가한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

정상/모순 지시 paired set에서 SFT, RL, RL+IGAR를 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3) · [저자 project/code](https://ray-nh.github.io/igar/). 수식·세부 구현·코드 실행은 미검증이다.
