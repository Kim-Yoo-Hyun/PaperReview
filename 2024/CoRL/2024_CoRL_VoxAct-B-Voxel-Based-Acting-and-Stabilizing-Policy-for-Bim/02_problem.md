# Problem - VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/liu25i.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): However, they are generally sample inefficient, and using primitives can hinder generalization to different tasks as they are not easily adaptable to other types of tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Bimanual manipulation is critical to many robotics applications.
- **p. 1 / Abstract - extractive body cue:** In contrast to single-arm manipulation, bimanual manipulation tasks are challenging due to higher-dimensional action spaces.
- **p. 1 / Abstract - extractive body cue:** Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose VoxAct-B, a language-conditioned, voxel-based method that leverages Vision Language Models (VLMs) to prioritize key regions within the scene and reconstruct ...
- **p. 1 / Abstract - extractive body cue:** We provide this voxel grid to our bimanual manipulation policy to learn acting and stabilizing actions.
- **p. 1 / 1 Introduction - extractive body cue:** However, they are generally sample inefficient, and using primitives can hinder generalization to different tasks as they are not easily adaptable to other types of ...
- **p. 1 / 1 Introduction - extractive body cue:** They typically require two-hand coordination and high-precision, fine-grained manipulation, which are challenging for current robotic manipulation systems.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, they are generally sample inefficient, and using primitives can hinder generalization to different tasks as they are not easily adaptable to ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | time, step, input, voxel, observation, proprioception, data, robot, arms, language | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Then, provide, appropriate, language, instructions, bimanual, manipulation, policy | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: time, step, input, voxel, observation, proprioception, data, robot, arms, language | p. 4 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: VoxAct-B, novel, voxel-based, language-conditioned, bimanual, manipulation, allows, learn | p. 1 (1 Introduction), p. 4 (4 Method), p. 1 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: overall, training, loss, VoxAct-B, Ltotal, Lacting, Lstabilizing, where | p. 5 (4 Method), p. 5 (4 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 14 (A.1 Additional Implementation Details), p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines) |
| Success / guarantee | instruction-conditioned task success | p. 14 (A.1 Additional Implementation Details), p. 16 (C Additional Implementation Details for the Baselines), p. 7 (6 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** They typically require two-hand coordination and high-precision, fine-grained manipulation, which are challenging for current robotic manipulation systems.

## What the Paper Changes

PDF contribution framing (p. 1 (1 Introduction), p. 4 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method)): To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.

- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **p. 1 / 1 Introduction - extractive body cue:** To address this, we propose utilizing VLMs to focus on the most pertinent regions within the scene by cropping out less relevant regions.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a bimanual version of Open Drawer, Open Jar, Put Item in Drawer, and Hand Over Item tasks.
- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | VoxAct-B succeeds in 6 out of 10 trials; the failures include robot joints hitting their limits, imprecision in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2: Overview of VoxAct-B. Given RGB-D images and a language goal, we input an RGB image from ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 3: Top: VLMs usage as part of VoxAct-B, visualizing the Open Jar task in simulation, showing the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 4 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method), objective p. 5 (4 Method), p. 5 (4 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
