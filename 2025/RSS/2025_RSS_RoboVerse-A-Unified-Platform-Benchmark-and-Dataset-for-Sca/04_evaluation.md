# Evaluation - RoboVerse: A Unified Platform, Benchmark and Dataset for Scalable and Generalizable Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p022.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p022.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 12 (dataset), p. 6 (IV. ROBOVERSE DATASET)): 10 demonstrate a consistent improvement in model performance as the number of generated data increases, highlighting both the effectiveness and scalability of the trajectory augmentation APL

## Evaluation Body Digest

- **p. 11 / dataset - extractive body cue:** In this session, we demonstrate how synthetic data from the ROBOVERSE: simulation can augment real-world datasets to train more capable robotics world models.
- **p. 7 / IV. ROBOVERSE DATASET - extractive body cue:** We offer an API to generate large-scale robot trajectory datasets from a limited number of source demonstrations.
- **p. 9 / C. Reinforcement Learning Benchmark - extractive body cue:** In addition to imitation learning, ROBOVERSE offers a comprehensive reinforcement learning (RL) benchmark designed to accommodate a diverse range of tasks, robot embodiments, and simulation ...
- **p. 5 / IV. ROBOVERSE DATASET - extractive body cue:** We apply the following approaches to collect tasks and demonstrations + Direct Migration from Other Simulation Environments Some benchmarks provide essential components integration into ROBOVERSE.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** RoboCasa [67] introduced dataset of 100 tasks and over 100k trajectories for generalist robots.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** ‘Simulation-based data collection provides a promising solution to the high cost and inefficiencies of real-world datasets.
- **p. 4 / Dataset - extractive body cue:** Powered by METASIM, the simulation platform facilitates dataset creation and benchmark construction.
- **p. 4 / Dataset - extractive body cue:** 2: ROBOVERSE consists of a simulation platform, a largescale, high-quality dataset, and unified benchmarks.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** B. Large-Scale Roboties Dataset (p. 3); C. Benchmarking in Robotics (p. 3); B. MptASIM Implementation (p. 3); Dataset (p. 4); IV. ROBOVERSE DATASET (p. 5); V. ROBOVERSE BENCHMARK (p. 8); A. Benchmark Overview (p. 8); B. Imitation Learning Benchmark (p. 9); C. Reinforcement Learning Benchmark (p. 9); VI. EXPERIMENTAL RESULTS (p. 9); B. Results on the Imitation Learning Benchmark (p. 9); C. Results on the Reinforcement Learning Benchmark (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| C. Results on the Reinforcement Learning Benchmark | BENCHMARK / DATASET | 10 demonstrate a consistent improvement in model performance as the number of generated data increases, highlighting both the effectiveness and scalability of the trajectory ... | p. 11 (C. Results on the Reinforcement Learning Benchmark) |
| B. Results on the Imitation Learning Benchmark | BENCHMARK / DATASET | The reported success rates are computed as the averages over three random seeds. | p. 10 (B. Results on the Imitation Learning Benchmark) |
| C. Results on the Reinforcement Learning Benchmark | BENCHMARK / DATASET | Success rates of policy trained with augmented dataset and source | p. 11 (C. Results on the Reinforcement Learning Benchmark) |
| B. Results on the Imitation Learning Benchmark | BENCHMARK / DATASET | Diffusion Policy [12] is the first work that applies the conditional denoising diffusion Process as a robot visuomotor policy and achieves great ‘generalization capabilities. | p. 10 (B. Results on the Imitation Learning Benchmark) |
| dataset | BENCHMARK / DATASET | The final performance score for each task is reported, where a baseline receives 1 point for successfully grasping the target. | p. 12 (dataset) |

## Dataset / Benchmark Role

- **p. 11 / dataset - extractive body cue:** In this session, we demonstrate how synthetic data from the ROBOVERSE: simulation can augment real-world datasets to train more capable robotics world models.
- **p. 7 / IV. ROBOVERSE DATASET - extractive body cue:** We offer an API to generate large-scale robot trajectory datasets from a limited number of source demonstrations.
- **p. 9 / C. Reinforcement Learning Benchmark - extractive body cue:** In addition to imitation learning, ROBOVERSE offers a comprehensive reinforcement learning (RL) benchmark designed to accommodate a diverse range of tasks, robot embodiments, and simulation ...
- **p. 5 / IV. ROBOVERSE DATASET - extractive body cue:** We apply the following approaches to collect tasks and demonstrations + Direct Migration from Other Simulation Environments Some benchmarks provide essential components integration into ROBOVERSE.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** RoboCasa [67] introduced dataset of 100 tasks and over 100k trajectories for generalist robots.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** ‘Simulation-based data collection provides a promising solution to the high cost and inefficiencies of real-world datasets.
- **p. 4 / Dataset - extractive body cue:** Powered by METASIM, the simulation platform facilitates dataset creation and benchmark construction.
- **p. 4 / Dataset - extractive body cue:** 2: ROBOVERSE consists of a simulation platform, a largescale, high-quality dataset, and unified benchmarks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: ROBOVERSE comprises a scalable simulation platform, a large-scale synthetic dataset, and unified benchmarks. The simulation platform supports seamless integration of new tasks and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: ROBOVERSE consists of a simulation platform, a large- scale, high-quality dataset, and unified benchmarks. At the core of the simulation platform is METASIM, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: METASIM provides a universal configuration system, aligned simulator backends, and a Gym [91] environment wrapper. ‘This three-layer architecture abstracts simulation environments into simulator-agnostic ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: The MetaCon£ig is a nested dataclass that abstracts the core components in any simulation environment in a simulator-agnostic way.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Teleoperation System. RoBOVERSE supports various user-friendly teleoperation approaches. Currently, it enables teleoperation via a phone app (second row), motion capture (middle), VR devices ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: AI-Assisted Task Generation. RoBOVERSE supports an Al-assisted task generation framework that leverages large generative models' extrapolation capabilities to generate non- trivial and semantically ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Real-to-Sim Tools. We use a mobile device to capture ‘multi-view images, reconstruct a high-quality mesh, build a URDF using VLM, and then perform ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Dataset Comparison and Gallery. Left: other representative synthetic robotics datasets. Right: the ROBOVERSE dataset

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this session, we demonstrate how synthetic data from the ROBOVERSE: simulation can augment real-world datasets to train more capable robotics world models. | embodiment, simulator version and control stack | p. 11 (dataset), p. 7 (IV. ROBOVERSE DATASET) |
| Task/environment | We offer an API to generate large-scale robot trajectory datasets from a limited number of source demonstrations. | reset, timeout, object/scene variation | p. 7 (IV. ROBOVERSE DATASET), p. 9 (C. Reinforcement Learning Benchmark) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1. IyrRopucTION), p. 4 (Dataset) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 6 (IV. ROBOVERSE DATASET), p. 2 (1. IyrRopucTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The reported success rates are computed as the averages over three random seeds. | definition/direction/unit from same section | p. 10 (B. Results on the Imitation Learning Benchmark) |
| Success rates of policy trained with augmented dataset and source | definition/direction/unit from same section | p. 11 (C. Results on the Reinforcement Learning Benchmark) |
| To verify the effectiveness of our trajectory augmentation API, on four representative tasks, we compare the success rates of trained Diffusion Policy on 50 ... | definition/direction/unit from same section | p. 11 (C. Results on the Reinforcement Learning Benchmark) |
| The final performance score for each task is reported, where a baseline receives 1 point for successfully grasping the target. | definition/direction/unit from same section | p. 12 (dataset) |
| The uncertainty comes from multiple aspects including simulation accuracy, rendering style and asset properties [52, 22]. | definition/direction/unit from same section | p. 3 (C. Benchmarking in Robotics) |
| They collectively define who performs the actions (agents), what the environment looks like (objects), ‘what the agents should do (tasks, including instructions, success ‘metrics, ... | definition/direction/unit from same section | p. 4 (Dataset) |
| Specifically, we integrate the PPO [83] algorithm from both Stable-Baselines3 [76] and rsl_sl [80] into our METASIM interface, enabling straightforward task definition, seamless environment ... | definition/direction/unit from same section | p. 9 (C. Reinforcement Learning Benchmark) |
| We successfully migrate the HumanoidBench [84] from MwoCo to RoBOVERSE, enabling training across multiple simulators (Isaac Sim and MuloCo) with consistent interfaces. | definition/direction/unit from same section | p. 10 (C. Results on the Reinforcement Learning Benchmark) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1) Baseline and Task Selection: ‘To genuinely reflect the data quality of the ROBOVERSE dataset and provide a standard benchmark for all kinds of ... | comparison identity and matched condition | p. 9 (B. Results on the Imitation Learning Benchmark) |
| Using Stable-Baselines3 [76] and rs! | comparison identity and matched condition | p. 10 (C. Results on the Reinforcement Learning Benchmark) |
| ‘TABLE Il: Baseline Results on ROBOVERSE Imitation Learning Benchmark. | comparison identity and matched condition | p. 10 (B. Results on the Imitation Learning Benchmark) |
| stable policy convergence across simulators, achieving comparable performance to native MuJoCo baselines. | comparison identity and matched condition | p. 11 (C. Results on the Reinforcement Learning Benchmark) |
| Compared to super vised learning tasks, it is relatively difficult to evaluate the performance of a robotics model. | comparison identity and matched condition | p. 3 (C. Benchmarking in Robotics) |
| We define a unified training and evaluation protocol within the ROBOVERSE platform and implement standardized baselines and learning frameworks for benchmarking. | comparison identity and matched condition | p. 8 (A. Benchmark Overview) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 12, we fine-tune OpenVLA [42] on the ROBOVERSE dataset and transfer the earned policy to real-world scenarios without additional finetuning. | component/input/data sensitivity | p. 11 (dataset) |
| To address these challenges, ROBOVERSE enables researchers to evaluate their policies across multiple benchmarks and simulators seamlessly, without familiarizing themselves with each one individually | component/input/data sensitivity | p. 3 (C. Benchmarking in Robotics) |
| (2) Feasibility Check: Since trajectory data is collected via human teleoperation, tasks deemed unreasonable by the teleoperator are removed. | component/input/data sensitivity | p. 6 (IV. ROBOVERSE DATASET) |
| By leveraging this minimal human annotation regarding the order of subtasks, we can efficiently divide each source demo into contiguous bject-centrie manipulation segments {7;}!, ... | component/input/data sensitivity | p. 7 (IV. ROBOVERSE DATASET) |
| For generalist models, the action is pre-processed into delta end-effector position space from absolute end-effector position space, and The gripper action is discretized into ... | component/input/data sensitivity | p. 10 (B. Results on the Imitation Learning Benchmark) |
| 11: Ablation Study of Action-conditioned World Model Learning. | component/input/data sensitivity | p. 11 (dataset) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Additionally, we propose unified benchmarks for imitation learning and reinforcement ‘data is resource-intensive learning, enabling consistent evaluation across different levels of ‘real-world scenarios generalization. | 10 demonstrate a consistent improvement in model performance as the number of generated data increases, highlighting both the effectiveness and scalability of the trajectory ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 12 (dataset), p. 6 (IV. ROBOVERSE DATASET) |
| Primary metric/result | The reported success rates are computed as the averages over three random seeds. | numeric claim only at cited anchor | p. 10 (B. Results on the Imitation Learning Benchmark) |

- Numeric sentences retained from the body:
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** DROID [41] has collected over 76k contact-rich robotic manipulation demonstrations across 86 tasks.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** RH20T [24] proposed a dataset with over 100k demonstrations and 147 tasks.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** At the same time, RT-I [4] set the record further to 130k demonstrations on over 700 tasks.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** Recently, Open X-Embodiment [14] has demonstrated a promising approach to unite the community's efforts, collecting over IM trajectories on 160,266 tasks with 22 different embodiments.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** [35] proposed a dataset containing 256M transitions on 256 tasks for offline compositional reinforcement learning.
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** RoboCasa [67] introduced dataset of 100 tasks and over 100k trajectories for generalist robots.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Moreover, simulation-based data often fails to capture complex physics and diverse task variations found in the real world (52, 22), potentially causing coverfitting to ... | p. 3 (B. Large-Scale Roboties Dataset) |
| body limitation/failure cue | Conversely, a model trained solely on DROID data fails to transfer effectively to the ROBOVERSE scene, We hypothesize that this shortcoming stems from limited ... | p. 11 (dataset) |
| body limitation/failure cue | While ROBOVERSE provides a comprehensive and sealable platform, several limitations remain. | p. 12 (dataset) |
| body limitation/failure cue | Additionally, while our large-scale dataset presents significant potential for pretraining a foundation model, this exploration falls beyond the scope of this paper due to ... | p. 12 (dataset) |
| body limitation/failure cue | Fig. 1: ROBOVERSE comprises a scalable simulation platform, a large-scale synthetic dataset, and unified benchmarks. The simulation platform supports seamless integration of new tasks ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | RoBOVERSE provides a unified solution for large-scale, high-quality, and diverse synthetic data, It enables agents to train on a large set of environments and ... | p. 3 (B. Large-Scale Roboties Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Code 1: Pseudocode for gym.Env implementation. | p. 4 (Dataset) |
| The reported success rates are computed as the averages over three random seeds. | p. 10 (B. Results on the Imitation Learning Benchmark) |
| Specific model implementation details and hyperparameters are provided in supplementary materials, | p. 10 (B. Results on the Imitation Learning Benchmark) |
| Code and dataset can be found at: htips://roboverseorg.github.jo/. | p. 2 (Abstract) |
| First, collecting demonstrations is time-consuming and resourceintensive, and the resulting data is often hardware-dependent ‘or modality-specific, limiting its adaptability to new scenarios. | p. 2 (1. IyrRopucTION) |
| We present METASIM, a high-level interface above specific simulation environment implementations. | p. 3 (A. METASIM Overview) |
| Advancements in computer graphics have contributed to the development of high-fidelity simulators, which are widely used in robotics research and development. | p. 3 (A. Robotics Simulators) |
| The usage of the APIs is illustrated in Code 1. | p. 4 (Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** Moreover, simulation-based data often fails to capture complex physics and diverse task variations found in the real world (52, 22), potentially causing coverfitting to specific ...
- **p. 11 / dataset - extractive body cue:** Conversely, a model trained solely on DROID data fails to transfer effectively to the ROBOVERSE scene, We hypothesize that this shortcoming stems from limited samples ...
- **p. 12 / dataset - extractive body cue:** While ROBOVERSE provides a comprehensive and sealable platform, several limitations remain.
- **p. 12 / dataset - extractive body cue:** Additionally, while our large-scale dataset presents significant potential for pretraining a foundation model, this exploration falls beyond the scope of this paper due to resource ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: ROBOVERSE comprises a scalable simulation platform, a large-scale synthetic dataset, and unified benchmarks. The simulation platform supports seamless integration of new tasks and ...
- **p. 3 / B. Large-Scale Roboties Dataset - extractive body cue:** RoBOVERSE provides a unified solution for large-scale, high-quality, and diverse synthetic data, It enables agents to train on a large set of environments and simulators ...

- **Evidence anchors reviewed:** datasets p. 11 (dataset), p. 7 (IV. ROBOVERSE DATASET), p. 9 (C. Reinforcement Learning Benchmark), p. 5 (IV. ROBOVERSE DATASET), p. 3 (B. Large-Scale Roboties Dataset), p. 3 (B. Large-Scale Roboties Dataset), metrics p. 10 (B. Results on the Imitation Learning Benchmark), p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 12 (dataset), p. 3 (C. Benchmarking in Robotics), p. 4 (Dataset), baselines p. 9 (B. Results on the Imitation Learning Benchmark), p. 10 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 3 (C. Benchmarking in Robotics), p. 8 (A. Benchmark Overview), results p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 11 (C. Results on the Reinforcement Learning Benchmark), p. 10 (B. Results on the Imitation Learning Benchmark), p. 12 (dataset), p. 6 (IV. ROBOVERSE DATASET).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** ‘TABLE Il: Baseline Results on ROBOVERSE Imitation Learning Benchmark. (p. 10, B. Results on the Imitation Learning Benchmark).
- **Metric evidence:** Compared to super vised learning tasks, it is relatively difficult to evaluate the performance of a robotics model. (p. 3, C. Benchmarking in Robotics).
- **Baseline/ablation evidence:** 1) Baseline and Task Selection: ‘To genuinely reflect the data quality of the ROBOVERSE dataset and provide a standard benchmark for all kinds of imitation learning policy models, (p. 9, B. Results on the Imitation Learning Benchmark).
- **Failure/negative evidence:** Conversely, a model trained solely on DROID data fails to transfer effectively to the ROBOVERSE scene, We hypothesize that this shortcoming stems from limited samples per scene coverage in DROID ... (p. 11, dataset).
