# Evaluation - Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WXFfMLyB6y; PDF retrieval source: https://openreview.net/pdf/c917563473da6d5f8455d72ba42222b9722824de.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption)): Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training settings. state-of-the-art method (Li et ...

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** A dataset containing 100 demonstrations per task along with a task description per trajectory is prepared for training.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** 5.2 REAL-WORLD EXPERIMENTS Experimental Setting We keep the training settings the same as in the simulation and list key modifications here.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** A comparison between Exp ID 4 and ours can further validate the performance gain from adding the object position dataset.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** 1) Base In the base version (corresponding to Exp ID 1), the coarse task planner is trained with only the robot trajectories to predict step ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Figure 3: Overview of the tasks in real-world experiments.
- **p. 18 / A.6 REAL-WORLD EXPERIMENTS - extractive PDF cue:** We evaluate the all these eight tasks acroos different variations and record the success rate.
- **p. 19 / A.6 REAL-WORLD EXPERIMENTS - extractive PDF cue:** We compare the results of training our method with different numbers of demonstrations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); A.3 EXPERIMENTAL DETAILS (p. 16); A.6 REAL-WORLD EXPERIMENTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different ... | p. 8 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves an overall success rate 12% higher than prior 7 | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | CLAP achieves 54.8% higher average success rates compared to RVT2 on the evaluation tasks. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Main Results The evaluation results on GemBench are summarized in Table 1, reporting the average success rate for tasks at each generalization level. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP place shape in shape sorter 60% 60% 35% 50% 30% 40% 20% 50% 36.2% ... | p. 9 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** A dataset containing 100 demonstrations per task along with a task description per trajectory is prepared for training.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** 5.2 REAL-WORLD EXPERIMENTS Experimental Setting We keep the training settings the same as in the simulation and list key modifications here.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** A comparison between Exp ID 4 and ours can further validate the performance gain from adding the object position dataset.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** 1) Base In the base version (corresponding to Exp ID 1), the coarse task planner is trained with only the robot trajectories to predict step ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Figure 3: Overview of the tasks in real-world experiments.
- **p. 18 / A.6 REAL-WORLD EXPERIMENTS - extractive PDF cue:** We evaluate the all these eight tasks acroos different variations and record the success rate.
- **p. 19 / A.6 REAL-WORLD EXPERIMENTS - extractive PDF cue:** We compare the results of training our method with different numbers of demonstrations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Intuition of CLAP. Our method achieves strong generalization ability by decomposing tasks into step-wise language instructions, each aligned with a 3D keypoint. reasoning, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of CLAP. We propose a novel coarse-to-fine 3D manipulation policy, compris- ing of a coarse task planner and a fine-grained action predictor. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Multi-Task Performance on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench. Except CLAP, we use the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of the tasks in real-world experiments. There are four training tasks: put shape in shape sorter, put block in cup, open drawer, ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Real-world Performance. Here are the average success rate under different generalization settings for real-world experiments. 5.2 REAL-WORLD EXPERIMENTS Experimental Setting We keep the ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3. Our method achieves a strong generalization ability to novel tasks and object variations, trained with only 10 demonstrations per task. CLAP achieves 54.8% ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 4: Number of samples. We record the number of samples in training set and validation set for different datasets used in the simulation experiments ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories. | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Task/environment | A dataset containing 100 demonstrations per task along with a task description per trajectory is prepared for training. | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 5 (4 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (4 METHOD), p. 4 (3 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP place shape in shape sorter 60% 60% 35% 50% 30% 40% 20% 50% 36.2% ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Our method achieves an overall success rate 12% higher than prior 7 | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| The detailed success rate for each task are recorded in Appendix A.4. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Here are the average success rates of 4 levels of evaluation tasks from Gembench. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| CLAP achieves 54.8% higher average success rates compared to RVT2 on the evaluation tasks. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| We evaluate the all these eight tasks acroos different variations and record the success rate. | definition/direction/unit from same section | p. 18 (A.6 REAL-WORLD EXPERIMENTS) |
| Table 7: Per-task Success Rate on GemBench Level 1. | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Success ↑ L1 L2 L3 L4 HiveFormer (Guhur et al., 2023) 30.4 60.3 ± 1.5 26.1 ± 1.4 35.1 ± 1.7 0.0 ± 0.0 ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We use this version as a baseline to ablate our method. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| CLAP achieves 54.8% higher average success rates compared to RVT2 on the evaluation tasks. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Number of Demos L1 L2 L3 L4 Average 10 84.5 ± 0.8 81.5 ± 0.6 43.3 ± 1.9 30.5 ± 2.1 60.0 ± 0.1 ... | comparison identity and matched condition | p. 19 (A.6 REAL-WORLD EXPERIMENTS) |
| Table 12: Ablation on inputs to Fine-grained Action Predictor. We compare the results of re- moving some inputs to our fine-grained action predictor. The ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| A specific ablation on the inputs of the fine-grained action predictor is include in Appendix A.5. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Number of Demos L1 L2 L3 L4 Average 10 84.5 ± 0.8 81.5 ± 0.6 43.3 ± 1.9 30.5 ± 2.1 60.0 ± 0.1 ... | component/input/data sensitivity | p. 19 (A.6 REAL-WORLD EXPERIMENTS) |
| Table 12: Ablation on inputs to Fine-grained Action Predictor. We compare the results of re- moving some inputs to our fine-grained action predictor. The ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Using all observations around the key-frames to fine-tune the VLM risks confusing it. | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories. | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task. | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption) |
| Primary metric/result | Our method achieves an overall success rate 12% higher than prior 7 | numeric claim only at cited anchor | p. 7 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** This training set contains 16 tasks with 31 variations.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Instead of evaluating on in-distribution tasks and variations, GemBench designs an evaluation set containing 4 levels of tasks, where different elements are varied: - Placements ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Following the evaluation setting in GemBench (Garcia et al., 2025), all trained models are evaluated with 20 episodes per task variation per seed, and 5 ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Apart from key-frame pairs of observation and action (otk, atk+1), RVT2 augments the training data by sampling observations every n frames (e.g., every 10 frames).
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** The experimental results demonstrate the strong generalization ability of our method to novel tasks and object variations, as indicated by the performance gain on Level2, ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Success ↑ L1 L2 L3 L4 HiveFormer (Guhur et al., 2023) 30.4 60.3 ± 1.5 26.1 ± 1.4 35.1 ± 1.7 0.0 ± 0.0 PolarNet ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate. | p. 16 (A.5 ADDITIONAL ABLATION STUDY) |
| body limitation/failure cue | Furthermore, our design leads to substantial performance gain on the most challenging Level-4 tasks, where several baselines methods fail consistently. | p. 8 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The hyperparameters, such as batch size and learning rate used in training are listed in Appendix A.3. | p. 7 (5 EXPERIMENTS) |
| The hyperparameters and training time are listed in Table 6. | p. 16 (A.3 EXPERIMENTAL DETAILS) |
| Finally, we choose to use observations (otk, ...otk+m) at the time steps immediately following each key-frame. | p. 7 (5 EXPERIMENTS) |
| ID Data Data Step Plan Objects Encoder 1 2 3 4 Succ. | p. 8 (5 EXPERIMENTS) |
| 5) CLAP w/o Pre-trained Encoder An ablation study (comparing Exp ID 5 and Exp ID 6) on the coarse planner confirms that incorporating the ... | p. 8 (5 EXPERIMENTS) |
| All experiments are conducted on 4 NVIDIA RTX 4090 GPU. | p. 16 (A.3 EXPERIMENTAL DETAILS) |
| The results are recorded with three runs of different random seeds. | p. 19 (A.6 REAL-WORLD EXPERIMENTS) |
| Considering the significant domain shift between the images focused around predicted ptk from those used to pretrain standard VLMs, we decide to employ instead ... | p. 6 (4 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / A.5 ADDITIONAL ABLATION STUDY - extractive PDF cue:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Furthermore, our design leads to substantial performance gain on the most challenging Level-4 tasks, where several baselines methods fail consistently.

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), metrics p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 18 (A.6 REAL-WORLD EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 19 (A.6 REAL-WORLD EXPERIMENTS), p. 19 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
