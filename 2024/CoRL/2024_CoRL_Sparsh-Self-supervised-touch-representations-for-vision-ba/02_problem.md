# Problem - Sparsh: Self-supervised touch representations for vision-based tactile sensing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.24090; PDF retrieval source: https://arxiv.org/pdf/2410.24090. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.
- **p. 1 / Abstract - extractive body cue:** Such sensors have led to many recent advances in robot manipulation as they markedly complement vision, yet solutions today often rely on task and sensor ...
- **p. 1 / Abstract - extractive body cue:** Collecting real data at scale with task centric ground truth labels, like contact forces and slip, is a challenge further compounded by sensors of various ...
- **p. 1 / Abstract - extractive body cue:** To tackle this we turn to self-supervised learning (SSL) that has demonstrated remarkable performance in computer vision.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 2 / 1 Introduction - extractive body cue:** Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.
- **p. 2 / 1 Introduction - extractive body cue:** Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | Vision-based tactile sensors [1, 2, 3, 4] have emerged as the leading form factor capable of capturing images of physical interactions at ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Vision-based, tactile, sensors, have, emerged, leading, form, factor, capable, capturing | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | prevailing, incorporating, vision-based, tactile, sensors, robot, tasks, train | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Vision-based, tactile, sensors, have, emerged, leading, form, factor, capable, capturing | p. 2 (1 Introduction), p. 8 (8 Discussion), p. 2 (1 Introduction) |
| Decision / output variable | contact-aware action/force; body terms: introduce, family, touch, representations, vision-based, tactile, sensors, trained | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | contact prediction/control error; cue terms: Specifically, provide, recipe, adapt, masking-based, objectives, computer, vision | p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 8 (8 Discussion) |
| Success / guarantee | slip/contact success and safe interaction | p. 28 (Figure/Table caption), p. 24 (Figure/Table caption), p. 24 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 8 (8 Discussion)): In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 8 / 8 Discussion - extractive body cue:** We evaluated five SSL approaches (see Figure 2) comparing their performance against task and sensor specific models through TacBench, a benchmark of six touch-centric tasks ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 25 | Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 24 | Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 28 | Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Both models perform similarly in bead maze test demonstrations, which require implicit knowledge of shear forces and slip. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 8 (8 Discussion), p. 2 (1 Introduction), p. 8 (8 Discussion). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 2 (1 Introduction), p. 8 (8 Discussion), p. 2 (1 Introduction), p. 8 (8 Discussion), objective p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, this did not translate to real robot performance due to lack of force control and system-level confounding variables not captured during training. (p. 8, 8 Discussion).
- **Formulation-changing contribution:** Our contributions are as follows: 1. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** In Figure 13, we illustrate a failure case for Sparsh (VJEPA), as its results do not align with the ground truth. (p. 24, Model).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
