# Evaluation - Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.03385; PDF retrieval source: https://arxiv.org/pdf/2012.03385. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 14 (Figure/Table caption), p. 2 (Figure/Table caption)): Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve 100% success rates ...

## Evaluation Body Digest

- **p. 6 / VIII. PHYSICAL EXPERIMENTS AND RESULTS - extractive body cue:** We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper.
- **p. 5 / VI. SIMULATION EXPERIMENTS - extractive body cue:** We use scripted, stochastic demonstrator policies to get 1000 demonstrations (i.e., episodes) per task, and train policies using 1, 10, 100, or all 1000 demonstrations.
- **p. 6 / VII. SIMULATION RESULTS - extractive body cue:** Task success rate (mean % over 60 test-time episodes in simulation of the best saved snapshot) vs. # of demonstration episodes (1, 10, 100, or ...
- **p. 5 / VI. SIMULATION EXPERIMENTS - extractive body cue:** Episodes for fabric-cover are successful if the fabric covers the cube.
- **p. 6 / VII. SIMULATION RESULTS - extractive body cue:** Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve 100% ...
- **p. 6 / VII. SIMULATION RESULTS - extractive body cue:** For fabric-flat-notarget, the performance of both goal-conditioned Transporters is more evenly matched, while for bag-color-goal, Transporter-Goal-Split achieves higher success rates of 12.2% and 29.8% with ...
- **p. 5 / VII. SIMULATION RESULTS - extractive body cue:** It performs reliably on fabric-cover with 100% success rates
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8: Results for models on the block-notarget task. From left to right, we report models trained with 1, 10, 100, and 1000 demonstrations. All ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** VI. SIMULATION EXPERIMENTS (p. 5); VII. SIMULATION RESULTS (p. 5); VIII. PHYSICAL EXPERIMENTS AND RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VII. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve ... | p. 6 (VII. SIMULATION RESULTS) |
| VII. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For fabric-flat-notarget, the performance of both goal-conditioned Transporters is more evenly matched, while for bag-color-goal, Transporter-Goal-Split achieves higher success rates of 12.2% and 29.8% ... | p. 6 (VII. SIMULATION RESULTS) |
| VII. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | It performs reliably on fabric-cover with 100% success rates | p. 5 (VII. SIMULATION RESULTS) |
| VII. SIMULATION RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Non-Goal Conditioned Tasks In these tasks, Transporter generally achieves orders of magnitude better sample efficiency than ground truth models. | p. 5 (VII. SIMULATION RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: Results for models on the block-notarget task. From left to right, we report models trained with 1, 10, 100, and 1000 demonstrations. ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / VIII. PHYSICAL EXPERIMENTS AND RESULTS - extractive body cue:** We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper.
- **p. 5 / VI. SIMULATION EXPERIMENTS - extractive body cue:** We use scripted, stochastic demonstrator policies to get 1000 demonstrations (i.e., episodes) per task, and train policies using 1, 10, 100, or all 1000 demonstrations.
- **p. 6 / VII. SIMULATION RESULTS - extractive body cue:** Task success rate (mean % over 60 test-time episodes in simulation of the best saved snapshot) vs. # of demonstration episodes (1, 10, 100, or ...
- **p. 5 / VI. SIMULATION EXPERIMENTS - extractive body cue:** Episodes for fabric-cover are successful if the fabric covers the cube.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Example of a trained Transporter Network policy in action on the bag-items-1 task (see Table I). The setup involves a simulated UR5 robot ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and deformable objects. Top row: (a) cable-ring, (b) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The proposed Transporter-Goal-Split, applied to an example on bag-color-goal, where given the current image ot and goal og, the objective is to insert ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Top row: examples of physical bags. The bags we use follow a design similar to the sack (top left) and drawstring (top middle). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: The physical setup from a third-person view, using a Franka robot with a hand-mounted camera. The blue contours show the field-of-view for the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: block-notarget. This task involves a red, rigid L-shaped block. At the current observation ot, the block starts at some random location on the ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8: Results for models on the block-notarget task. From left to right, we report models trained with 1, 10, 100, and 1000 demonstrations. All ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper. | embodiment, simulator version and control stack | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS) |
| Task/environment | We use scripted, stochastic demonstrator policies to get 1000 demonstrations (i.e., episodes) per task, and train policies using 1, 10, 100, or all 1000 ... | reset, timeout, object/scene variation | p. 5 (VI. SIMULATION EXPERIMENTS), p. 6 (VII. SIMULATION RESULTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (III. BACKGROUND), p. 2 (III. BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve ... | definition/direction/unit from same section | p. 6 (VII. SIMULATION RESULTS) |
| For fabric-flat-notarget, the performance of both goal-conditioned Transporters is more evenly matched, while for bag-color-goal, Transporter-Goal-Split achieves higher success rates of 12.2% and 29.8% ... | definition/direction/unit from same section | p. 6 (VII. SIMULATION RESULTS) |
| It performs reliably on fabric-cover with 100% success rates | definition/direction/unit from same section | p. 5 (VII. SIMULATION RESULTS) |
| Fig. 8: Results for models on the block-notarget task. From left to right, we report models trained with 1, 10, 100, and 1000 demonstrations. ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and deformable objects. Top row: (a) cable-ring, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Episodes for fabric-cover are successful if the fabric covers the cube. | definition/direction/unit from same section | p. 5 (VI. SIMULATION EXPERIMENTS) |
| Fig. 3: The proposed Transporter-Goal-Split, applied to an example on bag-color-goal, where given the current image ot and goal og, the objective is to ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 6: The physical setup from a third-person view, using a Franka robot with a hand-mounted camera. The blue contours show the field-of-view for ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Goal Conditioned Tasks Across all 4 dataset sizes for cable-line-notarget, cableshape-notarget, and fabric-flat-notarget, both TransporterGoal-Stack and Transporter-Goal-Split substantially outperform the two GT-State baselines. | comparison identity and matched condition | p. 6 (VII. SIMULATION RESULTS) |
| Models are trained for 20K iterations, with a batch size of 1 for the three Transporter models and 128 for the two ground truth ... | comparison identity and matched condition | p. 5 (VII. SIMULATION RESULTS) |
| Ground truth baselines are tested in both settings, where in the goalconditioned case, we concatenate the ground truth pose information in both the current ... | comparison identity and matched condition | p. 5 (VI. SIMULATION EXPERIMENTS) |
| For the first eight tasks listed, we benchmark with Transporter Networks [68] ("Transporter") and two baselines that use ground-truth pose information instead of images ... | comparison identity and matched condition | p. 6 (VII. SIMULATION RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 4: Top row: examples of physical bags. The bags we use follow a design similar to the sack (top left) and drawstring (top ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures. | Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 14 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Primary metric/result | For fabric-flat-notarget, the performance of both goal-conditioned Transporters is more evenly matched, while for bag-color-goal, Transporter-Goal-Split achieves higher success rates of 12.2% and 29.8% ... | numeric claim only at cited anchor | p. 6 (VII. SIMULATION RESULTS) |

- Numeric sentences retained from the body:
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Example of a trained Transporter Network policy in action on the bag-items-1 task (see Table I).
- **p. 1 / I. INTRODUCTION - extractive body cue:** We overlay arrows to indicate the movement of the robot's arm just before a given frame. one 1D deformable task, we show results on 12 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are: (i) an opensource simulated benchmark, DeformableRavens, with 12 tasks manipulating 1D, 2D, and 3D deformable objects to help ...
- **p. 4 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** All tested Transporter architectures produce Qpick and Qplace, which are each 320×160 dimensional heat maps colored so that darker pixels are low values and lighter ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** Benchmark for Manipulating Deformable Objects We design 12 tasks with deformables, listed in Table I.
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** For consistency, each uses a standardized setup: a UR5 arm, a 0.5×1m tabletop workspace, and 3 calibrated RGBD cameras diagonally overlooking the workspace, producing top-down ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on ... | p. 4 (V. SIMULATOR AND TASKS) |
| body limitation/failure cue | Changes from Simulation Unlike in simulation, we cannot assume "perfect" grasping of deformable objects. | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and deformable objects. Top row: (a) cable-ring, ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: The proposed Transporter-Goal-Split, applied to an example on bag-color-goal, where given the current image ot and goal og, the objective is to ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Bags with handles (e.g., top right) or with more stiffness will be addressed in future work. | p. 5 (V. SIMULATOR AND TASKS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper. | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS) |
| As a heuristic, we take a local image crop centered at the picking point and compute the best fit tangent line of the cable. | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS) |
| Models are trained for 20K iterations, with a batch size of 1 for the three Transporter models and 128 for the two ground truth ... | p. 5 (VII. SIMULATION RESULTS) |
| The project website contains supplementary material, including the appendix, code, data, and videos. | p. 1 (I. INTRODUCTION) |
| Depending on the task stage and the gripped item, actions lift the gripped object to a different hard-coded height. | p. 5 (V. SIMULATOR AND TASKS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering ...
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on the ...
- **p. 6 / VIII. PHYSICAL EXPERIMENTS AND RESULTS - extractive body cue:** Changes from Simulation Unlike in simulation, we cannot assume "perfect" grasping of deformable objects.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and deformable objects. Top row: (a) cable-ring, (b) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The proposed Transporter-Goal-Split, applied to an example on bag-color-goal, where given the current image ot and goal og, the objective is to insert ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** Bags with handles (e.g., top right) or with more stiffness will be addressed in future work.

- **Evidence anchors reviewed:** datasets p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS), metrics p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 14 (Figure/Table caption), p. 2 (Figure/Table caption), p. 5 (VI. SIMULATION EXPERIMENTS), baselines p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS), p. 6 (VII. SIMULATION RESULTS), results p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS), p. 14 (Figure/Table caption), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
