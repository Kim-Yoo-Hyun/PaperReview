# Method - Gaussian Grouping: Segment and Edit Anything in 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4195_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04195.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 4 (3 Method), p. 5 (3 Method)): 1 as input, we first add a linear layer f to recover its feature dimension back to K and then take softmax(f(Eid)) for identity classification, where K is the total ...

## Method Body Digest

- **p. 7 / 3 Method - extractive PDF cue:** 1 as input, we first add a linear layer f to recover its feature dimension back to K and then take softmax(f(Eid)) for identity classification, ...
- **p. 6 / 3 Method - extractive PDF cue:** (b) Then, to obtain the consistent mask IDs across training views, we take a universal temporal propagation model [7] to associate the mask labels and ...
- **p. 7 / 3 Method - extractive PDF cue:** 3D Regularization Loss leverages the 3D spatial consistency, which enforces the Identity Encodings of the top k-nearest 3D Gaussians to be close in their feature ...
- **p. 9 / 3 Method - extractive PDF cue:** Because of our fine-grained mask modeling, it also supports multiple concurrent local editings without interfering with each other or re-training the whole global 3D scene ...
- **p. 4 / 3 Method - extractive PDF cue:** Our work aims to build an expressive 3D scene representation, which not only models appearance and geometry, but also captures every instance and stuff
- **p. 5 / 3 Method - extractive PDF cue:** Our approach, called Gaussian Grouping, is capable of: 1) modeling each 3D part of the scene with appearance, geometry together with their mask identities; 2) ...
- **p. 6 / 3 Method - extractive PDF cue:** Projection at Camera View 𝑁 Gradient Gradient 3D Regularization Loss 𝐿#$ (a) Multi-view Captures with Anything Masks by SAM (b) Consistent IDs for Anything Coherent ...
- **p. 7 / 3 Method - extractive PDF cue:** 3D Regularization Loss: To further boost the grouping accuracy of Gaussians, besides the standard cross-entropy loss for indirect 2D supervision, we also introduce an unsupervised ...

## Design Rationale

- **p. 4 / 1 Introduction - extractive PDF cue:** To our knowledge, we propose the first Gaussian-based method to tackle open-world 3D scene understanding, where we show the advantages compared to existing NeRF-based approaches ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We propose Gaussian Grouping, which represents the whole 3D scene with a set of grouped 3D Gaussians.
- **p. 2 / 1 Introduction - extractive PDF cue:** By inputting multi-view captures and the corresponding automatically generated masks by SAM, our method learns a discrete and grouped 3D representation for reconstructing and segmenting ...

## Source Evidence Cues

- **p. 7 / 3 Method - extractive PDF cue:** 1 as input, we first add a linear layer f to recover its feature dimension back to K and then take softmax(f(Eid)) for identity classification, ...
- **p. 6 / 3 Method - extractive PDF cue:** (b) Then, to obtain the consistent mask IDs across training views, we take a universal temporal propagation model [7] to associate the mask labels and ...
- **p. 7 / 3 Method - extractive PDF cue:** 3D Regularization Loss leverages the 3D spatial consistency, which enforces the Identity Encodings of the top k-nearest 3D Gaussians to be close in their feature ...
- **p. 9 / 3 Method - extractive PDF cue:** Because of our fine-grained mask modeling, it also supports multiple concurrent local editings without interfering with each other or re-training the whole global 3D scene ...
- **p. 4 / 3 Method - extractive PDF cue:** Our work aims to build an expressive 3D scene representation, which not only models appearance and geometry, but also captures every instance and stuff
- **p. 5 / 3 Method - extractive PDF cue:** Our approach, called Gaussian Grouping, is capable of: 1) modeling each 3D part of the scene with appearance, geometry together with their mask identities; 2) ...
- **p. 6 / 3 Method - extractive PDF cue:** Projection at Camera View 𝑁 Gradient Gradient 3D Regularization Loss 𝐿#$ (a) Multi-view Captures with Anything Masks by SAM (b) Consistent IDs for Anything Coherent ...
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 1 as input, we first add a linear layer f to recover its feature dimension back to K and then take softmax(f(Eid)) ... | p. 7 (3 Method), p. 6 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (b) Then, to obtain the consistent mask IDs across training views, we take a universal temporal propagation model [7] to associate the ... | p. 6 (3 Method), p. 7 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3D Regularization Loss leverages the 3D spatial consistency, which enforces the Identity Encodings of the top k-nearest 3D Gaussians to be close ... | p. 7 (3 Method), p. 9 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 Method - extractive PDF cue:** Projection at Camera View 𝑁 Gradient Gradient 3D Regularization Loss 𝐿#$ (a) Multi-view Captures with Anything Masks by SAM (b) Consistent IDs for Anything Coherent ...
- **p. 7 / 3 Method - extractive PDF cue:** 3D Regularization Loss: To further boost the grouping accuracy of Gaussians, besides the standard cross-entropy loss for indirect 2D supervision, we also introduce an unsupervised ...
- **p. 6 / 3 Method - extractive PDF cue:** Our encoding is supervised by the 2D Identity Loss, leveraging the coherent segmentation views, and a 3D Regularization loss.
- **p. 7 / 3 Method - extractive PDF cue:** We adopt a standard cross-entropy loss L2d for K categories classification.
- **p. 8 / 3 Method - extractive PDF cue:** We formalize the KL divergence loss with m sampling points as, \ l a b e l {e q:reg_3d} \ ma t h cal
- **p. 8 / 3 Method - extractive PDF cue:** 3, we denote F as softmax operation combined after linear layer f (shared in computing the 2D Identity loss).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | then, detail, input, data, pre-processing, steps, further, describe, Gaussian, Grouping, Section, Image, Mask, prepare | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | then, detail, input, data, pre-processing, steps, further, describe, Gaussian, Grouping | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | knowledge, first, Gaussian-based, tackle, open-world, scene, understanding, where, advantages, compared | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Projection, Camera, View, Gradient, Regularization, Loss, Multi-view, Captures, Anything, Masks | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive PDF cue:** We then detail the input data pre-processing steps and further describe the proposed Gaussian Grouping in Section 3.2.
- **p. 5 / 3 Method - extractive PDF cue:** (a) 2D Image and Mask Input To prepare the input for Gaussian Grouping, in Figure 2(a), we first deploy SAM to automatically generate masks for ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Existing methods [8, 41] rely on manually-labeled datasets, which are both costly and limited in scope, or require accurately scanned point clouds [36, 46] as ...
- **p. 6 / 3 Method - extractive PDF cue:** We use color the denote object IDs across frames for input views.
- **p. 6 / 3 Method - extractive PDF cue:** (c) With the prepared training input, we jointly learn all properties of the 3D Gaussians, including their group Identity Encoding, by differentiable rendering.
- **p. 7 / 3 Method - extractive PDF cue:** 1 as input, we first add a linear layer f to recover its feature dimension back to K and then take softmax(f(Eid)) for identity classification, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Given a set of posed RGB images, our goal is to learn an effective 3D representation that jointly reconstructs and segments anything in the 3D ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We then detail the input data pre-processing steps and further describe the proposed Gaussian Grouping in Section 3.2. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This technique has established its effectiveness in the reconstruction tasks, exhibiting high inference speeds and remarkable quality of reconstruction within timeframes on ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | GT Image Rendered Image Rendered Mask Cost-based Linear Assignment (2K Iterations, training time: > 1 hour) Our Zero-shot Mask Association (2K Iterations, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive PDF cue:** (b) Then, to obtain the consistent mask IDs across training views, we take a universal temporal propagation model [7] to associate the mask labels and ...
- **p. 9 / 3 Method - extractive PDF cue:** Because of our fine-grained mask modeling, it also supports multiple concurrent local editings without interfering with each other or re-training the whole global 3D scene ...
- **p. 5 / 3 Method - extractive PDF cue:** Our approach, called Gaussian Grouping, is capable of: 1) modeling each 3D part of the scene with appearance, geometry together with their mask identities; 2) ...
- **p. 10 / 4 Experiments - extractive PDF cue:** GT Image Rendered Image Rendered Mask Cost-based Linear Assignment (2K Iterations, training time: > 1 hour) Our Zero-shot Mask Association (2K Iterations, training time: 1 ...
- **p. 9 / 4 Experiments - extractive PDF cue:** All datasets are trained for 30K iterations on one A100 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** input, first, linear, layer, recover, feature, dimension, back, then, take, softmax, Eid, identity, classification, where, total, number, masks, scene, obtain.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Also, our approach is better at distinguishing objects with similar colors, such as the "Green apple" prompt case. compare fine-grained mask localization ... | p. 12 (4 Experiments), p. 9 (4 Experiments) |
| Semantic / temporal fusion | Model Scene Seg Scene Edit PSNR↑SSIM↑LPIPS↓FPS Baseline: Gaussian Splatting [14] - - 28.69 0.870 0.182 ∼200 Gaussian Grouping ✓ ✓ 28.43 0.863 ... | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Robot query / planning handoff | 6 and Table 2, K = 5 achieves both the best balance between the scene reconstruction and 3D object removal accuracy. | p. 11 (4 Experiments), p. 12 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive PDF cue:** 4.2 Ablation Experiments Ablation on Mask Cross-view Association To study the effect of cross-view masks association [7] for input preparation, we replace the associated masks ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Visual Ablation on the Grouping Losses In Figure 7, we study the effect of our grouping loss components, where solely using 2D Identity Loss will ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 6: Visual ablation of K in the 3D Regularization Loss on object removal editing of MipNeRF360. We remove Gaussians classified as lego with various ...
- **p. 12 / 4 Experiments - extractive PDF cue:** In Figure 9, we compare the removal effect of our Gaussian Grouping with the Distilled Feature Fields (DFFs) [18].
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Our Gaussian Grouping jointly reconstructs (column a) and segments (column b) anything in full open-world 3D scenes, with fine-grained instance and stuff level ...
- **p. 10 / 4 Experiments - extractive PDF cue:** 4: Ablation on the Identity Consistency across views, where we treat multi-view images as a video and associate the mask labels to generate coherent segmentation ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Model Scene Seg Scene Edit PSNR↑SSIM↑LPIPS↓FPS Baseline: Gaussian Splatting [14] - - 28.69 0.870 0.182 ∼200 Gaussian Grouping ✓ ✓ 28.43 0.863 0.189 ∼170 Table ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 4 (3 Method), p. 5 (3 Method), objective p. 6 (3 Method), p. 7 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), temporal p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 10 (4 Experiments), p. 10 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
