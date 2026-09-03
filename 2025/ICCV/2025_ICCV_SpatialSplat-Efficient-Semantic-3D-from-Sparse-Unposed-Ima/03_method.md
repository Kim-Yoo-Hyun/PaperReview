# Method - SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Dual-field Architecture), p. 3 (3.1. 3D Geometry Prediction), p. 5 (3.3. Dual-field Architecture), p. 4 (3.2. Selective Gaussian Mechanism), p. 3 (3.1. 3D Geometry Prediction), p. 5 (3.3. Dual-field Architecture)): To mitigate this loss without increasing storage costs, we propose a dual-field architecture that decouples semantic representation into: 1) a fine-grained instance-aware radiance field, capturing scene geometry, textures, and instance ...

## Method Body Digest

- **p. 4 / 3.3. Dual-field Architecture - extractive body cue:** To mitigate this loss without increasing storage costs, we propose a dual-field architecture that decouples semantic representation into: 1) a fine-grained instance-aware radiance field, capturing ...
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** The features from encoder are then passed to a ViT-based decoder, where cross-attention is applied to better capture spatial relationships and aggregate information across views.
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground truth image extracted ...
- **p. 4 / 3.2. Selective Gaussian Mechanism - extractive body cue:** To address this, we propose a selective Gaussian mechanism that assigns each primitive an importance score to quantify its necessity for the scene representation.
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** Both the encoder and decoder in our geometric prediction module are built on pure ViT structures, requiring no geometric priors as in previous methods [3, ...
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** An additional advantage of dual-field architecture is that, unlike dense semantic supervision from LSeg [26], it allows the use of a much lighter pretrained model ...
- **p. 4 / 3.2. Selective Gaussian Mechanism - extractive body cue:** Therefore, we optimize βi through photometric loss minimization.
- **p. 5 / 3.4. Training Objective - extractive body cue:** Following previous methods [15], we perform end-to-end training to optimize our model with the following objective: \b egi n { s plit} \ m athcal ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we introduce a Selective Gaussian Mechanism (SGM) to eliminate redundancy in overlapping areas caused by pixelwise representations, along with a novel loss function that ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • A novel feed-forward 3DGS framework that, to the best of our knowledge, is the first to simultaneously learn semantic and ...
- **p. 3 / 3. Method - extractive body cue:** In the following sections, we provide a detailed explanation of each component of our method.

## Source Evidence Cues

- **p. 4 / 3.3. Dual-field Architecture - extractive body cue:** To mitigate this loss without increasing storage costs, we propose a dual-field architecture that decouples semantic representation into: 1) a fine-grained instance-aware radiance field, capturing ...
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** The features from encoder are then passed to a ViT-based decoder, where cross-attention is applied to better capture spatial relationships and aggregate information across views.
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground truth image extracted ...
- **p. 4 / 3.2. Selective Gaussian Mechanism - extractive body cue:** To address this, we propose a selective Gaussian mechanism that assigns each primitive an importance score to quantify its necessity for the scene representation.
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** Both the encoder and decoder in our geometric prediction module are built on pure ViT structures, requiring no geometric priors as in previous methods [3, ...
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** An additional advantage of dual-field architecture is that, unlike dense semantic supervision from LSeg [26], it allows the use of a much lighter pretrained model ...
- **Detected method headings:** 3. Method (p. 3); 3.3. Dual-field Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To mitigate this loss without increasing storage costs, we propose a dual-field architecture that decouples semantic representation into: 1) a fine-grained instance-aware ... | p. 4 (3.3. Dual-field Architecture), p. 3 (3.1. 3D Geometry Prediction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The features from encoder are then passed to a ViT-based decoder, where cross-attention is applied to better capture spatial relationships and aggregate ... | p. 3 (3.1. 3D Geometry Prediction), p. 5 (3.3. Dual-field Architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground ... | p. 5 (3.3. Dual-field Architecture), p. 4 (3.2. Selective Gaussian Mechanism) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Selective Gaussian Mechanism - extractive body cue:** Therefore, we optimize βi through photometric loss minimization.
- **p. 4 / 3.3. Dual-field Architecture - extractive body cue:** To mitigate this loss without increasing storage costs, we propose a dual-field architecture that decouples semantic representation into: 1) a fine-grained instance-aware radiance field, capturing ...
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground truth image extracted ...
- **p. 5 / 3.4. Training Objective - extractive body cue:** Following previous methods [15], we perform end-to-end training to optimize our model with the following objective: \b egi n { s plit} \ m athcal ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.2. Selective Gaussian Mechanism), p. 4 (3.2. Selective Gaussian Mechanism), p. 5 (3.3. Dual-field Architecture), p. 5 (3.3. Dual-field Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, image, patchified, flattened, sequences, along, camera, intrinsics, processed, linear, layer, encoder, Experiments, SpatialSplat | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | input, image, patchified, flattened, sequences, along, camera, intrinsics, processed, linear | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Additionally, introduce, Selective, Gaussian, Mechanism, SGM, eliminate, redundancy, overlapping, areas | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Therefore, optimize, through, photometric, loss, minimization, mitigate, without, increasing, storage | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** The input image is patchified and flattened into image sequences, which along with the camera intrinsics processed by a linear layer, are fed into the ...
- **p. 4 / 3.1. 3D Geometry Prediction - extractive body cue:** Experiments show that SpatialSplat effectively learns 3D priors from sparse unposed images without depth supervision, even while jointly learning multiple parameters and features.
- **p. 3 / 3.1. 3D Geometry Prediction - extractive body cue:** The encoder weights are shared across different input views.
- **p. 4 / 3.3. Dual-field Architecture - extractive body cue:** The instance feature map rendered at target image view with Eq.
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground truth image extracted ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments demonstrate that our method achieves state-of-the-art performance on multiple downstream 3D tasks while using only 40% of the representation parameters required by the ...
- **p. 2 / 1. Introduction - extractive body cue:** These methods follow a paradigm that generates pixel-wise Gaussian primitives from sparse posed images.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The input image is patchified and flattened into image sequences, which along with the camera intrinsics processed by a linear layer, are ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Method Latency↓ Gaussian Size ↓ Num. ↓ Feature-3DGS [52] 1069 s | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | To further incorporate semantics while avoiding the significant memory and storage costs of high-dimensional semantic features, existing methods extend this paradigm by ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Method Latency↓ Gaussian Size ↓ Num. ↓ Feature-3DGS [52] 1069 s | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** We minimize the loss between the rendered feature map at a novel view and the feature map ˆF S of the ground truth image extracted ...
- **p. 5 / 3.3. Dual-field Architecture - extractive body cue:** An additional advantage of dual-field architecture is that, unlike dense semantic supervision from LSeg [26], it allows the use of a much lighter pretrained model ...
- **p. 5 / 3.4. Training Objective - extractive body cue:** To save training time, the instance masks M are generated by SAM [21] prior to training, while the semantic feature map ˆ F S is ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For the 3D geometry prediction module, we use ViT-Large with a patch size of 16 as the encoder and ViT-Base as the decoder, both initialized ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** mitigate, loss, without, increasing, storage, costs, dual-field, architecture, decouples, semantic, representation, fine-grained, instance-aware, radiance, field, capturing, scene, geometry, textures, instance.
- **Relevant PDF headings:** 3. Method (p. 3); 3.3. Dual-field Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We filter out bad scenes and those with incomplete extrinsic parameters, resulting in a training dataset of approximately 1,500 scenes. | p. 5 (4.1. Experimental Setup), p. 8 (25.58 MB) |
| Semantic / temporal fusion | 1, SpatialSplat outperforms all compared methods, even surpassing L-Seg, which provides semantic feature supervision GT LSM LSM Ours Ours Figure 6. | p. 7 (4.2. Results and Analysis), p. 5 (4.1. Experimental Setup) |
| Robot query / planning handoff | In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last ... | p. 6 (4.1. Experimental Setup), p. 6 (4.2. Results and Analysis) |

## Failure and Ablation Link

- **p. 8 / 4.3. Ablations and Analysis - extractive body cue:** We perform ablations to answer the following questions: (1) Are the primitives removed by our selective Gaussian mechanism truly redundant?
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Qualitative results of ablations. (a) and (b) Qualitative results of importance score prediction, with red color indicating an importance score of 1 and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Quantitative Comparison in 3D Tasks on Scannet dataset. Our method outperforms both the latest SOTA semantic-aware feed-forward approach and per-scene optimization methods. "-Lite": ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of SpatialSplat. The SpatialSplat processes unposed images along with their intrinsics through a 3D geometry trans- former. The extracted features from the ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** In challenging cases where LSM fails, such as the table legs in the first two rows and the corners in the last two rows, our ...
- **p. 8 / 4.3. Ablations and Analysis - extractive body cue:** The primary issue is that per-primitive semantic learning struggles to maintain accurate semantics and fails to preserve clear instance boundaries, as illustrated in Fig.
- **p. 8 / 25.58 MB - extractive body cue:** Furthermore, as our method does not rely on dense semantic supervision, we leverage a lightweight pretrained 2D model, significantly accelerating inference speed.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.3. Dual-field Architecture), p. 3 (3.1. 3D Geometry Prediction), p. 5 (3.3. Dual-field Architecture), p. 4 (3.2. Selective Gaussian Mechanism), p. 3 (3.1. 3D Geometry Prediction), p. 5 (3.3. Dual-field Architecture), objective p. 4 (3.2. Selective Gaussian Mechanism), p. 4 (3.3. Dual-field Architecture), p. 5 (3.3. Dual-field Architecture), p. 5 (3.4. Training Objective), temporal p. 3 (3.1. 3D Geometry Prediction), p. 8 (4.2. Results and Analysis), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
