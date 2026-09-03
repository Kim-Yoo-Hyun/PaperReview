# Evaluation - RMA: Rapid Motor Adaptation for Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.04034; PDF retrieval source: https://arxiv.org/pdf/2107.04034. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 7 (IV. EXPERIMENTAL SETUP)): Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall grass and dirt pile without ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Environment Details Hardware Details: We use A1 robot from Unitree for all our real-world experiments.
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each RL episode lasts for a maximum of 1000 steps, with early termination if the height of the robots drops below 0.28m, magnitude of the ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** For reference, A1 robot weights 12Kg.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Learning Base Policy and Environmental Factor Encoder Network: We jointly train the base policy and the environment encoder network using PPO [48] for 15, 000 ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** 4: We analyze RMA as the robot walks over an oily plastic sheet with additional plastic covering on its feet.
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** When the robot enters the slippery patch we see a change in the two components of the extrinsics vector ˆz, indicating that the slip event ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** We find that RMA steps down a height of 15cm with 80% success rate and walks over unseen deformable surfaces, such as a memory foam ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** IV. EXPERIMENTAL SETUP (p. 5); V. RESULTS AND ANALYSIS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, ... | p. 1 (Figure/Table caption) |
| IV. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | We find that RMA steps down a height of 15cm with 80% success rate and walks over unseen deformable surfaces, such as a memory ... | p. 6 (IV. EXPERIMENTAL SETUP) |
| IV. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is also able to successfully climb inclines and steps. | p. 6 (IV. EXPERIMENTAL SETUP) |
| V. RESULTS AND ANALYSIS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This is an upper bound to the performance of RMA. | p. 7 (V. RESULTS AND ANALYSIS) |
| IV. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | RMA was successful in 90% of the runs over oily patch. | p. 7 (IV. EXPERIMENTAL SETUP) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Environment Details Hardware Details: We use A1 robot from Unitree for all our real-world experiments.
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each RL episode lasts for a maximum of 1000 steps, with early termination if the height of the robots drops below 0.28m, magnitude of the ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** For reference, A1 robot weights 12Kg.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Learning Base Policy and Environmental Factor Encoder Network: We jointly train the base policy and the environment encoder network using PPO [48] for 15, 000 ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** 4: We analyze RMA as the robot walks over an oily plastic sheet with additional plastic covering on its feet.
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** When the robot enters the slippery patch we see a change in the two components of the extrinsics vector ˆz, indicating that the slip event ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: RMA consists of two subsystems - the base policy π and the adaptation module φ. Top: RMA is trained in two phases. In ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: We evaluate RMA in several out-of-distribution setups in the real world. We compare RMA to A1's controller and RMA without the adaptation module. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: We analyze RMA as the robot walks over an oily plastic sheet with additional plastic covering on its feet. We plot the torque ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Environment Details Hardware Details: We use A1 robot from Unitree for all our real-world experiments. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (IV. EXPERIMENTAL SETUP) |
| Task/environment | Each RL episode lasts for a maximum of 1000 steps, with early termination if the height of the robots drops below 0.28m, magnitude of ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 2 (10 Hz), p. 5 (B. Adaptation Module) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 2 (10 Hz), p. 5 (B. Adaptation Module) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We find that RMA steps down a height of 15cm with 80% success rate and walks over unseen deformable surfaces, such as a memory ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL SETUP) |
| The coefficient of the reward terms are provided in Section III. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL SETUP) |
| We import the A1 URDF file from Unitree [53] and use the inbuilt fractal terrain generator to generate uneven terrain (fractal octaves = 2, ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL SETUP) |
| This is an upper bound to the performance of RMA. | definition/direction/unit from same section | p. 7 (V. RESULTS AND ANALYSIS) |
| RMA was successful in 90% of the runs over oily patch. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTAL SETUP) |
| Fig. 2: RMA consists of two subsystems - the base policy π and the adaptation module φ. Top: RMA is trained in two phases. ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Overall, the proposed method consistently dominates the baseline methods. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL SETUP) |
| We compare the performance of RMA with several baselines in simulation (Table II). | comparison identity and matched condition | p. 7 (V. RESULTS AND ANALYSIS) |
| We compare RMA to A1's controller and RMA without the adaptation module. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL SETUP) |
| 2) Robustness through Domain Randomization (Robust): The base policy is trained without zt to be robust to the variations in the training range [52, ... | comparison identity and matched condition | p. 7 (V. RESULTS AND ANALYSIS) |
| Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| We compare RMA to A1's controller and RMA without the adaptation module. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTAL SETUP) |
| 2) Robustness through Domain Randomization (Robust): The base policy is trained without zt to be robust to the variations in the training range [52, ... | component/input/data sensitivity | p. 7 (V. RESULTS AND ANALYSIS) |
| 4) RMA w/o Adaptation: We can also evaluate the performance of the base policy without the adaptation module to ablate the importance of the ... | component/input/data sensitivity | p. 7 (V. RESULTS AND ANALYSIS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The combination of these components enables the robot to adapt to novel situations in fractions of a second. | Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 7 (IV. EXPERIMENTAL SETUP) |
| Primary metric/result | We find that RMA steps down a height of 15cm with 80% success rate and walks over unseen deformable surfaces, such as a memory ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTAL SETUP) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** It has 18 degrees of freedom out of which 12 are actuated (3 motors on each leg) and weighs about 12 kg.
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each RL episode lasts for a maximum of 1000 steps, with early termination if the height of the robots drops below 0.28m, magnitude of the ...
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** The control frequency of the policy is 100 Hz, and the simulation time step is 0.025s.
- **p. 5 / IV. EXPERIMENTAL SETUP - extractive body cue:** For actions, we use position control for the 12 robot joints.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Success TTF Distance RMA 100 1 1 RMA w/o Adapt 20 1 0.6 A1 100 1 1 RMA 100 1 1 RMA w/o Adapt 0 ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The numbers reported are averaged over 5 trials. moves.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Fig. 3: We evaluate RMA in several out-of-distribution setups in the real world. We compare RMA to A1's controller and RMA without the adaptation ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | The controller was destabilized by unstable footholds in most of its failures. | p. 8 (6) Advantage Weighted Regression for Domain Adaptation) |
| body limitation/failure cue | Each trial of StepUp-n and StepDown-n is terminated after a success or a failure. | p. 8 (6) Advantage Weighted Regression for Domain Adaptation) |
| body limitation/failure cue | When the robot enters the slippery patch we see a change in the two components of the extrinsics vector ˆz, indicating that the slip ... | p. 7 (IV. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Note that post adaptation, the recovered gait time period is similar to the original, the torque magnitudes have increased and ˆz continues to capture ... | p. 7 (IV. EXPERIMENTAL SETUP) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run the optimization process for 1000 iterations with a learning rate of 5e-4 each of which uses a batch size of 80, 000 ... | p. 6 (IV. EXPERIMENTAL SETUP) |
| Learning Base Policy and Environmental Factor Encoder Network: We jointly train the base policy and the environment encoder network using PPO [48] for 15, ... | p. 6 (IV. EXPERIMENTAL SETUP) |
| That is at runtime, but at training time, life is easier. | p. 3 (10 Hz) |
| Environment Details Hardware Details: We use A1 robot from Unitree for all our real-world experiments. | p. 5 (IV. EXPERIMENTAL SETUP) |
| Each RL episode lasts for a maximum of 1000 steps, with early termination if the height of the robots drops below 0.28m, magnitude of ... | p. 5 (IV. EXPERIMENTAL SETUP) |
| Note that if a method drastically failed at a task, we only run two trials and then report a failure. | p. 8 (6) Advantage Weighted Regression for Domain Adaptation) |
| We run 5 trials for each method and report the success rate, time to fall (TTF), and distance covered. | p. 8 (6) Advantage Weighted Regression for Domain Adaptation) |
| The robot is successfully able to walk on sand, mud, hiking trails, tall grass and dirt pile without a single failure in all our ... | p. 1 (Body text (section boundary not confidently recovered)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: We evaluate RMA in several out-of-distribution setups in the real world. We compare RMA to A1's controller and RMA without the adaptation module. ...
- **p. 8 / 6) Advantage Weighted Regression for Domain Adaptation - extractive body cue:** The controller was destabilized by unstable footholds in most of its failures.
- **p. 8 / 6) Advantage Weighted Regression for Domain Adaptation - extractive body cue:** Each trial of StepUp-n and StepDown-n is terminated after a success or a failure.
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** When the robot enters the slippery patch we see a change in the two components of the extrinsics vector ˆz, indicating that the slip event ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Note that post adaptation, the recovered gait time period is similar to the original, the torque magnitudes have increased and ˆz continues to capture the ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (IV. EXPERIMENTAL SETUP), p. 7 (IV. EXPERIMENTAL SETUP), metrics p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 5 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 7 (IV. EXPERIMENTAL SETUP), baselines p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 1 (Figure/Table caption), results p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 7 (IV. EXPERIMENTAL SETUP).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall grass and dirt pile without ... (p. 1, Figure/Table caption).
- **Metric evidence:** We find that RMA steps down a height of 15cm with 80% success rate and walks over unseen deformable surfaces, such as a memory foam mattress and a slightly uneven ... (p. 6, IV. EXPERIMENTAL SETUP).
- **Baseline/ablation evidence:** We compare RMA to A1's controller and RMA without the adaptation module. (p. 6, IV. EXPERIMENTAL SETUP).
- **Failure/negative evidence:** RMA w/o adaptation fails to move for payloads more than 8Kg, but rarely falls. (p. 6, IV. EXPERIMENTAL SETUP).
