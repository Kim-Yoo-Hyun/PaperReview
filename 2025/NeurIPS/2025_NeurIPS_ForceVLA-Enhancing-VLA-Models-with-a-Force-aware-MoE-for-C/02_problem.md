# Problem - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=2845H8Ua5D; PDF retrieval source: https://arxiv.org/pdf/2505.22159. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction)): However, these methods largely omit explicit modeling of the force/tactile modalities, and lack mechanisms for dynamically routing across multimodal signals in contact-intensive tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations.
- **p. 1 / Abstract - extractive body cue:** However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems.
- **p. 1 / Abstract - extractive body cue:** ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding.
- **p. 1 / Abstract - extractive body cue:** This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics.
- **p. 3 / 1 Introduction - extractive body cue:** However, these methods largely omit explicit modeling of the force/tactile modalities, and lack mechanisms for dynamically routing across multimodal signals in contact-intensive tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Current methods lack mechanisms to perceive and adapt to these dynamic variations, limiting their ability to reason over time about physical interactions.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these methods largely omit explicit modeling of the force/tactile modalities, and lack mechanisms for dynamically routing across multimodal signals in contact-intensive ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | Given a language instruction L, the objective is to learn an end-to-end policy π(At/Ot, L) that outputs low-level, executable action chunk At ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, language, instruction, objective, learn, end-to-end, policy, At/Ot, outputs, low-level | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | adaptively, activating, experts, high-level, task, instructions, low-level, interaction | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Given, language, instruction, objective, learn, end-to-end, policy, At/Ot, outputs, low-level | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | contact-aware action/force; body terms: main, contributions, present, novel, framework, integrates, force, vision | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | contact prediction/control error; cue terms: Given, language, instruction, objective, learn, end-to-end, policy, At/Ot | p. 3 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction) |
| Success / guarantee | slip/contact success and safe interaction | p. 6 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Current methods lack mechanisms to perceive and adapt to these dynamic variations, limiting their ability to reason over time about physical interactions.
- **p. 3 / 1 Introduction - extractive body cue:** Multimodal fusion methods [38, 39] show promise in complex environments, though current approaches are often limited to static modality fusion and lack dynamic routing or ...
- **p. 5 / 1 Introduction - extractive body cue:** Existing datasets often lack the comprehensive force interactions or the diversity of contact-driven scenarios necessary to develop robust force-aware policies.
- **p. 2 / 1 Introduction - extractive body cue:** Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 3 (1 Introduction)): Our main contributions are: • We present a novel framework that integrates force, vision, language, and action for improved precision and stability on contact-rich manipulation tasks.

- **p. 2 / 1 Introduction - extractive body cue:** Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during action ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems.
- **p. 3 / 1 Introduction - extractive body cue:** The robot's observation at timestep t consists of base and hand visual inputs V b t and V h t , the proprioceptive state st ...
- **p. 3 / 1 Introduction - extractive body cue:** TCP position is represented by Cartesian coordinates (x, y, z) and orientation is represented by Euler angles (α, β, γ). ft is the estimated external ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 1: Comparison between ForceVLA and baselines without force input. Without force feedback, the policy fails to correct ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Figure 7: Trajectory visualizations across tasks and conditions. (a) USB insertion, (b) bottle pumping, and (c) plug insertion ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Visual Occlusion Unstable Socket Average π0-base[10] w/o F 48.00% 10.00% 66.67% 60.00% 10.00% 38.93% π0-base[10] w/ F 32.00% ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), interface p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), objective p. 3 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
