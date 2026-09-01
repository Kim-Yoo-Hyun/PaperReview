# Evaluation - PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p056.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p056.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption)): Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, ...

## Evaluation Body Digest

- **p. 2 / 4) We provide a full implementation and systematic evaluation - extractive body cue:** of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support further ...
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **p. 5 / A. Grasp Motion Dataset Synthesis - extractive body cue:** We synthesize grasping motions via trajectory optimization in simulation, eliminating the need for complex teleoperation interfaces.
- **p. 5 / A. Grasp Motion Dataset Synthesis - extractive body cue:** Upon contact, the fingers close gradually to pinch the object, each following an independently optimized trajectory while applying a target normal force (Figs.
- **p. 6 / A. Implementation Details - extractive body cue:** Control points are placed at intervals of 25 along the trajectory, resulting in a total of 5 control points.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) ...
- **p. 5 / A. Grasp Motion Dataset Synthesis - extractive body cue:** Lee can minimize the error between the fingertip positions and their targets, while L., regularizes the motion to remain close to the initial pose.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Reconstruction results. (a) Gallery of reconstructed depth and normal maps from tactile images. (b) Depth reconstruction error ‘of the indentation test.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 4) We provide a full implementation and systematic evaluation (p. 2); A. Grasp Motion Dataset Synthesis (p. 5); VI. EXPERIMENTS (p. 6); A. Implementation Details (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper ... | p. 9 (Figure/Table caption) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B). | p. 6 (VI. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: Force analysis during grasping flat objects. The grasping process relies on three key forces: 1) The contact normal force exerted by the ... | p. 4 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Reconstruction results. (a) Gallery of reconstructed depth and normal maps from tactile images. (b) Depth reconstruction error ‘of the indentation test. | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / 4) We provide a full implementation and systematic evaluation - extractive body cue:** of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support further ...
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **p. 5 / A. Grasp Motion Dataset Synthesis - extractive body cue:** We synthesize grasping motions via trajectory optimization in simulation, eliminating the need for complex teleoperation interfaces.
- **p. 5 / A. Grasp Motion Dataset Synthesis - extractive body cue:** Upon contact, the fingers close gradually to pinch the object, each following an independently optimized trajectory while applying a target normal force (Figs.
- **p. 6 / A. Implementation Details - extractive body cue:** Control points are placed at intervals of 25 along the trajectory, resulting in a total of 5 control points.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of PP-Tac. The system secre tactile feedback from the proposed hemispherical sensor (R-Tac), integrated into a <exterous robotic hand, to grasp thin, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Force analysis during grasping flat objects. The grasping process relies on three key forces: 1) The contact normal force exerted by the sensor ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Fingertip trajectories from data synthesis. Trajectories ensure fingertip sliding along the terrain surface. Adjusting the distance between waypoints and terrain affects sensor deformation, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Inference pipeline of the proposed PP-Tae policy. Conditioned on robot proprioception and the target force that needs to be exerted, PP-Tac can infer ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Reconstruction results. (a) Gallery of reconstructed depth and normal maps from tactile images. (b) Depth reconstruction error ‘of the indentation test.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Gallery of Grasping Different Objects in Real-World Evaluations. This figure demonstrates
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 10: Camera calibration using an indentation setup: The sensor frame is fist defined in (a). A holder is designed and 3D-printed

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support ... | embodiment, simulator version and control stack | p. 2 (4) We provide a full implementation and systematic evaluation), p. 6 (A. Grasp Motion Dataset Synthesis) |
| Task/environment | After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames. | reset, timeout, object/scene variation | p. 6 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 9 (B. Depth Reconstruction of VBTS) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 7 (A. Implementation Details), p. 6 (B. PP-Tac Policy) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Lee can minimize the error between the fingertip positions and their targets, while L., regularizes the motion to remain close to the initial pose. | definition/direction/unit from same section | p. 5 (A. Grasp Motion Dataset Synthesis) |
| Fig. 7: Reconstruction results. (a) Gallery of reconstructed depth and normal maps from tactile images. (b) Depth reconstruction error ‘of the indentation test. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 1: Overview of PP-Tac. The system secre tactile feedback from the proposed hemispherical sensor (R-Tac), integrated into a <exterous robotic hand, to grasp ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 4: Force analysis during grasping flat objects. The grasping process relies on three key forces: 1) The contact normal force exerted by the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| In contrast, our method relies on rigid-body ddynamies and demonstrates direct sim-to-real transfer, as vale | definition/direction/unit from same section | p. 5 (A. Grasp Motion Dataset Synthesis) |
| After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames. | definition/direction/unit from same section | p. 6 (A. Grasp Motion Dataset Synthesis) |
| Fig. 8: Gallery of Grasping Different Objects in Real-World Evaluations. This figure demonstrates | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Then, we per form systematic comparisons of our system on different flat ‘materials and supporting terrains (Section VI-C). | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| Last, ablation studies are conducted to examine the influence of parameters, and the necessary training steps (Section VI-E). | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Last, ablation studies are conducted to examine the influence of parameters, and the necessary training steps (Section VI-E). | component/input/data sensitivity | p. 6 (VI. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), ... | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B). | numeric claim only at cited anchor | p. 6 (VI. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 7 / B. Depth Reconstruction of VBTS - extractive body cue:** In terms of computational speed, the depth mapping process takes less than 10 ms, ensuring real-time performance for robotic applications,
- **p. 7 / B. Depth Reconstruction of VBTS - extractive body cue:** To assess the system's robustness, we also varied the terrain beneath the objects. ‘The four types of terrain used include: a flat plane, a slope ...
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** ‘TABLE : Experimental results for varying paper quantities: The system's performance was evaluated on paper materials with different buckling strengths, achieved by bonding 1, 3, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in ... | p. 9 (B. Depth Reconstruction of VBTS) |
| body limitation/failure cue | We also compare our system with various manipulators to highlight its advantages and limitations (Section VI-D). | p. 6 (VI. EXPERIMENTS) |
| body limitation/failure cue | After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames. | p. 6 (A. Grasp Motion Dataset Synthesis) |
| body limitation/failure cue | Fig. 6: Inference pipeline of the proposed PP-Tae policy. Conditioned on robot proprioception and the target force that needs to be exerted, PP-Tac can ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Slip) and the final success rate (Suce. | p. 8 (B. Depth Reconstruction of VBTS) |
| body limitation/failure cue | The average number of slip events detected (No. | p. 8 (B. Depth Reconstruction of VBTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support ... | p. 2 (4) We provide a full implementation and systematic evaluation) |
| Thus, the entire inference process consists of 10 steps. | p. 6 (A. Implementation Details) |
| First, we detail the implementation of our algorithm (Section VI-A). | p. 6 (VI. EXPERIMENTS) |
| The forward kinematics fk computes the four fingertips' trajectories by giving 7. | p. 5 (A. Grasp Motion Dataset Synthesis) |
| lated through physical experiments. ‘The grasping procedure begins by initiating contact between the fingertips and the object's surface (see Appendix B for implementation details). | p. 5 (A. Grasp Motion Dataset Synthesis) |
| 8 shows the typical successful grasp cases, highlighting that our hardware and PP-Tac algorithm can successfully handle flat objects placed above both the flat ... | p. 7 (B. Depth Reconstruction of VBTS) |
| trial allowed only one grasp attempt. | p. 8 (B. Depth Reconstruction of VBTS) |
| This baseline ‘can demonstrate the effectiveness of our hardware design. | p. 8 (B. Depth Reconstruction of VBTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We also compare our system with various manipulators to highlight its advantages and limitations (Section VI-D).
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Inference pipeline of the proposed PP-Tae policy. Conditioned on robot proprioception and the target force that needs to be exerted, PP-Tac can infer ...
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** Slip) and the final success rate (Suce.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** The average number of slip events detected (No.

- **PDF anchors reviewed:** datasets p. 2 (4) We provide a full implementation and systematic evaluation), p. 6 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis), p. 5 (A. Grasp Motion Dataset Synthesis), p. 6 (A. Implementation Details), metrics p. 9 (Figure/Table caption), p. 5 (A. Grasp Motion Dataset Synthesis), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), p. 5 (A. Grasp Motion Dataset Synthesis), baselines p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), results p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
