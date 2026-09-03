# Method - pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 3 (4. Image-conditioned 3D Gaussian Inference), p. 4 (4.1. Resolving Scale Ambiguity), p. 3 (4.1. Resolving Scale Ambiguity), p. 1 (Abstract), p. 2 (1. Introduction)): Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.
- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.
- **p. 4 / 4.1. Resolving Scale Ambiguity - extractive body cue:** Note that for brevity, we use h to represent the function that computes depths from bucket indices (see equations 6 and 7). date per-pixel features ...
- **p. 3 / 4.1. Resolving Scale Ambiguity - extractive body cue:** We first encode each view separately into feature volumes F and ˜F via a per-image feature encoder.
- **p. 1 / Abstract - extractive body cue:** We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.
- **p. 2 / 1. Introduction - extractive body cue:** We significantly outperform previous black-box based light field transformers on the real-world ACID and RealEstate10k datasets while drastically reducing both training and rendering cost and ...
- **p. 6 / 4.2. Gaussian Parameter Prediction - extractive body cue:** ACID RealEstate10k Inference Time (s) Memory (GB) PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Encode ↓ Render ↓ Training ↓ ...
- **p. 5 / 4.2. Gaussian Parameter Prediction - extractive body cue:** This means that in each backward pass, we assign the gradients of the loss L with respect to the opacities α to the gradients of ...

## Design Rationale

- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.
- **p. 1 / 1. Introduction - extractive body cue:** We present pixelSplat, which brings the benefits of a primitive-based 3D representation-fast and memoryefficient rendering as well as interpretable 3D structureto generalizable view synthesis.
- **p. 2 / 1. Introduction - extractive body cue:** We demonstrate the efficacy of our method by showcasing, for the first time, how a 3D Gaussian splatting representation can be predicted in a single ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.
- **p. 3 / 4. Image-conditioned 3D Gaussian Inference - extractive body cue:** Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module.
- **p. 4 / 4.1. Resolving Scale Ambiguity - extractive body cue:** Note that for brevity, we use h to represent the function that computes depths from bucket indices (see equations 6 and 7). date per-pixel features ...
- **p. 3 / 4.1. Resolving Scale Ambiguity - extractive body cue:** We first encode each view separately into feature volumes F and ˜F via a per-image feature encoder.
- **p. 1 / Abstract - extractive body cue:** We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images.
- **p. 2 / 1. Introduction - extractive body cue:** We significantly outperform previous black-box based light field transformers on the real-world ACID and RealEstate10k datasets while drastically reducing both training and rendering cost and ...
- **p. 6 / 4.2. Gaussian Parameter Prediction - extractive body cue:** ACID RealEstate10k Inference Time (s) Memory (GB) PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Encode ↓ Render ↓ Training ↓ ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time. | p. 1 (Abstract), p. 3 (4. Image-conditioned 3D Gaussian Inference) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our method consists of a two-view image encoder and a pixel-aligned Gaussian prediction module. | p. 3 (4. Image-conditioned 3D Gaussian Inference), p. 4 (4.1. Resolving Scale Ambiguity) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Note that for brevity, we use h to represent the function that computes depths from bucket indices (see equations 6 and 7). ... | p. 4 (4.1. Resolving Scale Ambiguity), p. 3 (4.1. Resolving Scale Ambiguity) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2. Gaussian Parameter Prediction - extractive body cue:** This means that in each backward pass, we assign the gradients of the loss L with respect to the opacities α to the gradients of ...
- **p. 1 / 1. Introduction - extractive body cue:** Next, optimizing primitive parameters directly via gradient descent suffers from local minima.
- **p. 2 / 1. Introduction - extractive body cue:** When receiving a gradient that would increase the opacity of a Gaussian at a 3D location, our model increases the probability that the Gaussian will ...
- **p. 5 / 4.2. Gaussian Parameter Prediction - extractive body cue:** In this case, gradient descent decreases the opacity of the Gaussian, lowering the probability of further incorrect depth predictions.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, in the generalizable case, we need to back-propagate gradients through the representation and thus cannot rely on non-differentiable operations.
- **p. 2 / 1. Introduction - extractive body cue:** We significantly outperform previous black-box based light field transformers on the real-world ACID and RealEstate10k datasets while drastically reducing both training and rendering cost and ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.2. Gaussian Parameter Prediction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Resolving Scale Ambiguity), p. 4 (4.1. Resolving Scale Ambiguity).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | investigate, problem, generalizable, novel, view, synthesis, sparse, image, observations, Given, pair, input, images, pixelSplat | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | investigate, problem, generalizable, novel, view, synthesis, sparse, image, observations, Given | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | consists, two-view, image, encoder, pixel-aligned, Gaussian, prediction, module, present, pixelSplat | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | means, backward, pass, assign, gradients, loss, respect, opacities, depth, probability | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** We investigate the problem of generalizable novel view synthesis from sparse image observations.
- **p. 1 / 1. Introduction - extractive body cue:** Given a pair of input images, pixelSplat reconstructs a 3D radiance field parameterized via 3D Gaussian primitives.
- **p. 4 / 4.1. Resolving Scale Ambiguity - extractive body cue:** For every pixel feature F[u] in the input feature map, a neural network f predicts Gaussian primitive parameters Σ and S.
- **p. 3 / 4.1. Resolving Scale Ambiguity - extractive body cue:** In practice, this means that a neural network making predictions about the geometry of a scene from a single image cannot possibly predict the depth ...
- **p. 2 / 1. Introduction - extractive body cue:** We significantly outperform previous black-box based light field transformers on the real-world ACID and RealEstate10k datasets while drastically reducing both training and rendering cost and ...
- **p. 4 / 4.1. Resolving Scale Ambiguity - extractive body cue:** Note that this mechanism can be extended to more than two input views.
- **p. 6 / 4.2. Gaussian Parameter Prediction - extractive body cue:** We outperform all baseline methods in terms PSNR, LPIPS, and SSIM for novel view synthesis on the real-world RealEstate10k and ACID datasets.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Meanwhile, recent work on single-scene novel view synthesis has shown that it is possible to use 3D Gaussian primitives to enable real-time ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.
- **p. 2 / 1. Introduction - extractive body cue:** We significantly outperform previous black-box based light field transformers on the real-world ACID and RealEstate10k datasets while drastically reducing both training and rendering cost and ...
- **p. 6 / 4.2. Gaussian Parameter Prediction - extractive body cue:** ACID RealEstate10k Inference Time (s) Memory (GB) PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Encode ↓ Render ↓ Training ↓ ...
- **p. 6 / 5.2. Results - extractive body cue:** Our method also uses significantly less memory per ray at training time.
- **p. 6 / 4.2. Gaussian Parameter Prediction - extractive body cue:** ACID RealEstate10k Inference Time (s) Memory (GB) PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Encode ↓ Render ↓ Training ↓ ...
- **p. 1 / Abstract - extractive body cue:** Our model features real-time and memory-efficient rendering for scalable training as well as fast 3D reconstruction at inference time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, features, real-time, memory-efficient, rendering, scalable, training, well, fast, reconstruction, inference, time, consists, two-view, image, encoder, pixel-aligned, Gaussian, prediction, module.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Both datasets include camera poses computed by SfM software, necessitating the scale-aware design discussed in Section 4.1. | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |
| Semantic / temporal fusion | Because the prior state-of-the-art wide-baseline novel view synthesis model by Du et al. | p. 6 (5.1. Experimental Setup), p. 6 (5.2. Results) |
| Robot query / planning handoff | Our method outperforms the baselines on all metrics, with especially significant improvements in perceptual distance (LPIPS). | p. 6 (5.2. Results), p. 8 (5.3. Ablations and Analysis) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Ablations. Without the epipolar transformer, our model is unable to resolve scale ambiguity, leading to ghosting artifacts. Without our sampling approach, our model ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For the "Plus Depth Regularization" ablation, we regularize depth maps by fine-tuning with 50,000 steps of edge-aware total variation regularization.
- **p. 6 / 5. Experiments - extractive body cue:** In this section, we describe our experimental setup, evaluate our method on wide-baseline novel view synthesis from image pairs, and perform ablations to validate our ...
- **p. 7 / 5.3. Ablations and Analysis - extractive body cue:** We perform ablations on RealEstate10k to answer the following questions: • Question 1a: Is our epipolar encoder responsible for our model's ability to handle scale ...
- **p. 8 / 5.3. Ablations and Analysis - extractive body cue:** To measure our epipolar encoding scheme's importance, we compare pixelSplat to a variant (No Epipolar Encoder) that eschews epipolar encoding.
- **p. 7 / 5.2. Results - extractive body cue:** We visualize point clouds using the version of our model that has been fine-tuned with a depth regularizer.
- **p. 8 / 6. Conclusion - extractive body cue:** Without our sampling approach, our model falls into local minima that manifest themselves as speckling artifacts.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 3 (4. Image-conditioned 3D Gaussian Inference), p. 4 (4.1. Resolving Scale Ambiguity), p. 3 (4.1. Resolving Scale Ambiguity), p. 1 (Abstract), p. 2 (1. Introduction), objective p. 5 (4.2. Gaussian Parameter Prediction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2. Gaussian Parameter Prediction), p. 1 (1. Introduction), p. 2 (1. Introduction), temporal p. 1 (Abstract), p. 1 (1. Introduction), p. 6 (5.2. Results), p. 6 (5.1. Experimental Setup), p. 8 (5.3. Ablations and Analysis), p. 2 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
