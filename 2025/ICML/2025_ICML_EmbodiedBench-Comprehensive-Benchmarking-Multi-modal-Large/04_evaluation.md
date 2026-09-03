# Evaluation - EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (56 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=DgGF2LEBPS; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/164956. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5.4. Visual-centric Ablation), p. 30 (Figure/Table caption), p. 26 (Figure/Table caption), p. 6 (5.2. Benchmark Results), p. 8 (5.4. Visual-centric Ablation), p. 9 (5.4. Visual-centric Ablation)): As shown in Figure 5 (d), the results demonstrate that visual ICL significantly outperforms language-only ICL.

## Evaluation Body Digest

- **p. 6 / 5.2. Benchmark Results - extractive body cue:** These findings emphasize two key insights: (1) when designing MLLM-based embodied AI benchmarks, it is essential to consider action-level taxonomy, with greater attention to low-level ...
- **p. 9 / 5.5. Error Analysis - extractive body cue:** For each environment, we sample 10 failure episodes from each subset, resulting in a total of 110 failed episodes to be analyzed.
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** We benchmark 24 models, including 8 leading proprietary models and 16 SOTA open-source models.
- **p. 7 / 5.2. Benchmark Results - extractive body cue:** EMBODIEDBENCH: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents Table 2.
- **p. 8 / 5.4. Visual-centric Ablation - extractive body cue:** In EB-Manipulation, detection boxes and visual markers are used to align language instructions with visual information, helping to localize key objects in the scene.
- **p. 9 / 5.5. Error Analysis - extractive body cue:** Overall, planning errors are the most common issue in both environments, while perception errors are more prevalent in low-level tasks.
- **p. 7 / 5.4. Visual-centric Ablation - extractive body cue:** Visual information is critical for the performance of lowlevel tasks.
- **p. 8 / 5.4. Visual-centric Ablation - extractive body cue:** Previous work has primarily relied on text-based ICL demonstrations.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Setups (p. 6); 5.2. Benchmark Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.4. Visual-centric Ablation | BENCHMARK / DATASET | As shown in Figure 5 (d), the results demonstrate that visual ICL significantly outperforms language-only ICL. | p. 9 (5.4. Visual-centric Ablation) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 16. Impact of visual in-context learning on EMBODIEDBENCH. impressive gains in manipulation tasks. For instance, Claude-3.5-Sonnet achieves a 16.7% improvement in performance. These ... | p. 30 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 7. Impact of different camera resolutions on EMBODIEDBENCH. F.4. Detection Boxes Figure 8 illustrates the impact of using detection (bounding) boxes. The results ... | p. 26 (Figure/Table caption) |
| 5.2. Benchmark Results | BENCHMARK / DATASET | Among proprietary models, we observe that different models excel at different task levels: Claude-3.5-Sonnet achieves the highest average accuracy on high-level tasks, with 64.0% ... | p. 6 (5.2. Benchmark Results) |
| 5.4. Visual-centric Ablation | BENCHMARK / DATASET | Our results, shown in Figure 5 (a), indicate that mid-range resolutions (500 × 500) achieve better results compared to both lower (300 × 300) ... | p. 8 (5.4. Visual-centric Ablation) |

## Dataset / Benchmark Role

- **p. 6 / 5.2. Benchmark Results - extractive body cue:** These findings emphasize two key insights: (1) when designing MLLM-based embodied AI benchmarks, it is essential to consider action-level taxonomy, with greater attention to low-level ...
- **p. 9 / 5.5. Error Analysis - extractive body cue:** For each environment, we sample 10 failure episodes from each subset, resulting in a total of 110 failed episodes to be analyzed.
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** We benchmark 24 models, including 8 leading proprietary models and 16 SOTA open-source models.
- **p. 7 / 5.2. Benchmark Results - extractive body cue:** EMBODIEDBENCH: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents Table 2.
- **p. 8 / 5.4. Visual-centric Ablation - extractive body cue:** In EB-Manipulation, detection boxes and visual markers are used to align language instructions with visual information, helping to localize key objects in the scene.
- **p. 9 / 5.5. Error Analysis - extractive body cue:** Overall, planning errors are the most common issue in both environments, while perception errors are more prevalent in low-level tasks.
- **p. 7 / 5.4. Visual-centric Ablation - extractive body cue:** Visual information is critical for the performance of lowlevel tasks.
- **p. 8 / 5.4. Visual-centric Ablation - extractive body cue:** Previous work has primarily relied on text-based ICL demonstrations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of EMBODIEDBENCH. Two key features of our benchmark: various action levels and capability-oriented evaluation. Habitat focus on high-level task decomposition and planning ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Comparison with related benchmarks. EMBODIEDBENCH is a multi-domain benchmark including household, manipulation, and navigation tasks. "Fine-grained" indicates a multi-dimensional evaluation approach rather than ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The vision-driven agent pipeline used in EMBODIEDBENCH. This pipeline serves as a robust framework for processing multimodal inputs, reflection and reasoning, and generating ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Planning examples in EB-ALFRED and EB-Manipulation based on GPT-4o. [57, 61, 20, 10, 60, 25, 1]; and (2) additional information like YOLO (Redmon, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Task success rates on 6 subsets of EB-ALFRED and EB-Habitat, with the best proprietary model in bold and open-source model underlines per column. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Language-centric ablations on EB-ALFRED.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Visual-centric ablations on EB-Manipulation. than on visual input.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Task success rates on 5 subsets of EB-Navigation and EB-Manipulation, with the best proprietary model in bold and open-source model underlines per column.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These findings emphasize two key insights: (1) when designing MLLM-based embodied AI benchmarks, it is essential to consider action-level taxonomy, with greater attention to ... | embodiment, simulator version and control stack | p. 6 (5.2. Benchmark Results), p. 9 (5.5. Error Analysis) |
| Task/environment | For each environment, we sample 10 failure episodes from each subset, resulting in a total of 110 failed episodes to be analyzed. | reset, timeout, object/scene variation | p. 9 (5.5. Error Analysis), p. 6 (5.1. Experimental Setups) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 3 (3. Problem Formulation), p. 3 (3. Problem Formulation) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the task success rate as the primary metric in our experiments. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setups) |
| In a 0-shot setting, the success rate drops to around 40%. | definition/direction/unit from same section | p. 7 (5.3. Language-centric Ablation) |
| Success rates for subsets are integers since each subset consists of 50 test instances. | definition/direction/unit from same section | p. 7 (5.2. Benchmark Results) |
| Task success rates on 5 subsets of EB-Navigation and EB-Manipulation, with the best proprietary model in bold and open-source model underlines per column. | definition/direction/unit from same section | p. 8 (5.4. Visual-centric Ablation) |
| Figure 7. Impact of different camera resolutions on EMBODIEDBENCH. F.4. Detection Boxes Figure 8 illustrates the impact of using detection (bounding) boxes. The results ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| The long-horizon subset consistently proves to be the most difficult, showing the largest performance gap compared to base scores. | definition/direction/unit from same section | p. 6 (5.2. Benchmark Results) |
| 22% spatial understanding 8% spatial reasoning 10% reflection error 13% inaccurate action 42% invalid action 1% (b) EB-Manipulation Figure 6. | definition/direction/unit from same section | p. 9 (5.4. Visual-centric Ablation) |
| For EB-Manipulation, planning errors remain the primary cause of failure (44%), due to inaccurate actions, indicating difficulties in estimating precise gripper poses. | definition/direction/unit from same section | p. 9 (5.5. Error Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 6. Error Analysis. image. Visual ICL examples are demonstrated in Figure 15. We limit the number of examples to two to avoid over- ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Low-level tasks show a much stronger reliance on vision compared to high-level tasks. | comparison identity and matched condition | p. 6 (5.2. Benchmark Results) |
| The long-horizon subset consistently proves to be the most difficult, showing the largest performance gap compared to base scores. | comparison identity and matched condition | p. 6 (5.2. Benchmark Results) |
| When compared with results in Table 2, where removing vision can even lead to performance gains, these findings highlight that high-level tasks rely more ... | comparison identity and matched condition | p. 7 (5.3. Language-centric Ablation) |
| Our results, shown in Figure 5 (a), indicate that mid-range resolutions (500 × 500) achieve better results compared to both lower (300 × 300) ... | comparison identity and matched condition | p. 8 (5.4. Visual-centric Ablation) |
| Figure 15. Visual in-context learning examples for EB-Navigation & EB-Manipulation F.7. Visual In-context Learning (ICL) Previous research has mainly focused on text-based in-context learning ... | comparison identity and matched condition | p. 29 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We investigate the effect of three camera resolutions on task performance. | component/input/data sensitivity | p. 8 (5.4. Visual-centric Ablation) |
| Figure 16. Impact of visual in-context learning on EMBODIEDBENCH. impressive gains in manipulation tasks. For instance, Claude-3.5-Sonnet achieves a 16.7% improvement in performance. These ... | component/input/data sensitivity | p. 30 (Figure/Table caption) |
| More results and ablations are deferred to Appendix F. | component/input/data sensitivity | p. 6 (5.1. Experimental Setups) |
| By comparing the performance of embodied agents with and without visual information (marked as "Lang") in Tables 2 and 3, we observe a clear ... | component/input/data sensitivity | p. 6 (5.2. Benchmark Results) |
| Language-centric ablations on EB-ALFRED. | component/input/data sensitivity | p. 7 (5.2. Benchmark Results) |
| Visual-centric ablations on EB-Manipulation. than on visual input. | component/input/data sensitivity | p. 7 (5.3. Language-centric Ablation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are threefold: (1) proposing a comprehensive benchmark suite for evaluating MLLM-based embodied agents with different action levels and fine-grained capability-oriented subsets, (2) ... | As shown in Figure 5 (d), the results demonstrate that visual ICL significantly outperforms language-only ICL. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5.4. Visual-centric Ablation), p. 30 (Figure/Table caption), p. 26 (Figure/Table caption), p. 6 (5.2. Benchmark Results), p. 8 (5.4. Visual-centric Ablation), p. 9 (5.4. Visual-centric Ablation) |
| Primary metric/result | Figure 16. Impact of visual in-context learning on EMBODIEDBENCH. impressive gains in manipulation tasks. For instance, Claude-3.5-Sonnet achieves a 16.7% improvement in performance. These ... | numeric claim only at cited anchor | p. 30 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Setups - extractive body cue:** All images are standardized to a resolution of 500×500 pixels.
- **p. 6 / 5.2. Benchmark Results - extractive body cue:** In EB-Manipulation, for example, Claude-3.5-Sonnet scores 14.6 and 5.6 points higher than GPT-4o on the complex instruction and visual appearance subsets, respectively, but falls significantly ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations A key limitation of this work is that our evaluation is conducted solely in simulated environments, without real-world experiments. | p. 9 (6. Conclusion) |
| body limitation/failure cue | Perception errors make up 33% of failures, with wrong recognition errors (22%) being the most frequent. | p. 9 (5.5. Error Analysis) |
| body limitation/failure cue | Figure 17. Error Analysis on EB-Navigation. Perception Errors. The first category involves the model's ability to interpret visual observations and recognize the spatial position ... | p. 31 (Figure/Table caption) |
| body limitation/failure cue | Table 11. Error Taxonomy with Definitions model failed to identify the target object even when it was present in the visual input. This suggests ... | p. 32 (Figure/Table caption) |
| body limitation/failure cue | These results highlight the importance of fine-grained evaluations to uncover nuanced limitations in current models. | p. 6 (5.2. Benchmark Results) |
| body limitation/failure cue | In EB-Manipulation, for example, Claude-3.5-Sonnet scores 14.6 and 5.6 points higher than GPT-4o on the complex instruction and visual appearance subsets, respectively, but falls ... | p. 6 (5.2. Benchmark Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The maximum number of environment steps is 30 for high-level tasks, 20 for EB-Navigation, and 15 for EB-Manipulation. | p. 6 (5.1. Experimental Setups) |
| For EB-Manipulation, we include observations from the past two steps in addition to the current step. | p. 8 (5.4. Visual-centric Ablation) |
| Among planning errors, missing steps (23%) and invalid actions (22%) are the most common issues, highlighting challenges in generating complete and valid plans. | p. 9 (5.5. Error Analysis) |
| For instance, a robotic arm's action is often parameterized as a 7-dimensional vector: a = [X, Y, Z, Roll, Pitch, Yaw, Gripper], where (X, ... | p. 3 (3. Problem Formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Conclusion - extractive body cue:** Limitations A key limitation of this work is that our evaluation is conducted solely in simulated environments, without real-world experiments.
- **p. 9 / 5.5. Error Analysis - extractive body cue:** Perception errors make up 33% of failures, with wrong recognition errors (22%) being the most frequent.
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 17. Error Analysis on EB-Navigation. Perception Errors. The first category involves the model's ability to interpret visual observations and recognize the spatial position of ...
- **p. 32 / Figure/Table caption - extractive body cue:** Table 11. Error Taxonomy with Definitions model failed to identify the target object even when it was present in the visual input. This suggests limitations ...
- **p. 6 / 5.2. Benchmark Results - extractive body cue:** These results highlight the importance of fine-grained evaluations to uncover nuanced limitations in current models.
- **p. 6 / 5.2. Benchmark Results - extractive body cue:** In EB-Manipulation, for example, Claude-3.5-Sonnet scores 14.6 and 5.6 points higher than GPT-4o on the complex instruction and visual appearance subsets, respectively, but falls significantly ...

- **Evidence anchors reviewed:** datasets p. 6 (5.2. Benchmark Results), p. 9 (5.5. Error Analysis), p. 6 (5.1. Experimental Setups), p. 7 (5.2. Benchmark Results), p. 8 (5.4. Visual-centric Ablation), p. 9 (5.5. Error Analysis), metrics p. 6 (5.1. Experimental Setups), p. 7 (5.3. Language-centric Ablation), p. 7 (5.2. Benchmark Results), p. 8 (5.4. Visual-centric Ablation), p. 26 (Figure/Table caption), p. 6 (5.2. Benchmark Results), baselines p. 9 (Figure/Table caption), p. 6 (5.2. Benchmark Results), p. 6 (5.2. Benchmark Results), p. 7 (5.3. Language-centric Ablation), p. 8 (5.4. Visual-centric Ablation), p. 29 (Figure/Table caption), results p. 9 (5.4. Visual-centric Ablation), p. 30 (Figure/Table caption), p. 26 (Figure/Table caption), p. 6 (5.2. Benchmark Results), p. 8 (5.4. Visual-centric Ablation), p. 9 (5.4. Visual-centric Ablation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
