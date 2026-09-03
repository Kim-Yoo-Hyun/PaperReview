# Object-centric 3D Motion Field for Robot Learning from Human Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=kp9B9iQDIt.
> PDF retrieval source: https://arxiv.org/pdf/2506.04227. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, learning from human videos, 3D motion field, cross-embodiment
- Official paper: https://openreview.net/forum?id=kp9B9iQDIt
- Full-text retrieval: https://arxiv.org/pdf/2506.04227
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.를 문제로 두고, We present a simple and novel architecture that can learn to see and predict object-centric 3D motion field in the real world for control.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning robot control policies from human videos is a promising direction for scaling up robot learning.
- **p. 1 / Abstract - extractive body cue:** However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge.
- **p. 1 / Abstract - extractive body cue:** Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework ...
- **p. 1 / Abstract - extractive body cue:** We introduce two novel components in its implementation.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.
- **p. 1 / 1 Introduction - extractive body cue:** Data is the primary bottleneck in robot learning - collecting large-scale high quality robotic data in real world at scale for training control policies is ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** We present a simple and novel architecture that can learn to see and predict object-centric 3D motion field in the real world for control.
- **p. 3 / 1 Introduction - extractive body cue:** We propose to use object-centric 3D motion field for robot learning from videos and present a novel learning framework for extracting this representation for control.
- **p. 1 / Abstract - extractive body cue:** We introduce two novel components in its implementation.
- **p. 1 / Abstract - extractive body cue:** Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse ...
- **p. 4 / 2 Preliminaries - extractive body cue:** We first discuss a very simple pipeline for this purpose as suggested by latest works [55] and its fundamental limitations, and then we introduce our ...
- **p. 7 / 2 Preliminaries - extractive body cue:** Model and Training Then, we train a policy network π to predict these labeled 3D motion field with the segmented RGBD image as input.
- **p. 2 / 1 Introduction - extractive body cue:** Although this line of work achieved some preliminary success, video frames turn out to be an overly noisy, redundant action representation, which not only unnecessarily ...
- **p. 5 / 2 Preliminaries - extractive body cue:** Data Augmentation During training, we use diverse data augmentations to simulate the noise effect of each sensor observations, and the underlying idea is relevant to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Dual Head UNet UNet Blocks concat Depth 3D PixelFlow Intrinsics Map Depth Motion Camera Intrinsics Phase I Phase II Input concat Output 3D Motion Field (Noisy Sensors) [H,W,1] [H,W,3] [H,W,1+1] [H,W,3+1] [H,W,4] | multi-view observation, language/task label과 action trajectory | p. 5 (2 Preliminaries), p. 2 (1 Introduction) |
| State/latent | Dual, Head, UNet, Blocks, concat, Depth, PixelFlow, Intrinsics, Map, Motion, Camera, Phase | shared representation, embodiment/task identity와 data distribution | p. 5 (2 Preliminaries), p. 2 (1 Introduction), p. 3 (2 Preliminaries) |
| Output/action | Learning to See 3D Motion Field 3D Motion Field Predictor 3D Motion Field 3D Motion Field Estimator Train 3D Motion Field (Extraction) (Simulation Pretraining) Camera Origin Noisy Fine 3D Pixel Flow Depth ... | dataset sample 또는 learned policy action | p. 2 (1 Introduction), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Objective/outcome | Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 1 (Abstract), p. 3 (2 Preliminaries), p. 6 (2 Preliminaries) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** We present a simple and novel architecture that can learn to see and predict object-centric 3D motion field in the real world for control.
- **p. 3 / 1 Introduction - extractive body cue:** We propose to use object-centric 3D motion field for robot learning from videos and present a novel learning framework for extracting this representation for control.
- **p. 1 / Abstract - extractive body cue:** We introduce two novel components in its implementation.
- **p. 1 / Abstract - extractive body cue:** Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse ...
- **p. 4 / 2 Preliminaries - extractive body cue:** We first discuss a very simple pipeline for this purpose as suggested by latest works [55] and its fundamental limitations, and then we introduce our ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8: (Left) SE3 motion estimation performance in real world. Our method achieves lower error compared to baseline. (Middle) Intrinsics Map Ablation Studies. Both inverse ...
- **p. 9 / 5 Experiments - extractive body cue:** Main Results We show the success rate of different methods in Figure 8 Right.
- **p. 9 / 5 Experiments - extractive body cue:** We find that our method significantly outperformed the other evaluated methods.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 9 (5 Experiments) |
| Embodiment/environment | We use an XArm7 robot arm with a parallel-jaw gripper for the test dataset collection and robot experiments. | hardware/simulator version and reset protocol | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Dataset/benchmark | In this task, the robot is required to pick, rotate, and insert an item into a slot (hole). | role, split, size and leakage | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments) |
| Metric | Focal Len Ours (Full) 0.0 0.5 1.0 1.5 2.0 2.5 ×10 6 3D Motion Field Error ( ) Motion (train) Motion (sim-test) Depth (train) Depth (sim-test) Task 1 Task 2 Task 3 ... | definition, denominator, direction and uncertainty | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Baseline/ablation | Our method achieves lower error compared to baseline. | fair input/data/compute/action matching | p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Experiments - extractive body cue:** Other recent methods fail on our setup due to their limitations (Table 2). to 256 × 256.
- **p. 9 / 5 Experiments - extractive body cue:** Our method is free from many limitations of existing works.
- **p. 9 / 5 Experiments - extractive body cue:** While these approaches offer certain advantages, each has notable limitations, as previously discussed.
- **p. 8 / 5 Experiments - extractive body cue:** Adversarial Robustness We test robustness further through adversarial attack in real world experiments by injecting Gaussian noise of different intensities into the depth observation (which ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Data Noise Simulation. We highlight several key randomization strategies. Type Setup Depth White Noise Gaussian, σ = Log-Uniform [0.01, 1]× 0.2mm Depth Correlated ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 14: Motion Field Comparison (1.5/2.5cm-wide pen motion): Our method produces a smoother motion field than the direct method, which exhibits noticeable noise. 18

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.를 문제로 두고, We present a simple and novel architecture that can learn to see and predict object-centric 3D motion field in the real world for control.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (2 Preliminaries), p. 7 (2 Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
