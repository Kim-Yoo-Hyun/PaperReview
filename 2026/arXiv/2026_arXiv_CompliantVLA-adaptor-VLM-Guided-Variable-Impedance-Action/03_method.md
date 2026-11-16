# CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

VLM이 task context에 따른 impedance를 정하고 실시간 force/torque feedback으로 조절한다.

## Observation–State–Action Interface

이미지·언어 → stiffness/damping; force feedback → controller 보정.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Prompt와 controller 설정 비용, force threshold, release 범위.

Source가 명시한 evaluation 범위: Simulation과 실제 접촉 과제에서 성공률·force violation을 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 VLA checkpoint에서 fixed gain·context/force rule·joint RL을 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2601.15541) · [저자 project/code](https://sites.google.com/view/compliantvla). 수식·세부 구현·코드 실행은 미검증이다.
