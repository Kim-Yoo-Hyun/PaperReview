# Reinforcement Learning with Action Chunking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Chunked action space에서 RL을 수행하여 시간적으로 일관된 exploration과 n-step TD backup을 결합한다.

## Observation–State–Action Interface

State → action chunk → 여러 환경 step 실행; critic도 action sequence를 평가한다.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: Chunk 실행 중 feedback 처리, n-step target 조건과 exploration budget.

Source가 명시한 evaluation 범위: 공식 abstract는 long-horizon sparse-reward manipulation task에서 offline 성능과 online sample efficiency를 비교한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

동일 FQL/RLPD 기반에서 single-step과 Q-chunking을 비교하고 chunk 길이에 따른 학습 효율·성공률·외란 후 회복 시간을 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) · [저자 project/code](https://github.com/ColinQiyangLi/qc). 수식·세부 구현·코드 실행은 미검증이다.
