# Problem - Scaffolding Dexterous Manipulation with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PdRf0O7baQ; PDF retrieval source: https://openreview.net/pdf/8ca7e389e552ce42c27f330fe80cd6672bf124e8.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a promising approach by enabling large-scale experience generation [3].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control.
- **p. 1 / Abstract - extractive PDF cue:** While reinforcement learning (RL) can alleviate the data bottleneck by generating experience in simulation, it typically relies on carefully designed, task-specific reward functions, which hinder ...
- **p. 1 / Abstract - extractive PDF cue:** Thus, contemporary works in dexterous manipulation have often bootstrapped from reference trajectories.
- **p. 1 / Abstract - extractive PDF cue:** These trajectories specify target hand poses that guide the exploration of RL policies and object poses that enable dense, task-agnostic rewards.
- **p. 1 / Abstract - extractive PDF cue:** However, sourcing suitable trajectories-particularly for dexterous hands-remains a significant challenge.
- **p. 1 / 1 Introduction - extractive PDF cue:** To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a promising approach by ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The prevailing approach for training generalist policies - imitation learning from demonstrations [5, 49] - has achieved limited success with robot hands, primarily due to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To avoid both data scarcity and the embodiment gap, a combination of reinforcement learning (RL) and sim-to-real transfer has emerged as a ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Proj, Inference, board, apple, wrist, Environment, keypoint, tracking, Generate, motion | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | large, amount, complexity, arises, need, guide, exploration, action | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Proj, Inference, board, apple, wrist, Environment, keypoint, tracking, Generate, motion | p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 2 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: Moreover, showcase, transfers, realworld, robotic, hands, without, human | p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: long, motions, generally, encapsulate, desired, behavior, optimize, per-timestep | p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (2. Plan Generation 𝜏) |
| Success / guarantee | instruction-conditioned task success | p. 29 (Figure/Table caption), p. 30 (Figure/Table caption), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** The prevailing approach for training generalist policies - imitation learning from demonstrations [5, 49] - has achieved limited success with robot hands, primarily due to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Though demonstration tracking overcomes the design challenges associated with RL, it paradoxically re-introduces the same dependence on demonstrations we sought to avoid in the first ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We evaluate our method across a suite of challenging dexterous manipulation tasks in simulation requiring semantic understanding, human knowledge about concepts like "hammering", and precise ...

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)): Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.

- **p. 2 / 1 Introduction - extractive PDF cue:** Building upon this insight, we introduce a framework for learning manipulation policies for dexterous robot hands with VLM-generated motion plans and residual RL.
- **p. 2 / 1 Introduction - extractive PDF cue:** Across 8 tasks, our method achieves close performance in both success rate and generalization to handcrafted, oracle plans despite requiring no manual reward engineering.
- **p. 1 / Abstract - extractive PDF cue:** Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our analysis reveals that the most significant failure mode is incomplete trajectory tracking, occurring in 26% of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | Figure 9: Results on the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 2 (1 Introduction), p. 6 (2. Plan Generation 𝜏). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 2 (1 Introduction), p. 6 (2. Plan Generation 𝜏), objective p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
