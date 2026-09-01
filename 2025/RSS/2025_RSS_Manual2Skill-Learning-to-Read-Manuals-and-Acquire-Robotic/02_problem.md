# Problem - Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p150.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p150.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 2 (A. Furniture Assembly), p. 3 (B. VLM Guided Robot Learning), p. 1 (I. INrRopuction), p. 2 (A. Furniture Assembly)): For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Humans possess an extraordinary ability to under stand and execute complex manipulation tasks by interpreting abstract instruction manuals.
- **p. 1 / Abstract - extractive body cue:** For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- **p. 1 / Abstract - extractive body cue:** Our approach leverages a VisionLanguage Model (VLM) to extract structured information from instructional images and then uses this information to construct hierarchical assembly graphs.
- **p. 1 / Abstract - extractive body cue:** These graphs represent parts, subassemblies, and the relationships between them.
- **p. 2 / A. Furniture Assembly - extractive body cue:** However, existing works typically focus on specific subproblems rather than addressing the entire assembly pipeline.
- **p. 3 / B. VLM Guided Robot Learning - extractive body cue:** However, they are mostly limited to tabletop manipulation tasks and do not generalize well to more complex, long-horizon assembly problems.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | triplet, format, enhances, interpretability, ensures, consistency, structuring, outputs, same, data | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | potential, direction, development, Vision, Language, Action, Model, VLA | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: triplet, format, enhances, interpretability, ensures, consistency, structuring, outputs, same, data | p. 4 (2. Per-step Assembly Pose Estimation), p. 17 (B. Pose Estimation Implementation), p. 2 (B. VLM Guided Robot Learning) |
| Decision / output variable | action, pose, option or chunk a; body terms: present, Manual2Skill, novel, framework, enables, robots, perform, complex | p. 1 (Abstract), p. 2 (I. INrRopuction), p. 2 (I. INrRopuction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Chamfer, Distance, Loss, function, minimizes, holistic, between, point | p. 14 (B. Pose Estimation Implementation), p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 16 (B. Pose Estimation Implementation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 16 (B. Pose Estimation Implementation), p. 16 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation) |
| Success / guarantee | instruction-conditioned task success | p. 16 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / A. Furniture Assembly - extractive body cue:** However, existing works typically focus on specific subproblems rather than addressing the entire assembly pipeline.
- **p. 3 / B. VLM Guided Robot Learning - extractive body cue:** However, they are mostly limited to tabletop manipulation tasks and do not generalize well to more complex, long-horizon assembly problems.
- **p. 1 / I. INrRopuction - extractive body cue:** Replicating the human ability to transfer abstract manuals to real-world actions re- ‘mains a significant challenge for robots.
- **p. 2 / A. Furniture Assembly - extractive body cue:** Part assembly is a long-standing challenge with extensive research exploring how to construct a complete shape from individual components or parts (6, 13, 20, 27, ...

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 2 (I. INrRopuction), p. 2 (I. INrRopuction), p. 1 (Front matter), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation)): In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.

- **p. 2 / I. INrRopuction - extractive body cue:** In this paper, we propose Manual2Skill, a novel robot learn
- **p. 2 / I. INrRopuction - extractive body cue:** + We propose Manual2Skill, a novel framework that leverages VLM to learn robotic skills from manuals, enabling 4 generalizable assembly pipeline for IKEA furniture
- **p. 1 / Front matter - extractive body cue:** We propose Manual2 ‘enabling robots to understand and execute complex manipulation tasks in mi the input of our pipeline: the pictures of the assembly manual ...
- **p. 3 / A. VLM Guided Hierarchical Assembly Graph Generation - extractive body cue:** Every VLM prompt consists of two components:

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | failure mode arises from planning limitations, particularly in handling complex obstacles. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The most common failure occurs when the VLM fails to generate a fully accurate assembly graph, leading to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We adopt the assembly success rate as the evaluation metric and define the following situations as a failure: ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (2. Per-step Assembly Pose Estimation), p. 17 (B. Pose Estimation Implementation), p. 2 (B. VLM Guided Robot Learning), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 2 (A. Furniture Assembly), p. 3 (B. VLM Guided Robot Learning), p. 1 (I. INrRopuction), p. 2 (A. Furniture Assembly), interface p. 4 (2. Per-step Assembly Pose Estimation), p. 17 (B. Pose Estimation Implementation), p. 2 (B. VLM Guided Robot Learning), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation), objective p. 14 (B. Pose Estimation Implementation), p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 16 (B. Pose Estimation Implementation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
