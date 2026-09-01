# Evaluation - Extreme Parkour with Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14341; PDF retrieval source: https://arxiv.org/pdf/2309.14341. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Results), p. 8 (4 Results), p. 9 (4 Results), p. 9 (4 Results), p. 7 (4 Results)): In addition, its feet clearance also helps it to achieve some performance with noisy measurements.

## Evaluation Body Digest

- **p. 9 / 4 Results - extractive body cue:** Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world comparisons instead.
- **p. 7 / 4 Results - extractive body cue:** 4.1 Experimental Setup We use the Unitree A1 robot with 12 joints.
- **p. 7 / 4 Results - extractive body cue:** 4.2.1 High jump Our robot is able to jump on a gym box 0.5m high (Fig.
- **p. 8 / 4 Results - extractive body cue:** Our robot can seamlessly transition between walking on four and its front two legs (Fig.
- **p. 8 / 4 Results - extractive body cue:** Our robot learns to make these adjustments and is even able to do a handstand walk on soft deformable grass with gentle slopes (Fig.
- **p. 9 / 4 Results - extractive body cue:** Robot Height Robot Height Robot Length Figure 7: For each terrain, we run 5 trials and record the number of successes.
- **p. 9 / 4 Results - extractive body cue:** We find that ours has much higher success rate in all environments.
- **p. 9 / 4 Results - extractive body cue:** Each method is run for 5 trials on each terrain for each difficulty and the success rate is recorded (Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 4 Results (p. 2); 4 Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition, its feet clearance also helps it to achieve some performance with noisy measurements. | p. 8 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world. | p. 8 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that ours has much higher success rate in all environments. | p. 9 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Each method is run for 5 trials on each terrain for each difficulty and the success rate is recorded (Fig. | p. 9 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.2 Emergent results 80cm (2x robot) Figure 5: Keyframes from a long jump (2x robot length) Our simple reward functions impose no priors and ... | p. 7 (4 Results) |

## Dataset / Benchmark Role

- **p. 9 / 4 Results - extractive body cue:** Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world comparisons instead.
- **p. 7 / 4 Results - extractive body cue:** 4.1 Experimental Setup We use the Unitree A1 robot with 12 joints.
- **p. 7 / 4 Results - extractive body cue:** 4.2.1 High jump Our robot is able to jump on a gym box 0.5m high (Fig.
- **p. 8 / 4 Results - extractive body cue:** Our robot can seamlessly transition between walking on four and its front two legs (Fig.
- **p. 8 / 4 Results - extractive body cue:** Our robot learns to make these adjustments and is even able to do a handstand walk on soft deformable grass with gentle slopes (Fig.
- **p. 9 / 4 Results - extractive body cue:** Robot Height Robot Height Robot Length Figure 7: For each terrain, we run 5 trials and record the number of successes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Extreme Parkour: Low-cost robot with imprecise actuation can perform precise athletic behaviors directly from a high-dimensional image without any explicit mapping and planning. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison of parkour setups. Starred papers in 2nd and 3rd row are concurrent works (recently released). The numbers in Climb and Gap denote ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Training overview. In phase 1, we use RL to learn a locomotion policy with access to privileged information like environment parameters and scandots ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Terrains in simulation with red dots indicating waypoints that are used to get heading direction. well to real settings. We therefore add a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Key frames of our robot executing a very high jump (2x its height). We note the emergent foot placement, power generated through hind ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Keyframes from a long jump (2x robot length) Our simple reward functions impose no priors and the robot is free to learn emergent ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Transition from quadrupedal walk- ing to bipedal walking. Our robot can seamlessly transition between walking on four and its front two legs (Fig. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: We create a simulated obstacle course consisting of versions of each terrain arranged in increasing levels of difficulty and measure the average displacement ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world comparisons instead. | embodiment, simulator version and control stack | p. 9 (4 Results), p. 7 (4 Results) |
| Task/environment | 4.1 Experimental Setup We use the Unitree A1 robot with 12 joints. | reset, timeout, object/scene variation | p. 7 (4 Results), p. 7 (4 Results) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 6 (3 Method) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 6 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We find that ours has much higher success rate in all environments. | definition/direction/unit from same section | p. 9 (4 Results) |
| Each method is run for 5 trials on each terrain for each difficulty and the success rate is recorded (Fig. | definition/direction/unit from same section | p. 9 (4 Results) |
| Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain ... | definition/direction/unit from same section | p. 8 (4 Results) |
| 4.2 Emergent results 80cm (2x robot) Figure 5: Keyframes from a long jump (2x robot length) Our simple reward functions impose no priors and ... | definition/direction/unit from same section | p. 7 (4 Results) |
| First, we test our reward design and overall pipeline (Tab. | definition/direction/unit from same section | p. 8 (4 Results) |
| We illustrate three such examples in Fig. | definition/direction/unit from same section | p. 7 (4 Results) |
| Figure 2: Training overview. In phase 1, we use RL to learn a locomotion policy with access to privileged information like environment parameters and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We find that our method outperforms the baselines in terms of both metrics. | comparison identity and matched condition | p. 8 (4 Results) |
| We find that ours is very close to the upper bound which receives oracle direction commands and it does much better in terms of ... | comparison identity and matched condition | p. 9 (4 Results) |
| Table 3: Ours reaches almost the same per- formance as oracle yaw angles as inputs. Both and Mask work poorly because the noisy yaw ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| 4.3 Comparison to Baselines We propose two sets of baselines to experimentally verify different parts of our system. | comparison identity and matched condition | p. 8 (4 Results) |
| Figure 1: Extreme Parkour: Low-cost robot with imprecise actuation can perform precise athletic behaviors directly from a high-dimensional image without any explicit mapping and ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 1: Comparison of parkour setups. Starred papers in 2nd and 3rd row are concurrent works (recently released). The numbers in Climb and Gap ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1: Extreme Parkour: Low-cost robot with imprecise actuation can perform precise athletic behaviors directly from a high-dimensional image without any explicit mapping and ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| 2 with velocity tracking in base frame used in [2]. • No feet clearance penalty (NoClear): Removes the penalization for stepping near the edges ... | component/input/data sensitivity | p. 8 (4 Results) |
| Due to the robustness of the handstand policy, our robot is able to descend stairs in a handstand pose without vision and stabilize against ... | component/input/data sensitivity | p. 8 (4 Results) |
| NoClear is trained without feet edge penalty and therefore steps very close to the edge which is unstable and often falls. | component/input/data sensitivity | p. 9 (4 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method. | In addition, its feet clearance also helps it to achieve some performance with noisy measurements. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Results), p. 8 (4 Results), p. 9 (4 Results), p. 9 (4 Results), p. 7 (4 Results) |
| Primary metric/result | NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world. | numeric claim only at cited anchor | p. 8 (4 Results) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Results - extractive body cue:** For exteroception, we use the Intel RealSense D435 inside the head of the robot which captures images at 10±2Hz.
- **p. 7 / 4 Results - extractive body cue:** We run both depth backbone (10Hz) and the base policy (50Hz) on the Jetson NX and communicate via UDP.
- **p. 7 / 4 Results - extractive body cue:** We preprocess the image by cropping dead pixels from the left hand side and downsampling to 58×87.
- **p. 7 / 4 Results - extractive body cue:** We enforce a constant depth latency of 0.08s to prevent jitter.
- **p. 7 / 4 Results - extractive body cue:** Similarly, proprioception latency is fixed at 0.016s.
- **p. 7 / 4 Results - extractive body cue:** The deployable policy can be trained on a single 3090 GPU in less than 20 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain ... | p. 8 (4 Results) |
| body limitation/failure cue | These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail. | p. 9 (4 Results) |
| body limitation/failure cue | NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world. | p. 8 (4 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each method is run for 5 trials on each terrain for each difficulty and the success rate is recorded (Fig. | p. 9 (4 Results) |
| Robot Height Robot Height Robot Length Figure 7: For each terrain, we run 5 trials and record the number of successes. | p. 9 (4 Results) |
| W is sampled randomly in {0,1} at training time and controlled via remote at deployment time. | p. 6 (3 Method) |
| Instead of randomly sampling directions, we compute direction using waypoints placed on the terrain (Fig. | p. 5 (3 Method) |
| The velocity tracking reward is then computed as rtracking = min(⟨v, ˆdw⟩,vcmd) (2) where v ∈R2 is the robot's current velocity in world frame ... | p. 5 (3 Method) |
| The deployable policy can be trained on a single 3090 GPU in less than 20 hours. | p. 7 (4 Results) |
| We run both depth backbone (10Hz) and the base policy (50Hz) on the Jetson NX and communicate via UDP. | p. 7 (4 Results) |
| 4.3.1 Simulation results For each terrain-tilted ramps, steps, gaps and hurdles we create an obstacle course consisting of each arranged in increasing difficulty in ... | p. 8 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on ...
- **p. 8 / 4 Results - extractive body cue:** Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain geometry ...
- **p. 9 / 4 Results - extractive body cue:** These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail.
- **p. 8 / 4 Results - extractive body cue:** NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world.

- **PDF anchors reviewed:** datasets p. 9 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), p. 9 (4 Results), metrics p. 9 (4 Results), p. 9 (4 Results), p. 8 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 7 (4 Results), baselines p. 8 (4 Results), p. 9 (4 Results), p. 9 (Figure/Table caption), p. 8 (4 Results), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 8 (4 Results), p. 8 (4 Results), p. 9 (4 Results), p. 9 (4 Results), p. 7 (4 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
