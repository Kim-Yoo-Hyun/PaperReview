# Problem - CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.03227; PDF retrieval source: https://arxiv.org/pdf/2112.03227. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 1 (A LONG-STANDING goal for robotics and embodied), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 3 (3) CALVIN Challenge)): Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** General-purpose robots coexisting with humans in their environment must learn to relate human language to their perceptions and actions to be useful in a range ...
- **p. 1 / Abstract - extractive body cue:** Moreover, they need to acquire a diverse repertoire of general-purpose skills that allow composing long-horizon tasks by following unconstrained language instructions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.
- **p. 1 / Abstract - extractive body cue:** Our aim is to make it possible to develop agents that can solve many robotic manipulation tasks over a long horizon, from onboard sensors, and ...
- **p. 1 / Abstract - extractive body cue:** CALVIN tasks are more complex in terms of sequence length, action space, and language than existing vision-and-language task datasets and supports flexible specification of sensor ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive body cue:** Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.
- **p. 1 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** This stands in contrast to current robots, which typically lack this generalization ability and learn individual tasks one at a time.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Observation, Action, Space, Unlike, prior, relies, RGB, images | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred | p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge) |
| Decision / output variable | method trajectory/action; body terms: present, CALVIN, Composing, Actions, Language, Vision, open-source, simulated | p. 1 (Abstract), p. 2 (A LONG-STANDING goal for robotics and embodied), p. 3 (III. CALVIN) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: short, horizon, goal, image, conditioned, demonstrations, simple, maximum | p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS) |
| Success / guarantee | comparable score and protocol validity | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** This stands in contrast to current robots, which typically lack this generalization ability and learn individual tasks one at a time.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In the most difficult evaluation, the methods must generalize to unseen entities by training on a large interaction corpora covering three environments and testing on ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive body cue:** We provide an evaluation protocol with evaluation modes of varying difficulty by choosing different combinations of sensor suites and amounts of training environments.
- **p. 3 / 3) CALVIN Challenge - extractive body cue:** Due to the general difficulty of languageconditioned multi-task closed-loop control, we reduced the complexity of the objects to unicolored primitive shapes.

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 2 (A LONG-STANDING goal for robotics and embodied), p. 3 (III. CALVIN), p. 4 (3) CALVIN Challenge), p. 4 (3) CALVIN Challenge)): In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.

- **p. 2 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** To address this problem we present CALVIN, a new opensource simulated benchmark that links human language to robot motor skills, behaviors, and objects in interactive ...
- **p. 3 / III. CALVIN - extractive body cue:** The CALVIN benchmark consists of three key components, which are:
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** This style of data is very different from commonly used task-specific data, which only consists of expert trajectories.
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** Thus, to accelerate progress in language-driven robotics, we present a set of evaluation protocols of varying difficulty by choosing different combinations of sensor suites and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 1 (A LONG-STANDING goal for robotics and embodied), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 3 (3) CALVIN Challenge), interface p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS), objective p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** The long horizon of CALVIN tasks poses a significant challenge with sub-problems including the acquisition of a diverse repertoire of general-purpose skills, object detection, referring expression and action grounding, and ... (p. 7, VI. CONCLUSION).
- **Formulation-changing contribution:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks. (p. 1, Abstract).
- **Assumption/failure evidence:** For the Long-Horizon MTLC evaluation we observe that the agents perform poorly on CALVIN's long-horizon tasks with high-dimensional state spaces. (p. 7, V. EXPERIMENTAL RESULTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
