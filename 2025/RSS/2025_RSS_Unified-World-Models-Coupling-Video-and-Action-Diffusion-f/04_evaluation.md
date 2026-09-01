# Evaluation - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/2025/program/papers/15/; PDF retrieval source: https://arxiv.org/pdf/2504.02792. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 9 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 2 (Figure/Table caption)): Fig. 6. Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. UWM exhibits strong performance and can further improve by co-training from action-free videos. accurately capture ...

## Evaluation Body Digest

- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The LIBERO-100 benchmark consists of 90 training environments across multiple scenes and 10 evaluation environments, each with accompanying expert demonstrations.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The DROID dataset is a diverse dataset consisting of robot trajectories collected across various institutions and operators, covering a large variety of tasks, camera positions ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The pretraining dataset (LIBERO-90) consists of 90 tasks sampled across the kitchen, living room, and study scenes.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this section, we examine the following research questions: (1) can UWM effectively learn from large robotic datasets as a pretraining paradigm?
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We answer these questions through a number of real robot experiments with a Franka robot using the DROID [25] manipulation platform, as well as simulated ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Real Robot Experiments 1) Setup: To evaluate UWM and baselines as pretraining methods, we leverage the DROID dataset [25] as a source of pretraining data.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We curate the finetuning datasets by teleoperating the robot and collecting a dataset of expert trajectories.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** VI.) For cotraining experiments, we mix up the robot and video datasets and sample batches uniformly from the mixture dataset, where each batch may contain ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 6. Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. UWM exhibits strong performance and can further improve by ... | p. 7 (Figure/Table caption) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | We find that given the same time limit as the trajectory length, the inverse dynamics model achieves a higher success rate than the policy. | p. 9 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | PAD achieves the lowest success across the board. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | DP achieves the second highest performance, followed by GR1 and PAD. | p. 8 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | BENCHMARK / DATASET | We find UWM to consistently improve performance when exposed to additional videos during pretraining. | p. 8 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The LIBERO-100 benchmark consists of 90 training environments across multiple scenes and 10 evaluation environments, each with accompanying expert demonstrations.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The DROID dataset is a diverse dataset consisting of robot trajectories collected across various institutions and operators, covering a large variety of tasks, camera positions ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The pretraining dataset (LIBERO-90) consists of 90 tasks sampled across the kitchen, living room, and study scenes.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** In this section, we examine the following research questions: (1) can UWM effectively learn from large robotic datasets as a pretraining paradigm?
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We answer these questions through a number of real robot experiments with a Franka robot using the DROID [25] manipulation platform, as well as simulated ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Real Robot Experiments 1) Setup: To evaluate UWM and baselines as pretraining methods, we leverage the DROID dataset [25] as a source of pretraining data.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We curate the finetuning datasets by teleoperating the robot and collecting a dataset of expert trajectories.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** VI.) For cotraining experiments, we mix up the robot and video datasets and sample batches uniformly from the mixture dataset, where each batch may contain ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Unified World Models integrates action and video diffusion in a unified transformer architecture controlled by modality-specific diffusion timesteps. The model can be trained ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Unified World Model training and inference pipeline. The left panel shows UWM pretraining on robot trajectories with actions and co-training on action-free videos ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. A single Unified World Model (UWM) block consists of a transformer block with observations and diffusion timesteps conditioning via adaptive layer norm. In ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Visualization of datasets used for pretraining and finetuning. The pretraining and cotraining dataset consists of diverse tasks performed by Franka robots in various ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Setup for real robot tasks: Stack-Bowls, Block-Cabinet, Paper-Towel, Hang-Towel, and Rice-Cooker. The first row illustrates the initial configurations for each task. The second ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. UWM exhibits strong performance and can further improve by co-training ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. Visualization of the LIBERO datasets. The pretraining dataset (LIBERO-90) consists of 90 tasks sampled across the kitchen, living room, and study scenes. The ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8. Visualization of the forward dynamics predictions. The model accurately predicts the robot and object poses conditioned on the initial observation and actions. TABLE ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LIBERO-100 benchmark consists of 90 training environments across multiple scenes and 10 evaluation environments, each with accompanying expert demonstrations. | embodiment, simulator version and control stack | p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | The DROID dataset is a diverse dataset consisting of robot trajectories collected across various institutions and operators, covering a large variety of tasks, camera ... | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| We find that UWM achieves the highest success rates across all five tasks among the methods, surpassing the best baseline by as much as ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| UWM achieves the highest success rates across the evauation tasks in the out-of-distribution setting. | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| We find that given the same time limit as the trajectory length, the inverse dynamics model achieves a higher success rate than the policy. | definition/direction/unit from same section | p. 9 (IV. EXPERIMENTS) |
| The second row demonstrates successful task completions. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Despite a slight performance drop compared to the ID setting, we find UWM to outperform the baselines, showcasing strong robustness under distribution shifts. | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| Fig. 1. Unified World Models integrates action and video diffusion in a unified transformer architecture controlled by modality-specific diffusion timesteps. The model can be ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| (3) what are the key design choices that contribute to UWM's performance. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Despite a slight performance drop compared to the ID setting, we find UWM to outperform the baselines, showcasing strong robustness under distribution shifts. | comparison identity and matched condition | p. 8 (IV. EXPERIMENTS) |
| GR1 consistently outputs the second best results, establishing a strong baseline performance for deterministic regressive models. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Detailed descriptions of each baseline are deferred to Appendix A. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Baselines We compare UWM to the following baselines throughout our experiments. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| We find that UWM achieves the highest success rates across all five tasks among the methods, surpassing the best baseline by as much as ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| While PAD showcases weak positive transfer as a result of cotraining, its baseline performance is suboptimal. | comparison identity and matched condition | p. 8 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Analysis and Ablation Experiments In this section, we conduct analysis and ablation experiments to help understand the various components and design choices in UWM. | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |
| (2) can UWM further benefit from additional video data without action labels in a co-training paradigm? | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| In this section, we examine the following research questions: (1) can UWM effectively learn from large robotic datasets as a pretraining paradigm? | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| We compare to GR1 to validate the effectiveness of diffusion as a pretraining objective relative to regression. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| To this end, we sample another 2000 trajectories from the rest of the DROID dataset and remove their action annotations to use as videos ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| This limits its performance at accurately capturing the conditional action distribution without expanding model capacity. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show that this learning framework leads to improved policies compared to standard imitation learning since, (1) the unified architecture enables feature sharing between ... | Fig. 6. Average success rates across all real robot tasks and in-distribution and out-of-distribution settings. UWM exhibits strong performance and can further improve by ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 9 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 2 (Figure/Table caption) |
| Primary metric/result | We find that given the same time limit as the trajectory length, the inverse dynamics model achieves a higher success rate than the policy. | numeric claim only at cited anchor | p. 9 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We curate a pretraining dataset by sampling a subset of 2000 trajectories from the DROID dataset based on location (Fig 4, top row).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To this end, we sample another 2000 trajectories from the rest of the DROID dataset and remove their action annotations to use as videos (Fig ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Book-Caddy Soup-Cheese Bowl-Drawer Moka-Moka Mug-Mug Average UWM (Ours) 0.91 ± 0.07 0.93 ± 0.01 0.80 ± 0.02 0.68 ± 0.02 0.65 ± 0.01 0.79 ± ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The pretraining dataset (LIBERO-90) consists of 90 tasks sampled across the kitchen, living room, and study scenes.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** The finetuning datasets (LIBERO-10) consist of 10 tasks used for evaluation.
- **p. 4 / III. METHOD - extractive body cue:** Encoder Decoder Encoder Unpatchify Patchify Encoder Decoder Encoder Patchify Unified World Model Training UWM UWM Marginal Inference (Policy) 𝑡! 𝑡"# Conditional Inference (Inverse Dynamics) Encoder ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Firstly, the proposed model does not yet learn from large scale human videos, bridging the embodiment gap. | p. 10 (VII. LIMITATIONS) |
| body limitation/failure cue | Fig. 1. Unified World Models integrates action and video diffusion in a unified transformer architecture controlled by modality-specific diffusion timesteps. The model can be ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | The third row highlights the out-of-distribution (OOD) configurations designed to evaluate the robustness of each method. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Unlike other baselines, GR1 does not model a distribution over data using a diffusion process. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | Fig. 10. Training models from scratch vs finetuning pretrained models. UWM scales more effectively with pretraining than DP. promising, they are still heavily reliant ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | This set of experiments tests the models' robustness to distribution shifts. | p. 7 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For flexible inference, we can leverage a connection between diffusion time-steps and masking - noising input tokens by setting the inference timestep for diffusion ... | p. 3 (III. METHOD) |
| The key conceptual difference between PAD and UWM is the decoupling of timesteps between actions and next-observations. | p. 6 (IV. EXPERIMENTS) |
| We train all methods on the pretraining / co-training datasets for 100K steps and then finetune to the evaluation tasks (task-specific parameters shown in ... | p. 7 (IV. EXPERIMENTS) |
| Compared to UWM which takes in image features preprocessed by an encoder, PAD takes in raw pixels, thus needing to incorporate the feature extraction ... | p. 7 (IV. EXPERIMENTS) |
| We finetune 3 random seeds for each method on each environment, and evaluate on 50 different initializations. | p. 8 (IV. EXPERIMENTS) |
| This suggests using diffusion time steps for masking as an effective strategy for co-training on multimodal data. | p. 8 (IV. EXPERIMENTS) |
| 4) Real-World Learning from Scratch: To study UWM's ability to scale with pretraining, we train UWM and DP on the task-specific expert demonstrations from ... | p. 9 (IV. EXPERIMENTS) |
| Timesteps closer to T (fully noised) indicate full masking, while timesteps closer to 0 (unnoised) indicate no masking. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / VII. LIMITATIONS - extractive body cue:** Firstly, the proposed model does not yet learn from large scale human videos, bridging the embodiment gap.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Unified World Models integrates action and video diffusion in a unified transformer architecture controlled by modality-specific diffusion timesteps. The model can be trained ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The third row highlights the out-of-distribution (OOD) configurations designed to evaluate the robustness of each method.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Unlike other baselines, GR1 does not model a distribution over data using a diffusion process.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Training models from scratch vs finetuning pretrained models. UWM scales more effectively with pretraining than DP. promising, they are still heavily reliant on ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This set of experiments tests the models' robustness to distribution shifts.

- **PDF anchors reviewed:** datasets p. 8 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 9 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), baselines p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), results p. 7 (Figure/Table caption), p. 9 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
