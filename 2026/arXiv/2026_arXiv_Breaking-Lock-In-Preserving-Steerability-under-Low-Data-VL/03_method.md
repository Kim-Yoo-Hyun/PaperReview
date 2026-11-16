# Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

후학습 중 시각 grounding을 보존하고 추론 시 contrastive prompt guidance로 denoising을 조절한다.

## Observation–State–Action Interface

영상·언어 → 시각 grounding을 보존한 VLA → 지시 조건부 동작.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 시각 보존 손실·guidance 입력·새 지시 split·RL과 SFT의 데이터/비용 차이.

Source가 명시한 evaluation 범위: Simulation과 실제 로봇의 여덟 평가에서 새로운 지시에 대한 일반화를 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 지시쌍에서 기본 정책·후학습·guidance의 효과와 추가 추론 비용을 분리한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2604.23121) · [저자 project/code](https://suninghuang19.github.io/delock_page/). 수식·세부 구현·코드 실행은 미검증이다.
