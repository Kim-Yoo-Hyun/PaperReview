# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Method in One Sentence

Outcome reward 기반 VLA RL에 trajectory sampling, parallel rollout/rendering 및 loss 계산 최적화를 결합한다.

## Observation–State–Action Interface

OpenVLA-OFT의 observation/language → action rollout → outcome reward → policy update.

## Pipeline and Optimization Boundary

위 pipeline은 abstract/project에서 확인한 module 연결이다. Exact loss/control law, gradient estimator, optimizer와 hyperparameter는 아직 확인하지 않았다.

## Training vs Inference

학습·추론 구분을 위해 확인할 항목: 실제 robot online training 범위, sparse reward 생성, data leakage 및 compute accounting.

Source가 명시한 evaluation 범위: ICLR abstract는 LIBERO, RoboTwin 1.0/2.0 및 real-world task 결과를 보고한다. Real-world 평가와 실제 online training은 구분해야 한다.

## Temporal and Runtime Contract

Action horizon, denoising/rollout horizon, memory 길이, policy inference rate와 실제 controller rate의 수치 및 관계는 본문에서 별도로 확인한다.

## Method-Specific Comparison — Researcher Interpretation

OFT SFT와 SimpleVLA-RL을 동일 task에서 비교하고 rollout 수·reward access·성공률·기존 task retention을 함께 기록한다.

위 비교는 제안한 실험이며 논문이 수행한 ablation을 뜻하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) · [저자 project/code](https://github.com/PRIME-RL/SimpleVLA-RL). 수식·세부 구현·코드 실행은 미검증이다.
