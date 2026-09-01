# Method - Object-centric 3D Motion Field for Robot Learning from Human Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kp9B9iQDIt; PDF retrieval source: https://arxiv.org/pdf/2506.04227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (2 Preliminaries), p. 2 (1 Introduction), p. 5 (2 Preliminaries), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction)): Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image as input.

## Method Body Digest

- **p. 7 / 2 Preliminaries - extractive PDF cue:** Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image as input.
- **p. 2 / 1 Introduction - extractive PDF cue:** Although this line of work achieved some preliminary success, video frames turn out to be an overly noisy, redundant action representation, which not only unnecessarily ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Data Augmentation During training, we use diverse data augmentations to simulate the noise effect of each sensor observations, and the underlying idea is relevant to ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework ...
- **p. 1 / Abstract - extractive PDF cue:** Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information.
- **p. 2 / 1 Introduction - extractive PDF cue:** Some recent works, such as UniPi [9] and UniSim [51], directly apply video prediction for control, which essentially view future video frames as action representations ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Since all the input and output information are geometrical (no RGB textures), we propose to use a simulator to generate training data due to minimal ...
- **p. 3 / 2 Preliminaries - extractive PDF cue:** Assuming a pinhole camera with focal length f, the observed pixel movement on x-axis is ∆xp = fX Z+∆Z -fX Z ≈-fX Z2 ∆Z, and ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** We present a simple and novel architecture that can learn to see and predict object-centric 3D motion field in the real world for control.
- **p. 3 / 1 Introduction - extractive PDF cue:** We propose to use object-centric 3D motion field for robot learning from videos and present a novel learning framework for extracting this representation for control.
- **p. 1 / Abstract - extractive PDF cue:** We introduce two novel components in its implementation.

## Source Evidence Cues

- **p. 7 / 2 Preliminaries - extractive PDF cue:** Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image as input.
- **p. 2 / 1 Introduction - extractive PDF cue:** Although this line of work achieved some preliminary success, video frames turn out to be an overly noisy, redundant action representation, which not only unnecessarily ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Data Augmentation During training, we use diverse data augmentations to simulate the noise effect of each sensor observations, and the underlying idea is relevant to ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework ...
- **p. 1 / Abstract - extractive PDF cue:** Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information.
- **p. 2 / 1 Introduction - extractive PDF cue:** Some recent works, such as UniPi [9] and UniSim [51], directly apply video prediction for control, which essentially view future video frames as action representations ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Since all the input and output information are geometrical (no RGB textures), we propose to use a simulator to generate training data due to minimal ...
- **Detected method headings:** A Further Details on Model Architecture and Training (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image ... | p. 7 (2 Preliminaries), p. 2 (1 Introduction) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Although this line of work achieved some preliminary success, video frames turn out to be an overly noisy, redundant action representation, which ... | p. 2 (1 Introduction), p. 5 (2 Preliminaries) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Data Augmentation During training, we use diverse data augmentations to simulate the noise effect of each sensor observations, and the underlying idea ... | p. 5 (2 Preliminaries), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive PDF cue:** Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information.
- **p. 3 / 2 Preliminaries - extractive PDF cue:** Assuming a pinhole camera with focal length f, the observed pixel movement on x-axis is ∆xp = fX Z+∆Z -fX Z ≈-fX Z2 ∆Z, and ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** (2) In the loss function above, Dsim is the generated synthetic dataset.
- **p. 6 / 2 Preliminaries - extractive PDF cue:** Training We apply a weighted Huber loss (∥· ∥) as a stable supervision to train this model: L = Ex,F,M∼Dsim∥M ⊙(fdepth(x) -Fdepth)∥+ α∥M ⊙(fmotion(x) -Fmotion)∥.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** We minimize ∥RP T 0 + t -P T 1 ∥2, which has a closed form solution (Kabsch method [16]).
- **p. 7 / 2 Preliminaries - extractive PDF cue:** We apply the following general regression objective for training (for both diffusion and Gaussian policy): Lπ = Eo,F,M∼Dhuman∥M ⊙(πdepth(o, ˜F, t) -Fdepth)∥+ α∥M ⊙(πmotion(o, ˜F, ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 3 (2 Preliminaries), p. 6 (2 Preliminaries), p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 7 (2 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Dual, Head, UNet, Blocks, concat, Depth, PixelFlow, Intrinsics, Map, Motion, Camera, Phase, Input, Output | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Dual, Head, UNet, Blocks, concat, Depth, PixelFlow, Intrinsics, Map, Motion | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | present, simple, novel, architecture, learn, predict, object-centric, motion, field, real | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Existing, action, representations, video, frames, pixelflow, pointcloud, flow, have, inherent | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 2 Preliminaries - extractive PDF cue:** Dual Head UNet UNet Blocks concat Depth 3D PixelFlow Intrinsics Map Depth Motion Camera Intrinsics Phase I Phase II Input concat Output 3D Motion Field ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Learning to See 3D Motion Field 3D Motion Field Predictor 3D Motion Field 3D Motion Field Estimator Train 3D Motion Field (Extraction) (Simulation Pretraining) Camera ...
- **p. 3 / 2 Preliminaries - extractive PDF cue:** The state-of-the-art robots have built-in functionality to realize arbitrary object movements: i.e., by calling well-established foundational grasping policy and task-space SE(3) movement commands, and therefore ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Since all the input and output information are geometrical (no RGB textures), we propose to use a simulator to generate training data due to minimal ...
- **p. 6 / 2 Preliminaries - extractive PDF cue:** Dataset: Human Videos We only require human object interaction video dataset Dhuman to train our control policy.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image as input.
- **p. 7 / 2 Preliminaries - extractive PDF cue:** (3) In this objective above, o is the segmented RGBD image observation, F is the groundtruth object 3D motion field (desired action over the object) ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Note that we use the gripper frame as the base for representing these transformations. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | To get a high-quality raw depth, we use the native temporal and spatial filters provided by the camera SDK. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | (Right) Real world Task Success Rate (3 seeds). | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 2 Preliminaries - extractive PDF cue:** Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image as input.
- **p. 2 / 1 Introduction - extractive PDF cue:** Although this line of work achieved some preliminary success, video frames turn out to be an overly noisy, redundant action representation, which not only unnecessarily ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Data Augmentation During training, we use diverse data augmentations to simulate the noise effect of each sensor observations, and the underlying idea is relevant to ...
- **p. 5 / 2 Preliminaries - extractive PDF cue:** Since all the input and output information are geometrical (no RGB textures), we propose to use a simulator to generate training data due to minimal ...
- **p. 7 / 2 Preliminaries - extractive PDF cue:** Deployment In the inference time, we need to convert the predicted 3D motion field F to the robot action.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Model, Training, Then, train, policy, network, predict, labeled, motion, field, segmented, RGBD, image, input, Although, line, achieved, some, preliminary, success.
- **Relevant PDF headings:** A Further Details on Model Architecture and Training (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | We use an XArm7 robot arm with a parallel-jaw gripper for the test dataset collection and robot experiments. | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Coverage / augmentation | Our method achieves lower error compared to baseline. | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Downstream learning interface | Figure 8: (Left) SE3 motion estimation performance in real world. Our method achieves lower error compared to baseline. (Middle) Intrinsics Map Ablation ... | p. 8 (Figure/Table caption), p. 9 (5 Experiments) |

## Failure and Ablation Link

- **p. 8 / 5 Experiments - extractive PDF cue:** (Middle) Intrinsics Map Ablation Studies.
- **p. 9 / 5 Experiments - extractive PDF cue:** 5.0% Full 35.0% Ablation Studies We also study the design choices of our policy architecture and training.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: We propose a novel framework for robot learning from human demonstration videos without relying on any robot-collected data. Our approach learns to control ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7: A rollout of fine-grained insertion. Our method can achieve high precision, even if we are observing the motion from 40cm away without a ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Policy Learning Ablation for Fine-grained Tasks. Setting Success w/o Diffusion (Diff.) 0.0% w/o Diff. Masking. 0.0%
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of proposed learning framework. We first pretrain a 3D motion field estimator in simulation (Phase I) and use it to estimate the ...
- **p. 8 / 5 Experiments - extractive PDF cue:** Other recent methods fail on our setup due to their limitations (Table 2). to 256 × 256.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (2 Preliminaries), p. 2 (1 Introduction), p. 5 (2 Preliminaries), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), objective p. 1 (Abstract), p. 3 (2 Preliminaries), p. 6 (2 Preliminaries), p. 6 (2 Preliminaries), p. 7 (2 Preliminaries), p. 7 (2 Preliminaries), temporal p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 5 (2 Preliminaries), p. 7 (2 Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
