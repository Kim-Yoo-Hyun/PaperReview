# Problem - Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, and the complexity of establishing standardized benchmark ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We present Habitat 3.0: a simulation platform for studying collaborative humanrobot tasks in home environments.
- **p. 1 / ABSTRACT - extractive body cue:** Habitat 3.0 offers contributions across three dimensions: (1) Accurate humanoid1 simulation: addressing challenges in modeling complex deformable bodies and diversity in appearance and motion, all ...
- **p. 1 / ABSTRACT - extractive body cue:** (2) Human-in-the-loop infrastructure: enabling real human interaction with simulated robots via mouse/keyboard or a VR interface, facilitating evaluation of robot policies with human input.
- **p. 1 / ABSTRACT - extractive body cue:** (3) Collaborative tasks: studying two collaborative tasks, Social Navigation and Social Rearrangement.
- **p. 1 / ABSTRACT - extractive body cue:** Social Navigation investigates a robot's ability to locate and follow humanoid avatars in unseen environments, whereas Social Rearrangement addresses collaboration between a humanoid and robot ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, and the complexity ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A simulation platform can overcome these challenges; however, the development of a collaborative human-robot simulation platform also comes with its own complexities.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Training and testing such social agents on hardware with real humans poses inherent challenges, including safety concerns, scalability limitations, substantial cost implications, ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | The policy uses a ResNet-18 (He et al., 2016) visual encoder to embed the 256 × 256 depth input image into a ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | policy, uses, ResNet-18, visual, encoder, embed, depth, input, image, dimension | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | LSTM, output, then, action, value, prediction, network, Additionally | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: policy, uses, ResNet-18, visual, encoder, embed, depth, input, image, dimension | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 2 (1 INTRODUCTION), p. 17 (A.2 SOCIAL REARRANGEMENT) |
| Decision / output variable | method trajectory/action; body terms: Social, tasks, Aiming, reproducible, standardized, benchmarking, present, collaborative | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: PPO, minibatches, epoch, update, entropy, loss, clip, gradient | p. 17 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Success / guarantee | comparable score and protocol validity | p. 25 (Figure/Table caption), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** A simulation platform can overcome these challenges; however, the development of a collaborative human-robot simulation platform also comes with its own complexities.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Today's embodied AI agents are largely hermits - existing within and navigating through virtual worlds as solitary occupants (Batra et al., 2020; Anderson et al., ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We conduct an in-depth study of learned and heuristic baselines on both tasks, with a focus on generalization to new scenes, layouts and collaboration partners.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT)): Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Habitat 3.0 - a simulator that supports both humanoid avatars and robots for the study of collaborative human-robot tasks in ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework is open-sourced, for more details see Appendix A.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 17 | Since the Spot robot has a long body shape and cannot be represented by a single cylinder, we ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Hence the high-level policy is not robust to low-level execution failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | These skills do not use privileged information, and hence are more prone to failures in the diverse set ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | During training, the episode terminates if there is a collision between the humanoid and the robot. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 17 (A.2 SOCIAL REARRANGEMENT), p. 2 (1 INTRODUCTION), p. 17 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 17 (A.2 SOCIAL REARRANGEMENT), p. 2 (1 INTRODUCTION), p. 17 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT), objective p. 17 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
