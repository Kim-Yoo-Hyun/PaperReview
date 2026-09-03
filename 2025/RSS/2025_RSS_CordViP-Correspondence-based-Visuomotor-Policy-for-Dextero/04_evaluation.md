# Evaluation - CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p110.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 8 (Figure/Table caption), p. 15 (B. Implementation Details), p. 15 (B. Implementation Details)): Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which demonstrate robustness to different viewpoints ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘We conduct comprehensive real-world experiments to answer the following questions:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ To what extent can our framework promote the learning of the visuomotor policy for dexterous manipulation across diverse real-world scenarios (Section IV-B)?
- **p. 6 / A. Experiment Setup - extractive body cue:** consists of a 6-Dof URS robot arm and a 16-Dof Leap Hand
- **p. 6 / A. Experiment Setup - extractive body cue:** ‘camera is mounted on the side of the robot to capture visual
- **p. 15 / B. Implementation Details - extractive body cue:** Hyperparameters Vale Robot poiat cloud size 10243, ‘Object point cloud size 10243,
- **p. 14 / B. Implementation Details - extractive body cue:** The state features of the robotic arm and the dexterous hand are each passed through a linear layer, mapped to 16 dimensions.
- **p. 15 / B. Implementation Details - extractive body cue:** All data collection i managed through ROS and data recording begins once both the camera feed and robot teleoperation inputs are received.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5); A. Experiment Setup (p. 6); B. Implementation Details (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, ... | p. 1 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Experimental results of efficiency. We train ACT, DP, DP3, and CordViP on the PickPlace and FlipCup tasks wi an increasing number of ... | p. 8 (Figure/Table caption) |
| B. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | The visual results are shown in the figure 10. | p. 15 (B. Implementation Details) |
| B. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | This step is necessary for DDIM [50] and DDPM (22), as they clip the predicted results to the range of (-1, 1] for training ... | p. 15 (B. Implementation Details) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘We conduct comprehensive real-world experiments to answer the following questions:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ To what extent can our framework promote the learning of the visuomotor policy for dexterous manipulation across diverse real-world scenarios (Section IV-B)?
- **p. 6 / A. Experiment Setup - extractive body cue:** consists of a 6-Dof URS robot arm and a 16-Dof Leap Hand
- **p. 6 / A. Experiment Setup - extractive body cue:** ‘camera is mounted on the side of the robot to capture visual
- **p. 15 / B. Implementation Details - extractive body cue:** Hyperparameters Vale Robot poiat cloud size 10243, ‘Object point cloud size 10243,
- **p. 14 / B. Implementation Details - extractive body cue:** The state features of the robotic arm and the dexterous hand are each passed through a linear layer, mapped to 16 dimensions.
- **p. 15 / B. Implementation Details - extractive body cue:** All data collection i managed through ROS and data recording begins once both the camera feed and robot teleoperation inputs are received.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview Framework (a) We first employ TripoSR to generate the initial object point cloud and FoundationPose
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Point Clouds Comparison, We present point clouds of two methods under three different viewpoints. Notably, for better visualization, we have applied color information ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Real robot system. Our system consists of a Leap Hand and a URS Arm, with a fixed Realsense L515 camera ‘employed to capture ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Visualization of six dexterous manipulation tasks, with the right side showing the end state.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Randomization of Object Positions. The red rectangles mark the range of positions of manipulated objects. For PickPlace and FlipCup, both the toy chicken ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Experimental results of efficiency. We train ACT, DP, DP3, and CordViP on the PickPlace and FlipCup tasks wi an increasing number of demonstrations.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Failure case. (a) Case / is a failure case from the

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ‘We conduct comprehensive real-world experiments to answer the following questions: | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | ‘+ To what extent can our framework promote the learning of the visuomotor policy for dexterous manipulation across diverse real-world scenarios (Section IV-B)? | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 6 (A. Experiment Setup) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Contact map size rose ‘Loss weight 0 1 horizon 2 nob steps 4 action steps 6 | definition/direction/unit from same section | p. 15 (B. Implementation Details) |
| Fig. 2: Overview Framework (a) We first employ TripoSR to generate the initial object point cloud and FoundationPose | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| For the FlipCup task, we focus on accurately estimating the 6D pose of the cup. | definition/direction/unit from same section | p. 15 (B. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The Diffusion Policy baseline utilizes ResNetI8 as the visual encoder and employs CNN-based backbones. | comparison identity and matched condition | p. 15 (B. Implementation Details) |
| In contrast, for other baselines, we synthesize the point cloud from RGBD data, and both the pose and the point clouds are transformed into ... | comparison identity and matched condition | p. 15 (B. Implementation Details) |
| Fig. 3: Point Clouds Comparison, We present point clouds of two methods under three different viewpoints. Notably, for better visualization, we have applied color ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Network Architecture, For point cloud encoding, we first use PointNetl41] to process point cloud data without RGB information, outputting a set of point feature ... | comparison identity and matched condition | p. 14 (B. Implementation Details) |
| Fig. 11: Comparison of Motion Patterns. DP3 Uses Axis Wise Actions. | comparison identity and matched condition | p. 16 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Network Architecture, For point cloud encoding, we first use PointNetl41] to process point cloud data without RGB information, outputting a set of point feature ... | component/input/data sensitivity | p. 14 (B. Implementation Details) |
| ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Point clouds are used to replace the original image inputs. | component/input/data sensitivity | p. 15 (B. Implementation Details) |
| ‘The BCRNNSD is trained for 3000 epochs with horizon=10, n_obs_steps=1, n_action_steps=l, where the observations are replaced from images to point clouds. | component/input/data sensitivity | p. 15 (B. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information, | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 8 (Figure/Table caption), p. 15 (B. Implementation Details), p. 15 (B. Implementation Details) |
| Primary metric/result | ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / A. Experiment Setup - extractive body cue:** The episode length of each task will be limited to a maximum of 500 steps and ‘each task is evaluated with 20 trials by default.
- **p. 14 / B. Implementation Details - extractive body cue:** The state features of the robotic arm and the dexterous hand are each passed through a linear layer, mapped to 16 dimensions.
- **p. 15 / B. Implementation Details - extractive body cue:** We utilize the RealSense L515 ‘camera to capture RGB-D images with a resolution of 480 X 640.
- **p. 15 / B. Implementation Details - extractive body cue:** The point cloud is synthesized from RGBD data. ‘The point cloud is then ‘cropped and processed using farthest point sampling (FPS) to generate 1024 points.
- **p. 15 / B. Implementation Details - extractive body cue:** We train the Diffusion Policy for 600 epochs with horizon=12, n_obs_steps=4, and n_action_steps=8.
- **p. 15 / B. Implementation Details - extractive body cue:** The 3D Diffusion Policy is trained for $000 epochs with horizon=12, n_obs_steps=4, n_action_steps=8, Ituses DP3 Encoder as the point cloud encoder.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work. | p. 10 (V. CONCLUSIONS AND LimiTATIONS) |
| body limitation/failure cue | Fig. 8: Failure case. (a) Case / is a failure case from the | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | We utilize FoundationPose (60] to perform robust 6D pose estimation for various objects across tasks. | p. 15 (B. Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The 3D Diffusion Policy is trained for $000 epochs with horizon=12, n_obs_steps=4, n_action_steps=8, Ituses DP3 Encoder as the point cloud encoder. | p. 15 (B. Implementation Details) |
| The episode length of each task will be limited to a maximum of 500 steps and ‘each task is evaluated with 20 trials by ... | p. 6 (A. Experiment Setup) |
| For BCRNN, we train the model for 1500 epochs with horizon=10, n_obs_steps=1, n_action_ste} | p. 15 (B. Implementation Details) |
| where £ represents the encoder of the observation, and ) is a hyperparameter that controls the relative strengths of the losses. | p. 5 (C. Comact and Coordination-Enhanced Feature Extraction) |
| Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the ... | p. 5 (C. Comact and Coordination-Enhanced Feature Extraction) |
| Furthermore, leveraging these observations, we compute contact maps between the robotic hhand and the manipulated objects, as well as capture col laborative interaction information ... | p. 3 (A. Problem Formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / V. CONCLUSIONS AND LimiTATIONS - extractive body cue:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Failure case. (a) Case / is a failure case from the
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...
- **p. 15 / B. Implementation Details - extractive body cue:** We utilize FoundationPose (60] to perform robust 6D pose estimation for various objects across tasks.

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup), p. 15 (B. Implementation Details), p. 14 (B. Implementation Details), metrics p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 15 (B. Implementation Details), p. 4 (Figure/Table caption), p. 15 (B. Implementation Details), baselines p. 15 (B. Implementation Details), p. 15 (B. Implementation Details), p. 4 (Figure/Table caption), p. 14 (B. Implementation Details), p. 16 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 8 (Figure/Table caption), p. 15 (B. Implementation Details), p. 15 (B. Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The visual results are shown in the figure 10. (p. 15, B. Implementation Details).
- **Metric evidence:** ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? (p. 5, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? (p. 5, IV. EXPERIMENTS).
- **Failure/negative evidence:** As shown in ‘Table VI, the image-based diffusion policy is highly sensitive to ‘camera viewpoints and completely fails across all three camera views. (p. 9, C. Efficiency).
