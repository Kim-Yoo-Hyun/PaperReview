# Problem - Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4GaB4fdIq; PDF retrieval source: https://openreview.net/pdf/a273e15cd7e38fd010663df74dfea2486251fe0e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): For example, when the initial navigation fails, entropy minimization intensifies the probabilities of the actions that lead to failure in repeated episodes.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Navigating in an unfamiliar environment during deployment poses a critical challenge for a vision-language navigation (VLN) agent.
- **p. 1 / Abstract - extractive PDF cue:** Yet, test-time adaptation (TTA) remains relatively underexplored in robotic navigation, leading us to the fundamental question: what are the key properties of TTA for online ...
- **p. 1 / Abstract - extractive PDF cue:** In our view, effective adaptation requires three qualities: 1) flexibility in handling different navigation outcomes, 2) interactivity with external environment, and 3) maintaining a harmony ...
- **p. 1 / Abstract - extractive PDF cue:** To address this, we introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based reinforcement learning.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, FEEDTTA learns by maximizing binary episodic feedback, a practical setup in which the agent receives a binary scalar after each episode that indicates the ...
- **p. 1 / 1. Introduction - extractive PDF cue:** For example, when the initial navigation fails, entropy minimization intensifies the probabilities of the actions that lead to failure in repeated episodes.
- **p. 1 / 1. Introduction - extractive PDF cue:** One existing approach (Gao et al., 2024a) relies on the widely adopted TTA paradigm of entropy minimization (Wang et al., 2020a; Zhang et al., 2022), ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For example, when the initial navigation fails, entropy minimization intensifies the probabilities of the actions that lead to failure in repeated episodes. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Right, Specifically, among, variants, negative, value, reversion, shifts, original, gradient | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | FEEDTTA, leverages, Monte, Carlo, policy, gradient, algorithm, REINFORCE | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Right, Specifically, among, variants, negative, value, reversion, shifts, original, gradient | p. 4 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, follows, introduce, FEEDTTA, novel, TTA, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Task Description) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: general, REINFORCE, algorithm, aims, optimizing, parameter, policy, maximize | p. 4 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 3 (3.2. Binary Episodic Feedback), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 3 (3.2. Binary Episodic Feedback) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (4.2. Evaluation Metrics), p. 8 (5.3. LLMs as Feedback Oracle), p. 5 (4.2. Evaluation Metrics) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** One existing approach (Gao et al., 2024a) relies on the widely adopted TTA paradigm of entropy minimization (Wang et al., 2020a; Zhang et al., 2022), ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This ensures that the policy can adjust dynamically to different outcomes without overfitting to specific failure patterns. • Interactivity.
- **p. 2 / 1. Introduction - extractive PDF cue:** For example, unlike conventional optimization signals, FEEDTTA estimates gradients at two distinct extremes (i.e., +1 for success and -1 for failure).

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Task Description), p. 4 (3.3. Stochastic Gradient Reversion), p. 1 (1. Introduction)): In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL.

- **p. 2 / 1. Introduction - extractive PDF cue:** Based on this analysis, we introduce FEEDTTA, a novel TTA framework for online VLN using feedback-based reinforcement learning (RL).
- **p. 3 / 3.1. Task Description - extractive PDF cue:** Each element Xn consists of a natural language instruction In, and an initial visual state s0 n, which is a 360◦panoramic view of the surrounding ...
- **p. 4 / 3.3. Stochastic Gradient Reversion - extractive PDF cue:** Therefore, we propose Stochastic Gradient Reversion (SGR), a gradient regularization method for FEEDTTA to maintain plasticity and stability during adaptation.
- **p. 1 / 1. Introduction - extractive PDF cue:** The navigation policies are typically trained *Equal contribution 1Department of AI, Korea University, Seoul, S.Korea 2Samsung AI Center, DS Division, Suwon, S.Korea.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | The proposed adaptation strategy utilizing binary episodic feedback enables agents to dynamically interact with their external environment by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Illustration of the learning paradigm of FEEDTTA. The navigation agent adapts to streaming online test data ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Feedback accuracies less than 50% leads to obvious adaptation failure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We leverage a two-step LLM architecture for determining the navigation success or failure. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback), objective p. 4 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 5 (3.3. Stochastic Gradient Reversion), p. 3 (3.2. Binary Episodic Feedback), p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
