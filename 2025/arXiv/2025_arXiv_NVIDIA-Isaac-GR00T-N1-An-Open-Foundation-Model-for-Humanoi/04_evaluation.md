# Evaluation - NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots; PDF retrieval source: https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results), p. 14 (4.3. Experiment Setup), p. 16 (4.4. Quantitative Results), p. 14 (4.3. Experiment Setup), p. 16 (4.4. Quantitative Results)): GR00T-N1-2B, achieves a significantly higher success rate across all tasks, outperforming Diffusion Policy by 32.4% in the 10% Data setting and by 30.4% in the Full Data setting.

## Evaluation Body Digest

- **p. 12 / 4.1. Simulation Benchmarks - extractive body cue:** We generate 1000 demonstrations for each task using the DexMimicGen data generation system and evaluate the model's ability to generalize to novel object configurations. • ...
- **p. 14 / 4.2. Real-World Benchmarks - extractive body cue:** These tasks closely mirror real-world industrial applications, making them highly relevant benchmarks for assessing dexterity in structured environments. • Multi-Agent Coordination (2 tasks, Coordination) Collaborative ...
- **p. 10 / 3.2. Synthetic Datasets - extractive body cue:** We trained the models for 100 epochs on a dataset comprising 3,000 real-world robot data samples with language annotations, each recorded at 480P resolution and ...
- **p. 17 / 4.5. Qualitative Results - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots suffers from immobility during the initial frames and frequently exhibits inaccurate grasping, resulting in a ...
- **p. 9 / 3. Pre-Training Datasets - extractive body cue:** Neural trajectories can be generated from datasets containing robot actions, while simulation trajectories rely on a physics simulator and utilize our DexMimicGen-based automated data generation ...
- **p. 9 / 3.1. Real-World Datasets - extractive body cue:** We include the RT-1 (Brohan et al., 2022), Bridge-v2 (Walke et al., 2023), Language Table (Lynch et al., 2022), DROID (Khazatsky et al., 2024), MUTEX ...
- **p. 10 / 3.3. Human Video Datasets - extractive body cue:** These datasets cover a wide range of real-world human behaviors, including grasping, tool use, cooking, assembly, and other task-oriented activities performed in natural environments, and ...
- **p. 11 / 4. Evaluation - extractive body cue:** Our simulation experiments are conducted on three distinct benchmarks designed to systematically assess the effectiveness of our model across various robot embodiments and manipulation tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 3. Pre-Training Datasets (p. 9); 3.1. Real-World Datasets (p. 9); 3.2. Synthetic Datasets (p. 9); 3.3. Human Video Datasets (p. 10); 4. Evaluation (p. 11); 4.1. Simulation Benchmarks (p. 11); 4.2. Real-World Benchmarks (p. 12); 4.3. Experiment Setup (p. 14); 4.4. Quantitative Results (p. 15); 4.5. Qualitative Results (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Quantitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | GR00T-N1-2B, achieves a significantly higher success rate across all tasks, outperforming Diffusion Policy by 32.4% in the 10% Data setting and by 30.4% in ... | p. 15 (4.4. Quantitative Results) |
| 4.4. Quantitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | GR00T-N1-2B achieves a success rate of 76.6% (11.5/15) in the first coordinated setting and 73.3% (11/15) in the second setting involving novel object manipulation. | p. 15 (4.4. Quantitative Results) |
| 4.3. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, ... | p. 14 (4.3. Experiment Setup) |
| 4.4. Quantitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | When comparing LAPA and IDM labels in RoboCasa, an interesting pattern emerges: LAPA slightly outperforms IDM in the relatively low-data regime (30), but as ... | p. 16 (4.4. Quantitative Results) |
| 4.3. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2.3 in a data-limited setting and evaluating the policy success rate in our simulated and real benchmarks described in Sections 4.1 and 4.2, respectively. | p. 14 (4.3. Experiment Setup) |

## Dataset / Benchmark Role

- **p. 12 / 4.1. Simulation Benchmarks - extractive body cue:** We generate 1000 demonstrations for each task using the DexMimicGen data generation system and evaluate the model's ability to generalize to novel object configurations. • ...
- **p. 14 / 4.2. Real-World Benchmarks - extractive body cue:** These tasks closely mirror real-world industrial applications, making them highly relevant benchmarks for assessing dexterity in structured environments. • Multi-Agent Coordination (2 tasks, Coordination) Collaborative ...
- **p. 10 / 3.2. Synthetic Datasets - extractive body cue:** We trained the models for 100 epochs on a dataset comprising 3,000 real-world robot data samples with language annotations, each recorded at 480P resolution and ...
- **p. 17 / 4.5. Qualitative Results - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots suffers from immobility during the initial frames and frequently exhibits inaccurate grasping, resulting in a ...
- **p. 9 / 3. Pre-Training Datasets - extractive body cue:** Neural trajectories can be generated from datasets containing robot actions, while simulation trajectories rely on a physics simulator and utilize our DexMimicGen-based automated data generation ...
- **p. 9 / 3.1. Real-World Datasets - extractive body cue:** We include the RT-1 (Brohan et al., 2022), Bridge-v2 (Walke et al., 2023), Language Table (Lynch et al., 2022), DROID (Khazatsky et al., 2024), MUTEX ...
- **p. 10 / 3.3. Human Video Datasets - extractive body cue:** These datasets cover a wide range of real-world human behaviors, including grasping, tool use, cooking, assembly, and other task-oriented activities performed in natural environments, and ...
- **p. 11 / 4. Evaluation - extractive body cue:** Our simulation experiments are conducted on three distinct benchmarks designed to systematically assess the effectiveness of our model across various robot embodiments and manipulation tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Data Pyramid for Robot Foundation Model Training. GR00T N1's heterogeneous training corpora can be represented as a pyramid: data quantity de- creases, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: GR00T N1 Model Overview. Our model is a Vision-Language-Action (VLA) model that adopts a dual-system design. We convert the image observation and language ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: GR00T N1 Model Architecture. GR00T N1 is trained on a diverse set of embodiments ranging from single-arm robot arms to bimanual humanoid dexterous ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Latent Actions. We retrieve similar latent embeddings across various embodiments. The left images illustrate the latent action that corresponds to moving the right ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Synthetically Generated Videos. We leverage off-the-shelf video generation models to create neural trajectories to increase the quantity and diversity of our training datasets. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Training Data Generation. Our data generation strategies leverage different data sources. The latent- action learning technique is broadly applied to diverse video datasets. ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 6: Data Collection via Teleoperation. Our teleoperation infrastructure supports multiple devices to capture human hand motion, including 6-DoF wrist poses and hand skeletons. Robot ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 7: Simulation Tasks. Our simulation experiments use tasks from two open-source benchmarks (Robo- Casa (Nasiriany et al., 2024) in the top row and DexMimicGen ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We generate 1000 demonstrations for each task using the DexMimicGen data generation system and evaluate the model's ability to generalize to novel object configurations. ... | embodiment, simulator version and control stack | p. 12 (4.1. Simulation Benchmarks), p. 14 (4.2. Real-World Benchmarks) |
| Task/environment | These tasks closely mirror real-world industrial applications, making them highly relevant benchmarks for assessing dexterity in structured environments. • Multi-Agent Coordination (2 tasks, Coordination) ... | reset, timeout, object/scene variation | p. 14 (4.2. Real-World Benchmarks), p. 10 (3.2. Synthetic Datasets) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (2. GR00T N1 Foundation Model), p. 4 (2.1. Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, ... | definition/direction/unit from same section | p. 14 (4.3. Experiment Setup) |
| 2.3 in a data-limited setting and evaluating the policy success rate in our simulated and real benchmarks described in Sections 4.1 and 4.2, respectively. | definition/direction/unit from same section | p. 14 (4.3. Experiment Setup) |
| Average policy success rate on real-world tasks with the GR-1 humanoid robots. | definition/direction/unit from same section | p. 15 (4.4. Quantitative Results) |
| Average success rate across three simulation benchmarks, using 100 demonstrations per task. | definition/direction/unit from same section | p. 15 (4.4. Quantitative Results) |
| To answer this, we consider the task "Turn Sink Spout" in RoboCasa - in the 100 sample regime, the DP baseline gets 11.8% success ... | definition/direction/unit from same section | p. 16 (4.5. Qualitative Results) |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots suffers from immobility during the initial frames and frequently exhibits inaccurate grasping, resulting in ... | definition/direction/unit from same section | p. 17 (4.5. Qualitative Results) |
| Figure 10: Average policy success rate on simulated manipulation tasks with varying numbers of demonstrations. | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| For post-trained GR00T N1, we observed that, compared to the baseline Diffusion Policy, its motion is generally much smoother, and its grasping accuracy is ... | definition/direction/unit from same section | p. 16 (4.5. Qualitative Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| GR00T N1 outperforms both baselines, especially on the GR-1 task where it outperforms by more than 17 %. | comparison identity and matched condition | p. 15 (4.4. Quantitative Results) |
| We observe that GR00T N1 consistently outperforms the baseline models across benchmark tasks and dataset sizes. | comparison identity and matched condition | p. 15 (4.4. Quantitative Results) |
| For post-trained GR00T N1, we observed that, compared to the baseline Diffusion Policy, its motion is generally much smoother, and its grasping accuracy is ... | comparison identity and matched condition | p. 16 (4.5. Qualitative Results) |
| Compared to DexMG, this benchmark features a significantly larger variety of objects with diverse placements. | comparison identity and matched condition | p. 12 (4.1. Simulation Benchmarks) |
| Our evaluation experiment consists of post-training GR00T N1 and baseline models as described in Sec. | comparison identity and matched condition | p. 14 (4.3. Experiment Setup) |
| Baselines To demonstrate the effectiveness of diverse pretraining of GR00T N1, we compare with two established baselines, BC-Transformer (Mandlekar et al., 2021) and Diffusion ... | comparison identity and matched condition | p. 14 (4.3. Experiment Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| It is natural, in the limit of large fine-tuning datasets, that the effect of pre-training dwindles. | component/input/data sensitivity | p. 16 (4.5. Qualitative Results) |
| It employs a U-Net architecture that progressively removes noise from random samples to generate precise robot actions conditioned on observation sequences. | component/input/data sensitivity | p. 14 (4.3. Experiment Setup) |
| Baselines To demonstrate the effectiveness of diverse pretraining of GR00T N1, we compare with two established baselines, BC-Transformer (Mandlekar et al., 2021) and Diffusion ... | component/input/data sensitivity | p. 14 (4.3. Experiment Setup) |
| Since all post-training data exclusively involve the right hand without any inter-hand transfer, the post-trained policy loses the capability to perform this behavior. | component/input/data sensitivity | p. 16 (4.5. Qualitative Results) |
| Figure 14: More Examples of Neural Generated Trajectories. We highlight 4 key capabilities of neural trajectories: (1) The first three rows shows an example ... | component/input/data sensitivity | p. 28 (Figure/Table caption) |
| We design two manipulation tasks to assess our pretrained models. | component/input/data sensitivity | p. 13 (4.2. Real-World Benchmarks) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce GR00T N1, an open foundation model for generalist humanoid robots. | GR00T-N1-2B, achieves a significantly higher success rate across all tasks, outperforming Diffusion Policy by 32.4% in the 10% Data setting and by 30.4% in ... | PDF body cue; verify exact table/figure and matched conditions | p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results), p. 14 (4.3. Experiment Setup), p. 16 (4.4. Quantitative Results), p. 14 (4.3. Experiment Setup), p. 16 (4.4. Quantitative Results) |
| Primary metric/result | GR00T-N1-2B achieves a success rate of 76.6% (11.5/15) in the first coordinated setting and 73.3% (11/15) in the second setting involving novel object manipulation. | numeric claim only at cited anchor | p. 15 (4.4. Quantitative Results) |

- Numeric sentences retained from the body:
- **p. 9 / 3.1. Real-World Datasets - extractive body cue:** The real-time teleoperation operates at a control frequency of 20Hz.
- **p. 9 / 3.1. Real-World Datasets - extractive body cue:** (2025) is a large-scale dataset of trajectories from 100 robots.
- **p. 9 / 3.1. Real-World Datasets - extractive body cue:** We used the 140,000 trajectories available at the time of launching our training run.
- **p. 10 / 3.2. Synthetic Datasets - extractive body cue:** We trained the models for 100 epochs on a dataset comprising 3,000 real-world robot data samples with language annotations, each recorded at 480P resolution and ...
- **p. 10 / 3.2. Synthetic Datasets - extractive body cue:** We generate a total of around 827 hours of videos; it takes 2 minutes to generate a one-second video on an L40 GPU, and required ...
- **p. 12 / 4.1. Simulation Benchmarks - extractive body cue:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robots illustrates some example tasks from these three benchmarks. • RoboCasa Kitchen (24 tasks, RoboCasa) RoboCasa ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | (Top) Post-trained GR00T-N1-2B successfully places the cucumber into the basket, whereas the Diffusion Policy fails due to an inaccurate grasp. | p. 24 (6. Conclusions) |
| body limitation/failure cue | In future work, we aim to extend its capabilities to tackle long-horizon loco-manipulation, which will require advancements in humanoid hardware, model architecture, and training ... | p. 17 (4.6. Limitations) |
| body limitation/failure cue | In contrast, the post-trained checkpoint fails in this scenario. | p. 16 (4.5. Qualitative Results) |
| body limitation/failure cue | Furthermore, we plan to explore novel model architectures and pre-training strategies to improve the robustness and generalization capabilities of our generalist robot models. | p. 17 (4.6. Limitations) |
| body limitation/failure cue | Videos that fail this criterion undergo re-captioning, with the videos downsampled to 16 frames at 256P resolution for this process. | p. 22 (6. Conclusions) |
| body limitation/failure cue | Figure 3: GR00T N1 Model Architecture. GR00T N1 is trained on a diverse set of embodiments ranging from single-arm robot arms to bimanual humanoid ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, ... | p. 14 (4.3. Experiment Setup) |
| When tuning the vision encoder, a batch size of up to 16 can be used. | p. 8 (2.3. Training Details) |
| If only tuning the adapter layers (action and state encoders + action decoder) and DiT, a batch size up to 200 can be used. | p. 8 (2.3. Training Details) |
| By default we use a global batch size of 1024 and train for 60k steps. | p. 14 (4.3. Experiment Setup) |
| The inference time for sampling a chunk of 16 actions is 63.9ms on an L40 GPU using bf16. | p. 3 (2. GR00T N1 Foundation Model) |
| The decoder is trained to take the latent action 𝑧𝑡and 𝑥𝑡and reconstruct 𝑥𝑡+𝐻. | p. 5 (2.2. Training Data Generation) |
| The encoder takes the current frame 𝑥𝑡and the future frame 𝑥𝑡+𝐻of a video with a fixed window size 𝐻and outputs the latent action 𝑧𝑡. | p. 5 (2.2. Training Data Generation) |
| We used the 140,000 trajectories available at the time of launching our training run. | p. 9 (3.1. Real-World Datasets) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 24 / 6. Conclusions - extractive body cue:** (Top) Post-trained GR00T-N1-2B successfully places the cucumber into the basket, whereas the Diffusion Policy fails due to an inaccurate grasp.
- **p. 17 / 4.6. Limitations - extractive body cue:** In future work, we aim to extend its capabilities to tackle long-horizon loco-manipulation, which will require advancements in humanoid hardware, model architecture, and training corpora.
- **p. 16 / 4.5. Qualitative Results - extractive body cue:** In contrast, the post-trained checkpoint fails in this scenario.
- **p. 17 / 4.6. Limitations - extractive body cue:** Furthermore, we plan to explore novel model architectures and pre-training strategies to improve the robustness and generalization capabilities of our generalist robot models.
- **p. 22 / 6. Conclusions - extractive body cue:** Videos that fail this criterion undergo re-captioning, with the videos downsampled to 16 frames at 256P resolution for this process.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: GR00T N1 Model Architecture. GR00T N1 is trained on a diverse set of embodiments ranging from single-arm robot arms to bimanual humanoid dexterous ...

- **Evidence anchors reviewed:** datasets p. 12 (4.1. Simulation Benchmarks), p. 14 (4.2. Real-World Benchmarks), p. 10 (3.2. Synthetic Datasets), p. 17 (4.5. Qualitative Results), p. 9 (3. Pre-Training Datasets), p. 9 (3.1. Real-World Datasets), metrics p. 14 (4.3. Experiment Setup), p. 14 (4.3. Experiment Setup), p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results), p. 16 (4.5. Qualitative Results), p. 17 (4.5. Qualitative Results), baselines p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results), p. 16 (4.5. Qualitative Results), p. 12 (4.1. Simulation Benchmarks), p. 14 (4.3. Experiment Setup), p. 14 (4.3. Experiment Setup), results p. 15 (4.4. Quantitative Results), p. 15 (4.4. Quantitative Results), p. 14 (4.3. Experiment Setup), p. 16 (4.4. Quantitative Results), p. 14 (4.3. Experiment Setup), p. 16 (4.4. Quantitative Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 0.875). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 9: Average Success Rate (%) across 24 Tasks in simulation and 8 tasks in the real world. In the RoboCasa simulation, we show all post-training results using 30, 100, ... (p. 16, Figure/Table caption).
- **Metric evidence:** Evaluation Protocol For simulated benchmark evaluation, we report the average success rate over 100 trials, taking the maximum score of the last 5 checkpoints, where checkpoints are written every 500 ... (p. 14, 4.3. Experiment Setup).
- **Baseline/ablation evidence:** GR00T N1 outperforms both baselines, especially on the GR-1 task where it outperforms by more than 17 %. (p. 15, 4.4. Quantitative Results).
- **Failure/negative evidence:** (Top) Post-trained GR00T-N1-2B successfully places the cucumber into the basket, whereas the Diffusion Policy fails due to an inaccurate grasp. (p. 24, 6. Conclusions).
