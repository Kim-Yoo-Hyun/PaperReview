# Problem - Benchmarking Safe Exploration in Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/; PDF retrieval source: https://cdn.openai.com/safexp-short.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard sequential decision-making problems that cannot ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) agents need to explore their environments in order to learn optimal policies by trial and error.
- **p. 1 / Abstract - extractive body cue:** In many environments, safety is a critical concern and certain errors are unacceptable: for example, robotics systems that interact with humans should never cause injury ...
- **p. 1 / Abstract - extractive body cue:** While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating ...
- **p. 1 / Abstract - extractive body cue:** Consequently we take the position that safe exploration should be viewed as a critical focus area for RL research, and in this work we make ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / 1 Introduction - extractive body cue:** While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard ...
- **p. 2 / 1 Introduction - extractive body cue:** However, there is not yet a standard set of environments for making progress on safe exploration specifically.2 Different papers use different environments and evaluation procedures, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | recommend, protocol, evaluating, constrained, algorithms, Safety, Gym, environments, three, metrics | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | While, sim-to-real, transfer, learning, algorithms, mitigate, issue, expect | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: recommend, protocol, evaluating, constrained, algorithms, Safety, Gym, environments, three, metrics | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Decision / output variable | method trajectory/action; body terms: address, present, Safety, Gym, tools, accelerating, safe, exploration | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: expressed, reward, function, auxiliary, cost, functions, respectively, fundamental | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 15 (5 Experiments), p. 16 (5.3 Results), p. 16 (5.3 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** However, there is not yet a standard set of environments for making progress on safe exploration specifically.2 Different papers use different environments and evaluation procedures, ...
- **p. 2 / 1 Introduction - extractive body cue:** There is a gradient of difficulty across benchmark environments.
- **p. 1 / 1 Introduction - extractive body cue:** However, for many problems simulators will either not be available or high-enough fidelity for RL to learn behaviors that succeed in the real environment.
- **p. 3 / 1 Introduction - extractive body cue:** Towards providing useful baselines: To make Safety Gym relevant out-of-the-box and to partially clarify state-of-the-art in safe exploration, we benchmark several existing constrained and unconstrained ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract)): To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.

- **p. 2 / 1 Introduction - extractive body cue:** Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / Abstract - extractive body cue:** Second, we present the Safety Gym benchmark suite, a new slate of high-dimensional continuous control environments for measuring research progress on constrained RL.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | [2017], we omit the learned failure predictor they used for cost shaping. | reported limitation/failure wording; scope must be verified |
| body cue at p. 21 | There are a number of avenues we consider promising for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Figure 6: Diversity of generated layouts for the Safexp-PointPush2-v0 env. 4.2 Safety Gym Benchmark Suite Safety Gym ships ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | First and foremost, it corresponds directly to safety outcomes: a lower cost rate means that fewer unsafe things ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
