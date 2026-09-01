# Method - MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=5uw1GRBFoT&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Scene graph), p. 4 (4.1. Scene graph), p. 5 (4.2. Local reconstruction), p. 5 (4.2. Local reconstruction)): In a nutshell, we consider the output 𝐹of the encoder as a bag of local features, apply feature whitening, quantize them according to a codebook previously obtained by k-means clustering, ...

## Method Body Digest

- **p. 4 / 4.1. Scene graph - extractive PDF cue:** In a nutshell, we consider the output 𝐹of the encoder as a bag of local features, apply feature whitening, quantize them according to a codebook ...
- **p. 4 / 4.1. Scene graph - extractive PDF cue:** While any off-the-shelf image retriever can in theory do, we propose to leverage MASt3R's encoder Enc(·).
- **p. 5 / 4.2. Local reconstruction - extractive PDF cue:** Since the encoder features {𝐹𝑛}𝑛=1..𝑁have already been extracted and cached during scene graph construction (section 4.1), we only need to run the ViT decoder Dec(), ...
- **p. 5 / 4.2. Local reconstruction - extractive PDF cue:** (1) From it, we then recover the canonical depthmap ˜𝑍𝑛= ˜𝑋𝑛 :,:,3 and the focal length using Weiszfeld algorithm [64]: 𝑓∗= arg min 𝑓 ∑︁ ...
- **p. 4 / 4. Proposed Method - extractive PDF cue:** Global optimization proceeds with gradient descent of a matching loss in 3D space, followed by refinement in terms of 2D reprojection error.
- **p. 4 / 4. Proposed Method - extractive PDF cue:** Third, we coarsely align every local pointmap in the same world coordinate system using gradient descent with a matching loss in 3D space.
- **p. 5 / 4.3. Coarse alignment - extractive PDF cue:** We minimize this objective using Adam [24] for a fixed number 𝜈1 of iterations.
- **p. 5 / 4.4. Refinement - extractive PDF cue:** To further refine cameras and scene geometry, we thus perform a second round of global optimization akin to bundle adjustment [59] with gradient descent for ...

## Design Rationale

- **p. 4 / 4. Proposed Method - extractive PDF cue:** We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig.
- **p. 2 / 1. Introduction - extractive PDF cue:** To achieve linear complexity in the number of images, we show as second contribution how the encoder from MASt3R can be exploited for large-scale image ...
- **p. 2 / 1. Introduction - extractive PDF cue:** First, we propose MASt3R-SfM, a full-fledged SfM pipeline able to process unconstrained image collections.

## Source Evidence Cues

- **p. 4 / 4.1. Scene graph - extractive PDF cue:** In a nutshell, we consider the output 𝐹of the encoder as a bag of local features, apply feature whitening, quantize them according to a codebook ...
- **p. 4 / 4.1. Scene graph - extractive PDF cue:** While any off-the-shelf image retriever can in theory do, we propose to leverage MASt3R's encoder Enc(·).
- **p. 5 / 4.2. Local reconstruction - extractive PDF cue:** Since the encoder features {𝐹𝑛}𝑛=1..𝑁have already been extracted and cached during scene graph construction (section 4.1), we only need to run the ViT decoder Dec(), ...
- **p. 5 / 4.2. Local reconstruction - extractive PDF cue:** (1) From it, we then recover the canonical depthmap ˜𝑍𝑛= ˜𝑋𝑛 :,:,3 and the focal length using Weiszfeld algorithm [64]: 𝑓∗= arg min 𝑓 ∑︁ ...
- **Detected method headings:** 4. Proposed Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In a nutshell, we consider the output 𝐹of the encoder as a bag of local features, apply feature whitening, quantize them according ... | p. 4 (4.1. Scene graph), p. 4 (4.1. Scene graph) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | While any off-the-shelf image retriever can in theory do, we propose to leverage MASt3R's encoder Enc(·). | p. 4 (4.1. Scene graph), p. 5 (4.2. Local reconstruction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Since the encoder features {𝐹𝑛}𝑛=1..𝑁have already been extracted and cached during scene graph construction (section 4.1), we only need to run the ... | p. 5 (4.2. Local reconstruction), p. 5 (4.2. Local reconstruction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4. Proposed Method - extractive PDF cue:** Global optimization proceeds with gradient descent of a matching loss in 3D space, followed by refinement in terms of 2D reprojection error.
- **p. 4 / 4. Proposed Method - extractive PDF cue:** Third, we coarsely align every local pointmap in the same world coordinate system using gradient descent with a matching loss in 3D space.
- **p. 5 / 4.3. Coarse alignment - extractive PDF cue:** We minimize this objective using Adam [24] for a fixed number 𝜈1 of iterations.
- **p. 5 / 4.4. Refinement - extractive PDF cue:** To further refine cameras and scene geometry, we thus perform a second round of global optimization akin to bundle adjustment [59] with gradient descent for ...
- **p. 6 / 4.4. Refinement - extractive PDF cue:** MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion the 2D reprojection error of 3D points in all cameras: 𝑍∗, 𝐾∗, 𝑃∗, 𝜎∗= arg min 𝑍,𝐾,𝑃,𝜎 L2, ...
- **p. 6 / 4.4. Refinement - extractive PDF cue:** This way, correspondences that do not overlap exactly are still both tied to the same anchor point with a high probability.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4.3. Coarse alignment), p. 5 (4.2. Local reconstruction), p. 6 (4.4. Refinement).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | builds, recently, introduced, MASt3R, model, given, input, images, performs, joint, local, reconstruction, pixelwise, matching | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | builds, recently, introduced, MASt3R, model, given, input, images, performs, joint | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, novel, large-scale, reconstruction, consisting, four, steps, outlined, achieve, linear | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Global, optimization, proceeds, gradient, descent, matching, loss, space, followed, refinement | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Preliminaries - extractive PDF cue:** The proposed method builds on the recently introduced MASt3R model which, given two input images 𝐼𝑛, 𝐼𝑚∈ ℝ𝐻×𝑊×3, performs joint local 3D reconstruction and pixelwise ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In this work, we propose MASt3R-SfM, a fullyintegrated SfM pipeline that can handle completely unconstrained input image collections, i.e. ranging from a single view to ...
- **p. 3 / 3. Preliminaries - extractive PDF cue:** These outputs intrinsically contain rich geometric information from the scene, to the extent that camera intrinsics and (metric) depthmaps can straightforwardly be recovered from the ...
- **p. 4 / 4.1. Scene graph - extractive PDF cue:** To that aim, we adopt the ASMK (Aggregated Selective Match Kernels) image retrieval method [56] considering the token features output by the encoder as local ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Unfortunately, this type of approach only works in certain configurations, namely for input images exhibiting high overlap and low illumination variations.
- **p. 1 / 1. Introduction - extractive PDF cue:** This approach has been the standard for several decades, yet it remains brittle and fails when the input images do not sufficiently overlap, or when ...
- **p. 4 / 4.1. Scene graph - extractive PDF cue:** The output from the retrieval step is a similarity matrix 𝑆∈[0, 1]𝑁×𝑁.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We first select a fixed number 𝑁𝑎of key images (or keyframes) using farthest point sampling (FPS) [16] based on 𝑆. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The output from the retrieval step is a similarity matrix 𝑆∈[0, 1]𝑁×𝑁. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In this work, we simplify and improve this procedure by taking advantage of pixel correspondences, thereby reducing the overall number of parameters ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We form new splits by regularly subsampling the original images for 25, 50, 100 and 200 frames. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4.1. Scene graph - extractive PDF cue:** Note that this method is training-free, only requiring to compute the whitening matrix and the codebook once from a representative set of features.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** nutshell, consider, output, encoder, local, features, apply, feature, whitening, quantize, them, according, codebook, previously, obtained, k-means, clustering, then, aggregate, binarize.
- **Relevant PDF headings:** 4. Proposed Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, ... | p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup) |
| Semantic / temporal fusion | Overall, we find that combining short-range (𝑘-NN) and long-range (keyframes) connections is important for Method Aachen-Day-Night↑ InLoc↑ Day Night DUC1 DUC2 Kapture ... | p. 8 (8.4 GB), p. 6 (5. Experimental Results) |
| Robot query / planning handoff | MASt3R-SfM provides nearly constant performance for all ranges, significantly outperforming COLMAP, Ace-Zero, FlowMap and VGGSfM in all settings. | p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art) |

## Failure and Ablation Link

- **p. 6 / 5. Experimental Results - extractive PDF cue:** We finally present several ablations.
- **p. 6 / 5.1. Experimental setup - extractive PDF cue:** 0.014) for 𝜈1 = 300 iterations and 𝜆1 = 1.5 (resp. 𝜈2 = 300 and 𝜆2 = 0.5) for the coarse (resp. refinement) optimization, each ...
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** The fact that COLMAP and VGGSfM also perform relatively poorly indicates a high sensitivity to not having highly overlapping images, meaning that in the end ...
- **p. 8 / 8.4 GB - extractive PDF cue:** 14.3 min Table 4: Ablation of scene graph construction on Tanks&Temples (200 view subset).
- **p. 9 / 8.4 GB - extractive PDF cue:** We also try to perform the optimization without optimizing depth (i.e. using frozen canonical depthmaps, which proves useful for purely rotational cases, denoted as ‘Fine ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Top: Relative rotation (RRA) and translation (RTA) accuracies on the CO3Dv2 dataset when varying the number of input views with random subsampling (the ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative reconstruction results for MASt3R-SfM on ETH-3D (top) and Tanks&Temples (bottom). These are the raw outputs of the proposed SfM pipeline, without further ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.1. Scene graph), p. 4 (4.1. Scene graph), p. 5 (4.2. Local reconstruction), p. 5 (4.2. Local reconstruction), objective p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4.3. Coarse alignment), p. 5 (4.4. Refinement), p. 6 (4.4. Refinement), p. 6 (4.4. Refinement), temporal p. 4 (4.1. Scene graph), p. 4 (4.1. Scene graph), p. 5 (4.3. Coarse alignment), p. 6 (5.1. Experimental setup), p. 6 (5.1. Experimental setup), p. 7 (5.2. Comparison with the state of the art).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
