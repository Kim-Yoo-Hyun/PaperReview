# MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v229/mandlekar23a.html.
> PDF retrieval source: https://arxiv.org/pdf/2310.17596. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, data generation, robot manipulation
- Official paper: https://proceedings.mlr.press/v229/mandlekar23a.html
- Full-text retrieval: https://arxiv.org/pdf/2310.17596
- Code/Project: https://mimicgen.github.io/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals.를 문제로 두고, We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting the human demonstrations to novel settings. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Imitation learning from a large set of human demonstrations has proved to be an effective paradigm for building capable robot agents.
- **p. 1 / Abstract - extractive body cue:** However, the demonstrations can be extremely costly and time-consuming to collect.
- **p. 1 / Abstract - extractive body cue:** We introduce MimicGen, a system for automatically synthesizing large-scale, rich datasets from only a small number of human demonstrations by adapting them to new contexts.
- **p. 1 / Abstract - extractive body cue:** We use MimicGen to generate over 50K demonstrations across 18 tasks with diverse scene configurations, object instances, and robot arms from just ∼200 human demonstrations.
- **p. 1 / Abstract - extractive body cue:** We show that robot agents can be effectively trained on this generated dataset by imitation learning to achieve strong performance in longhorizon and high-precision tasks, ...
- **p. 1 / 1 Introduction - extractive body cue:** For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals.
- **p. 1 / 1 Introduction - extractive body cue:** These works have shown that imitation learning on large diverse datasets can produce impressive performance, allowing robots to generalize toward new objects and unseen tasks.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce a novel data collection system that uses a small set of human demonstrations to automatically generate large datasets across diverse ...
- **p. 4 / 4 Method - extractive body cue:** In our experiments, we designed task variants for each robot manipulation task where we vary either the initial state distribution (D), an object in the ...
- **p. 3 / 4 Method - extractive body cue:** 4.1 Parsing the Source Dataset into Object-Centric Segments Each task consists of a sequence of object-centric subtasks (Assumption 2, Sec.
- **p. 4 / 4 Method - extractive body cue:** 2 (right), this consists of three key steps for each subtask: (1) choosing a reference subtask segment in the source dataset, (2) transforming the subtask ...
- **p. 3 / 4 Method - extractive body cue:** Then, to generate a demonstration for a new scene, MimicGen generates and executes a trajectory (sequence of end-effector control poses) for each subtask, by choosing ...
- **p. 4 / 4 Method - extractive body cue:** Then we can write τi = (T C0 W , T C1 W , ..., T CK W ) where Ct is the controller target ...
- **p. 5 / 4 Method - extractive body cue:** Each generated dataset was then used to train policies using Behavioral Cloning with an RNN policy [7].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | All policy learning results are shown on image-based agents trained with RGB observations (see Appendix Q for low-dim agent results). | observation history와 expert trajectory/action | p. 5 (4 Method), p. 4 (4 Method) |
| State/latent | policy, learning, image-based, agents, trained, RGB, observations, Appendix, low-dim, agent, Executing, segment | behavior policy와 temporal action context | p. 5 (4 Method), p. 4 (4 Method), p. 4 (4 Method) |
| Output/action | Executing the new segment: Finally, MimicGen executes the new segment τ ′ i by taking the target pose at each timestep, transforming it into a delta pose action (Assumption 1, Sec. | predicted action 또는 action chunk | p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method) |
| Objective/outcome | imitation error, task success, robustness와 compounding error | imitation error, task success, robustness와 compounding error | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce a novel data collection system that uses a small set of human demonstrations to automatically generate large datasets across diverse ...
- **p. 4 / 4 Method - extractive body cue:** In our experiments, we designed task variants for each robot manipulation task where we vary either the initial state distribution (D), an object in the ...
- **p. 3 / 4 Method - extractive body cue:** 4.1 Parsing the Source Dataset into Object-Centric Segments Each task consists of a sequence of object-centric subtasks (Assumption 2, Sec.
- **p. 4 / 4 Method - extractive body cue:** 2 (right), this consists of three key steps for each subtask: (1) choosing a reference subtask segment in the source dataset, (2) transforming the subtask ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 source ...
- **p. 5 / 6 Experiments - extractive body cue:** MimicGen data vastly improves agent performance on the source task.
- **p. 6 / 6 Experiments - extractive body cue:** Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 - ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 5 (6 Experiments) |
| Embodiment/environment | We present experiments that (1) highlight the diverse array of situations that MimicGen can generate data for, (2) show that MimicGen compares favorably to collecting additional human demonstrations, both in terms of ... | hardware/simulator version and reset protocol | p. 5 (6 Experiments), p. 5 (6 Experiments) |
| Dataset/benchmark | Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 - Mug Cleanup 12.7 ± 2.5 80.0 ± ... | role, split, size and leakage | p. 5 (6 Experiments), p. 5 (6 Experiments), p. 6 (6 Experiments) |
| Metric | Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 source demos and each 1000 demo MimicGen dataset. ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 6 (6 Experiments), p. 8 (Figure/Table caption) |
| Baseline/ablation | Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 - Mug Cleanup 12.7 ± 2.5 80.0 ± ... | fair input/data/compute/action matching | p. 6 (6 Experiments), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 8 Conclusion - extractive body cue:** We hope that MimicGen motivates and enables exploring a more data-centric perspective on imitation learning in future work.

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals.를 문제로 두고, We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting the human demonstrations to novel settings. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (4 Method), p. 4 (4 Method), p. 5 (4 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** For example, [3] showed that a dataset of over 20,000 trajectories enables generalization to tasks with modest changes in objects and goals. (p. 1, 1 Introduction).
- **Actual contribution:** We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by adapting the human demonstrations to novel ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 source demos and each 1000 demo ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** Why might a data generation attempt result in a failure? (p. 17, 2. What are some limitations of MimicGen?).
