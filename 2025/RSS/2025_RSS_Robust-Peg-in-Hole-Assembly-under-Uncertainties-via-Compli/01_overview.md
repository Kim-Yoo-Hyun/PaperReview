# Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p060.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p060.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, peg-in-hole, compliance, uncertainty, assembly
- Official paper: https://www.roboticsproceedings.org/rss21/p060.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p060.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted as the example).를 문제로 두고, (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robust and adaptive robotic peg-in-hole assembly. tunder tight tolerances is e
- **p. 1 / Abstract - extractive body cue:** However, it remains an physical uncertainties from contact-rie exceed the allowed clearance.
- **p. 1 / Abstract - extractive body cue:** In this paper, we study hon age contact between the peg and its matching hole to ‘uncertainties in the assembly process under unstructured settings.
- **p. 1 / Abstract - extractive body cue:** By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli
- **p. 1 / Abstract - extractive body cue:** interactions for the peg to 1) iter
- **p. 3 / A. Preliminaries - extractive body cue:** Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted ...
- **p. 4 / B. Problem Statement - extractive body cue:** As % shrinks over steps, the expected spread of Ton) decreases and the uncertainty range of the perceived hole's state is reduced,

## Core Idea

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Let n represents the positive direction of Z-axis of {'} with reference to {O} at the inclined state, we use a as the inclined angle ...
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** We first define the task-specific interactions based on the task mechanics in Section IV-A.
- **p. 4 / IV. FUNNEL-BASED MANIPULATION PLANNING - extractive body cue:** Then, we introsuce the formal approach to construct manipulation funnels in perception state space (Section IV-B) and execution task space (Section IV-C),

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | An interaction command cy = (xe, x3) at time ¢ is defined by its starting state x, (considered steady as %¢ - 0) and a desired state x}. | RGB-D/point cloud, object state와 contact/task observation | p. 4 (A. Preliminaries), p. 4 (B. Problem Statement) |
| State/latent | interaction, command, time, defined, starting, state, considered, steady, desired, Execution, Task, Space | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (A. Preliminaries), p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Output/action | Execution Task Space: Let Ax be the deviation between the steady state x, and the peg-in-hole state x", Based ‘on the estimated state distribution of Pr:(Tow), we aim to shrink Ax at ... | grasp, pose, force 또는 end-effector trajectory | p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Objective/outcome | forming an aligned comer between the inclined peg and the target hole to create contact constraints for undesired motion freedoms and progressively enter the allowed clearance (as illustrated in Fig. | task completion, contact success, pose/force error와 generalization | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |

## Main Claims and Actual Contribution

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.
- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.
- **p. 6 / B. Perception Manipulation Funnet - extractive body cue:** Additionally, a maximum entropy-based method is introduced to improve convergence efficiency.
- **p. 8 / 2 Sample grid points G - Area - extractive body cue:** Successful insertion motions are formulated as a sequence of interactions $ = [e},¢¥, ..¢?] that connect the initial inclined state to the target peg-inhole configuration.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: (a) Overview of the System Setup; (b) Ablation study on the perception manipulation funnel; (c) Ablation study on the physical manipulation funnel; (d) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (B. Perception Manipulation Funnet), p. 8 (2 Sample grid points G - Area) |
| Embodiment/environment | Despite the trajectory being a dominant action representation in manipulation planning, itis unsuitable for funnel-based ‘manipulations as interactions with the task environment are allowed to alter the motion of the manipulator [39]. | hardware/simulator version and reset protocol | p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area) |
| Dataset/benchmark | Interaction with inclined states is designed to identify and exploit its environmental contact constraints. | role, split, size and leakage | p. 5 (A. Task Mechanics and Interaction Primitives), p. 6 (2 Sample grid points G - Area), p. 5 (A. Task Mechanics and Interaction Primitives), p. 7 (2 Sample grid points G - Area) |
| Metric | Fig. 1: Motivation, Acknowledging that real-world uncertainties are inevitable, we exploit environmental constraints t0 shape the manipulation process toward the desired outcome rather than expecting the robot to precisely execute any t ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Baseline/ablation | Specifically, our objective is to formulate a potential well to let vj be the local minimum in a potential energy field so that vs tends to rest atv; without escaping. | fair input/data/compute/action matching | p. 7 (2 Sample grid points G - Area), p. 11 (Figure/Table caption), p. 7 (2 Sample grid points G - Area) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 2 Sample grid points G - Area - extractive body cue:** pose +1 automatically falls into its nearby local minimum
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than {C} in the work! frame.
- **p. 9 / 2 Sample grid points G - Area - extractive body cue:** Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric size.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted as the example).를 문제로 두고, (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (A. Preliminaries), p. 4 (B. Problem Statement), p. 4 (A. Preliminaries), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), p. 4 (IV. FUNNEL-BASED MANIPULATION PLANNING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
