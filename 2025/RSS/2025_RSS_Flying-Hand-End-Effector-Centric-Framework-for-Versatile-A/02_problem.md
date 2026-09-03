# Problem - Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p130.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction)): However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, In real-world scenarios, manipulation tasks ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Aerial manipulation has recently attracted inereasing interest from both industry and academia.
- **p. 1 / Abstract - extractive body cue:** Previous approaches have demonstrated success in various specific tasks.
- **p. 1 / Abstract - extractive body cue:** However, their hardware design and control frameworks are often tightly coupled with task specifications, limiting the detelopment of cros-las and crompatform algorithms, Ingpred by the ...
- **p. 1 / Abstract - extractive body cue:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller ...
- **p. 1 / Abstract - extractive body cue:** Real-world experiments show that the proposed framework significantly improves end-effector tracking accuracy and can handle multiple aerial teleoperation and tion learning tasks, including writing, peg-inchanging ...
- **p. 1 / 1. Iyrropuction - extractive body cue:** However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** However, there is no precedent to incorporate such IL-based policy into aerial manipulation fields due to the lack of a mature demonstration collection system, such ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | After, train, joint, space, ACT, policy, same, training, setting, ee-centric | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | hierarchical, framework, consists, understanding, module, trained, large, visual-language | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: After, train, joint, space, ACT, policy, same, training, setting, ee-centric | p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface) |
| Decision / output variable | joint/whole-body action; body terms: framework, consists, fully-actuated, hexarotor, DoF, robotic, end-effector-centrie, whole-body | p. 1 (Abstract), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: MPC, formulation, minimizes, cost, function, over, finite, time | p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 10 (B. Implementation Details), p. 11 (B. Implementation Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (B. Implementation Details), p. 10 (B. Implementation Details), p. 11 (B. Implementation Details) |
| Success / guarantee | motion/task success and recovery | p. 10 (B. Implementation Details), p. 11 (B. Implementation Details), p. 10 (B. Implementation Details) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** However, there is no precedent to incorporate such IL-based policy into aerial manipulation fields due to the lack of a mature demonstration collection system, such ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** Although the end-effector-centric paradigm has shown the advantage of versatility in the manipulation field, applying it to aerial manipulation systems presents significant challenges due to ...
- **p. 3 / C. Teleportation and Imitation Learning - extractive body cue:** their method is highly coupled with the specific UAM design, and the system struggles with versatile tasks due t0 the workspace limitation.
- **p. 2 / 1. Iyrropuction - extractive body cue:** We believe the proposed framework provides a step toward standardizing and unifying aerial manipulation into the broader manipulation ‘community, advancing the field toward greater versatility ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (VII. EE-CENTRIC TELEOPERATION AND POLICY), p. 2 (1. Iyrropuction)): Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for ...

- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** [As we mentioned, our framework enables the decoupling between the high-level policy and low-level controller, with the ee-centric interface serving asthe sole connection between them.
- **p. 2 / B. Mobile Manipulation Framework and EE-Centric Interface - extractive body cue:** [25] proposed a framework that consists of a robust humanoid whole-body controller with a high-level policy, either an autonomous agent like GPT-40 or an imitation ...
- **p. 7 / VII. EE-CENTRIC TELEOPERATION AND POLICY - extractive body cue:** In this section, we introduce two aerial manipulation systems we ‘developed based on this framework: the ee-centrc aerial tele- ‘operation system and the imitaton-Iearning-based autonomous ...
- **p. 2 / 1. Iyrropuction - extractive body cue:** By effectively decoupling high-level policies from low-level control, it enables the development ‘of embodiment-agnostic policies 47}, {10}.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Incorporating onboard perception to detect obstacles and generate safety constraints in real-time will be our next step, as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | MPC (orange) suffers from significant motion lag, as DFFC fails to account for trajectory feedforward. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (B. EE-Centrie Policy Learning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction), p. 3 (C. Teleportation and Imitation Learning), p. 2 (1. Iyrropuction), interface p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning), p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (B. EE-Centrie Policy Learning), objective p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 6 (A. End-Effector-Centric Model Predictive Controller), p. 10 (B. Implementation Details), p. 11 (B. Implementation Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, most previous works have been tailored to specific tasks, developing unique platforms and algorithms accordingly, lacking the ability to handle different types of tasks, In real-world scenarios, manipulation tasks ... (p. 1, 1. Iyrropuction).
- **Formulation-changing contribution:** Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector controller enables efficient and ‘operation for ... (p. 1, Abstract).
- **Assumption/failure evidence:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. (p. 11, IX. LIMITATIONS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
