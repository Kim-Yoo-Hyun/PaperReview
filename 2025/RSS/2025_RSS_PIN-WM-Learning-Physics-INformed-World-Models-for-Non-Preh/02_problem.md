# Problem - PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p153.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p153.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Iyrropuction), p. 2 (A. Non-Prehensile Manipulation), p. 1 (1. Iyrropuction), p. 2 (2 Wuhan Universi), p. 3 (B. World Models for Policy Learning)): However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While non-prehensile manipulation (e.g, controlled. pushing/poking) constitutes a foundational robotic skil, its learning remains challenging due to the high sensitivity to comple physical interactions involving ...
- **p. 1 / Abstract - extractive body cue:** To achieve robust policy learning and generalization, we opt to learn a world model of the 3D rigid body dynamics involved in nonprehensile manipulations and ...
- **p. 1 / Abstract - extractive body cue:** Adopting differentiable physics simulation, PIN-WM can be learned with few-shot and task-agnostic physical interaction trajectories. ‘observational loss induced ‘aussian Splatting without needing state estimation.
- **p. 1 / Abstract - extractive body cue:** To bridge Sim2Real gaps, we turn the learned PIN-WM into a group of Digital Cousins via perturb physics and rendering parameters to generate diverse and ...
- **p. 1 / Abstract - extractive body cue:** learning robust non-prehensile manipulation skills with Sim2Real transfer, surpassing the Real2Sim2Real state-of-the-arts.
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed.
- **p. 2 / A. Non-Prehensile Manipulation - extractive body cue:** However, the large gap between simulation and reality poses significant cha lenges for transferring these policies to the real world [12, 45], Building an interactive ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | Adopting differentiable physics simulation, PIN-WM can be learned with few-shot and task-agnostic physical interaction trajectories. ‘observational loss induced ‘aussian Splatting without needing ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Adopting, differentiable, physics, simulation, PIN-WM, learned, few-shot, task-agnostic, physical, interaction | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | history, recent, states, actions, input, Domain, Rand, denoted | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: Adopting, differentiable, physics, simulation, PIN-WM, learned, few-shot, task-agnostic, physical, interaction | p. 1 (Abstract), p. 5 (B. Physics-INformed World Model), p. 14 (A. Implementation Details for Baselines) |
| Decision / output variable | filtered/recovery action u_safe; body terms: introduce, PIN-WM, Physies-INformed, World, Mode, allows, end-to-end, identification | p. 2 (2 Wuhan Universi), p. 2 (2 Wuhan Universi), p. 3 (C. Domain Randomization) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: transformed, observations, then, obtained, simulation, Equation, where, updated | p. 5 (B. Physics-INformed World Model), p. 6 (B. Physics-INformed World Model), p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 3 (B. World Models for Policy Learning), p. 4 (B. Physics-INformed World Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (B. World Models for Policy Learning), p. 6 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 14 (A. Implementation Details for Baselines), p. 7 (A. Evaluations in Simulation), p. 7 (A. Evaluations in Simulation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / A. Non-Prehensile Manipulation - extractive body cue:** However, the large gap between simulation and reality poses significant cha lenges for transferring these policies to the real world [12, 45], Building an interactive ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** The complex underlying dynamics, caused by factors such as friction, restitution, and inertia, make motion prediction difficult and complicate motion planning and control
- **p. 2 / 2 Wuhan Universi - extractive body cue:** To bridge the Sim2Real gap, we turn the identified digital twin into plenty of digital cousins [15] through physics-sware perturbations which perturb the physics and ...
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** However, purely data-driven world models rely heavily on the quantity and quality of training data and struggle to generalize to outof-distribution (OOD) scenarios {79, 62].

## What the Paper Changes

PDF body contribution framing (p. 2 (2 Wuhan Universi), p. 2 (2 Wuhan Universi), p. 3 (C. Domain Randomization), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (B. World Models for Policy Learning)): We introduce PIN-WM, a Physies-INformed World Mode! that allows end-to-end identification of a 3D rigid body ‘dynamical system from visual observations.

- **p. 2 / 2 Wuhan Universi - extractive body cue:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real ...
- **p. 3 / C. Domain Randomization - extractive body cue:** We provide an overview of our framework in Figure 2
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** *Shenzhen University ".
- **p. 3 / B. World Models for Policy Learning - extractive body cue:** In contrast, PIN-WM enables end-to-end identification of 3D rigid-body dynamics from visual observations using few-shot, task-agnostic interaction data, which facilitates the training of vision-based manipulation ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Since neither of the two methods learns rendering parameters and their trained policies cannot work without aligned visual ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The purely data-driven world model Dreamer V2 [27], albeit having access to more task-agnostic data, fails to accurately ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Fig. 10: Push cube object on a slippery plane. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We can observe that Dreamer V2 quickly converges on the training dataset, but it does not generalize well ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 5 (B. Physics-INformed World Model), p. 14 (A. Implementation Details for Baselines), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Iyrropuction), p. 2 (A. Non-Prehensile Manipulation), p. 1 (1. Iyrropuction), p. 2 (2 Wuhan Universi), p. 3 (B. World Models for Policy Learning), interface p. 1 (Abstract), p. 5 (B. Physics-INformed World Model), p. 14 (A. Implementation Details for Baselines), p. 1 (Abstract), objective p. 5 (B. Physics-INformed World Model), p. 6 (B. Physics-INformed World Model), p. 5 (B. Physics-INformed World Model), p. 3 (B. World Models for Policy Learning), p. 3 (B. World Models for Policy Learning), p. 4 (B. Physics-INformed World Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, significant challenges arise from the difficulty of fully dictating. the motion and pose of the object being pushed. (p. 1, 1. Iyrropuction).
- **Formulation-changing contribution:** + We conduct real robot implementation to demonstrate that our approach enables learning control policies with minimal task-agnostic interaction data and attains high performance Real2Sim2Real without real-world fine-tuning. (p. 2, 2 Wuhan Universi).
- **Assumption/failure evidence:** Moreover, the policies trained with physics-based alternatives exhibit unsatisfactory performance in the target domain, ‘One reason is that their world models failed to effectively ‘capture the target-domain dynamics. (p. 8, A. Evaluations in Simulation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
