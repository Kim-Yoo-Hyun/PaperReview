# Problem - Benchmarking Knowledge Transfer for Lifelong Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (44 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.03310; PDF retrieval source: https://arxiv.org/pdf/2306.03310. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (2 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (2 Background)): A robot in the real world, however, often cannot choose which task to encounter first.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Lifelong learning offers a promising paradigm of building a generalist agent that learns and adapts over its lifespan.
- **p. 1 / Abstract - extractive PDF cue:** Unlike traditional lifelong learning problems in image and text domains, which primarily involve the transfer of declarative knowledge of entities and concepts, lifelong learning in ...
- **p. 1 / Abstract - extractive PDF cue:** To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.
- **p. 1 / Abstract - extractive PDF cue:** Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how ...
- **p. 1 / Abstract - extractive PDF cue:** We develop an extendible procedural generation pipeline that can in principle generate infinitely many tasks.
- **p. 4 / 2 Background - extractive PDF cue:** A robot in the real world, however, often cannot choose which task to encounter first.
- **p. 1 / 1 Introduction - extractive PDF cue:** Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗Equal contribution.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | A robot in the real world, however, often cannot choose which task to encounter first. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | In the end, a robot executes a policy by sampling a continuous value for end-effector action from the output distribution. | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | robot, executes, policy, sampling, continuous, value, end-effector, action, output, distribution | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Here, robot, sensory, input, including, perceptual, observation, information | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: robot, executes, policy, sampling, continuous, value, end-effector, action, output, distribution | p. 6 (2 Background), p. 4 (2 Background), p. 3 (2 Background) |
| Decision / output variable | method trajectory/action; body terms: present, initial, study, LIBERO, investigate, five, major, research | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: robot, objective, learn, policy, maximizes, expected, return, Est | p. 3 (2 Background), p. 3 (2 Background) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2 Background), p. 3 (2 Background), p. 5 (2 Background) |
| Success / guarantee | comparable score and protocol validity | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 27 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗Equal contribution.
- **p. 2 / 1 Introduction - extractive PDF cue:** So far, we lack methods to systematically and quantitatively analyze this complex knowledge transfer.
- **p. 2 / 1 Introduction - extractive PDF cue:** To bridge this research gap, this paper introduces a new simulation benchmark, LIfelong learning BEchmark on RObot manipulation tasks, LIBERO, to facilitate the systematic study ...
- **p. 3 / 2 Background - extractive PDF cue:** Indeed, robot manipulation tasks in general necessitate different types of knowledge, making it hard to determine the cause of failure.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 3 (2 Background), p. 2 (1 Introduction)): We present an initial study using LIBERO to investigate five major research topics in LLDM (Figure 1): 1) knowledge transfer with different types of distribution shift; 2) neural architecture design; ...

- **p. 1 / Abstract - extractive PDF cue:** To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.
- **p. 1 / 1 Introduction - extractive PDF cue:** Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗Equal contribution.
- **p. 3 / 2 Background - extractive PDF cue:** We present four task suites in Section 4.2: three task suites for studying the transfer of knowledge about spatial relationships, object concepts, and task goals ...
- **p. 2 / 1 Introduction - extractive PDF cue:** LIBERO is scalable, extendable, and designed explicitly for studying lifelong learning in robot manipulation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Q5: How robust are different LL algorithms to task ordering in LLDM? | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Therefore, we conjecture that PACKNET is not rich enough to learn on LIBEROLONG; 3) EWC works worse than ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | This finding highlights an important direction for future research: developing algorithms or architectures that are robust to varying ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (2 Background), p. 4 (2 Background), p. 3 (2 Background), p. 5 (2 Background). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (2 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (2 Background), interface p. 6 (2 Background), p. 4 (2 Background), p. 3 (2 Background), p. 5 (2 Background), objective p. 3 (2 Background), p. 3 (2 Background).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
