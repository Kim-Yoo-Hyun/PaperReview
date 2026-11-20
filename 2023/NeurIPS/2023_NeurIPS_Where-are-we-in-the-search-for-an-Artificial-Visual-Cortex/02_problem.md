# Problem - Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.18240; PDF retrieval source: https://arxiv.org/abs/2303.18240. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls for innovations in architecture, learning ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present the largest and most comprehensive empirical study of pre-trained visual representations (PVRs) or visual ‘foundation models' for Embodied AI.
- **p. 1 / Abstract - extractive body cue:** First, we curate CORTEXBENCH, consisting of 17 different tasks spanning locomotion, navigation, dexterous, and mobile manipulation.
- **p. 1 / Abstract - extractive body cue:** Next, we systematically evaluate existing PVRs and find that none are universally dominant.
- **p. 1 / Abstract - extractive body cue:** To study the effect of pre-training data size and diversity, we combine over 4,000 hours of egocentric videos from 7 different sources (over 4.3M images) ...
- **p. 1 / Abstract - extractive body cue:** Contrary to inferences from prior work, we find that scaling dataset size and diversity does not improve performance universally (but does so on average).
- **p. 3 / 1 Introduction - extractive body cue:** Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls ...
- **p. 1 / 1 Introduction - extractive body cue:** Unfortunately, prior studies are incommensurable - using different self-supervised learning (SSL) algorithms on different pre-training datasets, designed

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | Reach-Cube, state, policy, where, current, fingertip, position, latent, visual, vector | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Push-Cube, state, policy, where, goal, position, cube, specified | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Reach-Cube, state, policy, where, current, fingertip, position, latent, visual, vector | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 1 (1 Introduction), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Decision / output variable | method trajectory/action; body terms: visual, cortex, region, organism, brain, together, motor, enables | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: train, agents, reward, functions, presented, utilizing, following, settings | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Success / guarantee | comparable score and protocol validity | p. 4 (Results), p. 8 (Results), p. 2 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Unfortunately, prior studies are incommensurable - using different self-supervised learning (SSL) algorithms on different pre-training datasets, designed
- **p. 2 / 1 Introduction - extractive body cue:** We are simply motivated by the broad generalization capabilities of a biological visual cortex.
- **p. 2 / 1 Introduction - extractive body cue:** Our largest model trained on all data, named VC-1, outperforms the best existing PVR by 1.2% on average.
- **p. 3 / 1 Introduction - extractive body cue:** In this real-world setting, we find that VC-1 and VC-1 (adapted) substantially outperform pre-existing PVRs like MVP [8].

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH)): The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement.

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we ask the same question that Fukushima [1, 2] asked nearly 50 years ago - how do we design an artificial visual ...
- **p. 2 / 1 Introduction - extractive body cue:** The exhaustiveness of this study enables us to draw conclusions with unprecedented scope and confidence.
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We present an evaluation of object navigation (ObjectNav) using the HM3D-SEM dataset [61].
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** The dataset was collected using Habitat-Web [61, 71] and Amazon Mechanical Turk, and consists of 77k demonstrations for 80 scenes from the HM3D-SEM dataset [69].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | This study presents a thorough examination of visual foundation models but has several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Additionally, we include randomly initialized ViTs with frozen- and finetuned weights to assess the necessity of pre-training and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | While this adaptation strategy cannot address task-specialization, it may serve to mitigate domain gap. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 1 (1 Introduction), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 1 (1 Introduction), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), objective p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Our findings reveal a challenge and opportunity for the community - the search for a PVR that is universally dominant (or "foundational") for EAI calls for innovations in architecture, learning ... (p. 3, 1 Introduction).
- **Formulation-changing contribution:** The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement. (p. 1, 1 Introduction).
- **Assumption/failure evidence:** In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains or where E2E fine-tuning fails. (p. 9, Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
