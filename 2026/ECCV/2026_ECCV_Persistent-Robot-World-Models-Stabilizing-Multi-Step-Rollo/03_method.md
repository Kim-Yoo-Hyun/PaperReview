# Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

자신이 생성한 history에 conditioning하며 여러 미래 rollout을 비교하는 RL post-training과 multi-view visual fidelity reward를 제안한다.

## Observation–State–Action Interface

Robot action + predicted video history → future multi-view video; 최적화 대상은 robot policy가 아니라 world model이다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Reward metric의 geometry/contact 민감도, rollout horizon, 실제 robot policy evidence 유무.

Source가 명시한 evaluation 범위: 공식 abstract/project는 DROID에서 LPIPS/SSIM/PSNR 기반 rollout fidelity와 human preference 평가를 설명한다. Downstream policy improvement는 별도 검증 대상이다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 Ctrl-World backbone의 전후 checkpoint에서 video fidelity와 action-outcome ranking을 함께 평가하고 두 지표의 상관을 확인한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2603.25685) · [저자 project/code](https://jaibardhan.com/persistworld/). 수식·세부 구현·코드 실행은 미검증이다.
