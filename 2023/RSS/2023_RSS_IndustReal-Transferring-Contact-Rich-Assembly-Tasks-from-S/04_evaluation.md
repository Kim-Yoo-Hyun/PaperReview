# Evaluation - IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.17110; PDF retrieval source: https://arxiv.org/pdf/2305.17110. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 1 (Figure/Table caption), p. 9 (VI. REAL-WORLD EXPERIMENTS), p. 6 (Figure/Table caption)): Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value at test time. Boxes indicate median ...

## Evaluation Body Digest

- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects before releasing them.
- **p. 7 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Pick Experiment This experiment evaluated the ability of the real-world system to initiate contact and pick up arbitrarily-placed objects.
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Sort Demonstration This experiment qualitatively demonstrated the ability of the robot to execute a realistic sorting procedure.
- **p. 7 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** After developing and validating our algorithms, we performed comprehensive experiments and demos to evaluate our real-world system (Figure S10).
- **p. 9 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Top row: recovery behavior exhibited by the robot after human perturbation during gear insertion.
- **p. 9 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 9/10 ...
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III).
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** The higher success rates suggest that the randomization and noise ranges during the Insert experiment may have been particularly adverse.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** VI. REAL-WORLD EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value ... | p. 4 (Figure/Table caption) |
| VI. REAL-WORLD EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| VI. REAL-WORLD EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Key Results: The system demonstrated even higher success rates than during the Insert experiment: 80% and 88.3% success/engagement rates for peg insertion, 97.5% and ... | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. ... | p. 1 (Figure/Table caption) |
| VI. REAL-WORLD EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 ... | p. 9 (VI. REAL-WORLD EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects before releasing them.
- **p. 7 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Pick Experiment This experiment evaluated the ability of the real-world system to initiate contact and pick up arbitrarily-placed objects.
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Sort Demonstration This experiment qualitatively demonstrated the ability of the robot to execute a realistic sorting procedure.
- **p. 7 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** After developing and validating our algorithms, we performed comprehensive experiments and demos to evaluate our real-world system (Figure S10).
- **p. 9 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Top row: recovery behavior exhibited by the robot after human perturbation during gear insertion.
- **p. 9 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 9/10 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. Bottom: ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Problem setup and decomposition. Column 1: Three types of assemblies. Columns 2-4: Goal states of Pick, Place, and Insert phases. • Pick: The ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value at ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Joint evaluation of Simulation-Based Policy Update, SDF-Based Dense Reward, and Sampling-Based Curriculum. (A) Pegs and Holes assembly Insert policy. (B) Gears and Gearshafts ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Evaluation of PLAI in simulation. Results of Nominal are annotated when outside of plot bounds. Full-axis plot is in Figure S13. conditions in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Evaluation of PLAI in the real world. Each method was tested on 3 different goals with 20 trials each. Evaluation parameters are in ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Snapshots of real-world experiments. Top row: recovery behavior exhibited by the robot after human perturbation during gear insertion. Bottom row: search behavior exhibited ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects before releasing ... | embodiment, simulator version and control stack | p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS) |
| Task/environment | Pick Experiment This experiment evaluated the ability of the real-world system to initiate contact and pick up arbitrarily-placed objects. | reset, timeout, object/scene variation | p. 7 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). | definition/direction/unit from same section | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| The higher success rates suggest that the randomization and noise ranges during the Insert experiment may have been particularly adverse. | definition/direction/unit from same section | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 4: Joint evaluation of Simulation-Based Policy Update, SDF-Based Dense Reward, and Sampling-Based Curriculum. (A) Pegs and Holes assembly Insert policy. (B) Gears and ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 ... | definition/direction/unit from same section | p. 9 (VI. REAL-WORLD EXPERIMENTS) |
| Fig. 5: Evaluation of PLAI in simulation. Results of Nominal are annotated when outside of plot bounds. Full-axis plot is in Figure S13. conditions ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 7: Snapshots of real-world experiments. Top row: recovery behavior exhibited by the robot after human perturbation during gear insertion. Bottom row: search behavior ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and ... | comparison identity and matched condition | p. 8 (VI. REAL-WORLD EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and ... | component/input/data sensitivity | p. 8 (VI. REAL-WORLD EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well ... | Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 1 (Figure/Table caption), p. 9 (VI. REAL-WORLD EXPERIMENTS), p. 6 (Figure/Table caption) |
| Primary metric/result | Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). | numeric claim only at cited anchor | p. 8 (VI. REAL-WORLD EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Each method was tested on 3 different goals with 20 trials each.
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Key Results: The system demonstrated low steady-state errors, with a mean distance-to-goal of 4.23 ± 1.96 mm.
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** However, all rewards could be expressed in the following general form: G = wh0..whm  H-1 X t=0 [wd0Rd0(t) + ... + wdnRdn(t)] + ws0Rs0 ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** The module samples N = 1000 points on/inside the mesh of the plug, transforms the points to the socket frame, computes distances to the socket ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** After training policies with each strategy, we tested each policy in simulation over 5 seeds, with 1000 trials per seed; quantified dmax ip for each ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** 1 sample N points in mp →v, v = {v0, ..., vN-1}; 2 transform v to current mp pose pp in ms frame ; 3 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in ... | p. 9 (VIII. LIMITATIONS & FUTURE WORK) |
| body limitation/failure cue | Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve ... | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| body limitation/failure cue | Our work has limitations, which lend themselves naturally to future research directions. | p. 9 (VIII. LIMITATIONS & FUTURE WORK) |
| body limitation/failure cue | Failure cases were one missed detection of a peg, as well as one grasp of both a peg and its corresponding peg tray. | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| body limitation/failure cue | Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Fig. 4: Joint evaluation of Simulation-Based Policy Update, SDF-Based Dense Reward, and Sampling-Based Curriculum. (A) Pegs and Holes assembly Insert policy. (B) Gears and ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each method was tested on 3 different goals with 20 trials each. | p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| We used the PPO implementation from rl-games [42]; hyperparameters and architectures are in Table XI. | p. 3 (IV. POLICY LEARNING IN SIMULATION) |
| After training policies with each strategy, we tested each policy in simulation over 5 seeds, with 1000 trials per seed; quantified dmax ip for ... | p. 4 (IV. POLICY LEARNING IN SIMULATION) |
| Empirically, PLAI requires minimal implementation effort (1-2 lines of code), is simple to tune, and outperforms standard PID in our application. | p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |
| Policy-Level Action Integrator Method: Robotics simulations can exhibit marked discrepancies with the real world due to incomplete models, inaccurate parameters, and numerical artifacts [14]; ... | p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |
| Training Environments We developed our code within the Factory simulation framework [48]. | p. 3 (IV. POLICY LEARNING IN SIMULATION) |
| Specifically, we implemented a GPU-based interpenetrationchecking module using warp [40]. | p. 4 (IV. POLICY LEARNING IN SIMULATION) |
| As Factory [48] already precomputes SDFs for all objects for contact generation, we envision a single representationgeneration step for both physics and reward. | p. 5 (IV. POLICY LEARNING IN SIMULATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their ...
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this ...
- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Our work has limitations, which lend themselves naturally to future research directions.
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Failure cases were one missed detection of a peg, as well as one grasp of both a peg and its corresponding peg tray.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. Bottom: ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Joint evaluation of Simulation-Based Policy Update, SDF-Based Dense Reward, and Sampling-Based Curriculum. (A) Pegs and Holes assembly Insert policy. (B) Gears and Gearshafts ...

- **Evidence anchors reviewed:** datasets p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS), p. 9 (VI. REAL-WORLD EXPERIMENTS), p. 9 (VI. REAL-WORLD EXPERIMENTS), metrics p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 9 (VI. REAL-WORLD EXPERIMENTS), baselines p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS), results p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 1 (Figure/Table caption), p. 9 (VI. REAL-WORLD EXPERIMENTS), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 9/10 7/10 7/10 Round peg 16 ... (p. 9, VI. REAL-WORLD EXPERIMENTS).
- **Metric evidence:** Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). (p. 8, VI. REAL-WORLD EXPERIMENTS).
- **Baseline/ablation evidence:** To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and insertion) without any policy adaptation phase ... (p. 8, VI. REAL-WORLD EXPERIMENTS).
- **Failure/negative evidence:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this issue. (p. 8, VI. REAL-WORLD EXPERIMENTS).
