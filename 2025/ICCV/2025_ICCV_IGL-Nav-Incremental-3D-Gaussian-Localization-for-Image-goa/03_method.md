# Method - IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Incremental Scene Representation), p. 5 (3.3.2. Fine Target Localization), p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization), p. 6 (3.4. Navigation), p. 4 (3.3. Coarse-to-fine Localization)): We first concatenate the normalized RGB and depth images, and then extract dense monocular scene embedding E′ t with a UNet-based encoder E.

## Method Body Digest

- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** We first concatenate the normalized RGB and depth images, and then extract dense monocular scene embedding E′ t with a UNet-based encoder E.
- **p. 5 / 3.3.2. Fine Target Localization - extractive body cue:** Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the number of matching ...
- **p. 3 / 3.1. Problem Statement - extractive body cue:** A is the set of actions, which consists of move forward, turn left, turn right and stop.
- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** We use focal loss [17] to supervise the activation map after 3D convolution.
- **p. 6 / 3.4. Navigation - extractive body cue:** We then project the activation map obtained in our coarse target localization module to BEV to get Sa.
- **p. 4 / 3.3. Coarse-to-fine Localization - extractive body cue:** Initial Pose Target Pose Gaussian Encoder Current RGB-D Current Embedding 𝑬௧ ᇱ Target Image Gaussian Encoder Previous Embedding 𝑬௧ିଵ Update Scene Embedding 𝑬௧ RGB-D Stream ...
- **p. 2 / 3. Approach - extractive body cue:** Next, we explain several core modules of IGL-Nav, including in6809
- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** Additionally, we apply cross-entropy loss to supervise the outputs nearby target pose in the activation map.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose to leverage 3D Gaussian Splatting (3DGS) [10] as the scene representation for imagegoal navigation.
- **p. 3 / 3.1. Problem Statement - extractive body cue:** A is the set of actions, which consists of move forward, turn left, turn right and stop.

## Source Evidence Cues

- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** We first concatenate the normalized RGB and depth images, and then extract dense monocular scene embedding E′ t with a UNet-based encoder E.
- **p. 5 / 3.3.2. Fine Target Localization - extractive body cue:** Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the number of matching ...
- **p. 3 / 3.1. Problem Statement - extractive body cue:** A is the set of actions, which consists of move forward, turn left, turn right and stop.
- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** We use focal loss [17] to supervise the activation map after 3D convolution.
- **p. 6 / 3.4. Navigation - extractive body cue:** We then project the activation map obtained in our coarse target localization module to BEV to get Sa.
- **p. 4 / 3.3. Coarse-to-fine Localization - extractive body cue:** Initial Pose Target Pose Gaussian Encoder Current RGB-D Current Embedding 𝑬௧ ᇱ Target Image Gaussian Encoder Previous Embedding 𝑬௧ିଵ Update Scene Embedding 𝑬௧ RGB-D Stream ...
- **p. 2 / 3. Approach - extractive body cue:** Next, we explain several core modules of IGL-Nav, including in6809
- **Detected method headings:** 3. Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We first concatenate the normalized RGB and depth images, and then extract dense monocular scene embedding E′ t with a UNet-based encoder ... | p. 3 (3.2. Incremental Scene Representation), p. 5 (3.3.2. Fine Target Localization) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the ... | p. 5 (3.3.2. Fine Target Localization), p. 3 (3.1. Problem Statement) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | A is the set of actions, which consists of move forward, turn left, turn right and stop. | p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** Additionally, we apply cross-entropy loss to supervise the outputs nearby target pose in the activation map.
- **p. 5 / 3.3.2. Fine Target Localization - extractive body cue:** Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the number of matching ...
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** The training loss is a linear combination of L-2 and LPIPS [37] losses.
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** In each episode, K frames are randomly selected to predict 3DGS parameters, and images from other viewpoints are rendered for loss computation.
- **p. 4 / 3.3.1. Coarse Target Localization - extractive body cue:** By translating these embeddings to the discretized voxel grids and computing the extent of alignment between the translated embedding and Et, the coarse target pose ...
- **p. 4 / 3.3. Coarse-to-fine Localization - extractive body cue:** (c) Fine target localization via differentiable 3DGS rendering and matching-constrained optimization. 𝐿 𝑅 𝜃 𝜙 𝑋 𝑍 𝐴 𝐵 𝑂 𝑌 𝑂ᇱ: (𝑥, 𝑦, 𝑧) ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3.2. Incremental Scene Representation), p. 3 (3.2. Incremental Scene Representation), p. 5 (3.3.1. Coarse Target Localization), p. 5 (3.3.1. Coarse Target Localization), p. 4 (3.3. Coarse-to-fine Localization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Incremental, Scene, Representation, Embedding, Coarse-to-fine, Navigation, Reaching, Target, Local, Policy, Action, Renderingbased, Stopper, Exploration | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Incremental, Scene, Representation, Embedding, Coarse-to-fine, Navigation, Reaching, Target, Local, Policy | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | IGL-Nav, Incremental, Gaussian, Localization, framework, progressively, constructs, DGS, through, feed-forward | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Additionally, apply, cross-entropy, loss, supervise, outputs, nearby, target, pose, activation | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** Incremental Scene Representation Scene Embedding 𝑬௧ Coarse-to-fine Navigation Reaching Target Local Policy Action Renderingbased Stopper Exploration Current RGB-D Input Target Image Activation Map Target Embedding ...
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** Our incremental reconstruction model is essentially a mapping fθ from observations to 3DGS parameters, including position µk, opacity αk, covariance Σk and spherical harmonics ck: ...
- **p. 3 / 3.1. Problem Statement - extractive body cue:** It receives posed RGB-D video stream {It, Dt, Tt}T t=1 and is required to execute an action a ∈A at each time it receiving a ...
- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** We use two MLP f1 / f2 with input channel Cin and output channel C′ to project scene embedding and convolutional kernel to a learnable ...
- **p. 6 / 3.4. Navigation - extractive body cue:** Based on the posed RGB-D inputs, we maintain an online occupancy map to indicate explored, unexplored and occupied area in BEV, where the frontiers of ...
- **p. 1 / 1. Introduction - extractive body cue:** IGL-Nav effectively guides the agent to reach free-view image goal via incremental 3D gaussian localization. agent to precisely understand spatial information, as well as to ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments on various datasets in Habitat simulator show our IGL-Nav significantly outperforms previous state-of-the-art imagegoal navigation methods.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At time step t, the agent receives new RGB-D observations It ∈RH×W ×3 and Dt ∈RH×W ×1. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At each time step, we select the nearest frontier to the agent and generate binary scores Sf on the BEV map, where ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.3. Coarse-to-fine Localization - extractive body cue:** Initial Pose Target Pose Gaussian Encoder Current RGB-D Current Embedding 𝑬௧ ᇱ Target Image Gaussian Encoder Previous Embedding 𝑬௧ିଵ Update Scene Embedding 𝑬௧ RGB-D Stream ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Since some methods [7, 29, 30, 33] only release test code, we perform zeroshot transfer to apply them to the new setting without retraining.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, concatenate, normalized, RGB, depth, images, then, extract, dense, monocular, scene, embedding, UNet-based, encoder, formulate, optimization, loss, Q-1, Xi/2, where.
- **Relevant PDF headings:** 3. Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We further deploy IGL-Nav on real-world robotic platform to test its generalization ability. | p. 8 (4.4. Real-world Deployment), p. 6 (4.1. Experimental Setup) |
| Global / local decision | IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D ... | p. 6 (4.2. Comparison with State-of-the-art), p. 7 (4.2. Comparison with State-of-the-art) |
| Motion execution / recovery | It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the ... | p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art) |

## Failure and Ablation Link

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Since some methods [7, 29, 30, 33] only release test code, we perform zeroshot transfer to apply them to the new setting without retraining.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** All ablation studies are conducted on the free-view image-goal setting.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** We further conduct in-depth module-by-module analysis on our IGL-Nav framework with sufficient visualization results and ablation studies, which is divided into three parts according to ...
- **p. 8 / 4.4. Real-world Deployment - extractive body cue:** The model is directly taken from the free-view image-goal setting (supervised) without any finetuning on real-world data.
- **p. 8 / 5. Conclusion - extractive body cue:** A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** As shown in Table 3, with predicted depth and camera intrinsics, the performance of IGLNav is still robust.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.2. Incremental Scene Representation), p. 5 (3.3.2. Fine Target Localization), p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization), p. 6 (3.4. Navigation), p. 4 (3.3. Coarse-to-fine Localization), objective p. 5 (3.3.1. Coarse Target Localization), p. 5 (3.3.2. Fine Target Localization), p. 3 (3.2. Incremental Scene Representation), p. 3 (3.2. Incremental Scene Representation), p. 4 (3.3.1. Coarse Target Localization), p. 4 (3.3. Coarse-to-fine Localization), temporal p. 3 (3.2. Incremental Scene Representation), p. 6 (3.4. Navigation), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Analysis of IGL-Nav).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Our incremental reconstruction model is essentially a mapping fθ from observations to 3DGS parameters, including position µk, opacity αk, covariance Σk and spherical harmonics ck: fθ : (It, Dt) 7→{(µk, ... (p. 3, 3.2. Incremental Scene Representation).
- **Objective/update evidence:** Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the number of matching pairs. (p. 5, 3.3.2. Fine Target Localization).
- **Temporal/runtime evidence:** Each of the six subsets contains 500 randomly sampled episodes. (p. 6, 4.1. Experimental Setup).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
