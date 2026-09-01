# Evaluation - PointVLA: Injecting the 3D World into Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.07511; PDF retrieval source: https://arxiv.org/pdf/2503.07511. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.1. Implementation Details)): Notably, across all tasks and diverse settings, our proposed PointVLA achieves the highest average success rate, regardless of whether it is trained on 20 or 50 demonstrations.

## Evaluation Body Digest

- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment.
- **p. 5 / 4. Experiment - extractive body cue:** Finally, we compare our method against simulation benchmarks.
- **p. 6 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** These tasks assess the model's capability to manage both independent and coordinated robot movements across diverse scenarios.
- **p. 6 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** As illustrated in Fig 5, we designed four few-shot tasks for our real-world experiment: ChargePhone, WipePlate, PlaceBread, TransportFruit.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** First, the assembly line is in motion, requiring the robot to quickly and precisely grasp objects.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Third, as a long-range task, the robot must sequentially pick and place two bags of laundry detergent before sealing the packing box.
- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** This benchmark encompasses a diverse set of tasks.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** In this work, we conduct real robot experiments on two embodiments: • Bimanual UR5e.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Implementation Details (p. 5); 4.6. Experimental Results on Simulation Bench (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.6. Experimental Results on Simulation Bench | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, across all tasks and diverse settings, our proposed PointVLA achieves the highest average success rate, regardless of whether it is trained on 20 ... | p. 8 (4.6. Experimental Results on Simulation Bench) |
| 4.6. Experimental Results on Simulation Bench | EMPIRICAL / REAL-ROBOT OR HARDWARE | The mean and standard deviation of these success rates were computed to obtain the experimental results presented below. | p. 8 (4.6. Experimental Results on Simulation Bench) |
| 4.2. Few-Shot Multi-Tasking | EMPIRICAL / REAL-ROBOT OR HARDWARE | We show experimental results on the bottom table. sented in Table 6, where our method outperforms all baselines in this scenario. | p. 7 (4.2. Few-Shot Multi-Tasking) |
| 4.2. Few-Shot Multi-Tasking | EMPIRICAL / REAL-ROBOT OR HARDWARE | Objects were placed randomly within a small range, and we report the average success rate for each method. | p. 6 (4.2. Few-Shot Multi-Tasking) |
| 4.2. Few-Shot Multi-Tasking | EMPIRICAL / REAL-ROBOT OR HARDWARE | RealSense L515 Robotiq gripper Bimanual UR5e RealSense D435i RealSense D435i L515 Point Cloud L515 Image L515 Point Cloud L515 Image No Object Model Success ... | p. 7 (4.2. Few-Shot Multi-Tasking) |

## Dataset / Benchmark Role

- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment.
- **p. 5 / 4. Experiment - extractive body cue:** Finally, we compare our method against simulation benchmarks.
- **p. 6 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** These tasks assess the model's capability to manage both independent and coordinated robot movements across diverse scenarios.
- **p. 6 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** As illustrated in Fig 5, we designed four few-shot tasks for our real-world experiment: ChargePhone, WipePlate, PlaceBread, TransportFruit.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** First, the assembly line is in motion, requiring the robot to quickly and precisely grasp objects.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Third, as a long-range task, the robot must sequentially pick and place two bags of laundry detergent before sealing the packing box.
- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** This benchmark encompasses a diverse set of tasks.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** In this work, we conduct real robot experiments on two embodiments: • Bimanual UR5e.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. PointVLA builds upon the strengths of VLA, which is pre-trained on large-scale 2D robot data while incorporating 3D world into the action expert. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of PointVLA framework. Left: The 2D image observation and instruction are processed by the vision-language model. The vanilla action expert remains frozen, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Skip block analysis for action expert in VLA model. Left: skipping only one block at a time. Right: Skipping multiple consecutive blocks starting ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Setup for bimanual UR5e. We utilize three cameras: two RealSense D435i mounted on the wrists and one RealSense L515 positioned above. Our model ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Setup for bimanual AgileX. We utilize three cameras: two RealSense D435i mounted on the wrists and one RealSense L515 positioned above. Our model ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Experimental results on few-shot multi-tasking on bimanual AgileX. last checkpoint for evaluation to avoid cherry picking. We set chunk size to 50 for ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. The experimental setup for real-vs-photo discrimi- nation. We replace the real laundry detergent with its photo dis- played on a screen placed on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Experimental results for long-horizon task on biman- ual UR5e. The task is completed in a sequence. The Avg. Len. denotes the average success ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment. | embodiment, simulator version and control stack | p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment) |
| Task/environment | Finally, we compare our method against simulation benchmarks. | reset, timeout, object/scene variation | p. 5 (4. Experiment), p. 6 (4.2. Few-Shot Multi-Tasking) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.2. Injecting Point Cloud into VLA), p. 3 (3. Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The mean and standard deviation of these success rates were computed to obtain the experimental results presented below. | definition/direction/unit from same section | p. 8 (4.6. Experimental Results on Simulation Bench) |
| Objects were placed randomly within a small range, and we report the average success rate for each method. | definition/direction/unit from same section | p. 6 (4.2. Few-Shot Multi-Tasking) |
| RealSense L515 Robotiq gripper Bimanual UR5e RealSense D435i RealSense D435i L515 Point Cloud L515 Image L515 Point Cloud L515 Image No Object Model Success ... | definition/direction/unit from same section | p. 7 (4.2. Few-Shot Multi-Tasking) |
| Each policy was then tested 100 times, yielding three success rates. | definition/direction/unit from same section | p. 8 (4.6. Experimental Results on Simulation Bench) |
| DexVLA demonstrates strong few-shot learning capabilities despite the limited data; however, its performance remains on par with or inferior to PointVLA. | definition/direction/unit from same section | p. 7 (4.2. Few-Shot Multi-Tasking) |
| The phone's size tests action precision, while its fragility requires careful handling. | definition/direction/unit from same section | p. 6 (4.2. Few-Shot Multi-Tasking) |
| Table 2. Experimental results on RoboTwin [32]. Performance comparison across different tasks and demonstrations (results for 20 and 50 demonstrations). ing. Experiments in both ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 2. Overview of PointVLA framework. Left: The 2D image observation and instruction are processed by the vision-language model. The vanilla action expert remains ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 6. Experimental results on few-shot multi-tasking on bimanual AgileX. last checkpoint for evaluation to avoid cherry picking. We set chunk size to 50 ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| In our experiments, we compared with many state-of-the-art model, including the Diffusion Policy (DP) [9], 3D Diffusion Policy (DP3) [51], ScaleDP-1B [57], a variant ... | comparison identity and matched condition | p. 6 (4.1. Implementation Details) |
| It also outperforms several other baselines. | comparison identity and matched condition | p. 7 (4.2. Few-Shot Multi-Tasking) |
| We show experimental results on the bottom table. sented in Table 6, where our method outperforms all baselines in this scenario. | comparison identity and matched condition | p. 7 (4.2. Few-Shot Multi-Tasking) |
| Baseline results, including those for the 3D Diffusion Policy and Diffusion Policy, are reported by RoboTwin. | comparison identity and matched condition | p. 8 (4.6. Experimental Results on Simulation Bench) |
| Diffusion Policy is a well-established baseline for visuomotor policy learning, while DP3 extends it to the 3D domain. | comparison identity and matched condition | p. 8 (4.6. Experimental Results on Simulation Bench) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Note that since PointVLA is built on top of DexVLA, the DexVLA can be viewed as an ablation of our proposed PointVLA without the ... | component/input/data sensitivity | p. 6 (4.1. Implementation Details) |
| In our experiments, we compared with many state-of-the-art model, including the Diffusion Policy (DP) [9], 3D Diffusion Policy (DP3) [51], ScaleDP-1B [57], a variant ... | component/input/data sensitivity | p. 6 (4.1. Implementation Details) |
| Following the training setup in RoboTwin, the policy was trained using three random seeds (0, 1, 2) without cherry picking for each experiment. | component/input/data sensitivity | p. 8 (4.6. Experimental Results on Simulation Bench) |
| For both experiments, we use stage 1 pre-trained weights from DexVLA [46] and fine-tune for our model. | component/input/data sensitivity | p. 5 (4.1. Implementation Details) |
| Specifically, we replace the real object with a picture of the object. | component/input/data sensitivity | p. 7 (4.4. Real-vs-Photo Discrimination) |
| We replace the real laundry detergent with its photo displayed on a screen placed on the conveyor belt. | component/input/data sensitivity | p. 7 (4.2. Few-Shot Multi-Tasking) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce PointVLA, a novel framework that integrates point clouds into pre-trained visionlanguage-action models. | Notably, across all tasks and diverse settings, our proposed PointVLA achieves the highest average success rate, regardless of whether it is trained on 20 ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.1. Implementation Details) |
| Primary metric/result | The mean and standard deviation of these success rates were computed to obtain the experimental results presented below. | numeric claim only at cited anchor | p. 8 (4.6. Experimental Results on Simulation Bench) |

- Numeric sentences retained from the body:
- **p. 8 / 4.6. Experimental Results on Simulation Bench - extractive body cue:** The tests were conducted using datasets of 20 and 50 samples.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, the Diffusion Policy fails in most cases, likely because the sample size for each task is too small, causing the action representation space ... | p. 7 (4.2. Few-Shot Multi-Tasking) |
| body limitation/failure cue | Since the model believes the object is present but continuously fails to grasp it, it enters a repetitive grasping loop. | p. 8 (4.4. Real-vs-Photo Discrimination) |
| body limitation/failure cue | Furthermore, even increasing the model size (ScaleDP-1B) does not lead to significant improvement. | p. 7 (4.2. Few-Shot Multi-Tasking) |
| body limitation/failure cue | Our observations show that conventional 2D-based VLA models, such as OpenVLA [25], DP [9], ScaleDP-1B [57], and DexVLA [46] all failed in this scenario. | p. 8 (4.5. Height Adaptability) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the same training hyperparameters as the stage 2 training in DexVLA, and use the 5 | p. 5 (4.1. Implementation Details) |
| Experimental results on few-shot multi-tasking on bimanual AgileX. last checkpoint for evaluation to avoid cherry picking. | p. 6 (4.1. Implementation Details) |
| The implementation is carried out by RoboTwin. | p. 8 (4.6. Experimental Results on Simulation Bench) |
| The mean and standard deviation of these success rates were computed to obtain the experimental results presented below. | p. 8 (4.6. Experimental Results on Simulation Bench) |
| This architecture is similar to the iDP3 encoder. | p. 4 (3.2. Injecting Point Cloud into VLA) |
| We believe that employing a more advanced point cloud encoder could further enhance model performance. | p. 4 (3.2. Injecting Point Cloud into VLA) |
| The evaluation follows the same metrics-average score, a standard measure for long-horizon tasks [4, 31, 46]-by dividing the task into multiple steps and assessing ... | p. 5 (3.3. Which Blocks to Inject Point Cloud? A Skip) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Notably, the Diffusion Policy fails in most cases, likely because the sample size for each task is too small, causing the action representation space to ...
- **p. 8 / 4.4. Real-vs-Photo Discrimination - extractive body cue:** Since the model believes the object is present but continuously fails to grasp it, it enters a repetitive grasping loop.
- **p. 7 / 4.2. Few-Shot Multi-Tasking - extractive body cue:** Furthermore, even increasing the model size (ScaleDP-1B) does not lead to significant improvement.
- **p. 8 / 4.5. Height Adaptability - extractive body cue:** Our observations show that conventional 2D-based VLA models, such as OpenVLA [25], DP [9], ScaleDP-1B [57], and DexVLA [46] all failed in this scenario.

- **PDF anchors reviewed:** datasets p. 8 (4.6. Experimental Results on Simulation Bench), p. 5 (4. Experiment), p. 6 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), metrics p. 8 (4.6. Experimental Results on Simulation Bench), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), p. 8 (4.6. Experimental Results on Simulation Bench), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking), baselines p. 6 (Figure/Table caption), p. 6 (4.1. Implementation Details), p. 7 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench), results p. 8 (4.6. Experimental Results on Simulation Bench), p. 8 (4.6. Experimental Results on Simulation Bench), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.2. Few-Shot Multi-Tasking), p. 7 (4.2. Few-Shot Multi-Tasking), p. 6 (4.1. Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
