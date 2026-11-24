# Continuous Control with Deep Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1509.02971.
> PDF retrieval source: https://arxiv.org/pdf/1509.02971. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / ICLR
- Authors: Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, Daan Wierstra
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, continuous control, actor-critic
- Official paper: https://arxiv.org/abs/1509.02971
- Full-text retrieval: https://arxiv.org/pdf/1509.02971
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

DDPG는 결정론적 정책과 행동가치 함수를 함께 학습해 고차원 연속 행동을 제어한다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We adapt the ideas underlying the success of Deep Q-Learning to the continuous action domain.
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 1 / ABSTRACT - extractive body cue:** Using the same learning algorithm, network architecture and hyper-parameters, our algorithm robustly solves more than 20 simulated physics tasks, including classic problems such as cartpole ...
- **p. 1 / ABSTRACT - extractive body cue:** Our algorithm is able to find policies whose performance is competitive with those found by a planning algorithm with full access to the dynamics of ...
- **p. 1 / ABSTRACT - extractive body cue:** We further demonstrate that for many of the tasks the algorithm can learn policies "end-to-end": directly from raw pixel inputs.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such large action spaces are difficult to explore efficiently, and thus successfully training DQN-like networks in this context is likely intractable.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to evaluate our method we constructed a variety of challenging physical control problems that involve complex multi-joint movements, unstable and rich contact dynamics, ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, as we show below, a naive application of this actor-critic method with neural function approximators is unstable for challenging problems.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Our contribution here is to provide modifications to DPG, inspired by the success of DQN, which allow it to use neural network function approximators to ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q ...
- **p. 2 / 2 BACKGROUND - extractive body cue:** We model it as a Markov decision process with a state space S, action space A = IRN, an initial state distribution p(s1), transition dynamics ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A long-standing challenge of robotic control is to learn an action policy directly from raw sensory input such as video. | state 또는 observation, action, reward와 transition history | p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND) |
| State/latent | long-standing, challenge, robotic, control, learn, action, policy, directly, sensory, input, video, agent | policy/value state와 action-selection variable | p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND) |
| Output/action | An agent's behavior is defined by a policy, π, which maps states to a probability distribution over the actions π: S →P(A). | action policy와 induced trajectory | p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND) |
| Critic objective | 원문 대조: Background의 critic loss는 Q(s_t,a_t)와 Bellman target y_t 사이 squared error의 기대값이다. 실제 DDPG에서는 별도 target actor/critic과 soft update를 사용하므로, p. 3의 배경식을 최종 target-network 구현식으로 그대로 옮기지 않는다. ([PDF p. 3](https://arxiv.org/pdf/1509.02971#page=3), §2 Background, Eqs. (4)–(5); §3 p. 4) | Bellman-error regression; 평가 return과 구분 | [PDF p. 3](https://arxiv.org/pdf/1509.02971#page=3), §2 Background, Eqs. (4)–(5); §3 p. 4 |

## Main Claims and Actual Contribution

- 경험 재생을 사용하는 오프폴리시 actor–critic을 구성한다.
- 연속 제어 과제에서 심층 함수 근사를 이용한 학습을 비교한다.

[저자 원문](https://arxiv.org/abs/1509.02971)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 5 (4 RESULTS) |
| Embodiment/environment | We examined DDPG's estimates empirically by comparing the values estimated by Q after training with the true returns seen on test episodes. | hardware/simulator version and reset protocol | p. 6 (4 RESULTS), p. 5 (4 RESULTS) |
| Dataset/benchmark | In order from the left: the cartpole swing-up task, a reaching task, a gasp and move task, a puck-hitting task, a monoped balancing task, two locomotion tasks and Torcs (driving simulator). | role, split, size and leakage | p. 6 (4 RESULTS), p. 5 (4 RESULTS), p. 6 (4 RESULTS), p. 4 (4 RESULTS) |
| Metric | Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are normalized so ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (4 RESULTS), p. 5 (4 RESULTS) |
| Baseline/ablation | We normalized the scores using two baselines. | fair input/data/compute/action matching | p. 5 (4 RESULTS), p. 5 (4 RESULTS), p. 5 (4 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task ...
- **p. 8 / 6 CONCLUSION - extractive body cue:** The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a variety ...
- **p. 5 / 4 RESULTS - extractive body cue:** We evaluated the policy periodically during training by testing it without exploration noise.
- **p. 6 / 4 RESULTS - extractive body cue:** We used an identical network architecture and learning algorithm hyper-parameters to the physics tasks but altered the noise process for exploration because of the very ...
- **p. 6 / 4 RESULTS - extractive body cue:** On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom. (p. 1, 1 INTRODUCTION).
- **Actual contribution:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. (p. 1, 1 INTRODUCTION).
- **Evaluation boundary:** Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though other replicas failed to learn ... (p. 6, 4 RESULTS).

## 배포 범위 대조

- 데이터 — 원문에 학습 또는 제어 실험의 관측·궤적이 있다. 해당 실험의 원시 자료 배포 범위는 미확인이다. [검토 근거](https://arxiv.org/pdf/1509.02971#page=5)
