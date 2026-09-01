# Problem - AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=88RKxlFUNY; PDF retrieval source: https://openreview.net/pdf/1a99a8c26a0bf879894a517257af43defc03d88a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (ABSTRACT), p. 1 (ABSTRACT)): Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI.
- **p. 1 / ABSTRACT - extractive PDF cue:** Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes.
- **p. 1 / ABSTRACT - extractive PDF cue:** However, real-world outdoor exploration typically occurs in unknown environments where detailed navigation instructions are unavailable.
- **p. 1 / ABSTRACT - extractive PDF cue:** Instead, only coarse-grained positional or directional guidance can be provided, requiring UAVs to autonomously navigate through continuous planning and obstacle avoidance.
- **p. 1 / ABSTRACT - extractive PDF cue:** To bridge this gap, we propose AutoFly, an end-to-end Vision-Language-Action (VLA) model for autonomous UAV navigation.
- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive PDF cue:** This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.
- **p. 4 / 3 METHOD - extractive PDF cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | TASK, FORMULATION, formulate, autonomous, navigation, learning, control, policy, takes, current | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Vision-language, navigation, VLN, Chen, Misra, Krantz, Anderson, Thomason | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: TASK, FORMULATION, formulate, autonomous, navigation, learning, control, policy, takes, current | p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 1 (1 INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: standardized, backbone, enables, fair, comparison, core, contributions, while | p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: When, episode, continues, target, includes, immediate, reward, discounted | p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 22 (A.5.4 PARALLEL INFERENCE ARCHITECTURE), p. 22 (A.5.4 PARALLEL INFERENCE ARCHITECTURE) |
| Success / guarantee | goal reach with collision-free execution | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3.2 ABLATION EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / ABSTRACT - extractive PDF cue:** Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes.

## What the Paper Changes

PDF contribution framing (p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 22 (A.5.3 MODEL ACCELERATION)): This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.

- **p. 4 / 3 METHOD - extractive PDF cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 4 / 3 METHOD - extractive PDF cue:** Our framework integrates three core components, including a visionlanguage model, pseudo-depth encoder, and action de-tokenizer, as illustrated in Figure 2.
- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive PDF cue:** We utilize the same prism-siglip-7b backbone for consistency across VLM-based baselines, ensuring that performance differences reflect methodological contributions rather than backbone variations.
- **p. 22 / A.5.3 MODEL ACCELERATION - extractive PDF cue:** Additional CUDA operators are implemented for custom depth processing operations, while model parallelism enables distributed inference across multiple GPU processes to handle the computational demands ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 24 | To address these limitations, we plan to enhance AutoFly's sensing capabilities through LiDAR integration, which will provide comprehensive ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 24 | Future work will integrate Reinforcement Learning to enable active interaction with dynamic environments, allowing the system to learn ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | The baseline model's collision rate reaches 37.7%, frequently failing to maintain safe distances from moving obstacles or predict ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 1 (1 INTRODUCTION), p. 4 (3 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (ABSTRACT), p. 1 (ABSTRACT), interface p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 1 (1 INTRODUCTION), p. 4 (3 METHOD), objective p. 4 (3 METHOD), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL), p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 17 (A.2.3 DATA COLLECTION ALGORITHM BASED ON RL).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
