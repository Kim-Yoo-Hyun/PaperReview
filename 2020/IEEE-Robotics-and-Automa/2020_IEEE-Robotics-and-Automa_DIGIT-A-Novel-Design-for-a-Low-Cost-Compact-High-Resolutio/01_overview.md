# DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/LRA.2020.2977257.
> PDF retrieval source: https://doi.org/10.1109/LRA.2020.2977257. Reading tracker status/evidence was not changed.

- Year/Venue: 2020 / IEEE Robotics and Automation Letters
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, dexterous manipulation, contact
- Official paper: https://doi.org/10.1109/LRA.2020.2977257
- Full-text retrieval: https://doi.org/10.1109/LRA.2020.2977257
- Code/Project: https://digit.ml/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 [12], [13], [14], [15], the main bottleneck for wide adoption of touch sensing in robotic manipulation is the lack of sensors that fulfill at the same time all the requirements of being ...를 문제로 두고, To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Despite decades of research, general purpose inhand manipulation remains one of the unsolved challenges of robotics.
- **p. 1 / Abstract - extractive body cue:** One of the contributing factors that limit current robotic manipulation systems is the difficulty of precisely sensing contact forces - sensing and reasoning about contact ...
- **p. 1 / Abstract - extractive body cue:** As a step towards enabling better robotic manipulation, we introduce DIGIT, an inexpensive, compact, and high-resolution tactile sensor geared towards in-hand manipulation.
- **p. 1 / Abstract - extractive body cue:** DIGIT improves upon past vision-based tactile sensors by miniaturizing the form factor to be mountable on multi-fingered hands, and by providing several design improvements that ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a multi-finger robotic hand.
- **p. 1 / I. INTRODUCTION - extractive body cue:** [12], [13], [14], [15], the main bottleneck for wide adoption of touch sensing in robotic manipulation is the lack of sensors that fulfill at the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One contributing factor is the difficulty of precisely estimating contact forces.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, we present the design and manufacturing process of DIGIT, and analyze the properties of the resulting sensor.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of the DIGIT sensor by training deep neural network model-based controllers to manipulate glass marbles in-hand with a multi-finger robotic hand.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Forces are an important representation to understand and plan interactions with the environment - grasping a small screw, inserting a key, and manipulating a glass ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Second, we demonstrate the sensor by learning to manipulate small objects with a multi-finger hand from raw tactile inputs. | tactile image/force, vision과 proprioceptive history | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| State/latent | Second, demonstrate, sensor, learning, manipulate, small, objects, multi-finger, hand, tactile, inputs, One | contact geometry, force state 또는 latent dynamics | p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Output/action | One of the contributing factors that limit current robotic manipulation systems is the difficulty of precisely sensing contact forces - sensing and reasoning about contact forces are crucial to accurately control interactions ... | grasp/contact action, force command 또는 object motion | p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | To provide the robotic community access to reliable and low-cost tactile sensors, we open-source the DIGIT design at www.digit.ml. | slip/contact success, force/pose error와 robustness | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, we present the design and manufacturing process of DIGIT, and analyze the properties of the resulting sensor.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To scale up tactile-MPC, we propose new approaches for dynamics model learning and task specification that dramatically reduce the computational cost.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** This result is in agreement with previous results in [17], where learned models outperform simple handtuned controllers.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We hypothesize that improving the low level controller and collecting more data for improving the learned model will help in decreasing the number of marbles ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** These results are shown in Table III.
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | To validate our modeling choices, we measure the prediction error on a standard benchmark for video prediction, the BAIR robot pushing dataset [36], in addition to our DIGIT tactile marble manipulation videos. | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | A fixed P matrix can only be optimal in some of the operating regions but not all of them, especially at the boundary of the robot configuration space where some of the ... | role, split, size and leakage | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Metric | In both datasets, we use 64 × 64 images and compare prediction performance with CDNA [35] used for tactile servoing in [17] in terms of per-pixel root mean squared error (RMSE) on ... | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Baseline/ablation | However, compared to our MPC approach which is virtually parameters-free, this proved significantly more challenging. | fair input/data/compute/action matching | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** This is a very challenging task because it requires controlling the slipping and rolling dynamics of the marble over the small and deformable DIGIT surfaces ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** 3) and the robustness of the gel (Section III-D), we now evaluate the DIGIT in the complex in-hand tactile manipulation task described in Section IV.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** (Bottom) Due to control noise, potential planning inaccuracies and the challenging nature of this task, the hand tends to drop marbles over time.

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 [12], [13], [14], [15], the main bottleneck for wide adoption of touch sensing in robotic manipulation is the lack of sensors that fulfill at the same time all the requirements of being ...를 문제로 두고, To better fulfill these requirements, in this paper, we present the design of a novel tactile sensor.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 7 (V. EXPERIMENTAL RESULTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
