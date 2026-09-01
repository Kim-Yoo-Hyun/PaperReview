# Evaluation - SATA: Safe and Adaptive Torque-Based Locomotion Policies Inspired by Animal Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p124.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p124.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Simulation Experiments)): Sa, SATA significantly outperforms SATA w/o growth in early stages of training, demonstrating the impact of this mechanism in early stage exploration.

## Evaluation Body Digest

- **p. 7 / B. Lab Level Experiments - extractive PDF cue:** ‘To validate the effectiveness of our approach, we deployed it on a Unitree Go2 quadruped robot in real-world scenarios.
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ‘The environment resets ...
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** During this disturbance (0.5 < ¢ < 1.58) the robot dynamically
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Similarly, G(0) allows the robot to adapt reward priorities to align with specific training objectives.
- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** Moreover, when comparing the cumulative reward of both scenarios under OOD velocity commands (vz = 1.8m/s) as in Fig.
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** Training rewards (), without GiQ) adgptation, and cumulative rewards in simulation test (6), when Commanded to fun at '8 ms (lightly OOD),
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** The adjusted growthbased reward rorowen expressions are summarized in Table I:

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** A. Implementation of the Growth Mechanism (p. 5); V. EXPERIMENTS (p. 6); A. Simulation Experiments (p. 6); B. Lab Level Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Sa, SATA significantly outperforms SATA w/o growth in early stages of training, demonstrating the impact of this mechanism in early stage exploration. | p. 7 (A. Simulation Experiments) |
| A. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5b, we can see that our method ‘outperforms SATA w/o growth, demonstrating the impact of the growth mechanism on policy generalization. | p. 7 (A. Simulation Experiments) |
| A. Implementation of the Growth Mechanism | EMPIRICAL / REAL-ROBOT OR HARDWARE | Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ‘The environment ... | p. 6 (A. Implementation of the Growth Mechanism) |
| A. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1) Ablation Study: "To evaluate the contribution of each component of our approach, we compare the performance of the complete framework (SATA) with variants ... | p. 6 (A. Simulation Experiments) |

## Dataset / Benchmark Role

- **p. 7 / B. Lab Level Experiments - extractive PDF cue:** ‘To validate the effectiveness of our approach, we deployed it on a Unitree Go2 quadruped robot in real-world scenarios.
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ‘The environment resets ...
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** During this disturbance (0.5 < ¢ < 1.58) the robot dynamically
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Similarly, G(0) allows the robot to adapt reward priorities to align with specific training objectives.
- **p. 5 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities can ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Overview of our SATA Framework. Dotted lines ind
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3. Ablation study of the proposed framework. showing successful traning in green and failurofpremature convergence in red, SATA ts compared with varans that lack ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5." Comparison of SATA and SATA wo Growth. Training rewards (), without GiQ) adgptation, and cumulative rewards in simulation test (6), when Commanded to ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 7. Leg disturbance test with a) Backward sweep of the front legs, b) Backward sweep of the back legs. and e) Forward sweep of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 8. Walking under external downward foresreses, The blue line i the ‘actual torque command given tothe motors after the processing done by our biomechanical ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 10. Locomotion through a height-constrsined space. Notably, 10

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ‘To validate the effectiveness of our approach, we deployed it on a Unitree Go2 quadruped robot in real-world scenarios. | embodiment, simulator version and control stack | p. 7 (B. Lab Level Experiments), p. 6 (A. Implementation of the Growth Mechanism) |
| Task/environment | Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ‘The environment ... | reset, timeout, object/scene variation | p. 6 (A. Implementation of the Growth Mechanism), p. 7 (A. Simulation Experiments) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 2 (1. Iyrropuction), p. 4 (A. Biomechanical Modet) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (1. Iyrropuction), p. 3 (1. Iyrropuction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Moreover, when comparing the cumulative reward of both scenarios under OOD velocity commands (vz = 1.8m/s) as in Fig. | definition/direction/unit from same section | p. 7 (A. Simulation Experiments) |
| Training rewards (), without GiQ) adgptation, and cumulative rewards in simulation test (6), when Commanded to fun at '8 ms (lightly OOD), | definition/direction/unit from same section | p. 7 (A. Simulation Experiments) |
| Instead of granting the policy full access to the action space from the star of training, we propose that partially limiting the robot's abilities ... | definition/direction/unit from same section | p. 5 (A. Implementation of the Growth Mechanism) |
| The adjusted growthbased reward rorowen expressions are summarized in Table I: | definition/direction/unit from same section | p. 6 (A. Implementation of the Growth Mechanism) |
| Similarly, G(0) allows the robot to adapt reward priorities to align with specific training objectives. | definition/direction/unit from same section | p. 6 (A. Implementation of the Growth Mechanism) |
| The parameters ky, and ty denote the growth rate, the current training step, and the step at which the maximum growth rate occurs, respectively | definition/direction/unit from same section | p. 5 (A. Implementation of the Growth Mechanism) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also compared its performance against several baseline methods, including Unitree's built-in, MPC-based controller, | comparison identity and matched condition | p. 7 (B. Lab Level Experiments) |
| ‘TABLE IV PERFORMANCE COMPARISON BETWEEN OUR METHOD AND BASELINES ACROSS DIFFERENT ROBUSTNESS TESTS (5 TRIALS FER TEST) | comparison identity and matched condition | p. 7 (A. Simulation Experiments) |
| Ablation study of the proposed framework. showing successful traning in green and failurofpremature convergence in red, SATA ts compared with varans that lack the ... | comparison identity and matched condition | p. 6 (A. Implementation of the Growth Mechanism) |
| 1) Ablation Study: "To evaluate the contribution of each component of our approach, we compare the performance of the complete framework (SATA) with variants ... | comparison identity and matched condition | p. 6 (A. Simulation Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 1) Ablation Study: "To evaluate the contribution of each component of our approach, we compare the performance of the complete framework (SATA) with variants ... | component/input/data sensitivity | p. 6 (A. Simulation Experiments) |
| Ablation study of the proposed framework. showing successful traning in green and failurofpremature convergence in red, SATA ts compared with varans that lack the ... | component/input/data sensitivity | p. 6 (A. Implementation of the Growth Mechanism) |
| Training rewards (), without GiQ) adgptation, and cumulative rewards in simulation test (6), when Commanded to fun at '8 ms (lightly OOD), | component/input/data sensitivity | p. 7 (A. Simulation Experiments) |
| this biomechanical model is removed, the robot converges to unnatural gaits, such as three-legged support pattems, which reduce stability and limit energy efficiency. | component/input/data sensitivity | p. 7 (A. Simulation Experiments) |
| To unify these components, We introduce a time-dependent general scale C(t), derived from the Gompertz. model [72], « well-established framework for modeling growth: | component/input/data sensitivity | p. 5 (A. Implementation of the Growth Mechanism) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| + Stable and Efficient Torque-Based Learning: We propose «novel framework for learning torque-based loco- ‘motion policies with a growth mechanism that gradually. unlocks torque ... | Sa, SATA significantly outperforms SATA w/o growth in early stages of training, demonstrating the impact of this mechanism in early stage exploration. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Simulation Experiments) |
| Primary metric/result | 5b, we can see that our method ‘outperforms SATA w/o growth, demonstrating the impact of the growth mechanism on policy generalization. | numeric claim only at cited anchor | p. 7 (A. Simulation Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** This framework enables high-throughput simulation, allowing us to simulate 4096 instances of the GO2 robot in parallel on a single NVIDIA RTX 4090 GPU.
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Leveraging this framework, we achieve efficient policy learning within 20 minutes/ 3000 episodes. ‘The maximum episode length is set to 10 seconds. ‘The environment resets ...
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** Growth Schedule E_ [000003 [to [24000 [Face [7.05 Nm Fend_/ 23.5 Nm / Faon_[ 100 Hz [ fom [ 200 He.
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** Training rewards (), without GiQ) adgptation, and cumulative rewards in simulation test (6), when Commanded to fun at '8 ms (lightly OOD),
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** ‘TABLE IV PERFORMANCE COMPARISON BETWEEN OUR METHOD AND BASELINES ACROSS DIFFERENT ROBUSTNESS TESTS (5 TRIALS FER TEST)
- **p. 6 / A. Implementation of the Growth Mechanism - extractive PDF cue:** This framework enables high-throughput simulation, allowing us to simulate 4096 instances of the GO2 robot in parallel on a single NVIDIA RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | [Locomotion on wet slippery surfaces, showing both sucess (a) and failure (b), Even when the foot ofthe robot sip and fall down in Tile ... | p. 9 (1 Saco case) |
| body limitation/failure cue | In contrast, Figure 11b shows a failure case, where the robot is given an abrupt command on the slippery surface. | p. 9 (1 Saco case) |
| body limitation/failure cue | 2) Robustness to Single-Leg Failure: In this experiment, we simulate the failure of a single leg by abruptly reducing the maximum torque of its ... | p. 7 (A. Simulation Experiments) |
| body limitation/failure cue | This dynamic redistribution of effort ensures continuous and stable locomotion even under single leg failures. | p. 7 (A. Simulation Experiments) |
| body limitation/failure cue | 7, the robot's controller exhibited robust performance, successfully resisting these disturbances across all four legs ‘without overreacting. | p. 8 (4) Front eg sweep) |
| body limitation/failure cue | In the first subsection, we illustrate the compliance of our method during humanrobot interactions, while Sections V-B2 and V-B3 highlight its robustness against external ... | p. 8 (4) Front eg sweep) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This framework enables high-throughput simulation, allowing us to simulate 4096 instances of the GO2 robot in parallel on a single NVIDIA RTX 4090 GPU. | p. 6 (A. Implementation of the Growth Mechanism) |
| All hyperparameters related to the growth schedule and biomechanical model are summarized in Table IIL | p. 6 (A. Implementation of the Growth Mechanism) |
| ‘TABLE IV PERFORMANCE COMPARISON BETWEEN OUR METHOD AND BASELINES ACROSS DIFFERENT ROBUSTNESS TESTS (5 TRIALS FER TEST) | p. 7 (A. Simulation Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 1 Saco case - extractive PDF cue:** [Locomotion on wet slippery surfaces, showing both sucess (a) and failure (b), Even when the foot ofthe robot sip and fall down in Tile cases, ...
- **p. 9 / 1 Saco case - extractive PDF cue:** In contrast, Figure 11b shows a failure case, where the robot is given an abrupt command on the slippery surface.
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** 2) Robustness to Single-Leg Failure: In this experiment, we simulate the failure of a single leg by abruptly reducing the maximum torque of its motor ...
- **p. 7 / A. Simulation Experiments - extractive PDF cue:** This dynamic redistribution of effort ensures continuous and stable locomotion even under single leg failures.
- **p. 8 / 4) Front eg sweep - extractive PDF cue:** 7, the robot's controller exhibited robust performance, successfully resisting these disturbances across all four legs ‘without overreacting.
- **p. 8 / 4) Front eg sweep - extractive PDF cue:** In the first subsection, we illustrate the compliance of our method during humanrobot interactions, while Sections V-B2 and V-B3 highlight its robustness against external disturbances.

- **PDF anchors reviewed:** datasets p. 7 (B. Lab Level Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 5 (A. Implementation of the Growth Mechanism), metrics p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments), p. 5 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Implementation of the Growth Mechanism), p. 5 (A. Implementation of the Growth Mechanism), baselines p. 7 (B. Lab Level Experiments), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Simulation Experiments), results p. 7 (A. Simulation Experiments), p. 7 (A. Simulation Experiments), p. 6 (A. Implementation of the Growth Mechanism), p. 6 (A. Simulation Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
