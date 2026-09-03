# Method - SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Overall Framework), p. 4 (3.4. LR Image to HR 3DGS Mapping), p. 5 (3.4. LR Image to HR 3DGS Mapping), p. 5 (3.4. LR Image to HR 3DGS Mapping), p. 6 (3.5. Gaussian Offset Learning), p. 6 (3.5. Gaussian Offset Learning)): The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement module, a ViT decoder, and ...

## Method Body Digest

- **p. 4 / 3.2. Overall Framework - extractive body cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** It adopts a transformer-based architecture composed of a ViT encoder, a feature refinement module, a ViT decoder, and a Gaussian offset learning module.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The two attention outputs Uo←p and Up←o are then concatenated and fused through a fully connected layer to generate the refined feature token tca.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The decoded features are then provided to the Gaussian offset learning module (Section 3.5) to estimate residual corrections from the densified representation GDense to the ...
- **p. 6 / 3.5. Gaussian Offset Learning - extractive body cue:** These queried features are aggregated together with the Gaussian center and camera intrinsics K, and passed into a PointTransformerV3 network for spatial reasoning and multi-scale ...
- **p. 6 / 3.5. Gaussian Offset Learning - extractive body cue:** The encoded feature F is then fed into a Gaussian Head ΨGH, a lightweight MLP that predicts residual offsets for the Gaussian parameters: \ Delt ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We reformulate 3DGS-based 3DSR as a feed-forward mapping problem from LR multi-view images to an HR 3DGS representation.
- **p. 6 / 3.6. Training Objective - extractive body cue:** Following [38], we adopt a combination of pixel-wise reconstruction loss (MSE) and perceptual consistency loss (LPIPS) to jointly preserve geometric accuracy and visual fidelity.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows. • A novel formulation of 3DSR.
- **p. 2 / 1. Introduction - extractive body cue:** We propose SR3R, a feed-forward framework that directly reconstructs HR 3DGS from as few as two LR views through a learned mapping network.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.

## Source Evidence Cues

- **p. 4 / 3.2. Overall Framework - extractive body cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** It adopts a transformer-based architecture composed of a ViT encoder, a feature refinement module, a ViT decoder, and a Gaussian offset learning module.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The two attention outputs Uo←p and Up←o are then concatenated and fused through a fully connected layer to generate the refined feature token tca.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The decoded features are then provided to the Gaussian offset learning module (Section 3.5) to estimate residual corrections from the densified representation GDense to the ...
- **p. 6 / 3.5. Gaussian Offset Learning - extractive body cue:** These queried features are aggregated together with the Gaussian center and camera intrinsics K, and passed into a PointTransformerV3 network for spatial reasoning and multi-scale ...
- **p. 6 / 3.5. Gaussian Offset Learning - extractive body cue:** The encoded feature F is then fed into a Gaussian Head ΨGH, a lightweight MLP that predicts residual offsets for the Gaussian parameters: \ Delt ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We reformulate 3DGS-based 3DSR as a feed-forward mapping problem from LR multi-view images to an HR 3DGS representation.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, ... | p. 4 (3.2. Overall Framework), p. 4 (3.4. LR Image to HR 3DGS Mapping) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | It adopts a transformer-based architecture composed of a ViT encoder, a feature refinement module, a ViT decoder, and a Gaussian offset learning ... | p. 4 (3.4. LR Image to HR 3DGS Mapping), p. 5 (3.4. LR Image to HR 3DGS Mapping) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The two attention outputs Uo←p and Up←o are then concatenated and fused through a fully connected layer to generate the refined feature ... | p. 5 (3.4. LR Image to HR 3DGS Mapping), p. 5 (3.4. LR Image to HR 3DGS Mapping) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.6. Training Objective - extractive body cue:** Following [38], we adopt a combination of pixel-wise reconstruction loss (MSE) and perceptual consistency loss (LPIPS) to jointly preserve geometric accuracy and visual fidelity.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Unlike prior methods that rely on dense inputs and per-scene optimization supervised by pseudo-HR 2D labels, our formulation enables direct HR 3DGS reconstruction from as ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.6. Training Objective).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | task, become, increasingly, critical, because, state-of-the-art, Gaussian, Splatting, DGS, reconstruction, methods, typically, require, dense | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | task, become, increasingly, critical, because, state-of-the-art, Gaussian, Splatting, DGS, reconstruction | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, novel, formulation, DSR, SR3R, feed-forward, framework, directly | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Following, adopt, combination, pixel-wise, reconstruction, loss, MSE, perceptual, consistency, LPIPS | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** This task has become increasingly critical because state-of-the-art 3D Gaussian Splatting (3DGS)-based reconstruction methods [14, 25] typically require dense and high-resolution input views to recover ...
- **p. 2 / 1. Introduction - extractive body cue:** Current 3DSR methods [9, 15, 24, 40] typically employ pretrained 2D image or video super-resolution (2DSR) models to generate pseudo-HR images from dense multiview LR ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Formally, given a set of V LR input views with camera intrinsics {(Iv lr, Kv)}V v=1, our goal is to learn a feedforward mapping function ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The mapping network is the core of SR3R, learning a viewconsistent transformation from LR input images to feature representations used for HR 3DGS reconstruction.
- **p. 4 / 3.2. Overall Framework - extractive body cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** DepthSplat Up-DepthSplat NoPoSplat Up-NoPoSplat Ours (DepthSplat) Ours (NoPoSplat) Inputs GT Figure 3.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** SR3R delivers significantly sharper details and more stable geometry than DepthSplat, NoPoSplat, and their upsampled variants, consistently improving reconstruction quality across different 3DGS backbones under ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | An overview of the proposed SR3R framework is illustrated in Figure 2. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Each GLR is then densified via a Gaussian Shuffle Split operation [27] to produce GDense, which provides a structural scaffold for highfrequency ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | SR3R consistently and substantially outperforms all baselines and their upscaled-input versions across PSNR, SSIM, and LPIPS, with only moderate Gaussian complexity and ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Both the backbone and our mapping network are trained for 75,000 iterations with a batch size of 8 and a learning rate ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Both the backbone and our mapping network are trained for 75,000 iterations with a batch size of 8 and a learning rate of 2.5×10-5.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Incorporating bidirectional cross-attention further enhances structural consistency by injecting geometric priors from the pretrained 3DGS encoder.
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** Two crossattentions are computed in opposite directions: \b e gin {al i gned} \mathbf { U}_ { o \ leftar r o w p} & ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** input, images, upsampled, target, resolution, processed, mapping, network, consists, ViT, encoder, feature, refinement, module, decoder, Gaussian, offset, learning, adopts, transformer-based.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We further evaluate the zero-shot generalization ability of SR3R on the DTU dataset, a challenging object-centric benchmark with unseen geometries and illumination ... | p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup) |
| Semantic / temporal fusion | Table 1. Quantitative comparison of 4× 3DSR on the large-scale RE10K and ACID datasets. SR3R consistently and substantially outperforms all baselines and ... | p. 6 (Figure/Table caption), p. 7 (4.3. Zero-Shot Generalization) |
| Robot query / planning handoff | Table 3. Component-wise ablation on RE10K (4× 3DSR). Modules are added cumulatively to the NoPoSplat baseline. Each component improves performance, and Gaussian ... | p. 8 (Figure/Table caption), p. 8 (4.4. Ablation Study) |

## Failure and Ablation Link

- **p. 7 / 4.1. Experimental Setup - extractive body cue:** Qualitative ablation results of SR3R components.
- **p. 7 / 4.3. Zero-Shot Generalization - extractive body cue:** All feed-forward models, including SR3R and baselines, are trained on RE10K and directly tested on DTU without any fine-tuning.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Component-wise ablation on RE10K (4× 3DSR).
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** This setup allows us to evaluate large-scale 3DSR performance and demonstrate SR3R's superior zero-shot capability without scene-specific optimization.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ablation on upsampling strategies on RE10K (4× 3DSR).
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the SR3R framework. Given two LR input views, a feed-forward 3DGS backbone produces an LR 3DGS, which is then densified via ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison with SOTA feed-forward 3DGS reconstruction methods on Re10k (top three) and ACID (bottom three) datasets. SR3R delivers significantly sharper details and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Overall Framework), p. 4 (3.4. LR Image to HR 3DGS Mapping), p. 5 (3.4. LR Image to HR 3DGS Mapping), p. 5 (3.4. LR Image to HR 3DGS Mapping), p. 6 (3.5. Gaussian Offset Learning), p. 6 (3.5. Gaussian Offset Learning), objective p. 6 (3.6. Training Objective), p. 3 (3.1. Problem Formulation), temporal p. 4 (3.2. Overall Framework), p. 4 (3.2. Overall Framework), p. 5 (3.5. Gaussian Offset Learning), p. 6 (3.5. Gaussian Offset Learning), p. 6 (3.5. Gaussian Offset Learning), p. 7 (4.2. Comparison with State-of-the-Art).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
