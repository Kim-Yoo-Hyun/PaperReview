# Method - TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Architecture), p. 4 (3.4. Token Fusion for Scene Reconstruction), p. 4 (3.3. Asymmetric Dual-Flow Decoder), p. 3 (3.2. Architecture), p. 2 (3.1. Problem Formulation), p. 5 (3.6. Loss Functions)): The outputs of these decoders are then utilized in two parallel branches: the Camera Pose Estimation Head predicts per-view camera transformations, while the Token-aligned Gaussian Prediction module aggregates multi-view tokens ...

## Method Body Digest

- **p. 3 / 3.2. Architecture - extractive body cue:** The outputs of these decoders are then utilized in two parallel branches: the Camera Pose Estimation Head predicts per-view camera transformations, while the Token-aligned Gaussian ...
- **p. 4 / 3.4. Token Fusion for Scene Reconstruction - extractive body cue:** Multi-scale features {Fi}nl i=1 from different layers of the Transformer decoder corresponding to the fused tokens are first upsampled and linearly projected: ˆFi = Proji(Fi), ...
- **p. 4 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** The ADF-Decoder consists of 12 decoder blocks.
- **p. 3 / 3.2. Architecture - extractive body cue:** To establish a canonical scene representation, the reference view I1 is decoded using a ViT decoder with cross-attention to other views.
- **p. 2 / 3.1. Problem Formulation - extractive body cue:** We aim to learn a feed-forward network that jointly reconstructs 3D Gaussians and predicts camera poses from a sequence of N unposed images {Ii}N i=1, ...
- **p. 5 / 3.6. Loss Functions - extractive body cue:** The model is trained end-to-end with the total loss: L = Lrender + λcLpose, (17) where λc balances the contribution of the camera pose supervision.
- **p. 5 / 3.6. Loss Functions - extractive body cue:** The overall camera pose loss is: Lpose = LMSE(P, ˆP) + Lalign.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** (2) During training, both the 3D Gaussian attributes and camera poses are jointly optimized.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • We propose TokenSplat, a feed-forward pose-free reconstruction framework that jointly estimates camera poses and 3D Gaussian ...
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose TokenSplat, a feed-forward 3D Gaussian splatting framework that reconstructs 3D scenes from an arbitrary number of unposed images while ...
- **p. 2 / 1. Introduction - extractive body cue:** To jointly optimize 3D reconstruction and camera pose estimation within a feed-forward architecture, we introduce learnable camera tokens and an Asymmetric DualFlow Decoder (ADF-Decoder) that ...

## Source Evidence Cues

- **p. 3 / 3.2. Architecture - extractive body cue:** The outputs of these decoders are then utilized in two parallel branches: the Camera Pose Estimation Head predicts per-view camera transformations, while the Token-aligned Gaussian ...
- **p. 4 / 3.4. Token Fusion for Scene Reconstruction - extractive body cue:** Multi-scale features {Fi}nl i=1 from different layers of the Transformer decoder corresponding to the fused tokens are first upsampled and linearly projected: ˆFi = Proji(Fi), ...
- **p. 4 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** The ADF-Decoder consists of 12 decoder blocks.
- **p. 3 / 3.2. Architecture - extractive body cue:** To establish a canonical scene representation, the reference view I1 is decoded using a ViT decoder with cross-attention to other views.
- **p. 2 / 3.1. Problem Formulation - extractive body cue:** We aim to learn a feed-forward network that jointly reconstructs 3D Gaussians and predicts camera poses from a sequence of N unposed images {Ii}N i=1, ...
- **p. 5 / 3.6. Loss Functions - extractive body cue:** The model is trained end-to-end with the total loss: L = Lrender + λcLpose, (17) where λc balances the contribution of the camera pose supervision.
- **p. 5 / 3.6. Loss Functions - extractive body cue:** The overall camera pose loss is: Lpose = LMSE(P, ˆP) + Lalign.
- **Detected method headings:** 3. Method (p. 2); 3.2. Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The outputs of these decoders are then utilized in two parallel branches: the Camera Pose Estimation Head predicts per-view camera transformations, while ... | p. 3 (3.2. Architecture), p. 4 (3.4. Token Fusion for Scene Reconstruction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Multi-scale features {Fi}nl i=1 from different layers of the Transformer decoder corresponding to the fused tokens are first upsampled and linearly projected: ... | p. 4 (3.4. Token Fusion for Scene Reconstruction), p. 4 (3.3. Asymmetric Dual-Flow Decoder) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The ADF-Decoder consists of 12 decoder blocks. | p. 4 (3.3. Asymmetric Dual-Flow Decoder), p. 3 (3.2. Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.6. Loss Functions - extractive body cue:** The overall camera pose loss is: Lpose = LMSE(P, ˆP) + Lalign.
- **p. 5 / 3.6. Loss Functions - extractive body cue:** The model is trained end-to-end with the total loss: L = Lrender + λcLpose, (17) where λc balances the contribution of the camera pose supervision.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** (2) During training, both the 3D Gaussian attributes and camera poses are jointly optimized.
- **p. 3 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** To prevent entangling viewpoint-specific cues with scene semantics, it employs an asymmetric update scheme where image tokens primarily aggregate scene context, whereas camera tokens extract ...
- **p. 4 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** The updates are computed as: ˆtI i ←Softmax  QI iKI i ⊤/ √ d 
- **p. 4 / 3.4. Token Fusion for Scene Reconstruction - extractive body cue:** Features are then progressively fused from deep to shallow layers using the residual fusion module RF composed of residual blocks and upsampling: F fusion nl ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.6. Loss Functions), p. 5 (3.6. Loss Functions), p. 3 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.3. Asymmetric Dual-Flow Decoder).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | camera, pose, estimation, network, predicts, per-view, poses, transform, input, image, canonical, reference, view, Recent | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | camera, pose, estimation, network, predicts, per-view, poses, transform, input, image | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, main, contributions, follows, TokenSplat, feed-forward, pose-free, reconstruction, framework, jointly | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | overall, camera, pose, loss, Lpose, LMSE, Lalign, model, trained, end-to-end | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** For camera pose estimation, the network predicts per-view poses Pi that transform each input image Ii into the canonical reference view I1.
- **p. 1 / 1. Introduction - extractive body cue:** Recent feed-forward variants [1, 5, 18, 40, 50] alleviate this by predicting 3D Gaussians directly from input images, but their applicability remains constrained by the ...
- **p. 3 / 3.2. Architecture - extractive body cue:** Each input view is first encoded into image tokens via a shared ViT Encoder.
- **p. 2 / 1. Introduction - extractive body cue:** To jointly optimize 3D reconstruction and camera pose estimation within a feed-forward architecture, we introduce learnable camera tokens and an Asymmetric DualFlow Decoder (ADF-Decoder) that ...
- **p. 2 / 3.1. Problem Formulation - extractive body cue:** We aim to learn a feed-forward network that jointly reconstructs 3D Gaussians and predicts camera poses from a sequence of N unposed images {Ii}N i=1, ...
- **p. 4 / 3.3. Asymmetric Dual-Flow Decoder - extractive body cue:** Camera tokens attend to their corresponding image tokens to extract geometric cues for pose estimation.
- **p. 1 / 1. Introduction - extractive body cue:** More recent posefree frameworks [15, 31, 36, 44] attempt to infer both camera poses and 3D structure directly from sparse unposed images.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We aim to learn a feed-forward network that jointly reconstructs 3D Gaussians and predicts camera poses from a sequence of N unposed ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For each input view, the RGB image is divided into patches and embedded as a sequence of image tokens. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.6. Loss Functions - extractive body cue:** The model is trained end-to-end with the total loss: L = Lrender + λcLpose, (17) where λc balances the contribution of the camera pose supervision.
- **p. 6 / 4.2. Experimental Results - extractive body cue:** This gain stems from our directionally constrained ADF-Decoder, which enforces disentangled interaction between camera and image tokens, leading to more stable pose learning.
- **p. 8 / 4.3. Ablation Analysis - extractive body cue:** Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with SSIM ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** outputs, decoders, then, utilized, parallel, branches, Camera, Pose, Estimation, Head, predicts, per-view, transformations, while, Token-aligned, Gaussian, Prediction, module, aggregates, multi-view.
- **Relevant PDF headings:** 3. Method (p. 2); 3.2. Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our method on novel view synthesis (NVS) and camera pose estimation across sparse and long-sequence real-world datasets. | p. 5 (4. Experiment), p. 6 (4.2. Experimental Results) |
| Semantic / temporal fusion | As can be seen, TokenSplat consistently outperforms state-of-the-art pose-free methods, including those specifically designed for multi-view input such as VicaSplat and AnySplat, ... | p. 5 (4.2. Experimental Results), p. 6 (4.2. Experimental Results) |
| Robot query / planning handoff | Moreover, as the number of input images increases, our model achieves a higher SSIM of 0.061 over FreeSplat, while also showing improved ... | p. 6 (4.2. Experimental Results), p. 5 (4.2. Experimental Results) |

## Failure and Ablation Link

- **p. 8 / 4.2. Experimental Results - extractive body cue:** Component ablations on RE10K (8 view).
- **p. 8 / 4.3. Ablation Analysis - extractive body cue:** We perform ablation studies on RE10K (8 views), summarized in Tab.
- **p. 5 / 4.2. Experimental Results - extractive body cue:** Here, AnySplat refers to zero-shot results trained on other datasets, while AnySplat∗ denotes the results we achieved after fine-tuning on the corresponding dataset.
- **p. 8 / 5. Conclusion - extractive body cue:** It yields consistent accuracy improvements and robust zero-shot generalization across diverse datasets.
- **p. 5 / 4.2. Experimental Results - extractive body cue:** Despite the difference in view counts, TokenSplat maintains stable reconstruction quality, while competing methods, including AnySplat, which fuses pixel-aligned Gaussians by predicting fusion confidence, and ...
- **p. 6 / 4.2. Experimental Results - extractive body cue:** FreeSplat generates numerous scattered Gaussians, while NoPoSplat and SPFSplat show poor scalability and fail to generalize to unseen distant viewpoints.
- **p. 6 / 4.2. Experimental Results - extractive body cue:** On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, confirming both robustness and scalability of TokenSplat ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.2. Architecture), p. 4 (3.4. Token Fusion for Scene Reconstruction), p. 4 (3.3. Asymmetric Dual-Flow Decoder), p. 3 (3.2. Architecture), p. 2 (3.1. Problem Formulation), p. 5 (3.6. Loss Functions), objective p. 5 (3.6. Loss Functions), p. 5 (3.6. Loss Functions), p. 3 (3.1. Problem Formulation), p. 3 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.3. Asymmetric Dual-Flow Decoder), p. 4 (3.4. Token Fusion for Scene Reconstruction), temporal p. 2 (3.1. Problem Formulation), p. 3 (3.2. Architecture), p. 5 (4.1. Experimental Settings), p. 5 (4. Experiment), p. 6 (4.2. Experimental Results), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
