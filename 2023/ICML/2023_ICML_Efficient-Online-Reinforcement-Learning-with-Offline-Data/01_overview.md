# Efficient Online Reinforcement Learning with Offline Data

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v202/ball23a.html.
> PDF retrieval source: https://proceedings.mlr.press/v202/ball23a/ball23a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Reinforcement Learning, offline RL, online RL, robot data, sample efficiency
- Official paper: https://proceedings.mlr.press/v202/ball23a.html
- Full-text retrieval: https://proceedings.mlr.press/v202/ball23a/ball23a.pdf
- Code/Project: https://github.com/ikostrikov/rlpd
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 While the individual ingredients of RLPD are refreshingly simple modifications on existing RL components, we show that their combination delivers state-of-the-art performance on a number of popular online RL with offline data ...를 문제로 두고, First, we propose a simple mechanism for incorporating the prior data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Sample efficiency and exploration remain major challenges in online reinforcement learning (RL).
- **p. 1 / Abstract - extractive body cue:** A powerful approach that can be applied to address these issues is the inclusion of offline data, such as prior trajectories from a human expert ...
- **p. 1 / Abstract - extractive body cue:** Previous methods have relied on extensive modifications and additional complexity to ensure the effective use of this data.
- **p. 1 / Abstract - extractive body cue:** Instead, we ask: can we simply apply existing off-policy methods to leverage offline data when learning online?
- **p. 1 / Abstract - extractive body cue:** In this work, we demonstrate that the answer is yes; however, a set of minimal but important changes to existing off-policy RL algorithms are required ...
- **p. 2 / 1. Introduction - extractive body cue:** While the individual ingredients of RLPD are refreshingly simple modifications on existing RL components, we show that their combination delivers state-of-the-art performance on a number ...
- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.

## Core Idea

- **p. 3 / 4. Online RL with Offline Data - extractive body cue:** First, we propose a simple mechanism for incorporating the prior data.
- **p. 3 / 4. Online RL with Offline Data - extractive body cue:** To this end, we present an approach based on off-policy model-free RL, without pre-training or explicit constraints, which we call RLPD (Reinforcement Learning with Prior ...
- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach, RLPD, extends standard off-policy RL and achieves reliable state-of-the-art online performance on a number of tasks using offline data.
- **p. 2 / 1. Introduction - extractive body cue:** We show that online off-policy RL algorithms can be remarkably effective at learning with offline data.
- **p. 5 / 4.4. Per-Environment Design Choices - extractive body cue:** 3: Determine number of Critic targets to subset Z ∈{1, 2} 4: Initialize empty replay buffer R 5: Initialize buffer D with offline data 6: ...
- **p. 6 / 4. Does the proposed workflow around environment - extractive body cue:** To isolate the effect of the utilization of offline data, we use the same architecture and policy optimizer as our method and label this baseline ...
- **p. 6 / 4. Does the proposed workflow around environment - extractive body cue:** For evaluation, we first include SACfD, a baseline studied in prior work (Veˇcer´ık et al., 2017; Nair et al., 2020), which, similar to RLPD, is ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This in turn does not discourage the policy from exploring unknown and potentially valuable regions of the state-action space. | dataset state/observation, action, reward와 return-to-go | p. 4 (4. Online RL with Offline Data), p. 5 (4.4. Per-Environment Design Choices) |
| State/latent | turn, does, discourage, policy, exploring, unknown, potentially, valuable, regions, state-action, space, Determine | Q/value 또는 sequence-policy state | p. 4 (4. Online RL with Offline Data), p. 5 (4.4. Per-Environment Design Choices), p. 3 (3. Preliminaries) |
| Output/action | 3: Determine number of Critic targets to subset Z ∈{1, 2} 4: Initialize empty replay buffer R 5: Initialize buffer D with offline data 6: while True do 7: Receive initial observation ... | dataset-supported action sequence | p. 5 (4.4. Per-Environment Design Choices), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| Objective/outcome | 3: Determine number of Critic targets to subset Z ∈{1, 2} 4: Initialize empty replay buffer R 5: Initialize buffer D with offline data 6: while True do 7: Receive initial observation ... | offline policy value, OOD safety와 closed-loop success | p. 5 (4.4. Per-Environment Design Choices), p. 4 (4.4. Per-Environment Design Choices), p. 3 (3. Preliminaries) |

## Main Claims and Actual Contribution

- **p. 3 / 4. Online RL with Offline Data - extractive body cue:** First, we propose a simple mechanism for incorporating the prior data.
- **p. 3 / 4. Online RL with Offline Data - extractive body cue:** To this end, we present an approach based on off-policy model-free RL, without pre-training or explicit constraints, which we call RLPD (Reinforcement Learning with Prior ...
- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach, RLPD, extends standard off-policy RL and achieves reliable state-of-the-art online performance on a number of tasks using offline data.
- **p. 2 / 1. Introduction - extractive body cue:** We show that online off-policy RL algorithms can be remarkably effective at learning with offline data.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. LayerNorm is crucial for strong performance, particu- larly when data are limited or narrowly distributed. results in collapsed performance, with no progress made ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches already ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Using SAC with our symmetric sampling method can result in instabilities due to diverging Q-values; with LayerNorm in the critic this disappears, improving ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Embodiment/environment | To more clearly illustrate this effect, we construct a dataset of only the expert human demonstration data from the Adroit Sparse tasks (see "Expert Adroit Sparse Tasks" in Figure 7). | hardware/simulator version and reset protocol | p. 7 (5.1. RLPD Analysis and Ablation Study), p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Dataset/benchmark | To more clearly illustrate this effect, we construct a dataset of only the expert human demonstration data from the Adroit Sparse tasks (see "Expert Adroit Sparse Tasks" in Figure 7). | role, split, size and leakage | p. 7 (5.1. RLPD Analysis and Ablation Study), p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Metric | Figure 21. Visualizations of the environments we consider. We provide further details about the key domains we evaluate on. In Figure 21 we provide visualizations of the environments. Sparse Adroit In these ... | definition, denominator, direction and uncertainty | p. 17 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Baseline/ablation | Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches already achieve strong results in this domain. Notably, ... | fair input/data/compute/action matching | p. 15 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10. Symmetric sampling improves sample efficiency and reduces variance across seeds, and does not work by simply in- creasing the reward density in a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. In general, critic ensembling provides the best perfor- mance. Dropout performs worse in sparse reward tasks. In Figure 9, we see that ensembling ...

## Why Read It

RL, IL, offline learning, and robot data의 offline_rl 문제를 이해하기 위해 읽는다. 본문은 While the individual ingredients of RLPD are refreshingly simple modifications on existing RL components, we show that their combination delivers state-of-the-art performance on a number of popular online RL with offline data ...를 문제로 두고, First, we propose a simple mechanism for incorporating the prior data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 5 (4.4. Per-Environment Design Choices) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
