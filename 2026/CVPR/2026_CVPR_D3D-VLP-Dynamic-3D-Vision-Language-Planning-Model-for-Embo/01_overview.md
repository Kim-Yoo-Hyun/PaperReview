# D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: 3D Vision, Vision-Language, Planning, Navigation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, this simple black-box approach impairs VLA Model Modular System Instruction Actions Planning Model Instruction Sub-instructions Grounding Model Navigation Model Actions No target, explore Target is grounded, navigate x x No syn ...를 문제로 두고, In summary, our main contributions are: • We propose D3D-VLP, a 3D vision-language-planning model that unifies multi-step planning, grounding, and navigation in unseen and dynamic environments within a single 3D memory and ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Embodied agents face a critical dilemma that end-to-end models lack interpretability and explicit 3D reasoning, while modular systems ignore cross-component interdependencies and synergies.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we propose the Dynamic 3D Vision-Language-Planning Model (D3DVLP).
- **p. 1 / Abstract - extractive body cue:** Our model introduces two key innovations: 1) A Dynamic 3D Chain-of-Thought (3D CoT) that unifies planning, grounding, navigation, and question answering within a single 3D-VLM ...
- **p. 1 / Abstract - extractive body cue:** This allows different CoT components to mutually reinforce and implicitly supervise each other.
- **p. 1 / Abstract - extractive body cue:** To this end, we construct a largescale dataset with 10M hybrid samples from 5K real scans and 20K synthetic scenes that are compatible with online ...
- **p. 1 / 1. Introduction - extractive body cue:** However, this simple black-box approach impairs VLA Model Modular System Instruction Actions Planning Model Instruction Sub-instructions Grounding Model Navigation Model Actions No target, explore Target ...
- **p. 1 / 1. Introduction - extractive body cue:** However, existing methodologies present a fundamental dilemma.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are: • We propose D3D-VLP, a 3D vision-language-planning model that unifies multi-step planning, grounding, and navigation in unseen and dynamic ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we propose the Dynamic 3D Vision-Language-Planning Model (D3D-VLP).
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive body cue:** The ablation also reveals two complementary roles of SLFS: 1) SLFS enables the model to exploit massive partially annotated data (w/o Tplan, types 4-6) to ...
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive body cue:** The SG3D benchmark is specifically designed to evaluate planning, grounding, and memory capabilities in longhorizon stateful tasks of an agent.
- **p. 2 / 3. Our Method - extractive body cue:** At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464
- **p. 3 / 3. Our Method - extractive body cue:** RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, action, answer CoT ...
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive body cue:** Without it, the agent degenerates from a planning and stateful controller into a reactive and memory-less one, and the task-level accuracy t-ACC collapses from 9.3% ...
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive body cue:** For example, the Dynam3D-VisTA modular baseline, which pairs the strong 3D perception and navigation baseline model [57] with a 3D grounding model [82] achieves a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | RGB images Depth images Dynam3D Encoder Waypoint Predictor D3D-VLP Model "Set up a nightlight in the bathroom." Instruction Historical plans, grounded targets, action, answer CoT Memory Multi-level 3D Memory Panoramic patch tokens ... | camera/depth stream, pose, map와 language goal | p. 3 (3. Our Method), p. 1 (1. Introduction) |
| State/latent | RGB, images, Depth, Dynam3D, Encoder, Waypoint, Predictor, D3D-VLP, Model, Set, nightlight, bathroom | robot pose, free-space/semantic map와 local goal | p. 3 (3. Our Method), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | The end-to-end models directly map instructions to navigation actions, and modular systems assemble multiple specialized components. | collision-free trajectory 또는 velocity command | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | At each timestep, we use the encoder of Dynam3D [57] to process streaming posed RGB-D images to update a dynamic Multi-level 3D 32464 | goal reach, safety, localization error와 replanning latency | p. 2 (3. Our Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are: • We propose D3D-VLP, a 3D vision-language-planning model that unifies multi-step planning, grounding, and navigation in unseen and dynamic ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these limitations, we propose the Dynamic 3D Vision-Language-Planning Model (D3D-VLP).
- **p. 8 / 1. Synergistic Learning (SLFS) and Training Data - extractive body cue:** The ablation also reveals two complementary roles of SLFS: 1) SLFS enables the model to exploit massive partially annotated data (w/o Tplan, types 4-6) to ...
- **p. 7 / 4.3. Long-Horizon Grounding and Planning - extractive body cue:** The SG3D benchmark is specifically designed to evaluate planning, grounding, and memory capabilities in longhorizon stateful tasks of an agent.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.5. Real-World Mobile Manipulation Experiments), p. 6 (4.1. Experimental Setup) |
| Embodiment/environment | Grounding & Grasp Place Task OK-Robot [38] 11/32 4/16 3/16 0/10 DynaMem [37] 13/32 6/16 4/16 0/10 Dynam3D+OWLv2 [42, 57] 21/32 9/16 7/16 1/10 D3D-VLP (Ours) 23/32 12/16 11/16 3/10 To validate ... | hardware/simulator version and reset protocol | p. 8 (4.5. Real-World Mobile Manipulation Experiments), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | These tasks evaluate the ability of the agent to follow natural language instructions that ranges from stepby-step directions (R2R-CE) to coarse-grained destination descriptions (REVERIE-CE) and complex user-demand instructions (NavRAG-CE). | role, split, size and leakage | p. 8 (4.5. Real-World Mobile Manipulation Experiments), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.5. Real-World Mobile Manipulation Experiments) |
| Metric | Table 4. Ablation study on components and training data. Settings Training data R2R-CE Nav. SG3D Grounding OSR SR SPL | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Baseline/ablation | Figure 1. Model Architecture Comparison. The end-to-end models directly map instructions to navigation actions, and modu- lar systems assemble multiple specialized components. Our D3D- VLP employs a single 3D-VLM with 3D CoT ... | fair input/data/compute/action matching | p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future work could incorporate Reinforcement Learning to further enhance this framework.

## Why Read It

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, this simple black-box approach impairs VLA Model Modular System Instruction Actions Planning Model Instruction Sub-instructions Grounding Model Navigation Model Actions No target, explore Target is grounded, navigate x x No syn ...를 문제로 두고, In summary, our main contributions are: • We propose D3D-VLP, a 3D vision-language-planning model that unifies multi-step planning, grounding, and navigation in unseen and dynamic environments within a single 3D memory and ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (3. Our Method), p. 3 (3. Our Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
