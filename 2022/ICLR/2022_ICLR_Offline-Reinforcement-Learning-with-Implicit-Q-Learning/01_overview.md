# Offline Reinforcement Learning with Implicit Q-Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=68n2s9ZJWF8.
> PDF retrieval source: https://arxiv.org/pdf/2110.06169. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, offline reinforcement learning, implicit Q-learning, continuous control
- Official paper: https://openreview.net/forum?id=68n2s9ZJWF8
- Full-text retrieval: https://arxiv.org/pdf/2110.06169
- Code/Project: https://github.com/ikostrikov/implicit_q_learning
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 However, this also carries with it major challenges: improving the policy beyond the level of the behavior policy that collected the data requires estimating values for actions other than those that were ...를 문제로 두고, We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve substantially over the best behavior in the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Offline reinforcement learning requires reconciling two conflicting aims: learning a policy that improves over the behavior policy that collected the dataset, while at the same ...
- **p. 1 / ABSTRACT - extractive body cue:** This trade-off is critical, because most current offline reinforcement learning methods need to query the value of unseen actions during training to improve the policy, ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 1 / ABSTRACT - extractive body cue:** The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly ...
- **p. 1 / ABSTRACT - extractive body cue:** This leverages the generalization capacity of the function approximator to estimate the value of the best available action at a given state without ever directly ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this also carries with it major challenges: improving the policy beyond the level of the behavior policy that collected the data requires estimating values ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Offline reinforcement learning (RL) addresses the problem of learning effective policies entirely from previously collected data, without online interaction (Fujimoto et al., 2019; Lange et ...

## Core Idea

- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key idea in our method is to approximate an upper expectile of the distribution over values with respect to the distribution of dataset actions ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** In the following theorems, we show that under certain assumptions, our method indeed approximates the optimal state-action value Q∗and performs multi-step dynamical programming.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** 5 EXPERIMENTAL EVALUATION Our experiments aim to evaluate our method comparatively, in contrast to prior offline RL methods, and in particular to understand how our ...
- **p. 1 / ABSTRACT - extractive body cue:** The main insight in our work is that, instead of evaluating unseen actions from the latest policy, we can approximate the policy improvement step implicitly ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted ...
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Off-policy RL methods based on approximate dynamic programming typically utilize a state-action value function (Q-function), referred to as Q(s, a), which corresponds to the discounted returns obtained by starting from the state ... | dataset state/observation, action, reward와 return-to-go | p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| State/latent | Off-policy, methods, approximate, dynamic, programming, typically, utilize, state-action, value, function, Q-function, referred | Q/value 또는 sequence-policy state | p. 3 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 1 (ABSTRACT) |
| Output/action | When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from the rewarding states too quickly (c). | dataset-supported action sequence | p. 7 (3 PRELIMINARIES), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Objective/outcome | Like many recent offline RL methods, our work builds on approximate dynamic programming methods that minimize temporal difference error, according to the following loss: LT D(θ) = E(s,a,s′)∼D[(r(s, a) + γ max ... | offline policy value, OOD safety와 closed-loop success | p. 3 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 3 (3 PRELIMINARIES) |

## Main Claims and Actual Contribution

- **p. 1 / ABSTRACT - extractive body cue:** We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The key idea in our method is to approximate an upper expectile of the distribution over values with respect to the distribution of dataset actions ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** In the following theorems, we show that under certain assumptions, our method indeed approximates the optimal state-action value Q∗and performs multi-step dynamical programming.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** 5 EXPERIMENTAL EVALUATION Our experiments aim to evaluate our method comparatively, in contrast to prior offline RL methods, and in particular to understand how our ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Online finetuning results showing the initial perfor- mance after offline RL, and performance after 1M steps of on- line RL. In all tasks, ...
- **p. 9 / 3 PRELIMINARIES - extractive body cue:** On the Ant Maze domains, IQL significantly outperforms both prior methods after online finetuning.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Averaged normalized scores on MuJoCo locomotion and Ant Maze tasks. Our method outperforms prior methods on the challenging Ant Maze tasks, which require ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 9 (3 PRELIMINARIES) |
| Embodiment/environment | We will then compare IQL with state-of-theart single-step and multi-step algorithms on the D4RL (Fu et al., 2020) benchmark tasks, studying the degree to which we can learn effective policies using only ... | hardware/simulator version and reset protocol | p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Dataset/benchmark | (4) Our algorithm, implicit Q-Learning (IQL), aims to estimate this objective while evaluating the Qfunction only on the state-action pairs in the dataset. | role, split, size and leakage | p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES) |
| Metric | 1.0 0.5 0.0 0.5 1.0 u 0.0 0.2 0.4 0.6 0.8 1.0 / (u < 0)/u2 = 0.01 = 0.1 = 0.5 = 0.9 = 0.99 2 0 2 x 0.0 0.1 ... | definition, denominator, direction and uncertainty | p. 5 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES), p. 7 (3 PRELIMINARIES) |
| Baseline/ablation | Figure 3: Estimating a larger expectile τ is crucial for antmaze tasks that require dynamical program- ming ('stitching'). Comparisons and baselines. We compare to methods that are representative of both multi- step ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (3 PRELIMINARIES), p. 9 (3 PRELIMINARIES) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3 PRELIMINARIES - extractive body cue:** TD learning (IQL): for each gradient step do ψ ←ψ -λV ∇ψLV (ψ) θ ←θ -λQ∇θLQ(θ) ˆθ ←(1 -α)ˆθ + αθ end for Policy extraction ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** Note that the policy does not influence the value function in any way, and therefore extraction could be performed either concurrently or after TD learning.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** Since IQL (d) performs iterative dynamic programming, it correctly propagates the signal, and the values are no longer dominated by noise.
- **p. 7 / 3 PRELIMINARIES - extractive body cue:** When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function that degrades to zero far from the ...

## Why Read It

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 However, this also carries with it major challenges: improving the policy beyond the level of the behavior policy that collected the data requires estimating values for actions other than those that were ...를 문제로 두고, We propose a new offline RL method that never needs to evaluate actions outside of the dataset, but still enables the learned policy to improve substantially over the best behavior in the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 PRELIMINARIES), p. 1 (ABSTRACT) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, this also carries with it major challenges: improving the policy beyond the level of the behavior policy that collected the data requires estimating values for actions other than those ... (p. 1, 1 INTRODUCTION).
- **Actual contribution:** Our method is easy to implement by making a small change to the loss function in a simple SARSA-like TD update and is computationally very efficient. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Figure 2: Evaluation of our algorithm on a toy umaze environment (a). When the static dataset is heavily corrupted by suboptimal actions, one-step policy evaluation results in a value function ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** Our reproduced results offline are worse than the reported results, particularly on medium and large antmaze environments. (p. 13, C FINETUNING EXPERIMENTAL DETAILS).
