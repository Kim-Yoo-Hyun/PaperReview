# Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=s3FTX4Ay55.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114017. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=s3FTX4Ay55
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114017
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 ARTICULATE-ANYTHING represents a step function improvement in quality, accuracy (8.7-12.2% to 75%), and generalizability over prior art (Chen et al., 2024; Mandi et al., 2024), overcoming previous limitations that restricted success to ...를 문제로 두고, To address this challenge, we present ARTICULATE-ANYTHING, a novel approach in automatic articulation that harnesses the power of leading foundation vision-language models (VLMs) to articulate a diverse range of objects of arbitrary ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Interactive 3D simulated objects are crucial in AR/VR, animations, and robotics, driving immersive experiences and advanced automation.
- **p. 1 / ABSTRACT - extractive body cue:** However, creating these articulated objects requires extensive human effort and expertise, limiting their broader applications.
- **p. 1 / ABSTRACT - extractive body cue:** To overcome this challenge, we present ARTICULATEANYTHING, a system that automates the articulation of diverse, complex objects from many input modalities, including text, images, and ...
- **p. 1 / ABSTRACT - extractive body cue:** ARTICULATEANYTHING leverages vision-language models (VLMs) to generate code that can be compiled into an interactable digital twin for use in standard 3D simulators.
- **p. 1 / ABSTRACT - extractive body cue:** Our system exploits existing 3D asset datasets via a mesh retrieval mechanism, along with an actor-critic system that iteratively proposes, evaluates, and refines solutions for ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ARTICULATE-ANYTHING represents a step function improvement in quality, accuracy (8.7-12.2% to 75%), and generalizability over prior art (Chen et al., 2024; Mandi et al., 2024), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, a critical bottleneck in this research direction persists: the immense human labor required to construct realistic, interactable environments for these agents to learn within.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this challenge, we present ARTICULATE-ANYTHING, a novel approach in automatic articulation that harnesses the power of leading foundation vision-language models (VLMs) to articulate ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ARTICULATE-ANYTHING: We present a vision-language actor-critic system that accurately articulates objects from diverse input modalities, including texts, images, and videos.
- **p. 16 / A.3 ROBOTIC TRAINING DETAILS - extractive body cue:** We train a Franka arm to perform four robotic manipulation tasks in the Robosuite simulator using PPO and our generated assets.The policy outputs joint and ...
- **p. 16 / A.3 ROBOTIC TRAINING DETAILS - extractive body cue:** We randomize physics (friction, damping, frictionloss ect), objects' scales and poses to obtain robust policies.
- **p. 23 / A.7 MESH RECONSTRUCTION - extractive body cue:** Chamfer distance is included (lower is better) for different models for in-the-wild results.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Beyond robotics, the flexibility of ARTICULATE-ANYTHING's inputs married with its high-quality outputs puts automatic generation of rich, high-quality, and diverse virtual environments within reach with broad-reaching applications to 3D ... | image/video, language instruction, proprioception과 history | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | Beyond, robotics, flexibility, ARTICULATE-ANYTHING, inputs, married, high-quality, outputs, puts, automatic, generation, rich | language-grounded task state와 action-policy context | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.3 ROBOTIC TRAINING DETAILS) |
| Output/action | ARTICULATE-ANYTHING: We present a vision-language actor-critic system that accurately articulates objects from diverse input modalities, including texts, images, and videos. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 16 (A.3 ROBOTIC TRAINING DETAILS), p. 16 (A.3 ROBOTIC TRAINING DETAILS) |
| Objective/outcome | We randomize physics (friction, damping, frictionloss ect), objects' scales and poses to obtain robust policies. | instruction following, task success, generalization과 latency | p. 16 (A.3 ROBOTIC TRAINING DETAILS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this challenge, we present ARTICULATE-ANYTHING, a novel approach in automatic articulation that harnesses the power of leading foundation vision-language models (VLMs) to articulate ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ARTICULATE-ANYTHING: We present a vision-language actor-critic system that accurately articulates objects from diverse input modalities, including texts, images, and videos.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 10: In-context learning. ARTICULATE-ANYTHING improves with the number of prompting examples, demonstrating in-context learning. The zero-shot performance (0 example) is included. We conduct this ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** 1 2 3 Iteration 70 80 90 100 Success Rate (%) 80.2 85.5 86.0 84.0 89.4 90.1 Link Placement Ground Truth Critic 1 2 3 ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Both policies trained via ARTICULATE-ANYTHING's and human-annotated assets achieve 100% success rate in the real world.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Evaluation Metrics: We assess performance using success rates for each task.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Our approach significantly outperforms all baselines in the joint prediction task.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Our innovations allow ARTICULATE-ANYTHING to achieve superior performance as demonstrated in Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 9 (5 EXPERIMENTS) |
| Embodiment/environment | Articulate real-world videos 1 RL training in simulation 2 Transfer to real 3 Figure 13: Robotic Application: ARTICULATE-ANYTHING can automatically generate assets given in-the-wild input videos. | hardware/simulator version and reset protocol | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Dataset/benchmark | Both methods were trained or fine-tuned on five object categories in the PartNet-Mobility dataset. | role, split, size and leakage | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Metric | In Appendix A.6, table 1 reveals the raw joint prediction errors behind the success rate of Fig. | definition, denominator, direction and uncertainty | p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Baseline/ablation | Figure 7: In-the-wild Reconstruction. We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. Green and red borders denote correct and incorrect predictions with respect to the ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 8 breaks down the failure reasons for each method.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8: Breakdown of failure percentages in all classes. In ARTICULATE-ANYTHING, incorrect link placement leads to all predicted joints being marked incorrect. For baselines, 59.1% ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 14: Joint prediction failure visualization. We visualize different types of joint failures, ranging from the most egregious, joint type, to the least, joint limit. ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Link placement: Success is determined by the pose difference between predicted and ground-truth links falling below a small threshold.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Prior works are also limited to simplified inputs as they cannot handle videos.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Baseline limitations: URDFormer consistently predicts drawer-like structures and is sensitive to minor misalignments (e.g., slightly tilted drawers).
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: In-the-wild Reconstruction. We demonstrate ARTICULATE-ANYTHING's performance input modalities compared to prior works URDFormer and Real2Code. Green and red borders denote correct and incorrect ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 ARTICULATE-ANYTHING represents a step function improvement in quality, accuracy (8.7-12.2% to 75%), and generalizability over prior art (Chen et al., 2024; Mandi et al., 2024), overcoming previous limitations that restricted success to ...를 문제로 두고, To address this challenge, we present ARTICULATE-ANYTHING, a novel approach in automatic articulation that harnesses the power of leading foundation vision-language models (VLMs) to articulate a diverse range of objects of arbitrary ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.3 ROBOTIC TRAINING DETAILS), p. 16 (A.3 ROBOTIC TRAINING DETAILS), p. 23 (A.7 MESH RECONSTRUCTION), p. 9 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
