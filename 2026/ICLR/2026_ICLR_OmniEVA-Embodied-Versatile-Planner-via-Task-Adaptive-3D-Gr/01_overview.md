# OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=tkEmIJv1tB.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247599. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openreview.net/forum?id=tkEmIJv1tB
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247599
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (52 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms.를 문제로 두고, To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent advances in multimodal large language models (MLLMs) have opened new opportunities for embodied intelligence, enabling multimodal understanding, reasoning, and interaction, as well as continuous ...
- **p. 1 / ABSTRACT - extractive body cue:** Nevertheless, current MLLM-based embodied systems face two critical limitations.
- **p. 1 / ABSTRACT - extractive body cue:** First, Geometric Adaptability Gap: models trained solely on 2D inputs or with hard-coded 3D geometry injection suffer from either insufficient spatial information or restricted 2D ...
- **p. 1 / ABSTRACT - extractive body cue:** Second, Embodiment Constraint Gap: prior work often neglects the physical constraints of real robots, resulting in task plans that are theoretically valid but practically infeasible.To ...
- **p. 1 / ABSTRACT - extractive body cue:** (2) an Embodiment-Aware Reasoning framework that incorporates task goals and physical constraints into the reasoning loop, ensuring executable plans.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, the absence of embodied long-horizon planning benchmarks that explicitly incorporate embodiment constraints makes it difficult to systematically evaluate the unique challenges they pose.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** OmniEVA is the first framework to dynamically integrate 2D and 3D inputs via taskconditioned feature selection, enabling versatile and executable embodied reasoning through two key ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Dynamic 3D Injection via Gated Routing Rather than applying 3D positional encoding uniformly for all tasks, we propose a Task-Adaptive Gated Router (TAGR) that selectively ...
- **p. 18 / A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS - extractive body cue:** This format enables precise object localization and descriptive annotation within a single image frame.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Left: The overall architecture of OmniEVA, featuring a novel task-adaptive gated router that dynamically incorporates 3D positional embeddings.
- **p. 3 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Examples of the Activation of Gated Router Task‐Adaptive Gated Router Sentence Transformer 384 concatenate MLP Network Gumbel Softmax Task Condition Scene Condition Plus 𝒈ൌ𝟎 𝒈ൌ𝟏 ...
- **p. 17 / A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS - extractive body cue:** Detailed hyper-parameters as given in Table 7 TAGR Pretraining During TAGR pretraining, we freeze the sentence transformer and train the MLP encoder with a learning ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 OVERVIEW OmniEVA builds on pretrained MLLMs which typically comprises three principal components: 1) A vision transformer encoder Eimg that converts each RGB image into a sequence of discrete visual tokens, 2) ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| State/latent | OVERVIEW, OmniEVA, builds, pretrained, MLLMs, typically, comprises, three, principal, components, vision, transformer | geometry, map, object/relationship state | p. 3 (3 METHODOLOGY), p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS) |
| Output/action | The model accepts a natural language instruction T, a sequence of RGB images or video frames (I1, I2, . . . , IN), and optionally, depth maps (D1, D2, . . . ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 METHODOLOGY), p. 17 (A.2 INPUT MODALITIES AND OUTPUT REPRESENTATIONS), p. 18 (A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS) |
| Objective/outcome | Given a reward for the i-th response: ri,t(q, oi) = rformat i (oi) + racc i,t (q, oi) (11) 18 | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 18 (A.3 IMPLEMENTATION DETAIL OF EMBODIMENT-AWARE REASONING), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** OmniEVA is the first framework to dynamically integrate 2D and 3D inputs via taskconditioned feature selection, enabling versatile and executable embodied reasoning through two key ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** Dynamic 3D Injection via Gated Routing Rather than applying 3D positional encoding uniformly for all tasks, we propose a Task-Adaptive Gated Router (TAGR) that selectively ...
- **p. 18 / A.2.2 TEXTUAL AND COORDINATE-BASED OUTPUTS - extractive body cue:** This format enables precise object localization and descriptive annotation within a single image frame.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Left: The overall architecture of OmniEVA, featuring a novel task-adaptive gated router that dynamically incorporates 3D positional embeddings.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod -demonstrates ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Results of Different Embodiment Execution Success Rate. Models / Embodiments Average (SR) Seen Arm Length (cm) Unseen Arm Length (cm) 75 88 110
- **p. 30 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** The evaluation involves navigating to target poses, followed by assessing trajectory planning for safe mug placement on the table, with success rates calculated based on ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Embodiment/environment | For example: RT-1 (Brohan et al., 2022) dataset comprises over 130,000 real-world robotic demonstrations (episodes), covering more than 700 different tasks. | hardware/simulator version and reset protocol | p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Dataset/benchmark | E.3 EXAMPLES OF THE IN-HOUSE PRIMITIVE EMBODIED BENCHMARKS E.3.1 WHERE2GO The Where2Go benchmark is constructed using the validation splits of the HM3D (Chang et al., 2017) and MP3D (Chang et al., 2017) ... | role, split, size and leakage | p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 27 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Metric | Figure 5: Ablation Results of the proposed TE-GRPO Method on Local Mobile-Manipulation Tasks As shown in Figure 5, OmniEVA-ER-jointly optimized with rtask and rembod -demonstrates sub- stantial performance gains over OmniEVA-Base and ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING), p. 30 (C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING) |
| Baseline/ablation | Figure 9: Case study illustrating OmniEVA's reasoning process under embodiment-aware constraints. C ABLATION STUDY IMPLEMENTATION DETAILS C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION To rigorously evaluate the necessity of our ... | fair input/data/compute/action matching | p. 23 (Figure/Table caption), p. 24 (C.1 IMPLEMENTATION OF CROSS-ATTENTION BASED 3D FUSION), p. 24 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Performance Comparison across 2D and 3D Embodied Reasoning Benchmarks. Despite recent progress, two core challenges remain. First, the geometric adaptability gap: mod- els ...
- **p. 26 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Designed to overcome the limitations of traditional multimodal models-which primarily operate at the image-level or bounding box-level-it incorporates regional masks linked with precise language descriptions ...
- **p. 29 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** To overcome these limitations, we introduce a 3D-aware planning framework that ingests sequential RGB-D observations and directly generates subgoals in continuous 3D coordinate space.
- **p. 29 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Physical constraints, including object location, size, collision potential, must be considered, making this task highly relevant to the Mobile Placement (Easy) tasks. • Where2Approach: The ...
- **p. 32 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** In addition, it incorporates critical physical constraints, including object dimensions, fit within the available space, and collision avoidance with other objects.
- **p. 32 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** The entire benchmark consists of 464 samples, including 200 generation tasks that require the model to output corresponding points, and 264 judgment tasks where the ...
- **p. 51 / C.2 GATE ACTIVATION ANALYSIS BY SEMANTIC CLUSTERING - extractive body cue:** Common-Sense Considerations: - A vacant area must not overlap any existing objects ... large enough to accommodate ... avoid edges or corners where objects might ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 In particular, neglecting object affordances, workspace limitations, and kinematic feasibility leads to action sequences that cannot be executed on physical platforms.를 문제로 두고, To address these limitations, we introduce OmniEVA (Embodied Versatile Planner), a novel architecture that pioneers Task-Adaptive 3D Grounding and Embodiment-aware Reasoning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 17 (A.1 MODEL ARCHITECTURE AND TRAINING CONFIGURATIONS), p. 3 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
