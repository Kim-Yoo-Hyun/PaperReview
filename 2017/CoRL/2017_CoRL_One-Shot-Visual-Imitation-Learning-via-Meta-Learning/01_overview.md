# One-Shot Visual Imitation Learning via Meta-Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=0.833); canonical paper source: https://arxiv.org/abs/1703.07326.
> PDF retrieval source: https://arxiv.org/pdf/1703.07326. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, meta-learning, visual manipulation
- Official paper: https://arxiv.org/abs/1703.07326
- Full-text retrieval: https://arxiv.org/pdf/1703.07326
- Code/Project: https://arxiv.org/abs/1703.07326
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=0.833)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges.를 문제로 두고, In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitation learning has been commonly applied to solve different tasks in isolation.
- **p. 1 / Abstract - extractive body cue:** This usually requires either careful feature engineering, or a significant number of samples.
- **p. 1 / Abstract - extractive body cue:** This is far from what we desire: ideally, robots should be able to learn from very few demonstrations of any given task, and instantly generalize ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- **p. 1 / Abstract - extractive body cue:** Specifically, we consider the setting where there is a very large (maybe infinite) set of tasks, and each task has many instantiations.
- **p. 1 / 1 Introduction - extractive body cue:** Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges.
- **p. 2 / 1 Introduction - extractive body cue:** And second, there are many tasks that are extremely difficult to explain in words, even if we assume perfect linguistic abilities: for example, explaining how ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- **p. 5 / B C - extractive body cue:** The memory content to be extracted consists of the coordinates of each block, concatenated with the input embedding.
- **p. 3 / 1 Introduction - extractive body cue:** In particular, on a family of block stacking tasks, our neural network policy was able to perform well on novel block configurations which were not ...
- **p. 1 / Abstract - extractive body cue:** Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.
- **p. 5 / B C - extractive body cue:** Intuitively, this operation allows each block to query other blocks in relation to itself (e.g. find the closest block), and extract the queried information.
- **p. 2 / 1 Introduction - extractive body cue:** (a) Traditional Imitation Learning Task A e.g. stack blocks into towers of height 3 Many demonstrations Imitation Learning Algorithm Policy for task A action Environment ...
- **p. 6 / B C - extractive body cue:** We then apply standard soft attention over the current state to produce fixed-dimensional vectors, where the memory content only consists of positions of each block, ...
- **p. 1 / Abstract - extractive body cue:** A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the second demonstration, it ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | When conditioned on both the first demonstration and this observation, the network is trained to output the corresponding action. systems are not yet at a level where we could easily use language ... | observation history와 expert trajectory/action | p. 2 (1 Introduction), p. 1 (Abstract) |
| State/latent | When, conditioned, first, demonstration, observation, network, trained, output, corresponding, action, systems, level | behavior policy와 temporal action context | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | A neural net is trained such that when it takes as input the first demonstration demonstration and a state sampled from the second demonstration, it should predict the action corresponding to the ... | predicted action 또는 action chunk | p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (B C) |
| Objective/outcome | 1, where the objective is to maximize the expected performance of the learned policy when faced with a new, previously unseen, task, and having received as input only one demonstration of that ... | imitation error, task success, robustness와 compounding error | p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.
- **p. 5 / B C - extractive body cue:** The memory content to be extracted consists of the coordinates of each block, concatenated with the input embedding.
- **p. 3 / 1 Introduction - extractive body cue:** In particular, on a family of block stacking tasks, our neural network policy was able to perform well on novel block configurations which were not ...
- **p. 1 / Abstract - extractive body cue:** Our experiments show that the use of soft attention allows the model to generalize to conditions and tasks unseen in the training data.
- **p. 5 / B C - extractive body cue:** Intuitively, this operation allows each block to query other blocks in relation to itself (e.g. find the closest block), and extract the queried information.
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 2: Success rates of different architectures for particle reaching. The "Train" curves show the success rates when conditioned on demonstrations seen during training, and ...
- **p. 7 / 5 Experiments - extractive body cue:** 2 4 5 6 7 8 Number of Stages 0% 20% 40% 60% 80% 100% Average Success Rate Policy Type Demo BC DAGGER Snapshot Final ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of different conditioning strategies. The darkest bar shows the performance of the hard-coded policy, which unsurprisingly performs the best most of the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 14 (Figure/Table caption), p. 7 (5 Experiments) |
| Embodiment/environment | We conduct experiments with the block stacking tasks described in Section 3.2.2 These experiments are designed to answer the following questions: • How does training with behavioral cloning compare with DAGGER? • ... | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | However, a full trajectory, one which contains information about intermediate stages of the task's solution, can make it easier to train the optimal policy, because it could learn to rely on the ... | role, split, size and leakage | p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Metric | 2 4 5 6 7 8 Number of Stages 0% 20% 40% 60% 80% 100% Average Success Rate Policy Type Demo BC DAGGER Snapshot Final state (b) Performance on test tasks. | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 14 (Figure/Table caption) |
| Baseline/ablation | This assumes that a segmentation of the demonstration into multiple stages is available at test time, which gives it an unfair advantage compared to the other conditioning strategies. | fair input/data/compute/action matching | p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 19 / Figure/Table caption - extractive body cue:** Figure 6: Breakdown of the success and failure scenarios. The area that each color occupies represent the ratio of the corresponding scenario. B.5 Learning Curves ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 8: Breakdown of success and failure scenarios for DAGGER policy. 10
- **p. 22 / Figure/Table caption - extractive body cue:** Table 6: Success rates of a set of tasks that are equivalent up to permutations, using the DAGGER policy conditioned on full trajectories. #Stages Success ...
- **p. 7 / 5 Experiments - extractive body cue:** In fact, even our scripted policy frequently fails on the hardest tasks.
- **p. 6 / B C - extractive body cue:** We leave this possibility for future work.
- **p. 6 / B C - extractive body cue:** It processes both the current state and the embedding produced by the demonstration network, and outputs a context embedding, whose dimension does not depend on ...
- **p. 8 / 5 Experiments - extractive body cue:** There are a lot of exciting directions for future work.

## Why Read It

Manipulation, contact, tactile, and dexterity의 il 문제를 이해하기 위해 읽는다. 본문은 Demonstrations are an extremely convenient form of information we can use to teach robots to overcome these two challenges.를 문제로 두고, In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
