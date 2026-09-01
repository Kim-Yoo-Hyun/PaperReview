# Method - SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08870.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method)): Below, we first briefly review the radiance field representation and then introduce our joint optimization scheme.

## Method Body Digest

- **p. 7 / 3 Method - extractive PDF cue:** Below, we first briefly review the radiance field representation and then introduce our joint optimization scheme.
- **p. 5 / 3 Method - extractive PDF cue:** Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- **p. 5 / 3 Method - extractive PDF cue:** Given the training images, we first apply a widely used Structure-from-Motion (SfM) algorithm, i.e., COLMAP [40], to construct an initial scene graph of the images, ...
- **p. 8 / 3 Method - extractive PDF cue:** It consists of several training epochs.
- **p. 8 / 3 Method - extractive PDF cue:** 3) loss terms, we propose an intersection-over-union (IoU) loss.
- **p. 6 / 3 Method - extractive PDF cue:** Given a set of images, we first apply a Structure-from-Motion (SfM) algorithm to construct an initial scene graph (left), within which, each node represents a ...
- **p. 6 / 3 Method - extractive PDF cue:** In the first step, we apply pre-trained SuperPoint [12] to extract keypoints from images, and exhaustively match every pair of images with keypoints using pre-trained ...
- **p. 8 / 3 Method - extractive PDF cue:** The IoU loss aims to maximize the intersection-over-union between the two MoGs that correspond to the matched keypoints.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.
- **p. 3 / 1 Introduction - extractive PDF cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our method works effectively and can produce high-quality 3D reconstructions. produce a sparse scene representation.

## Source Evidence Cues

- **p. 7 / 3 Method - extractive PDF cue:** Below, we first briefly review the radiance field representation and then introduce our joint optimization scheme.
- **p. 5 / 3 Method - extractive PDF cue:** Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- **p. 5 / 3 Method - extractive PDF cue:** Given the training images, we first apply a widely used Structure-from-Motion (SfM) algorithm, i.e., COLMAP [40], to construct an initial scene graph of the images, ...
- **p. 8 / 3 Method - extractive PDF cue:** It consists of several training epochs.
- **p. 8 / 3 Method - extractive PDF cue:** 3) loss terms, we propose an intersection-over-union (IoU) loss.
- **p. 6 / 3 Method - extractive PDF cue:** Given a set of images, we first apply a Structure-from-Motion (SfM) algorithm to construct an initial scene graph (left), within which, each node represents a ...
- **p. 6 / 3 Method - extractive PDF cue:** In the first step, we apply pre-trained SuperPoint [12] to extract keypoints from images, and exhaustively match every pair of images with keypoints using pre-trained ...
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Below, we first briefly review the radiance field representation and then introduce our joint optimization scheme. | p. 7 (3 Method), p. 5 (3 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec. | p. 5 (3 Method), p. 5 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Given the training images, we first apply a widely used Structure-from-Motion (SfM) algorithm, i.e., COLMAP [40], to construct an initial scene graph ... | p. 5 (3 Method), p. 8 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3 Method - extractive PDF cue:** The IoU loss aims to maximize the intersection-over-union between the two MoGs that correspond to the matched keypoints.
- **p. 8 / 3 Method - extractive PDF cue:** During the training process, the goal is to minimize the difference between synthesized pixels and those in real images as an L1 photometric loss: \lab ...
- **p. 9 / 3 Method - extractive PDF cue:** Given a pair of matched keypoints from source and reference images, in order to maximize the IoU between the two rays, both the camera pose ...
- **p. 9 / 3 Method - extractive PDF cue:** 4: Illustration of the two-view intersection-over-union (IoU) loss in 2D that can be easily extended into 3D.
- **p. 7 / 3 Method - extractive PDF cue:** Explicitly, the confidence scores will be updated, the camera poses will be optimized, and the graph structure will remain fixed.
- **p. 5 / 3 Method - extractive PDF cue:** The training process is essentially a scene-specific joint optimization.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 7 (3 Method), p. 9 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, scene, input, RGB, images, output, surface, reconstruction, network, takes, location, viewing, direction, generates | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Specifically, scene, input, RGB, images, output, surface, reconstruction, network, takes | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | novel, framework, jointly, optimizes, neural, radiance, field, scene, graph, alleviate | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | IoU, loss, aims, maximize, intersection-over-union, between, MoGs, correspond, matched, keypoints | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive PDF cue:** Specifically, for each scene, the input is a set of RGB images I = {I1, I2, ..., In}, and the output is a 3D surface ...
- **p. 7 / 3 Method - extractive PDF cue:** The network takes a 3D location and viewing direction as input and generates the corresponding density and RGB color (i.e., radiance) as output.
- **p. 5 / 3 Method - extractive PDF cue:** Each node vi ∈V corresponds to an input image Ii ∈I, and an edge between two nodes indicates that the connected images share a co-visible ...
- **p. 9 / 3 Method - extractive PDF cue:** When σ < 1 (pixel), we stop the Gaussian filtering and use the original images as input (finest scale).
- **p. 9 / 3 Method - extractive PDF cue:** More specifically, the coarse-to-fine strategy is implemented by applying a Gaussian filter to the original input images at the beginning of each epoch.
- **p. 3 / 1 Introduction - extractive PDF cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The proposed can reconstruct 3D surface under significant camera pose noise with an adaptive inlier-outlier confidence estimation, an IoU loss that efficiently leverages the confidence ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The scene graph is initially constructed with the employed SfM module [40], which contains two major steps: a) correspondence search, and b) ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | In the first step, we apply pre-trained SuperPoint [12] to extract keypoints from images, and exhaustively match every pair of images with ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Method - extractive PDF cue:** Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- **p. 5 / 3 Method - extractive PDF cue:** Given the training images, we first apply a widely used Structure-from-Motion (SfM) algorithm, i.e., COLMAP [40], to construct an initial scene graph of the images, ...
- **p. 8 / 3 Method - extractive PDF cue:** It consists of several training epochs.
- **p. 6 / 3 Method - extractive PDF cue:** In the first step, we apply pre-trained SuperPoint [12] to extract keypoints from images, and exhaustively match every pair of images with keypoints using pre-trained ...
- **p. 11 / 4 Experiments - extractive PDF cue:** For each of them, we adopt the official implementation to optimize camera poses, and then apply the optimized poses to train NeuS.
- **p. 8 / 3 Method - extractive PDF cue:** It consists of several training epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Below, first, briefly, review, radiance, field, representation, then, introduce, joint, optimization, scheme, present, training, updating, scene, graph, Sec, Given, images.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec. | p. 10 (4 Experiments), p. 13 (7.71 3.77†) |
| Global / local decision | We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec. | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Motion execution / recovery | While BARF* achieves the best results in scene 37, it is more likely to impose negative impact on camera poses, thereby has ... | p. 13 (7.71 3.77†), p. 11 (4 Experiments) |

## Failure and Ablation Link

- **p. 10 / 4 Experiments - extractive PDF cue:** Furthermore, we perform a series of ablation studies and analyses to verify the effectiveness of each proposed component (Sec.
- **p. 13 / 7.71 3.77† - extractive PDF cue:** We select three representative scenes from the proposed dataset and conduct ablation studies to evaluate the effectiveness of each component.
- **p. 13 / 7.71 3.77† - extractive PDF cue:** To evaluate the effectiveness of the joint optimization, we directly train our method using the original scene graph obtained from SfM without further refinement.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative results of our ablation studies. We individually remove the use of sparsification by thresholding (w/o τ), confidence estimation (w/o CS), Intersection- over-Union ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3: Visualization of matches that are falsely established as correspondences from non-overlapping regions. The results are obtained using COLMAP [40] with Super- Point [12] ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Following hloc [37], we replace the keypoints and the matching module with SuperPoint [12] and SuperGlue [38], respectively.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 6 (3 Method), objective p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 7 (3 Method), p. 5 (3 Method), temporal p. 6 (3 Method), p. 6 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
