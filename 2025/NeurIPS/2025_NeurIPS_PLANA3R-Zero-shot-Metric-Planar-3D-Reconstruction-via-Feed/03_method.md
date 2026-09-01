# Method - PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=YTwRZP8mNO; PDF retrieval source: https://openreview.net/pdf/97ce495e96b390789b58ad6d64e1a93cade2a0cf.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 3 (3 Method)): These features are then processed by two transformer decoders with cross-attention to produce low-resolution decoder embeddings {Gi low}i=1,2 ∈ R H 16 × W 16 ×Ddec.

## Method Body Digest

- **p. 4 / 3 Method - extractive PDF cue:** These features are then processed by two transformer decoders with cross-attention to produce low-resolution decoder embeddings {Gi low}i=1,2 ∈ R H 16 × W 16 ...
- **p. 5 / 3 Method - extractive PDF cue:** To achieve a more compact and efficient geometric representation using fewer primitives, we propose a hierarchical primitive prediction architecture (HPPA) to fit the scene using ...
- **p. 5 / 3 Method - extractive PDF cue:** To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1
- **p. 4 / 3 Method - extractive PDF cue:** Input images {Ii}i=1,2 are first encoded in a Siamese fashion using a ViT encoder [7], producing feature maps {F i}i=1,2 ∈R H 16 × W ...
- **p. 6 / 3 Method - extractive PDF cue:** For the predicted relative pose Prel = [t, q], we use MSE loss and relative angle loss to provide supervision: Lpose = γ1
- **p. 3 / 3 Method - extractive PDF cue:** PLANA3R is a transformer-based model for two-view metric 3D reconstruction, using sparse 3D planar primitives as a scene representation.
- **p. 6 / 3 Method - extractive PDF cue:** 1 , (4) where ∗∈{low, high, selected} and β1, β2 balance the loss magnitudes for stable training.
- **p. 4 / 3 Method - extractive PDF cue:** 3.2, outline training objectives in Sec.

## Design Rationale

- **p. 5 / 3 Method - extractive PDF cue:** To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1
- **p. 2 / 1 Introduction - extractive PDF cue:** Once the model is trained, our method generates a set of 3D planar primitives that approximate indoor scenes far more efficiently than per-scene optimization methods ...
- **p. 4 / 3 Method - extractive PDF cue:** The input consists of two images I1, I2 ∈R3×H×W with camera intrinsics K1 and K2.

## Source Evidence Cues

- **p. 4 / 3 Method - extractive PDF cue:** These features are then processed by two transformer decoders with cross-attention to produce low-resolution decoder embeddings {Gi low}i=1,2 ∈ R H 16 × W 16 ...
- **p. 5 / 3 Method - extractive PDF cue:** To achieve a more compact and efficient geometric representation using fewer primitives, we propose a hierarchical primitive prediction architecture (HPPA) to fit the scene using ...
- **p. 5 / 3 Method - extractive PDF cue:** To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1
- **p. 4 / 3 Method - extractive PDF cue:** Input images {Ii}i=1,2 are first encoded in a Siamese fashion using a ViT encoder [7], producing feature maps {F i}i=1,2 ∈R H 16 × W ...
- **p. 6 / 3 Method - extractive PDF cue:** For the predicted relative pose Prel = [t, q], we use MSE loss and relative angle loss to provide supervision: Lpose = γ1
- **p. 3 / 3 Method - extractive PDF cue:** PLANA3R is a transformer-based model for two-view metric 3D reconstruction, using sparse 3D planar primitives as a scene representation.
- **p. 6 / 3 Method - extractive PDF cue:** 1 , (4) where ∗∈{low, high, selected} and β1, β2 balance the loss magnitudes for stable training.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | These features are then processed by two transformer decoders with cross-attention to produce low-resolution decoder embeddings {Gi low}i=1,2 ∈ R H 16 ... | p. 4 (3 Method), p. 5 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To achieve a more compact and efficient geometric representation using fewer primitives, we propose a hierarchical primitive prediction architecture (HPPA) to fit ... | p. 5 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = ... | p. 5 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive PDF cue:** 3.2, outline training objectives in Sec.
- **p. 5 / 3 Method - extractive PDF cue:** After the warm-up phase, we introduce a rendering loss.
- **p. 5 / 3 Method - extractive PDF cue:** 1 , (3) where ∗∈{low, high}, α1 and α2 are loss weights.
- **p. 6 / 3 Method - extractive PDF cue:** For the predicted relative pose Prel = [t, q], we use MSE loss and relative angle loss to provide supervision: Lpose = γ1
- **p. 6 / 3 Method - extractive PDF cue:** We compute the gradient magnitude for each pixel in low-resolution Npatch low and use high-resolution planar primitives only for those pixels whose gradients exceed a ...
- **p. 24 / A.2 Implementation Details - extractive PDF cue:** For our final model used for evaluation, we set the loss weights α1 = 5, α2 = 5, α3 = 20 in Eq.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 24 (A.2 Implementation Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, train, network, outputs, sparse, planar, primitives, DoF, relative, camera, pose, Prel, Given, images | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | goal, train, network, outputs, sparse, planar, primitives, DoF, relative, camera | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, challenges, facilitate, training, introduce, patch, loss, designed, stabilize, primitive | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | outline, training, objectives, Sec, After, warm-up, phase, introduce, rendering, loss | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Method - extractive PDF cue:** Our goal is to train a network F outputs a set of sparse 3D planar primitives and the 6-DoF relative camera pose Prel.
- **p. 4 / 3 Method - extractive PDF cue:** Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF relative camera pose Prel in metric scale.
- **p. 5 / 3 Method - extractive PDF cue:** For each input image, using dπ in predicted primitives, we derive the patched depth maps: Dpatch low ∈R1× H 16 × W 16 and Dpatch ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.3 Training Losses and Training Strategies For input images {Ii}i=1,2, PLANA3R generates planar primitives at both low and high resolutions.
- **p. 6 / 3 Method - extractive PDF cue:** 3.4 3D Plane Merge Given a pair of input images, once the collection of 3D planar primitives is predicted, we perform a similar merging in ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Planar reconstruction approaches include feedforward solutions in monocular [40, 16, 27, 24, 18, 42] and two-view [11, 1, 28] settings, and per-scene optimization approaches [29, ...
- **p. 6 / 3 Method - extractive PDF cue:** This process enables the extraction of semantic information for each plane and yields the final planar surface reconstruction.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In our training setup, we fix j = 1, treating I1 as the reference frame. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Then, the primitive centers ci π ∈R3 from both I1 and I2 are transformed into the coordinate frame of the camera j ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | To evaluate this capability, we tested PLANA3R on 50 eight-view samples, sampled every 20 frames from the ScanNetV2 dataset. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Method - extractive PDF cue:** To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1
- **p. 6 / 3 Method - extractive PDF cue:** 1 , (4) where ∗∈{low, high, selected} and β1, β2 balance the loss magnitudes for stable training.
- **p. 6 / 4 Experiment - extractive PDF cue:** The model is trained for a total of 256 GPU-days on NVIDIA H20 GPUs, with a per-GPU batch size of 6.
- **p. 6 / 4 Experiment - extractive PDF cue:** 4.1 Implementation Details We initialize the ViT encoder and the transformer decoder's part of PLANA3R model with DUSt3R's pre-trained 512-DPT weights.
- **p. 25 / A.3 Runtime Analysis - extractive PDF cue:** We evaluate the inference runtime of our PLANA3R using an NVIDIA RTX 3090 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** features, then, processed, transformer, decoders, cross-attention, produce, low-resolution, decoder, embeddings, Ddec, achieve, more, compact, efficient, geometric, representation, fewer, primitives, hierarchical.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | 4.2 Datasets Since PLANA3R targets structured indoor scenes, we train it on a combination of four public indoorscene datasets: ScanNetV2 [4], ScanNet++ ... | p. 6 (4 Experiment), p. 7 (4 Experiment) |
| Semantic / temporal fusion | 4.3 Baselines and Evaluation Metrics We evaluate our PLANA3R against state-of-the-art (SOTA) planar reconstruction methods across multiple tasks, including 3D reconstruction, pose ... | p. 6 (4 Experiment), p. 9 (4 Experiment) |
| Robot query / planning handoff | 1, both MASt3R and our PLANA3R significantly outperform prior learning-based planar reconstruction methods [28, 11, 1] in terms of pose estimation accuracy. | p. 7 (4 Experiment), p. 7 (4 Experiment) |

## Failure and Ablation Link

- **p. 8 / 4 Experiment - extractive PDF cue:** Here, we show that PLANA3R can perform zero-shot plane-level semantic segmentation without plane annotations.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 5: Ablation study on the gradient threshold (gth). We show the relationship between the number of per-view primitives and performance. ScanNetV2 Reconstruction NYUv2 Depth ...
- **p. 21 / A.2 Implementation Details - extractive PDF cue:** Data means training without 0.57M nonoverlapping image pairs).
- **p. 22 / A.2 Implementation Details - extractive PDF cue:** We also conduct an additional ablation study to evaluate the impact of incorporating the 0.57M non-overlapping image pairs on model performance during training.
- **p. 25 / A.5 Limitations - extractive PDF cue:** While this represents a limitation in our current analysis, it also highlights the urgent need for better benchmarks in this field.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our PLANA3R. Given two images captured from the same scene, PLANA3R outputs a set of 3D planar primitives and 6-DoF relative ...
- **p. 7 / 4 Experiment - extractive PDF cue:** This process does not require merging the primitives and can be performed with a single feed-forward pass.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 3 (3 Method), objective p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 24 (A.2 Implementation Details), temporal p. 4 (3 Method), p. 4 (3 Method), p. 7 (4 Experiment), p. 9 (4 Experiment), p. 10 (4 Experiment), p. 21 (A.2 Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
