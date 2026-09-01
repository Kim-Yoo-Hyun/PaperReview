# Problem - Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p073.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 2 (1. INTRODUCTION)): Detecting failures in robotic manipulation tasks poses several challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent years have witnessed impressive robotic ‘manipulation systems driven by advances
- **p. 1 / Abstract - extractive body cue:** fand generative modeling, such as approaches.
- **p. 1 / Abstract - extractive body cue:** As robot policy performance increases, so does the complexity and time horizon of achievable tasks,
- **p. 1 / Abstract - extractive body cue:** ing unexpected and diverse failure modes that are difficult to predict a priori.
- **p. 1 / Abstract - extractive body cue:** To enable trustworthy policy' deployment in safety-critical human environments, reliable runtime failure detection becomes important during policy inference.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Detecting failures in robotic manipulation tasks poses several challenges.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** This poses significant challenges since collecting and annotating a comprehensive set of failure examples is often time-consuming, expensive, and even infeasible in many real-world scenarios.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Detecting failures in robotic manipulation tasks poses several challenges. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | In the first stage, we extract scalar signals from policy inputs and/or outputs (e-g., robot states, visual features, generated future actions) that ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | first, stage, extract, scalar, signals, policy, inputs, and/or, outputs, robot | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | models, encounter, out-ofdistribution, OOD, conditions, where, input, observations | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: first, stage, extract, scalar, signals, policy, inputs, and/or, outputs, robot | p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 1 (1. INTRODUCTION) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Aside, being, performant, enables, faster, inference, prior, requires | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | low violation/failure probability with useful intervention | p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. INTRODUCTION - extractive body cue:** This poses significant challenges since collecting and annotating a comprehensive set of failure examples is often time-consuming, expensive, and even infeasible in many real-world scenarios.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** However, unlike FAIL-Detect, these methods require collecting failed trajectories a priori to detect failures.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** If the decision D(7;0) ~ 1, the rollout is flagged as a failure at time step ¢, For instance, in a pick-and-place task, a failure ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)): Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.

- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** STAC does not require failure data, consists ofa score ‘computed post-hoc from a batch of predicted actions and a cconstant-time CP threshold to flag failures, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We show that FAIL-Detect identifies failures accurately and quickly on diverse robotic manipulation tasks, both in simulation and on robot hardware, outperforming SOTA failure detection ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This performance shows the capacity of failure-free failure detection methods to robustly identify failures across many scenarios. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | 2) Calibrate time-varying thresholds 1, based on a CP band. ‘The final decision D(r:8) = 1(Dry(Ar.Or:6) > me) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | How performant is failure detection without failure data? | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 2 (1. INTRODUCTION), interface p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
