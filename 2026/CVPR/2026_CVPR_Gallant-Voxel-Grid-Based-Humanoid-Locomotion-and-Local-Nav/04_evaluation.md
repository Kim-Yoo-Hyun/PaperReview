# Evaluation - Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2.3. Result), p. 7 (4.2.3. Result), p. 8 (4.4. Further Analyses), p. 5 (4.2.1. Metrics), p. 7 (4.3.2. Ablation), p. 8 (4.4. Further Analyses)): With all other settings fixed, Gallant achieves much higher success rates than the variant that ignores dynamic objects (w/o-Self-Scan) across all tasks.

## Evaluation Body Digest

- **p. 5 / 4.2.1. Metrics - extractive body cue:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a ...
- **p. 8 / 4.4. Further Analyses - extractive body cue:** A clear correlation emerges: terrains with higher success in simulation also perform well on hardware, validating the use of large-scale simulated evaluation as a reliable ...
- **p. 7 / 4.2.3. Result - extractive body cue:** (a) The humanoid crouches to traverse under a low ceiling; (b) Voxel grid from LiDAR simulation that includes dynamic objects captures the robot's own links; ...
- **p. 5 / 4.1. Experimental Configuration - extractive body cue:** We conduct both simulation training and real-world deployment on the 29-DoF Unitree G1 humanoid.
- **p. 6 / 4.2.3. Result - extractive body cue:** Humanoid robot traverses diverse 3D constrained terrains in both simulation and the real world.
- **p. 8 / 4.3.2. Ablation - extractive body cue:** Unlike in simulation, where HeightMap occasionally excels on Pile or Stairs, its real-world performance is hindered by noisy elevation reconstruction.
- **p. 6 / 4.2.3. Result - extractive body cue:** 5 (a), when the robot ducks under the ceiling, the voxel grids with dynamics (Fig.
- **p. 7 / 4.3.1. Deployment - extractive body cue:** Despite the diverse and complex constraints, the robot consistently traverses these terrains with high success rates (see Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Configuration (p. 5); 4.2. Simulation Experiments (p. 5); 4.2.3. Result (p. 5); 4.3. Real-world Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2.3. Result | EMPIRICAL / REAL-ROBOT OR HARDWARE | With all other settings fixed, Gallant achieves much higher success rates than the variant that ignores dynamic objects (w/o-Self-Scan) across all tasks. | p. 6 (4.2.3. Result) |
| 4.2.3. Result | EMPIRICAL / REAL-ROBOT OR HARDWARE | This Gallant configuration achieves higher success rates than Only-Voxel-Grid (critic without height map) across all tasks, validating the proposed design. | p. 7 (4.2.3. Result) |
| 4.4. Further Analyses | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rates plateau around 80%, and simulation with zero LiDAR latency improves this to over 90%, indicating that realworld sensor delay is a key ... | p. 8 (4.4. Further Analyses) |
| 4.2.1. Metrics | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within ... | p. 5 (4.2.1. Metrics) |
| 4.3.2. Ablation | EMPIRICAL / REAL-ROBOT OR HARDWARE | To evaluate sim-to-real performance, we deploy three policies on the 29-DoF Unitree G1 and compare success rates across terrains: (i) HeightMap, which replaces the ... | p. 7 (4.3.2. Ablation) |

## Dataset / Benchmark Role

- **p. 5 / 4.2.1. Metrics - extractive body cue:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a ...
- **p. 8 / 4.4. Further Analyses - extractive body cue:** A clear correlation emerges: terrains with higher success in simulation also perform well on hardware, validating the use of large-scale simulated evaluation as a reliable ...
- **p. 7 / 4.2.3. Result - extractive body cue:** (a) The humanoid crouches to traverse under a low ceiling; (b) Voxel grid from LiDAR simulation that includes dynamic objects captures the robot's own links; ...
- **p. 5 / 4.1. Experimental Configuration - extractive body cue:** We conduct both simulation training and real-world deployment on the 29-DoF Unitree G1 humanoid.
- **p. 6 / 4.2.3. Result - extractive body cue:** Humanoid robot traverses diverse 3D constrained terrains in both simulation and the real world.
- **p. 8 / 4.3.2. Ablation - extractive body cue:** Unlike in simulation, where HeightMap occasionally excels on Pile or Stairs, its real-world performance is hindered by noisy elevation reconstruction.
- **p. 6 / 4.2.3. Result - extractive body cue:** 5 (a), when the robot ducks under the ceiling, the voxel grids with dynamics (Fig.
- **p. 7 / 4.3.1. Deployment - extractive body cue:** Despite the diverse and complex constraints, the robot consistently traverses these terrains with high success rates (see Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview. Gallant enables a single policy with voxel grids to traverse diverse 3D constrained terrains in real: (a) ascend and descend stairs, (b) ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Comparison between gallant and previous methods. FoV in Solid Angles are computed by parameter of the used sensors.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. (a) Curriculum-based training over 8 representative terrains enhances generalization, and realistic voxel path alignment achieved via efficient LiDAR simulation with domain-randomized ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Parameters for generating curriculum training terrains. Terrain Type τ Term pmin τ pmax τ Ceiling
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Terrain types used to train robots in simulation(pmax τ ) We adopt a curriculum-based training strategy where ter- rain difficulty increases progressively. Each ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Simulation ablation results. We present a success rate comparison between Gallant and baselines on the eight representative terrains. The means and standard variation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Humanoid robot traverses diverse 3D constrained terrains in both simulation and the real world. (a)Traversal across the eight simulated training terrain types. (b)Ducking ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of simulation ablation analyses. (a) The humanoid crouches to traverse under a low ceiling; (b) Voxel grid from LiDAR simulation that includes ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within ... | embodiment, simulator version and control stack | p. 5 (4.2.1. Metrics), p. 8 (4.4. Further Analyses) |
| Task/environment | A clear correlation emerges: terrains with higher success in simulation also perform well on hardware, validating the use of large-scale simulated evaluation as a ... | reset, timeout, object/scene variation | p. 8 (4.4. Further Analyses), p. 7 (4.2.3. Result) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (3. Method), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within ... | definition/direction/unit from same section | p. 5 (4.2.1. Metrics) |
| To evaluate sim-to-real performance, we deploy three policies on the 29-DoF Unitree G1 and compare success rates across terrains: (i) HeightMap, which replaces the ... | definition/direction/unit from same section | p. 7 (4.3.2. Ablation) |
| This Gallant configuration achieves higher success rates than Only-Voxel-Grid (critic without height map) across all tasks, validating the proposed design. | definition/direction/unit from same section | p. 7 (4.2.3. Result) |
| With the introduction of voxel grids, scenarios like overheading (e.g., Ceiling) and lateral (e.g., Door) constraints-previously difficult for height map-based methods-become the easiest considering ... | definition/direction/unit from same section | p. 8 (4.4. Further Analyses) |
| Across eight representative terrains, Gallant attains superior success rates relative to the baselines (see Tab. | definition/direction/unit from same section | p. 5 (4.2.3. Result) |
| Success rate is reported as a percentage (e.g., 90 means 90%). | definition/direction/unit from same section | p. 6 (4.2.3. Result) |
| We present a success rate comparison between Gallant and baselines on the eight representative terrains. | definition/direction/unit from same section | p. 6 (4.2.3. Result) |
| Gallant success rate in simulation and real world. | definition/direction/unit from same section | p. 8 (4.4. Further Analyses) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Gallant consistently outperforms both baselines across all real-world terrains. | comparison identity and matched condition | p. 8 (4.3.2. Ablation) |
| This LiDAR also provides input for elevation map generation in baseline comparisons. | comparison identity and matched condition | p. 5 (4.1. Experimental Configuration) |
| We present a success rate comparison between Gallant and baselines on the eight representative terrains. | comparison identity and matched condition | p. 6 (4.2.3. Result) |
| This is compared to Gallant, which models scans over both static terrain and moving links. • Perceptual network. | comparison identity and matched condition | p. 5 (4.2.2. Baselines) |
| The HeightMap baseline fails on overheading (e.g., Ceiling) and lateral (e.g., Door) obstacles due to its limited 2.5D representation, and performs worse than Gallant ... | comparison identity and matched condition | p. 8 (4.3.2. Ablation) |
| For each ablation setting, the best-performing value per metric on each terrain is highlighted in bold. | comparison identity and matched condition | p. 6 (4.2.3. Result) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To assess the effectiveness of core components in Gallant, we compare against the following ablations: • Self-scan. | component/input/data sensitivity | p. 5 (4.2.2. Baselines) |
| The NoDR variant performs reasonably well on Ceiling and Door, suggesting low sensitivity to sensing latency in these cases. | component/input/data sensitivity | p. 8 (4.3.2. Ablation) |
| We directly deploy the Gallant-trained policy onto the real Unitree G1 humanoid without any fine-tuning. | component/input/data sensitivity | p. 7 (4.3.1. Deployment) |
| To evaluate sim-to-real performance, we deploy three policies on the 29-DoF Unitree G1 and compare success rates across terrains: (i) HeightMap, which replaces the ... | component/input/data sensitivity | p. 7 (4.3.2. Ablation) |
| Ablationspecific analyses are summarized as follow: 28090 | component/input/data sensitivity | p. 5 (4.2.3. Result) |
| For each ablation setting, the best-performing value per metric on each terrain is highlighted in bold. | component/input/data sensitivity | p. 6 (4.2.3. Result) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To scale training and narrow the simulation-to-reality (simto-real) gap, we develop a LiDAR simulation pipeline that models sensor noise and latency and enables realistic ... | With all other settings fixed, Gallant achieves much higher success rates than the variant that ignores dynamic objects (w/o-Self-Scan) across all tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2.3. Result), p. 7 (4.2.3. Result), p. 8 (4.4. Further Analyses), p. 5 (4.2.1. Metrics), p. 7 (4.3.2. Ablation), p. 8 (4.4. Further Analyses) |
| Primary metric/result | This Gallant configuration achieves higher success rates than Only-Voxel-Grid (critic without height map) across all tasks, validating the proposed design. | numeric claim only at cited anchor | p. 7 (4.2.3. Result) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Configuration - extractive body cue:** Policy training is distributed across eight NVIDIA RTX 4090 GPUs (45GB memory each).
- **p. 5 / 4.2.1. Metrics - extractive body cue:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a ...
- **p. 7 / 4.3.1. Deployment - extractive body cue:** The control loop runs at 50Hz, consistent with simulation.
- **p. 7 / 4.3.1. Deployment - extractive body cue:** To ensure reliable voxel input, raw point clouds from dual LiDARs are processed onboard using OctoMap [16], generating a binary occupancy grid at 10Hz.
- **p. 8 / 4.3.2. Ablation - extractive body cue:** Plane Ceiling Door Platform Pile Upstair Downstair 0.0 2.5 5.0 7.5 10.0 12.5 15.0 15.0 0.0 1.0 11.0 10.0 13.0 12.0 15.0 15.0 12.0 4.0 ...
- **p. 8 / 4.3.2. Ablation - extractive body cue:** Real-world traversal success times over 15 trials.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within ... | p. 5 (4.2.1. Metrics) |
| body limitation/failure cue | 1, using only a height map as the perceptual representation for policy cannot represent multilayer structure; consequently, Only-Height-Map fails on terrains such as Ceiling. | p. 7 (4.2.3. Result) |
| body limitation/failure cue | On other terrains-especially Platforms and Stairs, previously considered unstable due to collision risk [21]-Gallant achieves high success by proactively adjusting foot trajectories. | p. 8 (4.4. Further Analyses) |
| body limitation/failure cue | In real-world tests, a single LiDAR policy covers the ground obstacles handled by elevation-map controllers while also tackling lateral and overhead structures, and on ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 2. Method Overview. (a) Curriculum-based training over 8 representative terrains enhances generalization, and realistic voxel path alignment achieved via efficient LiDAR simulation with ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | 5 (b)) correctly include the robot's legs, which occupy voxels and induce occlusion "holes" along LiDAR rays to the distant floor. | p. 6 (4.2.3. Result) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During deployment, both the learned policy and voxel grid processing run entirely onboard the G1 using an NVIDIA Orin NX. | p. 5 (4.1. Experimental Configuration) |
| We train every policy for 4{,} 000 iterations, then run 5 independent evaluations (each run evaluates over 1{,} 000 complete episodes), reporting mean \pm ... | p. 5 (4.2.1. Metrics) |
| In practice, this z-grouped 2D design delivers equal or better accuracy with markedly lower compute, making it the most suitable choice for our task. | p. 7 (4.2.3. Result) |
| These results highlight Gallant's ability to encode spatial constraints from perception and translate them into robust, real-time whole-body behaviors. | p. 7 (4.3.1. Deployment) |
| Real-world traversal success times over 15 trials. | p. 8 (4.3.2. Ablation) |
| Each policy is tested over 15 trials per terrain, with results shown in Fig. | p. 8 (4.3.2. Ablation) |
| To mitigate this, we precompute a BVH for each mesh in its local (body) frame. | p. 3 (3.2. Efficient LiDAR Simulation) |
| Most GPU-based simulators, such as IsaacGym and IsaacSim, either lack native support for efficient LiDAR simulation or are limited to scanning a single static ... | p. 3 (3.2. Efficient LiDAR Simulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.2.1. Metrics - extractive body cue:** 4.1), and the policy performance is measured by two distinct metrics: • Success rate E_{\mathrm {succ}}: fraction of episodes that reach the target within a ...
- **p. 7 / 4.2.3. Result - extractive body cue:** 1, using only a height map as the perceptual representation for policy cannot represent multilayer structure; consequently, Only-Height-Map fails on terrains such as Ceiling.
- **p. 8 / 4.4. Further Analyses - extractive body cue:** On other terrains-especially Platforms and Stairs, previously considered unstable due to collision risk [21]-Gallant achieves high success by proactively adjusting foot trajectories.
- **p. 8 / 5. Conclusion - extractive body cue:** In real-world tests, a single LiDAR policy covers the ground obstacles handled by elevation-map controllers while also tackling lateral and overhead structures, and on ground-only ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. (a) Curriculum-based training over 8 representative terrains enhances generalization, and realistic voxel path alignment achieved via efficient LiDAR simulation with domain-randomized ...
- **p. 6 / 4.2.3. Result - extractive body cue:** 5 (b)) correctly include the robot's legs, which occupy voxels and induce occlusion "holes" along LiDAR rays to the distant floor.

- **Evidence anchors reviewed:** datasets p. 5 (4.2.1. Metrics), p. 8 (4.4. Further Analyses), p. 7 (4.2.3. Result), p. 5 (4.1. Experimental Configuration), p. 6 (4.2.3. Result), p. 8 (4.3.2. Ablation), metrics p. 5 (4.2.1. Metrics), p. 7 (4.3.2. Ablation), p. 7 (4.2.3. Result), p. 8 (4.4. Further Analyses), p. 5 (4.2.3. Result), p. 6 (4.2.3. Result), baselines p. 8 (4.3.2. Ablation), p. 5 (4.1. Experimental Configuration), p. 6 (4.2.3. Result), p. 5 (4.2.2. Baselines), p. 8 (4.3.2. Ablation), p. 6 (4.2.3. Result), results p. 6 (4.2.3. Result), p. 7 (4.2.3. Result), p. 8 (4.4. Further Analyses), p. 5 (4.2.1. Metrics), p. 7 (4.3.2. Ablation), p. 8 (4.4. Further Analyses).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
