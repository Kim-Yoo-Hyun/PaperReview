# Evaluation - Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=8xTDnj39Ti; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247589. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 3 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS)): This suggests that pretraining with diverse in-domain multimodal data, spanning general QA, grounding, and spatial intelligence, could best facilitates transfer learning for VLA policy learning and leads to improved task ...

## Evaluation Body Digest

- **p. 8 / 3 EXPERIMENTS - extractive body cue:** SimplerENV is an open-source suite of purpose-built simulated environments with nearly 150K episodes for evaluating real-world robot manipulation policies in a scalable, reproducible way.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Robotwin is a scalable framework for bimanual manipulation, which integrates scalable training sets and pre-defined tasks as benchmarks for comprehensive robust bimanual manipulation.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** 3.1 PERFORMANCE ON EMBODIED REASONING CAPABILITY Evaluation Datasets We conduct a comprehensive evaluation of embodied reasoning capabilities across a total of 12 benchmarks, covering a ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.2 PERFORMANCE ON DOWNSTREAM CLOSE-LOOP ROBOT TASKS Finetuning Datasets We firstly conduct extensive experiments on SimplerENV (Li et al., 2024d) to evaluate the performance of ...
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** Therefore, it is urgent to shrink the domain gap between the foundational models and real-world robot embodiment for closed-loop task completion.
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** This observation illustrates the effectiveness of our Vlaser data engine, and meanwhile identifies that there is no positive correlation between common embodied reasoning benchmarks and ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** An interesting observation emerges that when finetuning on the same Vlaser-6M dataset, a smaller sized Vlaser-2B outperforms Vlaser-8B on simple point grounding tasks that require ...
- **p. 22 / A.3 SIMULATION EVALUATION DETAILS - extractive body cue:** To ensure fair evaluation, we use checkpoints with the same number of iterations for the WidowX Robot Task and the Google Robot Task, respectively.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3 EXPERIMENTS (p. 6); A.3 SIMULATION EVALUATION DETAILS (p. 22).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This suggests that pretraining with diverse in-domain multimodal data, spanning general QA, grounding, and spatial intelligence, could best facilitates transfer learning for VLA policy ... | p. 9 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | When compared against current state-of-the-art embodied-specific VLMs, including RoboBrain2.0 (Team et al., 2025a) and Embodied-R1 (Yuan et al., 2025), our method, Vlaser still achieves ... | p. 7 (3 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2: An illustration of Vlaser architecture. Vlaser includes two components and corresponding training phases: 1) the Multimodal Pretraining is for embodied reasoning enhancement ... | p. 3 (Figure/Table caption) |
| 3 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In the following section, we further examine how these enhanced reasoning capabilities, embedded within VLMs, translate into improved performance when fine-tuned for downstream Vision-Language ... | p. 7 (3 EXPERIMENTS) |
| 3 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is clear to see that, no matter in which group of hyperparameter settings, the performance based on Vlaser-OOD shows slight improvement compared with ... | p. 9 (3 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 3 EXPERIMENTS - extractive body cue:** SimplerENV is an open-source suite of purpose-built simulated environments with nearly 150K episodes for evaluating real-world robot manipulation policies in a scalable, reproducible way.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Robotwin is a scalable framework for bimanual manipulation, which integrates scalable training sets and pre-defined tasks as benchmarks for comprehensive robust bimanual manipulation.
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** 3.1 PERFORMANCE ON EMBODIED REASONING CAPABILITY Evaluation Datasets We conduct a comprehensive evaluation of embodied reasoning capabilities across a total of 12 benchmarks, covering a ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.2 PERFORMANCE ON DOWNSTREAM CLOSE-LOOP ROBOT TASKS Finetuning Datasets We firstly conduct extensive experiments on SimplerENV (Li et al., 2024d) to evaluate the performance of ...
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** Therefore, it is urgent to shrink the domain gap between the foundational models and real-world robot embodiment for closed-loop task completion.
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** This observation illustrates the effectiveness of our Vlaser data engine, and meanwhile identifies that there is no positive correlation between common embodied reasoning benchmarks and ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** An interesting observation emerges that when finetuning on the same Vlaser-6M dataset, a smaller sized Vlaser-2B outperforms Vlaser-8B on simple point grounding tasks that require ...
- **p. 22 / A.3 SIMULATION EVALUATION DETAILS - extractive body cue:** To ensure fair evaluation, we use checkpoints with the same number of iterations for the WidowX Robot Task and the Google Robot Task, respectively.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overall framework, capabilities, and evaluation of Vlaser. Top-left: Composition of the Vlaser-6M dataset, featuring multi-task embodied data-including QA, grounding, spatial reasoning, and planning-along ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: An illustration of Vlaser architecture. Vlaser includes two components and corresponding training phases: 1) the Multimodal Pretraining is for embodied reasoning enhancement based ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. We illustrate the two components respectively in this section. VLM Backbone Vision-language models (VLMs) are key candidates for embodied agents, providing both perception ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Comparison with existing close-sourced, open-sourced and embodied-related VLMs on 12 general embodied reasoning benchmarks, spanning from embodied QA, planning, embodied grounding to spatial ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: SimplerEnv Evaluation on WidowX Robot Tasks. Avg indicates the average success rate among the four tasks. Model sizes are indicated within parentheses. The ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Comparison with existing methods in SimplerEnv on Google Robot tasks. Avg indicates the average success rate among the three tasks. Model sizes are ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robotwin Evaluation on Aloha-AgileX Robot Tasks. Avg indicates the average success rate among the 12 tasks. The results of RDT-1B (Liu et al., ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Ablation Studies on WidowX Robot Tasks

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SimplerENV is an open-source suite of purpose-built simulated environments with nearly 150K episodes for evaluating real-world robot manipulation policies in a scalable, reproducible way. | embodiment, simulator version and control stack | p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Task/environment | Robotwin is a scalable framework for bimanual manipulation, which integrates scalable training sets and pre-defined tasks as benchmarks for comprehensive robust bimanual manipulation. | reset, timeout, object/scene variation | p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (2 METHOD), p. 5 (2 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (2 METHOD), p. 4 (2 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Avg indicates the average success rate among the four tasks. | definition/direction/unit from same section | p. 7 (3 EXPERIMENTS) |
| The task success rates of Vlaser-OOD and the baseline InternVL3-2B remain close. | definition/direction/unit from same section | p. 9 (3 EXPERIMENTS) |
| This suggests that pretraining with diverse in-domain multimodal data, spanning general QA, grounding, and spatial intelligence, could best facilitates transfer learning for VLA policy ... | definition/direction/unit from same section | p. 9 (3 EXPERIMENTS) |
| These significant performance gains underscore the high quality and effectiveness of the Vlaser-6M dataset in enhancing embodied reasoning abilities. | definition/direction/unit from same section | p. 7 (3 EXPERIMENTS) |
| Table 1: Comparison with existing close-sourced, open-sourced and embodied-related VLMs on 12 general embodied reasoning benchmarks, spanning from embodied QA, planning, embodied grounding to ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 1: Overall framework, capabilities, and evaluation of Vlaser. Top-left: Composition of the Vlaser-6M dataset, featuring multi-task embodied data-including QA, grounding, spatial reasoning, and ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| For EmbodiedBench, we further assess performance in two simulation environments ALFRED (Shridhar et al., 2020) and Habitat (Szot et al., 2021). | definition/direction/unit from same section | p. 6 (3 EXPERIMENTS) |
| It targets the key real-to-sim gaps - control and vision so that simulated performance reliably tracks real-robot outcomes. | definition/direction/unit from same section | p. 8 (3 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| When compared against current state-of-the-art embodied-specific VLMs, including RoboBrain2.0 (Team et al., 2025a) and Embodied-R1 (Yuan et al., 2025), our method, Vlaser still achieves ... | comparison identity and matched condition | p. 7 (3 EXPERIMENTS) |
| 36.8% 55.8% 54.5% 60.7% 61.2% 60.7% 67.5% Baselines Alongside comparisons with other commonly used VLA models (Black et al., 2024; Kim et al., 2024; ... | comparison identity and matched condition | p. 8 (3 EXPERIMENTS) |
| An interesting observation emerges that when finetuning on the same Vlaser-6M dataset, a smaller sized Vlaser-2B outperforms Vlaser-8B on simple point grounding tasks that ... | comparison identity and matched condition | p. 7 (3 EXPERIMENTS) |
| The task success rates of Vlaser-OOD and the baseline InternVL3-2B remain close. | comparison identity and matched condition | p. 9 (3 EXPERIMENTS) |
| Regarding the three types of in-domain data annotations, we experimentally find that incorporating any of them leads to significant performance gains over the baseline. | comparison identity and matched condition | p. 9 (3 EXPERIMENTS) |
| Table 1: Comparison with existing close-sourced, open-sourced and embodied-related VLMs on 12 general embodied reasoning benchmarks, spanning from embodied QA, planning, embodied grounding to ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3.1, without any in-domain data in Vlaser-6M dataset. | component/input/data sensitivity | p. 8 (3 EXPERIMENTS) |
| Across Google Robot and WidowX/BridgeData V2 setups, SimplerEnv reports strong real-vs-sim correlations and faithfully reflects behavior under distribution shifts, enabling fast, comparable policy assessment ... | component/input/data sensitivity | p. 8 (3 EXPERIMENTS) |
| 3.3 ABLATION STUDIES In this section, we adopt ablation studies regarding three key hyperparameters for VLA end-to-end training, i.e.,, the predicted action length P, ... | component/input/data sensitivity | p. 9 (3 EXPERIMENTS) |
| Figure 2: An illustration of Vlaser architecture. Vlaser includes two components and corresponding training phases: 1) the Multimodal Pretraining is for embodied reasoning enhancement ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Table 5: Ablation Studies on WidowX Robot Tasks | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| In the following section, we further examine how these enhanced reasoning capabilities, embedded within VLMs, translate into improved performance when fine-tuned for downstream Vision-Language ... | component/input/data sensitivity | p. 7 (3 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Here we present the overall data scale and sources for each reasoning modality, while more details about the construction methodologies are provided in Appendix ... | This suggests that pretraining with diverse in-domain multimodal data, spanning general QA, grounding, and spatial intelligence, could best facilitates transfer learning for VLA policy ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 3 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Primary metric/result | When compared against current state-of-the-art embodied-specific VLMs, including RoboBrain2.0 (Team et al., 2025a) and Embodied-R1 (Yuan et al., 2025), our method, Vlaser still achieves ... | numeric claim only at cited anchor | p. 7 (3 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Avg indicates the average success rate among the 12 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These results indicate that Vlaser delivers a well-balanced and robust capability set, performing strongly across multiple dimensions of embodied intelligence - from embodied question ... | p. 7 (3 EXPERIMENTS) |
| body limitation/failure cue | Robotwin is a scalable framework for bimanual manipulation, which integrates scalable training sets and pre-defined tasks as benchmarks for comprehensive robust bimanual manipulation. | p. 8 (3 EXPERIMENTS) |
| body limitation/failure cue | This conclusion is as same as the results in 3.2, which demonstrates great robustness of our method. | p. 9 (3 EXPERIMENTS) |
| body limitation/failure cue | Carrot on the plate Put eggplant in basket InternVL3-2B Fail Vlaser Success Vlaser-QA Success Spoon on the towel Stack Cube InternVL3-2B Fail Vlaser Success ... | p. 27 (A.4 QUALITATIVE DEMONSTRATION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector ... | p. 18 (A.1 TRAINING DETAILS) |
| 3.3 ABLATION STUDIES In this section, we adopt ablation studies regarding three key hyperparameters for VLA end-to-end training, i.e.,, the predicted action length P, ... | p. 9 (3 EXPERIMENTS) |
| In our experiments, we set H as 4, and δ as 0.1(δ-1 = 10 integration steps) at inference time for the improvement of inference ... | p. 6 (2 METHOD) |
| The results of RDT-1B (Liu et al., 2024) are from our self-implemented training for 30k steps, which aligns the training setting with Vlaser. | p. 8 (3 EXPERIMENTS) |
| It is clear to see that, no matter in which group of hyperparameter settings, the performance based on Vlaser-OOD shows slight improvement compared with ... | p. 9 (3 EXPERIMENTS) |
| Further details regarding the training setup, including hyperparameters and optimization settings, are provided in Table 6. | p. 18 (A.1 TRAINING DETAILS) |
| In the flow matching configuration, we use 10 inference steps during the inference phase and apply Euler method as numerical integration method. | p. 22 (A.3 SIMULATION EVALUATION DETAILS) |
| To ensure fair evaluation, we use checkpoints with the same number of iterations for the WidowX Robot Task and the Google Robot Task, respectively. | p. 22 (A.3 SIMULATION EVALUATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 3 EXPERIMENTS - extractive body cue:** These results indicate that Vlaser delivers a well-balanced and robust capability set, performing strongly across multiple dimensions of embodied intelligence - from embodied question answering ...
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Robotwin is a scalable framework for bimanual manipulation, which integrates scalable training sets and pre-defined tasks as benchmarks for comprehensive robust bimanual manipulation.
- **p. 9 / 3 EXPERIMENTS - extractive body cue:** This conclusion is as same as the results in 3.2, which demonstrates great robustness of our method.
- **p. 27 / A.4 QUALITATIVE DEMONSTRATION - extractive body cue:** Carrot on the plate Put eggplant in basket InternVL3-2B Fail Vlaser Success Vlaser-QA Success Spoon on the towel Stack Cube InternVL3-2B Fail Vlaser Success Vlaser-QA ...

- **Evidence anchors reviewed:** datasets p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), metrics p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 6 (Figure/Table caption), results p. 9 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 3 (Figure/Table caption), p. 7 (3 EXPERIMENTS), p. 9 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
