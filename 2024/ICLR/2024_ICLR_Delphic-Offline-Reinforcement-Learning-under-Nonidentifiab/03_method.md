# Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

관측과 양립하는 world model 간 차이로 confounding 불확실성을 정의하고 보수적 RL에 반영한다.

## Observation–State–Action Interface

offline trajectory → confounding/model uncertainty → pessimistic policy.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 비식별성 가정, uncertainty estimator, pessimism 수준, 의료→로봇 적용 한계.

Source가 명시한 evaluation 범위: Sepsis benchmark와 의료 기록에서 평가하며 robot/VLA 효과를 검증한 논문은 아니다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

숨은 cue가 있는 작은 환경에서 관측 적합도와 counterfactual action ranking을 따로 검사한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html). 수식·세부 구현·코드 실행은 미검증이다.
