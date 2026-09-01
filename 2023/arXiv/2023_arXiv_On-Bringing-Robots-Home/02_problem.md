# Problem - On Bringing Robots Home

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.16098; PDF retrieval source: https://arxiv.org/pdf/2311.16098. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (1 Introduction)): Such an effort requires a shift from the prevailing paradigm - current research in robotics is predominantly either conducted in industrial environments or in academic labs, both containing curated objects, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Throughout history, we have successfully integrated various machines into our homes.
- **p. 1 / Abstract - extractive PDF cue:** Dishwashers, laundry machines, stand mixers, and robot vacuums are just a few recent examples.
- **p. 1 / Abstract - extractive PDF cue:** However, these machines excel at performing only a single task effectively.
- **p. 1 / Abstract - extractive PDF cue:** The concept of a "generalist machine" in homes - a domestic assistant that can adapt and learn from our needs, all while remaining cost-effective - ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we initiate a large-scale effort towards this goal by introducing Dobb·E, an affordable yet versatile general-purpose system for learning robotic manipulation within ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Such an effort requires a shift from the prevailing paradigm - current research in robotics is predominantly either conducted in industrial environments or in academic ...
- **p. 4 / 1 Introduction - extractive PDF cue:** In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Such an effort requires a shift from the prevailing paradigm - current research in robotics is predominantly either conducted in industrial environments ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | Behavior cloning involves training a model to mimic a demonstrated behavior or action, often through the use of labeled training data mapping ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | Behavior, cloning, involves, training, model, mimic, demonstrated, action, often, through | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | However, augmenting, controllers, force, feedback, nearly, impossible, often | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: Behavior, cloning, involves, training, model, mimic, demonstrated, action, often, through | p. 6 (C D), p. 6 (C D), p. 7 (C D) |
| Decision / output variable | base plus arm/gripper action; body terms: present, Dobb, framework, teaching, robots, homes, embodying, three | p. 4 (1 Introduction), p. 1 (Abstract), p. 7 (C D) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: concept, generalist, machine, homes, domestic, assistant, adapt, learn | p. 6 (C D) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (C D), p. 6 (C D), p. 8 (C D) |
| Success / guarantee | task completion and recovery | p. 16 (3 Experiments), p. 23 (3 Experiments), p. 21 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / 1 Introduction - extractive PDF cue:** Such an effort requires a shift from the prevailing paradigm - current research in robotics is predominantly either conducted in industrial environments or in academic ...

## What the Paper Changes

PDF contribution framing (p. 4 (1 Introduction), p. 1 (Abstract), p. 7 (C D), p. 1 (Abstract), p. 4 (1 Introduction)): In this work we present Dobb·E, a framework for teaching robots in homes by embodying three core principles: efficiency, safety, and user comfort.

- **p. 1 / Abstract - extractive PDF cue:** Success 81% Pick up hat Open microwave door Pick up paper towel roll Place rag in laundry Open cabinet door Close cabinet door Open shower ...
- **p. 7 / C D - extractive PDF cue:** Our method can be divided into four broad stages: (a) designing a hardware setup that helps us in the collection of demonstrations and their seamless ...
- **p. 1 / Abstract - extractive PDF cue:** Then, in a novel home environment, with five minutes of demonstrations and fifteen minutes of adapting the HPR model, we show that Dobb·E can reliably ...
- **p. 4 / 1 Introduction - extractive PDF cue:** For user comfort, we have developed an ergonomic demonstration collection tool, enabling us to gather task-specific demonstrations in unfamiliar homes without direct robot operation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | Figure 20: First-person POV rollouts of Home 3 Pick and Place comparing (top) a policy trained on demos ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 18: Opening an outward facing window blind (top row) both without depth (second row) and with depth ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | We discuss the failure cases further in Section 3.3. | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Once we turned on an overhead light for even lighting, there were no more failures. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (C D), p. 6 (C D), p. 7 (C D), p. 7 (C D). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (1 Introduction), interface p. 6 (C D), p. 6 (C D), p. 7 (C D), p. 7 (C D), objective p. 6 (C D).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
