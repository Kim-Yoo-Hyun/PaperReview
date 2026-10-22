# Learning High-Frequency Continuous Action Chunks in Latent Space

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VAE latent action chunk와 Reuse-then-Refine 실행을 결합한다.

## Observation–State–Action Interface

관측 → latent chunk → 고주파 action decoding·경계 보정.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: controller mode, interpolation baseline, VAE 데이터, refinement timing.

Source가 명시한 evaluation 범위: 실제 contact manipulation과 여러 policy backbone 비교를 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Mode·gain·관측 시간을 고정해 저주파 보간과 learned high-frequency decoding을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v306/wang26lj.html) · [저자 project/code](https://github.com/tars-robotics/RTR). 수식·세부 구현·코드 실행은 미검증이다.
