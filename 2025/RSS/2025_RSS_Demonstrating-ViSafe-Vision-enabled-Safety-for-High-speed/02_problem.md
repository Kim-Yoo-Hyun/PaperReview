# Problem - Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p002.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (I. INTRopI), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 1 (Abstract)): However, most existing avoidance logics require special sensors and information to provide RAS.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 1 / Abstract - extractive body cue:** ViSafe offers a fullstack solution to the Detect and Avoid (DAA) problem by ightly integrating a learning-based edge-AI framework with ‘custom multi-camera hardware prototype designed ...
- **p. 1 / Abstract - extractive body cue:** By leveraging perceptual. input-focused ‘control barrier functions (CBF) to design, encode, and enforce safety thresholds, ViSafe can provide provably safe runtime guarantees for self-separation in ...
- **p. 1 / Abstract - extractive body cue:** We evaluate ViSafe's performance through an extensive test ‘campaign involving both simulated digital twins and real-world flight scenarios.
- **p. 1 / Abstract - extractive body cue:** By independently varying agent types, closure rates, interaction geometries, and environmental conditions (e.,
- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** However, most existing avoidance logics require special sensors and information to provide RAS.
- **p. 2 / I. INTRopI - extractive body cue:** These tests were run using the same hardware as the real-world payload, thereby minimizing our sim-to-real gap for testing.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most existing avoidance logics require special sensors and information to provide RAS. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | These logics involve generating cost tables for agent states and possible actions through simulation and optimization [8]. | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | logics, involve, generating, cost, tables, agent, states, possible, actions, through | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | follows, While, visual, detection, module, Seetion, IV-A, provides | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: logics, involve, generating, cost, tables, agent, states, possible, actions, through | p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (2) Custom-built SWaP-C hardware that simultaneously), p. 4 (IV. ViSafe FRAMEWORK) |
| Decision / output variable | filtered/recovery action u_safe; body terms: There, variants, algorithm, different, agent, types, airspaces, ACAS | p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 1 (Abstract), p. 2 (I. INTRopI) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: supervisory, controller, enforces, safety, actuation, constraints, devise, defined | p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 7 (A. Experiment Design), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRopI - extractive body cue:** These tests were run using the same hardware as the real-world payload, thereby minimizing our sim-to-real gap for testing.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** Squires er al{51] identify key challenges with designing CBF for collision avoidance and propose a construction technique.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** In particular, for aireraft detection, the challenge is detecting small objects within high-resolution images, where keypoint-based architectures prove more effective than traditional anchor-based methods like ...
- **p. 1 / Abstract - extractive body cue:** Existing solutions, such 4s Autonomous Collision Avoidance Systems (ACAS) [33] and Unmanned ‘Traffic Management (UTM) [18] frameworks,

## What the Paper Changes

PDF body contribution framing (p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 1 (Abstract), p. 2 (I. INTRopI), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 6 (C. Supervisory Safety Controller)): There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS algorithms is the availability of ...

- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 2 / I. INTRopI - extractive body cue:** We present ViSafe, a vision-only airborne collision avoidance system to impart see-and-avoid capabilities to sUAS.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** The control input w < R? consists of the rate of change of speed and heading, ic., Yown and Zoun Additionally, we also consider control ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Inspired by [32], we propose the following CBF:

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (2) Custom-built SWaP-C hardware that simultaneously), p. 4 (IV. ViSafe FRAMEWORK), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (I. INTRopI), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 1 (Abstract), interface p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (2) Custom-built SWaP-C hardware that simultaneously), p. 4 (IV. ViSafe FRAMEWORK), p. 1 (Abstract), objective p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** ViSafe offers a fullstack solution to the Detect and Avoid (DAA) problem by ightly integrating a learning-based edge-AI framework with ‘custom multi-camera hardware prototype designed under ‘SWaP-C constraints. (p. 1, Abstract).
- **Formulation-changing contribution:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, a high-speed vi ‘only airborne ... (p. 1, Abstract).
- **Assumption/failure evidence:** Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the intruder is below the horizon, As acknowledged in the benchmarking of ‘our ... (p. 11, B. Limitations).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
