# Evaluation - LLaRA: Supercharging Robot Learning Data for Vision-Language Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (47 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=iVxxgZlXh6; PDF retrieval source: https://openreview.net/pdf/88e833c98e7c9f665ef182cf0d30f65c58655784.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 17 (A.1.2 BUILD D-inBC FROM inBC), p. 10 (Figure/Table caption)): Figure 5: Success rates of the models trained on VIMA subsets. The log-scale x-axis shows the number of expert episodes used in the training set. See Appendix E for the ...

## Evaluation Body Digest

- **p. 7 / 6 EXPERIMENTS - extractive PDF cue:** We employ VIMA-Bench (Jiang et al., 2023), a simulated table-top robot manipulation environment to evaluate VLMs trained by our instruction tuning dataset.
- **p. 6 / 6 EXPERIMENTS - extractive PDF cue:** Then, we conduct real-world robot experiments using three protocols: zero-shot generalization, finetuning, and joint training.
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** All tasks occur in an environment where a robot arm, equipped with either a spatula or a suction cup, is positioned alongside a flat table.
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** Each episode in the dataset features a multimodal task description that clarifies the episode's goal, incorporating images referred to as ‘reference images'.
- **p. 7 / 6 EXPERIMENTS - extractive PDF cue:** The environment contains 17 tasks and each task is associated with a multi-modal instruction, including text instructions and reference images that refer to objects of ...
- **p. 8 / 6 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 episodes to avoid overwhelming the primary learning objectives.
- **p. 8 / 6 EXPERIMENTS - extractive PDF cue:** The ‘*' after a ‘✓' means the reference images that appeared only in the task description are not used to generate this dataset, which makes ...
- **p. 16 / A.1 DATASET PREPARATION - extractive PDF cue:** In this subsection, we give more details and examples of the datasets used in this paper.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 6 EXPERIMENTS (p. 6); A IMPLEMENTATION DETAILS (p. 16); A.1 DATASET PREPARATION (p. 16); A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES (p. 16); A.1.4 AUXILIARY DATASETS (p. 18); B EXPANDED SIMULATION EXPERIMENTS (p. 21); B.1 CLARIFICATION ON L4 RESULTS (p. 21); B.8 EXTENDED EXPERIMENTS ON RT-2 Style VARIANTS (p. 26); B.10 FEW-SHOT EXPERIMENTS USING LLM / VLM (p. 27); C DETAILS ON REAL-WORLD ROBOT EXPERIMENTS (p. 28); C.3 REAL-WORLD ROBOT DATASET (p. 28); C.4 EXTENDED REAL-WORLD EXPERIMENTS (p. 30).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Success rates of the models trained on VIMA subsets. The log-scale x-axis shows the number of expert episodes used in the training ... | p. 7 (Figure/Table caption) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Methods based on RT-2 Style improve when more robot supervision data is available; however, they significantly underperform compared to our methods when data is ... | p. 7 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our best model not only achieves better performance but also requires less input and is trained on only 12% of the expert trajectories used ... | p. 8 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1× 2× 3× 4× 5× 6× 7× Total dataset size relative to inBC 25 30 35 40 L1 Success Rate (%) 1× 2× 3× ... | p. 8 (6 EXPERIMENTS) |
| A.1.2 BUILD D-inBC FROM inBC | EMPIRICAL / REAL-ROBOT OR HARDWARE | In general, D-inBC (L) achieves comparable but slightly worse performance than D-inBC, which uses structured text to describe the reference images. | p. 17 (A.1.2 BUILD D-inBC FROM inBC) |

## Dataset / Benchmark Role

- **p. 7 / 6 EXPERIMENTS - extractive PDF cue:** We employ VIMA-Bench (Jiang et al., 2023), a simulated table-top robot manipulation environment to evaluate VLMs trained by our instruction tuning dataset.
- **p. 6 / 6 EXPERIMENTS - extractive PDF cue:** Then, we conduct real-world robot experiments using three protocols: zero-shot generalization, finetuning, and joint training.
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** All tasks occur in an environment where a robot arm, equipped with either a spatula or a suction cup, is positioned alongside a flat table.
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** Each episode in the dataset features a multimodal task description that clarifies the episode's goal, incorporating images referred to as ‘reference images'.
- **p. 7 / 6 EXPERIMENTS - extractive PDF cue:** The environment contains 17 tasks and each task is associated with a multi-modal instruction, including text instructions and reference images that refer to objects of ...
- **p. 8 / 6 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 episodes to avoid overwhelming the primary learning objectives.
- **p. 8 / 6 EXPERIMENTS - extractive PDF cue:** The ‘*' after a ‘✓' means the reference images that appeared only in the task description are not used to generate this dataset, which makes ...
- **p. 16 / A.1 DATASET PREPARATION - extractive PDF cue:** In this subsection, we give more details and examples of the datasets used in this paper.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: A real-world demonstration of LLaRA solving an unseen task. In this setting, LLaRA converts only eight thousand simulated expert trajectories from VIMA (Jiang ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: LLaVA overview. A Large Language Model (LLM) is connected to the visual domain with suitable encoder and adap- tor neural networks. Consider a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Example data for visuomotor instruction tuning. (left) inBC is our instruction tuning data created from BC, only taking textual task description. (right) D-inBC ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Auxiliary datasets for visuomotor instruction tuning. Given an input trajectory, we make use of expert information (e.g., object detections) to formulate conversations related ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Success rates of the models trained on VIMA subsets. The log-scale x-axis shows the number of expert episodes used in the training set. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison to VIMA (Jiang et al., 2023). Our best model not only achieves better performance but also requires less input and is trained ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: inBC (top) and D-inBC (bottom) with different auxiliary dataset settings. Each model is trained on VIMA-0.8k for 2 epochs. In general, the model ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Naming of different auxiliary dataset configurations. We always randomly sample the same amount of examples from each dataset. Det.: detection; Loc.: localization; Act.: ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We employ VIMA-Bench (Jiang et al., 2023), a simulated table-top robot manipulation environment to evaluate VLMs trained by our instruction tuning dataset. | embodiment, simulator version and control stack | p. 7 (6 EXPERIMENTS), p. 6 (6 EXPERIMENTS) |
| Task/environment | Then, we conduct real-world robot experiments using three protocols: zero-shot generalization, finetuning, and joint training. | reset, timeout, object/scene variation | p. 6 (6 EXPERIMENTS), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 2 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For each task, we evaluate all the methods with 20 random seeds and report the average success rates of each level and the average ... | definition/direction/unit from same section | p. 7 (6 EXPERIMENTS) |
| 8 × 102 8 × 103 8 × 104 8 × 105 Num of expert episodes 0 10 20 30 40 50 60 70 ... | definition/direction/unit from same section | p. 7 (6 EXPERIMENTS) |
| 1× 2× 3× 4× 5× 6× 7× Total dataset size relative to inBC 25 30 35 40 L1 Success Rate (%) 1× 2× 3× ... | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| Our best model not only achieves better performance but also requires less input and is trained on only 12% of the expert trajectories used ... | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| In action generation, the dataset is prepared such that the VLM is designed to generate all successive actions in the response, literally performing multi-step ... | definition/direction/unit from same section | p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES) |
| Figure 1: A real-world demonstration of LLaRA solving an unseen task. In this setting, LLaRA converts only eight thousand simulated expert trajectories from VIMA ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2: LLaVA overview. A Large Language Model (LLM) is connected to the visual domain with suitable encoder and adap- tor neural networks. Consider ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 8: Visual reference for the initial image (top row) and successful end positions (bottom row) in three real-world tasks. We also show some ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Key observations include: • inBC consistently surpasses the RT-2 Style baseline, and similarly, D-inBC outperforms D-RT-2 Style. | comparison identity and matched condition | p. 7 (6 EXPERIMENTS) |
| Method Config Data L1 (%) L2 (%) L3 (%) VIMA VIMA-200M + Oracle 100% 80.7 81.9 77.9 LLaRA (Ours) D-inBC + Aux (B) + ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| Oracle means that the groundtruth bounding box of objects is used as the object detection results only in the reference images. | comparison identity and matched condition | p. 7 (6 EXPERIMENTS) |
| Compared to VIMA, our best model not only achieves better performance but also requires less input and is trained on only 12% of the ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| Table 8: Comparison between our converted instruction tuning datasets inBC and D-inBC for a VIMA-Bench sample. The task description of the episode is in ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| Table 9: Another comparison between two converted instruction tuning datasets. In this example, the reference images in the task description depict reference images with ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 13: Effect of prompt sentence for action generation. B.8 EXTENDED EXPERIMENTS ON RT-2 Style VARIANTS As suggested by the reviewer, we evaluate two ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| A.1.3 D-inBC (L): DESCRIBING THE REFERENCE IMAGES IN NATURAL LANGUAGE Following the suggestion from the reviewer, we trained a variant of D-inBC, which completely ... | component/input/data sensitivity | p. 17 (A.1.2 BUILD D-inBC FROM inBC) |
| We compare variants of our method with baselines that follow the recipe of RT-2 (Brohan et al., 2023a), RT-2 Style, and D-RT-2 Style. | component/input/data sensitivity | p. 7 (6 EXPERIMENTS) |
| These textual descriptions replaced the original lists of image coordinates in the input prompt for the D-inBC setting, resulting in a variant we refer ... | component/input/data sensitivity | p. 17 (A.1.2 BUILD D-inBC FROM inBC) |
| Figure 11: Model performances on VIMA-80k for longer epochs. B.4 ABLATION ON ACTION HISTORY AND MULTI-STEP PLANNING As described in Appendix A.1.1, we enable ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 15: Ablation on multiple image inputs (Mul.). All models are trained on VIMA-8k for 2 epochs. | component/input/data sensitivity | p. 25 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Such a formulation based on conversation-style instruction-response data enables us to convert a VLM into a robot action policy effortlessly. | Figure 5: Success rates of the models trained on VIMA subsets. The log-scale x-axis shows the number of expert episodes used in the training ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 17 (A.1.2 BUILD D-inBC FROM inBC), p. 10 (Figure/Table caption) |
| Primary metric/result | Methods based on RT-2 Style improve when more robot supervision data is available; however, they significantly underperform compared to our methods when data is ... | numeric claim only at cited anchor | p. 7 (6 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 6 EXPERIMENTS - extractive PDF cue:** The environment contains 17 tasks and each task is associated with a multi-modal instruction, including text instructions and reference images that refer to objects of ...
- **p. 8 / 6 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 episodes to avoid overwhelming the primary learning objectives.
- **p. 8 / 6 EXPERIMENTS - extractive PDF cue:** On VIMA-0.8k, we control the total number of samples from the auxiliary dataset relative to the samples from the converted BC datasets and train all ...
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** The full accompanying dataset includes 660k expert trajectories, covering 13 of the 17 tasks.
- **p. 21 / A.4 RT-2-STYLE BASELINES - extractive PDF cue:** So the action space is now 5 Degrees of Freedom (DoF): 4 numerical values present the 2D pick and place locations in robot coordinates, and ...
- **p. 17 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** The full accompanying dataset includes 660k expert trajectories, covering 13 of the 17 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 17: Robostness evaluation results of D-inBC + Aux (B) + Oracle (VIMA-80k, 8 epochs) Prob. of Failure L1 (%) L2 (%) L3 (%) ... | p. 27 (Figure/Table caption) |
| body limitation/failure cue | Given the current limitations of LLaVA (Liu et al., 2023a), to optimize performance, we propose two techniques: • Action history in query. | p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES) |
| body limitation/failure cue | 8 has shown its great power in many aspects when the reference image contains a scene that has multiple objects instead of one, the ... | p. 17 (A.1.2 BUILD D-inBC FROM inBC) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| However, for VIMA-0.8k and VIMA-8k, we employ a batch size of 32, whereas for VIMA-80k, we restore the batch size to 128. | p. 18 (A.2 TRAINING) |
| Specifically, we utilize a single-cycle cosine annealing scheduling with 0.03 warm-up ratio and a maximum learning rate of 2 × 10-5. | p. 18 (A.2 TRAINING) |
| For each task, we evaluate all the methods with 20 random seeds and report the average success rates of each level and the average ... | p. 7 (6 EXPERIMENTS) |
| On VIMA-0.8k, we control the total number of samples from the auxiliary dataset relative to the samples from the converted BC datasets and train ... | p. 8 (6 EXPERIMENTS) |
| In this section, we provide more implementation details regarding dataset preparation, model training, inference, and RT-2 style baselines. | p. 16 (A IMPLEMENTATION DETAILS) |
| In our implementation, the procedure begins by normalizing each element of the action to a range from 0 to 1. | p. 21 (A.4 RT-2-STYLE BASELINES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 27 / Figure/Table caption - extractive PDF cue:** Table 17: Robostness evaluation results of D-inBC + Aux (B) + Oracle (VIMA-80k, 8 epochs) Prob. of Failure L1 (%) L2 (%) L3 (%) 0 ...
- **p. 16 / A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES - extractive PDF cue:** Given the current limitations of LLaVA (Liu et al., 2023a), to optimize performance, we propose two techniques: • Action history in query.
- **p. 17 / A.1.2 BUILD D-inBC FROM inBC - extractive PDF cue:** 8 has shown its great power in many aspects when the reference image contains a scene that has multiple objects instead of one, the inBC ...

- **PDF anchors reviewed:** datasets p. 7 (6 EXPERIMENTS), p. 6 (6 EXPERIMENTS), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 17 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), metrics p. 7 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 16 (A.1.1 BUILD inBC DATASET FROM EXPERT TRAJECTORIES), p. 1 (Figure/Table caption), baselines p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 19 (Figure/Table caption), p. 20 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 7 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 17 (A.1.2 BUILD D-inBC FROM inBC), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
