# Steering Your Diffusion Policy with Latent Space Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Base diffusion policy의 weight를 고정하고 latent-noise space에서 RL을 수행하는 DSRL을 제안한다.

## Observation–State–Action Interface

Observation → RL latent-noise policy → frozen BC diffusion policy → robot action.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Latent exploration 범위, base policy API, 성공/실패 reward와 reset 비용.

Source가 명시한 evaluation 범위: 공식 CoRL abstract는 simulated benchmark, real-world robot task 및 pretrained generalist policy adaptation 평가를 명시한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Frozen BC, DSRL, 직접 fine-tuning을 동일 초기 policy와 task로 비교하고 새로운 task 개선·기존 task retention·latency를 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v305/wagenmaker25a.html) · [저자 project/code](https://github.com/ajwagen/dsrl). 수식·세부 구현·코드 실행은 미검증이다.
