# Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, which are essential for precise real-world interaction.를 문제로 두고, In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed object understanding through materialaware, part-level segmentation an ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, partaware segmentation grounding and ...
- **p. 1 / Abstract - extractive body cue:** Existing 3D datasets largely focus on either vision-only part segmentation or vision-language scene segmentation, lacking the fine-grained multimodal segmentation needed for robotic navigation and interaction ...
- **p. 1 / Abstract - extractive body cue:** To address this gap, we present the 3DCoMPaT Grounded Instructions (3DCoMPaT-GrIn) Dataset, a comprehensive resource that pairs rich point cloud descriptions with corresponding part-level segmentation ...
- **p. 1 / Abstract - extractive body cue:** This dataset encompasses extensive samples designed for both PaPGD and fine-grained singlepart grounding tasks.
- **p. 1 / Abstract - extractive body cue:** To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language ...
- **p. 2 / 1. Introduction - extractive body cue:** However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, which are essential ...
- **p. 1 / 1. Introduction - extractive body cue:** Both armrests are also leather with a sleek black finish, matching the seat support, which is made of leather in brown.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges posed by PaPGD, we propose Kestrel, a novel part-aware 3D MLLM designed to capture the intricate spatial and compositional details required ...
- **p. 3 / 4. Method - extractive body cue:** To bridge this gap, we propose Kestrel, which combines a 3D MLLM with a query refinement mechanism to enable fine-grained part segmentation along with detailed ...
- **p. 4 / 4.1. Kestrel - extractive body cue:** We introduce projector P1 to align the latent space of language and 3D vision.
- **p. 6 / Model - extractive body cue:** In addition, we propose a new evaluation for the 3D CompositionAware Language Comprehension (3D-CALC) capabilities of 3D MLLMs.
- **p. 4 / 4.1. Kestrel - extractive body cue:** As shown in Figure 2, Kestrel is composed of a point encoder, an LLM, a point feature propagation module (PFPM), and a segmentation decoder.
- **p. 4 / 4.1. Kestrel - extractive body cue:** Each upsampled feature is combined with intermediate segmentation decoder queries, qi(i ↑{1, 2}), which will be projected through an MLP and then combined by a ...
- **p. 3 / 4. Method - extractive body cue:** 4.1, we formally introduce Kestrel as a part-aware point grounding 3D MLLM, followed by a detailed explanation of our training objective in Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The point encoder and LLM take a point-aware instruction and point cloud as input, generating a detailed part-level description of the point cloud. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4.1. Kestrel), p. 4 (4. Method) |
| State/latent | point, encoder, LLM, take, point-aware, instruction, cloud, input, generating, detailed, part-level, description | geometry, map, object/relationship state | p. 4 (4.1. Kestrel), p. 4 (4. Method), p. 2 (1. Introduction) |
| Output/action | The 3D Segmentation Decoder extracts the output embedding of the [SEG] token from the output hidden states of the 3D MLLM. | point map, pose, scene graph, affordance 또는 query result | p. 4 (4. Method), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | To achieve this, we utilize an auto-regressive cross-entropy loss LCE for text generation, along with binary cross-entropy loss LBCE and Dice loss LDice [20] for segmentation mask prediction. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.2. Training Objective), p. 3 (4. Method), p. 5 (4.2. Training Objective) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges posed by PaPGD, we propose Kestrel, a novel part-aware 3D MLLM designed to capture the intricate spatial and compositional details required ...
- **p. 3 / 4. Method - extractive body cue:** To bridge this gap, we propose Kestrel, which combines a 3D MLLM with a query refinement mechanism to enable fine-grained part segmentation along with detailed ...
- **p. 4 / 4.1. Kestrel - extractive body cue:** We introduce projector P1 to align the latent space of language and 3D vision.
- **p. 6 / Model - extractive body cue:** In addition, we propose a new evaluation for the 3D CompositionAware Language Comprehension (3D-CALC) capabilities of 3D MLLMs.
- **p. 5 / 5. Experiments - extractive body cue:** 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D [26]).
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results of Kestrel on Part-Aware Point Grounded Description, Reasoning and Direct Segmentation. The results show that Kestrel is capable of detailed 3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (5. Experiments), p. 5 (Figure/Table caption) |
| Embodiment/environment | 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point clouds are collected from noisy real-world environments. | hardware/simulator version and reset protocol | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Dataset/benchmark | 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point clouds are collected from noisy real-world environments. | role, split, size and leakage | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Metric | Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on PointLLM's dataset[64] and 3DCoMPaT-GrIn's point c ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Baseline/ablation | We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec. | fair input/data/compute/action matching | p. 5 (5. Experiments), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model ...
- **p. 8 / 6. Conclusion - extractive body cue:** Our work establishes a robust benchmark for part-aware 3D vision-language understanding, paving the way for future research in finegrained 3D object interaction and grounding.
- **p. 5 / 5. Experiments - extractive body cue:** 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # Refinement Levels Grounded Desc. Direct Segmentation Reasoning ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, which are essential for precise real-world interaction.를 문제로 두고, In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed object understanding through materialaware, part-level segmentation an ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Kestrel), p. 4 (4.1. Kestrel), p. 3 (4. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
