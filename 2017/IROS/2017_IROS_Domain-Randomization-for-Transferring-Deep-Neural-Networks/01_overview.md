# Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1703.06907.
> PDF retrieval source: https://arxiv.org/pdf/1703.06907. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Robotics, sim-to-real, domain randomization, perception
- Official paper: https://arxiv.org/abs/1703.06907
- Full-text retrieval: https://arxiv.org/pdf/1703.06907
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Though in principle domain randomization could be applied to any component of the reality gap, we focus on the challenge of transferring from low-fidelity simulated camera images.를 문제로 두고, Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Bridging the ‘reality gap' that separates simulated robotics from experiments on hardware could accelerate robotic research through improved data availability.
- **p. 1 / Abstract - extractive body cue:** This paper explores domain randomization, a simple technique for training models on simulated images that transfer to real images by randomizing rendering in the simulator.
- **p. 1 / Abstract - extractive body cue:** With enough variability in the simulator, the real world may appear to the model as just another variation.
- **p. 1 / Abstract - extractive body cue:** We focus on the task of object localization, which is a stepping stone to general robotic manipulation skills.
- **p. 1 / Abstract - extractive body cue:** We find that it is possible to train a real-world object detector that is accurate to 1.5 cm and robust to distractors and partial occlusions ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Though in principle domain randomization could be applied to any component of the reality gap, we focus on the challenge of transferring from low-fidelity simulated ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This paper explores domain randomization, a simple but promising method for addressing the reality gap.

## Core Idea

- **p. 4 / III. METHOD - extractive body cue:** Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in ...
- **p. 3 / III. METHOD - extractive body cue:** Our approach is to train a deep neural network in simulation using domain randomization.
- **p. 3 / III. METHOD - extractive body cue:** The remainder of this section describes the specific domain randomization and neural network training methodology we use.
- **p. 3 / III. METHOD - extractive body cue:** We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on the table • ...
- **p. 4 / III. METHOD - extractive body cue:** In particular, we use a modified version the VGG-16 architecture [39] shown in Figure 2.
- **p. 4 / III. METHOD - extractive body cue:** For the majority of our experiments, we use weights obtained by pretraining on ImageNet to initialize the convolutional layers, which we hypothesized would be essential ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input is an image from an external webcam downsized to (224 × 224) and the output of the network predicts the (x, y, z) coordinates of object(s) of interest. | state 또는 observation, action, reward와 transition history | p. 4 (III. METHOD), p. 2 (I. INTRODUCTION) |
| State/latent | input, image, external, webcam, downsized, output, network, predicts, coordinates, object, interest, localization | policy/value state와 action-selection variable | p. 4 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Output/action | Object localization from pixels is a well-studied problem in robotics, and state-ofthe-art methods employ complex, hand-engineered image processing pipelines (e.g., [6], [5], [44]). | action policy와 induced trajectory | p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | We train the detector through stochastic gradient descent on the L2 loss between the object positions estimated by the network and the true object positions using the Adam optimizer [17]. | expected return, task success, stability와 sample efficiency | p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 4 / III. METHOD - extractive body cue:** Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in ...
- **p. 3 / III. METHOD - extractive body cue:** Our approach is to train a deep neural network in simulation using domain randomization.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** However, using a pre-trained model can significantly improve performance when less training data is used.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** 1Categories for which the best final performance was achieved for detector trained from scratch.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Therefore no validation on real data can be done during training. few as 5, 000 training samples, but performance improves up to around 50, 000 ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We report the performance of the best network.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Embodiment/environment | The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) Assess which ... | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | We did not control for lighting conditions or the rest of the scene around the table (e.g., all images contain part of the robot and tape and wires on the floor). | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) Assess which ... | definition, denominator, direction and uncertainty | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | Randomizing the position of the camera also consistently provides a slight accuracy boost, but reasonably high accuracy is achievable without it. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 3 / II. RELATED WORK - extractive body cue:** However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.
- **p. 3 / II. RELATED WORK - extractive body cue:** Our approach also does not rely on precise camera information or calibration, instead randomizing the position, orientation, and field of view of the camera in ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Adding noise during pretraining appears to have a negligible effect.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our object detectors are able to localize objects to within 1.5 cm (on average) in the real world and perform well in the presence of ...

## Why Read It

RL, IL, offline learning, and robot data의 rl 문제를 이해하기 위해 읽는다. 본문은 Though in principle domain randomization could be applied to any component of the reality gap, we focus on the challenge of transferring from low-fidelity simulated camera images.를 문제로 두고, Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Though in principle domain randomization could be applied to any component of the reality gap, we focus on the challenge of transferring from low-fidelity simulated camera images. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Our approach is to train a deep neural network in simulation using domain randomization. (p. 3, III. METHOD).
- **Evaluation boundary:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) ... (p. 4, IV. EXPERIMENTS).
- **Explicit failure boundary:** Ablation study To evaluate the importance of different factors of our training methodology, we assessed the sensitivity of the algorithm to the following: • Number of training images • Number ... (p. 5, IV. EXPERIMENTS).
