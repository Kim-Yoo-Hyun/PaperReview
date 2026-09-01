# Problem - GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.03984; PDF retrieval source: https://arxiv.org/pdf/2503.03984. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. BACKGROUND)): To tackle the challenge, one of the most important bottlenecks lies on the difficulty in getting high-quality perception data when training the policy in conventional simulators [10], [11].

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Autonomous visual navigation is an essential element in robot autonomy.
- **p. 1 / Abstract - extractive PDF cue:** Reinforcement learning (RL) offers a promising policy training paradigm.
- **p. 1 / Abstract - extractive PDF cue:** However, existing RL methods suffer from high sample complexity, poor sim-to-real transfer, and limited runtime adaptability.
- **p. 1 / Abstract - extractive PDF cue:** These problems are particularly challenging for drones, with complex nonlinear and unstable dynamics, and strong dynamic coupling between control and perception.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose a novel framework that integrates 3D Gaussian Splatting (3DGS) with differentiable deep reinforcement learning (DDRL) to train vision-based drone navigation ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To tackle the challenge, one of the most important bottlenecks lies on the difficulty in getting high-quality perception data when training the policy in conventional ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, the integration of these different modules has many issues, including high system complexity and computational overhead, communication latency between modules, multiple points of failure, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To tackle the challenge, one of the most important bottlenecks lies on the difficulty in getting high-quality perception data when training the ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The policy transfers zero-shot to drone hardware and adapts to new navigation task instances at runtime. directly map sensor inputs to control ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | policy, transfers, zero-shot, drone, hardware, adapts, navigation, task, instances, runtime | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Differentiable, simulation, allows, backpropagation, gradient, through, states, actions | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: policy, transfers, zero-shot, drone, hardware, adapts, navigation, task, instances, runtime | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (II. BACKGROUND) |
| Decision / output variable | path/waypoint/velocity; body terms: main, contributions, introduce, simulator, training, robot, vision-based, control | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Simulator, Setting, Differentiable, Quadrotor, Dynamics, Simulation, implemented, parallelized | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, the integration of these different modules has many issues, including high system complexity and computational overhead, communication latency between modules, multiple points of failure, ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** based on imitation learning, which requires a large amount of high-quality expert pilot data, long training time, and suffers from a lack of generalization to ...
- **p. 2 / II. BACKGROUND - extractive PDF cue:** (1) 2) Short-Horizon Actor-Critic: The Short-Horizon ActorCritic method (SHAC) [30] was introduced to address the challenges associated with gradient-based policy learning.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol)): Our main contributions are: • We introduce a simulator for training robot vision-based control policies by integrating 3DGS for high-fidelity visuals with a differentiable dynamics model to enable end-to-end gradient ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To achieve the goal of visual-motor navigation, we propose a novel approach that leverages 3DGS in conjunction with DDRL, using SHAC-like training algorithm and a ...
- **p. 3 / III. METHOD - extractive PDF cue:** (10) The state st = [pt, vt, qt, ωt] consists of position, velocity, orientation (quaternion), and angular velocity.
- **p. 3 / III. METHOD - extractive PDF cue:** At its core, we introduce GRaD-Nav, a DDRL algorithm tailored for end-to-end visual navigation, improving sample efficiency over prior methods.
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** icy: Beyond training a single policy for a long horizon trajectory, our method can also train generalizable policies that can adapt to different surrounding environments ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | All of the failure cases without CENet on two trajectories "crash" due to unsuccessful obstacle avoidance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Future work includes (i) multi-task training with language input, (ii) improving generalization via stronger backbones and diverse environments, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As visual perception is our navigation policy's major sensor input, it is not surprising that the policy without ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. BACKGROUND), interface p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), objective p. 3 (III. METHOD), p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
