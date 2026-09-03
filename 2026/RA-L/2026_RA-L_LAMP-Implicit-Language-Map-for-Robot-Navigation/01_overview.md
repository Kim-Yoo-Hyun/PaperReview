# LAMP: Implicit Language Map for Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2602.11862.
> PDF retrieval source: https://arxiv.org/pdf/2602.11862. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, Navigation
- Official paper: https://arxiv.org/abs/2602.11862
- Full-text retrieval: https://arxiv.org/pdf/2602.11862
- Code/Project: https://lab-of-ai-and-robotics.github.io/LAMP/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This limitation arises from the inherent difficulty of densely and explicitly storing information on large scales.를 문제로 두고, We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field for finegrained path generation using only RGB ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in vision-language models have made zero-shot navigation feasible, enabling robots to interpret and follow natural language instructions without requiring labeling.
- **p. 1 / Abstract - extractive body cue:** However, existing methods that explicitly store language vectors in grid or node-based maps struggle to scale to large environments due to excessive memory requirements and ...
- **p. 1 / Abstract - extractive body cue:** We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path ...
- **p. 1 / Abstract - extractive body cue:** Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location.
- **p. 1 / Abstract - extractive body cue:** By combining this implicit representation with a sparse graph, LAMP supports efficient coarse path planning and then performs gradient-based optimization in the learned field to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This limitation arises from the inherent difficulty of densely and explicitly storing information on large scales.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current language map representations are limited to small environments and encounter significant challenges for large-scale deployment.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path planning that supports ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the strengths of our implicit language map, we propose methods to construct and utilize this representation more effectively.
- **p. 3 / III. METHOD - extractive body cue:** By dynamically generating embeddings through FΘ, our method significantly reduces storage while preserving language features.
- **p. 4 / III. METHOD - extractive body cue:** To address this, we propose a graph sampling method that retains only the most informative nodes, scored by three criteria.
- **p. 2 / III. METHOD - extractive body cue:** We introduce a map representation that continuously encodes language features within a large-scale space, ensuring memory efficiency and enabling fine-grained path planning.
- **p. 3 / III. METHOD - extractive body cue:** Our neural network FΘ then maps x to a d-dimensional CLIP embedding: FΘ(x) = z ∈Rd, where z captures the language features observed in the ...
- **p. 3 / III. METHOD - extractive body cue:** We enforce this unit-length condition by ℓ2-normalising every CLIP feature and network output, so cosine similarity is a true metric and the embeddings reside on ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path planning that supports not only coarse navigation but also fine-gra ... | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| State/latent | address, implicit, language, representation, continuously, models, vectors, RGB-only, input, facilitating, memoryefficient, path | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/action | Our neural network FΘ then maps x to a d-dimensional CLIP embedding: FΘ(x) = z ∈Rd, where z captures the language features observed in the input image I. | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Objective/outcome | (2), the posterior over the network parameters θ is proportional to: p(θ / x, zobs) ∝p(zobs / FΘ(x)) p(κΘ(x)), (3) and we train the network by minimizing the negative logposterior, which serves ... | goal reach, safety, localization error와 replanning latency | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path planning that supports ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the strengths of our implicit language map, we propose methods to construct and utilize this representation more effectively.
- **p. 3 / III. METHOD - extractive body cue:** By dynamically generating embeddings through FΘ, our method significantly reduces storage while preserving language features.
- **p. 4 / III. METHOD - extractive body cue:** To address this, we propose a graph sampling method that retains only the most informative nodes, scored by three criteria.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within 20 ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The purpose of our experiments is to demonstrate that LAMP, our method which implicitly incorporates language information within large-scale scenes, achieves memory efficiency and enables ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | In the following subsections, Section IV-A describes the dataset configuration and implementation details, Section IV-B presents the experimental results obtained in the Nvidia Isaac simulation environment along with a discussion, and S ... | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | In the following subsections, Section IV-A describes the dataset configuration and implementation details, Section IV-B presents the experimental results obtained in the Nvidia Isaac simulation environment along with a discussion, and S ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | First, success rate is computed considering only the top 1% of the predictions; a trial is deemed successful if the robot ends up within 20 m of the center of an object. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Baseline/ablation | Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory when increasing grid resolution to capture finer ... | fair input/data/compute/action matching | p. 2 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects at coarse resolutions and requires excessive memory ...
- **p. 6 / 1) Comparison of Language Map Representation Methods - extractive body cue:** In the Extinguisher scene, the node-based method fails because it does not directly observe the goal, whereas our method correctly identifies the target by leveraging ...
- **p. 5 / 1) Comparison of Language Map Representation Methods - extractive body cue:** Even with this increased memory usage, the grid-based approach captures large objects but fails to detect smaller ones.
- **p. 5 / 1) Comparison of Language Map Representation Methods - extractive body cue:** In contrast, the node-based method needs about 70 times more memory than our method to reach a similar success rate, yet its performance in the ...
- **p. 6 / 1) Comparison of Language Map Representation Methods - extractive body cue:** Finally, in the Boxes scene, the grid-based method is hindered by z-axis projection artifacts, while the node-based method detects the boxes but fails to plan ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This limitation arises from the inherent difficulty of densely and explicitly storing information on large scales.를 문제로 두고, We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field for finegrained path generation using only RGB ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
