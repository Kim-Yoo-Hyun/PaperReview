# Method - IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=swiL18PmUV; PDF retrieval source: https://openreview.net/pdf/817142b3bbdc845776217fe32eb67c0abcce545d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY)): (1) Our IGGT consists of three parts: 1) a Large Unified Transformer to capture Unified Token Representation from multiple images; 2) two Downstream Heads with a Cross-Modal Fusion Block to ...

## Method Body Digest

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** (1) Our IGGT consists of three parts: 1) a Large Unified Transformer to capture Unified Token Representation from multiple images; 2) two Downstream Heads with ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry supervision terms pose ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** (2) Moreover, to enhance the fine-grained spatial awareness of the instance head, we propose a crossmodal fusion block Fwin(·), which utilizes a sliding window cross ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** These masks are then used to guide state-of-the-art vision-language models (VLMs, e.g., CLIP, OpenSeg) and large multimodal models (LMMs, e.g., GPT-4o, Qwen2.5-VL) to perform open-vocabulary ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** We then aggregate the features within each 2D instance mask {flang k ∈RD}K i=1 via average mask pooling, yielding a compact representation for each instance.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** It first produces image-wise features {F lang i ∈RD×H×W }N i=1, which considers contextual information to enable accurate visual-language alignment of the features.
- **p. 7 / 3 METHODOLOGY - extractive PDF cue:** Similar colors in PCA indicate higher feature similarity between instances.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** This objective structures the instance representations according to the 3D scene geometry, improving generalization.

## Design Rationale

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** 3.1 OVERVIEW Our method consists of two main phases.
- **p. 7 / 3 METHODOLOGY - extractive PDF cue:** We present two example scenes from ScanNet (Dai et al., 2017) and ScanNet++ (Yeshwanth et al., 2023), and compare our method with SAM2* and SpaTracker+SAM.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** 1, our method is the only one that simultaneously enables multi-view instance matching, image-to-3D reconstruction, and scene understanding, while achieving state-of-the-art performance across all tasks.

## Source Evidence Cues

- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** (1) Our IGGT consists of three parts: 1) a Large Unified Transformer to capture Unified Token Representation from multiple images; 2) two Downstream Heads with ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry supervision terms pose ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** (2) Moreover, to enhance the fine-grained spatial awareness of the instance head, we propose a crossmodal fusion block Fwin(·), which utilizes a sliding window cross ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** These masks are then used to guide state-of-the-art vision-language models (VLMs, e.g., CLIP, OpenSeg) and large multimodal models (LMMs, e.g., GPT-4o, Qwen2.5-VL) to perform open-vocabulary ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** We then aggregate the features within each 2D instance mask {flang k ∈RD}K i=1 via average mask pooling, yielding a compact representation for each instance.
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** It first produces image-wise features {F lang i ∈RD×H×W }N i=1, which considers contextual information to enable accurate visual-language alignment of the features.
- **p. 7 / 3 METHODOLOGY - extractive PDF cue:** Similar colors in PCA indicate higher feature similarity between instances.
- **Detected method headings:** 3 METHODOLOGY (p. 4); A.2 USE OF LARGE LANGUAGE MODELS (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | (1) Our IGGT consists of three parts: 1) a Large Unified Transformer to capture Unified Token Representation from multiple images; 2) two ... | p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry ... | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | (2) Moreover, to enhance the fine-grained spatial awareness of the instance head, we propose a crossmodal fusion block Fwin(·), which utilizes a ... | p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** This objective structures the instance representations according to the 3D scene geometry, improving generalization.
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Cluster Masks CLIP Features " Sink" Instance Head Geometry Head OpenSeg Cross-Attention Block Self-Attention Block x L times Large Unified Transformer MVC-Loss InsScene-15K Qwen-VL 2.5 ...
- **p. 17 / A.4 TRAINING DETAILS - extractive PDF cue:** Training is performed on 8 NVIDIA A800 GPUs for 2 days using the AdamW optimizer.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Overall, train, whole, model, multi-task, loss, Loverall, Lpose, Ldepth, Lpmap, Lmvc, where, geometry, supervision | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Overall, train, whole, model, multi-task, loss, Loverall, Lpose, Ldepth, Lpmap | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | OVERVIEW, consists, main, phases, present, example, scenes, ScanNet, Dai, Yeshwanth | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | objective, structures, instance, representations, according, scene, geometry, improving, generalization, Cluster | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry supervision terms pose ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** A foundational goal in the pursuit of spatial intelligence (Yang et al., 2025) is to build representations that mirror human understanding-capturing both the precise geometric ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** 4, given N input images {Ii ∈RH×W ×3}N i=1, we aim to forge a unified representation, enabling comprehensive 3D reconstruction and understanding in a mutually ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** These masks are then used to guide state-of-the-art vision-language models (VLMs, e.g., CLIP, OpenSeg) and large multimodal models (LMMs, e.g., GPT-4o, Qwen2.5-VL) to perform open-vocabulary ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Given input images, our method encodes them into a series of Unified Token Representations, which are then processed by the Geometry Head and the Instance ...
- **p. 6 / 3 METHODOLOGY - extractive PDF cue:** 1, our method is the only one that simultaneously enables multi-view instance matching, image-to-3D reconstruction, and scene understanding, while achieving state-of-the-art performance across all tasks.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** For synthetic datasets (e.g., Aria and Infinigen), we simultaneously generate the RGB image, depth map, camera pose, and object-level segmentation masks for each rendered view.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To support arbitrary multi-view inputs while maintaining permutation equivariance, a learnable camera token is concatenated to each view's token sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 3.3 INSTANCE-GROUNDED SCENE UNDERSTANDING Unlike prior approaches that are tightly coupled with a specific language model (e.g., for OpenVocabulary Segmentation) and thus ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Time Final Time NeRF-DFF 50.33s 3min - - 3.84min Feature-3DGS 50.33s 47min - - 47.84min LSM (Multi-Views) - - 15.98s 13.72s 29.70s ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry supervision terms pose ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** IGGT, consists, three, parts, Large, Unified, Transformer, capture, Token, Representation, multiple, images, Downstream, Heads, Cross-Modal, Fusion, Block, simultaneously, predict, geometric.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 4); A.2 USE OF LARGE LANGUAGE MODELS (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our model on various OOD scenarios: outdoor scenes (ETH3D (Schops et al., 2017)), autonomous driving scenes (Waymo Open Dataset (Sun ... | p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS) |
| Semantic / temporal fusion | Figure 9: Visualization of the Class-Agnostic 3D Mask Segmentation Results. Applications of QA Scene Grounding. We present the QA application results in ... | p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENTS) |
| Robot query / planning handoff | Our method significantly outperforms graph-based grouping approaches such as VGGT+Graph Cut across all metrics, achieving an 8.83 improvement in AP. | p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 9 (8.83 AP while avoiding its expensive mesh gen) |

## Failure and Ablation Link

- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 19: Visualization on clustered masks with different granularities. A.11 ADDITIONAL VISUALIZATION ON 3D VQA As shown in Fig. 20, we showcase two tasks, object ...
- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive PDF cue:** We also conduct ablations on integrating different VLMs into our method (e.g., LSeg (Li et al., 2022), CLIP (Radford et al., 2021), OpenSeg (Ghiasi et ...
- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive PDF cue:** Without the cross-modal fusion model, the instance head struggles to capture high-resolution geometric information, leading to more difficult convergence, as reflected in the sharpness of ...
- **p. 10 / 8.83 AP while avoiding its expensive mesh gen - extractive PDF cue:** Images "Ottolegnghi" LSM Ours w/ LSeg Ours w/ CLIP "Cabinet" Ours w/OpenSeg "DALL-E" Figure 12: Visualization of our method using different VLMs. w/ Multi-Modal Fusion ...
- **p. 19 / Figure/Table caption - extractive PDF cue:** Table 6: Comparison of Different Datasets. Here, we evaluate these datasets along five dimen- sions: RGB images, camera poses, depth, instance masks, and diversity. Datasets ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Table 7: Ablation study with different values of λ of contrastive supervision. Metrics λ 0.1 0.5 1 2 10
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, we provide additional visualizations of our 3D-consistent instance features using Principal Component Analysis (PCA), along with their corresponding clustered masks, as shown in Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 17 (A.4 TRAINING DETAILS), temporal p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 7 (4 EXPERIMENTS), p. 7 (3 METHODOLOGY), p. 9 (8.83 AP while avoiding its expensive mesh gen).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
