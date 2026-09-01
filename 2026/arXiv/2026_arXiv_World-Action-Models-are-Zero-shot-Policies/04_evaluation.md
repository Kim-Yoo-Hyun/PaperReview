# Evaluation - World Action Models are Zero-shot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.15922; PDF retrieval source: https://arxiv.org/pdf/2602.15922. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 3 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (4.2. Post-training)): Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. Q3. Do WAMs improve post-training performance? We i ...

## Evaluation Body Digest

- **p. 10 / 4.1. Pretraining - extractive PDF cue:** As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks-significantly longer-horizon than typical robotic manipulation datasets (Khazatsky et al., ...
- **p. 11 / 4.1. Pretraining - extractive PDF cue:** Our default evaluation setting is unseen environments, unseen objects-because our pretraining and post-training data were collected in a different geographic location from our evaluation sites, ...
- **p. 12 / 4.1. Pretraining - extractive PDF cue:** For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across ...
- **p. 11 / 4.1. Pretraining - extractive PDF cue:** Additional details on the data collection pipeline are provided in Appendix E.5 We also validate DreamZero on the Franka single-arm robot using DROID (Khazatsky et ...
- **p. 13 / 5.1. Main Results - extractive PDF cue:** On DROID-Franka, we show a similar result as well; DreamZero which is only trained on the DROID dataset outperforms pre-trained baseline models trained on multiple ...
- **p. 10 / 4.1. Pretraining - extractive PDF cue:** While recent works have shown that VLAs can learn effective policies from moderate-sized datasets, these approaches typically rely on structured, task-focused demonstrations to ensure consistent ...
- **p. 12 / 4.1. Pretraining - extractive PDF cue:** For unseen tasks, we evaluate 10 tasks absent from training-such as ironing, painting, pulling carts, cube stacking, removing a hat from a mannequin, and untying ...
- **p. 13 / 5.1. Main Results - extractive PDF cue:** We attribute this gap to the joint video-action formulation: while VLAs require massive robot data to learn direct observation-to-a ction mappings, WAMs leverage video generation ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3.2.4. Implementation-level Optimizations (p. 8); 4. Experimental Setup (p. 10); 5. Experimental Results (p. 13); 5.1. Main Results (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. Q3. Do ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) ... | p. 16 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Seen Task Evaluation. DreamZero effectively learns from diverse data and generalizes to new environments, outperforming VLAs across all task categories. VLAs trained ... | p. 13 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments. ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 10 / 4.1. Pretraining - extractive PDF cue:** As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks-significantly longer-horizon than typical robotic manipulation datasets (Khazatsky et al., ...
- **p. 11 / 4.1. Pretraining - extractive PDF cue:** Our default evaluation setting is unseen environments, unseen objects-because our pretraining and post-training data were collected in a different geographic location from our evaluation sites, ...
- **p. 12 / 4.1. Pretraining - extractive PDF cue:** For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across ...
- **p. 11 / 4.1. Pretraining - extractive PDF cue:** Additional details on the data collection pipeline are provided in Appendix E.5 We also validate DreamZero on the Franka single-arm robot using DROID (Khazatsky et ...
- **p. 13 / 5.1. Main Results - extractive PDF cue:** On DROID-Franka, we show a similar result as well; DreamZero which is only trained on the DROID dataset outperforms pre-trained baseline models trained on multiple ...
- **p. 10 / 4.1. Pretraining - extractive PDF cue:** While recent works have shown that VLAs can learn effective policies from moderate-sized datasets, these approaches typically rely on structured, task-focused demonstrations to ensure consistent ...
- **p. 12 / 4.1. Pretraining - extractive PDF cue:** For unseen tasks, we evaluate 10 tasks absent from training-such as ironing, painting, pulling carts, cube stacking, removing a hat from a mannequin, and untying ...
- **p. 13 / 5.1. Main Results - extractive PDF cue:** We attribute this gap to the joint video-action formulation: while VLAs require massive robot data to learn direct observation-to-a ction mappings, WAMs leverage video generation ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview. By jointly predicting video and action, World Action Models (WAMs) inherit world physics priors that enable 1) effective learning from diverse, non-repetitive ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated video. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Free-form Evaluation. DreamZero performs a diverse range of tasks when conditioned on natural language instructions, including object manipulation, tool use, and human-robot interaction. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Model Architecture of DreamZero. The model takes three inputs: visual context (encoded via a VAE), language instructions (via a text encoder), and proprioceptive ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Decoupled Noise Schedules. DreamZero (blue) uses coupled noise for video and action (both uniform). DreamZero-Flash (red) biases video toward high-noise states via a ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Cumulative inference speedups. Each row includes all optimizations above it. Entries marked "-" indicate features not applicable to that hardware.
- **p. 11 / Figure/Table caption - extractive PDF cue:** Figure 6: Distribution statistics for the AgiBot pretraining corpus: episode durations, subtask density, and skill coverage across 7.2K episodes (∼500 hours). interaction with objects at ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 7: AgiBot Evaluation Set-up. We are first-citizens of generalization evals, where the default setting is unseen environment and unseen objects. the object type. For ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks-significantly longer-horizon than typical robotic manipulation datasets (Khazatsky et ... | embodiment, simulator version and control stack | p. 10 (4.1. Pretraining), p. 11 (4.1. Pretraining) |
| Task/environment | Our default evaluation setting is unseen environments, unseen objects-because our pretraining and post-training data were collected in a different geographic location from our evaluation ... | reset, timeout, object/scene variation | p. 11 (4.1. Pretraining), p. 12 (4.1. Pretraining) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 6 (3.1. Model Architecture), p. 2 (1. Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 7 (3.1. Model Architecture), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| PnP Easy PnP Hard Contact-Rich AVG (Task Progress) AVG (Task Progress) AVG (Success Rate) 0 20 40 60 80 100 Success Rate / Task ... | definition/direction/unit from same section | p. 13 (5.1. Main Results) |
| Each rollout is scored from 0 to 1.0 based on partial task completion; full details are provided in Appendix G. | definition/direction/unit from same section | p. 12 (4.1. Pretraining) |
| Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments. ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| On AgiBot G1, from-scratch VLAs achieve near-zero task progress score across all categories. | definition/direction/unit from same section | p. 13 (5.1. Main Results) |
| Figure 4: Model Architecture of DreamZero. The model takes three inputs: visual context (encoded via a VAE), language instructions (via a text encoder), and ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 3: DreamZero-Flash Evaluation. Task progress on table bussing with varying denoising steps (± standard error). DreamZero-Flash recovers most of the 4-step performance using ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 4: Model and Data Ablations. Task progress on PnP Easy tasks (± standard error). AR = autoregressive, BD = bidirectional. All models trained ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 8: Seen Task Evaluation. DreamZero effectively learns from diverse data and generalizes to new environments, outperforming VLAs across all task categories. VLAs trained ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| On DROID-Franka, we show a similar result as well; DreamZero which is only trained on the DROID dataset outperforms pre-trained baseline models trained on ... | comparison identity and matched condition | p. 13 (5.1. Main Results) |
| For each baseline, we evaluate two initialization strategies: (1) from-scratch, using pretrained VLM weights without prior robot data training for a fair apple-to-apple comparison ... | comparison identity and matched condition | p. 10 (4. Experimental Setup) |
| Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. Q3. Do ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| We compare against two state-of-the-art Vision-Language-Action models (VLAs): GR00T N1.6 (Bjorck et al., 2025) and 𝜋0.5 (Physical Intelligence, 2025). | comparison identity and matched condition | p. 10 (4. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also conduct some ablations (Section 5.2) where we initialize from Wan2.1-I2V-5B-480P to see the effect of model size (5B vs. | component/input/data sensitivity | p. 11 (4.1. Pretraining) |
| We hypothesize that learning to only predict actions without encoding the knowledge about future world states makes it challenging to leverage highly heterogeneous, non-repetitive ... | component/input/data sensitivity | p. 10 (4.1. Pretraining) |
| For each baseline, we evaluate two initialization strategies: (1) from-scratch, using pretrained VLM weights without prior robot data training for a fair apple-to-apple comparison ... | component/input/data sensitivity | p. 10 (4. Experimental Setup) |
| For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task ... | component/input/data sensitivity | p. 12 (4.1. Pretraining) |
| Figure 15: Data Collection Environments. We collect teleoperation data across 22 diverse real-world environ- ments, including offices, laboratories, restaurants, supermarkets, coffee shops, warehouses, homes, ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| Figure 6: Distribution statistics for the AgiBot pretraining corpus: episode durations, subtask density, and skill coverage across 7.2K episodes (∼500 hours). interaction with objects ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot ... | Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. Q3. Do ... | PDF body cue; verify exact table/figure and matched conditions | p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 3 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (4.2. Post-training) |
| Primary metric/result | Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) ... | numeric claim only at cited anchor | p. 16 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive PDF cue:** As a result, we reduce the diffusion steps from four to one, cutting inference from ∼350ms to ∼150ms with minimal performance loss (Table 3).
- **p. 10 / 4. Experimental Setup - extractive PDF cue:** Both variants are then trained on identical data as DreamZero: ∼500 hours of teleoperation data we collected for AgiBot G1, and DROID (Khazatsky et al., ...
- **p. 10 / 4.1. Pretraining - extractive PDF cue:** Using AgiBot G1, we collect approximately 500 hours of teleoperation data across 22 unique environments (see Figure 15), including homes, restaurants, supermarkets, coffee shops, and ...
- **p. 11 / 4.1. Pretraining - extractive PDF cue:** World Action Models are Zero-shot Policies 0 1 2 3 4 5 6 7 8 9 10 Duration (minutes) 0 5 10 15 20 25 ...
- **p. 12 / 4.1. Pretraining - extractive PDF cue:** For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across ...
- **p. 12 / 4.1. Pretraining - extractive PDF cue:** For unseen tasks, we evaluate 10 tasks absent from training-such as ironing, painting, pulling carts, cube stacking, removing a hat from a mannequin, and untying ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion ... | p. 19 (6. Discussion and Future Work) |
| body limitation/failure cue | Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments. ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | We leave this direction as future work. | p. 18 (6. Discussion and Future Work) |
| body limitation/failure cue | We leave deep investigation on scaling laws for WAMs as future work. | p. 18 (6. Discussion and Future Work) |
| body limitation/failure cue | Figure 13: Bidirectional vs. Autoregressive WAMs. When the sampling point falls mid-task (T=20), bidirec- tional WAMs must subsample video to align with the language ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | However, naively reducing steps degrades action quality because residual visual noise propagates into action predictions. | p. 9 (3.2.4. Implementation-level Optimizations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We keep the compute budget comparable across all methods by matching total batch size and gradient steps.4 | p. 10 (4. Experimental Setup) |
| We open-source the checkpoint and inference code to run some DROID-sim evals in PolaRiS (Jain et al., 2025).6 Training. | p. 11 (4.1. Pretraining) |
| The key insight is that, at inference time, actions should denoise to their final values while being conditioned on a still-noisy video representation within ... | p. 9 (3.2.4. Implementation-level Optimizations) |
| We train for 100K steps with a global batch size of 128 for AgiBot and 100K steps with a global batch size of 128 ... | p. 11 (4.1. Pretraining) |
| We use the cuDNN backend for attention and migrate scheduler operations to GPU to eliminate CPU-GPU synchronization stalls. | p. 9 (3.2.4. Implementation-level Optimizations) |
| For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task ... | p. 12 (4.1. Pretraining) |
| Moreover, because video and action are jointly trained for strong cross-modal alignment, naively reducing action denoising steps degrades quality. | p. 8 (3.2.4. Implementation-level Optimizations) |
| 3One might expect that generating only actions (not video) would accelerate inference, but at 14B scale we empirically found out that the speed gain ... | p. 8 (3.2.4. Implementation-level Optimizations) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 19 / 6. Discussion and Future Work - extractive PDF cue:** While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments. alignment ...
- **p. 18 / 6. Discussion and Future Work - extractive PDF cue:** We leave this direction as future work.
- **p. 18 / 6. Discussion and Future Work - extractive PDF cue:** We leave deep investigation on scaling laws for WAMs as future work.
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 13: Bidirectional vs. Autoregressive WAMs. When the sampling point falls mid-task (T=20), bidirec- tional WAMs must subsample video to align with the language caption, ...
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive PDF cue:** However, naively reducing steps degrades action quality because residual visual noise propagates into action predictions.

- **PDF anchors reviewed:** datasets p. 10 (4.1. Pretraining), p. 11 (4.1. Pretraining), p. 12 (4.1. Pretraining), p. 11 (4.1. Pretraining), p. 13 (5.1. Main Results), p. 10 (4.1. Pretraining), metrics p. 16 (Figure/Table caption), p. 13 (5.1. Main Results), p. 12 (4.1. Pretraining), p. 14 (Figure/Table caption), p. 13 (5.1. Main Results), p. 6 (Figure/Table caption), baselines p. 3 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (5.1. Main Results), p. 10 (4. Experimental Setup), p. 15 (Figure/Table caption), p. 10 (4. Experimental Setup), results p. 15 (Figure/Table caption), p. 16 (Figure/Table caption), p. 3 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (4.2. Post-training).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
