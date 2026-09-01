# Problem - XSkill: Cross Embodiment Skill Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/xu23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.09955. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference and unexpected execution failures.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Human demonstration videos are a widely available data source for robot learning and an intuitive user interface for expressing desired behavior.
- **p. 1 / Abstract - extractive body cue:** However, directly extracting reusable robot manipulation skills from unstructured human videos is challenging due to the big embodiment difference and unobserved action parameters.
- **p. 1 / Abstract - extractive body cue:** To bridge this embodiment gap, this paper introduces XSkill, an imitation learning framework that 1) discovers a cross-embodiment representation called skill prototypes purely from unlabeled ...
- **p. 1 / Abstract - extractive body cue:** Our experiments in simulation and real-world environments show that the discovered skill prototypes facilitate both skill transfer and composition for unseen tasks, resulting in a ...
- **p. 1 / Abstract - extractive body cue:** The benchmark, code, and qualitative results are on project website.
- **p. 2 / 1 Introduction - extractive body cue:** With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference ...
- **p. 2 / 1 Introduction - extractive body cue:** Meanwhile, our approach differs from existing work on single-embodiment skill discovery [7, 8, 9], which solely relies on on-robot demonstration data.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | In the transfer phase, the algorithm uses the robot teleoperation dataset Dr to learn the skill-conditioned visuomotor policy P(a/s, z), where z ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | transfer, phase, algorithm, uses, robot, teleoperation, dataset, learn, skill-conditioned, visuomotor | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | skill-conditioned, diffusion, policy, translates, observed, human, demonstration, robot | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: transfer, phase, algorithm, uses, robot, teleoperation, dataset, learn, skill-conditioned, visuomotor | p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: Together, cross-embodiment, dataset, simulation, real, world, hope, inspire | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: ftemporal, fprototype, trained, jointly, minimize, CorssEntropy, loss, between | p. 4 (3 Approach) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Approach), p. 4 (3 Approach) |
| Success / guarantee | closed-loop task success and robustness | p. 6 (4 Evaluation), p. 8 (Figure/Table caption), p. 6 (4 Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Meanwhile, our approach differs from existing work on single-embodiment skill discovery [7, 8, 9], which solely relies on on-robot demonstration data.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Approach), p. 1 (1 Introduction)): Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill ...

- **p. 1 / 1 Introduction - extractive body cue:** We refer to the task as "Cross-Embodiment Skill Discovery" and introduce our method 7th Conference on Robot Learning (CoRL 2023), Atlanta, USA. arXiv:2307.09955v2 [cs.RO] 28 ...
- **p. 2 / 1 Introduction - extractive body cue:** To encourage across-embodiment alignment, we introduce a set of learnable skill prototypes through feature clustering.
- **p. 3 / 3 Approach - extractive body cue:** The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- **p. 1 / 1 Introduction - extractive body cue:** 3) Compose, performing novel compositions of the learned skills to accomplish new tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 4 (3 Approach).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
