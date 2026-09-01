# Evaluation - 3D Equivariant Visuomotor Policy Learning via Spherical Projection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kXJd4JxF34; PDF retrieval source: https://openreview.net/pdf/20cb87b1441d2401c9489c5c43e121f801b3a4ee.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 8 (5 Experiments), p. 19 (Figure/Table caption)): Figure 6: Real-world environments for evaluation. A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations. In each subfigure, the left image shows the initial state, while ...

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive PDF cue:** 5.1 Simulation Experiment Setting We evaluate ISP on twelve robotic manipulation tasks from the MimicGen benchmark [40], which is widely used in previous work on ...
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** D1 Nut Assembly D0 ISP-SO(2) (Pretraining) 54.0 (-2.0) 66.7 (+8.0) 64.0 (-0.7) 56.3 (+10.6) 63.3 (+16.6) 85.0 (+11.3) ISP-SO(2) (Scratch) 56.0 58.7 64.7 45.7 46.7 ...
- **p. 10 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** These results demonstrate that the proposed method generalizes well to real-world disturbances and maintains strong task performance under challenging visual conditions.
- **p. 10 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** (a) Lighting Change (b) Background Clutter (c) Partial Camera Occlusion Figure 7: Real-world perturbation scenarios used to evaluate the robustness and generalization of our method ...
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations.
- **p. 18 / C Implementation of Our Policy - extractive PDF cue:** For the real-world experiments, we use the same hyperparameters as in the simulation, except that we replace DDPM with DDIM [55] for both training and ...
- **p. 20 / C Implementation of Our Policy - extractive PDF cue:** I Practical Guidelines for Data Collection Before starting data collection on the real robot, it is critical to establish a predefined task execution strategy to ...
- **p. 20 / C Implementation of Our Policy - extractive PDF cue:** Such a strategy typically involves defining consistent action sequences, execution ranges, and task progression patterns, helping to avoid ambiguous or poorly structured scenarios that may ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiments (p. 7); C Implementation of Our Policy (p. 16); 4. Experimental result reproducibility (p. 26); 7. Experiment statistical significance (p. 28); 8. Experiments compute resources (p. 28).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Real-world environments for evaluation. A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations. In each subfigure, the left ... | p. 9 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In terms of performance, ISP-SO(3) achieves the best results in 21 out of 24 task settings, consistently outperforming the baselines. | p. 8 (5 Experiments) |
| 68.7 58.7 58.0 32.0 54.3 (-6.7) | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the Grocery Bag task, which heavily relies on eye-in-hand perception, our method achieves a 95% success rate. | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| 68.7 58.7 58.0 32.0 54.3 (-6.7) | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using the same initial states and 20 rollouts per condition as in the previous real-world experiments, ISP-SO(2) achieves success rates of 85% under lighting ... | p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | These results collectively highlight that the explicit modeling of equivariance is the key factor driving both the improved performance and enhanced sample efficiency of ... | p. 8 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive PDF cue:** 5.1 Simulation Experiment Setting We evaluate ISP on twelve robotic manipulation tasks from the MimicGen benchmark [40], which is widely used in previous work on ...
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** D1 Nut Assembly D0 ISP-SO(2) (Pretraining) 54.0 (-2.0) 66.7 (+8.0) 64.0 (-0.7) 56.3 (+10.6) 63.3 (+16.6) 85.0 (+11.3) ISP-SO(2) (Scratch) 56.0 58.7 64.7 45.7 46.7 ...
- **p. 10 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** These results demonstrate that the proposed method generalizes well to real-world disturbances and maintains strong task performance under challenging visual conditions.
- **p. 10 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** (a) Lighting Change (b) Background Clutter (c) Partial Camera Occlusion Figure 7: Real-world perturbation scenarios used to evaluate the robustness and generalization of our method ...
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations.
- **p. 18 / C Implementation of Our Policy - extractive PDF cue:** For the real-world experiments, we use the same hyperparameters as in the simulation, except that we replace DDPM with DDIM [55] for both training and ...
- **p. 20 / C Implementation of Our Policy - extractive PDF cue:** I Practical Guidelines for Data Collection Before starting data collection on the real robot, it is critical to establish a predefined task execution strategy to ...
- **p. 20 / C Implementation of Our Policy - extractive PDF cue:** Such a strategy typically involves defining consistent action sequences, execution ranges, and task progression patterns, helping to avoid ambiguous or poorly structured scenarios that may ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: We propose the first SO(3)-equivariant policy learning framework based on a single eye- in-hand RGB image, where the predicted action sequence transforms equivariantly ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of Image-to-Sphere Policy (ISP) (a) An SO(3)-equivariant observation encoder extracts features from the RGB input, projects them onto the sphere, and applies ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Illustration of Equivariance Correction. The left side shows two identical scenes under different global transformations. Since the wrist-mounted camera captures images in its ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: A subset of experimental environments from MimicGen. Left: external view of the task. Right: eye-in-hand observation used in the experiments. The full set ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Illustration of translation invariance and rotation equivariance- to-invariance transition. The benefit of SO(2) camera-rotation invariance (Proposi- tion 2) is subtle. Under a rotation ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Success rates (%) on MimicGen tasks with 100 and 200 demonstrations, averaged over 3 seeds. We report both overall mean and per-task performance. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation study results. A red cross indicates that the corresponding module is removed in that variant. Sphere EquiEnc EquiU Sta. Cof. Nut. Squ. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Success rates (%) on MimicGen tasks with 100 demonstrations, comparing pretrained and scratch initialization of the equivariant image encoder. Results are averaged over ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.1 Simulation Experiment Setting We evaluate ISP on twelve robotic manipulation tasks from the MimicGen benchmark [40], which is widely used in previous work ... | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Task/environment | D1 Nut Assembly D0 ISP-SO(2) (Pretraining) 54.0 (-2.0) 66.7 (+8.0) 64.0 (-0.7) 56.3 (+10.6) 63.3 (+16.6) 85.0 (+11.3) ISP-SO(2) (Scratch) 56.0 58.7 64.7 45.7 ... | reset, timeout, object/scene variation | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 Background), p. 4 (4 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3 Background), p. 3 (3 Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Success rates (%) on MimicGen tasks with 100 and 200 demonstrations, averaged over 3 seeds. We report both overall mean and per-task ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 5: Maximum success rates (%) on MimicGen tasks with 100 and 200 demonstrations across different methods, averaged over three random seeds. The ± ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| We report the average of the best success rates from the three runs. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| D0 Method 100 200 100 200 100 200 100 200 100 200 100 200 ISP-SO(3) 54 59 64 69 75 79 42 66 41 ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| On the Grocery Bag task, which heavily relies on eye-in-hand perception, our method achieves a 95% success rate. | definition/direction/unit from same section | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Using the same initial states and 20 rollouts per condition as in the previous real-world experiments, ISP-SO(2) achieves success rates of 85% under lighting ... | definition/direction/unit from same section | p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Table 3: Success rates (%) on MimicGen tasks with 100 demonstrations, comparing pretrained and scratch initialization of the equivariant image encoder. Results are averaged ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| These results demonstrate that the proposed method generalizes well to real-world disturbances and maintains strong task performance under challenging visual conditions. | definition/direction/unit from same section | p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Similarly, ISP-SO(2) outperforms baselines in 20 settings, which further validates the effectiveness of our design. | comparison identity and matched condition | p. 8 (5 Experiments) |
| In terms of performance, ISP-SO(3) achieves the best results in 21 out of 24 task settings, consistently outperforming the baselines. | comparison identity and matched condition | p. 8 (5 Experiments) |
| Our method consistently outperforms the Diffusion Policy [5] baseline, with significant improvements on Box-Pipe (80% vs. | comparison identity and matched condition | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| We compare against three strong baselines: (1) Diffusion Policy [5]: A diffusion-based policy without any equivariance, serving as the primary reference. | comparison identity and matched condition | p. 7 (5 Experiments) |
| Figure 9: Real-world experimental setup. We use a UR5 robot equipped with a Robotiq-85 gripper and custom-designed soft fingers. A GoPro camera is mounted ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| Baselines Our experiments aim to validate the benefits of explicitly modeling equivariance in eyein-hand visuomotor policies. | comparison identity and matched condition | p. 7 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To ensure a fair comparison, all experiments in the following sections, including ablations and method variants, consistently apply SO(2) data augmentation during training by ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| Table 2: Ablation study results. A red cross indicates that the corresponding module is removed in that variant. Sphere EquiEnc EquiU Sta. Cof. Nut. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| (3) EquiU: With or without an equivariant temporal denoising U-Net in the diffusion module. | component/input/data sensitivity | p. 8 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| These results confirm the effectiveness of our equivariant design in addressing diverse manipulation challenges in the real world. | component/input/data sensitivity | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Specifically, we evaluated (a) a variant of our method without rotation correction that uses delta control, and (b) the original Diffusion Policy with delta ... | component/input/data sensitivity | p. 18 (C Implementation of Our Policy) |
| For eyein-hand control, we replace its image encoder with a standard ResNet [12], so only proprioception and denoising remain equivariant. | component/input/data sensitivity | p. 7 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our key contributions are summarized as follows: • We introduce Image-to-Sphere Policy (ISP), the first SO(3)-equivariant policy learning framework that uses spherical projection from ... | Figure 6: Real-world environments for evaluation. A GoPro camera is mounted on the robot's wrist to capture eye-in-hand observations. In each subfigure, the left ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 8 (5 Experiments), p. 19 (Figure/Table caption) |
| Primary metric/result | In terms of performance, ISP-SO(3) achieves the best results in 21 out of 24 task settings, consistently outperforming the baselines. | numeric claim only at cited anchor | p. 8 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 5 Experiments - extractive PDF cue:** In terms of performance, ISP-SO(3) achieves the best results in 21 out of 24 task settings, consistently outperforming the baselines.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** Demonstrations are collected via the Gello teleoperation interface [68], with observations and actions recorded at 5 Hz.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** Results Table 4 reports success rates over 20 trials per task.
- **p. 10 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** Using the same initial states and 20 rollouts per condition as in the previous real-world experiments, ISP-SO(2) achieves success rates of 85% under lighting changes, ...
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** To enable the wrist-mounted camera to capture more contextual information, we increase its FOV from 75 to 130 degrees, similar to that of a typical ...
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** In both cases, the denoising network outputs a sequence of 16 action steps, which are used for optimization during training, while only the first 8 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations Our method has several limitations for future investigation. | p. 10 (6 Conclusion) |
| body limitation/failure cue | See Appendix J for a detailed failure analysis. | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| body limitation/failure cue | Finally, our method does not yet leverage vision-language models. | p. 10 (6 Conclusion) |
| body limitation/failure cue | In addition, we discuss potential limitations and practical considerations of equivariance in Appendix L. | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| body limitation/failure cue | Generalization Perspective Although gripper-relative control guarantees invariance under singlecamera setups, it does not generalize seamlessly to multi-camera or hybrid sensing configurations, where additional viewpoints ... | p. 19 (C Implementation of Our Policy) |
| body limitation/failure cue | Finally, an equivariant decoder maps the denoised representation to the noise estimate ϵk. | p. 17 (C Implementation of Our Policy) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For all baselines, we retain their original hyperparameter settings for evaluation and only adjust the number of training steps to ensure consistency across methods. | p. 17 (C Implementation of Our Policy) |
| For the real-world experiments, we use the same hyperparameters as in the simulation, except that we replace DDPM with DDIM [55] for both training ... | p. 18 (C Implementation of Our Policy) |
| For eyein-hand control, we replace its image encoder with a standard ResNet [12], so only proprioception and denoising remain equivariant. | p. 7 (5 Experiments) |
| For each task, we train three independent models with different random seeds (0, 1, and 2) for each of the 100- and 200-demonstration settings. | p. 7 (5 Experiments) |
| Appendix F provides the full experimental results with standard deviations across three random seeds. | p. 8 (5 Experiments) |
| We compare the ISP-SO(2) with two variants: Pretraining, which initializes the image encoder with an 8 | p. 8 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Results are averaged over three seeds. | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |
| Results Table 4 reports success rates over 20 trials per task. | p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 Conclusion - extractive PDF cue:** Limitations Our method has several limitations for future investigation.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** See Appendix J for a detailed failure analysis.
- **p. 10 / 6 Conclusion - extractive PDF cue:** Finally, our method does not yet leverage vision-language models.
- **p. 9 / 68.7 58.7 58.0 32.0 54.3 (-6.7) - extractive PDF cue:** In addition, we discuss potential limitations and practical considerations of equivariance in Appendix L.
- **p. 19 / C Implementation of Our Policy - extractive PDF cue:** Generalization Perspective Although gripper-relative control guarantees invariance under singlecamera setups, it does not generalize seamlessly to multi-camera or hybrid sensing configurations, where additional viewpoints can ...
- **p. 17 / C Implementation of Our Policy - extractive PDF cue:** Finally, an equivariant decoder maps the denoised representation to the noise estimate ϵk.

- **PDF anchors reviewed:** datasets p. 7 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 18 (C Implementation of Our Policy), metrics p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)), baselines p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 7 (5 Experiments), p. 19 (Figure/Table caption), p. 7 (5 Experiments), results p. 9 (Figure/Table caption), p. 8 (5 Experiments), p. 9 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 10 (68.7 58.7 58.0 32.0 54.3 (-6.7)), p. 8 (5 Experiments), p. 19 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
