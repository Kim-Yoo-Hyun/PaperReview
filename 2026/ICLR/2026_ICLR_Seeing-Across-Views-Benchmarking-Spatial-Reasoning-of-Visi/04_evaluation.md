# Evaluation - Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jXDZJAfRZB; PDF retrieval source: https://openreview.net/pdf/458ff860f6b8211513575bef44521e0241b321c0.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 33 (Figure/Table caption), p. 8 (Figure/Table caption), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption)): Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) compared to the Single-View baseline. Positive ...

## Evaluation Body Digest

- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** F.10 SUMMARY OF BENCHMARK CONSTRUCTION Taken together, the eight subtasks provide a comprehensive evaluation of spatial and robotic reasoning in multi-view environments.
- **p. 18 / C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS - extractive PDF cue:** While effective for clean object-level inputs, they proved unsuitable for cluttered robotic scenes, as selecting accurate masks is non-trivial and the outputs often failed to ...
- **p. 20 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** The top row shows the original RGB images; the bottom row shows the corresponding MoGe-2 depth predictions (red indicates closer, blue indicates farther). spatial intelligence ...
- **p. 21 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** E PREPARATIONS OF BENCHMARK CONSTRUCTION E.1 ANNOTATION TOOL AND INTERFACE To construct and annotate our dataset, we developed a custom graphical annotation tool based on ...
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** F.8 AFFORDANCE RECOGNITION This subtask belongs to the robotic category and evaluates a model's ability to recognize feasible grasp candidates in multi-view scenes.
- **p. 19 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** D EVALUATION ON EXTERNAL SPATIAL BENCHMARKS Our study focuses on spatial intelligence within robotic operation scenarios.
- **p. 34 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** While this result highlights a limitation in zero-shot generalization, we note that in real-world robotic deployment, camera mounting poses are strictly controlled, and input images ...
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** B EXPERIMENTAL SETUP (p. 16); B.4 EVALUATION PROTOCOL (p. 17); B.5 HUMAN EVALUATION (p. 17); C IMPLEMENTATION OF COT-INSPIRED ENHANCEMENTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) ... | p. 33 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: ... | p. 8 (Figure/Table caption) |
| C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS | BENCHMARK / DATASET | This suggests that MV-RoboBench does not merely lower raw accuracy; it exposes non-trivial limitations in current vision-language models' spatial reasoning, and can serve as ... | p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 10: Structural augmentation via depth priors. The top row shows the original RGB images; the bottom row shows the corresponding MoGe-2 depth predictions ... | p. 20 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Table 4: Comparison of model performance on OmniSpatial, covering four categories: dynamic reasoning, spatial interaction, complex logic, and perspective taking. Results are reported as ... | p. 21 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** F.10 SUMMARY OF BENCHMARK CONSTRUCTION Taken together, the eight subtasks provide a comprehensive evaluation of spatial and robotic reasoning in multi-view environments.
- **p. 18 / C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS - extractive PDF cue:** While effective for clean object-level inputs, they proved unsuitable for cluttered robotic scenes, as selecting accurate masks is non-trivial and the outputs often failed to ...
- **p. 20 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** The top row shows the original RGB images; the bottom row shows the corresponding MoGe-2 depth predictions (red indicates closer, blue indicates farther). spatial intelligence ...
- **p. 21 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** E PREPARATIONS OF BENCHMARK CONSTRUCTION E.1 ANNOTATION TOOL AND INTERFACE To construct and annotate our dataset, we developed a custom graphical annotation tool based on ...
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** F.8 AFFORDANCE RECOGNITION This subtask belongs to the robotic category and evaluates a model's ability to recognize feasible grasp candidates in multi-view scenes.
- **p. 19 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** D EVALUATION ON EXTERNAL SPATIAL BENCHMARKS Our study focuses on spatial intelligence within robotic operation scenarios.
- **p. 34 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** While this result highlights a limitation in zero-shot generalization, we note that in real-world robotic deployment, camera mounting poses are strictly controlled, and input images ...
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of spatial reasoning benchmarks. Prior datasets emphasize single-view rela- tions, abstract reasoning, or non-embodied multi-view perception. The "Partial" in "Multi-View" indicates that ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Representative multi-view QA instances from the eight tasks in MV-RoboBench, with spatial tasks shown on the left and robotic tasks on the right. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Construction pipeline of MV-RoboBench, consisting of three stages: data collection, QA generation, and human-in-the-loop quality review. Figure 1 illustrates representative examples from the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Data distribution of MV-RoboBench, showing QA counts per subtask and dataset source (AgiWorld and BridgeV2), and the overall balance between spatial and robotic ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Evaluation on MV-RoboBench under a unified zero-shot prompt. denotes the best score and the second-best within each column. Qwen2.5-vl-72B leads among open-source models, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Best-per-group model perfor- mance across MV-RoboBench subtasks. indicating that they fail to leverage multi-view infor- mation and effectively guess without spatial integration. In ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: w ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: Spatial vs. robotic accuracy on MV-RoboBench. Models clustered near the lower-left op- erate close to random guessing, while reasoning-enhanced proprietary models show a ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | F.10 SUMMARY OF BENCHMARK CONSTRUCTION Taken together, the eight subtasks provide a comprehensive evaluation of spatial and robotic reasoning in multi-view environments. | embodiment, simulator version and control stack | p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |
| Task/environment | While effective for clean object-level inputs, they proved unsuitable for cluttered robotic scenes, as selecting accurate masks is non-trivial and the outputs often failed ... | reset, timeout, object/scene variation | p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 10 (1 INTRODUCTION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Evaluation on MV-RoboBench under a unified zero-shot prompt. denotes the best score and the second-best within each column. Qwen2.5-vl-72B leads among open-source ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 5: Spatial vs. robotic accuracy on MV-RoboBench. Models clustered near the lower-left op- erate close to random guessing, while reasoning-enhanced proprietary models show ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| While ERQA is domain-relevant, our analysis suggests that it exhibits low discriminative power for comparing current SOTA models: • Compressed Performance Range: The overall ... | definition/direction/unit from same section | p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Figure 10: Structural augmentation via depth priors. The top row shows the original RGB images; the bottom row shows the corresponding MoGe-2 depth predictions ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Table 4: Comparison of model performance on OmniSpatial, covering four categories: dynamic reasoning, spatial interaction, complex logic, and perspective taking. Results are reported as ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 5: Evaluation results on the ERQA benchmark. Results are reported as accuracy (%). Note the relatively narrow performance gap between open-source and proprietary ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| We report the full multi-view accuracy and the performance gap (∆) relative to the single-view baseline. | definition/direction/unit from same section | p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) ... | definition/direction/unit from same section | p. 33 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) ... | comparison identity and matched condition | p. 33 (Figure/Table caption) |
| For the Single-View setting, we retained only the most informative third-person perspective to ensure a strong baseline: • For the AgiWorld dataset, we used ... | comparison identity and matched condition | p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| To investigate this, we conducted a systematic ablation study comparing the performance of representative models under a Single-View baseline versus the standard Multi-View setting. | comparison identity and matched condition | p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Compared to generative NVS pipelines, they provided more stable results in cluttered manipulation scenes. | comparison identity and matched condition | p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |
| In our robotic setup (e.g., gripper and head-mounted cameras), interpolated views were severely blurred and inconsistent, particularly under narrow baselines and cluttered tabletops (Appendix ... | comparison identity and matched condition | p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4: Best-per-group model perfor- mance across MV-RoboBench subtasks. indicating that they fail to leverage multi-view infor- mation and effectively guess without spatial integration. ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| This suggests that effectively fusing discordant visual information requires strong spatial reasoning capabilities; without this, smaller models may be distracted by the increased visual ... | component/input/data sensitivity | p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Annotators carefully removed pairs containing occlusions, poor synchronization, or ambiguous spatial relationships to ensure that only high-quality candidates entered the QA generation stage. | component/input/data sensitivity | p. 24 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| This abstraction allows spatial relations to be expressed consistently without requiring precise metric depth. | component/input/data sensitivity | p. 28 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| We ensure that exactly one candidate is feasible across views and can complete the task without collisions; every instance is human-validated to confirm that ... | component/input/data sensitivity | p. 31 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios. | Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) ... | PDF body cue; verify exact table/figure and matched conditions | p. 33 (Figure/Table caption), p. 8 (Figure/Table caption), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption) |
| Primary metric/result | Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 24 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** Collection and Filtering of Image Pairs (∼200 hours).
- **p. 24 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** QA Construction and Iterative Refinement (∼600 hours).
- **p. 24 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** Cross-Checking and Validation (∼400 hours).
- **p. 30 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** F.6 STEP EXECUTION This subtask belongs to the robotic category and focuses on low-level action execution in manipulation tasks.
- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** G.1 TASK SELECTION AND EXPERIMENTAL SETUP Our benchmark consists of eight subtasks.
- **p. 24 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** Collection and Filtering of Image Pairs (∼200 hours).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for ... | p. 36 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| body limitation/failure cue | Figure 30: Case Study 2: Instance-Level Correspondence Failure (Qwen2.5-VL-72B). The scene contains multiple instances of the same class (yellow peppers). The model correctly iden- ... | p. 49 (Figure/Table caption) |
| body limitation/failure cue | A second common failure mode involves incorrect reasoning about depth, occlusion, and 3D layout. | p. 36 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| body limitation/failure cue | Overall, these failures indicate that current VLMs still lack robust modeling of robotic affordances and physical constraints, especially when such reasoning must be carried ... | p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| body limitation/failure cue | This suggests that MV-RoboBench does not merely lower raw accuracy; it exposes non-trivial limitations in current vision-language models' spatial reasoning, and can serve as ... | p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| body limitation/failure cue | Published as a conference paper at ICLR 2026 Figure 7: Failure of object-centric synthesis (Trellis). | p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This appendix provides implementation details for the three CoT-inspired enhancement strategies explored in Section 17 | p. 17 (C IMPLEMENTATION OF COT-INSPIRED ENHANCEMENTS) |
| E.5.1 ANNOTATOR TRAINING AND TASK UNDERSTANDING All annotators participating in the construction of MV-RoboBench were senior undergraduate students or Ph.D. candidates in computer science ... | p. 23 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Finally, annotators completed a trial stage in which they produced small batches of QA items. | p. 24 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| All trial results were reviewed individually by the authors, and detailed feedback was provided for every ambiguous, incorrect, or poorly structured item. | p. 24 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Flagged items are either revised through further discussion-during which annotators and authors jointly inspect the visual evidence and reasoning steps-or discarded entirely. | p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| The reference view marks the target with a red bounding box; other views contain color-coded candidate boxes, one of which corresponds to the ground-truth ... | p. 26 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| We then add distractors from the same episode but different time steps, ensuring a non-trivial temporal gap in the gripper poses so that the ... | p. 27 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Each instance presents five candidate grasps illustrated with color-coded lines (red, yellow, green, blue, and pink). | p. 31 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 36 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a ...
- **p. 49 / Figure/Table caption - extractive PDF cue:** Figure 30: Case Study 2: Instance-Level Correspondence Failure (Qwen2.5-VL-72B). The scene contains multiple instances of the same class (yellow peppers). The model correctly iden- tifies ...
- **p. 36 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** A second common failure mode involves incorrect reasoning about depth, occlusion, and 3D layout.
- **p. 37 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** Overall, these failures indicate that current VLMs still lack robust modeling of robotic affordances and physical constraints, especially when such reasoning must be carried out ...
- **p. 37 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** This suggests that MV-RoboBench does not merely lower raw accuracy; it exposes non-trivial limitations in current vision-language models' spatial reasoning, and can serve as a ...
- **p. 19 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Figure 7: Failure of object-centric synthesis (Trellis).

- **PDF anchors reviewed:** datasets p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 21 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 31 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), metrics p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption), baselines p. 33 (Figure/Table caption), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 8 (Figure/Table caption), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), results p. 33 (Figure/Table caption), p. 8 (Figure/Table caption), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
