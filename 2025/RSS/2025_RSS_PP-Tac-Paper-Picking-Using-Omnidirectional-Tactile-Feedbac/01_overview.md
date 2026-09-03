# PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p056.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p056.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, dexterous manipulation, deformable objects, force control, slip detection
- Official paper: https://www.roboticsproceedings.org/rss21/p056.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p056.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.를 문제로 두고, To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating the creation of a buckling region for ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robots are inereasingly envisioned as human com- 1.
- **p. 1 / Abstract - extractive body cue:** Ivrropucrion anions, assisting with everyday tasks that offen involve manip
- **p. 1 / Abstract - extractive body cue:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly ...
- **p. 1 / Abstract - extractive body cue:** and fabric. ‘These' limitations stem from the lack of robust perception techniques for reliable state estimation under diverse often involving the grasp of thin, deformable ...
- **p. 1 / Abstract - extractive body cue:** fal conditions and the absence of planning methods capa- paper and fabric [51].
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Although creases or irregularities in the ‘material can sometimes provide grasping points, a particularly challenging scenario arises when the object is extremely flat and lacks ...

## Core Idea

- **p. 5 / V. POLICY LEARNING FOR PAPER-PICKING - extractive body cue:** To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating ...
- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** These evaluations showcase the robustness and adaptability of our approach,
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** This research introduces a novel approach to tackle the paper picking problem that was previously unexplored.
- **p. 6 / A. Implementation Details - extractive body cue:** Our diffusion policy is implemented as a fourlayer Transformer encoder with a latent dimension of 512 and four attention heads.
- **p. 6 / B. PP-Tac Policy - extractive body cue:** Such an overparameterized input allows the network to extract more robust and expressive latent features for the diffusion policy.
- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** trajectory with compliant finger control via tactile feedback; (3) Model based force tracking": combines the PP-Tac-lerived hand trajectory with compliant finger control via tactile feedback; ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2) Diffusion Policy Training: Train a policy fon this dataset t0 infer motions from tactile feedback and proprioceptive states, ensuring generalization to real-world robotic systems, | tactile image/force, vision과 proprioceptive history | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS) |
| State/latent | Diffusion, Policy, Training, Train, dataset, infer, motions, tactile, feedback, proprioceptive, states, ensuring | contact geometry, force state 또는 latent dynamics | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details) |
| Output/action | trajectory with compliant finger control via tactile feedback; (3) Model based force tracking": combines the PP-Tac-lerived hand trajectory with compliant finger control via tactile feedback; (4) Non-disturbance: grasp using our dextero ... | grasp/contact action, force command 또는 object motion | p. 9 (B. Depth Reconstruction of VBTS), p. 7 (A. Implementation Details), p. 6 (B. PP-Tac Policy) |
| Objective/outcome | reconstruction loss of 0.35 mm, and a median loss of 0.28 mm, with 60% of reconstruction losses below 0.3 mm. | slip/contact success, force/pose error와 robustness | p. 7 (B. Depth Reconstruction of VBTS), p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 8 (B. Depth Reconstruction of VBTS) |

## Main Claims and Actual Contribution

- **p. 5 / V. POLICY LEARNING FOR PAPER-PICKING - extractive body cue:** To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating ...
- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** These evaluations showcase the robustness and adaptability of our approach,
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** This research introduces a novel approach to tackle the paper picking problem that was previously unexplored.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B).
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Force analysis during grasping flat objects. The grasping process relies on three key forces: 1) The contact normal force exerted by the sensor ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS) |
| Embodiment/environment | of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support further research and. community development, | hardware/simulator version and reset protocol | p. 2 (4) We provide a full implementation and systematic evaluation), p. 6 (A. Grasp Motion Dataset Synthesis) |
| Dataset/benchmark | We synthesize grasping motions via trajectory optimization in simulation, eliminating the need for complex teleoperation interfaces. | role, split, size and leakage | p. 2 (4) We provide a full implementation and systematic evaluation), p. 6 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis) |
| Metric | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 5 (A. Grasp Motion Dataset Synthesis), p. 7 (Figure/Table caption) |
| Baseline/ablation | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We also compare our system with various manipulators to highlight its advantages and limitations (Section VI-D).
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Inference pipeline of the proposed PP-Tae policy. Conditioned on robot proprioception and the target force that needs to be exerted, PP-Tac can infer ...
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** Slip) and the final success rate (Suce.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** The average number of slip events detected (No.
- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** Additionally, the increase in material stiffness also led to a higher number of detected slips.

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.를 문제로 두고, To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating the creation of a buckling region for ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (IV. PROBLEM STATEMENT), p. 4 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT), p. 5 (IV. PROBLEM STATEMENT), p. 6 (A. Implementation Details), p. 6 (B. PP-Tac Policy) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces. (p. 4, IV. PROBLEM STATEMENT).
- **Actual contribution:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly within household environments (3) with ... (p. 1, Abstract).
- **Evaluation boundary:** Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** However, vision-based methods often struggle in real-world DOM tasks due to variability in object appearance, unknown physical properties, visual occlusions [25, 6], and inconsistent lighting conditions [48, 22) ‘These limitations ... (p. 2, A. Deformable Object Manipulation).
