# Problem - ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich manipulation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Embodied intelligence for contact-rich manipulation has predominantly relied on position control, while explicit awareness and regulation of interaction forces remain under-explored, limiting stability, precision, and ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 1 / Abstract - extractive body cue:** ForceVLA2 introduces force-based prompts into the VLM expert to construct force-aware task concepts across stages, and employs a Cross-Scale Mixture-of-Experts (MoE) in the action expert ...
- **p. 1 / Abstract - extractive body cue:** To support learning and evaluation, we construct ForceVLA2-Dataset, containing 1,000 trajectories over 5 contact-rich tasks, including wiping, pressing, and assembling, with multi-view images, task prompts, ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments show that ForceVLA2 substantially improves success rates and reliability in contact-rich manipulation, outperforming π0 and π0.5 by 48.0% and 35.0%, respectively, across the ...
- **p. 2 / 1. Introduction - extractive body cue:** However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** Current VLAs, however, still lack mechanisms to reason about the spatiotemporal relationships required across different task stages and to integrate force perception with active force-position ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | A 6D force/torque sensor attached to the end-effector recorded interaction forces at 300 Hz, while the robot joint states and end-effector (EE) ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | force/torque, sensor, attached, end-effector, recorded, interaction, forces, while, robot, joint | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Inspired, findings, human, sensorimotor, control, posit, force, acts | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: force/torque, sensor, attached, end-effector, recorded, interaction, forces, while, robot, joint | p. 5 (4. ForceVLA2-Dataset), p. 4 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework) |
| Decision / output variable | contact-aware action/force; body terms: contributions, summarized, follows, introduce, ForceVLA2, first, end-to-end, hybrid | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract) |
| Objective / loss / cost | contact prediction/control error; cue terms: parallel, force, observation, bypasses, high-level, fusion, modulates, action | p. 3 (3. ForceVLA2 Framework), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 3 (3.1. Long-Horizon Force Awareness via Prompting) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1. Introduction), p. 3 (3.1. Long-Horizon Force Awareness via Prompting), p. 4 (3.1. Long-Horizon Force Awareness via Prompting) |
| Success / guarantee | slip/contact success and safe interaction | p. 6 (5.2. Main Experiment Results), p. 6 (5.1. Experiment Setting), p. 7 (5.2. Main Experiment Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Current VLAs, however, still lack mechanisms to reason about the spatiotemporal relationships required across different task stages and to integrate force perception with active force-position ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these models remain confined to virtual domains, lacking the embodiment necessary for authentic physical understanding and interaction in real-world settings.
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this limitation, vision-language-action models (VLAs) [2, 3, 22, 47, 50] extend VLMs toward physical intelligence by seamlessly connecting perception and reasoning to embodied ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 3 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework)): Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ...

- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 3 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** To address this, we introduce force prompts as textual cues that indicate the current subtask and encode stage-specific physical context, thereby constructing force-aware task concepts.
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Building upon these principles, we propose the ForceVLA2 architecture, which integrates multi-scale perception, contextual reasoning, and force-aware manipulation into a unified VLA framework.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In contrast, other VLAs slowly chase the new EE 6D pose, leading to failure to maintain stable contact. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (4. ForceVLA2-Dataset), p. 4 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework), p. 3 (3.1. Long-Horizon Force Awareness via Prompting). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 5 (4. ForceVLA2-Dataset), p. 4 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework), p. 3 (3.1. Long-Horizon Force Awareness via Prompting), objective p. 3 (3. ForceVLA2 Framework), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 3 (3.1. Long-Horizon Force Awareness via Prompting).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, these models remain confined to virtual domains, lacking the embodiment necessary for authentic physical understanding and interaction in real-world settings. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, as shown in Fig. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive tasks such as object search, ... (p. 7, 5.2. Main Experiment Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
