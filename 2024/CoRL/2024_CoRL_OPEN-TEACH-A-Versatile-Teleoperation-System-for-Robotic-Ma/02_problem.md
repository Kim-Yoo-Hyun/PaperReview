# Problem - OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/iyer25a.html; PDF retrieval source: https://arxiv.org/pdf/2403.07870. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. BACKGROUND ON IMITATION LEARNING)): The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space.

## PDF Body Digest

- **p. 2 / Abstract - extractive body cue:** Open-sourced, user-friendly tools form the bedrock of scientific advancement across disciplines.
- **p. 2 / Abstract - extractive body cue:** The widespread adoption of data-driven learning has led to remarkable progress in multi-fingered dexterity, bimanual manipulation, and applications ranging from logistics to home robotics.
- **p. 2 / Abstract - extractive body cue:** However, existing data collection platforms are often proprietary, costly, or tailored to specific robotic morphologies.
- **p. 2 / Abstract - extractive body cue:** We present OPEN TEACH, a new teleoperation system leveraging VR headsets to immerse users in mixed reality for intuitive robot control.
- **p. 2 / Abstract - extractive body cue:** Built on the affordable Meta Quest 3, which costs $500, OPEN TEACH enables realtime control of various robots, including multi-fingered hands, bimanual arms, and mobile ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Recently proposed exoskeleton-based teleoperation frameworks like ALOHA [67], GELLO [61], and AirExo [14] attempt to alleviate this problem by having the human teleoperator directly control ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF body |
| State / latent | Behavior, Cloning, Given, dataset, expert, rollouts, desired, task, form, observation | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | underscores, effectiveness, OPEN, TEACH, collecting, data, policy, learning | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: Behavior, Cloning, Given, dataset, expert, rollouts, desired, task, form, observation | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 6 (4) How intuitive is the system for new users?) |
| Decision / output variable | normalized sample or downstream action; body terms: contributions, summarized, follows, present, OPEN, TEACH, open-source, system | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Following, convention, objective, find, value, maximizes, probability, observed | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 2 (I. INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 5 (IV. OPEN TEACH), p. 6 (4) How intuitive is the system for new users?) |
| Success / guarantee | cross-domain transfer and task performance | p. 8 (4) How intuitive is the system for new users?), p. 8 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** Recently proposed exoskeleton-based teleoperation frameworks like ALOHA [67], GELLO [61], and AirExo [14] attempt to alleviate this problem by having the human teleoperator directly control ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Following this convention, the objective of BC is to find the value θ that maximizes the probability of the observed data. θ∗= argmax θ Y ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Body text (section boundary not confidently recovered)), p. 4 (IV. OPEN TEACH), p. 4 (IV. OPEN TEACH)): The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we present OPEN TEACH, an open-source framework for robot teleoperation that supports a variety of robots, including bimanual and multi-finger manipulation, all ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We present OPEN TEACH, a unified robot teleoperation framework that supports multiple arms and hands, allows mobile manipulation, is calibration-free, and works across both ...
- **p. 4 / IV. OPEN TEACH - extractive body cue:** In this section, we provide details about the VR-based teleoperation setup and the system design that enables data collection using this framework.
- **p. 4 / IV. OPEN TEACH - extractive body cue:** We observe that OPEN TEACH is the only framework that enables controlling multiple arms, hands, and mobile manipulators, is calibration-free, and is completely open-source.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. BACKGROUND ON IMITATION LEARNING), interface p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?), objective p. 3 (III. BACKGROUND ON IMITATION LEARNING), p. 2 (I. INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space. (p. 2, I. INTRODUCTION).
- **Formulation-changing contribution:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset. (p. 8, VI. LIMITATIONS AND DISCUSSION).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
