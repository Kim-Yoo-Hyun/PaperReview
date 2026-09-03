# Method - G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning), p. 6 (Model), p. 6 (Model)): As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated to visual geometry learning and one semantic perception ...

## Method Body Digest

- **p. 4 / 3.1. Model Architecture - extractive body cue:** As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated to visual geometry ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** For geometric perception expert, we incorporate a DINOV2 vision encoder to inject low-level visual information to LLM which further reasons the 3D-aware feature through global ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** This forces the model to learn to use the visual geometry features via in-context learning.
- **p. 6 / Model - extractive body cue:** Model SPAR-Bench MindCube OST-Bench∗ OmniSpatial∗ Avg.
- **p. 6 / Model - extractive body cue:** Our model, G2VLM, demonstrate comparable performance against SOTA feed-forward 3D recontruction methods.
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** We explore three distinct joint-training strategies, where the semantic perception expert is, by default, optimized using a cross-entropy (CE) loss: • CE Loss Only: Freeze ...
- **p. 4 / 3.2. Visual Geometry Learning - extractive body cue:** Specifically, the rotation loss minimizes the geodesic distance (angle) between the predicted relative rotation ˆRi←j and its ground-truth target Ri←j: Lrot(i, j) = arccos  ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive body cue:** We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and ...

## Source Evidence Cues

- **p. 4 / 3.1. Model Architecture - extractive body cue:** As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated to visual geometry ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** For geometric perception expert, we incorporate a DINOV2 vision encoder to inject low-level visual information to LLM which further reasons the 3D-aware feature through global ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** This forces the model to learn to use the visual geometry features via in-context learning.
- **p. 6 / Model - extractive body cue:** Model SPAR-Bench MindCube OST-Bench∗ OmniSpatial∗ Avg.
- **p. 6 / Model - extractive body cue:** Our model, G2VLM, demonstrate comparable performance against SOTA feed-forward 3D recontruction methods.
- **Detected method headings:** 3. Unified Spatial Vision-Language Model (p. 4); 3.1. Model Architecture (p. 4); Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated ... | p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days. | p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.1. Model Architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For geometric perception expert, we incorporate a DINOV2 vision encoder to inject low-level visual information to LLM which further reasons the 3D-aware ... | p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** We explore three distinct joint-training strategies, where the semantic perception expert is, by default, optimized using a cross-entropy (CE) loss: • CE Loss Only: Freeze ...
- **p. 4 / 3.2. Visual Geometry Learning - extractive body cue:** Specifically, the rotation loss minimizes the geodesic distance (angle) between the predicted relative rotation ˆRi←j and its ground-truth target Ri←j: Lrot(i, j) = arccos  ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** Given this scalability constraint, we select the CE Loss Only approach for our main G2VLM.
- **p. 4 / 3.2. Visual Geometry Learning - extractive body cue:** The point cloud reconstruction loss, Lpoints, is defined using the optimal scale factor s∗: Lpoints = 1 3NHW N X i=1 H×W X j=1 1 ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | where, camera, pose, associated, pixel-aligned, point, represented, coordinate, system, corresponding, input, image, visual, geometry | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | where, camera, pose, associated, pixel-aligned, point, represented, coordinate, system, corresponding | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, G2VLM, first, unified, model, bridges, spatial | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | explore, three, distinct, joint-training, strategies, where, semantic, perception, expert, default | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Model Architecture - extractive body cue:** (1) where Ti ∈SE(3) ⊂R4×4 is the camera pose, Xi ∈ RH×W ×3 is the associated pixel-aligned 3D point map represented in its own camera ...
- **p. 2 / 1. Introduction - extractive body cue:** On visual geometry tasks, G2VLM achieves competitive results against state-of-theart (SOTA) feed-forward 3D reconstruction models, such as VGGT [52], across depth estimation, point estimation, and ...
- **p. 2 / 1. Introduction - extractive body cue:** Except incorporating 3D priors as in specific 3D-VLMs [22, 82, 83], general VLMs simply employ feature projection layers and are trained with auto-regressive next-token prediction, ...
- **p. 4 / 3.1. Model Architecture - extractive body cue:** This process maps each image Ii to LLM hidden states hi ∈RC×d.
- **p. 3 / 1. Introduction - extractive body cue:** Qwen Vision Enoder G²VLM DinoV2 Enoder Text Tokenizer Geometry Heads Self-Attention QKV FFN FFN QKV Geometric Perception Expert Semantic Perception Expert Camera poses Depth Maps ...
- **p. 6 / Model - extractive body cue:** OST-Bench∗denotes a subset with ≤15 input frames.
- **p. 6 / Model - extractive body cue:** OmniSpatial∗denotes evaluation on its two main categories: Spatial Interaction (SI) and Perspective Taking (PT).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Except incorporating 3D priors as in specific 3D-VLMs [22, 82, 83], general VLMs simply employ feature projection layers and are trained with ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For spatial understanding and reasoning, we evaluate our model on comprehensive benchmarks, including SPAR-Bench [79], OmniSpatial [24], MindCube [73] (spatial mental modeling), ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Horizontal rotation 110 degrees left. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days.
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** Across all training, we employ gradient norm clipping with a threshold of 1.0 to ensure training stability and leverage bfloat16 precision and gradient checkpointing to ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** illustrated, Figure, G2VLM, adopts, Mixture-ofTransformer-Experts, MoT, architecture, consists, transformer, experts-one, geometry, perception, expert, dedicated, visual, learning, semantic, multimodal, understanding, joint-training.
- **Relevant PDF headings:** 3. Unified Spatial Vision-Language Model (p. 4); 3.1. Model Architecture (p. 4); Model (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D ... | p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results) |
| Semantic / temporal fusion | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of ... | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results) |
| Robot query / planning handoff | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of ... | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Experimental study results. (a) The dual encoder design, with both a semantic-rich CLIP encoder and a low-level vision DINO encoder, yields the best ...
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior or ...
- **p. 8 / 5. Conclusion - extractive body cue:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive body cue:** We leave the scaling of our model to future work, as this is a promising direction to unlock even stronger performance.
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior or ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning), p. 6 (Model), p. 6 (Model), objective p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.2. Visual Geometry Learning), temporal p. 2 (1. Introduction), p. 6 (Model), p. 7 (4.2. Spatial Understanding & Reasoning Results), p. 8 (4.3. Discussions and Ablation Study), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
