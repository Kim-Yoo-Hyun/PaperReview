# Diffusion Policy Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Denoising 과정을 policy-gradient 최적화에 포함하고 diffusion policy에 맞춘 학습 설계를 제안한다.

## Observation–State–Action Interface

Observation-conditioned diffusion policy → 연속 action sequence; denoising step과 환경 실행 step은 구분해야 한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 정확한 likelihood 구성, denoising horizon, 실행 chunk와 sim-to-real reset 조건.

Source가 명시한 evaluation 범위: Continuous-control/robotic simulation, pixel/state 입력 및 Furniture-Bench sim-to-real assembly 평가를 project에서 확인했다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 pretrained Diffusion Policy에서 BC 유지와 DPPO를 비교하고, denoising 설정만 바꾸어 성공률·interaction 수·실행 latency를 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html) · [저자 project/code](https://diffusion-ppo.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
