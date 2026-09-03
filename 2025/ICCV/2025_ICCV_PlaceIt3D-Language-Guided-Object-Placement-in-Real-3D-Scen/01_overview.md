# PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in that it requires addressing all of the following challenges simultaneously: ...를 문제로 두고, To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each consisting of a real ScanNet scene [15], ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the task of Language-Guided Object Placement in Real 3D Scenes.
- **p. 1 / Abstract - extractive body cue:** Given a 3D reconstructed point-cloud scene, a 3D asset, and a natural-language instruction, the goal is to place the asset so that the instruction is ...
- **p. 1 / Abstract - extractive body cue:** The task demands tackling four intertwined challenges: (a) one-to-many ambiguity in valid placements; (b) precise geometric and physical reasoning; (c) joint understanding across the scene, ...
- **p. 1 / Abstract - extractive body cue:** The first three challenges mirror the complexities of synthetic scene generation, while the metadata-free, noisy-scan scenario is inherited from language-guided 3D visual grounding.
- **p. 1 / Abstract - extractive body cue:** We inaugurate this task by introducing a benchmark and evaluation protocol, releasing a dataset for training multi-modal large language models (MLLMs), and establishing a first ...
- **p. 2 / 1. Introduction - extractive body cue:** We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in that it requires ...
- **p. 2 / 1. Introduction - extractive body cue:** Many constraints are geometric and cannot be resolved from 2D projections alone.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each ...
- **p. 2 / 1. Introduction - extractive body cue:** Like the benchmark, it uses ScanNet scenes and PartObjaverse-Tiny assets. • We propose PLACEWIZARD, a proto-method for this task built on recent 3D LLMs [25].
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we focus on the novel task of languageguided 3D object placement in a reconstructed real 3D scene.
- **p. 6 / 4.4. Losses - extractive body cue:** We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask ...
- **p. 6 / 4.4. Losses - extractive body cue:** Finally, our total loss is defined as \Lo = \Lo _ {seg}(\bar {\mas k }_{l oc}, \mask _{loc}) + \Lo _{rot} + \Lo _{seg}(\bar {\mask ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As in the shoe example, the goal is to find a valid placement of the object among multiple configurations that satisfy the instruction. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | shoe, example, goal, find, valid, placement, object, among, multiple, configurations, satisfy, instruction | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | At two to three years old, neurotypical children learn to follow two-step instructions like "Get your shoes and put them on the shelf" [42]. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask M, so \Lo _{ se g }(\b ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4.4. Losses), p. 6 (4.4. Losses) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each ...
- **p. 2 / 1. Introduction - extractive body cue:** Like the benchmark, it uses ScanNet scenes and PartObjaverse-Tiny assets. • We propose PLACEWIZARD, a proto-method for this task built on recent 3D LLMs [25].
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we focus on the novel task of languageguided 3D object placement in a reconstructed real 3D scene.
- **p. 8 / 5.1.1. Ablations - extractive body cue:** The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative benchmark results. Colored highlights indicate anchors referenced in the textual prompts (predictions are generated entirely from point clouds, with anchor information provided ...
- **p. 7 / 5.1. Quantitative results - extractive body cue:** Our method, row G, consistently outperforms both baselines across all overall evaluation metrics.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results: We compare our full method with variations where some components are removed. The results validate our design choices, and they show ...
- **p. 4 / 3.2.2. Benchmark metrics - extractive body cue:** To evaluate placement performance, we compute metrics that capture constraint validity overall and by subgroup: • Global Constraint Accuracy: The percentage of all constraints (across ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption) |
| Embodiment/environment | PLACEIT3D-dataset-full has ∼4M examples: the 565 scenes x 140 objects x 50 prompts. | hardware/simulator version and reset protocol | p. 5 (3.2.3. Benchmark statistics), p. 4 (3.2.3. Benchmark statistics) |
| Dataset/benchmark | The dataset consists of 100,505 training examples, sourced from 565 distinct ScanNet scenes and 20 unique assets. | role, split, size and leakage | p. 5 (3.2.3. Benchmark statistics), p. 4 (3.2.3. Benchmark statistics), p. 5 (3.2.3. Benchmark statistics), p. 7 (5. Experiments) |
| Metric | To evaluate placement performance, we compute metrics that capture constraint validity overall and by subgroup: • Global Constraint Accuracy: The percentage of all constraints (across all groups) that are correctly satisfied over ... | definition, denominator, direction and uncertainty | p. 4 (3.2.2. Benchmark metrics), p. 7 (5.1. Quantitative results), p. 7 (5.1. Quantitative results) |
| Baseline/ablation | Our method, row G, consistently outperforms both baselines across all overall evaluation metrics. | fair input/data/compute/action matching | p. 7 (5.1. Quantitative results), p. 7 (5.1. Quantitative results), p. 7 (5.1.1. Ablations) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Limitations and Future Work - extractive body cue:** Our novel task formulation currently has several limitations.
- **p. 8 / 6. Limitations and Future Work - extractive body cue:** Despite these limitations, we believe our work lays the groundwork for further research in this area.
- **p. 7 / 5.1. Quantitative results - extractive body cue:** Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while other anchor objects are selected based on ...
- **p. 7 / 5.1. Quantitative results - extractive body cue:** In contrast, the rule-based system, which leverages both asset and scene meshes, can produce more plausible placements, albeit at the cost of expensive collision checks ...
- **p. 4 / 3.2.2. Benchmark metrics - extractive body cue:** This is a strict metric that reflects the robustness of the placement method under full constraint satisfaction. • Language Adherence Success: The percentage of placements ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We study language-guided 3D asset placement in reconstructed scenes, a problem closest to grounding and to synthetic scene generation, yet distinct in that it requires addressing all of the following challenges simultaneously: ...를 문제로 두고, To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each consisting of a real ScanNet scene [15], ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.4. Losses), p. 6 (4.4. Losses), p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
