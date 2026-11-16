# LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

구조화된 시각 latent에서 dynamics·policy·forecasting을 공동 학습하고 이질적 데이터를 통합한다.

## Observation–State–Action Interface

비동기 vision·action → multimodal diffusion transformer → 행동·미래 표현.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 저품질 데이터 정의, 데이터 역할별 objective, action/vision rate, 학습 데이터 중복.

Source가 명시한 evaluation 범위: Simulation과 실제 contact-rich·dexterous·long-horizon 조작을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 데이터·backbone·compute에서 action-only와 dynamics 공동 학습 후 동일 RL budget으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p210.html) · [저자 project/code](https://github.com/jiangranlv/LDA-1B). 수식·세부 구현·코드 실행은 미검증이다.
