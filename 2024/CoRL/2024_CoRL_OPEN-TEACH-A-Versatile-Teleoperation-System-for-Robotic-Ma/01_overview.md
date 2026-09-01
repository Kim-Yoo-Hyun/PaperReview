# OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/iyer25a.html.
> PDF retrieval source: https://arxiv.org/pdf/2403.07870. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, teleoperation, cross-embodiment, dexterous manipulation, bimanual manipulation, data collection
- Official paper: https://proceedings.mlr.press/v270/iyer25a.html
- Full-text retrieval: https://arxiv.org/pdf/2403.07870
- Code/Project: https://open-teach.github.io/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space.를 문제로 두고, The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in both simula ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** Open-sourced, user-friendly tools form the bedrock of scientific advancement across disciplines.
- **p. 2 / Abstract - extractive body cue:** The widespread adoption of data-driven learning has led to remarkable progress in multi-fingered dexterity, bimanual manipulation, and applications ranging from logistics to home robotics.
- **p. 2 / Abstract - extractive body cue:** However, existing data collection platforms are often proprietary, costly, or tailored to specific robotic morphologies.
- **p. 2 / Abstract - extractive body cue:** We present OPEN TEACH, a new teleoperation system leveraging VR headsets to immerse users in mixed reality for intuitive robot control.
- **p. 2 / Abstract - extractive body cue:** Built on the affordable Meta Quest 3, which costs $500, OPEN TEACH enables realtime control of various robots, including multi-fingered hands, bimanual arms, and mobile ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Recently proposed exoskeleton-based teleoperation frameworks like ALOHA [67], GELLO [61], and AirExo [14] attempt to alleviate this problem by having the human teleoperator directly control ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we present OPEN TEACH, an open-source framework for robot teleoperation that supports a variety of robots, including bimanual and multi-finger manipulation, all ...
- **p. 4 / IV. OPEN TEACH - extractive body cue:** In this section, we provide details about the VR-based teleoperation setup and the system design that enables data collection using this framework.
- **p. 4 / IV. OPEN TEACH - extractive body cue:** We observe that OPEN TEACH is the only framework that enables controlling multiple arms, hands, and mobile manipulators, is calibration-free, and is completely open-source.
- **p. 5 / IV. OPEN TEACH - extractive body cue:** The high frame rate streaming enables reactive control by the user, while widgets for visualizing the robot's camera view help the user focus on fine-grained ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O ...
- **p. 5 / IV. OPEN TEACH - extractive body cue:** We use different controllers for each.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O × A, behavior cloning (BC) aims to ... | multi-view observation, language/task label과 action trajectory | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING) |
| State/latent | Behavior, Cloning, Given, dataset, expert, rollouts, desired, task, form, observation, action, pairs | shared representation, embodiment/task identity와 data distribution | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 6 (4) How intuitive is the system for new users?) |
| Output/action | For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ∈A. | dataset sample 또는 learned policy action | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |
| Objective/outcome | Following this convention, the objective of BC is to find the value θ that maximizes the probability of the observed data. θ∗= argmax θ Y t P(at/ot; θ) (1) When constrained to ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 2 (I. INTRODUCTION), p. 2 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we present OPEN TEACH, an open-source framework for robot teleoperation that supports a variety of robots, including bimanual and multi-finger manipulation, all ...
- **p. 4 / IV. OPEN TEACH - extractive body cue:** In this section, we provide details about the VR-based teleoperation setup and the system design that enables data collection using this framework.
- **p. 4 / IV. OPEN TEACH - extractive body cue:** We observe that OPEN TEACH is the only framework that enables controlling multiple arms, hands, and mobile manipulators, is calibration-free, and is completely open-source.
- **p. 5 / IV. OPEN TEACH - extractive body cue:** The high frame rate streaming enables reactive control by the user, while widgets for visualizing the robot's camera view help the user focus on fine-grained ...
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies.
- **p. 6 / 4) How intuitive is the system for new users? - extractive body cue:** Similar to prior work [20, 22], these policies were learned within 20 minutes and achieved an average success rate of 82%, validating the high quality ...
- **p. 8 / 4) How intuitive is the system for new users? - extractive body cue:** On these tasks, OPEN TEACH demonstrates a higher success rate along with significantly reduced median time to complete tasks compared to the other baselines.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |
| Embodiment/environment | The primary idea behind OPEN TEACH is that given any robotic setup, a user can purchase an affordable off-the-shelf VR headset (in this case, Quest 3) and plug the headset and robot ... | hardware/simulator version and reset protocol | p. 6 (4) How intuitive is the system for new users?), p. 6 (V. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | Robot Setup Task Number of Demos Success Rate Franka-Allegro Open Box 3 9/10 Grasp Sponge 6 7/10 Pick Up Tea Sachet 4 7/10 Grasp Object and Twist 6 8/10 Allegro Sim Flip ... | role, split, size and leakage | p. 6 (4) How intuitive is the system for new users?), p. 6 (V. EXPERIMENTAL EVALUATION), p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?) |
| Metric | In Table IV, we present a comparative analysis of success rates and median completion times for new users across Holo-Dex, AnyTeleop, and OPEN TEACH for the tasks of cube flipping and pinch ... | definition, denominator, direction and uncertainty | p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |
| Baseline/ablation | On these tasks, OPEN TEACH demonstrates a higher success rate along with significantly reduced median time to complete tasks compared to the other baselines. | fair input/data/compute/action matching | p. 8 (4) How intuitive is the system for new users?), p. 5 (Figure/Table caption), p. 8 (4) How intuitive is the system for new users?) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. LIMITATIONS AND DISCUSSION - extractive body cue:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. High ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 robot_data 문제를 이해하기 위해 읽는다. 본문은 The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space.를 문제로 두고, The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in both simula ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 5 (IV. OPEN TEACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
