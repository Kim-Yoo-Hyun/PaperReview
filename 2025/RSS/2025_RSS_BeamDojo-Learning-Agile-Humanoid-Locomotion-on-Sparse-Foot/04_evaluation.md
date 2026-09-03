# Evaluation - BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p068.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p068.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 8 (B. Simulation Experiments), p. 8 (B. Simulation Experiments), p. 10 (Figure/Table caption), p. 6 (evaluation)): 1) Quantitative results: We report the success rate (Race) and traverse rate (R,9y) for four terrains at medium and hard difficulty levels (terrain level 6 and level 8, respectively) in ...

## Evaluation Body Digest

- **p. 6 / evaluation - extractive body cue:** 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work.
- **p. 7 / A. Experimental Setup - extractive body cue:** ‘TABLE I: Benchmarked Comparison in Simulation.
- **p. 5 / evaluation - extractive body cue:** This terrain requires the robot to make large steps to cross, the gaps.
- **p. 5 / evaluation - extractive body cue:** We begin by training the robot on the Stones Everywhere terrain in Stage 1 with soft terrain constraints to develop generalizable policy.
- **p. 6 / evaluation - extractive body cue:** To address this, we followed [34] to construct a robotcentric, complete, and robust elevation map.
- **p. 7 / A. Experimental Setup - extractive body cue:** The foothold error benchmarks of all methods are evaluated in (a) stepping stones and (b) balancing
- **p. 8 / B. Simulation Experiments - extractive body cue:** 6, Both the two-stage training setup and the double critic improve learning efficiency, with the two-stage setup contributing the ‘most.
- **p. 7 / B. Simulation Experiments - extractive body cue:** single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** evaluation (p. 5); V. EXPERIMENTS (p. 6); A. Experimental Setup (p. 6); B. Simulation Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1) Quantitative results: We report the success rate (Race) and traverse rate (R,9y) for four terrains at medium and hard difficulty levels (terrain level ... | p. 7 (B. Simulation Experiments) |
| A. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4 Success Rate Raocc: The percentage of successful at | p. 7 (A. Experimental Setup) |
| B. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, ‘our method and the ablation with double critic demonstrates superior motion smoothness and improved feet clearance. | p. 8 (B. Simulation Experiments) |
| B. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6, Both the two-stage training setup and the double critic improve learning efficiency, with the two-stage setup contributing the ‘most. | p. 8 (B. Simulation Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: Failure Case Analysis. We evaluate the success rate on varying (a) stove sizes, and (b) step distances. | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / evaluation - extractive body cue:** 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work.
- **p. 7 / A. Experimental Setup - extractive body cue:** ‘TABLE I: Benchmarked Comparison in Simulation.
- **p. 5 / evaluation - extractive body cue:** This terrain requires the robot to make large steps to cross, the gaps.
- **p. 5 / evaluation - extractive body cue:** We begin by training the robot on the Stones Everywhere terrain in Stage 1 with soft terrain constraints to develop generalizable policy.
- **p. 6 / evaluation - extractive body cue:** To address this, we followed [34] to construct a robotcentric, complete, and robust elevation map.
- **p. 7 / A. Experimental Setup - extractive body cue:** The foothold error benchmarks of all methods are evaluated in (a) stepping stones and (b) balancing
- **p. 8 / B. Simulation Experiments - extractive body cue:** 6, Both the two-stage training setup and the double critic improve learning efficiency, with the two-stage setup contributing the ‘most.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Foothold Reward. We sample n points under the foot. Green points indicate contact with the surface within the safe region, while red points ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Terrain Setting in Simulation. (a) is used for stage 1 taining, while (b) and (c) are used for stage 2 taining. The training ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Foothold Error Comparison. The foothold error benchmarks of all methods are evaluated in (a) stepping stones and (b) balancing
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Learning Efficiency. The learning curves show the maximum terrain levels achieved in two training stages of all methods. Faster attainment of terrain level ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Foot Placement Planning Visualization. We illustrate (wo trajectories forthe foot placement process: the yellow line represents BEAMDOvO, while the red line corresponds to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Real-world Experiments. We build terrains inthe real world similar to those in simulation. (a) Stepping Stones: stones with a size of 20 cm, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Robustness Test. We evaluate the robusiness of the humanoid robot in real-world scenarios with: (a) heavy payload, (b) external
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Generalization ‘Test on Non-Flat Terrains. We conduct real-world experiments on (a) stairs with a width of 2Sem and a height of 15cm, and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work. | embodiment, simulator version and control stack | p. 6 (evaluation), p. 7 (A. Experimental Setup) |
| Task/environment | ‘TABLE I: Benchmarked Comparison in Simulation. | reset, timeout, object/scene variation | p. 7 (A. Experimental Setup), p. 5 (evaluation) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 5 (C. Learning Terrain-Aware Locomotion via Two-Stage RL), p. 4 (C. Learning Terrain-Aware Locomotion via Two-Stage RL) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 1 (Abstract), p. 2 (1. INrRopucTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains. | definition/direction/unit from same section | p. 7 (B. Simulation Experiments) |
| 4 Success Rate Raocc: The percentage of successful at | definition/direction/unit from same section | p. 7 (A. Experimental Setup) |
| Fig. 11: Failure Case Analysis. We evaluate the success rate on varying (a) stove sizes, and (b) step distances. | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| We additionally add our foothold reward risaseis 10 encourage the humanoid to step accurately on the foothold areas. | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| VE (ois) Time Cost (6) Average Speed (ws) Error Rate (1) | definition/direction/unit from same section | p. 8 (B. Simulation Experiments) |
| Meanwhile, the double-critic setup separates the foothold reward from the locomotion rewards, ensuring that its updates remain unaffected by the noise of unstable locomotion ... | definition/direction/unit from same section | p. 8 (B. Simulation Experiments) |
| The only addition is the foothold reward. | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| Fig. 2: Foothold Reward. We sample n points under the foot. Green points indicate contact with the surface within the safe region, while red ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This requires a distinct gait compared to regular Jocomotion tasks. | comparison identity and matched condition | p. 5 (evaluation) |
| We compare our proposed framework BEAMDOsO, which integrates two-stage RL training and a double critic, with the following baselines: | comparison identity and matched condition | p. 6 (A. Experimental Setup) |
| 4) use soft terrain dynamics constrains, while all other baselines use hard terrain dynamics constraints. | comparison identity and matched condition | p. 7 (A. Experimental Setup) |
| ‘observations are as follows: «+ Leveraging the efficient two-stage RL framework and the double critic, BEAMDOsO consistently outperforms, | comparison identity and matched condition | p. 7 (B. Simulation Experiments) |
| Gait Regularization: The combination of small-scale gait regularization rewards with sparse foothold reward can hinder gait performance, as shown in Table Ill, where the ... | comparison identity and matched condition | p. 8 (B. Simulation Experiments) |
| This terrain is challenging for the robot as it must learn to keep its feet together on the beams without colliding with each other, ... | comparison identity and matched condition | p. 5 (evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Gait Regularization: The combination of small-scale gait regularization rewards with sparse foothold reward can hinder gait performance, as shown in Table Ill, where the ... | component/input/data sensitivity | p. 8 (B. Simulation Experiments) |
| BL 3) Ours w/o Soft Dyn: This is an ablation which removing the first stage of training with soft terrain dynamics, constraints | component/input/data sensitivity | p. 6 (A. Experimental Setup) |
| This terrain is challenging for the robot as it must learn to keep its feet together on the beams without colliding with each other, ... | component/input/data sensitivity | p. 5 (evaluation) |
| BL 4) Ours w/o Double Critie: This is an ablation which uses a single critic to handle both locomotion rewards and foothold reward, instead ... | component/input/data sensitivity | p. 6 (A. Experimental Setup) |
| 2) Detailed Ablation Analysis: We conduct additional ablation studies by comparing BEAMDO4O with BL. | component/input/data sensitivity | p. 7 (B. Simulation Experiments) |
| single-stage approaches and ablation designs, achieving, high success rates and low foothold errors across all ‘challenging terrains. | component/input/data sensitivity | p. 7 (B. Simulation Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we introduce BEAMDOJO, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. | 1) Quantitative results: We report the success rate (Race) and traverse rate (R,9y) for four terrains at medium and hard difficulty levels (terrain level ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 8 (B. Simulation Experiments), p. 8 (B. Simulation Experiments), p. 10 (Figure/Table caption), p. 6 (evaluation) |
| Primary metric/result | 4 Success Rate Raocc: The percentage of successful at | numeric claim only at cited anchor | p. 7 (A. Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 6 / evaluation - extractive body cue:** The robot weighs 35 kg. stands 1.32 meters tall, and features 23 actuated degrees of freedom: 6 in each leg, 5 in each arm, and ...
- **p. 6 / evaluation - extractive body cue:** During deployment, the elevation map publishes information ata frequency of 10 Hz, while the learned policy operates at 50 Hz.
- **p. 6 / evaluation - extractive body cue:** The policy's action outputs are subsequently sent to 4 PD controller, which runs at 500 Hz, ensuring smooth and precise actuation
- **p. 5 / C. Learning Terrain-Aware Locomotion via Two-Stage RL - extractive body cue:** This map samples 15 > 15 points within a 0.1 m grid in both the longitudinal and lateral directions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in ... | p. 10 (7 Single Leg Support ) Stand Still) |
| body limitation/failure cue | Meanwhile, the double-critic setup separates the foothold reward from the locomotion rewards, ensuring that its updates remain unaffected by the noise of unstable locomotion ... | p. 8 (B. Simulation Experiments) |
| body limitation/failure cue | Fig. 11: Failure Case Analysis. We evaluate the success rate on varying (a) stove sizes, and (b) step distances. | p. 10 (Figure/Table caption) |
| body limitation/failure cue | before falling to the total terrain length (8 m). | p. 7 (A. Experimental Setup) |
| body limitation/failure cue | This advantage is achieved by leveraging LiDAR to its full potential, whereas a single depth camera, cannot handle such scenarios. | p. 8 (10 3 oss Liss) |
| body limitation/failure cue | ‘We compare this approach with other binary and coarse reward designs: when p% of the sampled points fall outside the safe area, a full ... | p. 9 (7 Single Leg Support ) Stand Still) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| BEAMDOJO further incorporates a two-stage approach to encourage fully trial-and-error exploration, In the first stage, terrain dynamics constraints are relaxed, allowing the humanoid robot ... | p. 2 (1. INrRopucTION) |
| This terrain requires the robot to make large steps to cross, the gaps. | p. 5 (evaluation) |
| This is an naive implementation to solve this task | p. 6 (A. Experimental Setup) |
| 1) Hardware Setup: We use Unitree G1 humanoid robot for our experiments in this work. | p. 6 (evaluation) |
| e123 5 7 0 ‘Training Steps (&) "= Naive + Ours wio Sot Dyn + Ours wio Double Critic ->- Ours | p. 7 (B. Simulation Experiments) |
| In comparison, the naive implementation shows higher error rates, with a substantial proportion of foot placements landing outside the safe foothold areas. | p. 7 (B. Simulation Experiments) |
| In contrast, the naive implementation struggles to reach higher terrain levels in both stages. | p. 8 (B. Simulation Experiments) |
| The advantage of two-stage learning lies in its ability to allow the agent to continuously attempt foot placements, even in the presence of missteps, ... | p. 8 (B. Simulation Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 7 Single Leg Support ) Stand Still - extractive body cue:** 5) Failure Cases: ‘To investigate the framework's perfor- ‘mance limitations, we evaluate its performance across varying. stone sizes and step distances, as shown in Fig.
- **p. 8 / B. Simulation Experiments - extractive body cue:** Meanwhile, the double-critic setup separates the foothold reward from the locomotion rewards, ensuring that its updates remain unaffected by the noise of unstable locomotion signals, ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 11: Failure Case Analysis. We evaluate the success rate on varying (a) stove sizes, and (b) step distances.
- **p. 7 / A. Experimental Setup - extractive body cue:** before falling to the total terrain length (8 m).
- **p. 8 / 10 3 oss Liss - extractive body cue:** This advantage is achieved by leveraging LiDAR to its full potential, whereas a single depth camera, cannot handle such scenarios.
- **p. 9 / 7 Single Leg Support ) Stand Still - extractive body cue:** ‘We compare this approach with other binary and coarse reward designs: when p% of the sampled points fall outside the safe area, a full penalty ...

- **Evidence anchors reviewed:** datasets p. 6 (evaluation), p. 7 (A. Experimental Setup), p. 5 (evaluation), p. 5 (evaluation), p. 6 (evaluation), p. 7 (A. Experimental Setup), metrics p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 10 (Figure/Table caption), p. 6 (A. Experimental Setup), p. 8 (B. Simulation Experiments), p. 8 (B. Simulation Experiments), baselines p. 5 (evaluation), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 7 (B. Simulation Experiments), p. 8 (B. Simulation Experiments), p. 5 (evaluation), results p. 7 (B. Simulation Experiments), p. 7 (A. Experimental Setup), p. 8 (B. Simulation Experiments), p. 8 (B. Simulation Experiments), p. 10 (Figure/Table caption), p. 6 (evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
