# Dynamic Safety in Complex Environments: Synthesizing Safety Filters with Poisson's Equation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p137.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p137.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, safety filter, control barrier function, perception, humanoid, quadruped
- Official paper: https://www.roboticsproceedings.org/rss21/p137.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p137.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p137.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 humanoid 문제를 이해하기 위해 읽는다. 본문은 which present challenges in synthesizing safe controllers.를 문제로 두고, The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) we illustrate and prove how the resulting ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Synthesizing safe sets for robotic systems oper ating in complex and dynamically changing environments is fa challenging. problem.
- **p. 1 / Abstract - extractive body cue:** Solving this problem can enable the construction of safety filters that guarantee safe control actions- ‘most notably by employing Control Barrier Functions (CBFS).
- **p. 1 / Abstract - extractive body cue:** This paper presents an algorithm for generating safe sets from perception data by leveraging elliptic partial differential equations, specifically Poisson's equation.
- **p. 1 / Abstract - extractive body cue:** Given a local occupancy ‘map, we solve Poisson's equation subject to Dirichlet boundary ‘a novel forcing function.
- **p. 1 / Abstract - extractive body cue:** Specifically, we design a smooth guidance vector field, which encodes gradient information required for safety.
- **p. 1 / 1. IyrRopUCTION - extractive body cue:** which present challenges in synthesizing safe controllers.
- **p. 3 / B. Ouputs and Relative Degree - extractive body cue:** In what follows, we demonstrate how Poisson's equation can be leveraged to overcome these challenges and generate a single smooth function /: for environments with ...

## Core Idea

- **p. 2 / 1. IyrRopUCTION - extractive body cue:** The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** We propose several methods for constructing the forcing function within Poisson's equation, including an average flux method and a guidance field method {26} that provides ...
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive body cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to classes of systems with outputs of nonuniform ... | proprioception, reference pose/motion, visual or language command | p. 6 (B. Indirect Assignment - Variational Approach), p. 1 (1. IyrRopUCTION) |
| State/latent | focus, systems, defined, integrator, chains, input, appearing, last, layer-note, extended, classes, outputs | whole-body pose, balance/contact state와 skill/mode | p. 6 (B. Indirect Assignment - Variational Approach), p. 1 (1. IyrRopUCTION), p. 2 (1. IyrRopUCTION) |
| Output/action | Achieving this level of dynamic safety necessitates a quantifiable description of the safety requirement, i.e. a functional representation of the environment via a safety constraint, Additionally, this representation must be integrated ... | joint/whole-body action, motion target 또는 task trajectory | p. 1 (1. IyrRopUCTION), p. 2 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree) |
| Objective/outcome | Specifically, let h be the minimizer of the cost functional: | tracking, balance, skill/task success와 recovery | p. 5 (B. Indirect Assignment - Variational Approach), p. 5 (B. Indirect Assignment - Variational Approach), p. 4 (IV. FORCING FUNCTION CONSTRUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1. IyrRopUCTION - extractive body cue:** The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** However. the condition V-v(y) <0 may not necessarily hold for all y < ©, which is sufficient to guarantee h(y) > 0 in 2. ‘To ...
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** We focus on systems defined by integrator chains as (10), with the input appearing at the last layer-note that our method can be extended to ...
- **p. 2 / 1. IyrRopUCTION - extractive body cue:** We propose several methods for constructing the forcing function within Poisson's equation, including an average flux method and a guidance field method {26} that provides ...
- **p. 4 / IV. FORCING FUNCTION CONSTRUCTION - extractive body cue:** In this section, we present methods of designing forcing functions that ensure the solution to the boundary value problem for Poisson's equation (16) is a ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, producing
- **p. 8 / B. Hardware Experiments - extractive body cue:** The results corresponding to this experiment are depicted in Fig 5,

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Embodiment/environment | First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy map, buffered for robot size. | hardware/simulator version and reset protocol | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Dataset/benchmark | First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy map, buffered for robot size. | role, split, size and leakage | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Metric | ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 quadruped and G1 humanoid robots. | definition, denominator, direction and uncertainty | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Baseline/ablation | In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations. | fair input/data/compute/action matching | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These ...
- **p. 7 / VI. DEMONSTRATIONS - extractive body cue:** Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © where J® characterizes obstacle surfaces. and consider ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective.
- **p. 8 / B. Hardware Experiments - extractive body cue:** ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 quadruped ...
- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** Examining the value of h during the experiment, it ean be ‘observed that the robot effectively employed its safety filter to avoid collisions.

## Why Read It

World models, safety, uncertainty, and recovery의 humanoid 문제를 이해하기 위해 읽는다. 본문은 which present challenges in synthesizing safe controllers.를 문제로 두고, The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, (2) we illustrate and prove how the resulting ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree), p. 4 (A. Direct Assignment), p. 4 (A. Direct Assignment), p. 1 (Abstract), p. 8 (B. Hardware Experiments) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
