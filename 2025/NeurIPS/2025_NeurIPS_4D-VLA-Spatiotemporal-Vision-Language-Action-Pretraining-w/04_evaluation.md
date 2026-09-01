# Evaluation - 4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yFjgV3cJje; PDF retrieval source: https://openreview.net/pdf/d30c75fa560b194e7ca1144a7d0d1dad6a0ee401.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption)): Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data.

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and simulation environments DROID [2] A diverse real-world robot manipulation dataset with 76,000 demonstration trajectories, or 350 hours of interaction data, spanning a ...
- **p. 6 / 4 Experiments - extractive PDF cue:** LIBERO [4] The LIBERO benchmark is a simulation suite with 4 task sets designed to advance lifelong learning in robotic manipulation.
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.5 Real-world evaluation To evaluate models in real-world scenarios, we conducted physical experiments using a Franka robotic arm.
- **p. 5 / 4 Experiments - extractive PDF cue:** We first introduce the datasets and simulation environment, then describe pretraining and fine-tuning.
- **p. 5 / 4 Experiments - extractive PDF cue:** Our model is pretrained on real-world data and fine-tuned with both simulation and real-world trajectories.
- **p. 7 / 4 Experiments - extractive PDF cue:** Task2: Robustness to distractors Task3: Precise placement Task4: Instruction following Figure 4: Our real-world experiment settings.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Our real-world experiment settings. These settings aim to evaluate the model's spatial generalization, robustness to distractors, precision in placement, and ability to follow ...
- **p. 6 / 4 Experiments - extractive PDF cue:** Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, our model achieves a 81.0% success rate in the In-View setting, demonstrating its capability to handle diverse training views effectively. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On average, 4D-VLA improves success rate by 12.1% than OpenVLA, demonstrating stronger stability and spatiotemporal reasoning in complex settings. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | UniAct-0.5B [33]† 64.5 77.5 68.0 46.5 64.1 SparseVLM [34]† 79.8 67.0 72.6 39.4 64.7 FastV [35]† 83.4 84.0 74.2 51.6 73.3 VLA-Cache [36]† 83.8 ... | p. 6 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 8: Frame sampling ablations on Libero-Spatial. MBS attains the highest success (0.866) with competitive efficiency, while single-frame is fastest and most memory-light but ... | p. 22 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and simulation environments DROID [2] A diverse real-world robot manipulation dataset with 76,000 demonstration trajectories, or 350 hours of interaction data, spanning a ...
- **p. 6 / 4 Experiments - extractive PDF cue:** LIBERO [4] The LIBERO benchmark is a simulation suite with 4 task sets designed to advance lifelong learning in robotic manipulation.
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.5 Real-world evaluation To evaluate models in real-world scenarios, we conducted physical experiments using a Franka robotic arm.
- **p. 5 / 4 Experiments - extractive PDF cue:** We first introduce the datasets and simulation environment, then describe pretraining and fine-tuning.
- **p. 5 / 4 Experiments - extractive PDF cue:** Our model is pretrained on real-world data and fine-tuned with both simulation and real-world trajectories.
- **p. 7 / 4 Experiments - extractive PDF cue:** Task2: Robustness to distractors Task3: Precise placement Task4: Instruction following Figure 4: Our real-world experiment settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Top: Our pretraining design philosophy highlights that prior methods often lack key cues in their input for accurate action inference. This leads to ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Our 4D-VLA pipeline. Our memory bank sampling method selects informative frames from sequential RGB-D inputs. A vision encoder with 3D coordinate embeddings generates ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Our MV-Bench camera setting. We select 6 diverse viewpoints as training views and render images for all LIBERO-SPATIAL tasks. Novel inference views are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Evaluation of success rate on LIBERO. Bold indicates the best-performing model. Our model significantly outperforms other competitors, with an average success rate 12.1 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Our real-world experiment settings. These settings aim to evaluate the model's spatial generalization, robustness to distractors, precision in placement, and ability to follow ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Evaluation of success rate on MV-Bench. ∆symbol representing the angular deviation from the nearest training viewpoint along the z-axis. As shown in Tab. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Real-world evaluation results. We incrementally improve the Base VLA by adding pretraining, coordinate encoding, and historical frames selected via memory bank sampling . ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Our multi-view real-world experiment settings. These settings aim to evaluate the model's out-of-distribution and novel-view generalization ability.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 Datasets and simulation environments DROID [2] A diverse real-world robot manipulation dataset with 76,000 demonstration trajectories, or 350 hours of interaction data, spanning ... | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Task/environment | LIBERO [4] The LIBERO benchmark is a simulation suite with 4 task sets designed to advance lifelong learning in robotic manipulation. | reset, timeout, object/scene variation | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3 Method), p. 5 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3 Method), p. 4 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Our real-world experiment settings. These settings aim to evaluate the model's spatial generalization, robustness to distractors, precision in placement, and ability to ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| To evaluate each task, we randomly sample 3 different seeds to calculate the mean and standard deviation of the success rate. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| UniAct-0.5B [33]† 64.5 77.5 68.0 46.5 64.1 SparseVLM [34]† 79.8 67.0 72.6 39.4 64.7 FastV [35]† 83.4 84.0 74.2 51.6 73.3 VLA-Cache [36]† 83.8 ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Figure 6: Historical image analysis. Larger points indicate lower efficiency. Encoding Position Fusion Success rate learnable relative | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 8: Frame sampling ablations on Libero-Spatial. MBS attains the highest success (0.866) with competitive efficiency, while single-frame is fastest and most memory-light but ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 7: Success rates under varying coor- dinate chaos levels. Chaos generation. To simulate the diverse view- points in the pretraining dataset-where the robot's ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 1: Top: Our pretraining design philosophy highlights that prior methods often lack key cues in their input for accurate action inference. This leads ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | comparison identity and matched condition | p. 6 (4 Experiments) |
| This result shows that the integration of spatiotemporal information enables our model to manage challenging and conflicting perspectives, outperforming OpenVLA [1] by a significant ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Figure 1: Top: Our pretraining design philosophy highlights that prior methods often lack key cues in their input for accurate action inference. This leads ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| In addition, we evaluate on the ARM4R [32] benchmark for a direct comparison with ARM4R. | comparison identity and matched condition | p. 5 (4 Experiments) |
| Table 5: Ablation on temporal encoding | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Table 7: Ablations on heads and inputs (Libero-Long). Left: action head vs. FPS and success (MLP, autoregressive, diffusion). Right: effect of pretraining, 3D coordinate ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7: Ablations on heads and inputs (Libero-Long). Left: action head vs. FPS and success (MLP, autoregressive, diffusion). Right: effect of pretraining, 3D coordinate ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Table 8: Frame sampling ablations on Libero-Spatial. MBS attains the highest success (0.866) with competitive efficiency, while single-frame is fastest and most memory-light but ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| We remove frames with unchanged proprioception, specifically the stationary frames, and exclude trajectories with a total action count exceeding 600. | component/input/data sensitivity | p. 6 (4 Experiments) |
| Unlike the pretraining phase, we used the simplest input settings to enable our model to learn the interaction effects between 3D information and historical ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| We first introduce the datasets and simulation environment, then describe pretraining and fine-tuning. | component/input/data sensitivity | p. 5 (4 Experiments) |
| Our model is pretrained on real-world data and fine-tuned with both simulation and real-world trajectories. | component/input/data sensitivity | p. 5 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are: (i) We propose 4D-VLA, an efficient VLA model that integrates a spatial module with vision features to generate 3D-aware spatial vision ... | Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | 2, our model achieves a 81.0% success rate in the In-View setting, demonstrating its capability to handle diverse training views effectively. | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive PDF cue:** UniAct-0.5B [33]† 64.5 77.5 68.0 46.5 64.1 SparseVLM [34]† 79.8 67.0 72.6 39.4 64.7 FastV [35]† 83.4 84.0 74.2 51.6 73.3 VLA-Cache [36]† 83.8 85.8 ...
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and simulation environments DROID [2] A diverse real-world robot manipulation dataset with 76,000 demonstration trajectories, or 350 hours of interaction data, spanning a ...
- **p. 6 / 4 Experiments - extractive PDF cue:** LIBERO [4] The LIBERO benchmark is a simulation suite with 4 task sets designed to advance lifelong learning in robotic manipulation.
- **p. 6 / 4 Experiments - extractive PDF cue:** LIBERO-100 includes 90 short-horizon (LIBERO-90) and 10 long-horizon (LIBERO-LONG) tasks, covering 130 subtasks, each with 50 trajectories captured from both a main and wrist-mounted camera.
- **p. 6 / 4 Experiments - extractive PDF cue:** RGB-D frames are resized to 448×252, and each trajectory is uniformly downsampled to 100 actions.
- **p. 6 / 4 Experiments - extractive PDF cue:** Our model was trained for 1 epoch with a batch size of 512, requiring around 20k steps to complete.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A limitation of our approach is its reliance on RGB-D input, which introduces hardware restriction. | p. 10 (6 Conclusion) |
| body limitation/failure cue | To avoid occlusion from the black box, test views in blocked areas are excluded. | p. 6 (4 Experiments) |
| body limitation/failure cue | It highlights the robustness of our model in handling diverse viewpoints. | p. 7 (4 Experiments) |
| body limitation/failure cue | Task2: Robustness to distractors Task3: Precise placement Task4: Instruction following Figure 4: Our real-world experiment settings. | p. 7 (4 Experiments) |
| body limitation/failure cue | Figure 5: Our multi-view real-world experiment settings. These settings aim to evaluate the model's out-of-distribution and novel-view generalization ability. | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 4: Real-world multi-view evaluation. We test our model's spatial generalization across varying viewpoints and object layouts. 4D-VLA shows strong in-view and cross-view performance, ... | p. 9 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We employed a cosine learning rate scheduler with a learning rate of 4e-5, using a batch size of 128 and training for 20 epochs. ... | p. 7 (4 Experiments) |
| Our model was trained for 1 epoch with a batch size of 512, requiring around 20k steps to complete. | p. 6 (4 Experiments) |
| We utilize a cosine learning rate scheduler with an initial learning rate of 2e-5. | p. 6 (4 Experiments) |
| We run closed-loop evaluations in diverse environments and report task performance. | p. 5 (4 Experiments) |
| The random seed is used to alter the initial state of the objects. | p. 7 (4 Experiments) |
| The evaluation metric is the task success rate, computed as the ratio of successful trials to the total number of trials. | p. 9 (Method) |
| These multimodal tokens are then fed into the decoder D for next-token prediction. | p. 3 (3 Method) |
| The vision encoder processes visual observations, which are subsequently compressed by an MLP projector P to generate vision embeddings, while text inputs are tokenized ... | p. 3 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 Conclusion - extractive PDF cue:** A limitation of our approach is its reliance on RGB-D input, which introduces hardware restriction.
- **p. 6 / 4 Experiments - extractive PDF cue:** To avoid occlusion from the black box, test views in blocked areas are excluded.
- **p. 7 / 4 Experiments - extractive PDF cue:** It highlights the robustness of our model in handling diverse viewpoints.
- **p. 7 / 4 Experiments - extractive PDF cue:** Task2: Robustness to distractors Task3: Precise placement Task4: Instruction following Figure 4: Our real-world experiment settings.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Our multi-view real-world experiment settings. These settings aim to evaluate the model's out-of-distribution and novel-view generalization ability.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Real-world multi-view evaluation. We test our model's spatial generalization across varying viewpoints and object layouts. 4D-VLA shows strong in-view and cross-view performance, highlighting ...

- **PDF anchors reviewed:** datasets p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 5 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (Figure/Table caption), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), baselines p. 6 (4 Experiments), p. 7 (4 Experiments), p. 1 (Figure/Table caption), p. 5 (4 Experiments), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), results p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 22 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
