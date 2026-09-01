# Evaluation - DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=VdwdU81Uzy; PDF retrieval source: https://openreview.net/pdf/d9ad5d722d8a8e6e1a4f5748391ef1c439c2c706.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 6 (4.2. Real-World Multi-Task Learning), p. 7 (4.3. End-to-End Sorting on Real Robot), p. 7 (4.3. End-to-End Sorting on Real Robot)): Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success rate, outperforming the runner-up OpenVLA by ...

## Evaluation Body Digest

- **p. 8 / 4.5. Zero-Shot Bin Picking of Unseen Objects - extractive PDF cue:** (c) Seen Tableware (d) Unseen Tableware (a) Bimanual Robot Setup (b) Setup for Table Bussing (e) Seen Trash (f) Unseen Trash Figure 9: (a) Environmental ...
- **p. 7 / 4.5. Zero-Shot Bin Picking of Unseen Objects - extractive PDF cue:** This section evaluates instance generalization for DiVLA, focusing specifically on the bin-picking task-a standard benchmark for assessing robot model performance.
- **p. 8 / 4.5. Zero-Shot Bin Picking of Unseen Objects - extractive PDF cue:** It highlights the potential for applications in dynamic, unstructured environments where robots encounter unfamiliar objects and must perform tasks with minimal human intervention.
- **p. 6 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** The task is considered successful only if the robot successfully grasps the object and places it in the correct sector.
- **p. 6 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** We evaluate the capability of DiVLA in an industrial setting, where a robot is tasked with sorting items into designated sectors within a large box ...
- **p. 7 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** Scaling Robot Foundation Models via Unified Diffusion and Autoregression Furthermore, both seen and unseen objects are mixed in these scenarios.
- **p. 5 / 4. Experiments - extractive PDF cue:** In Section 4.3, we evaluate DiVLA in the challenging factory sorting task, showcasing its remarkable performance and illustrating how reasoning enables the model to analyze ...
- **p. 5 / 4. Experiments - extractive PDF cue:** In Section 4.5, we showcase DiVLA's impressive generalization abilities in a zero-shot bin-picking task involving over 102 unseen objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success ... | p. 5 (Figure/Table caption) |
| 4.6. Adapt to Real-World Bimanual Robot | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, the Diffusion Policy and OpenVLA achieve 45.8% and 0% success rates. | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| 4.6. Adapt to Real-World Bimanual Robot | EMPIRICAL / REAL-ROBOT OR HARDWARE | For tasks involving both seen and unseen objects, DiVLA achieves up to a 70.8% success rate, a slight decrease in success rate compared to ... | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| 4.2. Real-World Multi-Task Learning | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our evaluation of these scenarios reveals that while all methods experience a decline in performance due to these visual changes, our method consistently maintains ... | p. 6 (4.2. Real-World Multi-Task Learning) |
| 4.3. End-to-End Sorting on Real Robot | EMPIRICAL / REAL-ROBOT OR HARDWARE | DiVLA demonstrates robust performance with an average success rate of 66.2% across all experimental settings. | p. 7 (4.3. End-to-End Sorting on Real Robot) |

## Dataset / Benchmark Role

- **p. 8 / 4.5. Zero-Shot Bin Picking of Unseen Objects - extractive PDF cue:** (c) Seen Tableware (d) Unseen Tableware (a) Bimanual Robot Setup (b) Setup for Table Bussing (e) Seen Trash (f) Unseen Trash Figure 9: (a) Environmental ...
- **p. 7 / 4.5. Zero-Shot Bin Picking of Unseen Objects - extractive PDF cue:** This section evaluates instance generalization for DiVLA, focusing specifically on the bin-picking task-a standard benchmark for assessing robot model performance.
- **p. 8 / 4.5. Zero-Shot Bin Picking of Unseen Objects - extractive PDF cue:** It highlights the potential for applications in dynamic, unstructured environments where robots encounter unfamiliar objects and must perform tasks with minimal human intervention.
- **p. 6 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** The task is considered successful only if the robot successfully grasps the object and places it in the correct sector.
- **p. 6 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** We evaluate the capability of DiVLA in an industrial setting, where a robot is tasked with sorting items into designated sectors within a large box ...
- **p. 7 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** Scaling Robot Foundation Models via Unified Diffusion and Autoregression Furthermore, both seen and unseen objects are mixed in these scenarios.
- **p. 5 / 4. Experiments - extractive PDF cue:** In Section 4.3, we evaluate DiVLA in the challenging factory sorting task, showcasing its remarkable performance and illustrating how reasoning enables the model to analyze ...
- **p. 5 / 4. Experiments - extractive PDF cue:** In Section 4.5, we showcase DiVLA's impressive generalization abilities in a zero-shot bin-picking task involving over 102 unseen objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Our proposed DiffusionVLA model unifies autoregressive and diffusion modeling to enable self-reasoning and robot policy learning. This approach generalizes effectively to visual changes, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Environmental Setup for the Franka Robot and Experimental Configuration for Factory Sorting. Left: For factor sorting tasks, (a) The target sorting box is ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Experimental Results for Multi-Task Learning on Real Robot. We report the count of pre-trained trajectories. We also report the average success rate for ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success rate, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Zero-shot Bin Picking on 102 Unseen Objects. Our method outperforms the state-of-the-art robot foundation models by a large margin.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5: Examples of visual variations, including randomly placed distractors, different backgrounds, and distracting lighting. Di- VLA is robust to visual changes in different scenarios.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6: What internal processes guide a model's actions? We illustrate this using an example of DiVLA's reasoning, inferred from shifts in its behavior based ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7: Some of the unseen objects used for evaluation in the zero-shot bin-picking tasks. illustrated in Figure 6, the model might initially identify a ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (c) Seen Tableware (d) Unseen Tableware (a) Bimanual Robot Setup (b) Setup for Table Bussing (e) Seen Trash (f) Unseen Trash Figure 9: (a) ... | embodiment, simulator version and control stack | p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 7 (4.5. Zero-Shot Bin Picking of Unseen Objects) |
| Task/environment | This section evaluates instance generalization for DiVLA, focusing specifically on the bin-picking task-a standard benchmark for assessing robot model performance. | reset, timeout, object/scene variation | p. 7 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3.2. Model Design Choices), p. 5 (3.1. Architecture) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3. Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our evaluation of these scenarios reveals that while all methods experience a decline in performance due to these visual changes, our method consistently maintains ... | definition/direction/unit from same section | p. 6 (4.2. Real-World Multi-Task Learning) |
| DiVLA demonstrates robust performance with an average success rate of 66.2% across all experimental settings. | definition/direction/unit from same section | p. 7 (4.3. End-to-End Sorting on Real Robot) |
| While other methods show significant performance degradation as scene complexity increases (i.e., higher object count and clutter level), particularly evident in DP's sharp decline ... | definition/direction/unit from same section | p. 7 (4.3. End-to-End Sorting on Real Robot) |
| The success rate is computed by how many objects are correctly placed. | definition/direction/unit from same section | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| In contrast, the Diffusion Policy and OpenVLA achieve 45.8% and 0% success rates. | definition/direction/unit from same section | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| Table 1: Experimental Results for Multi-Task Learning on Real Robot. We report the count of pre-trained trajectories. We also report the average success rate ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 6: Experimental results for view shifting generalization. We conduct view shifting generalization on factory sorting task. The experimental setup is shown in Figure ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms the state-of-the-art robot foundation models by a large margin. | comparison identity and matched condition | p. 6 (4. Experiments) |
| Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| In Section 4.2, we compare DiVLA against other state-of-the-art models within a standard multi-task setting, assessing its performance in both in-distribution and out-of-distribution scenarios. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Deep learning has demonstrated superior performance and generalization capabilities compared to traditional methods. | comparison identity and matched condition | p. 7 (4.4. Behavior Analysis of Robot Foundation Model) |
| Our method significantly outperforms both Diffusion Policy and OpenVLA by a large margin. | comparison identity and matched condition | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| For tasks involving both seen and unseen objects, DiVLA achieves up to a 70.8% success rate, a slight decrease in success rate compared to ... | comparison identity and matched condition | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 8: Ablation study on reasoning injection module. In-Distribution Model \ Tasks Task 1 Task 2 Task 3 Task 4 Task 5 | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Table 7: Ablation study on OpenVLA using one camera view and three camera views. For a fair comparison, our main experi- ments evaluate OpenVLA ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| We apply LoRA on VLM for fine-tuning. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| We use LoRA (Hu et al., 2021) to fine-tune the VLM models. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| Figure 10: Multi-task Learning and Visual Generalization. We evaluate each method on multi-task learning and visual generalizations, including adding additional distractors, changing the background, ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we introduce the overall framework of our method in Section 3.1 and explore the design choices that inform our model architecture ... | Figure 3: Experimental Results for Factory Sorting. We compared our DiVLA with Diffusion Policy, Octo, TinyVLA, and OpenVLA. DiVLA achieves the highest average success ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 6 (4.2. Real-World Multi-Task Learning), p. 7 (4.3. End-to-End Sorting on Real Robot), p. 7 (4.3. End-to-End Sorting on Real Robot) |
| Primary metric/result | In contrast, the Diffusion Policy and OpenVLA achieve 45.8% and 0% success rates. | numeric claim only at cited anchor | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Our dataset includes 500 trajectories for the factory sorting task and 580 trajectories for multi-task learning.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** For the table bussing task, we gathered 400 trajectories, where objects are randomly placed on the table, often overlapping with each other.
- **p. 6 / 4.3. End-to-End Sorting on Real Robot - extractive PDF cue:** A total of 500 trajectories are collected as training data.
- **p. 8 / 4.6. Adapt to Real-World Bimanual Robot - extractive PDF cue:** Scenarios Diffusion Policy OpenVLA DiVLA-2B Seen 45.8 0 72.9 Mixed 31.2 0 70.8 objects.
- **p. 4 / 3.1. Architecture - extractive PDF cue:** Pre-trained In-Distribution Visual Generalization Model \ Tasks Trajectory Task 1 Task 2 Task 3 Task 4 Task 5 Avg.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Failure case analysis via self-generated reasoning. | p. 7 (4.4. Behavior Analysis of Robot Foundation Model) |
| body limitation/failure cue | Additionally, we show that DiVLA has robust generalization capabilities, adapting effectively to new instructions, tasks, and environments. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Table 1: Experimental Results for Multi-Task Learning on Real Robot. We report the count of pre-trained trajectories. We also report the average success rate ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | In Section 4.2, we compare DiVLA against other state-of-the-art models within a standard multi-task setting, assessing its performance in both in-distribution and out-of-distribution scenarios. | p. 5 (4. Experiments) |
| body limitation/failure cue | DiVLA is robust to visual changes in different scenarios. | p. 6 (4. Experiments) |
| body limitation/failure cue | We further evaluate our method in a multi-task setting with visual changes to assess its robustness and adaptability in diverse, dynamic environments. | p. 6 (4.2. Real-World Multi-Task Learning) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use 2e-5 as a fixed learning rate to train the model, similar to OpenVLA. | p. 6 (4.1. Experimental Setup) |
| We provide experimental setup and implementation details in the Appendix. | p. 5 (4. Experiments) |
| The visual encoder and VLM are frozen. | p. 6 (4.1. Experimental Setup) |
| The success rate is computed by how many objects are correctly placed. | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| Our evaluation consisted of twelve trials, with three to five objects randomly placed on the table. | p. 8 (4.6. Adapt to Real-World Bimanual Robot) |
| Given any sequence of interleaved images, text, and video, we first encode the images into dense visual features using SigLIP (Zhai et al., 2023). | p. 3 (3.1. Architecture) |
| We initialized the VLM backbone with the publicly released checkpoint. | p. 4 (3.1. Architecture) |
| An MLP layer is attached to the last layer at the bottom of the action decoder to predict the robot's joint space. | p. 4 (3.1. Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.4. Behavior Analysis of Robot Foundation Model - extractive PDF cue:** Failure case analysis via self-generated reasoning.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Additionally, we show that DiVLA has robust generalization capabilities, adapting effectively to new instructions, tasks, and environments.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Experimental Results for Multi-Task Learning on Real Robot. We report the count of pre-trained trajectories. We also report the average success rate for ...
- **p. 5 / 4. Experiments - extractive PDF cue:** In Section 4.2, we compare DiVLA against other state-of-the-art models within a standard multi-task setting, assessing its performance in both in-distribution and out-of-distribution scenarios.
- **p. 6 / 4. Experiments - extractive PDF cue:** DiVLA is robust to visual changes in different scenarios.
- **p. 6 / 4.2. Real-World Multi-Task Learning - extractive PDF cue:** We further evaluate our method in a multi-task setting with visual changes to assess its robustness and adaptability in diverse, dynamic environments.

- **PDF anchors reviewed:** datasets p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 7 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 8 (4.5. Zero-Shot Bin Picking of Unseen Objects), p. 6 (4.3. End-to-End Sorting on Real Robot), p. 6 (4.3. End-to-End Sorting on Real Robot), p. 7 (4.3. End-to-End Sorting on Real Robot), metrics p. 6 (4.2. Real-World Multi-Task Learning), p. 7 (4.3. End-to-End Sorting on Real Robot), p. 7 (4.3. End-to-End Sorting on Real Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 4 (Figure/Table caption), baselines p. 6 (4. Experiments), p. 5 (Figure/Table caption), p. 5 (4. Experiments), p. 7 (4.4. Behavior Analysis of Robot Foundation Model), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot), results p. 5 (Figure/Table caption), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 8 (4.6. Adapt to Real-World Bimanual Robot), p. 6 (4.2. Real-World Multi-Task Learning), p. 7 (4.3. End-to-End Sorting on Real Robot), p. 7 (4.3. End-to-End Sorting on Real Robot).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
