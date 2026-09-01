# Evaluation - FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2505.10075; PDF retrieval source: https://arxiv.org/pdf/2505.10075. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 13 (A. Implementation Details), p. 14 (A. Implementation Details)): Figure 4. Visual planning results on the VP2 benchmark. We report the mean and the min/max performance of different methods over multiple runs with different random seeds. On the right, ...

## Evaluation Body Digest

- **p. 14 / A. Implementation Details - extractive body cue:** We conduct video prediction experiments on the real-world RT-1 robot manipulation dataset.
- **p. 14 / A. Implementation Details - extractive body cue:** The RT-1 real-world dataset contains more tasks, lighting conditions, and camera positions, making it a much harder task than on the simulation data.
- **p. 13 / A. Implementation Details - extractive body cue:** Scene flow obtainment pipeline on the real-world dataset.
- **p. 13 / A. Implementation Details - extractive body cue:** An "episode" refers to a complete trajectory where the robot completes a task.
- **p. 2 / 3. We perform comprehensive evaluations across several - extractive body cue:** benchmarks, demonstrating the efficacy of our approach in both visual performance and visual planning tasks.
- **p. 4 / 4. Experiments - extractive body cue:** In this section, we conduct extensive experiments in four different benchmarks to verify the performance of FlowDreamer.
- **p. 8 / 4.3. Additional Analysis on Flow Prediction - extractive body cue:** We first reverse the direction of input flows at stage 2 while the robot action remains unchanged.
- **p. 8 / 4.3. Additional Analysis on Flow Prediction - extractive body cue:** We can observe that the robot did not really take contrary actions due to the action input at stage 2, while its performance becomes worse ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3. We perform comprehensive evaluations across several (p. 2); 4. Experiments (p. 4); A. Implementation Details (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Visual planning results on the VP2 benchmark. We report the mean and the min/max performance of different methods over multiple runs with ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Qualitative results on the SimplerEnv RT-1 and Language Table benchmark. We show the predicted frames and the scene flows except for Vanilla, ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Proposed RGB-D world model with flow-based mo- tion representations. FlowDreamer adopts a two-stage prediction framework, which explicitly predict scene flow as motion ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3. The correlation coefficient r between the flow predic- tion error and image assessment metrics. r > 0 indicates a positive correlation and ... | p. 8 (Figure/Table caption) |
| A. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | We notice that increasing sampling steps more than 20 cannot improve the accuracy of future prediction yet is more time-consuming. | p. 13 (A. Implementation Details) |

## Dataset / Benchmark Role

- **p. 14 / A. Implementation Details - extractive body cue:** We conduct video prediction experiments on the real-world RT-1 robot manipulation dataset.
- **p. 14 / A. Implementation Details - extractive body cue:** The RT-1 real-world dataset contains more tasks, lighting conditions, and camera positions, making it a much harder task than on the simulation data.
- **p. 13 / A. Implementation Details - extractive body cue:** Scene flow obtainment pipeline on the real-world dataset.
- **p. 13 / A. Implementation Details - extractive body cue:** An "episode" refers to a complete trajectory where the robot completes a task.
- **p. 2 / 3. We perform comprehensive evaluations across several - extractive body cue:** benchmarks, demonstrating the efficacy of our approach in both visual performance and visual planning tasks.
- **p. 4 / 4. Experiments - extractive body cue:** In this section, we conduct extensive experiments in four different benchmarks to verify the performance of FlowDreamer.
- **p. 8 / 4.3. Additional Analysis on Flow Prediction - extractive body cue:** We first reverse the direction of input flows at stage 2 while the robot action remains unchanged.
- **p. 8 / 4.3. Additional Analysis on Flow Prediction - extractive body cue:** We can observe that the robot did not really take contrary actions due to the action input at stage 2, while its performance becomes worse ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Proposed RGB-D world model with flow-based mo- tion representations. FlowDreamer adopts a two-stage prediction framework, which explicitly predict scene flow as motion repre- ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of FlowDreamer. At stage 1, FlowDreamer receives the RGB-D frame and the robot action as input to explicitly predict the scene flow ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Video prediction results on the SimplerEnv RT-1 benchmark. We categorize the metrics into three groups: semantic similarity, pixel similarity, and media quality. Bold ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Video prediction results on the Language Table benchmark. We categorize the metrics into three groups: semantic similarity, pixel similarity, and media quality. Bold ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results on the SimplerEnv RT-1 and Language Table benchmark. We show the predicted frames and the scene flows except for Vanilla, where ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visual planning results on the VP2 benchmark. We report the mean and the min/max performance of different methods over multiple runs with different ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results on the Robodesk and Robosuite dataset. The trajectory comes from the validation set, which is split from the original training trajectories ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. The qualitative results when flows are reversed. With reversed (therefore incorrect) scene flow, the diffusion model in FlowDreamer can only utilize action condition, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct video prediction experiments on the real-world RT-1 robot manipulation dataset. | embodiment, simulator version and control stack | p. 14 (A. Implementation Details), p. 14 (A. Implementation Details) |
| Task/environment | The RT-1 real-world dataset contains more tasks, lighting conditions, and camera positions, making it a much harder task than on the simulation data. | reset, timeout, object/scene variation | p. 14 (A. Implementation Details), p. 13 (A. Implementation Details) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 6 (4.2. Visual Planning) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 6 (4.2. Visual Planning), p. 13 (A. Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4. Visual planning results on the VP2 benchmark. We report the mean and the min/max performance of different methods over multiple runs with ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| For DINOv2 L2 and CLIP scores, the correlations are weak, where we infer that the semantic metrics extracted by DINOv2 and CLIP do not ... | definition/direction/unit from same section | p. 8 (4.3. Additional Analysis on Flow Prediction) |
| Figure 7. The correlation between the flow prediction error and image assessment metrics. We show the scatter plots of SSIM (higher is better), LPIPS ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We notice that increasing sampling steps more than 20 cannot improve the accuracy of future prediction yet is more time-consuming. | definition/direction/unit from same section | p. 13 (A. Implementation Details) |
| Our world model trains and predicts based on the original observation and crops the predicted observation to calculate the visual planning reward. | definition/direction/unit from same section | p. 13 (A. Implementation Details) |
| Method Semantic Similarity Pixel Similarity Media Quality DINOv2 L2↓ CLIP score↑ PSNR↑ SSIM↑ LPIPS↓ FID↓ FVD↓ Vanilla 15.6659 0.8618 17.9724 0.5401 0.1882 13.1636 195.3965 ... | definition/direction/unit from same section | p. 14 (A. Implementation Details) |
| benchmarks, demonstrating the efficacy of our approach in both visual performance and visual planning tasks. | definition/direction/unit from same section | p. 2 (3. We perform comprehensive evaluations across several) |
| In this section, we conduct extensive experiments in four different benchmarks to verify the performance of FlowDreamer. | definition/direction/unit from same section | p. 4 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5. Qualitative results on the Robodesk and Robosuite dataset. The trajectory comes from the validation set, which is split from the original training ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3. The correlation coefficient r between the flow predic- tion error and image assessment metrics. r > 0 indicates a positive correlation and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We also design a conditional MinkowskiNet [13] as a point-cloud-based baseline. | comparison identity and matched condition | p. 13 (A. Implementation Details) |
| For the Language Table environment, we generate trajectories by the RRT* oracle policy provided in the official repositories. | comparison identity and matched condition | p. 13 (A. Implementation Details) |
| However, our performance still outperforms Vanilla, as Vanilla cannot even keep the consistency of the background during generation. | comparison identity and matched condition | p. 14 (A. Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In this section, we conduct further analysis to figure out the effect of the predicted flow. | component/input/data sensitivity | p. 8 (4.3. Additional Analysis on Flow Prediction) |
| Figure 3. Qualitative results on the SimplerEnv RT-1 and Language Table benchmark. We show the predicted frames and the scene flows except for Vanilla, ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We only finetune the parameters of the denoising network yet freeze the weight of the encoder and decoder. | component/input/data sensitivity | p. 13 (A. Implementation Details) |
| The structure of the conditional MinkowskiNet is modified from MinkUNet34B in the official repository, where we replace the batch normalization layers in the basic ... | component/input/data sensitivity | p. 13 (A. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We validate the effectiveness of our method on multiple benchmarks commonly used in robotic manipulation. | Figure 4. Visual planning results on the VP2 benchmark. We report the mean and the min/max performance of different methods over multiple runs with ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 13 (A. Implementation Details), p. 14 (A. Implementation Details) |
| Primary metric/result | Figure 3. Qualitative results on the SimplerEnv RT-1 and Language Table benchmark. We show the predicted frames and the scene flows except for Vanilla, ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 13 / A. Implementation Details - extractive body cue:** Each model is trained on 8 GPUs in parallel, with a batch size of 16 per GPU.
- **p. 13 / A. Implementation Details - extractive body cue:** For the RT-1 SimplerEnv environment, we choose 5 tasks implemented by SimplerEnv [46]: pick coke can, pick object, move near, open drawer, close drawer, and ...
- **p. 14 / A. Implementation Details - extractive body cue:** We conduct video prediction experiments on the real-world RT-1 robot manipulation dataset.
- **p. 7 / 4.2. Visual Planning - extractive body cue:** We run our experiments with 4 seeds on RoboDesk tasks and 3 seeds with Robosuite tasks, which keeps same with other VP2 experiments.
- **p. 13 / A. Implementation Details - extractive body cue:** Each model is trained on 8 GPUs in parallel, with a batch size of 16 per GPU.
- **p. 13 / A. Implementation Details - extractive body cue:** For the RT-1 SimplerEnv environment, we choose 5 tasks implemented by SimplerEnv [46]: pick coke can, pick object, move near, open drawer, close drawer, and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and Future Works While FlowDreamer has made progress, there are some limitations that could be improved by future works. | p. 14 (A. Implementation Details) |
| body limitation/failure cue | Limitations and future directions can be found in the Appendix. | p. 8 (5. Conclusion) |
| body limitation/failure cue | We can observe that the robot did not really take contrary actions due to the action input at stage 2, while its performance becomes ... | p. 8 (4.3. Additional Analysis on Flow Prediction) |
| body limitation/failure cue | We notice that increasing sampling steps more than 20 cannot improve the accuracy of future prediction yet is more time-consuming. | p. 13 (A. Implementation Details) |
| body limitation/failure cue | However, our performance still outperforms Vanilla, as Vanilla cannot even keep the consistency of the background during generation. | p. 14 (A. Implementation Details) |
| body limitation/failure cue | Depth map Dt and the scene flow ˆft→t+1 are firstly downsampled to the same shape of zt by several convolutional layers, and then channel-wise ... | p. 4 (3.3. Future Generation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All models are trained for 60k steps with a constant learning rate of 1e-4. | p. 13 (A. Implementation Details) |
| Each model is trained on 8 GPUs in parallel, with a batch size of 16 per GPU. | p. 13 (A. Implementation Details) |
| Future works could explore a better tradeoff between inference time and prediction performance. | p. 14 (A. Implementation Details) |
| We run our experiments with 4 seeds on RoboDesk tasks and 3 seeds with Robosuite tasks, which keeps same with other VP2 experiments. | p. 7 (4.2. Visual Planning) |
| We report the mean and the min/max performance of different methods over multiple runs with different random seeds. | p. 7 (4.2. Visual Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / A. Implementation Details - extractive body cue:** Limitations and Future Works While FlowDreamer has made progress, there are some limitations that could be improved by future works.
- **p. 8 / 5. Conclusion - extractive body cue:** Limitations and future directions can be found in the Appendix.
- **p. 8 / 4.3. Additional Analysis on Flow Prediction - extractive body cue:** We can observe that the robot did not really take contrary actions due to the action input at stage 2, while its performance becomes worse ...
- **p. 13 / A. Implementation Details - extractive body cue:** We notice that increasing sampling steps more than 20 cannot improve the accuracy of future prediction yet is more time-consuming.
- **p. 14 / A. Implementation Details - extractive body cue:** However, our performance still outperforms Vanilla, as Vanilla cannot even keep the consistency of the background during generation.
- **p. 4 / 3.3. Future Generation - extractive body cue:** Depth map Dt and the scene flow ˆft→t+1 are firstly downsampled to the same shape of zt by several convolutional layers, and then channel-wise concatenated ...

- **PDF anchors reviewed:** datasets p. 14 (A. Implementation Details), p. 14 (A. Implementation Details), p. 13 (A. Implementation Details), p. 13 (A. Implementation Details), p. 2 (3. We perform comprehensive evaluations across several), p. 4 (4. Experiments), metrics p. 7 (Figure/Table caption), p. 8 (4.3. Additional Analysis on Flow Prediction), p. 8 (Figure/Table caption), p. 13 (A. Implementation Details), p. 13 (A. Implementation Details), p. 14 (A. Implementation Details), baselines p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 13 (A. Implementation Details), p. 13 (A. Implementation Details), p. 14 (A. Implementation Details), results p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 13 (A. Implementation Details), p. 14 (A. Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
