# VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2307.05973.
> PDF retrieval source: https://arxiv.org/pdf/2307.05973. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: LLM, VLM, Planning, Robotics
- Official paper: https://arxiv.org/abs/2307.05973
- Full-text retrieval: https://arxiv.org/pdf/2307.05973
- Code/Project: https://voxposer.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM or a planner, and ...를 문제로 두고, We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists of a desired 6-DoF end-effector pose, end-effector ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning ...
- **p. 1 / Abstract - extractive body cue:** Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck.
- **p. 1 / Abstract - extractive body cue:** In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction.
- **p. 1 / Abstract - extractive body cue:** More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into ...
- **p. 2 / 1 Introduction - extractive body cue:** However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked ...
- **p. 2 / 1 Introduction - extractive body cue:** In addressing this challenge, we first note that it is impractical for LLMs to directly output control actions in text, which are typically driven by ...

## Core Idea

- **p. 4 / 3 Method - extractive body cue:** We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather than relying on robotic data that are often of limited amount or variability, the method leverages LLMs for open-world reasoning and VLMs for generalizable ...
- **p. 3 / 3 Method - extractive body cue:** The central problem 2Note that the decomposition and sequencing of these sub-tasks are also done by LLMs in this work, though we do not investigate ...
- **p. 6 / 3 Method - extractive body cue:** We further demonstrate how VoxPoser enables efficient learning of more challenging tasks (Sec.
- **p. 3 / 1 Introduction - extractive body cue:** Despite the promising signs, hand-designed motion primitives are still required, and while LLMs are shown to be capable of composing sequential policy logic, it remains ...
- **p. 5 / 3 Method - extractive body cue:** Consider the standard setup where a robot interleaves between 1) collecting environment transition data (ot, at, ot+1), where ot is the environment observation at time ...
- **p. 8 / 3 Method - extractive body cue:** We conduct experiments in simulation where we have access to ground-truth perception and dynamics model (i.e., the simulator). . "Dynamics error" refers to errors made ...
- **p. 5 / 3 Method - extractive body cue:** We use simple zeroth-order optimization by randomly sampling trajectories and scoring them with the proposed objective.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | On top of value map LMPs, we define two high-level LMPs to orchestrate their behaviors: planner takes user instruction L as input (e.g., "open drawer") and outputs a sequence of sub-tasks ℓ1:N, ... | image/video, language instruction, proprioception과 history | p. 6 (3 Method), p. 4 (3 Method) |
| State/latent | value, LMPs, define, high-level, orchestrate, behaviors, planner, takes, user, instruction, input, open | language-grounded task state와 action-policy context | p. 6 (3 Method), p. 4 (3 Method), p. 6 (3 Method) |
| Output/action | Given the RGB-D observation of the environment and a language instruction, LLMs generate code, which interacts with VLMs, to produce a sequence of 3D affordance maps and constraint maps (collectively referred to ... | continuous action, pose 또는 action chunk | p. 4 (3 Method), p. 6 (3 Method), p. 3 (3 Method) |
| Objective/outcome | Note that while these additional trajectory parametrizations are not mapped to a real-valued "cost", they can also be factored in the optimization procedure (Equation 1) to parametrize the trajectories. | instruction following, task success, generalization과 latency | p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 4 / 3 Method - extractive body cue:** We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists ...
- **p. 2 / 1 Introduction - extractive body cue:** Rather than relying on robotic data that are often of limited amount or variability, the method leverages LLMs for open-world reasoning and VLMs for generalizable ...
- **p. 3 / 3 Method - extractive body cue:** The central problem 2Note that the decomposition and sequencing of these sub-tasks are also done by LLMs in this work, though we do not investigate ...
- **p. 6 / 3 Method - extractive body cue:** We further demonstrate how VoxPoser enables efficient learning of more challenging tasks (Sec.
- **p. 3 / 1 Introduction - extractive body cue:** Despite the promising signs, hand-designed motion primitives are still required, and while LLMs are shown to be capable of composing sequential policy logic, it remains ...
- **p. 7 / 3 Method - extractive body cue:** VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but takes ...
- **p. 22 / A.5.2 Full Results on Simulated Environments - extractive body cue:** Each entry represents success rate averaged across 20 episodes.
- **p. 7 / 3 Method - extractive body cue:** We find that VoxPoser can effectively synthesize robot trajectories for everyday manipulation tasks with a high average success rate.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (3 Method), p. 22 (A.5.2 Full Results on Simulated Environments) |
| Embodiment/environment | 4.2 Generalization to Unseen Instructions and Attributes To provide rigorous quantitative evaluations on generalization, we set up a simulated block-world environment that mirrors our real-world robot setup [120, 121] but features 13 ... | hardware/simulator version and reset protocol | p. 7 (3 Method), p. 18 (A.1 Code Release) |
| Dataset/benchmark | For tasks with disturbances, we apply three kinds of disturbances to the environment, which we pre-select a sequence of them at the start of the evaluation: 1) random forces applied to the ... | role, split, size and leakage | p. 7 (3 Method), p. 18 (A.1 Code Release), p. 20 (A.4 Real-World Environment Setup), p. 18 (A.2 Emergent Behavioral Capabilities) |
| Metric | Each entry represents success rate averaged across 20 episodes. | definition, denominator, direction and uncertainty | p. 22 (A.5.2 Full Results on Simulated Environments), p. 7 (3 Method), p. 7 (3 Method) |
| Baseline/ablation | VoxPoser outperforms both baselines across 13 tasks from two categories on both seen and unseen tasks and maintains similar success rates. smoother trajectories but takes more time for optimization. | fair input/data/compute/action matching | p. 7 (3 Method), p. 7 (3 Method), p. 20 (A.4 Real-World Environment Setup) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 3 Method - extractive body cue:** 5 Conclusion, Limitations, & Future Works In this work, we present VOXPOSER, a general framework for extracting affordances and constraints, grounded in 3D perceptual space, ...
- **p. 8 / 3 Method - extractive body cue:** Despite compelling results, VoxPoser has several limitations.
- **p. 18 / A.2 Emergent Behavioral Capabilities - extractive body cue:** This serves as a lighthearted example that language models can exhibit limitations similar to human reasoning.
- **p. 7 / 3 Method - extractive body cue:** VoxPoser performs everyday manipulation tasks with high success and is more robust to disturbances than the baseline using action primitives.
- **p. 7 / 3 Method - extractive body cue:** Due to fast replanning capabilities, it is also robust to external disturbances, such as moving targets/obstacles and pulling the drawer open after it has been ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VOXPOSER. Given the RGB-D observation of the environment and a language in- struction, LLMs generate code, which interacts with VLMs, to ...
- **p. 20 / A.4 Real-World Environment Setup - extractive body cue:** For each task, we evaluate each method on two settings: without and with disturbances.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM or a planner, and ...를 문제로 두고, We represent τ r i as a sequence of dense end-effector waypoints to be executed by an Operational Space Controller [117], where each waypoint consists of a desired 6-DoF end-effector pose, end-effector ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 8 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, to enable physical interactions with the environment, existing approaches typically rely on a repertoire of pre-defined motion primitives (i.e., skills) that may be invoked by an LLM or a ... (p. 2, 1 Introduction).
- **Actual contribution:** Rather than relying on robotic data that are often of limited amount or variability, the method leverages LLMs for open-world reasoning and VLMs for generalizable visual grounding in a model-based ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 4: Full experimental results in simulation on seen tasks and unseen tasks. "SA" indicates seen attributes and "UA" indicates unseen attributes. Each entry represents success rate averaged across 20 ... (p. 22, Figure/Table caption).
- **Explicit failure boundary:** 5 Conclusion, Limitations, & Future Works In this work, we present VOXPOSER, a general framework for extracting affordances and constraints, grounded in 3D perceptual space, from LLMs and VLMs for ... (p. 8, 3 Method).
