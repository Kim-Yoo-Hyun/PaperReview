# Method - Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.3. Text-query based 3D localization), p. 6 (3.3. Text-query based 3D localization), p. 5 (3.2. Product-Quantized CLIP embeddings), p. 4 (3.1. Feature registration process)): Moreover, we propose to use a Product Quantization (PQ) feature encoding method to represent embeddings compactly and efficiently without any per-scene optimization.

## Method Body Digest

- **p. 2 / 1. Introduction - extractive PDF cue:** Moreover, we propose to use a Product Quantization (PQ) feature encoding method to represent embeddings compactly and efficiently without any per-scene optimization.
- **p. 2 / 1. Introduction - extractive PDF cue:** Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method ...
- **p. 6 / 3.3. Text-query based 3D localization - extractive PDF cue:** After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates direct interaction with ...
- **p. 6 / 3.3. Text-query based 3D localization - extractive PDF cue:** Given a text, we first extract a query feature q using CLIP text encoder [31].
- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** During the feature registration process, our algorithm iterates through training images of the scene.
- **p. 4 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** LangSplat [30] addresses this by introducing an encoder-decoder network, while LeGaussian [34] and OpenGaussian [37] utilize codebook construc14140
- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** The centroid indices ji = [ji1, ji2, . . . , jiL] are optimized by minimizing arg mink∥vi -sik∥to quantize a given vector vi where ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We propose Dr.
- **p. 3 / 3. Dr. Splat - extractive PDF cue:** Then, we introduce Product Quantization (PQ) into our framework to efficiently store Gaussian-registered language embeddings, Sec.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive PDF cue:** Moreover, we propose to use a Product Quantization (PQ) feature encoding method to represent embeddings compactly and efficiently without any per-scene optimization.
- **p. 2 / 1. Introduction - extractive PDF cue:** Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding method ...
- **p. 6 / 3.3. Text-query based 3D localization - extractive PDF cue:** After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates direct interaction with ...
- **p. 6 / 3.3. Text-query based 3D localization - extractive PDF cue:** Given a text, we first extract a query feature q using CLIP text encoder [31].
- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** During the feature registration process, our algorithm iterates through training images of the scene.
- **p. 4 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** LangSplat [30] addresses this by introducing an encoder-decoder network, while LeGaussian [34] and OpenGaussian [37] utilize codebook construc14140
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Moreover, we propose to use a Product Quantization (PQ) feature encoding method to represent embeddings compactly and efficiently without any per-scene optimization. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the ... | p. 2 (1. Introduction), p. 6 (3.3. Text-query based 3D localization) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates ... | p. 6 (3.3. Text-query based 3D localization), p. 6 (3.3. Text-query based 3D localization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** The centroid indices ji = [ji1, ji2, . . . , jiL] are optimized by minimizing arg mink∥vi -sik∥to quantize a given vector vi where ...
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** The proposed process can be interpreted as an inverse volume rendering without gradient-based optimization, which enables our method to be faster than the prior methods ...
- **p. 1 / 1. Introduction - extractive PDF cue:** The 2D approach relies on multiview rendering, incurring high computational costs.
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** The weights are computed with the volume rendering equation Eq.
- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** However, these approaches introduce additional perscene computational costs for scene-specific parameter tuning of neural networks or codebooks (see Fig.
- **p. 1 / 1. Introduction - extractive PDF cue:** First, we found that there is a discrepancy between optimized embeddings in 3D Gaussians and 2D language-aligned embeddings.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process), p. 6 (3.2. Product-Quantized CLIP embeddings).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | After, training, Gaussians, ours, feature, registration, process, describe, details, inference, mode, facilitates, direct, interaction | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | After, training, Gaussians, ours, feature, registration, process, describe, details, inference | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Splat, direct, registration, referencing, language-aligned, features, Gaussians, bypassing, intermediate, rendering | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | centroid, indices, jiL, optimized, minimizing, mink, quantize, given, vector, where | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.3. Text-query based 3D localization - extractive PDF cue:** After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates direct interaction with ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our method bypasses the rendering stage, enabling direct interaction with 3D Gaussians for registering and referring the well-preserved language-aligned CLIP embeddings in the 3D space.
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** (1) as: w_i (\ m athbf { I }, \ma thbf {r}) = T_i(\mathbf {I}, \mathbf {r})\cdot \tilde {\alpha _i}(\mathbf {I}, \mathbf {r}), \label {eq:weight ...
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** Given training images, we extracts a dictionary of binary masks and language embeddings extracted from the images as: Fmap = {Mj : f map j ...
- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- **p. 6 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** In our setup for language-based 3D scene understanding, we build PQ centroids based on CLIP embeddings using a large-scale image dataset, the LVIS dataset [10], ...
- **p. 1 / 1. Introduction - extractive PDF cue:** This unique representation uses 3D Gaussians to achieve high-quality scene rendering, offering a more structured representation that addresses some limitations of point clouds.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | By preserving the richness of embeddings while reducing memory usage, PQ is integral to our framework's high scalability and its ability to ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | PQ introduces a trade-off between memory usage, computational efficiency, and accuracy. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | By preserving the richness of embeddings while reducing memory usage, PQ is integral to our framework's high scalability and its ability to ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.3. Text-query based 3D localization - extractive PDF cue:** After training 3D Gaussians Φours with our feature registration process and PQ, we describe the details of an inference mode that facilitates direct interaction with ...
- **p. 5 / 3.2. Product-Quantized CLIP embeddings - extractive PDF cue:** In contrast, we propose to use Product Quantization (PQ) on a large-scale image dataset, eliminating per-scene training.
- **p. 4 / 3.1. Feature registration process - extractive PDF cue:** During the feature registration process, our algorithm iterates through training images of the scene.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Moreover, Product, Quantization, feature, encoding, represent, embeddings, compactly, efficiently, without, per-scene, optimization, Splat, direct, registration, referencing, language-aligned, features, Gaussians, bypassing.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.1), we use the LERF [17] dataset annotated by LangSplat [30], which consists of several multi-view images of 3D scenes containing long-tail ... | p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Semantic / temporal fusion | The results demonstrate that our method performs better object selection in most scenes, showing an improvement of over 0.5 in mIoU and ... | p. 7 (4.1. 3D object selection), p. 7 (4. Experiments) |
| Robot query / planning handoff | Even with the 3D space search method, OpenGaussian [37], our model consistently demonstrates superior performance and achieves higher accuracy in localization. | p. 8 (4.2. 3D object localization), p. 8 (4.4. Ablation study) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed ...
- **p. 7 / 4. Experiments - extractive PDF cue:** 2, without modification, global search over a whole scene is quite demanding.
- **p. 8 / 4.4. Ablation study - extractive PDF cue:** Ablation study on (a) PQ and (b) Top-k Gaussians.
- **p. 8 / 4.4. Ablation study - extractive PDF cue:** We conduct an ablation study using the ScanNet dataset on different hyper-parameters of Dr.
- **p. 7 / 4. Experiments - extractive PDF cue:** Splat (ours) model on the same RGB-pretrained 3DGS.
- **p. 7 / 4.1. 3D object selection - extractive PDF cue:** For LangSplat-m, the activations often shows random 3D Gaussians or fail to localize entirely (e.g., see "coffee mug"), highlighting the limitations of rasterization-based methods and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.3. Text-query based 3D localization), p. 6 (3.3. Text-query based 3D localization), p. 5 (3.2. Product-Quantized CLIP embeddings), p. 4 (3.1. Feature registration process), objective p. 5 (3.2. Product-Quantized CLIP embeddings), p. 4 (3.1. Feature registration process), p. 1 (1. Introduction), p. 4 (3.1. Feature registration process), p. 5 (3.2. Product-Quantized CLIP embeddings), p. 1 (1. Introduction), temporal p. 2 (1. Introduction), p. 8 (4.4. Ablation study), p. 8 (4.4. Ablation study), p. 2 (1. Introduction), p. 3 (3. Dr. Splat), p. 3 (2. Related Work and Motivation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
