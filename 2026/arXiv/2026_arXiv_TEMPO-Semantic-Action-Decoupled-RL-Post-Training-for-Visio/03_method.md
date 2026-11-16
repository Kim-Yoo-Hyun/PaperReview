# TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM을 동결하고 semantic projection과 action expert를 서로 다른 빈도의 RL 갱신으로 적응한다.

## Observation–State–Action Interface

영상·지시 → 동결 VLM·적응 projection → RL action expert → 로봇 동작.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 학습 task-set·두 학습기의 데이터/gradient 경계·초기 능력·비용 정의.

Source가 명시한 evaluation 범위: CALVIN과 실제 조작 과제에서 후학습 정책·갱신 전략을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 정책·학습 목표에서 uniform update와 모듈별 update를 목표별 성공·비용으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2608.07314) · [저자 project/code](https://anonymous.4open.science/w/tempo-page/). 수식·세부 구현·코드 실행은 미검증이다.
