# Problem - Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p135.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p135.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we consider the problem of nonprehensile manipulation using grasped objects.
- **p. 1 / Abstract - extractive body cue:** This problem is a superset of many common manipulation skills including instances of tool-use (e.g., grasped spatula flipping a burger) and assembly (e.g., screwdriver tightening ...
- **p. 1 / Abstract - extractive body cue:** Here, we present an algorithmic approach for non-prehensile manipulation leveraging a gripper with highly compliant and high-resolution tactile sensors.
- **p. 1 / Abstract - extractive body cue:** Our approach solves for robot actions that drive object poses and forces to desired values while obeying the complex dynamics induced by the sensors as ...
- **p. 1 / Abstract - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions.
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** The key technical challenges are computing trajectories that obey the many unilateral and hybrid contact constraints, kinematic constraints imposed by geometry, accounting for the compliance ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These failures are due to the nonlinear, discontinuous, and multimodal nature of contact interactions. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | composed, core, components, stateestimation, pipeline, feedback, tactile, sensor, estimate, object | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | because, robots, future, will, likely, extensively, tactile, sensors | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: composed, core, components, stateestimation, pipeline, feedback, tactile, sensor, estimate, object | p. 3 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | contact-aware action/force; body terms: contribution, formulate, contact, trajectory, optimization, precisely, address, requirements | p. 5 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | contact prediction/control error; cue terms: resultant, cost, function, defined, follows, Lcone, Lsmooth, Lcontact | p. 5 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY) |
| Success / guarantee | slip/contact success and safe interaction | p. 8 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** The key technical challenges are computing trajectories that obey the many unilateral and hybrid contact constraints, kinematic constraints imposed by geometry, accounting for the compliance ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we consider the class of problems in which the robot is tasked with using an object grasped with tactile sensors to: i) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This makes our approach more robust to uncertainty and accessible given the lower technical barrier to entery.

## What the Paper Changes

PDF body contribution framing (p. 5 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY)): The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based optimization and capable of producing a ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** An integral part of our method is the use of tactile sensors.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method is able to produce a variety of "manipulation skills" and is amenable to gradient-based optimization by exploiting differentiability within contact modes (e.g., specifications ...
- **p. 3 / IV. METHODOLOGY - extractive body cue:** Our method is composed of 4 core components: i) a stateestimation pipeline using the feedback from the tactile sensor to estimate object pose and extrinsic ...
- **p. 5 / IV. METHODOLOGY - extractive body cue:** Trajectory Optimization Overview: Given a desired trajectory of the extrinsic object {xeo,k}K k=1 as well as the contact modes {ck}K k=1, our method optimizes the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | DISCUSSION, LIMITATIONS, AND FUTURE WORK In this paper, we proposed an approach to extrinsic object manipulation leveraging tactile ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In this instance, the contacts between the object and the environment must be sticking, i.e. fc,i ∈int Fc,i. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We display the sticking contact points in red and the slipping contacts in green. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY), objective p. 5 (IV. METHODOLOGY), p. 5 (IV. METHODOLOGY), p. 6 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), p. 4 (IV. METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In this paper, we consider the class of problems in which the robot is tasked with using an object grasped with tactile sensors to: i) transmit desired forces to the ... (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** The main contributions of our work are in components (iii) and (iv) where we augment the model in (ii) with contact-aware constraints for object poses and force transmission, then formulating ... (p. 3, IV. METHODOLOGY).
- **Assumption/failure evidence:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. (p. 10, V. EXPERIMENTS AND RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
