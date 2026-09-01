# Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p111.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p111.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, multi-contact, trajectory optimization
- Official paper: https://www.roboticsproceedings.org/rss21/p111.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p111.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p111.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any learning framework ‘The goal of the new contact model is ...를 문제로 두고, Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A significant barrier preventing model-based methods from achieving real-time and versatile dexterous robotic maniptation is the inherent complexity of multi-contact dynamics. ‘Traditionally formulated as complementarity ...
- **p. 1 / Abstract - extractive body cue:** Our new model, derived from the duality of optimization-based contact models, dispenses with the complementarity constructs entirely, providing
- **p. 1 / Abstract - extractive body cue:** 1s closed-form time stepping, uutomatic satisfaction with Coulomb's friction
- **p. 1 / Abstract - extractive body cue:** ind Allegro hand on-palm reorientation, all performed with rse objects.
- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 2 / Abstract - extractive body cue:** (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any learning framework ‘The ...
- **p. 1 / Abstract - extractive body cue:** This introduces computational challenges in both learning of contact dynamics [42] and combinatorics optimization of contact modes [14, 41.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 1 / Front matter - extractive body cue:** 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols.
- **p. 2 / Abstract - extractive body cue:** Our method sets a new benchmark for model-based contact-rich dexterous manipulation: « Highly versatile dexterity: 96.5% average success rate across all objects and environments « ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** (62, 33] developed penalty-based contact models.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** 1) Nonconvex Complementarity Contact Models: Rigid body contact dynamics is traditionally formulated using complermentarity models [S1, 49, 52]: it enforces no interpenetration and no contact ...
- **p. 5 / C. Physical Interpretation of the New Model - extractive body cue:** The total force consists of two components: (i) the non-contact force b (e.g., gravity and actuation forces) shown in green arrows in Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This implementation creates « closed-loop control effect on the real system, ie., feedback from system state qf to control input 1 (qi | RGB-D/point cloud, object state와 contact/task observation | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model) |
| State/latent | implementation, creates, closed-loop, control, effect, real, system, feedback, state, input, manipulation, MPC | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model) |
| Output/action | In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system state qf encountered at the policy rollout step & and ... | grasp, pose, force 또는 end-effector trajectory | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 2 (Abstract) |
| Objective/outcome | With qo, (8) searches for the optimal input sequence (ty and Us, are control bounds), by minimizing the path c(-) and final cost V(-). | task completion, contact success, pose/force error와 generalization | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 1 / Front matter - extractive body cue:** 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols.
- **p. 2 / Abstract - extractive body cue:** Our method sets a new benchmark for model-based contact-rich dexterous manipulation: « Highly versatile dexterity: 96.5% average success rate across all objects and environments « ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** (62, 33] developed penalty-based contact models.
- **p. 10 / B. MPC Setting and Results - extractive body cue:** (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success
- **p. 10 / B. MPC Setting and Results - extractive body cue:** to the very low success rate of Implicit MPC for this task type,
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the upper panel shows the success rate across ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |
| Embodiment/environment | ABLE Il: The model setting for all objects and tasks. | hardware/simulator version and reset protocol | p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results) |
| Dataset/benchmark | to the very low success rate of Implicit MPC for this task type, | role, split, size and leakage | p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |
| Metric | Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the upper panel shows the success rate across 20 trials based on criterion (49). The ... | definition, denominator, direction and uncertainty | p. 12 (Figure/Table caption), p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |
| Baseline/ablation | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | fair input/data/compute/action matching | p. 10 (B. MPC Setting and Results), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. MPC Setting and Results - extractive body cue:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 17: An failure case for stick reorientation,
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical velocity trajectories, respectively. Compared to MuloCo, our ...
- **p. 9 / A. Environment and Task Setup - extractive body cue:** The fingertips must coordinate to prevent the object from falling while moving it to the target.
- **p. 10 / B. MPC Setting and Results - extractive body cue:** Fil postion Vial quaeiion MPC soe Succes ust prevent the object from falling while moving it to 8% Shor 8) ere 8) ng time te ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any learning framework ‘The goal of the new contact model is ...를 문제로 두고, Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (C. Reinforcement Learning for Dexterous Manipulation), p. 2 (A. Rigid Body Multi-contact Models) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
