# Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.13705.
> PDF retrieval source: https://arxiv.org/pdf/2304.13705. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, bimanual manipulation, Imitation Learning, action chunking
- Official paper: https://arxiv.org/abs/2304.13705
- Full-text retrieval: https://arxiv.org/pdf/2304.13705
- Code/Project: https://tonyzhaozh.github.io/aloha/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced.를 문제로 두고, The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact ...
- **p. 1 / Abstract - extractive body cue:** Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up.
- **p. 1 / Abstract - extractive body cue:** Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks?
- **p. 1 / Abstract - extractive body cue:** We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface.
- **p. 1 / Abstract - extractive body cue:** Imitation learning, however, presents its own challenges, particularly in highprecision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Millimeters of error would lead to task failure.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To further improve the smoothness of the policy, we propose temporal ensembling, which queries the policy more frequently and averages across the overlapping action chunks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we seek to develop a low-cost system for fine manipulation that is, in contrast, accessible and reproducible.
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We therefore develop a novel algorithm, Action Chunking with Transformers (ACT), to leverage the data collected by ALOHA.
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** Implementing ACT We implement the CVAE encoder and decoder with transformers, as transformers are designed for both synthesizing information across a sequence and generating new ...
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use ResNet image encoders, a transformer encoder, and a transformer decoder to implement the CVAE decoder.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use L1 loss for reconstruction instead of the more common L2 loss: we noted that L1 loss leads to more precise modeling of the ...
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Thus with action chunking, the policy outputs a k × 14 tensor given the current observation. | RGB-D/point cloud, object state와 contact/task observation | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| State/latent | Thus, action, chunking, policy, outputs, tensor, given, current, observation, CVAE, decoder, takes | object geometry, affordance, contact mode 또는 end-effector state | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 1 (I. INTRODUCTION) |
| Output/action | The CVAE decoder (i.e. the policy) takes the current observations and z as the input, and predicts the next k actions (Figure 4 right). | grasp, pose, force 또는 end-effector trajectory | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective/outcome | The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which has two terms: a reconstruction loss and ... | task completion, contact success, pose/force error와 generalization | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To further improve the smoothness of the policy, we propose temporal ensembling, which queries the policy more frequently and averages across the overlapping action chunks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we seek to develop a low-cost system for fine manipulation that is, in contrast, accessible and reproducible.
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We therefore develop a novel algorithm, Action Chunking with Transformers (ACT), to leverage the data collected by ALOHA.
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** Implementing ACT We implement the CVAE encoder and decoder with transformers, as transformers are designed for both synthesizing information across a sequence and generating new ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each task.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on the ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** Our method ACT reaches 84% success for Cup Open, 20% for Thread Velcro, 64% for Prep Tape and 92% for Put On Shoe, again outperforming ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (V. EXPERIMENTS), p. 10 (Figure/Table caption) |
| Embodiment/environment | For all 8 tasks, the initial placement of the objects is either varied randomly along the 15cm white reference line (real-world tasks), or uniformly in 2D regions (simulated tasks). | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Dataset/benchmark | To teleoperate in simulation, we use the "leader robots" of ALOHA to control the simulated robot, with the operator looking at the real-time renderings of the environment on the monitor. | role, split, size and leakage | p. 6 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | Open Cup (real) Thread Velcro (real) Prep Tape (real) Put On Shoe (real) Tip Over Grasp Open Lid Lift Grasp Insert Grasp Cut Handover Hang Lift Insert Support Secure BeT 12 0 ... | definition, denominator, direction and uncertainty | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |
| Baseline/ablation | ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each task. | fair input/data/compute/action matching | p. 9 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. EXPERIMENTS - extractive body cue:** Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result in collisions and task failure.
- **p. 9 / V. EXPERIMENTS - extractive body cue:** The failure modes we observe are 1) at stage 2, the right arm closes its gripper too early and fails to grasp the tail of ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Because of the cup's small size, the grippers cannot grasp the body of the cup by just approaching it from the side.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The left arm then lays the tape segment flat on the surface of the box while the right gripper pushes down on the tape to ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 10: Image observation examples for 5 real-world tasks. The 4 columns are [top camera, front camera, left wrist camera, right wrist camera] respectively. We ...
- **p. 9 / VI. ABLATIONS - extractive body cue:** In contrast, VINN retrieves ground-truth actions from the dataset and does not suffer from this issue.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, low-cost hardware is inevitably less precise than high-end platforms, making the sensing and planning challenge more pronounced.를 문제로 두고, The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
