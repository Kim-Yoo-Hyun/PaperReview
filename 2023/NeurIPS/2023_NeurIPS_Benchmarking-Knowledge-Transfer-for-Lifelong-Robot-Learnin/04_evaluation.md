# Evaluation - Benchmarking Knowledge Transfer for Lifelong Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (44 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.03310; PDF retrieval source: https://arxiv.org/pdf/2306.03310. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 27 (Figure/Table caption), p. 8 (5 Experiments)): This is surprising since it indicates all lifelong learning algorithms we consider actually hurt forward transfer; 2) PACKNET outperforms other lifelong learning algorithms on LIBERO-X but is outperformed by ER ...

## Evaluation Body Digest

- **p. 8 / 5 Experiments - extractive body cue:** But since PACKNET splits the network into different sub-networks, the essential capacity of the network for learning any individual task is smaller.
- **p. 8 / 5 Experiments - extractive body cue:** In contrast, if ER is used, we observe that RESNET-T performs better than VIT-T on all task suites except LIBERO-OBJECT.
- **p. 6 / 5 Experiments - extractive body cue:** Q5: How robust are different LL algorithms to task ordering in LLDM?
- **p. 6 / 5 Experiments - extractive body cue:** Q3: How do existing algorithms from lifelong supervised learning perform on LLDM tasks?
- **p. 7 / 5 Experiments - extractive body cue:** Please refer to Appendix E.1 for the full results across all algorithms, policy architectures, and task suites.
- **p. 7 / 5 Experiments - extractive body cue:** Results are reported when ER and PACKNET are used as they demonstrate the best lifelong learning performance across all task suites.
- **p. 9 / 5 Experiments - extractive body cue:** The multi-task learning performance is also included for reference.
- **p. 9 / 5 Experiments - extractive body cue:** Study on task ordering (Q5) Figure 4 shows the result of the study on Q4.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | BENCHMARK / DATASET | This is surprising since it indicates all lifelong learning algorithms we consider actually hurt forward transfer; 2) PACKNET outperforms other lifelong learning algorithms on ... | p. 8 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | Q6: Can supervised pretraining improve downstream lifelong learning performance in LLDM? | p. 6 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | Then, we find the earliest epoch e∗ i in which the agent achieves the best performance on task i (i.e., e∗ i = arg ... | p. 6 (5 Experiments) |
| 5 Experiments | BENCHMARK / DATASET | The best performance is bolded, and colored in purple if the improvement is statistically significant over other neural architectures, when a two-tailed, Student's t-test ... | p. 7 (5 Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 13: Comparison of different algorithms using the RESNET-T policy architecture. The y-axis represents the success rate, while the x-axis shows the agent's performance ... | p. 27 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 5 Experiments - extractive body cue:** But since PACKNET splits the network into different sub-networks, the essential capacity of the network for learning any individual task is smaller.
- **p. 8 / 5 Experiments - extractive body cue:** In contrast, if ER is used, we observe that RESNET-T performs better than VIT-T on all task suites except LIBERO-OBJECT.
- **p. 6 / 5 Experiments - extractive body cue:** Q5: How robust are different LL algorithms to task ordering in LLDM?
- **p. 6 / 5 Experiments - extractive body cue:** Q3: How do existing algorithms from lifelong supervised learning perform on LLDM tasks?
- **p. 7 / 5 Experiments - extractive body cue:** Please refer to Appendix E.1 for the full results across all algorithms, policy architectures, and task suites.
- **p. 7 / 5 Experiments - extractive body cue:** Results are reported when ER and PACKNET are used as they demonstrate the best lifelong learning performance across all task suites.
- **p. 9 / 5 Experiments - extractive body cue:** The multi-task learning performance is also included for reference.
- **p. 9 / 5 Experiments - extractive body cue:** Study on task ordering (Q5) Figure 4 shows the result of the study on Q4.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Top: LIBERO has four procedurally-generated task suites: LIBERO-SPATIAL, LIBERO- OBJECT, and LIBERO-GOAL have 10 tasks each and require transferring knowledge about spatial relationships, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: LIBERO's procedural generation pipeline: Extracting behavioral templates from a large- scale human activity dataset (1), Ego4D, for generating task instructions (2); Based on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Metrics for LLDM. 5.2 Experimental Results We present empirical results to address the research questions. Please refer to Appendix E.1 for the full ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance of the three neural architectures using ER and PACKNET on the four task suites. Results are averaged over three seeds and we ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Performance of three lifelong algorithms and the SEQL and MTL baselines on the four task suites, where the policy is fixed to be ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Performance of a lifelong learner using four different language embeddings on LIBERO- LONG, where we fix the policy architecture to RESNET-T and the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Performance of ER and PACKNET using RESNET-T on five different task orderings. An error bar shows the performance standard deviation for a fixed ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Performance of different combinations of algorithms and architectures without pretraining or with pretraining. The multi-task learning performance is also included for reference. Findings: ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | But since PACKNET splits the network into different sub-networks, the essential capacity of the network for learning any individual task is smaller. | embodiment, simulator version and control stack | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Task/environment | In contrast, if ER is used, we observe that RESNET-T performs better than VIT-T on all task suites except LIBERO-OBJECT. | reset, timeout, object/scene variation | p. 8 (5 Experiments), p. 6 (5 Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 6 (2 Background), p. 4 (2 Background) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (2 Background), p. 5 (2 Background) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| All metrics are computed in terms of success rate, as previous literature has shown that the success rate is a more reliable metric than ... | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Let ci,i be the best success rate over all evaluated epochs e for the current task i (i.e., ci,i = maxe ci,i,e). | definition/direction/unit from same section | p. 6 (5 Experiments) |
| Figure 13: Comparison of different algorithms using the RESNET-T policy architecture. The y-axis represents the success rate, while the x-axis shows the agent's performance ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |
| Figure 18: Losses and success rates of ER (violet), EWC (grey), and PACKNET (blue) on four task suites with RESNET-RNN policy. The first (second) ... | definition/direction/unit from same section | p. 31 (Figure/Table caption) |
| An error bar shows the performance standard deviation for a fixed ordering. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Table 1: Performance of the three neural architectures using ER and PACKNET on the four task suites. Results are averaged over three seeds and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 2: Performance of three lifelong algorithms and the SEQL and MTL baselines on the four task suites, where the policy is fixed to ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 3: Performance of a lifelong learner using four different language embeddings on LIBERO- LONG, where we fix the policy architecture to RESNET-T and ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Study on Lifelong Learning Algorithms (Q1, Q3) Table 2 reports the lifelong learning performance of the three lifelong learning algorithms, together with the SEQL ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| This is surprising since it indicates all lifelong learning algorithms we consider actually hurt forward transfer; 2) PACKNET outperforms other lifelong learning algorithms on ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| Figure 26: Attention map comparison between models without/with pretrained models using RESNET- T and different lifelong learning algorithms on three selected tasks from LIBERO-LONG. ... | comparison identity and matched condition | p. 43 (Figure/Table caption) |
| Figure 5: Performance of different combinations of algorithms and architectures without pretraining or with pretraining. The multi-task learning performance is also included for reference. ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 7: Hyper parameters of VIT-T. B.1 Lifelong Learning Algorithms Lifelong learning (LL) is a field of study that aims to understand how an ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| Figure 13: Comparison of different algorithms using the RESNET-T policy architecture. The y-axis represents the success rate, while the x-axis shows the agent's performance ... | comparison identity and matched condition | p. 27 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5: Performance of different combinations of algorithms and architectures without pretraining or with pretraining. The multi-task learning performance is also included for reference. ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 26: Attention map comparison between models without/with pretrained models using RESNET- T and different lifelong learning algorithms on three selected tasks from LIBERO-LONG. ... | component/input/data sensitivity | p. 43 (Figure/Table caption) |
| Table 7: Hyper parameters of VIT-T. B.1 Lifelong Learning Algorithms Lifelong learning (LL) is a field of study that aims to understand how an ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Task-ID embeddings are produced by feeding a string such as "Task 5" into a pretrained BERT model. | component/input/data sensitivity | p. 8 (5 Experiments) |
| Study on Language Embeddings as the Task Identifier (Q4) To investigate to what extent language embedding play a role in LLDM, we compare the ... | component/input/data sensitivity | p. 8 (5 Experiments) |
| For pretraining, we apply behavioral cloning on the 90 tasks using the three policy architectures for 50 epochs. | component/input/data sensitivity | p. 9 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present an initial study using LIBERO to investigate five major research topics in LLDM (Figure 1): 1) knowledge transfer with different types of ... | This is surprising since it indicates all lifelong learning algorithms we consider actually hurt forward transfer; 2) PACKNET outperforms other lifelong learning algorithms on ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 27 (Figure/Table caption), p. 8 (5 Experiments) |
| Primary metric/result | Q6: Can supervised pretraining improve downstream lifelong learning performance in LLDM? | numeric claim only at cited anchor | p. 6 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** Then the three metrics are defined: FWT = X k∈[K] FWTk K , FWTk = 1 11 X e∈{0...50} ck,k,e NBT = X k∈[K] NBTk ...
- **p. 9 / 5 Experiments - extractive body cue:** Embedding Type Dimension FWT(↑) NBT(↓) AUC(↑) BERT 768 0.48 ± 0.02 0.32 ± 0.04 0.32 ± 0.01 CLIP 512 0.52 ± 0.00 0.34 ± 0.01 ...
- **p. 9 / 5 Experiments - extractive body cue:** For pretraining, we apply behavioral cloning on the 90 tasks using the three policy architectures for 50 epochs.
- **p. 9 / 5 Experiments - extractive body cue:** We save a checkpoint every 5 epochs of training and then pick the checkpoint for each architecture that has the best performance as the pretrained ...
- **p. 1 / Abstract - extractive body cue:** For benchmarking purpose, we create four task suites (130 tasks in total) that we use to investigate the above-mentioned research topics.
- **p. 2 / 1 Introduction - extractive body cue:** Procedural Generation Involve declarative knowledge Involve procedural knowledge LIBERO-Object LIBERO-Spatial LIBERO-Goal LIBERO-100 Different layouts, same objects Different objects, same layout Different goals, same objects & ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Q5: How robust are different LL algorithms to task ordering in LLDM? | p. 6 (5 Experiments) |
| body limitation/failure cue | Therefore, we conjecture that PACKNET is not rich enough to learn on LIBEROLONG; 3) EWC works worse than SEQL, showing that the regularization on ... | p. 8 (5 Experiments) |
| body limitation/failure cue | This finding highlights an important direction for future research: developing algorithms or architectures that are robust to varying task orderings. | p. 9 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| But we keep the best checkpoint among those saved at epochs {e} as if the agent stops learning after e∗ i . | p. 6 (5 Experiments) |
| We save a checkpoint every 5 epochs of training and then pick the checkpoint for each architecture that has the best performance as the ... | p. 9 (5 Experiments) |
| Let ci,i be the best success rate over all evaluated epochs e for the current task i (i.e., ci,i = maxe ci,i,e). | p. 6 (5 Experiments) |
| Results are averaged over three seeds and we report the mean and standard error. | p. 7 (5 Experiments) |
| For pretraining, we apply behavioral cloning on the 90 tasks using the three policy architectures for 50 epochs. | p. 9 (5 Experiments) |
| Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder ... | p. 1 (Abstract) |
| Specifically, the sequential nature of LLDM suggests that even minor forgetting over successive steps can potentially lead to a total failure in execution. | p. 4 (2 Background) |
| LIBERO procedurally generates new tasks in three steps: 1) extract behavioral templates from language annotations of human activities and generate sampled tasks described in ... | p. 4 (2 Background) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5 Experiments - extractive body cue:** Q5: How robust are different LL algorithms to task ordering in LLDM?
- **p. 8 / 5 Experiments - extractive body cue:** Therefore, we conjecture that PACKNET is not rich enough to learn on LIBEROLONG; 3) EWC works worse than SEQL, showing that the regularization on the ...
- **p. 9 / 5 Experiments - extractive body cue:** This finding highlights an important direction for future research: developing algorithms or architectures that are robust to varying task orderings.

- **Evidence anchors reviewed:** datasets p. 8 (5 Experiments), p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments), metrics p. 6 (5 Experiments), p. 6 (5 Experiments), p. 27 (Figure/Table caption), p. 31 (Figure/Table caption), p. 9 (5 Experiments), p. 7 (Figure/Table caption), baselines p. 8 (5 Experiments), p. 8 (5 Experiments), p. 43 (Figure/Table caption), p. 9 (Figure/Table caption), p. 19 (Figure/Table caption), p. 27 (Figure/Table caption), results p. 8 (5 Experiments), p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 27 (Figure/Table caption), p. 8 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (44 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 2: Performance of three lifelong algorithms and the SEQL and MTL baselines on the four task suites, where the policy is fixed to be RESNET-T. Results are averaged over ... (p. 8, Figure/Table caption).
- **Metric evidence:** All metrics are computed in terms of success rate, as previous literature has shown that the success rate is a more reliable metric than training loss for manipulation policies [42] ... (p. 6, 5 Experiments).
- **Baseline/ablation evidence:** Study on Lifelong Learning Algorithms (Q1, Q3) Table 2 reports the lifelong learning performance of the three lifelong learning algorithms, together with the SEQL and MTL baselines. (p. 8, 5 Experiments).
- **Failure/negative evidence:** Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails (p. 1, 1 Introduction).
