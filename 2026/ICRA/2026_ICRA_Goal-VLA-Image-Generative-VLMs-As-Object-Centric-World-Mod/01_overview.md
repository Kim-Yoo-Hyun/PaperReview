# Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2506.23919. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2506.23919
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This generalization gap is the primary barrier hindering the practical deployment of autonomous robots in unstructured environments.를 문제로 두고, To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate goal object states, serving as the bridge ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Generalization remains a fundamental challenge in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** To tackle this challenge, recent VisionLanguage-Action (VLA) models build policies on top of VisionLanguage Models (VLMs), seeking to transfer their openworld semantic knowledge.
- **p. 1 / Abstract - extractive body cue:** However, their zero-shot capability lags significantly behind the base VLMs, as the instructionvision-action data is too limited to cover diverse scenarios, tasks, and robot embodiments.
- **p. 1 / Abstract - extractive body cue:** In this work, we present GoalVLA, a zero-shot framework that leverages Image-Generative VLMs as world models to generate desired goal states, from which the target ...
- **p. 1 / Abstract - extractive body cue:** The key insight is that object state representation is the golden interface, naturally separating a manipulation system into high-level and low-level policies.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This generalization gap is the primary barrier hindering the practical deployment of autonomous robots in unstructured environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Foundation models, pre-trained on vast datasets, have emerged as a promising direction to address this challenge.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose a decoupled architecture that leverages the VLM as an objectcentric world model.
- **p. 3 / III. METHOD - extractive body cue:** The overall workflow of our framework is illustrated conceptually in Figure 2 and detailed procedurally in Algorithm 1.
- **p. 4 / III. METHOD - extractive body cue:** This overlay is crucial as it provides an in-context visualization of the goal, which mitigates the semantic gap and enables a more robust evaluation. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These models are either developed by finetuning existing Vision-Language Models (VLMs) [7]-[9]
- **p. 3 / III. METHOD - extractive body cue:** Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure ...
- **p. 4 / III. METHOD - extractive body cue:** The Low-level Policy takes the current observation O = (I, D) and the mask M as input, then outputs a sequence of actions {a}i to ...
- **p. 4 / III. METHOD - extractive body cue:** "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure Success Depth-Anything Initial ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: procedure GOAL-VLA(O, L) Stage 1: Goal State Reasoning ... | image/video, language instruction, proprioception과 history | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| State/latent | Algorithm, Goal-VLA, Execution, Framework, Require, Initial, observation, Language, instruction, End-effector, pose, Pinit | language-grounded task state와 action-policy context | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | "Place tomato in pan" Task Description Initial Image (a) Goal State Reasoning World Model Goal Image Goal Depth Synthesized Image Reflector Failure Success Depth-Anything Initial Mask Goal Mask Segmentation (b) Spatial Grounding ... | continuous action, pose 또는 action chunk | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | Problem Formulation Given a single-view RGBD image observation O = (I ∈ RH×W ×3, D ∈RH×W ×1), and a natural language task description L , the objective is to generate an action ... | instruction following, task success, generalization과 latency | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To this end, we propose a decoupled architecture that leverages the VLM as an objectcentric world model.
- **p. 3 / III. METHOD - extractive body cue:** The overall workflow of our framework is illustrated conceptually in Figure 2 and detailed procedurally in Algorithm 1.
- **p. 4 / III. METHOD - extractive body cue:** This overlay is crucial as it provides an in-context visualization of the goal, which mitigates the semantic gap and enables a more robust evaluation. • ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These models are either developed by finetuning existing Vision-Language Models (VLMs) [7]-[9]
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** As shown in Table III, our method achieves a 60% average success rate, significantly outperforming baselines like MOKA (22.5%) and MolmoAct (27.5%).
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Starting from a 40.0% success rate for the baseline model, adding Input Enhancement provides the most significant single improvement (+27.5pp), while the Reflector alone yields ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Embodiment/environment | Q3: Can our framework generalize across diverse environments, tasks, object categories, and robot embodiments? | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Dataset/benchmark | The robot arm is fixed to a tabletop, and for each task, objects are placed in randomized | role, split, size and leakage | p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Metric | Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Baseline/ablation | In this section, we conduct comprehensive experiments and analyses to answer the following key questions: Q1: How well does our proposed method perform compared to existing baselines? | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENT - extractive body cue:** Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Failures originating from the Spatial Grounding module are the primary obstacle in several precision-demanding tasks.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Failure Cases Analysis In our real-world experiments, we observe several typical failure modes as different tasks place varying demands on each module of our framework.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Goal-VLA maps a single-view RGB-D image and a language instruction to executable manipulation actions. Our approach employs an object-centric world model to generate ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** To robustly assess performance and account for variations in object placement, each task is evaluated across 10 random seeds.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This generalization gap is the primary barrier hindering the practical deployment of autonomous robots in unstructured environments.를 문제로 두고, To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to generate goal object states, serving as the bridge ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
