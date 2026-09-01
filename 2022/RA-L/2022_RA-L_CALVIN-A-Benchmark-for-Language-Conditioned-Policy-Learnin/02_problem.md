# Problem - CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.03227; PDF retrieval source: https://arxiv.org/pdf/2112.03227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 1 (A LONG-STANDING goal for robotics and embodied), p. 1 (Front matter), p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 3 (3) CALVIN Challenge)): Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** General-purpose robots coexisting with humans in their environment must learn to relate human language to their perceptions and actions to be useful in a range ...
- **p. 1 / Abstract - extractive PDF cue:** Moreover, they need to acquire a diverse repertoire of general-purpose skills that allow composing long-horizon tasks by following unconstrained language instructions.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.
- **p. 1 / Abstract - extractive PDF cue:** Our aim is to make it possible to develop agents that can solve many robotic manipulation tasks over a long horizon, from onboard sensors, and ...
- **p. 1 / Abstract - extractive PDF cue:** CALVIN tasks are more complex in terms of sequence length, action space, and language than existing vision-and-language task datasets and supports flexible specification of sensor ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive PDF cue:** Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.
- **p. 1 / A LONG-STANDING goal for robotics and embodied - extractive PDF cue:** This stands in contrast to current robots, which typically lack this generalization ability and learn individual tasks one at a time.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Observation, Action, Space, Unlike, prior, relies, RGB, images | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred | p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge) |
| Decision / output variable | method trajectory/action; body terms: present, CALVIN, Composing, Actions, Language, Vision, open-source, simulated | p. 1 (Abstract), p. 2 (A LONG-STANDING goal for robotics and embodied), p. 3 (III. CALVIN) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: short, horizon, goal, image, conditioned, demonstrations, simple, maximum | p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS) |
| Success / guarantee | comparable score and protocol validity | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / A LONG-STANDING goal for robotics and embodied - extractive PDF cue:** This stands in contrast to current robots, which typically lack this generalization ability and learn individual tasks one at a time.
- **p. 1 / Front matter - extractive PDF cue:** In the most difficult evaluation, the methods must generalize to unseen entities by training on a large interaction corpora covering three environments and testing on ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive PDF cue:** We provide an evaluation protocol with evaluation modes of varying difficulty by choosing different combinations of sensor suites and amounts of training environments.
- **p. 3 / 3) CALVIN Challenge - extractive PDF cue:** Due to the general difficulty of languageconditioned multi-task closed-loop control, we reduced the complexity of the objects to unicolored primitive shapes.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 2 (A LONG-STANDING goal for robotics and embodied), p. 3 (III. CALVIN), p. 4 (3) CALVIN Challenge), p. 4 (3) CALVIN Challenge)): In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.

- **p. 2 / A LONG-STANDING goal for robotics and embodied - extractive PDF cue:** ACCEPTED MAY, 2022 To address this problem we present CALVIN, a new opensource simulated benchmark that links human language to robot motor skills, behaviors, and ...
- **p. 3 / III. CALVIN - extractive PDF cue:** The CALVIN benchmark consists of three key components, which are:
- **p. 4 / 3) CALVIN Challenge - extractive PDF cue:** This style of data is very different from commonly used task-specific data, which only consists of expert trajectories.
- **p. 4 / 3) CALVIN Challenge - extractive PDF cue:** Thus, to accelerate progress in language-driven robotics, we present a set of evaluation protocols of varying difficulty by choosing different combinations of sensor suites and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 1 (A LONG-STANDING goal for robotics and embodied), p. 1 (Front matter), p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 3 (3) CALVIN Challenge), interface p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS), objective p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
