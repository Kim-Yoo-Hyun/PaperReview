# Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p002.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p002.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, safe control, collision avoidance, control barrier function, aerial robotics, sim-to-real
- Official paper: https://www.roboticsproceedings.org/rss21/p002.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p002.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, most existing avoidance logics require special sensors and information to provide RAS.를 문제로 두고, There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS algorithms is the availability of extended surveillance ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 1 / Abstract - extractive body cue:** ViSafe offers a fullstack solution to the Detect and Avoid (DAA) problem by ightly integrating a learning-based edge-AI framework with ‘custom multi-camera hardware prototype designed ...
- **p. 1 / Abstract - extractive body cue:** By leveraging perceptual. input-focused ‘control barrier functions (CBF) to design, encode, and enforce safety thresholds, ViSafe can provide provably safe runtime guarantees for self-separation in ...
- **p. 1 / Abstract - extractive body cue:** We evaluate ViSafe's performance through an extensive test ‘campaign involving both simulated digital twins and real-world flight scenarios.
- **p. 1 / Abstract - extractive body cue:** By independently varying agent types, closure rates, interaction geometries, and environmental conditions (e.,
- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** However, most existing avoidance logics require special sensors and information to provide RAS.
- **p. 2 / I. INTRopI - extractive body cue:** These tests were run using the same hardware as the real-world payload, thereby minimizing our sim-to-real gap for testing.

## Core Idea

- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS ...
- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 2 / I. INTRopI - extractive body cue:** We present ViSafe, a vision-only airborne collision avoidance system to impart see-and-avoid capabilities to sUAS.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** The control input w < R? consists of the rate of change of speed and heading, ic., Yown and Zoun Additionally, we also consider control ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Inspired by [32], we propose the following CBF:
- **p. 7 / C. Supervisory Safety Controller - extractive body cue:** We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Considering these three key requirements, we used a Control Barrier Function (CBF) based Quadratic Program (QP) for our supervisory safety controller.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These logics involve generating cost tables for agent states and possible actions through simulation and optimization [8]. | observation, uncertainty/risk estimate와 task command | p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (2) Custom-built SWaP-C hardware that simultaneously) |
| State/latent | logics, involve, generating, cost, tables, agent, states, possible, actions, through, simulation, optimization | safe set, recovery state 또는 constraint margin | p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (2) Custom-built SWaP-C hardware that simultaneously), p. 4 (IV. ViSafe FRAMEWORK) |
| Output/action | streams multiple camera inputs, provides state estimation, performs deep learning model edge inference, and computes avoidance maneuvers on board in real time. | shielded, recovery 또는 safe action | p. 2 (2) Custom-built SWaP-C hardware that simultaneously), p. 4 (IV. ViSafe FRAMEWORK), p. 1 (Abstract) |
| Objective/outcome | Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be defined as C, then a straightforward distance ... | task return과 violation/failure probability | p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller) |

## Main Claims and Actual Contribution

- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS ...
- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 2 / I. INTRopI - extractive body cue:** We present ViSafe, a vision-only airborne collision avoidance system to impart see-and-avoid capabilities to sUAS.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** The control input w < R? consists of the rate of change of speed and heading, ic., Yown and Zoun Additionally, we also consider control ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Inspired by [32], we propose the following CBF:

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (A. Experiment Design) |
| Embodiment/environment | These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. | hardware/simulator version and reset protocol | p. 7 (A. Experiment Design) |
| Dataset/benchmark | These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. | role, split, size and leakage | p. 7 (A. Experiment Design) |
| Metric | The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. | definition, denominator, direction and uncertainty | p. 7 (A. Experiment Design), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Baseline/ablation | Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. Across the diferent weather scenarios, ViSafeshoweases consistent b ... | fair input/data/compute/action matching | p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / VI. LEARNED CHALLENGES AND LIMITATIONS - extractive body cue:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use ...
- **p. 7 / A. Experiment Design - extractive body cue:** The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows the various agents, collision geometries, commanded ground ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, most existing avoidance logics require special sensors and information to provide RAS.를 문제로 두고, There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS algorithms is the availability of extended surveillance ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (I. INTRopI), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 1 (Abstract), p. 7 (C. Supervisory Safety Controller) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** ViSafe offers a fullstack solution to the Detect and Avoid (DAA) problem by ightly integrating a learning-based edge-AI framework with ‘custom multi-camera hardware prototype designed under ‘SWaP-C constraints. (p. 1, Abstract).
- **Actual contribution:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, a high-speed vi ‘only airborne ... (p. 1, Abstract).
- **Evaluation boundary:** These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. (p. 7, A. Experiment Design).
- **Explicit failure boundary:** Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the intruder is below the horizon, As acknowledged in the benchmarking of ‘our ... (p. 11, B. Limitations).
