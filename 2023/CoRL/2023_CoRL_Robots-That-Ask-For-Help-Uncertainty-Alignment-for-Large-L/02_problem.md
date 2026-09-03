# Problem - Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.01928; PDF retrieval source: https://arxiv.org/pdf/2307.01928. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and untethered from reality.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large language models (LLMs) exhibit a wide range of promising capabilities - from step-by-step planning to commonsense reasoning - that may provide utility for robots, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they ...
- **p. 1 / Abstract - extractive body cue:** KNOWNO builds on the theory of conformal prediction to provide statistical guarantees on task completion while minimizing human help in complex multi-step planning settings.
- **p. 1 / Abstract - extractive body cue:** Experiments across a variety of simulated and real robot setups that involve tasks with different modes of ambiguity (e.g., from spatial to numeric uncertainties, from ...
- **p. 1 / Abstract - extractive body cue:** KNOWNO can be used with LLMs out of the box without modelfinetuning, and suggests a promising lightweight approach to modeling uncertainty that can complement and ...
- **p. 1 / 1 Introduction - extractive body cue:** However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and ...
- **p. 5 / 1 Introduction - extractive body cue:** However, the original CP formulation cannot be applied here since the context xt between steps are dependent; moreover, the robot's actions at step t influence ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | environment, formulated, partially, observable, Markov, decision, process, POMDP, given, state | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | formalize, considering, joint, distribution, over, scenarios, where, environment | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: environment, formulated, partially, observable, Markov, decision, process, POMDP, given, state | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Here, present, novel, extension, multi-step, settings, tackles, challenge | p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: eliminates, plans, LLM, considers, unlikely, reduces, problem, next-step | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / 1 Introduction - extractive body cue:** However, the original CP formulation cannot be applied here since the context xt between steps are dependent; moreover, the robot's actions at step t influence ...
- **p. 1 / 1 Introduction - extractive body cue:** Accurately modeling and accounting for uncertainty is a longstanding challenge towards robots that operate reliably in unstructured and novel environments.
- **p. 2 / 1 Introduction - extractive body cue:** We formalize these challenges via two desiderata: (i) calibrated confidence: the robot should seek sufficient help to ensure a statistically guaranteed level of task success ...
- **p. 4 / 1 Introduction - extractive body cue:** Overall, CP is a powerful and easy-to-use statistical tool to produce (1) tight coverage guarantees-addressing the goal of calibrated confidence, and (2) small prediction sets ...

## What the Paper Changes

PDF body contribution framing (p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction)): Here, we present a novel extension of CP to multi-step settings that tackles this challenge.

- **p. 2 / 1 Introduction - extractive body cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 4 / 1 Introduction - extractive body cue:** We introduce CP below, and then present the different practical settings we consider (possibly involving multiple planning steps and/or multiple correct plans per step).
- **p. 5 / 1 Introduction - extractive body cue:** Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where T is the ...
- **p. 6 / 1 Introduction - extractive body cue:** We extend our method and confidence guarantees to this setting for both single- and multi-step problems in Section A3 and Section A4.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | First, we investigate whether KNOWNO and the baselines achieve a given target task success rate consistently in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Note that the ϵ level is not used in Prompt Set or Binary, and so the user cannot ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), interface p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), objective p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
