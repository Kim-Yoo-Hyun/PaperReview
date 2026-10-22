# When would Vision-Proprioception Policies Fail in Robotic Manipulation?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Motion-transition phase에 따라 proprioception gradient를 조정하는 GAP을 제안한다.

## Observation–State–Action Interface

영상·proprioception → manipulation action; 학습 중 phase-guided gradient 조정.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: phase 추정 신호, task split, native Octo 코드·checkpoint.

Source가 명시한 evaluation 범위: Simulation·실제 single/dual-arm 및 Octo 적용을 보고한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 데이터에서 GAP와 corruption augmentation을 hidden-fault holdout으로 비교한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) · [저자 project/code](https://gewu-lab.github.io/GAP/). 수식·세부 구현·코드 실행은 미검증이다.
