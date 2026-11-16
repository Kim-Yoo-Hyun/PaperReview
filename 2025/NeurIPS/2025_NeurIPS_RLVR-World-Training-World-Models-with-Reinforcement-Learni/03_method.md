# RLVR-World: Training World Models with Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Decoded prediction의 검증 가능한 지표를 reward로 삼아 world model을 RL 후학습한다.

## Observation–State–Action Interface

Action-conditioned state prediction → decoded metric reward → world model update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: reward metric과 task 목표 정합성, planner의 model exploitation, 로봇 행동 평가 유무.

Source가 명시한 evaluation 범위: 언어·영상 world model의 여러 도메인을 평가한다. RT-1 로봇 영상의 예측 품질을 로봇 제어 성공으로 해석하지 않는다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

같은 planner·rollout budget에 MLE/RL world model을 각각 넣고 예측 지표와 실제 return을 함께 측정한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · [저자 project/code](https://thuml.github.io/RLVR-World/) · [공식 code](https://github.com/thuml/RLVR-World). 수식·세부 구현·코드 실행은 미검증이다.
