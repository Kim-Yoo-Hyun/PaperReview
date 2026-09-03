# Problem - GOAT: GO to Any Thing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p073.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): In deployment scenarios such as homes and warehouses, mobile robots are expected to autonomously navigate for extended periods, seamlessly executing tasks articulated in terms that are intuitively understandable by human ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In deployment scenarios such as homes and warehouses, mobile robots are expected to autonomously navigate for extended periods, seamlessly executing tasks articulated in terms that ...
- **p. 1 / Abstract - extractive body cue:** We present GO To Any Thing (GOAT), a universal navigation system capable of tackling these requirements with three key features: a) Multimodal: it can tackle ...
- **p. 1 / Abstract - extractive body cue:** GOAT is made possible through a modular system design and a continually augmented instanceaware semantic memory that keeps track of the appearance of objects from ...
- **p. 1 / Abstract - extractive body cue:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and language descriptions.
- **p. 1 / Abstract - extractive body cue:** In experimental comparisons spanning over 90 hours in 9 different homes consisting of 675 goals selected across 200+ different object instances, we find GOAT achieves ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In deployment scenarios such as homes and warehouses, mobile robots are expected to autonomously navigate for extended periods, seamlessly executing tasks articulated ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | It takes as input the current depth image Dt, RGB image It, and pose reading xt from onboard sensors. | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | takes, input, current, depth, image, RGB, pose, reading, onboard, sensors | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | frontierbased, exploration, selects, closest, unexplored, region, goal, Local | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: takes, input, current, depth, image, RGB, pose, reading, onboard, sensors | p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD) |
| Decision / output variable | base plus arm/gripper action; body terms: enables, GOAT, distinguish, between, different, instances, same, category | p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: take, simple, when, observations, received, sensors, overwrite, relevant | p. 4 (IV. GOAT METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. GOAT METHOD) |
| Success / guarantee | task completion and recovery | p. 5 (V. RESULTS), p. 5 (V. RESULTS), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** We present GO To Any Thing (GOAT), a universal navigation system capable of tackling these requirements with three key features: a) Multimodal: it can tackle ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION)): This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions.

- additional contribution PDF body cue not selected; no claim inferred

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | environment is fully explored, failures are almost exclusively due to failures in matching the correct goal. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | The most common failure is a language goal being matched against the an object of the correct class, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | a) Modularity allows GOAT to Achieve Robust GeneralPurpose Navigation in the Real World: The GOAT system as a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), objective p. 4 (IV. GOAT METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, for extremely long trajectories a mechanism to increase parallelism or cull duplicate images would be necessary to increase matching speeds. g) Additional Limitations: To achieve robust imagematching results GOAT's ... (p. 10, VII. DISCUSSION).
- **Formulation-changing contribution:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** 68.2). d) Real-World Open-Vocabulary Detection: Limitations and Opportunities: An interesting and noteworthy observation is that despite the rapid advances in open (or large) vocabulary vision-and-language models (VLMs) [37, 43], we ... (p. 10, VII. DISCUSSION).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
