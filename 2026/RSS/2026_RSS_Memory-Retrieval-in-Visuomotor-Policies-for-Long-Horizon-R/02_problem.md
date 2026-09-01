# Problem - Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/10/; PDF retrieval source: https://roboticsconference.org/program/papers/10/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, directly applying attention-based memory retrieval to long-horizon robotic imitation learning via offline data exposes two fundamental challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** General-purpose robots operating in partially observable environments, such as homes, require memory to support autonomy.
- **p. 1 / Abstract - extractive body cue:** They must recall diverse information from the past, such as where objects were placed, which tasks a human partner has completed, and when an appliance ...
- **p. 1 / Abstract - extractive body cue:** Achieving this versatility requires a memory retrieval mechanism that generalizes well across tasks.
- **p. 1 / Abstract - extractive body cue:** However, hand-designed or heuristicbased methods rely on task-specific assumptions that may not transfer to different settings.
- **p. 1 / Abstract - extractive body cue:** Transformer architectures that use attention over long contexts for memory retrieval provide a promising alternative, as they learn retrieval from data without task-specific assumptions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying attention-based memory retrieval to long-horizon robotic imitation learning via offline data exposes two fundamental challenges.
- **p. 2 / I. INTRODUCTION - extractive body cue:** HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, directly applying attention-based memory retrieval to long-horizon robotic imitation learning via offline data exposes two fundamental challenges. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | We parameterize the visuomotor policy πθ(at / τt, l) with three main components: (i) modality-specific encoders consisting of an observation encoder gobs ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | parameterize, visuomotor, policy, three, main, components, modality-specific, encoders, consisting, observation | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | HALO, learns, visuomotor, policy, retrieves, information, past, observations | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: parameterize, visuomotor, policy, three, main, components, modality-specific, encoders, consisting, observation | p. 3 (III. HALO), p. 3 (III. HALO), p. 4 (III. HALO) |
| Decision / output variable | filtered/recovery action u_safe; body terms: address, challenges, HALO, HistoryAware, visuomotor, policy, LOng-horizon, robotic | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: VQA, objective, biases, memory, retrieval, towards, task-relevant, information | p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 4 (III. HALO), p. 4 (III. HALO), p. 5 (III. HALO), p. 5 (III. HALO) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (III. HALO), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from vision-language foundation models. observations can amplify this effect, as ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Long-horizon household tasks require robots to act on information no longer present in the current sensory input.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION)): To address these challenges, we propose HALO: HistoryAware visuomotor policy for LOng-horizon robotic imitation learning.

- **p. 2 / I. INTRODUCTION - extractive body cue:** Across these settings, we show that VQA-induced task priors provide a general solution, improving absolute task success by 7% on average across diverse tasks and ...
- **p. 1 / Abstract - extractive body cue:** To address both challenges, we introduce HALO, a visuomotor policy with an attention-based memory retrieval mechanism for long-horizon control.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of a general memory retrieval mechanism that can be learned end-to-end, rather than tailored to individual tasks or modalities [6]-[9].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Fig. 2. HALO learns to retrieve diverse forms of task-relevant information from history, guided by priors distilled from ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These results support our hypothesis that HALO reduces model drift (fewer manipulation failures) | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | In addition, we measure manipulation and memory failures in real-world evaluations, finding that HALO reduces them by 8% ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Method Retrieve Object Return to Container LSTM 0.14 0.12 Mamba 0.20 0.18 TransformerXL 0.12 0.20 Window Attention 0.13 ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. HALO), p. 3 (III. HALO), p. 4 (III. HALO), p. 4 (III. HALO). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. HALO), p. 3 (III. HALO), p. 4 (III. HALO), p. 4 (III. HALO), objective p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 4 (III. HALO), p. 4 (III. HALO), p. 5 (III. HALO), p. 5 (III. HALO).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
