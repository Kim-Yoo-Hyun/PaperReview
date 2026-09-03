# Evaluation - ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=1lyKflUOhp; PDF retrieval source: https://arxiv.org/pdf/2505.21906.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption)): In contrast, our method achieved an average success rate of 81.4%, representing a 3.52-times improvement over DexVLA.

## Evaluation Body Digest

- **p. 15 / B.2 Data details - extractive body cue:** Additionally, we gathered 5k samples from real-world environments, covering both tabletop setups and broader scenes.
- **p. 15 / B.2 Data details - extractive body cue:** The image-text dataset used in our experiments integrates samples from multiple established benchmarks, including COCO, TextVQA, and GQA, alongside additional data specifically constructed to align ...
- **p. 7 / 4 Experiments - extractive body cue:** We do not evaluate using simulation benchmarks, as the VLA capabilities demonstrated by our approach exceed what current simulation benchmarks can assess.
- **p. 7 / 4 Experiments - extractive body cue:** These experiments examine the model's proficiency in mathematical reasoning, spatial reasoning, optical character recognition (OCR), and object recognition and localization, most within an open-world context ...
- **p. 8 / 4 Experiments - extractive body cue:** Even ChatVLA, despite its multimodal understanding capability, fails these tasks when the robot control expert is activated.
- **p. 8 / 4 Experiments - extractive body cue:** We utilize a 7-Degree-of-Freedom Franka Emika robot equipped with a Robotiq gripper.
- **p. 9 / 4 Experiments - extractive body cue:** We hypothesize that this decline is due to conflicts in the parameter space between robotic actions and reasoning/understanding.
- **p. 9 / 4 Experiments - extractive body cue:** When Stage 2 was excluded, the model's robotic control performance in open-world scenarios dropped to 23% under the same number of training steps.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); B Implementation Details (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, our method achieved an average success rate of 81.4%, representing a 3.52-times improvement over DexVLA. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, ChatVLA-2 achieves meaningful performance: 3.58 in OCR accuracy, 1.73 in mathematical reasoning accuracy, and 82.7% manipulation success rate. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate average object recognition score, spatial affordance score and task success rate at both setups. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1) Manipulation success rate: We report the average success rate to measure whether the model completes the task or not. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We conducted experiments on the math matching game and observed a significant drop in the average success rate. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 15 / B.2 Data details - extractive body cue:** Additionally, we gathered 5k samples from real-world environments, covering both tabletop setups and broader scenes.
- **p. 15 / B.2 Data details - extractive body cue:** The image-text dataset used in our experiments integrates samples from multiple established benchmarks, including COCO, TextVQA, and GQA, alongside additional data specifically constructed to align ...
- **p. 7 / 4 Experiments - extractive body cue:** We do not evaluate using simulation benchmarks, as the VLA capabilities demonstrated by our approach exceed what current simulation benchmarks can assess.
- **p. 7 / 4 Experiments - extractive body cue:** These experiments examine the model's proficiency in mathematical reasoning, spatial reasoning, optical character recognition (OCR), and object recognition and localization, most within an open-world context ...
- **p. 8 / 4 Experiments - extractive body cue:** Even ChatVLA, despite its multimodal understanding capability, fails these tasks when the robot control expert is activated.
- **p. 8 / 4 Experiments - extractive body cue:** We utilize a 7-Degree-of-Freedom Franka Emika robot equipped with a Robotiq gripper.
- **p. 9 / 4 Experiments - extractive body cue:** We hypothesize that this decline is due to conflicts in the parameter space between robotic actions and reasoning/understanding.
- **p. 9 / 4 Experiments - extractive body cue:** When Stage 2 was excluded, the model's robotic control performance in open-world scenarios dropped to 23% under the same number of training steps.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our proposed ChatVLA-2 model enables generalized open-world embodied reasoning and reasoning following abilities. We designed two tasks-a math matching game and a toy ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Model architecture. Left: A reasoning-following enhancement module is incorporated to ensure that the VLA model adheres to logical reasoning when performing actions. Right: ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Training Strategy. We leverage a two-stage training strategy. In the first stage, we perform co-training on image-text data and robot data to empower ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Experimental setup for math matching game and toy placement. We use a Franka Emika robot equipped with a Robotiq gripper to pick and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results on the math matching game. We evaluate multiple models on both in-domain settings, where the data is presented in the training data, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Results on the toy placement task. We evaluate multiple models on both in-domain settings, where the data is presented in the training data, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation on mixture-of-expert.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Ablation on training strategy. Stage 1 Stage 2 Math Matching Game OCR Math Avg. ✓

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Additionally, we gathered 5k samples from real-world environments, covering both tabletop setups and broader scenes. | embodiment, simulator version and control stack | p. 15 (B.2 Data details), p. 15 (B.2 Data details) |
| Task/environment | The image-text dataset used in our experiments integrates samples from multiple established benchmarks, including COCO, TextVQA, and GQA, alongside additional data specifically constructed to ... | reset, timeout, object/scene variation | p. 15 (B.2 Data details), p. 7 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 6 (3 Methodology), p. 6 (3 Methodology) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 Methodology), p. 5 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In contrast, ChatVLA-2 achieves meaningful performance: 3.58 in OCR accuracy, 1.73 in mathematical reasoning accuracy, and 82.7% manipulation success rate. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We evaluate average score of OCR (4 scores in total) and mathematical reasoning (2 scores in total), and average success rate of task execution ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We evaluate average object recognition score, spatial affordance score and task success rate at both setups. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 1) Manipulation success rate: We report the average success rate to measure whether the model completes the task or not. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We conducted experiments on the math matching game and observed a significant drop in the average success rate. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 3: Training Strategy. We leverage a two-stage training strategy. In the first stage, we perform co-training on image-text data and robot data to ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We first examine the in-domain performance. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Figure 2: Model architecture. Left: A reasoning-following enhancement module is incorporated to ensure that the VLA model adheres to logical reasoning when performing actions. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare our method against several state-of-the-art models, including Octo [70], Diffusion Policy [32], OpenVLA [10], GR00T N1 [66], DexVLA [2], ChatVLA [7], and ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Consequently, none of the compared methods successfully completed any manipulation tasks in open-world conditions. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Similarly, in manipulation tasks, ChatVLA-2 does not significantly outperform models like π0 and DexVLA, which already exhibit near-perfect performance. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Specifically, using the exact same training configuration, we compare the baseline models that do not incorporate MoE. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Ablation study on two-stage training. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Table 6: Ablation study on reasoning-following enhancement module. | comparison identity and matched condition | p. 15 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on two-stage training. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Dynamic MoE 3.58 1.73 43/52 Static MoE + Dynamic MoE 2.38/4 0.92/2 11/52 Shared MoE + Dynamic MoE 3.07/4 1.12/2 25/52 3B Dense Model ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Figure 3: Training Strategy. We leverage a two-stage training strategy. In the first stage, we perform co-training on image-text data and robot data to ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 6: Ablation study on reasoning-following enhancement module. | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Table 5: Ablation study on number of experts. Expert numbers Top-k numbers OCR Math 8 2 3.58 | component/input/data sensitivity | p. 15 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To achieve this, we propose a novel VLA model architecture employing a dynamic mixture-ofexperts within the VLM backbone. | In contrast, our method achieved an average success rate of 81.4%, representing a 3.52-times improvement over DexVLA. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption) |
| Primary metric/result | In contrast, ChatVLA-2 achieves meaningful performance: 3.58 in OCR accuracy, 1.73 in mathematical reasoning accuracy, and 82.7% manipulation success rate. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** 2) OCR: For OCR, we assign 1 point for correctly recognizing hand-written numbers, 1 point for identifying card values and their positions and 2 points ...
- **p. 7 / 4 Experiments - extractive body cue:** 3) Mathematical reasoning: For mathematical reasoning, we assign 1 point for a correct answer and 1 point for correctly selecting the card.
- **p. 7 / 4 Experiments - extractive body cue:** We utilize the bimanual, ALOHA-style robot arm system, ARX-R5, featuring two arms, each with 6 degrees of freedom (6-DoF) and equipped with a top RealSense ...
- **p. 7 / 4 Experiments - extractive body cue:** Data collection is performed through teleoperation equipment at a frequency of 50 Hz.
- **p. 8 / 4 Experiments - extractive body cue:** Data collection is performed using teleoperation equipment at a frequency of 15 Hz.
- **p. 15 / B.1 Training details - extractive body cue:** The total training cost is 340 GPU hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Upon investigating the cause of the failure, we discovered that for unseen mathematical equations, both dense models fail completely. | p. 9 (4 Experiments) |
| body limitation/failure cue | Even ChatVLA, despite its multimodal understanding capability, fails these tasks when the robot control expert is activated. | p. 8 (4 Experiments) |
| body limitation/failure cue | Similarly, in manipulation tasks, ChatVLA-2 does not significantly outperform models like π0 and DexVLA, which already exhibit near-perfect performance. | p. 8 (4 Experiments) |
| body limitation/failure cue | Furthermore, we find that increasing the number of parameters to 7B does not alleviate these conflicts. | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is trained for 50k steps, starting with a learning rate of 2e-5 and a warm-up phase over the first 3k steps. | p. 15 (B.1 Training details) |
| For training stage 1, we co-train on image-text data and robot data, setting the initial learning rate to 2e-5 and training for 15k steps. | p. 15 (B.1 Training details) |
| When Stage 2 was excluded, the model's robotic control performance in open-world scenarios dropped to 23% under the same number of training steps. | p. 9 (4 Experiments) |
| Subsequently, we apply a cosine learning rate scheduler, scaling down the learning rate to 2e-6. | p. 6 (3 Methodology) |
| The image encoders project the robot's visual observations into the same embedding space as the language tokens. | p. 4 (3 Methodology) |
| On the board is 18+16=34… Pick 34 from right 1 Step Math Matching Game Franka Setup Toy Placement Instruction: Pick the [obj] and place ... | p. 7 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** Upon investigating the cause of the failure, we discovered that for unseen mathematical equations, both dense models fail completely.
- **p. 8 / 4 Experiments - extractive body cue:** Even ChatVLA, despite its multimodal understanding capability, fails these tasks when the robot control expert is activated.
- **p. 8 / 4 Experiments - extractive body cue:** Similarly, in manipulation tasks, ChatVLA-2 does not significantly outperform models like π0 and DexVLA, which already exhibit near-perfect performance.
- **p. 9 / 4 Experiments - extractive body cue:** Furthermore, we find that increasing the number of parameters to 7B does not alleviate these conflicts.

- **Evidence anchors reviewed:** datasets p. 15 (B.2 Data details), p. 15 (B.2 Data details), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), metrics p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 15 (Figure/Table caption), results p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
