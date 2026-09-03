# Method - DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2108.10869; PDF retrieval source: https://arxiv.org/pdf/2108.10869. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (3 Approach), p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach), p. 6 (3 Approach)): At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition on the reduced camera block.

## Method Body Digest

- **p. 7 / 3 Approach - extractive body cue:** At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition on ...
- **p. 4 / 3 Approach - extractive body cue:** Like RAFT[49], we use two separate networks: a feature network and a context network.
- **p. 4 / 3 Approach - extractive body cue:** The network consists of 6 residual blocks and 3 downsampling layers, producing dense feature maps at 1/8 the input image resolution.
- **p. 5 / 3 Approach - extractive body cue:** We denote the corrected correspondence as p∗ ij = rij + pij We then pool the hidden state over all features which share the same ...
- **p. 5 / 3 Approach - extractive body cue:** For each edge (i, j) ∈E we use pij to perform lookup from the correlation volume Cij to retrieve correlation features.
- **p. 6 / 3 Approach - extractive body cue:** The training set is composed of a collection of videos.
- **p. 6 / 3 Approach - extractive body cue:** Constructing training video Each training example consists of a 7-frame video sequence.
- **p. 5 / 3 Approach - extractive body cue:** We define the cost function over the entire frame graph E(G′, d′) = X (i,j)∈E

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** In this work we introduce DROID-SLAM, a new SLAM system based on deep learning.
- **p. 2 / 1 Introduction - extractive body cue:** Specifically, it consists of recurrent iterative updates, building upon RAFT [49] for optical flow but introducing two key innovations.
- **p. 4 / 3 Approach - extractive body cue:** The network consists of 6 residual blocks and 3 downsampling layers, producing dense feature maps at 1/8 the input image resolution.

## Source Evidence Cues

- **p. 7 / 3 Approach - extractive body cue:** At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition on ...
- **p. 4 / 3 Approach - extractive body cue:** Like RAFT[49], we use two separate networks: a feature network and a context network.
- **p. 4 / 3 Approach - extractive body cue:** The network consists of 6 residual blocks and 3 downsampling layers, producing dense feature maps at 1/8 the input image resolution.
- **p. 5 / 3 Approach - extractive body cue:** We denote the corrected correspondence as p∗ ij = rij + pij We then pool the hidden state over all features which share the same ...
- **p. 5 / 3 Approach - extractive body cue:** For each edge (i, j) ∈E we use pij to perform lookup from the correlation volume Cij to retrieve correlation features.
- **p. 6 / 3 Approach - extractive body cue:** The training set is composed of a collection of videos.
- **p. 6 / 3 Approach - extractive body cue:** Constructing training video Each training example consists of a 7-frame video sequence.
- **Detected method headings:** 3 Approach (p. 3); C Camera Model and Jacobians (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse ... | p. 7 (3 Approach), p. 4 (3 Approach) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Like RAFT[49], we use two separate networks: a feature network and a context network. | p. 4 (3 Approach), p. 4 (3 Approach) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The network consists of 6 residual blocks and 3 downsampling layers, producing dense feature maps at 1/8 the input image resolution. | p. 4 (3 Approach), p. 5 (3 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Approach - extractive body cue:** We define the cost function over the entire frame graph E(G′, d′) = X (i,j)∈E
- **p. 7 / 3 Approach - extractive body cue:** In the case of RGB-D, we still treat depth as a variable, since sensor depth can be noisy and have missing observations, and simply add ...
- **p. 3 / 3 Approach - extractive body cue:** We take a video as input with two objectives: estimate the trajectory of the camera and build a 3D map of the environment.
- **p. 6 / 3 Approach - extractive body cue:** The flow loss is applied to pairs of adjacent frames.
- **p. 6 / 3 Approach - extractive body cue:** The loss is taken to be the average l2 distance between the two flow fields.
- **p. 3 / 3 Approach - extractive body cue:** After each pose or depth update, we can recompute 3
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3 Approach), p. 6 (3 Approach), p. 6 (3 Approach), p. 7 (3 Approach), p. 3 (3 Approach), p. 4 (3 Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Feature, Extraction, input, images, processed, network, extract, global, context, averaging, hidden, state, across, spatial | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Feature, Extraction, input, images, processed, network, extract, global, context, averaging | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | introduce, DROID-SLAM, SLAM, system, deep, learning, Specifically, consists, recurrent, iterative | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | define, cost, function, over, entire, frame, graph, case, RGB-D, still | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Approach - extractive body cue:** Feature Extraction Each of the input images are processed by a feature extraction network.
- **p. 5 / 3 Approach - extractive body cue:** We extract global context by averaging the hidden state across the spatial dimensions of the image and use this feature vector as additional input to ...
- **p. 5 / 3 Approach - extractive body cue:** We map the hidden state through two additional convoluation layers to produce two outputs: (1) a revision flow field rij ∈RH×W ×2 and (2) associated ...
- **p. 3 / 3 Approach - extractive body cue:** For each image t, we maintain two state variables: camera pose Gt ∈SE(3) and inverse depth dt ∈RH×W + .
- **p. 3 / 3 Approach - extractive body cue:** We take a video as input with two objectives: estimate the trajectory of the camera and build a 3D map of the environment.
- **p. 4 / 3 Approach - extractive body cue:** Each application of the operator updates the hidden state, and additionally produces a pose update, ∆ξ(k), and depth update, ∆d(k).
- **p. 7 / 3 Approach - extractive body cue:** In the case of RGB-D, we still treat depth as a variable, since sensor depth can be noisy and have missing observations, and simply add ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We train our network for 250k steps with a batch size of 4, resolution 384 × 512, and 7 frame clips, and ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The score is computed using normalized relative pose error for all possible sequences of length {5, 10, 15, ..., 40} meters, see ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Timing and Memory Our system can run in real-time with 2 3090 GPUs. | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We train our network for 250k steps with a batch size of 4, resolution 384 × 512, and 7 frame clips, and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3 Approach - extractive body cue:** At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition on ...
- **p. 6 / 3 Approach - extractive body cue:** The training set is composed of a collection of videos.
- **p. 6 / 3 Approach - extractive body cue:** Constructing training video Each training example consists of a 7-frame video sequence.
- **p. 7 / 4 Experiments - extractive body cue:** We train our network for 250k steps with a batch size of 4, resolution 384 × 512, and 7 frame clips, and unroll 15 update ...
- **p. 7 / 3 Approach - extractive body cue:** At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition on ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** inference, time, custom, CUDA, kernel, takes, advantage, block-sparse, structure, problem, then, perform, sparse, Cholesky, decomposition, reduced, camera, block, Like, RAFT.
- **Relevant PDF headings:** 3 Approach (p. 3); C Camera Model and Jacobians (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | TUM-RGBD [44] The RGBD dataset consists of indoor scenes captured with handheld camera. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Global / local decision | We retrain DeepV2D [48] on TartanAir as a baseline. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Motion execution / recovery | On most sequences, we outperform existing methods by an order-of-magnitude and achieve 8x lower average error than TartanVO [54] and 20x lower ... | p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive body cue:** Without any finetuning, our method ranks 1st on both the train and test splits.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Stereo SLAM on the EuRoC datasets, ATE[m]. We provide stereo results on the EuRoC dataset[2] in Tab. 5 using our network trained on ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 6: (Left) we show the performance of the system with different inputs (monocular vs. stereo) and whether global optimization is performed in addition to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of the update operator. The operator acts on edges in the frame graph, predicting flow revisions which are mapped to depth and ...
- **p. 8 / 4 Experiments - extractive body cue:** 1 demonstrates both the robustness of our method (no catastrophic failures) and accuracy (very low drift).
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the camera ...
- **p. 8 / 4 Experiments - extractive body cue:** In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ORB-SLAM3 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (3 Approach), p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach), p. 6 (3 Approach), objective p. 5 (3 Approach), p. 7 (3 Approach), p. 3 (3 Approach), p. 6 (3 Approach), p. 6 (3 Approach), p. 3 (3 Approach), temporal p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (3 Approach), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We take a video as input with two objectives: estimate the trajectory of the camera and build a 3D map of the environment. (p. 3, 3 Approach).
- **Objective/update evidence:** In the case of RGB-D, we still treat depth as a variable, since sensor depth can be noisy and have missing observations, and simply add a term to the optimization ... (p. 7, 3 Approach).
- **Temporal/runtime evidence:** On EuRoC, we average 20fps (camera hz) by downsampling to 320 × 512 resolution and skipping every other frame. (p. 9, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
