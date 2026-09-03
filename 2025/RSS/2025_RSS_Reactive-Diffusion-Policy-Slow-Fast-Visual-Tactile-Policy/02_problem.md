# Problem - Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p052.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p052.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. Ivrropucrion), p. 3 (B. Robot Data Collection System), p. 4 (A. 3D Deformation Field Extraction), p. 1 (Abstract), p. 1 (Abstract)): In order to compensate for the limitations of purely visual input, numerous approaches [40 27, 45, 64, 31] have explored the integration of tactile input into imitation learning policies However, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans can accomplish complex contact-rich tasks using vision and touch, with highly rea r fast response (o external changes and adaptive control of contact forces: ...
- **p. 1 / Abstract - extractive body cue:** Ex ‘visual imitation learning (IL) approaches rly on aetion chunking ‘model complex behaviors, which lacks the ability to respond instantly to real-time tactile feedback during ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, most teleoperation systems. sirugsle to provide fine-grained tactile / force feedback, which limits the range of tasks that can be performed.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce TactAR, 4 low-cost tleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy ...
- **p. 1 / Abstract - extractive body cue:** RDP employs a two-level hierarchy: (1) a slow latent diffusion policy for predicting high-level ation chunks in latent space at low frequency, (2) a fast ...
- **p. 2 / I. Ivrropucrion - extractive body cue:** In order to compensate for the limitations of purely visual input, numerous approaches [40 27, 45, 64, 31] have explored the integration of tactile input ...
- **p. 3 / B. Robot Data Collection System - extractive body cue:** By integrating both tactile and visual modalities, our approach overcomes the limitations of prior works and achieves greater versatility in robotic manipulation,

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In order to compensate for the limitations of purely visual input, numerous approaches [40 27, 45, 64, 31] have explored the integration ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | ForceMimiec [1] adds a force sensor on a handheld device [11] to get force feedback, but suffers from the inaccuracy of pose ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | ForceMimiec, adds, force, sensor, handheld, device, feedback, suffers, inaccuracy, pose | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | action, chunk, policy, leaming, Dpotiey, encoder, downsamples, latent | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: ForceMimiec, adds, force, sensor, handheld, device, feedback, suffers, inaccuracy, pose | p. 3 (B. Robot Data Collection System), p. 1 (Body text (section boundary not confidently recovered)), p. 6 (B. Slow-Fast Policy Learning) |
| Decision / output variable | contact-aware action/force; body terms: address, challenges, introduce, TactAR, low-cost, tleoperation, system, provides | p. 1 (Abstract), p. 2 (I. Ivrropucrion), p. 2 (I. Ivrropucrion) |
| Objective / loss / cost | contact prediction/control error; cue terms: During, training, given, observation, including, image, tactlity, propri- | p. 6 (B. Slow-Fast Policy Learning), p. 6 (B. Slow-Fast Policy Learning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (A. 3D Deformation Field Extraction), p. 5 (A. 3D Deformation Field Extraction), p. 6 (B. Slow-Fast Policy Learning) |
| Success / guarantee | slip/contact success and safe interaction | p. 9 (B. Results), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / B. Robot Data Collection System - extractive body cue:** By integrating both tactile and visual modalities, our approach overcomes the limitations of prior works and achieves greater versatility in robotic manipulation,
- **p. 4 / A. 3D Deformation Field Extraction - extractive body cue:** Compared to other haptic teleoperation, systems based on isomorphic hardware{32, 9], our system only needs one Meta Quest3 VR headset, which greatly reduces the reproducibility ...
- **p. 1 / Abstract - extractive body cue:** Ex ‘visual imitation learning (IL) approaches rly on aetion chunking ‘model complex behaviors, which lacks the ability to respond instantly to real-time tactile feedback during ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we introduce TactAR, 4 low-cost tleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 2 (I. Ivrropucrion), p. 2 (I. Ivrropucrion), p. 3 (B. Robot Data Collection System), p. 3 (B. Robot Data Collection System)): To address these challenges, we introduce TactAR, 4 low-cost tleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy (RDP), a novel slow-fast visuale ...

- **p. 2 / I. Ivrropucrion - extractive body cue:** In this work, we propose two critical components to solve the above issues of visual-tactile imitation learning:
- **p. 2 / I. Ivrropucrion - extractive body cue:** To leverage the high-quality visual tactile data collected by the TactAR system, we propose an imitation learning algorithm called Reactive Diffusion Policy (RDP) (Fig. / ...
- **p. 3 / B. Robot Data Collection System - extractive body cue:** ‘In contrast, our method combines normal force, shear force, and visual RGB inputs into a unified visual-tactile policy, enabling deployment across a broader range of ...
- **p. 3 / B. Robot Data Collection System - extractive body cue:** Our method ‘combines the advantages of low-cost VR controller and tactile sensing, getting tactile feedback via Augmented Reality, while preserving the accuracy needed for precise ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | It may get stuck when making contact with the object (e.2., failure case 2 in Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | However, despite similar performance, these two DP baselines exhibit different failure modes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | 8: Evaluation results and failure cases of baselines. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | V that when the action chunk size is reduced from 8 to 2, the DP baseline tends to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (B. Robot Data Collection System), p. 1 (Body text (section boundary not confidently recovered)), p. 6 (B. Slow-Fast Policy Learning), p. 2 (I. Ivrropucrion). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. Ivrropucrion), p. 3 (B. Robot Data Collection System), p. 4 (A. 3D Deformation Field Extraction), p. 1 (Abstract), p. 1 (Abstract), interface p. 3 (B. Robot Data Collection System), p. 1 (Body text (section boundary not confidently recovered)), p. 6 (B. Slow-Fast Policy Learning), p. 2 (I. Ivrropucrion), objective p. 6 (B. Slow-Fast Policy Learning), p. 6 (B. Slow-Fast Policy Learning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In order to compensate for the limitations of purely visual input, numerous approaches [40 27, 45, 64, 31] have explored the integration of tactile input into imitation learning policies However, ... (p. 2, I. Ivrropucrion).
- **Formulation-changing contribution:** To address these challenges, we introduce TactAR, 4 low-cost tleoperation system that provides real-time tactile feedback through Augmented Reality (AR), along with Reactive Diffusion Policy (RDP), a novel slow-fast visuale ... (p. 1, Abstract).
- **Assumption/failure evidence:** We ‘observe that DP with pure visual input frequently predicts inaccurate trajectories and results in large contact forces (e.g. failure case 2 in Fig. (p. 9, B. Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
