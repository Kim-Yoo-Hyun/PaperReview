# Problem - OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vSLzoUoJt6; PDF retrieval source: https://openreview.net/pdf/b83bcc6b13bf3bed81ebb73be9bae7cc2be710e7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): However, directly applying pre-trained VLMs to our embodied agent presents challenges of domain shift: 1) Rare grounding tasks: Robotic planners and controllers require multi-modal inputs, including both tools and coordinates ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The rapid progress of navigation, manipulation, and vision models has made mobile manipulators capable in many specialized tasks.
- **p. 1 / Abstract - extractive PDF cue:** However, the open-world mobile manipulation (OWMM) task remains a challenge due to the need for generalization to open-ended instructions and environments, as well as the ...
- **p. 1 / Abstract - extractive PDF cue:** To address this complexity, we propose a novel multi-modal agent architecture that maintains multi-view scene frames and agent states for decision-making and controls the robot ...
- **p. 1 / Abstract - extractive PDF cue:** A second challenge is the hallucination from domain shift.
- **p. 1 / Abstract - extractive PDF cue:** To enhance the agent performance, we further introduce an agentic data synthesis pipeline for the OWMM task to adapt the VLM model to our task ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, directly applying pre-trained VLMs to our embodied agent presents challenges of domain shift: 1) Rare grounding tasks: Robotic planners and controllers require multi-modal inputs, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** A central difficulty in OWMM is the need for comprehensive global scene understanding and reasoning conditioned on natural language instructions and agent state.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, directly applying pre-trained VLMs to our embodied agent presents challenges of domain shift: 1) Rare grounding tasks: Robotic planners and controllers ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | Thus, we introduce a pose graph G and associated RGB images I as the output of the pre-mapping stage on the basis ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Then, linked, planner, takes, state, robot, point, clouds | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage | p. 4 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology) |
| Decision / output variable | base plus arm/gripper action; body terms: summary, contributions, follows, OWMM-Agent, unified, VLM-based, agent, architecture | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: planners, generate, waypoints, satisfy, mechanical, constraints, base, chassis | p. 5 (3 Methodology), p. 25 (C.2 Camera Pose Selection), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 26 (C.2 Camera Pose Selection) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 Methodology), p. 6 (3 Methodology), p. 25 (C.2 Camera Pose Selection) |
| Success / guarantee | task completion and recovery | p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** A central difficulty in OWMM is the need for comprehensive global scene understanding and reasoning conditioned on natural language instructions and agent state.
- **p. 3 / 1 Introduction - extractive PDF cue:** This terminology aligns with the HOMERobot challenge [40].
- **p. 3 / 1 Introduction - extractive PDF cue:** In our formulation, "open-world" refers to semantic diversitythe ability to generalize to unseen scenes, novel object categories, and diverse instances-rather than unconstrained physical exploration without ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Methodology)): In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene understanding, state tracking, and end-to-end action ...

- **p. 3 / 1 Introduction - extractive PDF cue:** • We introduce a simulation-based agentic data synthesis pipeline that enables scalable data collection for instruction fine-tuning for domain adaptation with minimized human effort, with ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Based on the aforementioned observations, we propose a novel VLM agent framework, OWMM-Agent, to address these challenges and leverage the power of VLMs for OWMM ...
- **p. 3 / 1 Introduction - extractive PDF cue:** (3) Simto-real transfer: Our framework is validated on real robotic hardware.
- **p. 4 / 3 Methodology - extractive PDF cue:** The overview of our method is shown in Figure 2.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 27 | H Failure Mode Analysis To better understand the limitations and bottlenecks of our system, we conducted a comprehensive ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Episodic evaluations in simulated environments further confirmed the OWMM-Agent's superior success rates and robustness against common failure modes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 27 | Since the current evaluation pipeline does not support automatic failure case analysis, we manually reviewed the action sequences ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 2 (1 Introduction), objective p. 5 (3 Methodology), p. 25 (C.2 Camera Pose Selection), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 26 (C.2 Camera Pose Selection).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
