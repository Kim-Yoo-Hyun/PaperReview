# Problem - FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): However, robot control has stricter real-time requirements than text generation: extra inference computation can introduce delays, causing jitter or even task failure.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans naturally allocate more time before acting when handling complex tasks in the physical world.
- **p. 1 / Abstract - extractive body cue:** This paradigm has recently led to remarkable advances in boosting Large Language Models (LLMs) on complex tasks in digital domains.
- **p. 1 / Abstract - extractive body cue:** However, the potential of test-time computing remains largely unexplored for robotic foundation models that interact with the physical world.
- **p. 1 / Abstract - extractive body cue:** FM-Steer first introduces an intermediate flow verifier to estimate state-action values for candidate actions.
- **p. 1 / Abstract - extractive body cue:** At test time, the policy iteratively samples multiple noisy action proposals and retains the one with the highest predicted value, yielding value-aligned, high-quality actions without ...
- **p. 2 / 1. Introduction - extractive body cue:** However, robot control has stricter real-time requirements than text generation: extra inference computation can introduce delays, causing jitter or even task failure.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce FM-Steer, a framework that enhances flow-based VLA models at test time with value-guided test-time sampling and cascaded action denoising.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, robot control has stricter real-time requirements than text generation: extra inference computation can introduce delays, causing jitter or even task failure. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | flow-based, VLA, aims, model, data, distribution, At/ot, mapping, observation, consists | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | intermediate, flow, verifier, estimates, state-action, value, candidate, point | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: flow-based, VLA, aims, model, data, distribution, At/ot, mapping, observation, consists | p. 3 (3. Preliminaries), p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling) |
| Decision / output variable | filtered/recovery action u_safe; body terms: summary, main, contributions, FM-Steer, test-time, computing, framework, enhances | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: Due, multiple, Euler, forward, iterations, required, flow-based, VLA | p. 3 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.1. Value-Guided Test-Time Sampling) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.3. Training and Deployment Strategy), p. 7 (5.3. Efficiency Improvement), p. 3 (4.1. Value-Guided Test-Time Sampling) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce FM-Steer, a framework that enhances flow-based VLA models at test time with value-guided test-time sampling and cascaded action denoising.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 6 (Model)): In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving the robot control frequency. • We ...

- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** The model typically consists of a VLM backbone and a flow matching expert.
- **p. 3 / 3. Preliminaries - extractive body cue:** A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, and robot state ...
- **p. 6 / Model - extractive body cue:** We present the success rate (SR) and standard error for each method across four task suites.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | FM-Steer combines valueguided test-time sampling with effective best-of-N selection and cascaded action denoising, integrating the original VLA with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Preliminaries), p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3. Preliminaries), p. 4 (4.2. Cascaded Action Denoising), p. 4 (4.1. Value-Guided Test-Time Sampling), p. 2 (1. Introduction), objective p. 3 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.1. Value-Guided Test-Time Sampling).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
