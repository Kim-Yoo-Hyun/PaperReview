# OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=oL1WEZQal8.
> PDF retrieval source: https://arxiv.org/pdf/2406.08858. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris M. Kitani, Changliu Liu, Guanya Shi
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body teleoperation, loco-manipulation, Imitation Learning
- Official paper: https://proceedings.mlr.press/v270/he25b.html
- Full-text retrieval: https://arxiv.org/pdf/2406.08858
- Code/Project: https://omni.human2humanoid.com/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, due to the delay and inaccuracy of RGB-based pose estimation and the requirement for global linear velocity estimation, H2O [3] requires MoCap during test time, only supports simple mobility tasks, and ...를 문제로 두고, In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with a universal interface that enables versatile human ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
- **p. 1 / Abstract - extractive body cue:** Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using ...
- **p. 1 / Abstract - extractive body cue:** OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4o.
- **p. 1 / Abstract - extractive body cue:** OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting ...
- **p. 1 / Abstract - extractive body cue:** We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input ...
- **p. 3 / 1 Introduction - extractive body cue:** However, due to the delay and inaccuracy of RGB-based pose estimation and the requirement for global linear velocity estimation, H2O [3] requires MoCap during test ...
- **p. 2 / 1 Introduction - extractive body cue:** Controlling humanoid robots is a long-standing robotic problem due to their high degree-of-freedom (DoF) and lack of self-stabilization [16, 17].

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose OmniH2O, a learning-based system for whole-body humanoid teleoperation and autonomy.
- **p. 4 / 1 Introduction - extractive body cue:** To encourage standing still and taking large steps during locomotion, we propose a key reward function max feet height for each step.
- **p. 3 / 1 Introduction - extractive body cue:** By contrast, OmniH2O enables high-precision dexterous loco-manipulation indoors and in the wild.
- **p. 7 / 1 Introduction - extractive body cue:** By linking πOmniH2O with a pretrained text to motion generative model (MDM) [57], it enables controlling the humanoid via verbal instructions.
- **p. 4 / 1 Introduction - extractive body cue:** To tackle this issue, We first train a teacher policy that uses privileged state information and then distill it to a student policy with limited ...
- **p. 8 / 1 Introduction - extractive body cue:** We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of actions ...
- **p. 8 / 1 Introduction - extractive body cue:** We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We design our learning from demonstration policy to be πLfD(ˆpSparse-lfd t:t+ϕ /It), where πLfD outputs ϕ frames of motion goals given the image input It. | proprioception, reference pose/motion, visual or language command | p. 8 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | design, learning, demonstration, policy, LfD, pSparse-lfd, where, outputs, frames, motion, goals, given | whole-body pose, balance/contact state와 skill/mode | p. 8 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction) |
| Output/action | 원문 대조: 보상은 proprioception, goal state, action의 함수 R(s_t^p,s_t^g,a_t)이다. Action은 목표 관절각을 지정하고 PD controller가 구동하며, PPO로 motion imitation policy를 학습한다. ([PDF p. 3](https://arxiv.org/pdf/2406.08858#page=3), §3 Problem Formulation) | 목표 관절각 → PD controller | [PDF p. 3](https://arxiv.org/pdf/2406.08858#page=3), §3 Problem Formulation |
| Objective/outcome | We apply the Proximal Policy Optimization algorithm (PPO) [48] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i . | tracking, balance, skill/task success와 recovery | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose OmniH2O, a learning-based system for whole-body humanoid teleoperation and autonomy.
- **p. 4 / 1 Introduction - extractive body cue:** To encourage standing still and taking large steps during locomotion, we propose a key reward function max feet height for each step.
- **p. 3 / 1 Introduction - extractive body cue:** By contrast, OmniH2O enables high-precision dexterous loco-manipulation indoors and in the wild.
- **p. 7 / 1 Introduction - extractive body cue:** By linking πOmniH2O with a pretrained text to motion generative model (MDM) [57], it enables controlling the humanoid via verbal instructions.
- **p. 8 / 1 Introduction - extractive body cue:** We draw two key conclusions: (1) The Diffusion Policy significantly outperforms vanilla BC with ResNet; (2) In our LfD training, predicting a sequence of actions ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows that ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 15: Reward components and weights: penalty rewards for preventing undesired behaviors for sim-to-real transfer, regularization to refine motion, and task reward to achieve successful ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (1 Introduction), p. 7 (Figure/Table caption) |
| Embodiment/environment | We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising Diffusion Probabilistic Model [59] (DP-DDPM) and Denoising ... | hardware/simulator version and reset protocol | p. 8 (1 Introduction), p. 8 (1 Introduction) |
| Dataset/benchmark | We benchmark a variety of imitation learning algorithms on four tasks in our collected dataset (shown in Figure 7), including Diffusion Policy [58] with Denoising Diffusion Probabilistic Model [59] (DP-DDPM) and Denoising ... | role, split, size and leakage | p. 8 (1 Introduction), p. 8 (1 Introduction) |
| Metric | To evaluate πLfD, we report the average MSE loss and the success rate in Table 3, where we average the metrics across all tasks. | definition, denominator, direction and uncertainty | p. 8 (1 Introduction), p. 8 (1 Introduction), p. 21 (Figure/Table caption) |
| Baseline/ablation | Figure 8: The illustration of using ZED camera VIO module, and the comparison of the velocity estimation of VIO with neural state estimators. H Ablation on Dataset Motion Distribution The ablation study ... | fair input/data/compute/action matching | p. 22 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (1 Introduction) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 1 Introduction - extractive body cue:** Another limitation is safety; although the OmniH2O policy has shown great robustness, we do not have guarantees or safety checks for extreme disturbances or out-of-distribution ...
- **p. 8 / 1 Introduction - extractive body cue:** 5 Limitations and Future Work Summary.
- **p. 6 / 1 Introduction - extractive body cue:** 2 Unable to finish the real-world test due to falling on the ground.
- **p. 7 / 1 Introduction - extractive body cue:** OmniH2O demonstrates great robustness under disturbances and unstructured terrains.
- **p. 7 / 1 Introduction - extractive body cue:** (a) Disturbances (b) Outdoor Terrains Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains.
- **p. 6 / 1 Introduction - extractive body cue:** In Table 1(d), we find that linear velocity information does not boost performance in simulation, but it introduces significant challenges in real-world deployment (details illustrated ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 16: Here we describe the range of dynamics randomization for simulated dynamics randomization, ex- ternal perturbation, and terrain, which are important for sim-to-real transfer, ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, due to the delay and inaccuracy of RGB-based pose estimation and the requirement for global linear velocity estimation, H2O [3] requires MoCap during test time, only supports simple mobility tasks, and ...를 문제로 두고, In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with a universal interface that enables versatile human ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Controlling humanoid robots is a long-standing robotic problem due to their high degree-of-freedom (DoF) and lack of self-stabilization [16, 17]. (p. 2, 1 Introduction).
- **Actual contribution:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with a universal interface that enables ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 5: OmniH2O shows superior robustness against human strikes and different outdoor terrains. History Steps and Architecture. Real-world evaluation in Table 2(b) also shows that our choice of 25 steps ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** Another limitation is safety; although the OmniH2O policy has shown great robustness, we do not have guarantees or safety checks for extreme disturbances or out-of-distribution motion goals (e.g., large discontinuity ... (p. 8, 1 Introduction).
