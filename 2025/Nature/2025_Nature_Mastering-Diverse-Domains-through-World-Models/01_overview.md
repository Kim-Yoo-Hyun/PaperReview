# Mastering Diverse Domains through World Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2301.04104.
> PDF retrieval source: https://arxiv.org/pdf/2301.04104. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / Nature
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, generalist reinforcement learning, latent imagination
- Official paper: https://arxiv.org/abs/2301.04104
- Full-text retrieval: https://arxiv.org/pdf/2301.04104
- Code/Project: https://danijar.com/project/dreamerv3/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (40 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human data has been widely recognized as a ...를 문제로 두고, We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Developing a general algorithm that learns to solve tasks across a wide range of applications has been a fundamental challenge in artificial intelligence.
- **p. 1 / Abstract - extractive body cue:** Although current reinforcement learning algorithms can be readily applied to tasks similar to what they have been developed for, configuring them for new application domains ...
- **p. 1 / Abstract - extractive body cue:** We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration.
- **p. 1 / Abstract - extractive body cue:** Dreamer learns a model of the environment and improves its behavior by imagining future scenarios.
- **p. 1 / Abstract - extractive body cue:** Robustness techniques based on normalization, balancing, and transformations enable stable learning across domains.
- **p. 3 / Abstract - extractive body cue:** The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human ...
- **p. 2 / Abstract - extractive body cue:** This brittleness poses a bottleneck in applying reinforcement learning to new problems and also limits the applicability of reinforcement learning to computationally expensive models or ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration.
- **p. 2 / Abstract - extractive body cue:** We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning readily ...
- **p. 3 / Abstract - extractive body cue:** Learning algorithm We present the third generation of the Dreamer algorithm21,22.
- **p. 3 / Abstract - extractive body cue:** The algorithm consists of three neural networks: the world model predicts the outcomes of potential actions, the critic judges the value of each outcome, and ...
- **p. 1 / Abstract - extractive body cue:** Our work allows solving challenging control problems without extensive experimentation, making reinforcement learning broadly applicable.
- **p. 4 / Abstract - extractive body cue:** The world model learns an understanding of the underlying structure of each environment. ht and zt forms the model state from which we predict rewards ...
- **p. 3 / Abstract - extractive body cue:** Then, a sequence model with recurrent state ht predicts the sequence of these representations given past actions at-1.
- **p. 6 / Abstract - extractive body cue:** The critic replay loss uses the imagination returns Rλ t at the start states of the imagination rollouts as on-policy value annotations for the replay ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The world model encodes sensory inputs into discrete representations zt that are predicted by a sequence model with recurrent state ht given actions at. | observation, uncertainty/risk estimate와 task command | p. 3 (Abstract), p. 5 (Abstract) |
| State/latent | world, model, encodes, sensory, inputs, discrete, representations, predicted, sequence, recurrent, state, given | safe set, recovery state 또는 constraint margin | p. 3 (Abstract), p. 5 (Abstract), p. 2 (Abstract) |
| Output/action | To consider rewards beyond the prediction horizon T = 16, the critic learns to approximate the distribution of returns28 for each state under the current actor behavior: Actor: at ∼πθ(at / st) ... | shielded, recovery 또는 safe action | p. 5 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |
| Objective/outcome | Given a sequence batch of inputs x1:T, actions a1:T, rewards r1:T, and continuation flags c1:T, the world model parameters ϕ are optimized end-to-end to minimize the prediction loss Lpred, the dynamics loss ... | task return과 violation/failure probability | p. 4 (Abstract), p. 7 (Abstract), p. 6 (Abstract) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration.
- **p. 2 / Abstract - extractive body cue:** We present Dreamer, a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters, making reinforcement learning readily ...
- **p. 3 / Abstract - extractive body cue:** Learning algorithm We present the third generation of the Dreamer algorithm21,22.
- **p. 3 / Abstract - extractive body cue:** The algorithm consists of three neural networks: the world model predicts the outcomes of potential actions, the critic judges the value of each outcome, and ...
- **p. 1 / Abstract - extractive body cue:** Our work allows solving challenging control problems without extensive experimentation, making reinforcement learning broadly applicable.
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 9: Item success rates as a percentage of episodes. Dreamer obtains items at substantially higher rates than the baselines and continues to improve until ...
- **p. 2 / Abstract - extractive body cue:** Notably, larger model sizes not only achieve higher scores but also require less interaction to solve a task.
- **p. 2 / Abstract - extractive body cue:** Although intuitively appealing, robustly learning and leveraging world models to achieve strong task performance has been an open problem17.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 24 (Figure/Table caption), p. 2 (Abstract) |
| Embodiment/environment | Dreamer sets a new state-of-the-art on this benchmark, outperforming D4PG, DMPO, and MPO33. • Visual Control This benchmark consists of 20 continuous control tasks where the agent receives only high-dimensional images as ... | hardware/simulator version and reset protocol | p. 9 (Abstract), p. 9 (Abstract) |
| Dataset/benchmark | 0 300 600 900 PPO Rainbow MuZero Dreamer 57 tasks, 200M steps Atari 10 30 50 70 PPO Rainbow PPG Dreamer 16 tasks, 50M steps ProcGen 10 30 50 70 PPO R2D2+ ... | role, split, size and leakage | p. 9 (Abstract), p. 9 (Abstract), p. 1 (Abstract), p. 2 (Abstract) |
| Metric | Figure 16: BSuite scores visualized by category48. Dreamer exceeds previous methods in the categories scale and memory. The scale category measure robustness to reward scales. 37 | definition, denominator, direction and uncertainty | p. 37 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (Abstract) |
| Baseline/ablation | Dreamer establishes a new state-of-the-art on this benchmark, outperforming DrQ-v2 and CURL47, which are specialized to visual environments and leverage data augmentation. | fair input/data/compute/action matching | p. 9 (Abstract), p. 9 (Abstract), p. 10 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Abstract - extractive body cue:** Importantly, the network can output any continuous value in the interval because the weighted average can fall between the buckets: ˆy .= softmax(f(x))TB B .= ...
- **p. 6 / Abstract - extractive body cue:** In practice, substracting an offset from the returns does not change the actor gradient and thus dividing by the range S is sufficient.
- **p. 7 / Abstract - extractive body cue:** The symlog function approximates the identity around the origin so that it does not affect learning of targets that are already small enough.
- **p. 11 / Abstract - extractive body cue:** In comparison, Dreamer masters a diverse range of environments with fixed hyperparameters, does not require expert data, and its implementation is open source.
- **p. 1 / Abstract - extractive body cue:** Robustness techniques based on normalization, balancing, and transformations enable stable learning across domains.
- **p. 2 / Abstract - extractive body cue:** Dreamer overcomes this challenge through a range of robustness techniques based on normalization, balancing, and transformations.
- **p. 2 / Abstract - extractive body cue:** Although intuitively appealing, robustly learning and leveraging world models to achieve strong task performance has been an open problem17.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 The actor and critic predict actions at and values vt and learn from trajectories of abstract representations predicted by the world model. problem without human data has been widely recognized as a ...를 문제로 두고, We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
