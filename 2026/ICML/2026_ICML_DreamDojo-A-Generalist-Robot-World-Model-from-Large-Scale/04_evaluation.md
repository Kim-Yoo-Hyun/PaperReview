# Evaluation - DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.06949; PDF retrieval source: https://arxiv.org/abs/2602.06949. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (4.5. Ablations of Our Design Choices), p. 11 (0.219 Method), p. 12 (4.5. Ablations of Our Design Choices), p. 13 (4.7. Downstream Applications)): Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, we ablate the choice of teacher model in ...

## Evaluation Body Digest

- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** Our curated data mixture excels in both scale and diversity, encompassing 15× longer duration, 96× more skills, and 2,000× more scenes than the previously largest ...
- **p. 9 / 4. Experiments - extractive body cue:** We rigorously construct six evaluation benchmarks that reflect the diverse scenarios and actions present in human datasets, while being out-of-distribution for the robot training datasets.
- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** It contains several new objects and new verbs that are unseen in our default robot training dataset.
- **p. 10 / 0.219 Method - extractive body cue:** We also collect a (4) Counterfactual Eval set that focuses on counterfactual actions not present in current robot learning datasets, such as patting a toy ...
- **p. 9 / 4.1. Experimental Setup - extractive body cue:** It is trained on a data mixture of the three human video datasets, as well as our in-house robot datasets, including Unitree G1, Fourier GR-1, ...
- **p. 10 / 0.219 Method - extractive body cue:** To be specific, we mirror the diverse and novel interactions in the three human datasets and construct three corresponding evaluation sets using the Fourier GR-1 ...
- **p. 13 / 4.7. Downstream Applications - extractive body cue:** The final success rate is averaged across all 20 scenes for both real-world and DreamDojo.
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** Existing robot world models are primarily limited to in-distribution settings and fall short in generalizing to unseen interactions with new objects (Team et al., 2025; ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3.2. DreamDojo-HV Dataset (p. 4); 4. Experiments (p. 8); 4.1. Experimental Setup (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, we ablate ... | p. 13 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Live teleoperation. We can teleoperate a virtual G1 robot using the PICO VR controller in real time. to DreamDojo to predict future ... | p. 14 (Figure/Table caption) |
| 4.5. Ablations of Our Design Choices | EMPIRICAL / REAL-ROBOT OR HARDWARE | Both relative actions and chunked injection can significantly improve simulation quality, indicating their importance for achieving precise action controllability. | p. 12 (4.5. Ablations of Our Design Choices) |
| 0.219 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adding more human datasets to pretraining consistently improves the performance for both out-of-distribution scenarios and counterfactual actions, highlighting the the potential of our approach. | p. 11 (0.219 Method) |
| 4.5. Ablations of Our Design Choices | EMPIRICAL / REAL-ROBOT OR HARDWARE | The proposed temporal consistency loss further improves performance on both benchmarks, demonstrating its effectiveness in enhancing action following and object modeling. | p. 12 (4.5. Ablations of Our Design Choices) |

## Dataset / Benchmark Role

- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** Our curated data mixture excels in both scale and diversity, encompassing 15× longer duration, 96× more skills, and 2,000× more scenes than the previously largest ...
- **p. 9 / 4. Experiments - extractive body cue:** We rigorously construct six evaluation benchmarks that reflect the diverse scenarios and actions present in human datasets, while being out-of-distribution for the robot training datasets.
- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** It contains several new objects and new verbs that are unseen in our default robot training dataset.
- **p. 10 / 0.219 Method - extractive body cue:** We also collect a (4) Counterfactual Eval set that focuses on counterfactual actions not present in current robot learning datasets, such as patting a toy ...
- **p. 9 / 4.1. Experimental Setup - extractive body cue:** It is trained on a data mixture of the three human video datasets, as well as our in-house robot datasets, including Unitree G1, Fourier GR-1, ...
- **p. 10 / 0.219 Method - extractive body cue:** To be specific, we mirror the diverse and novel interactions in the three human datasets and construct three corresponding evaluation sets using the Fourier GR-1 ...
- **p. 13 / 4.7. Downstream Applications - extractive body cue:** The final success rate is averaged across all 20 scenes for both real-world and DreamDojo.
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** Existing robot world models are primarily limited to in-distribution settings and fall short in generalizing to unseen interactions with new objects (Team et al., 2025; ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: DreamDojo overview. DreamDojo acquires comprehensive physical knowledge from large-scale human datasets by utilizing latent actions as unified labels. After post-training and distillation on ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Distribution analysis of DreamDojo-HV. (a) Distribution of the scenarios and random examples from the most frequent categories. (b) [Left]: Distribution of subtask numbers ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Scale and diversity comparison to existing large-scale datasets used by previous world models. Our curated data mixture excels in both scale and diversity, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Latent action model. [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that represents ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Benchmark visualization. We rigorously construct six evaluation benchmarks that reflect the diverse scenarios and actions present in human datasets, while being out-of-distribution for ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Effects of different action conditioning methods. Latent action conditioning performs on par with the ideal settings in simulation quality and is the most ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Effects of using different data mixtures. Adding more human datasets to pretraining consistently improves the performance for both out-of-distribution scenarios and counterfactual actions, ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Human preference evaluation in diverse out-of-distribution scenarios. DreamDojo outperforms the pretrained Cosmos-Predict2.5 by a non-trivial margin. Our DreamDojo-14B demonstrates the most competitive performance ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our curated data mixture excels in both scale and diversity, encompassing 15× longer duration, 96× more skills, and 2,000× more scenes than the previously ... | embodiment, simulator version and control stack | p. 5 (3.2. DreamDojo-HV Dataset), p. 9 (4. Experiments) |
| Task/environment | We rigorously construct six evaluation benchmarks that reflect the diverse scenarios and actions present in human datasets, while being out-of-distribution for the robot training ... | reset, timeout, object/scene variation | p. 9 (4. Experiments), p. 5 (3.2. DreamDojo-HV Dataset) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 5 (3.3.1. Model Architecture), p. 2 (1. Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 3 (2. Preliminary), p. 3 (2. Preliminary) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The final success rate is averaged across all 20 scenes for both real-world and DreamDojo. | definition/direction/unit from same section | p. 13 (4.7. Downstream Applications) |
| The success rate is determined by the number of fruits successfully picked up from the table and placed into the bag, with 5 fruits ... | definition/direction/unit from same section | p. 13 (4.7. Downstream Applications) |
| 0.0 0.2 0.4 0.6 0.8 DreamDojo Success Rate 0.0 0.1 0.2 0.3 0.4 Real Success Rate Pearson r = 0.995 MMRV = 0.003 | definition/direction/unit from same section | p. 14 (4.7. Downstream Applications) |
| Next, for the distillation step, we have the student randomly generate between 13 and 49 frames during training, and compute loss on the last ... | definition/direction/unit from same section | p. 10 (0.219 Method) |
| Our DreamDojo-14B demonstrates the most competitive performance in both physics correctness and action following. | definition/direction/unit from same section | p. 12 (4.3. Effects of Different Data Mixtures) |
| The proposed temporal consistency loss further improves performance on both benchmarks, demonstrating its effectiveness in enhancing action following and object modeling. | definition/direction/unit from same section | p. 12 (4.5. Ablations of Our Design Choices) |
| In this section, we conduct extensive experiments to demonstrate DreamDojo's strengths. | definition/direction/unit from same section | p. 8 (4. Experiments) |
| 4.5) (4) Can our distillation pipeline accelerate and stabilize long-horizon interactions? | definition/direction/unit from same section | p. 8 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, we ablate ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Specifically, we aim to answer the following questions: (1) Compared to actionless pretraining, can latent actions enable more effective transfer from human videos? | comparison identity and matched condition | p. 8 (4. Experiments) |
| Specifically, we make a web UI and invite 12 volunteers to judge side-by-side video pairs from physics correctness of object interactions and action following ... | comparison identity and matched condition | p. 10 (0.219 Method) |
| In this baseline, we pretrain the world model with ground-truth action conditioning. | comparison identity and matched condition | p. 11 (4.2. Effects of Different Action Conditions) |
| In this baseline, we pretrain the world model on unlabeled videos as passive future prediction. | comparison identity and matched condition | p. 11 (4.2. Effects of Different Action Conditions) |
| DreamDojo outperforms the pretrained Cosmos-Predict2.5 by a non-trivial margin. | comparison identity and matched condition | p. 12 (4.3. Effects of Different Data Mixtures) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| When evaluating the models without distillation, we generate 100 future videos over three rounds by autoregressively resetting the condition frame with the last prediction ... | component/input/data sensitivity | p. 10 (0.219 Method) |
| Unlike our final models, the sampling ratio is uniform across each dataset for the model variants in this ablation study. | component/input/data sensitivity | p. 11 (4.3. Effects of Different Data Mixtures) |
| Pretraining with latent actions can reach a much higher upper bound than action-free pretraining and without pretraining. | component/input/data sensitivity | p. 11 (4.2. Effects of Different Action Conditions) |
| To benchmark the generalization ability in unseen scenarios, we generate video samples using the two final models, DreamDojo-2B and DreamDojo-14B, and conduct evaluations with ... | component/input/data sensitivity | p. 12 (4.4. Generalization to Unseen Scenarios) |
| 7, evaluating the distillation results of a teacher pretrained on human videos versus one without pretraining (Cosmos-Predict2.5). | component/input/data sensitivity | p. 13 (4.6. Benefits of Distillation) |
| Table 5: Ablations of architecture and loss designs. Our design choices can effectively enhance the simulation quality of both expert and counterfactual trajectories. | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| By scaling up human videos and introducing continuous latent actions as unified proxy, we present DreamDojo, the first world model of its kind that ... | Table 7: Generalization ability after distillation. Thanks to our strong pretraining, DreamDojo shows consistently better generalization than the baseline after distillation. Lastly, we ablate ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (4.5. Ablations of Our Design Choices), p. 11 (0.219 Method), p. 12 (4.5. Ablations of Our Design Choices), p. 13 (4.7. Downstream Applications) |
| Primary metric/result | Figure 6: Live teleoperation. We can teleoperate a virtual G1 robot using the PICO VR controller in real time. to DreamDojo to predict future ... | numeric claim only at cited anchor | p. 14 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos Dataset Type Prior Works # Hour # Trajectory # Skill # Scene RT-1 Robot IRASim, ...
- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** Our curated data mixture excels in both scale and diversity, encompassing 15× longer duration, 96× more skills, and 2,000× more scenes than the previously largest ...
- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** It has 829 hours of egocentric videos with high-precision 3D hand and finger poses collected at the time of recording.
- **p. 5 / 3.2. DreamDojo-HV Dataset - extractive body cue:** 1, our final dataset comprises a total of 44,711 hours, making it the largest human interaction dataset to date for world model pretraining.
- **p. 9 / 4.1. Experimental Setup - extractive body cue:** In the post-training stage, the videos of the target embodiment (e.g., G1, GR-1, AgiBot) are sampled at roughly 10 Hz to capture feasible motions.
- **p. 10 / 0.219 Method - extractive body cue:** The distillation stage initializes the autoregressive student model with the weights of the teacher, while replacing bidirectional attention with causal attention over a sliding window ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, when conducting policy evaluation, the absolute success rates in DreamDojo are often higher than their real counterparts, indicating a limitation in accurately generating ... | p. 15 (5. Conclusion) |
| body limitation/failure cue | As a result, training on these datasets often fails to preserve the model's abilities when extending to out-of-distribution scenarios. | p. 4 (3.2. DreamDojo-HV Dataset) |
| body limitation/failure cue | Future work should explore how to cover broader action distribution, e.g., using policy rollouts (Ho et al., 2025; Zhu et al., 2025). | p. 15 (5. Conclusion) |
| body limitation/failure cue | To address this limitation, one might consider increasing the scale of real robot data. | p. 4 (3.2. DreamDojo-HV Dataset) |
| body limitation/failure cue | Figure 3: Latent action model. [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | In contrast, we introduce the first foundation world model for dexterous manipulation, which exhibits strong generalization in simulating diverse out-of-distribution manipulation skills across multiple ... | p. 16 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| By default, post-training is conducted with 128 NVIDIA H100 GPUs for 50k steps with a batch size of 512. | p. 9 (4.1. Experimental Setup) |
| Both models are pretrained for 140k steps with an effective batch size of 1024 using 256 NVIDIA H100 GPUs. | p. 9 (4.1. Experimental Setup) |
| We ensemble 5 model checkpoints from training to generate action proposals that exhibit sufficient variance at inference time. | p. 13 (4.7. Downstream Applications) |
| All distillation is conducted on 64 NVIDIA H100 GPUs, using a batch size of 256 for the warmup stage and 64 for the distillation ... | p. 10 (0.219 Method) |
| The VAE decoder receives this embedding along with the former frame 𝑓𝑡, aggregates the information and predicts the subsequent frame 𝑓𝑡+1. | p. 7 (3.3.2. Pretraining from Human Videos) |
| Specifically, unlike the standard VAE, our VAE encoder takes two consecutive frames 𝑓𝑡:𝑡+1, extracts spatiotemporal features, and projects the global features to a low-dimensional ... | p. 7 (3.3.2. Pretraining from Human Videos) |
| We run this distillation step for 3k iterations. | p. 10 (0.219 Method) |
| Specifically, we pretrain our model on different data combinations for 50k steps, and then post-train on the GR-1 dataset for 25k steps. | p. 11 (4.3. Effects of Different Data Mixtures) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / 5. Conclusion - extractive body cue:** Additionally, when conducting policy evaluation, the absolute success rates in DreamDojo are often higher than their real counterparts, indicating a limitation in accurately generating nuanced ...
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** As a result, training on these datasets often fails to preserve the model's abilities when extending to out-of-distribution scenarios.
- **p. 15 / 5. Conclusion - extractive body cue:** Future work should explore how to cover broader action distribution, e.g., using policy rollouts (Ho et al., 2025; Zhu et al., 2025).
- **p. 4 / 3.2. DreamDojo-HV Dataset - extractive body cue:** To address this limitation, one might consider increasing the scale of real robot data.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Latent action model. [Left]: The information bottleneck design of our latent action model enforces action disentanglement, producing a continuous latent vector that represents ...
- **p. 16 / 5. Conclusion - extractive body cue:** In contrast, we introduce the first foundation world model for dexterous manipulation, which exhibits strong generalization in simulating diverse out-of-distribution manipulation skills across multiple embodiments.

- **PDF anchors reviewed:** datasets p. 5 (3.2. DreamDojo-HV Dataset), p. 9 (4. Experiments), p. 5 (3.2. DreamDojo-HV Dataset), p. 10 (0.219 Method), p. 9 (4.1. Experimental Setup), p. 10 (0.219 Method), metrics p. 13 (4.7. Downstream Applications), p. 13 (4.7. Downstream Applications), p. 14 (4.7. Downstream Applications), p. 10 (0.219 Method), p. 12 (4.3. Effects of Different Data Mixtures), p. 12 (4.5. Ablations of Our Design Choices), baselines p. 13 (Figure/Table caption), p. 8 (4. Experiments), p. 10 (0.219 Method), p. 11 (4.2. Effects of Different Action Conditions), p. 11 (4.2. Effects of Different Action Conditions), p. 12 (4.3. Effects of Different Data Mixtures), results p. 13 (Figure/Table caption), p. 14 (Figure/Table caption), p. 12 (4.5. Ablations of Our Design Choices), p. 11 (0.219 Method), p. 12 (4.5. Ablations of Our Design Choices), p. 13 (4.7. Downstream Applications).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
