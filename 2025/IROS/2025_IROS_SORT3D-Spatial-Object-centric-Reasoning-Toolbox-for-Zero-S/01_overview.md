# SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2504.18684.
> PDF retrieval source: https://arxiv.org/pdf/2504.18684. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://arxiv.org/abs/2504.18684
- Full-text retrieval: https://arxiv.org/pdf/2504.18684
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being an intuitive task fo ...를 문제로 두고, To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown 를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Interpreting object-referential language and grounding objects in 3D with spatial relations and attributes is essential for robots operating alongside humans.
- **p. 1 / Abstract - extractive body cue:** However, this task is often challenging due to the diversity of scenes, large number of fine-grained objects, and complex free-form nature of language references.
- **p. 1 / Abstract - extractive body cue:** Furthermore, in the 3D domain, obtaining large amounts of natural language training data is difficult.
- **p. 1 / Abstract - extractive body cue:** Thus, it is important for methods to learn from little data and zero-shot generalize to new environments.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose SORT3D, an approach that utilizes rich object attributes from 2D data and merges a heuristics-based spatial reasoning toolbox with ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, training end-to-end learning-based methods on 3D referential grounding requires a large amount of annotated data aligning language references to a 3D scene, which the ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As a result, our method only requires a single in-context example of the toolbox usage and no other training data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** This component is the only pipeine change required for our method to be deployed in the real-world.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D bounding boxes to ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. nightstand and bed), ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** The usage of open-vocabulary 2D foundation models allows our semantic mapping module to generalize to new environments as we show in our real-world experiments (section ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3D referential grounding additionally acts as a precursor to downstream tasks such as object-goal navigation, multi-action instruction-following, and scene visual question answering (VQA). | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| State/latent | referential, grounding, additionally, acts, precursor, downstream, tasks, object-goal, navigation, multi-action, instruction-following, scene | geometry, map, object/relationship state | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Output/action | The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language. | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Objective/outcome | We use Qwen2-VL-7B [27] as our VLM as we found it to perform best in generating accurate and concise descriptions following our template, and the quantized version of Qwen2.5-VL-Instruct-3B for system deployment ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As a result, our method only requires a single in-context example of the toolbox usage and no other training data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** This component is the only pipeine change required for our method to be deployed in the real-world.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy.
- **p. 5 / V. RESULTS AND DISCUSSION - extractive body cue:** Similarly, while Transcrib3D reports higher accuracies, it relies on guiding principles [6] that are tailored to the language used in Nr3D and Sr3D, which improve ...
- **p. 5 / V. RESULTS AND DISCUSSION - extractive body cue:** We see that our method achieves higher accuracy with GPT4o as the LLM backend and is on par with SOTA methods on View-Dependent statements in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION) |
| Embodiment/environment | Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to SOTA baselines. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION) |
| Dataset/benchmark | Both datasets consist of utterances describing a target object in a ScanNet [13] scene using spatial relations. | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION), p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION) |
| Metric | For our methods, we conduct multiple trials on each data split to measure variance in LLMs, reported with standard deviation values on the grounding accuracy, which we note that other LLM-based methods ... | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION) |
| Baseline/ablation | Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to SOTA baselines. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that the sentence implies choosing a pillow on ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being an intuitive task fo ...를 문제로 두고, To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown 를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
