# Evaluation - Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (53 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/prl/publication/isaaclab2025/; PDF retrieval source: https://research.nvidia.com/labs/prl/publication/isaaclab2025/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 33 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption), p. 26 (Figure/Table caption), p. 29 (5.5.2. SkillGen-based Dataset Augmentation), p. 39 (7.1.3. Solver Implementations)): Figure 27: Assembly Environments in Isaac Lab (Tang et al., 2023). Left: Simulation. Right: Real World. The Factory environments combine SDF-based con- tact generation, a contact reduction technique, and a ...

## Evaluation Body Digest

- **p. 41 / 7.2.2. Assembly Benchmark - extractive body cue:** Isaac Lab provides optimized environments for evaluating and benchmarking robotic manipulation policies on contact-rich tasks.
- **p. 41 / 7.2.2. Assembly Benchmark - extractive body cue:** A natural next step is to extend these contact-rich environments to cover the full set of NIST benchmark tasks, further broadening their applicability and impact.
- **p. 29 / 5.5.2. SkillGen-based Dataset Augmentation - extractive body cue:** SkillGen (Garrett et al., 2024) is an automated demonstration generation system in Isaac Lab Mimic that produces high-quality, collision-aware robot demonstrations at scale.
- **p. 29 / 5.5.2. SkillGen-based Dataset Augmentation - extractive body cue:** It combines human-provided subtask segments with GPU-accelerated motion planning (described in Section 3.4.3) to create diverse feasible trajectories that adapt to new object placements and ...
- **p. 40 / 7.1.3. Solver Implementations - extractive body cue:** Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning solvers for cloth dynamics, e.g.
- **p. 39 / 7.1.3. Solver Implementations - extractive body cue:** This provides significant performance gains over previous JAX-based MuJoCo XLA (MJX) implementations, particularly for complex scenes involving numerous contacts (e.g. dexterous manipulation, humanoid locomotion), without ...
- **p. 40 / 7.1.3. Solver Implementations - extractive body cue:** Newton USD as a Staging Schema for USD Physics Standardization As part of the AOUSD's initiative to advance USD as a descriptive language for Physical ...
- **p. 39 / 7.1.3. Solver Implementations - extractive body cue:** In addition, Newton will include a dedicated maximal coordinate solver called the Kamino Solver from Disney Research designed to robustly handle systems with closed loops ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5.5.2. SkillGen-based Dataset Augmentation (p. 29); 7.1.3. Solver Implementations (p. 39); 7.2. Policy Evaluation and Benchmarks (p. 40); 7.2.2. Assembly Benchmark (p. 41).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 27: Assembly Environments in Isaac Lab (Tang et al., 2023). Left: Simulation. Right: Real World. The Factory environments combine SDF-based con- tact generation, ... | p. 33 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 15: Log-scale throughput comparison for perceptive learning task in dexterous manipulation (DextrAH). Results are shown for the Tiled and Raycaster-based camera at 64x64 ... | p. 21 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 16: Log-scale throughput comparison of the rough terrain locomotion task for ANYmal-D robot imple- mented using the manager-based and direct workflows. Right: The ... | p. 22 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 20: An overview of the PBT framework for RL in Isaac Lab. Each worker runs an independent RL training process with its own ... | p. 26 (Figure/Table caption) |
| 5.5.2. SkillGen-based Dataset Augmentation | BENCHMARK / DATASET | Users can select planner-backed generation with a single flag, configure the number of trials, number of parallel environments, and compute devices, and adjust the ... | p. 29 (5.5.2. SkillGen-based Dataset Augmentation) |

## Dataset / Benchmark Role

- **p. 41 / 7.2.2. Assembly Benchmark - extractive body cue:** Isaac Lab provides optimized environments for evaluating and benchmarking robotic manipulation policies on contact-rich tasks.
- **p. 41 / 7.2.2. Assembly Benchmark - extractive body cue:** A natural next step is to extend these contact-rich environments to cover the full set of NIST benchmark tasks, further broadening their applicability and impact.
- **p. 29 / 5.5.2. SkillGen-based Dataset Augmentation - extractive body cue:** SkillGen (Garrett et al., 2024) is an automated demonstration generation system in Isaac Lab Mimic that produces high-quality, collision-aware robot demonstrations at scale.
- **p. 29 / 5.5.2. SkillGen-based Dataset Augmentation - extractive body cue:** It combines human-provided subtask segments with GPU-accelerated motion planning (described in Section 3.4.3) to create diverse feasible trajectories that adapt to new object placements and ...
- **p. 40 / 7.1.3. Solver Implementations - extractive body cue:** Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning solvers for cloth dynamics, e.g.
- **p. 39 / 7.1.3. Solver Implementations - extractive body cue:** This provides significant performance gains over previous JAX-based MuJoCo XLA (MJX) implementations, particularly for complex scenes involving numerous contacts (e.g. dexterous manipulation, humanoid locomotion), without ...
- **p. 40 / 7.1.3. Solver Implementations - extractive body cue:** Newton USD as a Staging Schema for USD Physics Standardization As part of the AOUSD's initiative to advance USD as a descriptive language for Physical ...
- **p. 39 / 7.1.3. Solver Implementations - extractive body cue:** In addition, Newton will include a dedicated maximal coordinate solver called the Kamino Solver from Disney Research designed to robustly handle systems with closed loops ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Isaac Lab supports diverse robotic applications with exteroceptive observation inputs. It provides a user-friendly API for experimentation and includes features to facilitate sim-to-real ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Isaac Lab uses OpenUSD to define rich, complex simulation scenes for robotics. Robots, objects, and sensors are arranged in hierarchical scene graphs, where ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Integration of USD with PhysX in OmniPhysics. The USD stage provides a hierarchical representation of all objects and robots in the scene. This ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Photo-realistic rendering in Isaac Lab using the Omniverse RTX renderer, demonstrating high-quality ray tracing with complex physically-based materials authored using NVIDIA's MDL. The ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Tiled rendering of multiple simulated environments. Each environment has a separate camera, and their outputs are spatially tiled into a single GPU frame-buffer. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: 3D Gaussian rendering combined with mesh rendering, with shadows from the mesh af- fecting the Gaussian scene. The RTX renderer can also perform ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Isaac Lab supports diverse asset types (articulated robots, rigid and deformable objects), sensor modalities (proprioception, RGB/depth images, height scans), controllers (IK, cuRoBo), and ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 8: Custom actuator integration in Isaac Lab. Different robot joints can use different actuator models. Implicit actuators rely on the simulator's PD controller, while ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Isaac Lab provides optimized environments for evaluating and benchmarking robotic manipulation policies on contact-rich tasks. | embodiment, simulator version and control stack | p. 41 (7.2.2. Assembly Benchmark), p. 41 (7.2.2. Assembly Benchmark) |
| Task/environment | A natural next step is to extend these contact-rich environments to cover the full set of NIST benchmark tasks, further broadening their applicability and ... | reset, timeout, object/scene variation | p. 41 (7.2.2. Assembly Benchmark), p. 29 (5.5.2. SkillGen-based Dataset Augmentation) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (1. Introduction), p. 14 (3.4. Controllers) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Users can select planner-backed generation with a single flag, configure the number of trials, number of parallel environments, and compute devices, and adjust the ... | definition/direction/unit from same section | p. 29 (5.5.2. SkillGen-based Dataset Augmentation) |
| Figure 27: Assembly Environments in Isaac Lab (Tang et al., 2023). Left: Simulation. Right: Real World. The Factory environments combine SDF-based con- tact generation, ... | definition/direction/unit from same section | p. 33 (Figure/Table caption) |
| Figure 20: An overview of the PBT framework for RL in Isaac Lab. Each worker runs an independent RL training process with its own ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Newton supports a diverse array of solver implementations including a mix of explicit and implicit methods, as well as reduced and maximal coordinate approaches, ... | definition/direction/unit from same section | p. 39 (7.1.3. Solver Implementations) |
| Figure 2: Isaac Lab uses OpenUSD to define rich, complex simulation scenes for robotics. Robots, objects, and sensors are arranged in hierarchical scene graphs, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 23: Platforms using Isaac Lab for learning robust and agile locomotion. Top to right: (a) Boston Dynamics Spot (Miller et al., 2025), (b) ... | definition/direction/unit from same section | p. 30 (Figure/Table caption) |
| Previous works (Noseworthy et al., 2025; Tang et al., 2023, 2024) have demonstrated that the policies trained and evaluated in these environments can be ... | definition/direction/unit from same section | p. 41 (7.2.2. Assembly Benchmark) |
| Figure 4: Photo-realistic rendering in Isaac Lab using the Omniverse RTX renderer, demonstrating high-quality ray tracing with complex physically-based materials authored using NVIDIA's MDL. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 12: Suite of environments in Isaac Lab. They illustrate a variety of simulation capabilities, including contact-rich interactions, multiple sensor modalities for observations, and ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| Figure 15: Log-scale throughput comparison for perceptive learning task in dexterous manipulation (DextrAH). Results are shown for the Tiled and Raycaster-based camera at 64x64 ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |
| Figure 5: Tiled rendering of multiple simulated environments. Each environment has a separate camera, and their outputs are spatially tiled into a single GPU ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 13: Log-scale throughput comparison for state-based manipulation tasks on three GPU platforms, including distributed training with two, four, and eight GPUs. These are ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Figure 14: Log-scale throughput comparison for perceptive locomotion tasks across GPU models and distributed training setups. The task for both Unitree G1 and Agility ... | comparison identity and matched condition | p. 21 (Figure/Table caption) |
| Figure 16: Log-scale throughput comparison of the rough terrain locomotion task for ANYmal-D robot imple- mented using the manager-based and direct workflows. Right: The ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5: Tiled rendering of multiple simulated environments. Each environment has a separate camera, and their outputs are spatially tiled into a single GPU ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 19: Singh et al. (2024) train a student policy with stereo RGB images. (a) The stereo encoder uses a pre-trained ResNet-18 (with the ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| Figure 21: Top: Camera renderings from different environment instances in simulation, adapted from Singh et al. (2024). Bottom: Examples of data augmentations (such as ... | component/input/data sensitivity | p. 27 (Figure/Table caption) |
| Figure 23: Platforms using Isaac Lab for learning robust and agile locomotion. Top to right: (a) Boston Dynamics Spot (Miller et al., 2025), (b) ... | component/input/data sensitivity | p. 30 (Figure/Table caption) |
| This provides significant performance gains over previous JAX-based MuJoCo XLA (MJX) implementations, particularly for complex scenes involving numerous contacts (e.g. dexterous manipulation, humanoid locomotion), ... | component/input/data sensitivity | p. 39 (7.1.3. Solver Implementations) |
| Figure 20: An overview of the PBT framework for RL in Isaac Lab. Each worker runs an independent RL training process with its own ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This enables large-scale data collection, systematic stress testing, and the development of algorithms that transfer more effectively to real-world systems. | Figure 27: Assembly Environments in Isaac Lab (Tang et al., 2023). Left: Simulation. Right: Real World. The Factory environments combine SDF-based con- tact generation, ... | PDF body cue; verify exact table/figure and matched conditions | p. 33 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption), p. 26 (Figure/Table caption), p. 29 (5.5.2. SkillGen-based Dataset Augmentation), p. 39 (7.1.3. Solver Implementations) |
| Primary metric/result | Figure 15: Log-scale throughput comparison for perceptive learning task in dexterous manipulation (DextrAH). Results are shown for the Tiled and Raycaster-based camera at 64x64 ... | numeric claim only at cited anchor | p. 21 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 26 / 5.2. Population-Based Training - extractive body cue:** Isaac Lab includes an implementation of DexPBT with RL-Games for the dexterous manipulation environments in DextrAH (Lum et al., 2024; Singh et al., 2024).It reproduces ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: Isaac Lab uses OpenUSD to define rich, complex simulation scenes for robotics. Robots, objects, and sensors are arranged in hierarchical scene graphs, ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | This addresses key limitations of existing engines in complex robotic scenarios. | p. 37 (7. Future Work and Discussion) |
| body limitation/failure cue | Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning MuJoCo Warp MJX Isaac Lab MuJoCo Solver Collision State Model Solver Custom Solver Warp ... | p. 38 (7. Future Work and Discussion) |
| body limitation/failure cue | SkillGen (Garrett et al., 2024) is an automated demonstration generation system in Isaac Lab Mimic that produces high-quality, collision-aware robot demonstrations at scale. | p. 29 (5.5.2. SkillGen-based Dataset Augmentation) |
| body limitation/failure cue | Developed through a collaborative effort by NVIDIA, Google DeepMind, and Disney Research, Newton aims to advance robot learning and development by providing a robust, ... | p. 38 (7.1. Newton Engine and Isaac Lab Integration) |
| body limitation/failure cue | In addition, Newton will include a dedicated maximal coordinate solver called the Kamino Solver from Disney Research designed to robustly handle systems with closed ... | p. 39 (7.1.3. Solver Implementations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Isaac Lab includes an implementation of DexPBT with RL-Games for the dexterous manipulation environments in DextrAH (Lum et al., 2024; Singh et al., 2024).It ... | p. 26 (5.2. Population-Based Training) |
| Each worker runs an independent RL training process with its own hyperparameters. | p. 26 (5.2. Population-Based Training) |
| This provides significant performance gains over previous JAX-based MuJoCo XLA (MJX) implementations, particularly for complex scenes involving numerous contacts (e.g. dexterous manipulation, humanoid locomotion), ... | p. 39 (7.1.3. Solver Implementations) |
| These solvers are generally lightweight implementations of well-established methods as reference for implementers or solver developers. • New Solvers: An important new development in ... | p. 39 (7.1.3. Solver Implementations) |
| Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning solvers for cloth dynamics, e.g. | p. 40 (7.1.3. Solver Implementations) |
| Multiple solvers can run independently to manage these diverse dynamics, with ongoing development focused on achieving two-way coupling for more intricate interactions. | p. 40 (7.1.3. Solver Implementations) |
| Users can select planner-backed generation with a single flag, configure the number of trials, number of parallel environments, and compute devices, and adjust the ... | p. 29 (5.5.2. SkillGen-based Dataset Augmentation) |
| The cuRobo (Sundaralingam et al., 2023) integration in Isaac Lab enables fast, GPU-parallelized collision-aware motion planning. | p. 15 (3.4.3. Motion Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Isaac Lab uses OpenUSD to define rich, complex simulation scenes for robotics. Robots, objects, and sensors are arranged in hierarchical scene graphs, where ...
- **p. 37 / 7. Future Work and Discussion - extractive body cue:** This addresses key limitations of existing engines in complex robotic scenarios.
- **p. 38 / 7. Future Work and Discussion - extractive body cue:** Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning MuJoCo Warp MJX Isaac Lab MuJoCo Solver Collision State Model Solver Custom Solver Warp Warp ...
- **p. 29 / 5.5.2. SkillGen-based Dataset Augmentation - extractive body cue:** SkillGen (Garrett et al., 2024) is an automated demonstration generation system in Isaac Lab Mimic that produces high-quality, collision-aware robot demonstrations at scale.
- **p. 38 / 7.1. Newton Engine and Isaac Lab Integration - extractive body cue:** Developed through a collaborative effort by NVIDIA, Google DeepMind, and Disney Research, Newton aims to advance robot learning and development by providing a robust, scalable, ...
- **p. 39 / 7.1.3. Solver Implementations - extractive body cue:** In addition, Newton will include a dedicated maximal coordinate solver called the Kamino Solver from Disney Research designed to robustly handle systems with closed loops ...

- **Evidence anchors reviewed:** datasets p. 41 (7.2.2. Assembly Benchmark), p. 41 (7.2.2. Assembly Benchmark), p. 29 (5.5.2. SkillGen-based Dataset Augmentation), p. 29 (5.5.2. SkillGen-based Dataset Augmentation), p. 40 (7.1.3. Solver Implementations), p. 39 (7.1.3. Solver Implementations), metrics p. 29 (5.5.2. SkillGen-based Dataset Augmentation), p. 33 (Figure/Table caption), p. 26 (Figure/Table caption), p. 39 (7.1.3. Solver Implementations), p. 4 (Figure/Table caption), p. 30 (Figure/Table caption), baselines p. 19 (Figure/Table caption), p. 21 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption), results p. 33 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption), p. 26 (Figure/Table caption), p. 29 (5.5.2. SkillGen-based Dataset Augmentation), p. 39 (7.1.3. Solver Implementations).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
