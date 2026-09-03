# Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38947.
> PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38947. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / AAAI
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Robotics, action representation, camera space, cross-view generalization, real-world manipulation
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/38947
- Full-text retrieval: https://ojs.aaai.org/index.php/AAAI/article/view/38947
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view inputs are available.를 문제로 두고, To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate system, named ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces.
- **p. 1 / Abstract - extractive body cue:** Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies.
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space.
- **p. 1 / Abstract - extractive body cue:** Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets ...
- **p. 1 / Abstract - extractive body cue:** This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although this paradigm has achieved impressive performance across a variety of benchmarks, it remains fundamentally constrained by the intrinsic limitations of the robotics domain-namely, the ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, our method exhibits markedly improved adaptability to previously unseen camera view.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce the Observation-Centric VLA (OC-VLA) framework.
- **p. 3 / III. METHOD - extractive body cue:** Different from previous end-effector action prediction, the predicted action in our method is in the camera space.
- **p. 3 / III. METHOD - extractive body cue:** Based on the baseline architecture, we implement a variant specifically designed for discrete action prediction or continuous action prediction.
- **p. 3 / III. METHOD - extractive body cue:** While these representations are widely used as supervision signals for Vision-Language-Action (VLA) models, they are tightly coupled with specific robot embodiment configurations, rather than being ...
- **p. 3 / III. METHOD - extractive body cue:** Consequently, it is difficult for the model to achieve a reasonable projection from image observation to corresponding actions, and thus the model generalization is limited, ...
- **p. 4 / III. METHOD - extractive body cue:** For instance, Droid [9] features 1417 distinct camera viewpoints, requiring the model to internally infer the correct transformation T for each view to predict actions ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the third-person camera coordinate, unifying the observation and prediction targets across ... | image/video, language instruction, proprioception과 history | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| State/latent | OC-VLA, transforms, effector, pose, whether, defined, discrete, continuous, action, space, robot, base | language-grounded task state와 action-policy context | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD) |
| Output/action | This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view inputs are available. | continuous action, pose 또는 action chunk | p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Objective/outcome | Meanwhile, given an end-effector pose Pworld of the robot, we can get, Pcam = TPworld (5) Equations 4 and 5 present that both the end effector pose and action in world space ... | instruction following, task success, generalization과 latency | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, our method exhibits markedly improved adaptability to previously unseen camera view.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce the Observation-Centric VLA (OC-VLA) framework.
- **p. 3 / III. METHOD - extractive body cue:** Different from previous end-effector action prediction, the predicted action in our method is in the camera space.
- **p. 3 / III. METHOD - extractive body cue:** Based on the baseline architecture, we implement a variant specifically designed for discrete action prediction or continuous action prediction.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, when the prediction target is switched from robot-base coordinate actions to camera-base coordinate actions, the model achieves a further 10% improvement in the metric ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The results demonstrate that, regardless of the type of action space used, employing robot actions defined in the third-person camera coordinate frame as prediction targets ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This improvement is particularly pronounced in models utilizing a discrete action space, where we observe an increase in success rate of about 14%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Dataset/benchmark | Real Robot Evaluation 1) Setup: We evaluate OC-VLA on a real-world Franka Robot setup, which comprises a 7-DoF tabletop Franka Emika Panda robot arm equipped with a Robotiq 2F-85 gripper as shown ... | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | For each task, we conduct 10 trials and measure performance by computing the task success rate. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Baseline/ablation | These models serve as baselines in our evaluation. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This indicates that our method can partially compensate ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA aligns ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** This diversity makes it an ideal choice for evaluating the generalizability and robustness of our observationcentric action prediction framework.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In addition to language and image tokens, we concatenate the current timestep and the noise-perturbed action as inputs to the causal transformer.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this setting, the camera viewpoint remains fixed and identical throughout both the finetuning and evaluation phases. • Slight Camera Perturbations To further validate the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To assess the model's robustness to changes in camera perspective, we conduct zero-shot evaluations using models fine-tuned with demonstrations from Camera 1.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view inputs are available.를 문제로 두고, To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate system, named ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view inputs are available. (p. 1, I. INTRODUCTION).
- **Actual contribution:** To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate ... (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Lastly, we present a comprehensive evaluation of the performance of our proposed method on both simulated benchmarks and real-world robotic platforms. (p. 4, IV. EXPERIMENTS).
- **Explicit failure boundary:** Failures are highlighted with red circles. the same data. (p. 7, IV. EXPERIMENTS).
