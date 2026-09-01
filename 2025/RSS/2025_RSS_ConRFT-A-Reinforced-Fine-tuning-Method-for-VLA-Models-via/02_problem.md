# Problem - ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p019.html; PDF retrieval source: https://arxiv.org/pdf/2502.05450. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based ...
- **p. 1 / Abstract - extractive body cue:** In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating.
- **p. 1 / Abstract - extractive body cue:** In the online stage, the VLA model is further finetuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In the subsequent online stage, we solve two challenges of sample efficiency and real-world safety requirements by exploiting task-specific rewards with CPQL [18] under human ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | To address these issues, we formulate each robotic task as a Markov Decision Process (MDP), where the goal of RL is to ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | address, issues, formulate, robotic, task, Markov, Decision, Process, MDP, where | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | coupling, VLA, policy, learned, Q-function, RFT, allows, model | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: address, issues, formulate, robotic, task, Markov, Decision, Process, MDP, where | p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD), p. 2 (III. PROBLEM SETUP AND PRELIMINARIES) |
| Decision / output variable | action, pose, option or chunk a; body terms: Motivated, insights, CPQL, unified, training, objective, integrates, supervised | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (IV. METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: loss, directly, minimizes, difference, between, actions, generated, policy | p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 5 (IV. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 2 (IV. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), p. 6 (V. EXPERIMENT AND RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** In the subsequent online stage, we solve two challenges of sample efficiency and real-world safety requirements by exploiting task-specific rewards with CPQL [18] under human ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD)): Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** To leverage the benefits of RL-based techniques for efficiently fine-tuning VLA models with online interaction data, we propose a reinforced fine-tuning (RFT) approach consisting of ...
- **p. 2 / IV. METHOD - extractive body cue:** The proposed pipline ConRFT consists of two stages: offline fine-tuning followed by online fine-tuning to optimize robotic policies, as shown in Fig.
- **p. 3 / IV. METHOD - extractive body cue:** To address this issue, we propose augmenting the offline training process by incorporating a BC loss.
- **p. 3 / IV. METHOD - extractive body cue:** Motivated by combining the BC loss with Q guidance under a consistency-based objective [18], we introduce Cal-ConRFT in the offline stage.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | While HG-DAgger leverages human corrections to fine-tune the VLA model through supervised learning, it fails to achieve significant ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | They also show the limitations of supervised methods in handling sub-optimal data and efficient policy exploration. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD), p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD), p. 2 (III. PROBLEM SETUP AND PRELIMINARIES), p. 4 (IV. METHOD), objective p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 5 (IV. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
