# Evaluation - MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.09516v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption)): On average, MAP-VLA achieves an 83.4% success rate, whereas the baseline OpenVLA and π0 achieve 54.0% and 76.4%, respectively.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** To validate the real-world effectiveness of MAP-VLA, we conduct evaluations on a physical robotic platform and compare its performance with the strongest baseline, π0, across ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** For real-world experiments, MAP-VLA is deployed on a 6DoF Galaxea A1 robotic arm shown in Fig.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Overall, the comparisons confirm that MAP-VLA sets a new stateof-the-art for long-horizon task execution in both simulation and real-robot settings, with significantly higher success rates ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Effective long-horizon robot manipulation often demands fine-grained memory to maintain a coherent trajectory across multiple stages.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Comparison with Visual Variations To assess robustness under real-world visual variations, we evaluate MAP-VLA on LIBERO-Long tasks subjected to various challenging visual conditions.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** We also note that MAP-VLA's trial outcomes are more consistent, with a lower standard deviation in success rate (0.7%) across runs than π0 (2.3%).
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Metric Base VLA Universal Prompt Task Prompt Stage Prompt MAP-VLA Success Rate (SR) 76.4% 76.9% 79.3% 81.4% 83.4% Standard Deviation (Std) ± 2.3% ± 2.4% ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On average, MAP-VLA achieves an 83.4% success rate, whereas the baseline OpenVLA and π0 achieve 54.0% and 76.4%, respectively. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Averaged over the three tasks, MAP-VLA's partial success and complete success rates are 68.3% and 48.3%, versus 53.3% and 23.3% for the baseline, showing ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | MAP-VLA achieves average success rates of 55.8% and 75.9% for the 10-shot and 20-shot settings, which are consistently higher than those of the baseline ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite these visual shifts, MAP-VLA consistently retains a significantly higher success rate compared to the baseline π0 policy. | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task. | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** To validate the real-world effectiveness of MAP-VLA, we conduct evaluations on a physical robotic platform and compare its performance with the strongest baseline, π0, across ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** For real-world experiments, MAP-VLA is deployed on a 6DoF Galaxea A1 robotic arm shown in Fig.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Overall, the comparisons confirm that MAP-VLA sets a new stateof-the-art for long-horizon task execution in both simulation and real-robot settings, with significantly higher success rates ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Effective long-horizon robot manipulation often demands fine-grained memory to maintain a coherent trajectory across multiple stages.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Comparison with Visual Variations To assess robustness under real-world visual variations, we evaluate MAP-VLA on LIBERO-Long tasks subjected to various challenging visual conditions.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Simplified execution pipeline of existing VLA methods and MAP-VLA. specific memory prompts and the generalized base prompts. This whole framework, shown in Fig. ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. The framework of MAP-VLA. Our method augments a frozen pre-trained VLA model with demonstration-derived memory prompts for enhanced action generation during task execution. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3. Performance comparison on all LIBERO task suites, "*" denotes results reported by OpenVLA [3]. Using the computed αt, the final memory-augmented action for ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4. Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5. Visualization and comparison of Task2: place the green cube and orange into the bowl. box in the basket, (Task4) put both the alphabet ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6. Performance comparison with visual variations on LIBERO-Long. TABLE III ABLATION STUDY ON LIBERO-LONG. Metric Base VLA Universal Prompt Task Prompt

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To validate the real-world effectiveness of MAP-VLA, we conduct evaluations on a physical robotic platform and compare its performance with the strongest baseline, π0, ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | For real-world experiments, MAP-VLA is deployed on a 6DoF Galaxea A1 robotic arm shown in Fig. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We also note that MAP-VLA's trial outcomes are more consistent, with a lower standard deviation in success rate (0.7%) across runs than π0 (2.3%). | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Metric Base VLA Universal Prompt Task Prompt Stage Prompt MAP-VLA Success Rate (SR) 76.4% 76.9% 79.3% 81.4% 83.4% Standard Deviation (Std) ± 2.3% ± ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Averaged over the three tasks, MAP-VLA's partial success and complete success rates are 68.3% and 48.3%, versus 53.3% and 23.3% for the baseline, showing ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Despite these visual shifts, MAP-VLA consistently retains a significantly higher success rate compared to the baseline π0 policy. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1. Simplified execution pipeline of existing VLA methods and MAP-VLA. specific memory prompts and the generalized base prompts. This whole framework, shown in ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Implementation Details The proposed MAP-VLA is based on the π0 model [4]. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 2. The framework of MAP-VLA. Our method augments a frozen pre-trained VLA model with demonstration-derived memory prompts for enhanced action generation during task ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As summarized in Table II, MAPVLA again outperforms the baseline policy. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| As shown in Table I, MAP-VLA consistently outperforms all baselines across every individual task in this benchmark. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Despite these visual shifts, MAP-VLA consistently retains a significantly higher success rate compared to the baseline π0 policy. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Comparison under Few-Shot Setting To further evaluate the adaptability of our method, we compare it with baseline approaches under few-shot learning scenarios. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Fig. 1. Simplified execution pipeline of existing VLA methods and MAP-VLA. specific memory prompts and the generalized base prompts. This whole framework, shown in ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| We first compare MAP-VLA to baseline VLA models, OpenVLA [3] and π0 [4], on the challenging long-horizon manipulation tasks suite LIBERO-Long (also referred to ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Overall, MAP-VLA achieves an average relative gain of 9.6%, slightly above the 9.2% relative gain without visual variations. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| We first follow [4] to fine-tune the π0 model on the finetuning dataset using LoRA [25] on a server with 6 NVIDIA RTX 6000 ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Fig. 1. Simplified execution pipeline of existing VLA methods and MAP-VLA. specific memory prompts and the generalized base prompts. This whole framework, shown in ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Fig. 6. Performance comparison with visual variations on LIBERO-Long. TABLE III ABLATION STUDY ON LIBERO-LONG. Metric Base VLA Universal Prompt Task Prompt | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model ... | On average, MAP-VLA achieves an 83.4% success rate, whereas the baseline OpenVLA and π0 achieve 54.0% and 76.4%, respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption) |
| Primary metric/result | Averaged over the three tasks, MAP-VLA's partial success and complete success rates are 68.3% and 48.3%, versus 53.3% and 23.3% for the baseline, showing ... | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Real-world environment setup. settings of OpenVLA [3], where the success rate is the average over 3 random seeds x 50 rollouts for each task.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** 4 to perform 20 rollouts for each task.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** All real-world computations are conducted on a system with an NVIDIA RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, the memoryless baseline policy π0 exhibits inconsistent and ambiguous object alignment behavior, especially during critical pick-and-place phases (as circled in the figure), often ... | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | By dynamically balancing the task-level generalization of the base prompt with the stage-specificity of the retrieved prompt, the model maintains robustness to retrieval inaccuracies, ... | p. 5 (III. METHODOLOGY) |
| body limitation/failure cue | This reduced variability suggests improved robustness and reliability, as a result of encoding additional contextual memory into the prompt and dynamic prompt ensembling as ... | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | In contrast, our MAP-VLA framework demonstrates memory-augmented robustness in such settings. | p. 7 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details The proposed MAP-VLA is based on the π0 model [4]. | p. 5 (IV. EXPERIMENTS) |
| All real-world computations are conducted on a system with an NVIDIA RTX 4090 GPU. | p. 5 (IV. EXPERIMENTS) |
| We also note that MAP-VLA's trial outcomes are more consistent, with a lower standard deviation in success rate (0.7%) across runs than π0 (2.3%). | p. 6 (IV. EXPERIMENTS) |
| Our framework comprises two components: (i) Memory Prompt Construction (MPC), which encodes stage-level memory into soft prompts derived from expert demonstrations, and (ii) Memory-Augmented ... | p. 3 (III. METHODOLOGY) |
| (3) This process effectively encodes the demonstration memory of a stage into the prompt embeddings to augment action generation. | p. 4 (III. METHODOLOGY) |
| The final stage-specific memory prompt Pk input to the VLA model is computed via element-wise addition: [Pk]j = [Pbase]j + [Vk]j , ∀j = ... | p. 4 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** However, the memoryless baseline policy π0 exhibits inconsistent and ambiguous object alignment behavior, especially during critical pick-and-place phases (as circled in the figure), often leading ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** By dynamically balancing the task-level generalization of the base prompt with the stage-specificity of the retrieved prompt, the model maintains robustness to retrieval inaccuracies, improves ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** This reduced variability suggests improved robustness and reliability, as a result of encoding additional contextual memory into the prompt and dynamic prompt ensembling as we ...
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** In contrast, our MAP-VLA framework demonstrates memory-augmented robustness in such settings.

- **PDF anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
