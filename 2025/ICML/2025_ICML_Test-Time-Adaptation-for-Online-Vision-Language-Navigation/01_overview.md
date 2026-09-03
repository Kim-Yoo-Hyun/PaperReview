# Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=K4GaB4fdIq.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168050. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Vision-Language Model, Navigation, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=K4GaB4fdIq
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/168050
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 navigation 문제를 이해하기 위해 읽는다. 본문은 For example, when the initial navigation fails, entropy minimization intensifies the probabilities of the actions that lead to failure in repeated episodes.를 문제로 두고, In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Navigating in an unfamiliar environment during deployment poses a critical challenge for a vision-language navigation (VLN) agent.
- **p. 1 / Abstract - extractive body cue:** Yet, test-time adaptation (TTA) remains relatively underexplored in robotic navigation, leading us to the fundamental question: what are the key properties of TTA for online ...
- **p. 1 / Abstract - extractive body cue:** In our view, effective adaptation requires three qualities: 1) flexibility in handling different navigation outcomes, 2) interactivity with external environment, and 3) maintaining a harmony ...
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based reinforcement learning.
- **p. 1 / Abstract - extractive body cue:** Specifically, FEEDTTA learns by maximizing binary episodic feedback, a practical setup in which the agent receives a binary scalar after each episode that indicates the ...
- **p. 1 / 1. Introduction - extractive body cue:** For example, when the initial navigation fails, entropy minimization intensifies the probabilities of the actions that lead to failure in repeated episodes.
- **p. 1 / 1. Introduction - extractive body cue:** One existing approach (Gao et al., 2024a) relies on the widely adopted TTA paradigm of entropy minimization (Wang et al., 2020a; Zhang et al., 2022), ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL.
- **p. 2 / 1. Introduction - extractive body cue:** Based on this analysis, we introduce FEEDTTA, a novel TTA framework for online VLN using feedback-based reinforcement learning (RL).
- **p. 3 / 3.1. Task Description - extractive body cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...
- **p. 4 / 3.3. Stochastic Gradient Reversion - extractive body cue:** Therefore, we propose Stochastic Gradient Reversion (SGR), a gradient regularization method for FEEDTTA to maintain plasticity and stability during adaptation.
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive body cue:** This mechanism allows for a more flexible and dynamic adaptation, taking both possible outcomes into consideration rather than limiting updates to a single extreme.
- **p. 3 / 3.2. Binary Episodic Feedback - extractive body cue:** FEEDTTA leverages a Monte Carlo policy gradient algorithm REINFORCE (Williams, 1992) to learn from the received feedback at the end of each navigation episode.
- **p. 4 / 3.2. Binary Episodic Feedback - extractive body cue:** (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient of the policy ...
- **p. 4 / 3.2. Binary Episodic Feedback - extractive body cue:** Here, the parameter update directly depends on the navigation outcome F and the log probability for each selected action, implying that the policy flexibly adopts ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient of the policy πθ is: ∇θJ(θ) ≈Eat,st∼τ "T -1 X ... | camera/depth stream, pose, map와 language goal | p. 4 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description) |
| State/latent | Right, Specifically, among, variants, negative, value, reversion, shifts, original, gradient, closest, counterfactual | robot pose, free-space/semantic map와 local goal | p. 4 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback) |
| Output/action | Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding environment. | collision-free trajectory 또는 velocity command | p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback) |
| Objective/outcome | A general REINFORCE algorithm aims at optimizing the parameter θ of a policy πθ to maximize the score function of the expected return Gt = PT -t i=1 γi-1Rt+i, where R is ... | goal reach, safety, localization error와 replanning latency | p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.3. Stochastic Gradient Reversion), p. 4 (3.3. Stochastic Gradient Reversion) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL.
- **p. 2 / 1. Introduction - extractive body cue:** Based on this analysis, we introduce FEEDTTA, a novel TTA framework for online VLN using feedback-based reinforcement learning (RL).
- **p. 3 / 3.1. Task Description - extractive body cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...
- **p. 4 / 3.3. Stochastic Gradient Reversion - extractive body cue:** Therefore, we propose Stochastic Gradient Reversion (SGR), a gradient regularization method for FEEDTTA to maintain plasticity and stability during adaptation.
- **p. 5 / 3.3. Stochastic Gradient Reversion - extractive body cue:** This mechanism allows for a more flexible and dynamic adaptation, taking both possible outcomes into consideration rather than limiting updates to a single extreme.
- **p. 9 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** Furthermore, while GD and GS exhibit catastrophic forgetting, the proposed SGR rather brings substantial improvements in the success rates, strengthening the policy's generalizability as well ...
- **p. 5 / 4.2. Evaluation Metrics - extractive body cue:** In addition to these metrics, we propose the ‘Adapted Success Rate (ASR)' metric to accurately measure sample-wise transition of results before and after adaptation.
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive body cue:** The performance improves further in proportion to the increase in the percentage of episodes receiving feedback.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 5 (4.2. Evaluation Metrics) |
| Embodiment/environment | For the REVERIE dataset, the results in the paper are obtained with p = 0.01 and α = -0.2 for the validation seen split, and p = 0.05 and α = -0.2 ... | hardware/simulator version and reset protocol | p. 6 (4.3. Implementation Details), p. 9 (5.4. Effects of Stochastic Gradient Reversion) |
| Dataset/benchmark | Specifically, our method improves SR and OSR of DUET up to 41.53% and 40.20% on the validation unseen split, respectively. | role, split, size and leakage | p. 6 (4.3. Implementation Details), p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 6 (5.1. Main Navigation Results), p. 7 (5.2. Quality and Quantity of Feedback) |
| Metric | We follow the standard evaluation protocol from the previous works (Chen et al., 2021; 2022c; Gao et al., 2024a) and report Trajectory Length (TL), Navigation Error (NE), Success Rate (SR), Oracle Success ... | definition, denominator, direction and uncertainty | p. 5 (4.2. Evaluation Metrics), p. 8 (5.3. LLMs as Feedback Oracle), p. 5 (4.2. Evaluation Metrics) |
| Baseline/ablation | For the test unseen split, we utilize LLMs as the feedback oracle due to the unavailability of goal-viewpoint data, yet the results remain promising compared to other baselines in both HAMT and ... | fair input/data/compute/action matching | p. 6 (5.1. Main Navigation Results), p. 6 (5.1. Main Navigation Results), p. 7 (5.2. Quality and Quantity of Feedback) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6. Conclusion - extractive body cue:** The proposed adaptation strategy utilizing binary episodic feedback enables agents to dynamically interact with their external environment by providing them with a notion of success ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the learning paradigm of FEEDTTA. The navigation agent adapts to streaming online test data by learning to maximize the cumulative binary ...
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive body cue:** Feedback accuracies less than 50% leads to obvious adaptation failure.
- **p. 7 / 5.3. LLMs as Feedback Oracle - extractive body cue:** We leverage a two-step LLM architecture for determining the navigation success or failure.
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** Specifically, for both data splits, SGR brings 14.21% and 10.28% improvements in CSR, respectively, indicating the flexibility of FEEDTTA in dealing with failure scenarios.
- **p. 9 / 6. Conclusion - extractive body cue:** Impact Statement Although our FEEDTTA leads significant performance improvements, it does not guarantee perfect prediction across the diverse environment.
- **p. 6 / 4.3. Implementation Details - extractive body cue:** However, FEEDTTA does not require high-end server-grade GPUs and can be efficiently deployed on practical hardware (e.g., GTX 1080).

## Why Read It

RL, IL, offline learning, and robot data의 navigation 문제를 이해하기 위해 읽는다. 본문은 For example, when the initial navigation fails, entropy minimization intensifies the probabilities of the actions that lead to failure in repeated episodes.를 문제로 두고, In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
