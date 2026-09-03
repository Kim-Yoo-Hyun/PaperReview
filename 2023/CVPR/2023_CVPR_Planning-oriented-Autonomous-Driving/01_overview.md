# Planning-oriented Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2212.10156.
> PDF retrieval source: https://arxiv.org/pdf/2212.10156. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Planning, sensor fusion, 3D perception
- Official paper: https://arxiv.org/abs/2212.10156
- Full-text retrieval: https://arxiv.org/pdf/2212.10156
- Code/Project: https://github.com/OpenDriveLab/UniAD
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due to the isolation of optimization targets [57,66,82].를 문제로 두고, To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via an exquisitely designed attention module when unrolling ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Modern autonomous driving system is characterized as modular tasks in sequential order, i.e., perception, prediction, and planning.
- **p. 1 / Abstract - extractive body cue:** In order to perform a wide diversity of tasks and achieve advanced-level intelligence, contemporary approaches either deploy standalone models for individual tasks, or design a ...
- **p. 1 / Abstract - extractive body cue:** However, they might suffer from accumulative errors or deficient task coordination.
- **p. 1 / Abstract - extractive body cue:** Instead, we argue that a favorable framework should be devised and optimized in pursuit of the ultimate goal, i.e., planning of the self-driving car.
- **p. 1 / Abstract - extractive body cue:** Oriented at this, we revisit the key components within perception and prediction, and prioritize the tasks such that all these tasks contribute to planning.
- **p. 1 / 1. Introduction - extractive body cue:** Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due ...
- **p. 2 / 1. Introduction - extractive body cue:** The choice and priority of preceding tasks should be determined in favor of planning.

## Core Idea

- **p. 4 / 2. Methodology - extractive body cue:** To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via ...
- **p. 2 / 1. Introduction - extractive body cue:** (b) we present UniAD, a comprehensive end-to-end system that leverages a wide span of tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive ablations, we verify the superiority of our method over previous state-of-the-arts in all aspects.
- **p. 3 / 2. Methodology - extractive body cue:** Prediction: Motion Forecasting Recent studies have proven the effectiveness of transformer structure on the motion task [43,44,63,69,70,84,99], inspired by which we propose MotionFormer in the ...
- **p. 3 / 2. Methodology - extractive body cue:** Besides queries encoding other agents surrounding the ego-vehicle, we introduce one particular ego-vehicle query in the query set to explicitly model the self-driving vehicle itself, ...
- **p. 5 / 2. Methodology - extractive body cue:** Detailedly, F t ds is passed through a self-attention layer to model responses between distant grids, then a crossattention layer models interactions between agent features ...
- **p. 5 / 2. Methodology - extractive body cue:** To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at 1/8 downscaled feature, ...
- **p. 2 / 2. Methodology - extractive body cue:** 2, UniAD comprises four transformer decoder-based perception and prediction modules and one planner in the end.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | MapFormer also has N stacked layers whose output results of each layer are all supervised, while only the updated queries QM in the last layer are forwarded to MotionFormer for agent-map interaction. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (2. Methodology), p. 3 (2. Methodology) |
| State/latent | MapFormer, stacked, layers, whose, output, layer, supervised, while, only, updated, queries, last | geometry, map, object/relationship state | p. 3 (2. Methodology), p. 3 (2. Methodology), p. 4 (2. Methodology) |
| Output/action | Similar to [8], TrackFormer contains N layers and the final output state QA provides knowledge of Na valid agents for downstream prediction tasks. | point map, pose, scene graph, affordance 또는 query result | p. 3 (2. Methodology), p. 4 (2. Methodology), p. 2 (2. Methodology) |
| Objective/outcome | The cost function regularizes the target trajectory to obey kinematic constraints. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (2. Methodology), p. 5 (2.4. Planning), p. 4 (2. Methodology) |

## Main Claims and Actual Contribution

- **p. 4 / 2. Methodology - extractive body cue:** To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via ...
- **p. 2 / 1. Introduction - extractive body cue:** (b) we present UniAD, a comprehensive end-to-end system that leverages a wide span of tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive ablations, we verify the superiority of our method over previous state-of-the-arts in all aspects.
- **p. 3 / 2. Methodology - extractive body cue:** Prediction: Motion Forecasting Recent studies have proven the effectiveness of transformer structure on the motion task [43,44,63,69,70,84,99], inspired by which we propose MotionFormer in the ...
- **p. 3 / 2. Methodology - extractive body cue:** Besides queries encoding other agents surrounding the ego-vehicle, we introduce one particular ego-vehicle query in the query set to explicitly model the self-driving vehicle itself, ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Detailed ablations on the effectiveness of each task. We can conclude that two perception sub-tasks greatly help motion forecasting, and prediction performance also ...
- **p. 6 / 3.2. Modular Results - extractive body cue:** Moreover, UniAD achieves the lowest ID switch score, showing its temporal consistency for each tracklet.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption) |
| Embodiment/environment | We conduct experiments on the challenging nuScenes dataset [6]. | hardware/simulator version and reset protocol | p. 6 (3. Experiments), p. 6 (3.2. Modular Results) |
| Dataset/benchmark | In the Supplementary, we show more visualizations of challenging scenarios and one promising case for the planning-oriented design, that inaccurate results occur in prior modules while the later tasks could still recover, ... | role, split, size and leakage | p. 6 (3. Experiments), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results), p. 7 (3.3. Qualitative Results) |
| Metric | UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety of our system. | definition, denominator, direction and uncertainty | p. 7 (3.3. Qualitative Results), p. 7 (3.3. Qualitative Results), p. 6 (3.2. Modular Results) |
| Baseline/ablation | The first row (ID-0) serves as a vanilla multi-task baseline with separate task heads for comparison. | fair input/data/compute/action matching | p. 6 (3.1. Joint Results), p. 6 (3.2. Modular Results), p. 7 (3.3. Qualitative Results) |

## Explicit Limitations and Failure Boundary

- **p. 24 / Figure/Table caption - extractive body cue:** Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 13. Failure cases 1. Here we present a long-tail scenario, where a large trailer with a white container occupies the entire road. We can ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** Besides, we analyze that failure cases of UniAD are mainly under some long-tail scenarios such as large trucks and trailers, shown in the Supplementary as ...
- **p. 6 / 3.1. Joint Results - extractive body cue:** In Exp.1012, only when the two tasks are introduced simultaneously (Exp.12), both metrics of the planning L2 and collision rate achieve the best results, compared ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 10. Ablation for designs in the planning module. Results demonstrate the necessity of each preceding task. "BEV Att." in- dicates attending to BEV feature. ...

## Why Read It

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due to the isolation of optimization targets [57,66,82].를 문제로 두고, To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via an exquisitely designed attention module when unrolling ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (2. Methodology), p. 5 (2. Methodology), p. 2 (2. Methodology), p. 4 (2. Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
