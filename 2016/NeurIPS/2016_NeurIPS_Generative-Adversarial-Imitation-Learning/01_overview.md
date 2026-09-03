# Generative Adversarial Imitation Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1606.03476.
> PDF retrieval source: https://arxiv.org/pdf/1606.03476. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, Imitation Learning, Reinforcement Learning
- Official paper: https://arxiv.org/abs/1606.03476
- Full-text retrieval: https://arxiv.org/pdf/1606.03476
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 Given that learner's true goal often is to take actions imitating the expert-indeed, many IRL algorithms are evaluated on the quality of the optimal actions of the costs they learn-why, then, must ...를 문제로 두고, We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free imitation learning algorithm that obtains significant performance ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Consider learning a policy from example expert behavior, without interaction with the expert or access to reinforcement signal.
- **p. 1 / Abstract - extractive body cue:** One approach is to recover the expert's cost function with inverse reinforcement learning, then extract a policy from that cost function with reinforcement learning.
- **p. 1 / Abstract - extractive body cue:** This approach is indirect and can be slow.
- **p. 1 / Abstract - extractive body cue:** We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- **p. 1 / Abstract - extractive body cue:** We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free ...
- **p. 1 / 1 Introduction - extractive body cue:** Given that learner's true goal often is to take actions imitating the expert-indeed, many IRL algorithms are evaluated on the quality of the optimal actions ...
- **p. 4 / 2 Background - extractive body cue:** In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free ...
- **p. 1 / 1 Introduction - extractive body cue:** Then, we instantiate our framework in Sections 4 and 5 with a new model-free imitation learning algorithm.
- **p. 3 / 2 Background - extractive body cue:** We explore such algorithms in Sections 4 and 5, where we show that certain settings of ψ lead to both existing algorithms and a novel ...
- **p. 3 / 2 Background - extractive body cue:** The occupancy measure can be interpreted as the distribution of state-action pairs that an agent encounters when navigating the environment with policy π, and it ...
- **p. 4 / 2 Background - extractive body cue:** Keeping in mind that we wish to eventually develop an imitation learning algorithm suitable for large environments, we would like to relax Eq.
- **p. 2 / 1 Introduction - extractive body cue:** networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our algorithm harnesses generative ...
- **p. 4 / 2 Background - extractive body cue:** For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing ...
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** We propose the following new cost regularizer that combines the best of both worlds, as we will show in the coming sections: ψGA(c) ≜ EπE[g(c(s, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | There are two main approaches suitable for this setting: behavioral cloning [20], which learns a policy as a supervised learning problem over state-action pairs from expert trajectories; and inverse reinforcement learning [25, ... | observation history와 expert trajectory/action | p. 1 (1 Introduction), p. 4 (2 Background) |
| State/latent | There, main, approaches, suitable, setting, behavioral, cloning, learns, policy, supervised, learning, problem | behavior policy와 temporal action context | p. 1 (1 Introduction), p. 4 (2 Background), p. 3 (2 Background) |
| Output/action | In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy measure values will be exactly zero, and ... | predicted action 또는 action chunk | p. 4 (2 Background), p. 3 (2 Background), p. 4 (2 Background) |
| Objective/outcome | For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing the objective minimize π max c∈C Eπ[c(s, ... | imitation error, task success, robustness와 compounding error | p. 4 (2 Background), p. 5 (2 Background), p. 2 (2 Background) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free ...
- **p. 1 / 1 Introduction - extractive body cue:** Then, we instantiate our framework in Sections 4 and 5 with a new model-free imitation learning algorithm.
- **p. 3 / 2 Background - extractive body cue:** We explore such algorithms in Sections 4 and 5, where we show that certain settings of ψ lead to both existing algorithms and a novel ...
- **p. 3 / 2 Background - extractive body cue:** The occupancy measure can be interpreted as the distribution of state-action pairs that an agent encounters when navigating the environment with policy π, and it ...
- **p. 4 / 2 Background - extractive body cue:** Keeping in mind that we wish to eventually develop an imitation learning algorithm suitable for large environments, we would like to relax Eq.
- **p. 7 / 6 Experiments - extractive body cue:** Our algorithm almost always achieved at least 70% of expert performance for all dataset 7
- **p. 7 / 6 Experiments - extractive body cue:** We were able to slightly improve our algorithm's performance on Reacher using causal entropy regularization-in the 4-trajectory setting, the improvement from λ = 0 to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 1: Environments Task Observation space Action space Random policy performance Expert performance Cartpole-v0 4 (continuous)

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Embodiment/environment | We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to FEM and GTAL, which for the most part were able ... | hardware/simulator version and reset protocol | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Dataset/benchmark | We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to FEM and GTAL, which for the most part were able ... | role, split, size and leakage | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Metric | The policy is trained with supervised learning, using Adam [12] with minibatches of 128 examples, until validation error stops decreasing. | definition, denominator, direction and uncertainty | p. 7 (6 Experiments), p. 7 (6 Experiments), p. 13 (Figure/Table caption) |
| Baseline/ablation | We tested Algorithm 1 against three baselines: 1. | fair input/data/compute/action matching | p. 7 (6 Experiments), p. 7 (6 Experiments), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** When D cannot distinguish data generated by G from the true data, then G has successfully matched the true data.
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** The indicator regularizers δC, used by the linear apprenticeship learning algorithms described in Section 4, are always fixed, and cannot adapt to data as ψGA ...
- **p. 5 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** This carefully constructed step scheme ensures that divergence does not occur due to high noise in estimating the gradient (12).
- **p. 5 / 2 Background - extractive body cue:** If C does not include a cost function that explains expert behavior well, then attempting to recover a policy from such an encoding will not ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 Given that learner's true goal often is to take actions imitating the expert-indeed, many IRL algorithms are evaluated on the quality of the optimal actions of the costs they learn-why, then, must ...를 문제로 두고, We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free imitation learning algorithm that obtains significant performance ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 4 (2 Background), p. 1 (1 Introduction), p. 2 (2 Background), p. 3 (2 Background), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Inverse reinforcement learning (IRL), on the other hand, learns a cost function that prioritizes entire trajectories over others, so compounding error, a problem for methods that fit single-timestep decisions, is ... (p. 1, 1 Introduction).
- **Actual contribution:** Then, we instantiate our framework in Sections 4 and 5 with a new model-free imitation learning algorithm. (p. 1, 1 Introduction).
- **Evaluation boundary:** We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to FEM and GTAL, which for the most part ... (p. 7, 6 Experiments).
- **Explicit failure boundary:** FEM and GTAL performed poorly for Ant, producing policies consistently worse than a policy that chooses actions uniformly at random. (p. 8, 6 Experiments).
