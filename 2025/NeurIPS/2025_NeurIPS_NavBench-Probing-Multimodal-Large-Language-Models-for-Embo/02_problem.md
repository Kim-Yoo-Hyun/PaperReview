# Problem - NavBench: Probing Multimodal Large Language Models for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nf8PKQKtl2; PDF retrieval source: https://arxiv.org/pdf/2506.01031. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): However, most existing benchmarks treat all navigation episodes equally difficult, failing to capture this essential variation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Multimodal Large Language Models (MLLMs) have demonstrated strong generalization in vision-language tasks, yet their ability to understand and act within embodied environments remains underexplored.
- **p. 1 / Abstract - extractive body cue:** We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings.
- **p. 1 / Abstract - extractive body cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...
- **p. 1 / Abstract - extractive body cue:** To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.
- **p. 1 / Abstract - extractive body cue:** We evaluate both proprietary and open-source models, finding that GPT-4o performs well across tasks, while lighter open-source models succeed in simpler cases.
- **p. 2 / 1 Introduction - extractive body cue:** However, most existing benchmarks treat all navigation episodes equally difficult, failing to capture this essential variation.
- **p. 2 / 1 Introduction - extractive body cue:** This allows detailed analysis of models' generalization and decision-making performance across varying levels of difficulty.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, most existing benchmarks treat all navigation episodes equally difficult, failing to capture this essential variation. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | NavBench, consists, components, navigation, comprehension, assessed, through, three, cognitively, grounded | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Formally, step, navigation, episode, MLLM, receives, instruction, wLu | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: NavBench, consists, components, navigation, comprehension, assessed, through, three, cognitively, grounded | p. 1 (Abstract), p. 4 (C Progress Level), p. 5 (C Progress Level) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, main, contributions, follows, introduce, NavBench, benchmark, evaluating | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: ensure, data, quality, minimize, ambiguity, filter, examples, curated | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) |
| Success / guarantee | goal reach with collision-free execution | p. 8 (C Progress Level), p. 9 (5.3 Discussion), p. 9 (C Progress Level) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** This allows detailed analysis of models' generalization and decision-making performance across varying levels of difficulty.
- **p. 3 / 1 Introduction - extractive body cue:** (2) We decompose the evaluation into two components: Navigation Comprehension, with tasks targeting spatial, temporal, and local reasoning, and Navigation Execution, which assesses decision-making across ...
- **p. 3 / 1 Introduction - extractive body cue:** Furthermore, our results suggest several notable trends: (1) comprehension and execution abilities appear to be closely related, (2) temporal reasoning may pose a persistent challenge ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)): In summary, our main contributions are as follows: (1) We introduce NavBench, a benchmark for evaluating MLLMs in embodied navigation under zero-shot settings.

- **p. 2 / 1 Introduction - extractive body cue:** To fill these gaps, we introduce NavBench, a benchmark designed to systematically evaluate MLLMs in embodied navigation under zero-shot settings.
- **p. 3 / 1 Introduction - extractive body cue:** pipeline includes a waypoint selection module, an MLLM-based navigator, and a low-level controller, demonstrating the deployability of our framework in physical environments.
- **p. 1 / Abstract - extractive body cue:** To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions.
- **p. 1 / Abstract - extractive body cue:** NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Error Analysis We manually analyze 100 failed cases to understand model failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The models' failure in this setting highlights their limited ability to reason about temporal order within complex instructions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | All physical experiments are conducted in a controlled indoor lab to assess robustness and feasibility. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 4 (C Progress Level), p. 5 (C Progress Level), p. 8 (C Progress Level). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 1 (Abstract), p. 4 (C Progress Level), p. 5 (C Progress Level), p. 8 (C Progress Level), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
