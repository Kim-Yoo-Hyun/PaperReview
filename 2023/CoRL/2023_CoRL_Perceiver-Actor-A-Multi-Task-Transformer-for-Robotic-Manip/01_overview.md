# Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2209.05451.
> PDF retrieval source: https://arxiv.org/pdf/2209.05451. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Imitation Learning, 3D manipulation
- Official paper: https://arxiv.org/abs/2209.05451
- Full-text retrieval: https://arxiv.org/pdf/2209.05451
- Code/Project: https://peract.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?를 문제로 두고, In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF actions. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets.
- **p. 1 / Abstract - extractive body cue:** But in robotic manipulation, data is both limited and expensive.
- **p. 1 / Abstract - extractive body cue:** Can manipulation still benefit from Transformers with the right problem formulation?
- **p. 1 / Abstract - extractive body cue:** We investigate this question with PERACT, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation.
- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 1 / 1 Introduction - extractive body cue:** Thus, while Transformers may be domain agnostic, they still require the right problem formulation to be data efficient.
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...
- **p. 1 / 1 Introduction - extractive body cue:** To this end, we present PERACT (short for PERCEIVER-ACTOR), a language-conditioned BC agent that can learn to imitate a wide variety of 6-DoF manipulation tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** We also demonstrate our approach with a Franka Panda on 7 real-world tasks (k-o; only 5 shown) with a multi-task agent trained with just 53 ...
- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 2 / 1 Introduction - extractive body cue:** But in PERACT, we use a Perceiver2 Transformer [1] to encode very high-dimensional input of up to 1 million voxels with only a small set ...
- **p. 1 / 1 Introduction - extractive body cue:** In contrast, recent works in reinforcement-learning like C2FARM [14] construct a voxelized observation and action space to efficiently learn visual representations of 3D actions with ...
- **p. 2 / 1 Introduction - extractive body cue:** Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action". | image/video, language instruction, proprioception과 history | p. 1 (Abstract), p. 2 (1 Introduction) |
| State/latent | PERACT, encodes, language, goals, RGB-D, voxel, observations, Perceiver, Transformer, outputs, discretized, actions | language-grounded task state와 action-policy context | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/action | Our results show that PERACT significantly outperforms image-to-action agents (by 34×) and 3D ConvNet baselines (by 2.8×), without using any explicit representations of instance segmentations, object poses, memory, or symbolic states. | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...
- **p. 1 / 1 Introduction - extractive body cue:** To this end, we present PERACT (short for PERCEIVER-ACTOR), a language-conditioned BC agent that can learn to imitate a wide variety of 6-DoF manipulation tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** We also demonstrate our approach with a Franka Panda on 7 real-world tasks (k-o; only 5 shown) with a multi-task agent trained with just 53 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 5. Success rates (mean %) of multi-task and single-task PERACT agents trained with 100 demos and evaluated on 25 episodes. In Table 1, PERACT ...
- **p. 8 / 4 Results - extractive body cue:** Similar to the simulation results, we find that PERACT is able to achieve > 65% success on simple short-horizon tasks like pressing hand-sanitizers from just ...
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 11. Perturbation Tests. Results from a multi-task PERACT agent trained on a single drawer and evaluated on several instances perturbed drawers. Each perturbation consists ...
- **p. 6 / 4 Results - extractive body cue:** [14] that has achieved state-of-the-art results on RLBench tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Embodiment/environment | All keyframes from an episode have the same language goal, which is constructed from templates (but human-annotated for real-world tasks). | hardware/simulator version and reset protocol | p. 6 (4 Results), p. 6 (4 Results) |
| Dataset/benchmark | Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. | role, split, size and leakage | p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results) |
| Metric | Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. Each evaluation ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 7 (4 Results) |
| Baseline/ablation | PERACT outperforms C2FARM-BC [14], the most competitive baseline, with an average improvement of 1.33× with 10 demos and 2.83× with 100 demos. | fair input/data/compute/action matching | p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 Results - extractive body cue:** Evaluations are scored either 0 for failures or 100 for complete successes.
- **p. 7 / 4 Results - extractive body cue:** Each evaluation episode is scored either a 0 for failure or 100 for succces.
- **p. 7 / 4 Results - extractive body cue:** These are very high-precision tasks where being off by a few centimeters or degrees could lead to unrecoverable failures.
- **p. 8 / 4 Results - extractive body cue:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. PERACT Overview. PERACT is a language-conditioned behavior-cloning agent trained with supervised learning to detect actions. PERACT takes as input a language goal and ...
- **p. 8 / 4 Results - extractive body cue:** See Appendix L for an extended discussion on PERACT's limitations.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Language-Conditioned Manipulation Tasks: PERACT is a language-conditioned multi-task agent capable of imitating a wide range of 6-DoF manipulation tasks. We conduct experiments on ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?를 문제로 두고, In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF actions. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
