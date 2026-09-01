# Method - Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.1. Appearance Transform Module), p. 5 (3.5.1. Appearance Transform Module), p. 3 (3.2. Scene and Data Division), p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail)): The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3).

## Method Body Digest

- **p. 6 / 3.6. Loss of Individual Partition Training - extractive PDF cue:** The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3).
- **p. 5 / 3.5.1. Appearance Transform Module - extractive PDF cue:** We propose a fine-grained appearance transform module that assigns embeddings to both individual images and each 3D Gaussian independently.
- **p. 5 / 3.5.1. Appearance Transform Module - extractive PDF cue:** To prevent the model from unnecessarily overusing transparency to fit color variations, we introduce an additional regularization term for the opacity offset, restricting transparency changes ...
- **p. 3 / 3.2. Scene and Data Division - extractive PDF cue:** We partition the scene horizontally and then assign training images to them.
- **p. 3 / 3.2.1. Point-based Visibility - extractive PDF cue:** These extracted feature points are then used to calculate the convex hull area Vij.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** Only cameras with high visibility are utilized for training.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** (a) Obtain the 3D point cloud and its corresponding 2D feature points through estimating camera poses by SfM.
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** By optimizing the attributes of the Gaussians and carrying out densification to minimize this loss, 3DGS ultimately fulfills its goal of reconstructing the target scene.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient urban-scale ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- **p. 2 / 1. Introduction - extractive PDF cue:** Experimental results demonstrate that our method outperform existing methods in terms of reconstruction quality, resource efficiency, and rendering speed, enabling the reconstruction of arbitrarily large ...

## Source Evidence Cues

- **p. 6 / 3.6. Loss of Individual Partition Training - extractive PDF cue:** The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3).
- **p. 5 / 3.5.1. Appearance Transform Module - extractive PDF cue:** We propose a fine-grained appearance transform module that assigns embeddings to both individual images and each 3D Gaussian independently.
- **p. 5 / 3.5.1. Appearance Transform Module - extractive PDF cue:** To prevent the model from unnecessarily overusing transparency to fit color variations, we introduce an additional regularization term for the opacity offset, restricting transparency changes ...
- **p. 3 / 3.2. Scene and Data Division - extractive PDF cue:** We partition the scene horizontally and then assign training images to them.
- **p. 3 / 3.2.1. Point-based Visibility - extractive PDF cue:** These extracted feature points are then used to calculate the convex hull area Vij.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** Only cameras with high visibility are utilized for training.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** (a) Obtain the 3D point cloud and its corresponding 2D feature points through estimating camera poses by SfM.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3). | p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.1. Appearance Transform Module) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We propose a fine-grained appearance transform module that assigns embeddings to both individual images and each 3D Gaussian independently. | p. 5 (3.5.1. Appearance Transform Module), p. 5 (3.5.1. Appearance Transform Module) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To prevent the model from unnecessarily overusing transparency to fit color variations, we introduce an additional regularization term for the opacity offset, ... | p. 5 (3.5.1. Appearance Transform Module), p. 3 (3.2. Scene and Data Division) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Preliminary - extractive PDF cue:** By optimizing the attributes of the Gaussians and carrying out densification to minimize this loss, 3DGS ultimately fulfills its goal of reconstructing the target scene.
- **p. 6 / 3.6. Loss of Individual Partition Training - extractive PDF cue:** The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3).
- **p. 5 / 3.5.2. Scale Regularization - extractive PDF cue:** To address this, we introduce a scale regularization with two components: a maximum constraint to prevent excessive growth and a ratio constraint to maintain reasonable ...
- **p. 3 / 3.3. In-Partition Prioritized Densification - extractive PDF cue:** The i-th Gaussian will only be considered for densification if and only if its mean gradient satisfies ¯∆Gi > τi.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** Point colors indicate gradient thresholds. 𝐵1,ܶ 1, ܦ1 𝐵2,ܶ 2, ܦ2 𝐵3,ܶ 3, ܦ3 Start Training Level 1 Level 2 Level 3 (a) Detail level ...
- **p. 5 / 3.5.1. Appearance Transform Module - extractive PDF cue:** Since normalized embeddings are used, cosine similarity is adopted to compute the loss: Lsim i,j = wi,j
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.2. Scale Regularization), p. 3 (3.3. In-Partition Prioritized Densification), p. 3 (3.4. Controllable Level-of-detail), p. 4 (3.4. Controllable Level-of-detail), p. 5 (3.5.1. Appearance Transform Module).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | unselected, image, point, cloud, scene, projected, onto, plane, compute, convex, hull, area, Obtain, corresponding | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | unselected, image, point, cloud, scene, projected, onto, plane, compute, convex | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, novel, visibility-based, data, division, strategy, in-partition | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimizing, attributes, Gaussians, carrying, densification, minimize, loss, DGS, ultimately, fulfills | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2.1. Point-based Visibility - extractive PDF cue:** For an unselected image Ii, the 3D point cloud of the scene is projected onto its image plane, and compute its convex hull area Vi.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** (a) Obtain the 3D point cloud and its corresponding 2D feature points through estimating camera poses by SfM.
- **p. 4 / 3.5. Quality Enhancements - extractive PDF cue:** Section 3.5.1 proposes the appearance transform module to ensure robust adaptation to appearance variations in images.
- **p. 5 / 3.5.1. Appearance Transform Module - extractive PDF cue:** We propose a fine-grained appearance transform module that assigns embeddings to both individual images and each 3D Gaussian independently.
- **p. 5 / 3.5.3. Depth Regularization - extractive PDF cue:** Inspired by the DNGaussian [12], we utilize Depth Anything V2 [47] to predict fine-grained depth maps from RGB images and align them to actual depths ...
- **p. 3 / 3.2.1. Point-based Visibility - extractive PDF cue:** Visibility is calculated using the 3D point cloud and its association with 2D feature points, both generated by Structure from Motion (SfM).
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, we also propose scale and depth regularization to mitigate the generation of floaters and artifacts to further improving the reconstruction quality (Section 3.5).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Regarding efficiency-related metrics-#G and FPS, while the #G in our method is not the smallest, it remains within a reasonable range and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Meanwhile, the FPS does not experience a significant decline and consistently ranks as either the best or second-best, making real-time rendering entirely ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Regarding efficiency-related metrics-#G and FPS, while the #G in our method is not the smallest, it remains within a reasonable range and ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.6. Loss of Individual Partition Training - extractive PDF cue:** The loss for partition training consists of five components: L′ = L+λsimLsim +λ∆oL∆o +λdLd +λs(Lms +Lr) (15) Where L is Equation (3).
- **p. 3 / 3.2. Scene and Data Division - extractive PDF cue:** We partition the scene horizontally and then assign training images to them.
- **p. 4 / 3.4. Controllable Level-of-detail - extractive PDF cue:** Only cameras with high visibility are utilized for training.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Impact of in-partition prioritized densification on training time and the number of Gaussians.
- **p. 4 / 3.4.1. Controllable Detail Level Generation - extractive PDF cue:** For the i-th level, upon completion of training, a checkpoint is created, and the budget, interval and downsample factor are changed to Bi+1, Ti+1 and ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** loss, partition, training, consists, five, components, simLsim, dLd, Lms, Where, Equation, fine-grained, appearance, transform, module, assigns, embeddings, individual, images, Gaussian.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Notably, we also conducted validation using Building scene from Mega-NeRF [42] as well as Residences, Sci-Art and Campus scenes from UrbanScene3D [17], ... | p. 6 (4.1. Experimental Setup), p. 7 (4.3. LOD Generation) |
| Semantic / temporal fusion | Compared to other LOD-enabled methods, our method consistently outperforms previous approaches across all three quality-related metrics. | p. 6 (4.2. Results), p. 6 (4.2. Results) |
| Robot query / planning handoff | This model significantly improves all three quality metrics across all scenes. | p. 8 (4.4. Ablation Study), p. 6 (4.2. Results) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Visualization results of ablation study. Our proposed components effectively suppress the artifacts. eras are assigmend to partitions solely based on spatial lo- cations. ...
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** We conduct ablation experiments to evaluate the impact of different components of our proposed method.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** The 2nd row of Table 3 demonstrates the effect of omitting the appearance transform model.
- **p. 6 / 4.2. Results - extractive PDF cue:** The first section of the table compares our method, with the LOD mode disabled, against other methods without LOD mode or with it disabled.
- **p. 6 / 4.2. Results - extractive PDF cue:** By comparing the results of our method with and without LOD mode, it becomes evident that the number of Gaussians is significantly reduced, leading to ...
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** But without it will lead to severe artifacts, as shown in Figure 6c.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Illustration of the appearance transform. For each image and 3D Gaussian, ℓ(G) represents the Gaussian embedding and ℓ(I) represents the image embedding, respectively. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.1. Appearance Transform Module), p. 5 (3.5.1. Appearance Transform Module), p. 3 (3.2. Scene and Data Division), p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail), objective p. 3 (3.1. Preliminary), p. 6 (3.6. Loss of Individual Partition Training), p. 5 (3.5.2. Scale Regularization), p. 3 (3.3. In-Partition Prioritized Densification), p. 4 (3.4. Controllable Level-of-detail), p. 5 (3.5.1. Appearance Transform Module), temporal p. 6 (4.2. Results), p. 6 (4.2. Results), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (2.2. Large Scale Scene Reconstruction), p. 3 (3.2. Scene and Data Division).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
