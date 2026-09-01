# NaVILA: Legged Robot Vision-Language-Action Model for Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p018.html.
> PDF retrieval source: https://arxiv.org/pdf/2412.04453. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, locomotion, Navigation, legged robot, hierarchical policy, language grounding
- Official paper: https://www.roboticsproceedings.org/rss21/p018.html
- Full-text retrieval: https://arxiv.org/pdf/2412.04453
- Code/Project: https://github.com/AnjieCheng/NaVILA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 locomotion 문제를 이해하기 위해 읽는다. 본문은 We construct a height map from raw LiDAR point clouds and introduce randomization to bridge the sim-to-real gap.를 문제로 두고, To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper proposes to solve the problem of Visionand-Language Navigation with legged robots, which not only provides a flexible way for humans to command but ...
- **p. 1 / Abstract - extractive body cue:** However, it is non-trivial to translate human language ∗Equal contribution, ordered alphabetically. † Equal advising. instructions all the way to low-level leg joint actions.
- **p. 1 / Abstract - extractive body cue:** We propose NaVILA, a 2-level framework that unifies a Vision-LanguageAction model (VLA) with locomotion skills.
- **p. 1 / Abstract - extractive body cue:** Instead of directly predicting low-level actions from VLA, NaVILA first generates mid-level actions with spatial information in the form of language, (e.g., "moving forward 75cm"), ...
- **p. 1 / Abstract - extractive body cue:** NaVILA substantially arXiv:2412.04453v2 [cs.RO] 17 Feb 2025
- **p. 2 / I. INTRODUCTION - extractive body cue:** We construct a height map from raw LiDAR point clouds and introduce randomization to bridge the sim-to-real gap.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for legged robot VLN: ...
- **p. 3 / II. METHOD - extractive body cue:** VILA consists of three main components: a vision encoder, a projector, and an LLM.
- **p. 3 / II. METHOD - extractive body cue:** To address this challenge, we opt for image-based vision-language models in our approach.
- **p. 4 / II. METHOD - extractive body cue:** This flexibility allows us to enhance generalizability for navigation.
- **p. 3 / II. METHOD - extractive body cue:** VILA undergoes a 3-stage training process: first, it pre-trains a connector between the frozen LLM and vision backbones using alignment data [20]; then it pre-trains ...
- **p. 3 / II. METHOD - extractive body cue:** Our VLA model processes single-view images to produce mid-level actions in natural language, which are then converted into precise joint movements by an advanced low-level ...
- **p. 2 / II. METHOD - extractive body cue:** We first describe how we tame VLMs for high-level VLN in Sec.II-A, then outline our robot configuration and locomotion policy in Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for legged robot VLN: A VLM is finetuned to output a ... | proprioception, terrain/perception observation과 velocity command | p. 2 (I. INTRODUCTION), p. 3 (II. METHOD) |
| State/latent | Inspired, recent, progress, VLM, spatial, location, distance, reasoning, NaVILA, twolevel, framework, legged | body/contact state, foothold 또는 behavior mode | p. 2 (I. INTRODUCTION), p. 3 (II. METHOD), p. 2 (I. INTRODUCTION) |
| Output/action | Instruction Joint Positions Policy π VLA History Views Velocity Commands Proprioception Prior Actions Joint Pos. & Vel. | joint target, torque, footstep 또는 locomotion action | p. 3 (II. METHOD), p. 2 (I. INTRODUCTION), p. 5 (II. METHOD) |
| Objective/outcome | The right image shows a preprocessed height map with values clipped to sensor constraints; darker colors indicate higher heights. | velocity/progress, stability, energy와 terrain generalization | p. 5 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for legged robot VLN: ...
- **p. 3 / II. METHOD - extractive body cue:** VILA consists of three main components: a vision encoder, a projector, and an LLM.
- **p. 3 / II. METHOD - extractive body cue:** To address this challenge, we opt for image-based vision-language models in our approach.
- **p. 4 / II. METHOD - extractive body cue:** This flexibility allows us to enhance generalizability for navigation.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 - 0.67 - ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** As shown in Table II, our method significantly outperforms NaVid, the current state-of-the-art model, with a substantial 10% improvement in SR.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Error ↓ Collision Rate ↓ ROA(w/BCLoss) [68] 0.189 0.152 3.25 ROA [68] 0.161 0.152 3.09 NaVILA 0.066 0.113 0.81 the vision-based policy outperforms the blind ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |
| Embodiment/environment | To evaluate NaVILA's capabilities in scene understanding, we conduct evaluations on the ScanQA Validation benchmark, a widely used dataset for 3D Question Answering. | hardware/simulator version and reset protocol | p. 6 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Dataset/benchmark | Legged Robot Navigation Performance in Simulation High-fidelity VLN-CE-Isaac Benchmark. | role, split, size and leakage | p. 6 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS) |
| Metric | We employ the following widely used evaluation metrics for VLN tasks: Navigation Error (NE), Oracle Success Rate (OS), Success Rate (SR), Success-weighted Path Length (SPL), and normalize dynamic time wrapping (nDTW). | definition, denominator, direction and uncertainty | p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS) |
| Baseline/ablation | We also compare NaVILAs with a baseline using Oracle's low-level policy (assuming perfect command execution without realistic physics). | fair input/data/compute/action matching | p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / V. CONCLUSION AND LIMITATIONS - extractive body cue:** While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Obstacle avoidance screenshots. Locomotion policy can ensure collision-free in the face of high grass, certain transparent glass, and large objects under strong sunlight. ...
- **p. 7 / III. EXPERIMENTS - extractive body cue:** To overcome this limitation, we introduce a new benchmark VLN-CE-Isaac built on Isaac Sim.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** As shown in Table V, our low-level policy outperforms ROA in all three metrics, particularly achieving a significantly lower collision rate, demonstrating the effectiveness of ...
- **p. 9 / V. CONCLUSION AND LIMITATIONS - extractive body cue:** NaVILA generates high-level language commands while a realtime locomotion policy handles obstacle avoidance, enhancing robustness across robots.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8: Comparison between Go2 blind policy and vision policy. The blind policy failed to avoid the obstacles and got stuck. The vision policy detected ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Height map reconstruction from point cloud. (a) Go2 robot follows velocity commands while avoiding obstacles in simulation. Red dots show LiDAR points raycasting ...

## Why Read It

VLA and generalist robot policies의 locomotion 문제를 이해하기 위해 읽는다. 본문은 We construct a height map from raw LiDAR point clouds and introduce randomization to bridge the sim-to-real gap.를 문제로 두고, To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. METHOD), p. 3 (II. METHOD), p. 2 (II. METHOD), p. 5 (II. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
