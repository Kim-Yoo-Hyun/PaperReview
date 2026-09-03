# GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=4SsNofUQf1.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168191. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://openreview.net/forum?id=4SsNofUQf1
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/168191
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the transition of these PEFT methods from 2D to 3D vision poses significant challenges due to the inherent sparsity and irregularity of point clouds.를 문제로 두고, In summary, the key contributions of this work are: (1) We propose GAPrompt, a novel geometry-aware prompt learning method tailored for pre-trained 3D vision models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Pre-trained 3D vision models have gained significant attention for their promising performance on point cloud data.
- **p. 1 / Abstract - extractive body cue:** However, fully fine-tuning these models for downstream tasks is computationally expensive and storage-intensive.
- **p. 1 / Abstract - extractive body cue:** Existing parameter-efficient fine-tuning (PEFT) approaches, which focus primarily on input token prompting, struggle to achieve competitive performance due to their limited ability to capture the ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.
- **p. 1 / Abstract - extractive body cue:** First, we introduce a Point Prompt that serves as an auxiliary input alongside the original point cloud, explicitly guiding the model to capture fine-grained geometric ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the transition of these PEFT methods from 2D to 3D vision poses significant challenges due to the inherent sparsity and irregularity of point clouds.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, parameter-efficient fine-tuning (PEFT) methods have been introduced, particularly in 2D vision, to improve the efficiency and effectiveness of adapting pre-trained models.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of this work are: (1) We propose GAPrompt, a novel geometry-aware prompt learning method tailored for pre-trained 3D vision models.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt), specifically designed for parameter-efficient fine-tuning of 3D models.
- **p. 1 / 1. Introduction - extractive body cue:** This advancement has propelled the development of various 3D vision applications, including 3D reconstruction (Xu et al., 2022; Lu et al., 2024) and autonomous driving ...
- **p. 4 / 3.1. Point Prompt - extractive body cue:** Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), (3) where ˜hi ...
- **p. 4 / 3.1. Point Prompt - extractive body cue:** Furthermore, we adjust the tokens with adapters enhanced by shape feature f. ˆhi, ˆpi = Attn.([˜hi, pi]), (4) hi+1 = ˆhi + Adapter( ˆhi + ...
- **p. 3 / 3.1. Point Prompt - extractive body cue:** This module also generates instance-specific informative shape features f ∈RD, where D is the embedding dimension of transformers, formulated as: ˜x, f = Point-Shift-Prompter(x).
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** Firstly, an upsampling strategy is employed to propagate features from center points to neighbor points.
- **p. 5 / 3.2. Point Shift Prompter - extractive body cue:** Then we further process the features with another pointnet: ˜d n j = Pointnet(Propagate(˜dj)), (10) where ˜d n j ∈RCj×Kj×Dj is features of neighbor points ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then we feed these tokens into our Prompt Propagation mechanism, injecting prompt tokens into the feature extraction process: ˜hi = Prompt-Propagation([hi; pi]), (3) where ˜hi ∈RLt×D is the propagated input tokens. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.1. Point Prompt), p. 3 (3.1. Point Prompt) |
| State/latent | Then, feed, tokens, Prompt, Propagation, mechanism, injecting, feature, extraction, process, Prompt-Propagation, where | geometry, map, object/relationship state | p. 4 (3.1. Point Prompt), p. 3 (3.1. Point Prompt), p. 4 (3.1. Point Prompt) |
| Output/action | Given a raw input point cloud x ∈RS×3 with S points, firstly we hybrid Point Prompt P ∈RP ×3 into its 3D space, denoted as [x; P] ∈R(S+P )×3, where "[ ]" ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Point Prompt), p. 4 (3.1. Point Prompt), p. 5 (3.2. Point Shift Prompter) |
| Objective/outcome | Specifically, to acquire global shape information of point clouds without much computational cost, we utilize a hierarchical downsampling strategy. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Point Shift Prompter), p. 3 (3. The Proposed Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of this work are: (1) We propose GAPrompt, a novel geometry-aware prompt learning method tailored for pre-trained 3D vision models.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt), specifically designed for parameter-efficient fine-tuning of 3D models.
- **p. 1 / 1. Introduction - extractive body cue:** This advancement has propelled the development of various 3D vision applications, including 3D reconstruction (Xu et al., 2022; Lu et al., 2024) and autonomous driving ...
- **p. 7 / 4.2. Quantitative Analysis - extractive body cue:** In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT.
- **p. 7 / 4.2. Quantitative Analysis - extractive body cue:** As shown in Table 1, our method GAPrompt achieves the highest accuracy among all the parameter-efficient fine-tuning methods for 3D vision models.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This suggests that the Point Shift Prompter can enhance the geometric features of the point cloud at the input level, thereby contributing to improved performance.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 10. Ablation study on different input for downstream head. C.2. Analysis on Adapter Enhancing Factor βa. As shown in Figure 8, we conduct further ...
- **p. 6 / 4. Experiments - extractive body cue:** We evaluate the performance of our proposed GAPrompt on the point cloud classification task.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Quantitative Analysis), p. 7 (4.2. Quantitative Analysis) |
| Embodiment/environment | The ScanObjectNN (Uy et al., 2019) is a highly challenging 3D dataset comprising 15K real-world objects across 15 categories. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study) |
| Dataset/benchmark | Note that our experiments on dataset ScanObjectNN sample 6 | role, split, size and leakage | p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Study) |
| Metric | Since voting (Liu et al., 2019) is time-consuming, we focus on reporting overall accuracy without it. | definition, denominator, direction and uncertainty | p. 7 (4.1. Experimental Settings), p. 7 (4.2. Quantitative Analysis), p. 8 (4.3. Ablation Study) |
| Baseline/ablation | In terms of FLOPs, our approach adds virtually no extra computational burden compared to baselines, significantly outperforming IDPT and Point-PEFT. | fair input/data/compute/action matching | p. 7 (4.2. Quantitative Analysis), p. 6 (4. Experiments), p. 6 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 3.4. Analysis and Discussion - extractive body cue:** The key distinction of our approach lies in the point-level operation, addressing the limitations of previous prompting 5
- **p. 7 / 4.2. Quantitative Analysis - extractive body cue:** In contrast, IDPT, DAPT, and Point-PEFT fall short of full fine-tuning performance due to their limited ability to capture geometric information from point clouds.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Methods for adapting pre-trained 3D vision models. (a) Fine-tuning updates entire model parameters. (b) Prompt-based methods adapt the model to downstream tasks by ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** These objects consist of indoor scene data obtained by scanning, exhibiting characteristics such as cluttered backgrounds and occlusions.
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** ModelNet40 (Wu et al., 2015) comprises 12,311 pristine 3D CAD models across 40 categories, with complete, uniform, and noise-free point clouds that simplify the task.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Intuitively, it is because this setting brings more randomness and results in more robust convergence.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the transition of these PEFT methods from 2D to 3D vision poses significant challenges due to the inherent sparsity and irregularity of point clouds.를 문제로 두고, In summary, the key contributions of this work are: (1) We propose GAPrompt, a novel geometry-aware prompt learning method tailored for pre-trained 3D vision models.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Point Prompt), p. 4 (3.1. Point Prompt) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
