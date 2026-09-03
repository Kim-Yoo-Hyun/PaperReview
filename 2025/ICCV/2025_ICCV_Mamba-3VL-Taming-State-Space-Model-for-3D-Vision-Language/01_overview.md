# Mamba-3VL: Taming State Space Model for 3D Vision Language Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the unmodified utilization of mamba does not yield satisfactory performance on 3D-VL tasks due to the following challenges: (1) 3D point clouds are sparse, unordered and encode rich spatial information.를 문제로 두고, To capture spatial relationships of 3D object sequences while enhancing fine-grained interactions of 3D-VL interaction, we develop a Mamba Mixer module, which consists of a relation-prioritized spatial scanning and a channel twisting.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D vision-language (3D-VL) reasoning, connecting natural language with 3D physical world, represents a milestone in advancing spatial intelligence.
- **p. 1 / Abstract - extractive body cue:** While transformer-based methods dominate 3D-VL research, their quadratic complexity and simplistic positional embedding mechanisms severely limits effective modeling of long-range 3D-VL dependencies and spatial relationships ...
- **p. 1 / Abstract - extractive body cue:** State Space Models (SSM) have emerged as promising linear-complexity alternatives for sequential data processing, while inherent selection mechanism offers notable capability for spatial modeling.
- **p. 1 / Abstract - extractive body cue:** Despite its potential, straightforward adoption of Mamba to 3D-VL tasks encounters two obstacles: (1) how to perceive the position of 3D objects and understand complex ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Mamba-3VL, a pioneering 3D-VL framework to model complex intra- and inter-modality correlations and enhance spatial relation reasoning, while guaranteeing top-tier ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the unmodified utilization of mamba does not yield satisfactory performance on 3D-VL tasks due to the following challenges: (1) 3D point clouds are sparse, ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) Mamba's vanilla framework lacks native cross-modal interaction mechanisms necessary to seamlessly align semantics with 3D geometries.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To capture spatial relationships of 3D object sequences while enhancing fine-grained interactions of 3D-VL interaction, we develop a Mamba Mixer module, which consists of a ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose an Instance-aware Dynamic Position Adapter (IDPA) with intercalated EdgeConv [56-58] and Language-modulated InStance Adapter (LISA) layers.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To better adapt mamba to 3D-VL tasks, we introduce Mamba Mixer, which interprets spatial relationships of 3D objects and achieves holistic inter-modality and intra-modality interactions.
- **p. 4 / 3.3. Instance-aware Dynamic Position Adapter - extractive body cue:** Inspired by this, we introduce an Instance-aware Dynamic Position Adapter (IDPA) to provide fine-grained, instance-specific positional embeddings for Mamba Mixer with enhanced spatial relation modeling.
- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** We propose Mamba3VL with designs like relation-prioritized scanning, which paves the road to spearhead new avenues in 3D-VL research.
- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** Vim [72] presents the first pure SSM-based model that efficiently compress the vision representation for intensive prediction tasks.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To establish the correspondence between 3D vision and task prompts, we first construct a hybrid feature chain by channel-wisely concatenating 3D instance queries and prompt ...
- **p. 3 / 3.1. Overall Framework - extractive body cue:** For the point cloud, we use the pre-trained PointNet++ [47] to obtain point features P={p0, p1, ..., pS} of the segments.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Recent studies [32, 36, 65, 66] investigate the applicability of mamba on 3D tasks by employing distinct point cloud ordering policy. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (2.2. State Space Models and Visual Applications), p. 2 (1. Introduction) |
| State/latent | Recent, studies, investigate, applicability, mamba, tasks, employing, distinct, point, cloud, ordering, policy | geometry, map, object/relationship state | p. 3 (2.2. State Space Models and Visual Applications), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Leveraging State Space Models (SSMs) as its core, a flux of mamba proposes a selection scanning mechanism, enabling it to handle long-range sequences and spatial modeling in near-linear complexity. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overall Framework) |
| Objective/outcome | We compute the cross entropy loss Lgrd and Lgen for both grounding and generation heads, while the dice loss Lmask is applied to the mask head. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Output Heads and Losses), p. 5 (3.4. Output Heads and Losses) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To capture spatial relationships of 3D object sequences while enhancing fine-grained interactions of 3D-VL interaction, we develop a Mamba Mixer module, which consists of a ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose an Instance-aware Dynamic Position Adapter (IDPA) with intercalated EdgeConv [56-58] and Language-modulated InStance Adapter (LISA) layers.
- **p. 4 / 3.2. Multi-Modal Mamba Mixer Block - extractive body cue:** To better adapt mamba to 3D-VL tasks, we introduce Mamba Mixer, which interprets spatial relationships of 3D objects and achieves holistic inter-modality and intra-modality interactions.
- **p. 4 / 3.3. Instance-aware Dynamic Position Adapter - extractive body cue:** Inspired by this, we introduce an Instance-aware Dynamic Position Adapter (IDPA) to provide fine-grained, instance-specific positional embeddings for Mamba Mixer with enhanced spatial relation modeling.
- **p. 3 / 2.2. State Space Models and Visual Applications - extractive body cue:** We propose Mamba3VL with designs like relation-prioritized scanning, which paves the road to spearhead new avenues in 3D-VL research.
- **p. 6 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** The model achieves landmark accuracies of 79.9% (Unique) and 48.9% (Multiple) on the ScanRefer [6], outperforming PQ3D [74] by 1.7% and 2.7%, respectively.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Visualization results of the scene-aware task planning and embodied conversation on the 3RPlan [21] and 3RDialog [21] datasets. petitors on challenging unseen tasks, ...
- **p. 6 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** On Multi3DRefer [67], Mamba3VL attains 69.5%, 45.7%, and 43.5% scores, showing a substantial improvement in different object referencing levels.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption) |
| Embodiment/environment | (2) 80-epoch full-task training on all benchmark datasets with promptable queries. | hardware/simulator version and reset protocol | p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Dataset/benchmark | For embodied AI tasks, we replace the T5-small [49] model of generation head with Vicuna-7B [13] using the instructionfollowing dataset [21]. | role, split, size and leakage | p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 5 (4.1. Implementation Details) |
| Metric | Figure 6. Visualization results of the scene-aware task planning and embodied conversation on the 3RPlan [21] and 3RDialog [21] datasets. petitors on challenging unseen tasks, while achieving seen performance on par with ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Baseline/ablation | For the SQA3D [42], Mamba3VL outperforms all existing state-of-the-arts across different challenging question types as illustrated in Tab. | fair input/data/compute/action matching | p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption), p. 6 (4.2. Results on 3D Vision-Language Tasks) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Our method exhibits view-invariant robustness with 3.9% and 6.2% improvements over PQ3D on VD subsets of Nr3D/Sr3D benchmarks.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** FIS/NIS) results in performance degradation, suggesting their complementary roles.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** Crossattention treats all tokens within a sequence equally, failing to capture the hierarchical dependencies within 3D scenes.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the unmodified utilization of mamba does not yield satisfactory performance on 3D-VL tasks due to the following challenges: (1) 3D point clouds are sparse, unordered and encode rich spatial information.를 문제로 두고, To capture spatial relationships of 3D object sequences while enhancing fine-grained interactions of 3D-VL interaction, we develop a Mamba Mixer module, which consists of a relation-prioritized spatial scanning and a channel twisting.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.2. State Space Models and Visual Applications), p. 4 (3.2. Multi-Modal Mamba Mixer Block), p. 3 (3.1. Overall Framework), p. 4 (3.2. Multi-Modal Mamba Mixer Block) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
