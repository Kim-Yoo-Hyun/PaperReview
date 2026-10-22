# EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Stereo fixation 기반 표현과 gaze/행동 제어를 연결한다.

## Observation–State–Action Interface

Stereo 시선·관측 → fixation-relative 표현 → manipulation.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 물리/가상 gaze 경계, stereo calibration, RL/BC supervision, robot 범위.

Source가 명시한 evaluation 범위: Simulation 및 실제 bimanual manipulation을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

Fixed gaze와 adaptive gaze를 같은 실행기·시야 예산으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.03710) · [저자 project/code](https://eyerobot2.github.io/). 수식·세부 구현·코드 실행은 미검증이다.
