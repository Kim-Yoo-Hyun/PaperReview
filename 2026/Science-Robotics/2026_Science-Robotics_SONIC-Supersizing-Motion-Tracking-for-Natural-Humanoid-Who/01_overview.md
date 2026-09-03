# SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://research.nvidia.com/labs/dair/publication/sonic2026/.
> PDF retrieval source: https://research.nvidia.com/labs/dair/publication/sonic2026/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / Science Robotics
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, whole-body control, Motion Tracking, NVIDIA
- Official paper: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Full-text retrieval: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Code/Project: https://research.nvidia.com/labs/dair/publication/sonic2026/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve [7-9].를 문제로 두고, We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie S1).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Despite the rise of billion-parameter foundation models trained across thousands of graphical processing units (GPUs), similar scaling gains have not been shown for humanoid control.
- **p. 1 / Abstract - extractive body cue:** Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs.
- **p. 1 / Abstract - extractive body cue:** We show that scaling model capacity, data, and compute yields a generalist humanoid controller capable of natural, robust whole-body movements.
- **p. 1 / Abstract - extractive body cue:** We position motion tracking as a scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual ...
- **p. 1 / Abstract - extractive body cue:** We build a foundation model for motion tracking by scaling along three axes: network size (1.2M to 42M parameters), dataset volume (100M+ frames from 700 ...
- **p. 1 / 1. Introduction - extractive body cue:** These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve [7-9].
- **p. 1 / 1. Introduction - extractive body cue:** Each new capability demands redesigned rewards and objectives, making scaling up difficult.

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie S1).
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions.
- **p. 3 / 1. Introduction - extractive body cue:** Third, we provide a comprehensive evaluation demonstrating humanoid control scaling trends, zero-shot transfer to unseen motions, robust simto-real deployment on physical humanoid robots, and successful ...
- **p. 2 / 1. Introduction - extractive body cue:** SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control Figure 1: SONIC enables diverse humanoid tasks through a universal control policy that handles diverse input ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ℒrecon serves as ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Specialized encoders map heterogeneous human and robot motion inputs into a shared latent representation, which is quantized into a universal token that drives a common ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** First, a robot control decoder 𝒟𝑐transforms the universal token into motor commands that control the robot's joints. 𝒟𝑐takes as input the concatenation of the universal ...
- **p. 16 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** We used asymmetric actor-critic training [63]: the critic observes privileged simulation state (base linear velocity, full body link positions and orientations, and noise-free observations) during ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ℒrecon serves as a retargeting loss that enables learning from ... | proprioception, reference pose/motion, visual or language command | p. 15 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking) |
| State/latent | Notably, when, input, command, human, motion, encoder-decoder, acts, retargeting, pipeline, robot, recon | whole-body pose, balance/contact state와 skill/mode | p. 15 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.3. Generative Kinematic Motion Planner) |
| Output/action | The policy 𝜋outputs target joint positions 𝑎𝑡as actions, which are tracked by proportional-derivative (PD) controllers at each joint. | joint/whole-body action, motion target 또는 task trajectory | p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.3. Generative Kinematic Motion Planner), p. 16 (3.2. Universal Humanoid Motion Tracking) |
| Objective/outcome | We defined the reward as 𝑟𝑡= ℛ(𝑠p 𝑡, 𝑠g 𝑡) + 𝒫(𝑠p 𝑡, 𝑎𝑡), combining a tracking term that minimizes root and body-link pose and velocity errors (including an end-effector term on ... | tracking, balance, skill/task success와 recovery | p. 14 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Introduction - extractive body cue:** We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie S1).
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions.
- **p. 3 / 1. Introduction - extractive body cue:** Third, we provide a comprehensive evaluation demonstrating humanoid control scaling trends, zero-shot transfer to unseen motions, robust simto-real deployment on physical humanoid robots, and successful ...
- **p. 2 / 1. Introduction - extractive body cue:** SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control Figure 1: SONIC enables diverse humanoid tasks through a universal control policy that handles diverse input ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ℒrecon serves as ...
- **p. 19 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; no statistical test ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Scaling and benchmarking of SONIC for universal motion tracking. (A to C) Effect of scaling data size, model size, and compute on test-content ...
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** Scaling yielded consistent improvements on both test-content (out-of-distribution, OOD) and test-repetition: the largest model achieved 99.6% success with 23.8 mm MPJPE-L on test-content, compared to ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 19 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Embodiment/environment | 14,513 701 253 Dance 9,689 504 485 Injured 9,386 1,167 528 Action / Tool use 9,920 228 322 Others (10+ main cat.) 63,583 429 890 Table 2: Dataset split statistics and main/sub-category ... | hardware/simulator version and reset protocol | p. 13 (3.1. Humanoid Motion Dataset), p. 3 (2.1. Motion Tracking) |
| Dataset/benchmark | This comparison primarily reflects cross-dataset generalization and scaling effects rather than a fully data-matched benchmark, as the baselines were trained on different source data and retargeting pipelines than SONIC. | role, split, size and leakage | p. 13 (3.1. Humanoid Motion Dataset), p. 3 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 3 (2.1. Motion Tracking) |
| Metric | (m/s) (H) Commanded vs Achieved Ideal OpenHomie SONIC 0 1 2 3 4 5 Commanded Velocity (m/s) 0 20 40 60 80 100 Survival Rate (%) (I) Stability SONIC OpenHomie 0 1 ... | definition, denominator, direction and uncertainty | p. 4 (2.1. Motion Tracking), p. 4 (2.1. Motion Tracking), p. 11 (2.5. Foundation-Model-Driven Loco-manipulation) |
| Baseline/ablation | We compared against state-of-the-art trackers: GMT [33], Any2Track [30], and BeyondMimic [29]. | fair input/data/compute/action matching | p. 5 (2.1. Motion Tracking), p. 5 (2.1. Motion Tracking), p. 3 (2.1. Motion Tracking) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 2.1. Motion Tracking - extractive body cue:** Our metric, similar to [29], captured the physically meaningful failure modes such as falling.
- **p. 12 / 2.6. Discussion - extractive body cue:** Limitations include the lack of formal treatment of safety and energy efficiency for extended deployments.
- **p. 12 / 2.6. Discussion - extractive body cue:** It also contrasts with task-specific reward engineering (for example, locomotion controllers such as OpenHomie [13]), where each behavior requires a tailored objective that does not ...
- **p. 13 / 3.1. Humanoid Motion Dataset - extractive body cue:** After retargeting to the Unitree G1 using General Motion Retargeting (GMR) [54] and PyRoki [55], we filtered out physically implausible motions (such as stair climbing ...
- **p. 5 / 2.1. Motion Tracking - extractive body cue:** Visualizations of out-of-distribution test motions, including successful and failed tracking cases, are provided in the Supplementary Materials (Fig.
- **p. 3 / 2.1. Motion Tracking - extractive body cue:** The second, testrepetition (9,395 clips, 12 hours), evaluated robustness to new performances and repetitions of known motion types.
- **p. 6 / 2.2. Interactive Motion Control - extractive body cue:** In this section, we demonstrated the scalability and robustness of SONIC in whole-body, real-time interactive control tasks (Movie S2).

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve [7-9].를 문제로 두고, We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie S1).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (39 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Each new capability demands redesigned rewards and objectives, making scaling up difficult. (p. 1, 1. Introduction).
- **Actual contribution:** In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions. (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 3: Ablation studies. SR denotes success rate. Each entry reports a single evaluation per configuration on the full test split (descriptive; no statistical test applied). (A) FSQ outperforms VQ-VAE ... (p. 19, Figure/Table caption).
- **Explicit failure boundary:** Our metric, similar to [29], captured the physically meaningful failure modes such as falling. (p. 5, 2.1. Motion Tracking).
