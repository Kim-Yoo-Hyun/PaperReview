# Problem - Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7BLXhmWvwF; PDF retrieval source: https://arxiv.org/pdf/2502.07005. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND)): They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body manipulation with diverse objects to more challenging tasks ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Manipulating objects with varying geometries and deformable objects is a major challenge in robotics.
- **p. 1 / ABSTRACT - extractive PDF cue:** Tasks such as insertion with different objects or cloth hanging require precise control and effective modelling of complex dynamics.
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we frame this problem through the lens of a heterogeneous graph that comprises smaller sub-graphs, such as actuators and objects, accompanied by ...
- **p. 1 / ABSTRACT - extractive PDF cue:** This graph representation serves as a unified structure for both rigid and deformable objects tasks, and can be extended further to tasks comprising multiple actuators.
- **p. 1 / ABSTRACT - extractive PDF cue:** To evaluate this setup, we present a novel and challenging reinforcement learning benchmark, including rigid insertion of diverse objects, as well as rope and cloth ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body manipulation with diverse ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Unlike supervised imitation, training policies with reinforcement learning presents additional challenges, particularly due to the need for high-frequency data collection and efficient adaptation to new ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | Right: Overview of Heterogeneous Equivariant Policy (HEPi), consisting of multiple Equivariant Message Passing Networks (EMPNs) process the graph, and the outputs are ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | Right, Overview, Heterogeneous, Equivariant, Policy, HEPi, consisting, multiple, Message, Passing | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | exception, recent, Equibot, Yang, where, policy, outputs, velocity | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: Right, Overview, Heterogeneous, Equivariant, Policy, HEPi, consisting, multiple, Message, Passing | p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION) |
| Decision / output variable | normalized sample or downstream action; body terms: evaluate, future, advancements, direction, novel, suite, seven, tasks | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Trust-Region, Projection, Layers, Standard, on-policy, reinforcement, learning, approaches | p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 3 (3 METHODOLOGY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 6 (3 METHODOLOGY) |
| Success / guarantee | cross-domain transfer and task performance | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Unlike supervised imitation, training policies with reinforcement learning presents additional challenges, particularly due to the need for high-frequency data collection and efficient adaptation to new ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** In this paper, we frame manipulation problems as heterogeneous graphs.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Using Equivariant Message Passing Networks (EMPNs), they learn policies that generalize to different poses by leveraging the geometric structure of the scene.
- **p. 3 / 2 BACKGROUND - extractive PDF cue:** This allows leveraging symmetries to reduce the complexity of learning, potentially improving sample efficiency and generalization, as it results in a group-structured MDP homomorphism (Van ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY)): To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., 2023) to utilize its GPU-based ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** The architecture's equivariance allows generalizing between poses and its heterogeneity enables us to include and exploit knowledge about the scene as well as the unactuated ...
- **p. 3 / 3 METHODOLOGY - extractive PDF cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 5 / 3 METHODOLOGY - extractive PDF cue:** For actuator nodes, the output consists of both a scalar c and a vector vout, where the final output vector is computed as vout = ...
- **p. 4 / 3 METHODOLOGY - extractive PDF cue:** Our approach captures these roles by first processing local information within the object and actuator clusters and then aggregating it globally to the actuators via ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | This limitation could be addressed by integrating state-of-the-art computer vision techniques to extract keypoints from cameras (Tumanyan et ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | As shown in Figure 5 (left), HEPi maintains high performance across resolutions with only mild degradation at higher ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Overall, as depicted in Figure 8, in tasks requiring high exploration such as cloth-hanging-3D, PPO struggles to maintain ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (3 METHODOLOGY). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 BACKGROUND), interface p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), objective p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 6 (3 METHODOLOGY), p. 3 (3 METHODOLOGY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
