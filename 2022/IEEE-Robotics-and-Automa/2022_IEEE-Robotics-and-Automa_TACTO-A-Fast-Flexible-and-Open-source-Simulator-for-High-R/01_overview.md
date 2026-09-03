# TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/LRA.2022.3146945.
> PDF retrieval source: https://doi.org/10.1109/LRA.2022.3146945. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / IEEE Robotics and Automation Letters
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, tactile sensing, simulation, contact
- Official paper: https://doi.org/10.1109/LRA.2022.3146945
- Full-text retrieval: https://doi.org/10.1109/LRA.2022.3146945
- Code/Project: https://github.com/facebookresearch/tacto
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 simulation 문제를 이해하기 위해 읽는다. 본문은 One aspect that has proven so far to be difficult to simulate is tactile sensing, and in particular visionbased tactile sensors [2], [3], [4] which provide rich highresolution measurements.를 문제로 두고, This allows to perform orders of magnitude more experiments at a fraction of the effort, and in many cases of the time.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Simulators perform an important role in prototyping, debugging, and benchmarking new advances in robotics and learning for control.
- **p. 1 / Abstract - extractive body cue:** Although many physics engines exist, some aspects of the real world are harder than others to simulate.
- **p. 1 / Abstract - extractive body cue:** One of the aspects that have so far eluded accurate simulation is touch sensing.
- **p. 1 / Abstract - extractive body cue:** To address this gap, we present TACTO - a fast, flexible, and open-source simulator for vision-based tactile sensors.
- **p. 1 / Abstract - extractive body cue:** This simulator allows to render realistic high-resolution touch readings at hundreds of frames per second, and can be easily configured to simulate different vision-based tactile ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One aspect that has proven so far to be difficult to simulate is tactile sensing, and in particular visionbased tactile sensors [2], [3], [4] which ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** This allows to perform orders of magnitude more experiments at a fraction of the effort, and in many cases of the time.
- **p. 3 / 1. Phong's model for RGB rendering from Depth (simple - extractive body cue:** but less powerful): PyBullet built-in camera can provide a depth map of the contact area.
- **p. 3 / 1. Phong's model for RGB rendering from Depth (simple - extractive body cue:** To render the RGB image from the depth map, researchers from [13] implemented their own renderer based on Phong's reflection model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Hence, it is difficult to adapt to existing and future sensor designs that require advanced functionalities, like reflection, refraction, and shadows with fast speed. | simulated state, geometry, contact와 control input | p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 3 (1. Phong's model for RGB rendering from Depth (simple) |
| State/latent | Hence, difficult, adapt, existing, future, sensor, designs, require, advanced, functionalities, like, reflection | dynamics/contact state 또는 learned simulator representation | p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 1 (I. INTRODUCTION) |
| Output/action | To render the RGB image from the depth map, researchers from [13] implemented their own renderer based on Phong's reflection model. | simulation step, trajectory 또는 environment query | p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | physical plausibility, speed, reproducibility와 task utility | physical plausibility, speed, reproducibility와 task utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** This allows to perform orders of magnitude more experiments at a fraction of the effort, and in many cases of the time.
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that increasing ...
- **p. 5 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The experiments in simulation achieve similar results to the ones with real robots, which demonstrates the effectiveness and potentials of the simulated environment.
- **p. 7 / V. SIM2REAL EXPERIMENTS - extractive body cue:** Without any real data, Sim2Real with augmentation can achieve comparable results with Real2Real (64).
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** Since there are rich contacts with friction happening during the rolling, we aim to investigate how stable the TACTO and PyBullet are, and explore whether ...
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** To evaluate the performance of different dataset sizes, we used K-fold cross-validation and computed the median and 68% percentile of the classification accuracy.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 6: If readings from a real-world sensor are available, TACTO allows to fine-tune the simulator using the real-world data. This is achieved by calculating ...
- **p. 5 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The goal is to predict whether a grasped object will be successfully lifted, based on the touch

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS) |
| Embodiment/environment | The vertical dashed line shows the largest dataset collected on real robot [6]. | hardware/simulator version and reset protocol | p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS) |
| Dataset/benchmark | The experiments in simulation achieve similar results to the ones with real robots, which demonstrates the effectiveness and potentials of the simulated environment. | role, split, size and leakage | p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS) |
| Metric | The cost is defined as cumulative error distance in tactile space P t ∥¯xt∥, and we set eight different target locations and take the average cost for robustness. | definition, denominator, direction and uncertainty | p. 7 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS) |
| Baseline/ablation | Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that increasing the amount of data helps to improve ... | fair input/data/compute/action matching | p. 6 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** In the failure grasp, the object is only grasped by the corner and begins to slip after being lifted.
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** (Left) Examples of a successful grasp and a failure grasp.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 8: TACTO supports rendering shadows to obtain more realistic simula- tions. The real-world measurement is collected from a DIGIT sensor touching a ball of ...
- **p. 7 / V. SIM2REAL EXPERIMENTS - extractive body cue:** It makes the model more robust to a variety of illumination conditions (Sim2Real with augmentation vs.
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The cost is defined as cumulative error distance in tactile space P t ∥¯xt∥, and we set eight different target locations and take the average ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 simulation 문제를 이해하기 위해 읽는다. 본문은 One aspect that has proven so far to be difficult to simulate is tactile sensing, and in particular visionbased tactile sensors [2], [3], [4] which provide rich highresolution measurements.를 문제로 두고, This allows to perform orders of magnitude more experiments at a fraction of the effort, and in many cases of the time.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
