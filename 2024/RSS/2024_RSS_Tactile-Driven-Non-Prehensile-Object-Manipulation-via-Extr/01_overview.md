# Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p135.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p135.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, contact-rich manipulation, tactile sensing, non-prehensile manipulation
- Official paper: https://www.roboticsproceedings.org/rss20/p135.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p135.pdf
- Code/Project: https://www.roboticsproceedings.org/rss20/p135.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions.를 문제로 두고, The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization and capable of producing a variety of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we consider the problem of nonprehensile manipulation using grasped objects.
- **p. 1 / Abstract - extractive body cue:** This problem is a superset of many common manipulation skills including instances of tool-use (e.g., grasped spatula flipping a burger) and assembly (e.g., screwdriver tightening ...
- **p. 1 / Abstract - extractive body cue:** Here, we present an algorithmic approach for non-prehensile manipulation leveraging a gripper with highly compliant and high-resolution tactile sensors.
- **p. 1 / Abstract - extractive body cue:** Our approach solves for robot actions that drive object poses and forces to desired values while obeying the complex dynamics induced by the sensors as ...
- **p. 1 / Abstract - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions.
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** The key technical challenges are computing trajectories that obey the many unilateral and hybrid contact constraints, kinematic constraints imposed by geometry, accounting for the compliance ...

## Core Idea

- **p. 5 / IV. METHODOLOGY - extractive body cue:** The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** An integral part of our method is the use of tactile sensors.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Trajectory Optimization Overview: Given a desired trajectory of the extrinsic object {xeo,k}K k=1 as well as the contact modes {ck}K k=1, our method optimizes the ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Extrinsic Contact Trajectory Optimization The goal of the controller is to generate a trajectory of endeffector and grasped object poses that results in the desired ...
- **p. 6 / IV. METHODOLOGY - extractive body cue:** We use the log-barrier function to enforce this constraint.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic contacts; ii) a passive compliance model for ... | tactile image/force, vision과 proprioceptive history | p. 3 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| State/latent | composed, core, components, stateestimation, pipeline, feedback, tactile, sensor, estimate, object, pose, extrinsic | contact geometry, force state 또는 latent dynamics | p. 3 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | Here, we use high-resolution and highly deformable tactile sensors (Soft Bubbles [2]) because they: i) allow for state-estimation that provides key feedback for controls that would not be available without the sensors, ... | grasp/contact action, force command 또는 object motion | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY) |
| Objective/outcome | The resultant cost function is defined as follows: L = Lcone + Lsmooth + Lcontact force + Lpenetration where: • Cone Loss (Lcone): Incentivizes the contact forces between the grasped object and ... | slip/contact success, force/pose error와 robustness | p. 6 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 5 / IV. METHODOLOGY - extractive body cue:** The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** An integral part of our method is the use of tactile sensors.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Trajectory Optimization Overview: Given a desired trajectory of the extrinsic object {xeo,k}K k=1 as well as the contact modes {ck}K k=1, our method optimizes the ...
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance.
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Our experiments show that the closedloop controllers achieve superior performance tracking the desired trajectories than the other tested control approaches.
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS) |
| Embodiment/environment | This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions. | hardware/simulator version and reset protocol | p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS) |
| Dataset/benchmark | For object-object interactions, we attach the object to the scene similar to the setup described in section V-A and have the robot perform object-object interactions. | role, split, size and leakage | p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS), p. 6 (V. EXPERIMENTS AND RESULTS), p. 6 (V. EXPERIMENTS AND RESULTS) |
| Metric | We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error. | definition, denominator, direction and uncertainty | p. 8 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS) |
| Baseline/ablation | To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: one with 100 QP queries and another with 1000 queries. | fair input/data/compute/action matching | p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK In this paper, we proposed an approach to extrinsic object manipulation leveraging tactile sensor compliance, tactile sensor measurements, and contact ...
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** In this instance, the contacts between the object and the environment must be sticking, i.e. fc,i ∈int Fc,i. • Grasped Object Pivoting: The goal is ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We display the sticking contact points in red and the slipping contacts in green.
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** The desired contact mode is sticking contact between the grasped and extrinsic objects contacts, while the contact between the extrinsic object and the environment must ...
- **p. 9 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Additionally, we observed instances of slippage between the sensor and the grasped object, which violates the assumption of sticking contact between them.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Notation using a grasped tool. The main difference between this ap- proach and ours is that we consider different primitive motions beyond pivoting, ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions.를 문제로 두고, The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization and capable of producing a variety of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** In this paper, we consider the class of problems in which the robot is tasked with using an object grasped with tactile sensors to: i) transmit desired forces to the ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses and force transmission, then formulating ... (p. 3, IV. METHODOLOGY).
- **Evaluation boundary:** While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. (p. 10, V. EXPERIMENTS AND RESULTS).
- **Explicit failure boundary:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. (p. 10, V. EXPERIMENTS AND RESULTS).
