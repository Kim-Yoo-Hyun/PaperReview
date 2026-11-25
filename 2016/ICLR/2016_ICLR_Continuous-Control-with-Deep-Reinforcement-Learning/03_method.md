# Method - Continuous Control with Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1509.02971; PDF retrieval source: https://arxiv.org/pdf/1509.02971. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q network prior to the action ...

## Method Body Digest

- **p. 4 / 2 BACKGROUND - extractive body cue:** In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- **p. 2 / 2 BACKGROUND - extractive body cue:** We model it as a Markov decision process with a state space S, action space A = IRN, an initial state distribution p(s1), transition dynamics ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** The DPG algorithm maintains a parameterized actor function µ(s/θµ) which specifies the current policy by deterministically mapping states to a specific action.
- **p. 3 / 2 BACKGROUND - extractive body cue:** 3 ALGORITHM It is not possible to straightforwardly apply Q-learning to continuous action spaces, because in continuous spaces finding the greedy policy requires an optimization ...
- **원문 대조:** Background의 critic loss는 Q(s_t,a_t)와 Bellman target y_t 사이 squared error의 기대값이다. 실제 DDPG에서는 별도 target actor/critic과 soft update를 사용하므로, p. 3의 배경식을 최종 target-network 구현식으로 그대로 옮기지 않는다. ([PDF p. 3](https://arxiv.org/pdf/1509.02971#page=3), §2 Background, Eqs. (4)–(5); §3 p. 4).

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to evaluate our method we constructed a variety of challenging physical control problems that involve complex multi-joint movements, unstable and rich contact dynamics, ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.

## Source Evidence Cues

- **p. 4 / 2 BACKGROUND - extractive body cue:** In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- **p. 2 / 2 BACKGROUND - extractive body cue:** We model it as a Markov decision process with a state space S, action space A = IRN, an initial state distribution p(s1), transition dynamics ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** The DPG algorithm maintains a parameterized actor function µ(s/θµ) which specifies the current policy by deterministically mapping states to a specific action.
- **p. 3 / 2 BACKGROUND - extractive body cue:** 3 ALGORITHM It is not possible to straightforwardly apply Q-learning to continuous action spaces, because in continuous spaces finding the greedy policy requires an optimization ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Policy / value representation | state에서 action과 return estimate를 표현한다 | state/observation과 task context | actor, critic, value, Q 또는 sequence policy를 계산 | policy/value estimate | In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers ... | p. 4 (2 BACKGROUND), p. 1 (ABSTRACT) |
| Rollout / target construction | interaction에서 update target을 만든다 | state, action, reward, next state | return, advantage, TD target 또는 trajectory statistics를 구성 | training target | We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces. | p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION) |
| Policy / value update | 목표를 최적화해 다음 policy를 만든다 | target, replay/data와 parameters | gradient, trust region, entropy, replay 또는 constraint update를 수행 | updated policy/controller | In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action ... | p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** Background의 critic loss는 Q(s_t,a_t)와 Bellman target y_t 사이 squared error의 기대값이다. 실제 DDPG에서는 별도 target actor/critic과 soft update를 사용하므로, p. 3의 배경식을 최종 target-network 구현식으로 그대로 옮기지 않는다. ([PDF p. 3](https://arxiv.org/pdf/1509.02971#page=3), §2 Background, Eqs. (4)–(5); §3 p. 4).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** DQN cannot be straightforwardly applied to continuous domains since it relies on a finding the action that maximizes the action-value function, which in the continuous ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** DQN is able to learn value functions using such function approximators in a stable and robust way due to two innovations: 1. the network is ...
- **p. 2 / 2 BACKGROUND - extractive body cue:** The return from a state is defined as the sum of discounted future reward Rt = PT i=t γ(i-t)r(si, ai) with a discounting factor γ ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** Since the network Q(s, a/θQ) being updated is also used in calculating the target value (equation 5), the Q update is prone to divergence.
- **p. 3 / 2 BACKGROUND - extractive body cue:** NFQCA (Hafner & Riedmiller, 2011), which uses the same update rules as DPG but with neural network function approximators, uses batch learning for stability, which ...
- **Formal bridge:** s_t/o_t -> a_t sampled or selected by πθ -> expected return / constrained return -> task return, success and safe execution.
- **Equation/algorithm anchors:** p. 4 (2 BACKGROUND), p. 1 (ABSTRACT), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | long-standing, challenge, robotic, control, learn, action, policy, directly, sensory, input, video, agent, behavior, defined | state 또는 observation, action, reward와 transition history | body cue; exact tensor/frame verify |
| State/latent | long-standing, challenge, robotic, control, learn, action, policy, directly, sensory, input | policy/value state와 action-selection variable | body cue; notation verify |
| Action/output | present, model-free, off-policy, actor-critic, algorithm, deep, function, approximators, learn, policies | action policy와 induced trajectory | body cue; unit/decoder verify |
| Objective/constraint | consider, function, approximators, parameterized, optimize, minimizing, loss, Est, where, DQN | expected return / constrained return | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** A long-standing challenge of robotic control is to learn an action policy directly from raw sensory input such as video.
- **p. 2 / 2 BACKGROUND - extractive body cue:** An agent's behavior is defined by a policy, π, which maps states to a probability distribution over the actions π: S →P(A).
- **p. 3 / 2 BACKGROUND - extractive body cue:** The DPG algorithm maintains a parameterized actor function µ(s/θµ) which specifies the current policy by deterministically mapping states to a specific action.
- **p. 4 / 2 BACKGROUND - extractive body cue:** In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Recently, significant progress has been made by combining advances in deep learning for sensory processing (Krizhevsky et al., 2012) with reinforcement learning, resulting in the ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, while DQN solves problems with high-dimensional observation spaces, it can only handle discrete and low-dimensional action spaces.
- **p. 3 / 2 BACKGROUND - extractive body cue:** 2In practice, as in commonly done in policy gradient implementations, we ignored the discount in the statevisitation distribution ρβ.
- **Normalized interface:** observation=state 또는 observation, action, reward와 transition history; state=policy/value state와 action-selection variable; output/action=action policy와 induced trajectory.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | rollout/return horizon과 episode termination; exact n-step/discount는 exact value was not selected from the PDF body. | At each timestep t the agent receives an observation xt, takes an action at and receives a scalar reward rt. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 environment step이 분리되며 deployment control rate는 별도 contract다. | We consider a standard reinforcement learning setup consisting of an agent interacting with an environment E in discrete timesteps. | Hz/fps, inference time and control rate |
| Memory | replay/rollout buffer와 actor/critic parameters; recurrent history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment interaction, value/policy update와 batch size가 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 2 BACKGROUND - extractive body cue:** 3 ALGORITHM It is not possible to straightforwardly apply Q-learning to continuous action spaces, because in continuous spaces finding the greedy policy requires an optimization ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** Additionally, to make efficient use of hardware optimizations, it is essential to learn in minibatches, rather than online.

## Method-Specific Formal Details

- **Body-defined terms:** low-dimensional, case, batch, normalization, state, input, layers, network, prior, action, details, networks, given, supplementary, material, present, actor-critic, model-free, algorithm, deterministic.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Policy / value representation | We examined DDPG's estimates empirically by comparing the values estimated by Q after training with the true returns seen on test episodes. | p. 6 (4 RESULTS), p. 5 (4 RESULTS) |
| Rollout / target construction | We normalized the scores using two baselines. | p. 5 (4 RESULTS), p. 5 (4 RESULTS) |
| Policy / value update | Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed ... | p. 7 (Figure/Table caption), p. 5 (4 RESULTS) |

## Failure and Ablation Link

- **p. 5 / 4 RESULTS - extractive body cue:** We also report results with components of our algorithm (i.e. the target network or batch normalization) removed.
- **p. 5 / 4 RESULTS - extractive body cue:** We evaluated the policy periodically during training by testing it without exploration noise.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Performance curves for a selection of domains using variants of DPG: original DPG algorithm (minibatch NFQCA) with batch normalization (light grey), with target ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task ...
- **p. 8 / 6 CONCLUSION - extractive body cue:** The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a variety ...
- **p. 6 / 4 RESULTS - extractive body cue:** We used an identical network architecture and learning algorithm hyper-parameters to the physics tasks but altered the noise process for exploration because of the very ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (2 BACKGROUND), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), objective p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), temporal p. 2 (2 BACKGROUND), p. 2 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (4 RESULTS), p. 1 (1 INTRODUCTION).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The DPG algorithm maintains a parameterized actor function µ(s/θµ) which specifies the current policy by deterministically mapping states to a specific action. (p. 3, 2 BACKGROUND).
- **원문 대조:** Background의 critic loss는 Q(s_t,a_t)와 Bellman target y_t 사이 squared error의 기대값이다. 실제 DDPG에서는 별도 target actor/critic과 soft update를 사용하므로, p. 3의 배경식을 최종 target-network 구현식으로 그대로 옮기지 않는다. ([PDF p. 3](https://arxiv.org/pdf/1509.02971#page=3), §2 Background, Eqs. (4)–(5); §3 p. 4).
- **Temporal/runtime evidence:** DQN cannot be straightforwardly applied to continuous domains since it relies on a finding the action that maximizes the action-value function, which in the continuous valued case requires an iterative ... (p. 1, 1 INTRODUCTION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
