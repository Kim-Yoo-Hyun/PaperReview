# Problem - Habitat 2.0: Training Home Assistants to Rearrange their Habitat

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2021/file/021bbc7ee20b71134d53e20206bd6feb-Paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** We make comprehensive contributions to all levels of the embodied AI stack - data, simulation, and benchmark tasks.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...
- **p. 1 / Abstract - extractive body cue:** These large-scale engineering contributions allow us to systematically compare deep reinforcement learning (RL) at scale and classical sense-plan-act (SPA) pipelines in long-horizon structured tasks, with ...
- **p. 1 / Abstract - extractive body cue:** We find that (1) flat RL policies struggle on HAB compared to hierarchical ones; (2) a hierarchy with independent skills suffers from ‘hand-off problems', and ...
- **p. 2 / 1 Introduction - extractive body cue:** Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.
- **p. 3 / 1 Introduction - extractive body cue:** Hierarchy cuts both ways: However, a hierarchy with independent skills suffers from ‘hand-off problems' where a succeeding skill isn't set up for success by the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL). | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | MonolithicRL, sensors-to-actions, policy, trained, end-to-end, reinforcement, learning, supplementary, analyze, different | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | every, step, outputs, desired, change, end-effector, position, inverse | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: MonolithicRL, sensors-to-actions, policy, trained, end-to-end, reinforcement, learning, supplementary, analyze, different | p. 7 (8 GPUs), p. 8 (8 GPUs), p. 7 (8 GPUs) |
| Decision / output variable | method trajectory/action; body terms: support, long-term, research, agenda, present, ReplicaCAD, artist-authored, fully-interactive | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: However, performance, drop, SPA, qualitative, suggest, unseen, receptacles | p. 8 (8 GPUs), p. 7 (8 GPUs) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 6 (8 GPUs), p. 6 (8 GPUs) |
| Success / guarantee | comparable score and protocol validity | p. 10 (Figure/Table caption), p. 8 (8 GPUs), p. 10 (8 GPUs) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** Hierarchy cuts both ways: However, a hierarchy with independent skills suffers from ‘hand-off problems' where a succeeding skill isn't set up for success by the ...
- **p. 2 / 1 Introduction - extractive body cue:** As we will show, they also directly translate to training-time speed-up and accuracy improvements from training agents (for object rearrangement tasks) on more experience. • ...
- **p. 3 / 1 Introduction - extractive body cue:** We conduct a systematic study of two distinct techniques - monolithic ‘sensors-to-actions' policies trained with reinforcement learning (RL) at scale, and classical senseplan-act pipelines (SPA) ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction)): To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 unique layouts of a single ...

- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Developing such embodied intelligent systems is a goal of deep scientific and societal value.
- **p. 3 / 1 Introduction - extractive body cue:** H2.0 is free, open-sourced under the MIT license, and under active development.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The agent fails if the accumulated contact force experienced by the arm/body exceeds a threshold of 5k Newtons. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | If the scalar is negative and the gripper is currently holding an object, then the object currently held ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We cannot make any such claims for SPA. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 7 (8 GPUs), p. 8 (8 GPUs), p. 7 (8 GPUs), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 7 (8 GPUs), p. 8 (8 GPUs), p. 7 (8 GPUs), p. 2 (1 Introduction), objective p. 8 (8 GPUs), p. 7 (8 GPUs).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
