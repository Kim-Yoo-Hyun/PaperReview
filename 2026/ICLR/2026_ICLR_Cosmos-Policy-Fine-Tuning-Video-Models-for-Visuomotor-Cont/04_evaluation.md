# Evaluation - Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006732; PDF retrieval source: https://arxiv.org/pdf/2601.16163. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 19 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS), p. 10 (Figure/Table caption), p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS)): Table 1: LIBERO simulation benchmark results. Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). Cosmos Policy success rates are averaged over 500 trials for each ...

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The LIBERO benchmark (Liu et al., 2024) consists of a variety of environments and tasks featuring a single Franka Emika Panda robot arm.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The benchmark provides a set of 50 human-teleoperated demonstrations for each task and an additional set of 1000 demonstrations generated via MimicGen (Mandlekar et al., ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Our method achieves a state-of-the-art average success rate of 67.1% while requiring significantly fewer training demonstrations (50 versus >300). # Training Demos per Task Average ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Spatial Object Goal Long Average SR (%) SR (%) SR (%) SR (%) SR (%) Diffusion Policy (Chi et al., 2023) 78.3 92.5 68.3 50.5 ...
- **p. 18 / A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS - extractive PDF cue:** For each task, we test on both in-distribution and out-of-distribution (OOD) generalization scenarios with respect to the training demonstration dataset (see Figures 10 and 11 ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** We further evaluate Cosmos Policy trained from scratch on the ALOHA robot for additional supporting evidence and find that it obtains an average score of ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** We evaluate the base Cosmos Policy on challenging initial states for the last two ALOHA robot tasks, and compare it with two planning variants (model-based ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); A.1 LATENT INJECTION IMPLEMENTATION DETAILS (p. 15); A.3 EVALUATION DETAILS (p. 17); A.3.1 GENERAL COSMOS POLICY EVALUATION DETAILS (p. 17); A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS (p. 18); A.4 ADDITIONAL EXPERIMENTS AND DETAILS (p. 20); A.4.1 ADDITIONAL ABLATION EXPERIMENTS (p. 20).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: LIBERO simulation benchmark results. Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). Cosmos Policy success rates are ... | p. 8 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves a state-of-the-art average success rate of 67.1% while requiring significantly fewer training demonstrations (50 versus >300). # Training Demos per Task ... | p. 8 (5 EXPERIMENTS) |
| A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Cosmos Policy achieves highest aggregate success rates, though π0.5 shows slightly better performance specifically in OOD test scenarios. | p. 19 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7: Model-based planning results. We evaluate the base Cosmos Policy on challenging initial states for the last two ALOHA robot tasks, and compare ... | p. 10 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that model-based planning using the V (s′) formulation consistently improves success rates over the base Cosmos Policy without planning, as shown in ... | p. 10 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The LIBERO benchmark (Liu et al., 2024) consists of a variety of environments and tasks featuring a single Franka Emika Panda robot arm.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The benchmark provides a set of 50 human-teleoperated demonstrations for each task and an additional set of 1000 demonstrations generated via MimicGen (Mandlekar et al., ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Our method achieves a state-of-the-art average success rate of 67.1% while requiring significantly fewer training demonstrations (50 versus >300). # Training Demos per Task Average ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Spatial Object Goal Long Average SR (%) SR (%) SR (%) SR (%) SR (%) Diffusion Policy (Chi et al., 2023) 78.3 92.5 68.3 50.5 ...
- **p. 18 / A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS - extractive PDF cue:** For each task, we test on both in-distribution and out-of-distribution (OOD) generalization scenarios with respect to the training demonstration dataset (see Figures 10 and 11 ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** We further evaluate Cosmos Policy trained from scratch on the ALOHA robot for additional supporting evidence and find that it obtains an average score of ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** We evaluate the base Cosmos Policy on challenging initial states for the last two ALOHA robot tasks, and compare it with two planning variants (model-based ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: We present Cosmos Policy, a state-of-the-art robot policy fine-tuned from the NVIDIA Cosmos- Predict2-2B video foundation model. Cosmos Policy handles multimodal inputs and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The latent diffusion sequence of Cosmos Policy. We illustrate latent frame injection-the primary mechanism for adapting the pretrained Cosmos-Predict2 into a policy that ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Cosmos Policy in the ALOHA robot tasks. Cosmos Policy can successfully execute real-world robotic control tasks that require long-horizon, high-precision manipulation and have ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: LIBERO simulation benchmark results. Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). Cosmos Policy success rates are averaged ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: RoboCasa simulation benchmark results. Success rates (SR) across 24 kitchen manipulation tasks (Nasiriany et al., 2024). Cosmos Policy success rates are averaged over ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Real-world ALOHA robot evaluation results. We evaluate state-of-the-art policies on a suite of four tasks and measure the score, which represents average percent ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Common failure modes of π0.5 and OpenVLA-OFT+ on two challenging ALOHA robot tasks. Left: π0.5 struggles to execute a high-precision grasp and loses ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: World model predictions: base Cosmos Policy vs. fine-tuned checkpoint. Top: The base Cosmos Policy's world model may fail to predict errors such as ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LIBERO benchmark (Liu et al., 2024) consists of a variety of environments and tasks featuring a single Franka Emika Panda robot arm. | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Task/environment | The benchmark provides a set of 50 human-teleoperated demonstrations for each task and an additional set of 1000 demonstrations generated via MimicGen (Mandlekar et ... | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 5 (3 PRELIMINARIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use score instead of success rate since a binary metric does not capture fine-grained details. • "put X on plate": 50 points for ... | definition/direction/unit from same section | p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS) |
| As shown in Table 4, removing the auxiliary losses leads to a 1.5% absolute drop in average success rate while training from scratch leads ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Figure 10: In-distribution initial conditions for ALOHA robot evaluations. Here we show sample initial positions used for evaluating policies in conditions similar to the ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| We find that Cosmos Policy achieves highest overall performance in all three domains, while establishing a new state of the art in the LIBERO ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Specifically, for each task, success rate is evaluated over 50 trials across five evaluation scenes with different floor plans and styles (10 trials per ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| The benchmark provides a set of 50 human-teleoperated demonstrations for each task and an additional set of 1000 demonstrations generated via MimicGen (Mandlekar et ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| We observe that model-based planning using the V (s′) formulation consistently improves success rates over the base Cosmos Policy without planning, as shown in ... | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method achieves highest performance overall, even outperforming fine-tuned state-of-the-art vision-language-action (VLA) models. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Figure 4: Real-world ALOHA robot evaluation results. We evaluate state-of-the-art policies on a suite of four tasks and measure the score, which represents average ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| However, to assess the relative data efficiency of Cosmos Policy compared to prior works, we train our method on the 50 human-teleoperated demonstrations alone. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Compared to these methods, Cosmos Policy handles both high multimodality and high precision with substantially greater reliability. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Figure 1: We present Cosmos Policy, a state-of-the-art robot policy fine-tuned from the NVIDIA Cosmos- Predict2-2B video foundation model. Cosmos Policy handles multimodal inputs ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We follow the evaluation protocol of several prior works (Nasiriany et al., 2024; Bjorck et al., 2025; Zheng et al., 2025; Han et al., ... | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Cosmos Policy ablations in LIBERO. Here we report the results of two independent ablations: (1) In Section 4.2, we discussed that Cosmos ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| To further study the effects of individual components of the Cosmos Policy design, as well as the joint training objectives discussed in Section 4.2, ... | component/input/data sensitivity | p. 20 (A.4.1 ADDITIONAL ABLATION EXPERIMENTS) |
| We find that the model-based variant (V (s′)) leads to highest overall performance. pares different variants of planning, such as directly learning a Q-value ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| The V (s′) variant requires a world model to predict the future state before the value can be estimated, while the Q(s, a) variant ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Table 5: Cosmos Policy ablations and additional experiments in RoboCasa. Top: We ablate individual components of the joint objectives training scheme and auxiliary supervision ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| We answer Q1 by comparing Cosmos Policy as a direct policy (without planning) with state-of-the-art imitation learning policies and assessing their relative effectiveness. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We evaluate our method in two modes: first as a direct policy (without planning) and then with model-based planning using the future state and ... | Table 1: LIBERO simulation benchmark results. Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). Cosmos Policy success rates are ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 19 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS), p. 10 (Figure/Table caption), p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Primary metric/result | Our method achieves a state-of-the-art average success rate of 67.1% while requiring significantly fewer training demonstrations (50 versus >300). # Training Demos per Task ... | numeric claim only at cited anchor | p. 8 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Each task suite provides a training dataset of 500 total demonstrations (10 tasks and 50 demonstrations each).
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Specifically, for each task, success rate is evaluated over 50 trials across five evaluation scenes with different floor plans and styles (10 trials per scene), ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The ALOHA platform (Zhao et al., 2023) consists of two ViperX 300 S robot arms with three cameras: one top-down and two wrist-mounted.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** We reduce the controller frequency from 50 Hz to 25 Hz for computational efficiency.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The evaluations consist of both in-distribution and out-of-distribution testing conditions, with 101 trials total per method across all tasks.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Cosmos Policy success rates are averaged over 500 trials for each suite (10 tasks × 50 episodes) and three random seeds (6000 trials total).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability ... | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | For OOD trials, we replace the pink ziploc bag with an unseen blue ziploc bag that is filled to about 75 percent full (more ... | p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS) |
| body limitation/failure cue | Figure 5: Common failure modes of π0.5 and OpenVLA-OFT+ on two challenging ALOHA robot tasks. Left: π0.5 struggles to execute a high-precision grasp and ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 6: World model predictions: base Cosmos Policy vs. fine-tuned checkpoint. Top: The base Cosmos Policy's world model may fail to predict errors such ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: The latent diffusion sequence of Cosmos Policy. We illustrate latent frame injection-the primary mechanism for adapting the pretrained Cosmos-Predict2 into a policy ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Note that extracting non-image modalities like these does not require any VAE decoding since these elements were directly injected into the latent space during ... | p. 15 (A.1 LATENT INJECTION IMPLEMENTATION DETAILS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Finally, for the significantly smaller Diffusion Policy, which only contains approximately 150M parameters (as opposed to 2-7B for the other methods), we train from ... | p. 17 (A.2.4 ALOHA TRAINING DETAILS) |
| Specifically, for each task, success rate is evaluated over 50 trials across five evaluation scenes with different floor plans and styles (10 trials per ... | p. 7 (5 EXPERIMENTS) |
| Each version of the policy is trained with the exact same training hyperparameters and compute as the original Cosmos Policy in RoboCasa, and evaluated ... | p. 22 (A.4.2 COSMOS POLICY INFERENCE LATENCY) |
| We train Cosmos Policy for 45K gradient steps using 32 H100 GPUs with global batch size 800 (taking 48 hours total). | p. 17 (A.2.3 ROBOCASA TRAINING DETAILS) |
| Cosmos Policy success rates are averaged over 50 trials for each task and three random seeds (3600 trials total). | p. 8 (5 EXPERIMENTS) |
| Max time limit is 350 timesteps (14 seconds). • "fold shirt": 12 in-distribution + 8 OOD trials. | p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS) |
| At inference time, Cosmos Policy generates clean (denoised) latent frames. | p. 15 (A.1 LATENT INJECTION IMPLEMENTATION DETAILS) |
| The evaluations consist of both in-distribution and out-of-distribution testing conditions, with 101 trials total per method across all tasks. | p. 7 (5 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from ...
- **p. 18 / A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS - extractive PDF cue:** For OOD trials, we replace the pink ziploc bag with an unseen blue ziploc bag that is filled to about 75 percent full (more than ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Common failure modes of π0.5 and OpenVLA-OFT+ on two challenging ALOHA robot tasks. Left: π0.5 struggles to execute a high-precision grasp and loses ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: World model predictions: base Cosmos Policy vs. fine-tuned checkpoint. Top: The base Cosmos Policy's world model may fail to predict errors such as ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The latent diffusion sequence of Cosmos Policy. We illustrate latent frame injection-the primary mechanism for adapting the pretrained Cosmos-Predict2 into a policy that ...
- **p. 15 / A.1 LATENT INJECTION IMPLEMENTATION DETAILS - extractive PDF cue:** Note that extracting non-image modalities like these does not require any VAE decoding since these elements were directly injected into the latent space during training.

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS), metrics p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS), p. 9 (5 EXPERIMENTS), p. 19 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), baselines p. 8 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 1 (Figure/Table caption), p. 7 (5 EXPERIMENTS), results p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 19 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS), p. 10 (Figure/Table caption), p. 10 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
