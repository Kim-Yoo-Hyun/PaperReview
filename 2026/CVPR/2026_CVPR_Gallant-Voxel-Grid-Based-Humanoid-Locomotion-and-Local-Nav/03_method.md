# Method - Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation)): Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout.

## Method Body Digest

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We formulate humanoid perceptive locomotion as a partially observable Markov decision process (POMDP) M = (S, A, O, P, R, Ω, γ) and train an ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** The objective is to maximize expected return J(π) = E[PH-1 t=0 γtrt].
- **p. 3 / 3.2. Efficient LiDAR Simulation - extractive body cue:** Traditional raycasting builds a Bounding Volume Hierarchy (BVH) over scene geometry, which becomes costly if updated at every simulation step due to dynamics.
- **p. 2 / 1. Introduction - extractive body cue:** In contrast, 3D LiDAR provides detailed scene geometry with a wide FoV, but its raw point clouds are sparse and noisy, which bottlenecks sample-efficient policy ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Actor and critic share all features except privileged inputs, which are critic-only.
- **p. 3 / 3. Method - extractive body cue:** Together, these components form a fullstack pipeline-from data generation to perception to control-that trains a single policy to robustly traverse all-space obstacles and deploy zero-shot ...
- **p. 2 / 1. Introduction - extractive body cue:** Experiments also highlight the importance of our high-fidelity LiDAR simulation, which dynamically generates realistic observations essential for scalable, LiDAR-based training.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic scanning ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose voxel grid as a lightweight yet geometrypreserving representation for humanoid locomotion and loco-navigation [31] in 3D-constrained environments.
- **p. 3 / 3. Method - extractive body cue:** We introduce Gallant, a voxel-grid-based perceptive learning framework for humanoid locomotion and local navigation [31] in 3D constrained environments.

## Source Evidence Cues

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We formulate humanoid perceptive locomotion as a partially observable Markov decision process (POMDP) M = (S, A, O, P, R, Ω, γ) and train an ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout. | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We formulate humanoid perceptive locomotion as a partially observable Markov decision process (POMDP) M = (S, A, O, P, R, Ω, γ) ... | p. 3 (3.1. Problem Formulation) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Episodes end on fall, harsh collision (contact on the torso, hip, or knee links with a force exceeding 100 N), or timeout. | p. 3 (3.1. Problem Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** The objective is to maximize expected return J(π) = E[PH-1 t=0 γtrt].
- **p. 3 / 3.2. Efficient LiDAR Simulation - extractive body cue:** Traditional raycasting builds a Bounding Volume Hierarchy (BVH) over scene geometry, which becomes costly if updated at every simulation step due to dynamics.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (3.1. Problem Formulation), p. 3 (3.2. Efficient LiDAR Simulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contrast, LiDAR, provides, detailed, scene, geometry, wide, FoV, point, clouds, sparse, noisy, bottlenecks, sample-efficient | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | contrast, LiDAR, provides, detailed, scene, geometry, wide, FoV, point, clouds | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | scale, training, narrow, simulation-to-reality, simto-real, develop, LiDAR, simulation, pipeline, models | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | objective, maximize, expected, return, PH-1, Traditional, raycasting, builds, Bounding, Volume | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In contrast, 3D LiDAR provides detailed scene geometry with a wide FoV, but its raw point clouds are sparse and noisy, which bottlenecks sample-efficient policy ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Actor and critic share all features except privileged inputs, which are critic-only.
- **p. 3 / 3. Method - extractive body cue:** Together, these components form a fullstack pipeline-from data generation to perception to control-that trains a single policy to robustly traverse all-space obstacles and deploy zero-shot ...
- **p. 2 / 1. Introduction - extractive body cue:** Experiments also highlight the importance of our high-fidelity LiDAR simulation, which dynamically generates realistic observations essential for scalable, LiDAR-based training.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Here, the subscript range t -a : t -b denotes inclusion of temporal history from time step t -a to t -b. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | To align simulation with real-world sensing, we apply domain randomization: (a) LiDAR Pose: Perturbed at episode start by P rand LiDAR = ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | Here, the subscript range t -a : t -b denotes inclusion of temporal history from time step t -a to t -b. | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | To align simulation with real-world sensing, we apply domain randomization: (a) LiDAR Pose: Perturbed at episode start by P rand LiDAR = ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** We formulate humanoid perceptive locomotion as a partially observable Markov decision process (POMDP) M = (S, A, O, P, R, Ω, γ) and train an ...
- **p. 5 / 4.2.1. Metrics - extractive body cue:** We train every policy for 4{,} 000 iterations, then run 5 independent evaluations (each run evaluates over 1{,} 000 complete episodes), reporting mean \pm standard ...
- **p. 7 / 4.3.1. Deployment - extractive body cue:** These results highlight Gallant's ability to encode spatial constraints from perception and translate them into robust, real-time whole-body behaviors.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Episodes, fall, harsh, collision, contact, torso, knee, links, force, exceeding, timeout, formulate, humanoid, perceptive, locomotion, partially, observable, Markov, decision, process.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the ... | p. 5 (4.2.1. Metrics), p. 8 (4.4. Further Analyses) |
| Balance-aware whole-body execution | Gallant consistently outperforms both baselines across all real-world terrains. | p. 8 (4.3.2. Ablation), p. 5 (4.1. Experimental Configuration) |
| Recovery / adaptation | With all other settings fixed, Gallant achieves much higher success rates than the variant that ignores dynamic objects (w/o-Self-Scan) across all tasks. | p. 6 (4.2.3. Result), p. 7 (4.2.3. Result) |

## Failure and Ablation Link

- **p. 5 / 4.2.2. Baselines - extractive body cue:** To assess the effectiveness of core components in Gallant, we compare against the following ablations: • Self-scan.
- **p. 8 / 4.3.2. Ablation - extractive body cue:** The NoDR variant performs reasonably well on Ceiling and Door, suggesting low sensitivity to sensing latency in these cases.
- **p. 7 / 4.3.1. Deployment - extractive body cue:** We directly deploy the Gallant-trained policy onto the real Unitree G1 humanoid without any fine-tuning.
- **p. 7 / 4.3.2. Ablation - extractive body cue:** To evaluate sim-to-real performance, we deploy three policies on the 29-DoF Unitree G1 and compare success rates across terrains: (i) HeightMap, which replaces the voxel ...
- **p. 5 / 4.2.3. Result - extractive body cue:** Ablationspecific analyses are summarized as follow: 28090
- **p. 6 / 4.2.3. Result - extractive body cue:** For each ablation setting, the best-performing value per metric on each terrain is highlighted in bold.
- **p. 6 / 4.2.3. Result - extractive body cue:** With all other settings fixed, Gallant achieves much higher success rates than the variant that ignores dynamic objects (w/o-Self-Scan) across all tasks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), objective p. 3 (3.1. Problem Formulation), p. 3 (3.2. Efficient LiDAR Simulation), temporal p. 3 (3.1. Problem Formulation), p. 4 (C Voxel Grid), p. 3 (3.1. Problem Formulation), p. 5 (4.2.1. Metrics), p. 7 (4.3.1. Deployment), p. 8 (4.4. Further Analyses).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
