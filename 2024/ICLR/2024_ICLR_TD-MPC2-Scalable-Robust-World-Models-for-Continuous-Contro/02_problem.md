# Problem - TD-MPC2: Scalable, Robust World Models for Continuous Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.16828; PDF retrieval source: https://arxiv.org/pdf/2310.16828. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate that TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single ...
- **p. 1 / ABSTRACT - extractive body cue:** We further show that agent capabilities increase with model and data size, and successfully train a single 317M parameter agent to perform 80 tasks across ...
- **p. 1 / ABSTRACT - extractive body cue:** We conclude with an account of lessons, opportunities, and risks associated with large TD-MPC2 agents.
- **p. 3 / 2 BACKGROUND - extractive body cue:** However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** However, in the general case where domain knowledge cannot be assumed, we may instead choose to learn the task embeddings (and, implicitly, task relations) from ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Tasks, include, high-dimensional, state, action, spaces, R39, image | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent | p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION) |
| Decision / output variable | filtered/recovery action u_safe; body terms: present, TDMPC2, significant, step, towards, achieving, goal, algorithmic | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: components, jointly, optimized, minimize, objective, Joint-embedding, prediction, Reward | p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 7 (4.1 RESULTS), p. 5 (Figure/Table caption), p. 6 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / 2 BACKGROUND - extractive body cue:** However, in the general case where domain knowledge cannot be assumed, we may instead choose to learn the task embeddings (and, implicitly, task relations) from ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** However, learning a large generalist TD-MPC2 agent that performs a variety of tasks across multiple task domains, embodiments, and action spaces poses several unique challenges: ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We argue that current approaches to generalist embodied agents suffer from (a) the assumption of near-expert trajectories for behavior cloning which severely limits the amount ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** An algorithm that can consume large multitask datasets will invariably need to be robust to variation between different tasks (e.g., action space dimensionality, difficulty of ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND)): In this work, we present TDMPC2: a significant step towards achieving this goal.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: (1) improved algorithmic robustness by revisiting core design choices, and (2) careful ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 3 / 2 BACKGROUND - extractive body cue:** We introduce the TD-MPC2 algorithm in the following, and provide a full list of algorithmic improvements in Appendix A.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Specifically, we propose a series of improvements to the TD-MPC algorithm, which have been key to achieving strong algorithmic robustness (can use the same hyperparameters ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Notably, performance does not appear to have saturated for our largest models (317M parameters) on either dataset, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 2. Tasks. TD-MPC2 performs 104 diverse tasks from (left to right) DMControl (Tassa et al., 2018), Meta-World ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND), objective p. 4 (2 BACKGROUND), p. 4 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., ... (p. 3, 2 BACKGROUND).
- **Formulation-changing contribution:** In this work, we present TDMPC2: a significant step towards achieving this goal. (p. 2, 1 INTRODUCTION).
- **Assumption/failure evidence:** While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes (Clark & Amodei, 2016) that may ... (p. 9, 4.1 RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
