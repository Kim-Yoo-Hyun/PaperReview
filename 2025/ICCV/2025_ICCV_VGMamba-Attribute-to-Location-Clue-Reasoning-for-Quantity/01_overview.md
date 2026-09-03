# VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, SVD alone lacks long-range modeling capability, which is critical for capturing hierarchical dependencies among attributes.를 문제로 두고, Our chief contributions are threefold: • We explore a novel mechanism, i.e., attribute-to-location clue reasoning, for performing 3D visual grounding. • We propose a novel framework VGMamba, comprising three core modules: the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** As an important direction of embodied intelligence, 3D Visual Grounding has attracted much attention, aiming to identify 3D objects matching the given language description.
- **p. 1 / Abstract - extractive body cue:** Most existing methods often follow a two-stage process, i.e., first detecting proposal objects and identifying the right objects based on the relevance to the given ...
- **p. 1 / Abstract - extractive body cue:** However, when the query is complex, it is difficult to leverage an abstract language representation to lock the corresponding objects accurately, affecting the grounding performance.
- **p. 1 / Abstract - extractive body cue:** In general, given a specific object, humans usually follow two clues to finish the corresponding grounding, i.e., attribute and location clues.
- **p. 1 / Abstract - extractive body cue:** To this end, we explore a new mechanism, attribute-to-location clue reasoning, to conduct accurate grounding.
- **p. 2 / 1. Introduction - extractive body cue:** However, SVD alone lacks long-range modeling capability, which is critical for capturing hierarchical dependencies among attributes.
- **p. 2 / 1. Introduction - extractive body cue:** Existing approaches lack a mechanism to systematically leverage this reasoning process, resulting in suboptimal performance in complex scenes.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our chief contributions are threefold: • We explore a novel mechanism, i.e., attribute-to-location clue reasoning, for performing 3D visual grounding. • We propose a novel ...
- **p. 2 / 1. Introduction - extractive body cue:** To be specific, we propose VGMamba, a novel architecture that systematically models attribute-to-location dependencies while efficiently capturing long-range interactions.
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Finally, we present an Instructive Dual-Mamba block to localize the object that matches the given query. Δ to convert continuous parameters into discrete ones.
- **p. 5 / 4.4. Training Objectives - extractive body cue:** Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and object detection loss ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Then, a location mamba is further designed to select location-relevant objects.
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Recently, state space models (SSMs) [9, 12, 30, 32] have attracted much attention for their ability to model continuous systems, constructing the foundation for the ...
- **p. 2 / 3. Overview of State Space Models - extractive body cue:** Particularly, SSMs generally take an input sequence x(t) ∈RL as the input and output the corresponding sequence y(t) ∈RL through hidden states h(t) ∈RN, where ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** (2) The discretized state-space output can be represented as: hk = Ahk-1 + Bxk, yk = Chk.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Particularly, SSMs generally take an input sequence x(t) ∈RL as the input and output the corresponding sequence y(t) ∈RL through hidden states h(t) ∈RN, where N is the number of hidden states. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3. Overview of State Space Models), p. 2 (3. Overview of State Space Models) |
| State/latent | Particularly, SSMs, generally, take, input, sequence, output, corresponding, through, hidden, states, where | geometry, map, object/relationship state | p. 2 (3. Overview of State Space Models), p. 2 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models) |
| Output/action | The system is governed by differential equations that describe how the hidden state evolves over time: h′(t) = Ah(t) + Bx(t), y(t) = Ch(t), (1) where A, B, and C are matrices ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (3. Overview of State Space Models), p. 3 (3. Overview of State Space Models), p. 1 (1. Introduction) |
| Objective/outcome | Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and object detection loss Ldet, which is formulated as: L = ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.4. Training Objectives), p. 2 (3. Overview of State Space Models) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our chief contributions are threefold: • We explore a novel mechanism, i.e., attribute-to-location clue reasoning, for performing 3D visual grounding. • We propose a novel ...
- **p. 2 / 1. Introduction - extractive body cue:** To be specific, we propose VGMamba, a novel architecture that systematically models attribute-to-location dependencies while efficiently capturing long-range interactions.
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Finally, we present an Instructive Dual-Mamba block to localize the object that matches the given query. Δ to convert continuous parameters into discrete ones.
- **p. 5 / 4.4. Training Objectives - extractive body cue:** Building on previous work [42], the loss of VGMamba consists of the 3D Visual Grounding loss Lref, text-object contrastive loss Lcon, and object detection loss ...
- **p. 3 / 3. Overview of State Space Models - extractive body cue:** Then, a location mamba is further designed to select location-relevant objects.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study of proposed modules on Multi3DRefer. its intricate and free-form textual descriptions, which in- crease the difficulty of cross-modal alignment. Despite this, ...
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** VGMamba achieves the highest accuracy with significantly lower FLOPs than methods like Chat-Scene, demonstrating superior efficiency.
- **p. 6 / 5.1.3. Baseline Comparison - extractive body cue:** 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and 53.9% at IoU ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies) |
| Embodiment/environment | The ScanRefer dataset comprises 51,583 natural language descriptions for 11,046 objects across 800 3D scenes from the ScanNet dataset [8]. | hardware/simulator version and reset protocol | p. 5 (5.1.1. Datasets and Evaluation Metrics), p. 6 (5.1.1. Datasets and Evaluation Metrics) |
| Dataset/benchmark | To evaluate the effectiveness of our proposed VGMamba on 3D Visual Grounding tasks with varying numbers of target objects, we conducted experiments on both single-object datasets (ScanRefer [3], Nr3D and Sr3D [1]) ... | role, split, size and leakage | p. 5 (5.1.1. Datasets and Evaluation Metrics), p. 6 (5.1.1. Datasets and Evaluation Metrics), p. 5 (5. Experiments), p. 6 (5.1.1. Datasets and Evaluation Metrics) |
| Metric | 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and 53.9% at IoU 0.5, surpassing the best baseline PQ3D [44] ... | definition, denominator, direction and uncertainty | p. 6 (5.1.3. Baseline Comparison), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies) |
| Baseline/ablation | 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and 53.9% at IoU 0.5, surpassing the best baseline PQ3D [44] ... | fair input/data/compute/action matching | p. 6 (5.1.3. Baseline Comparison), p. 6 (Figure/Table caption), p. 7 (5.1.3. Baseline Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.1.3. Baseline Comparison - extractive body cue:** (iii) Unlike previous methods [13, 44] that show notable performance variations across settings, our VGMamba maintains consistently high accuracy, validating its robust generalization capability in ...
- **p. 7 / 5.2.3. Baseline Comparison - extractive body cue:** 46.7%, surpassing the second-best competitor by 3.1%, which highlights its robustness in managing complex scenes with multiple potential matches.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, SVD alone lacks long-range modeling capability, which is critical for capturing hierarchical dependencies among attributes.를 문제로 두고, Our chief contributions are threefold: • We explore a novel mechanism, i.e., attribute-to-location clue reasoning, for performing 3D visual grounding. • We propose a novel framework VGMamba, comprising three core modules: the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3. Overview of State Space Models), p. 5 (4.4. Training Objectives) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
