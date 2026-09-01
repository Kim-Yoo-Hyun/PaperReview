# Problem - Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007319; PDF retrieval source: https://openreview.net/pdf?id=pZuZWRuPyi. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES)): 1 (b), where standard RSSM-based baselines (APV and ContextWM), even when equipped with ensemble heads, exhibit artificially low and nearly flat predictive uncertainty that fails to grow with the prediction ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Pre-training world models on large, action-free video datasets offers a promising path toward generalist agents, but a fundamental flaw undermines this paradigm.
- **p. 1 / ABSTRACT - extractive PDF cue:** Prevailing methods train models to predict a single, deterministic future, an objective that is ill-posed for inherently stochastic environments where actions are unknown.
- **p. 1 / ABSTRACT - extractive PDF cue:** We contend that a world model should instead learn a structured, probabilistic representation of the future where predictive uncertainty correctly scales with the temporal horizon.
- **p. 1 / ABSTRACT - extractive PDF cue:** To achieve this, we introduce a pre-training framework, Horizon-cAlibrated Uncertainty World Model (HAUWM), built on a probabilistic ensemble that predicts frames at randomly sampled future ...
- **p. 1 / ABSTRACT - extractive PDF cue:** The core of our method is a Horizon-Calibrated Uncertainty (HCU) loss, which explicitly shapes the latent space by encouraging predictive variance to grow as the ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 1 (b), where standard RSSM-based baselines (APV and ContextWM), even when equipped with ensemble heads, exhibit artificially low and nearly flat predictive uncertainty that fails ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, a critical flaw undermines current approaches.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 1 (b), where standard RSSM-based baselines (APV and ContextWM), even when equipped with ensemble heads, exhibit artificially low and nearly flat predictive ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | Formally, each ensemble head outputs the Gaussian parameters for the future latent state: p(i) θ (st+k / st, ∆te k) = N ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | Formally, ensemble, head, outputs, Gaussian, parameters, future, latent, state, ensure | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | However, video, data, inherently, lacks, explicit, action, labels | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: Formally, ensemble, head, outputs, Gaussian, parameters, future, latent, state, ensure | p. 5 (4 METHODOLOGY), p. 4 (3 PRELIMINARIES), p. 5 (4 METHODOLOGY) |
| Decision / output variable | filtered/recovery action u_safe; body terms: novel, framework, variable-horizon, prediction, introduce, Horizon-Calibrated, Uncertainty, HCU | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (4 METHODOLOGY) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: dynamically, balance, predictive, accuracy, against, uncertainty, representation, formulate | p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4 METHODOLOGY), p. 6 (4 METHODOLOGY), p. 7 (4 METHODOLOGY) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 10 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, a critical flaw undermines current approaches.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We identify and analyze the key limitation of deterministic prediction in action-free world model pre-training: it suppresses environmental stochasticity rather than representing it.
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** A key challenge is to integrate this new information without overwriting the valuable priors learned during pre-training.
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** This model is typically a variant of a latent dynamics model, such as a Recurrent State-Space Model (RSSM) (Hafner et al., 2019), which learns to ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY)): We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty explicitly.

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Instead of single-step prediction, our method trains a probabilistic ensemble to forecast states across variable, randomly sampled time horizons.
- **p. 4 / 4 METHODOLOGY - extractive PDF cue:** Our methodology is structured around a two-phase framework as shown in fig.
- **p. 5 / 4 METHODOLOGY - extractive PDF cue:** To explicitly preserve future-state diversity, we introduce a Horizon-Calibrated Uncertainty (HCU) loss.
- **p. 5 / 4 METHODOLOGY - extractive PDF cue:** In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over randomly sampled time ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | To maintain compatibility with this stream's original design, we condition it on relative temporal embeddings ∆te k=1 (as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This led to significant performance degradation, particularly on the DMC benchmark, confirming that explicitly modeling structured temporal uncertainty ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Robustness (RQ4): Can our pre-training world model generalize to diverse downstream learning paradigms? | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We attribute this strong performance to our core contribution: by pre-training a model that explicitly represents temporal uncertainty, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (4 METHODOLOGY), p. 4 (3 PRELIMINARIES), p. 5 (4 METHODOLOGY), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), interface p. 5 (4 METHODOLOGY), p. 4 (3 PRELIMINARIES), p. 5 (4 METHODOLOGY), p. 1 (1 INTRODUCTION), objective p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
