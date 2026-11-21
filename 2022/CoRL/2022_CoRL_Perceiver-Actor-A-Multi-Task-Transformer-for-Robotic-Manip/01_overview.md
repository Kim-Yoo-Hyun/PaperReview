# Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2209.05451.
> PDF retrieval source: https://arxiv.org/pdf/2209.05451. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CoRL
- Authors: Mohit Shridhar, Lucas Manuelli, Dieter Fox
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Imitation Learning, 3D manipulation
- Official paper: https://arxiv.org/abs/2209.05451
- Venue verification: https://proceedings.mlr.press/v205/shridhar23a.html
- Conference edition: 2022 · https://proceedings.mlr.press/v205/
- Full-text retrieval: https://arxiv.org/pdf/2209.05451
- Code/Project: https://peract.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

PerAct는 언어 지시와 RGB-D 복셀 관측에서 다음 그리퍼 동작을 예측하는 다중 작업 모방 정책이다. [PDF 1쪽](https://proceedings.mlr.press/v205/shridhar23a/shridhar23a.pdf#page=1)

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

- Perceiver가 관측을 압축한 뒤 다음 동작의 병진 위치를 복셀에서 찾고 회전과 그리퍼 상태를 이산적으로 예측한다. [PDF 3쪽](https://proceedings.mlr.press/v205/shridhar23a/shridhar23a.pdf#page=3) · [PDF 4쪽](https://proceedings.mlr.press/v205/shridhar23a/shridhar23a.pdf#page=4)
- RLBench와 실제 탁상 조작에서 같은 정책을 여러 작업에 학습시켜 영상 기반 정책 및 3D 합성곱 기준선과 비교했다. [PDF 6쪽](https://proceedings.mlr.press/v205/shridhar23a/shridhar23a.pdf#page=6) · [PDF 8쪽](https://proceedings.mlr.press/v205/shridhar23a/shridhar23a.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation? (p. 1, 1 Introduction).
- **Actual contribution:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 1. Multi-Task Test Results. Success rates (mean %) of various multi-task agents tasks trained with either 10 or 100 demonstrations per task and evaluated on 25 episodes per task. ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. (p. 8, 4 Results).
