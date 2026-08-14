# Insights — Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> Evidence maturity: `UNREAD`. 이 문서는 읽기 위치와 검증 질문을 정리한 curation note이며, 정독 완료를 뜻하지 않는다.

## Why CORE

이 논문은 **RL, IL, and policy learning foundations**에서 data distribution, policy objective, value/sequence/generative action interface를 비교하기 위한 robot-learning 기반로 선정됐다.

## Captured Source Cues — Not Yet Independently Verified

- Problem cue: However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning.
- Method cue: In this paper, we propose soft actor-critic, an offpolicy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework.
- Result/evaluation cue: By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy ...

위 cue는 기존 official abstract 또는 local text extraction에서 보존한 것이다. 수치·조건·인과적 해석은 full-text 정독 전까지 `UNVERIFIED`다.

## Dependency Position

`Proximal Policy Optimization Algorithms → Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor → Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World`

이 화살표는 reading dependency다. 직접 citation 관계는 references와 related work를 확인한 뒤 synthesis 문서에만 확정한다.

## Close-Reading Checklist

- learning setting, objective, policy/value representation, data source, interaction budget, generalization split, optimization failure
- 논문이 고정한 가정과 실제 deployment에서 깨질 조건
- strongest baseline과 공정한 비교가 성립하는 조건
- negative result, failure case, compute/data/hardware dependency

## Research Use

- 성능 향상이 objective, data coverage, architecture 중 어디에서 오는지 분리한다.
- 연결 gap: `G-06 / G-08 / G-12` in [RESEARCH_GAPS.md](../../../research/RESEARCH_GAPS.md)

## Minimal Reproduction

동일 observation/action/data split에서 objective만 바꾸고 success, OOD degradation와 calibration을 비교한다.

## Promotion Rule

`READ`로 올리려면 method/evaluation 필드를 채우고, `SYNTHESIZED`로 올리려면 같은 track의 선행·후속 논문과 comparison matrix를 갱신한다.
