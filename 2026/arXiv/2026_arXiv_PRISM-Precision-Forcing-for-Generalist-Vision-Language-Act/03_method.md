# PRISM: Precision Forcing for Generalist Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

시연의 proprioception으로 정밀도 요구를 점수화하고 flow supervision과 VLM 조건 표현 학습에 반영한다. 저자 project는 학습용 보조 head/label을 추론에서 제거한다고 설명한다.

## Observation–State–Action Interface

VLM condition과 flow action expert의 학습을 조정한다. 정밀도 점수는 학습 신호이며 별도 센서나 test-time oracle 입력으로 설명하지 않는다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 정밀도 proxy와 실제 공차의 차이·flow-time weighting·SNR gate·auxiliary loss·task별 trial·공개 구현의 논문 일치.

Source가 명시한 evaluation 범위: 초록·project는 simulation과 실제 로봇의 connector insertion, 양팔 connector mating, screw tightening을 보고한다. Trial 수·task별 분모·성공 정의와 수치 비교는 본문 대조 전 미확정이다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Action-expert 재가중과 geometry adapter 학습을 동일 데이터/label/compute에서 분리하고 정밀도별 성공·일반 task 유지 성능을 함께 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.14704) · [저자 project/code](https://seen-e.github.io/PRISM/) · [공식 code](https://github.com/seen-e/PRISM). 수식·세부 구현·코드 실행은 미검증이다.
