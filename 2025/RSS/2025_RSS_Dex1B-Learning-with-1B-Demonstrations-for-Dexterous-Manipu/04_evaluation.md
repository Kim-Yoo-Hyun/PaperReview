# Evaluation - Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p106.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p106.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (B. Dataset Analysis), p. 6 (A. Grasping Synthesis Evaluation), p. 6 (A. Grasping Synthesis Evaluation), p. 8 (B. Dataset Analysis), p. 7 (B. Dataset Analysis), p. 7 (B. Dataset Analysis)): Although LD slightly increases the penetration value, it significantly contributes to an improved success rate and Qi score, highlighting its importance in achieving reliable grasps.

## Evaluation Body Digest

- **p. 7 / B. Dataset Analysis - extractive body cue:** We benchmark two methods for grasping and auticuation tasks on our datasets, and compare them with the
- **p. 7 / B. Dataset Analysis - extractive body cue:** ‘TABLE Ill: Benchmarks on (a) lifting tasks with Dex¥CB (7 and our datasets, and (b) articulation tasks with ARCTIC [16] and our datasets.
- **p. 6 / A. Grasping Synthesis Evaluation - extractive body cue:** Grasping is essential in most manipulation tasks, we firstly evalute the proposed method's effectiveness in grasp synthesis using the DexGraspNet [45] benchmark, We train DexSimple ...
- **p. 8 / B. Dataset Analysis - extractive body cue:** When comparing models trained on Dex1B to those trained on DexYCB/ARCTIC, we ‘consistently find that the former outperforms the latter across tasks, baselines and splits. ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Then, we provide details on the synthesized Dex 1B demonstration dataset and compare it with human-annotated demonstration datasets on both lifting and articulation tasks.
- **p. 8 / B. Dataset Analysis - extractive body cue:** In contrast, the articulation task, which emphasizes trajectory execution, shows greater resilience to data reduction as it can adapt to unseen objects through a more ...
- **p. 6 / A. Grasping Synthesis Evaluation - extractive body cue:** We adhere to the metrics established in the benchmark to ensure fair comparisons with baseline methods, which are divided into two categories: ‘quality (Success Rate, ...
- **p. 8 / B. Dataset Analysis - extractive body cue:** Although LD slightly increases the penetration value, it significantly contributes to an improved success rate and Qi score, highlighting its importance in achieving reliable grasps.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 6); A. Grasping Synthesis Evaluation (p. 6); B. Dataset Analysis (p. 6); VI. REAL-WORLD EXPERIMENTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Dataset Analysis | BENCHMARK / DATASET | Although LD slightly increases the penetration value, it significantly contributes to an improved success rate and Qi score, highlighting its importance in achieving reliable ... | p. 8 (B. Dataset Analysis) |
| A. Grasping Synthesis Evaluation | BENCHMARK / DATASET | In terms of quality, DexSimple ¢with post-optimization) achieves the highest success rate (86.0%), the highest Qi soe (0.125), andthe lowest penetration (0.1) | p. 6 (A. Grasping Synthesis Evaluation) |
| A. Grasping Synthesis Evaluation | BENCHMARK / DATASET | It is worth noting, the success rate of DexSimple without post-optimization and filtering is slightly lower than that of DDG [22]; this is expected ... | p. 6 (A. Grasping Synthesis Evaluation) |
| B. Dataset Analysis | BENCHMARK / DATASET | 8, the performance degradation ratio increases as data is reduced, illustrating that the success rates of the proposed DexSimple consistently improve with ‘more training ... | p. 8 (B. Dataset Analysis) |
| B. Dataset Analysis | BENCHMARK / DATASET | We collected 62% and 61% of all trajectories from the DexYCB and ARCTIC datasets, respectively, that successfully achieve task goals We highlight the diversity ... | p. 7 (B. Dataset Analysis) |

## Dataset / Benchmark Role

- **p. 7 / B. Dataset Analysis - extractive body cue:** We benchmark two methods for grasping and auticuation tasks on our datasets, and compare them with the
- **p. 7 / B. Dataset Analysis - extractive body cue:** ‘TABLE Ill: Benchmarks on (a) lifting tasks with Dex¥CB (7 and our datasets, and (b) articulation tasks with ARCTIC [16] and our datasets.
- **p. 6 / A. Grasping Synthesis Evaluation - extractive body cue:** Grasping is essential in most manipulation tasks, we firstly evalute the proposed method's effectiveness in grasp synthesis using the DexGraspNet [45] benchmark, We train DexSimple ...
- **p. 8 / B. Dataset Analysis - extractive body cue:** When comparing models trained on Dex1B to those trained on DexYCB/ARCTIC, we ‘consistently find that the former outperforms the latter across tasks, baselines and splits. ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Then, we provide details on the synthesized Dex 1B demonstration dataset and compare it with human-annotated demonstration datasets on both lifting and articulation tasks.
- **p. 8 / B. Dataset Analysis - extractive body cue:** In contrast, the articulation task, which emphasizes trajectory execution, shows greater resilience to data reduction as it can adapt to unseen objects through a more ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The Dex1B benchmark consists of 1B generated high-quality demonstrations for grasping and articulation tasks. In the bottom row, we show the deployment results ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: DexIB demonstration collection. ‘The engine takes object assets and hand pose initialization as input, using a control- based optimization algorithm to generate the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: DexSimple Pipeline. Our model takes in hand parameters and object point clouds as fixed input for CVAE, while root
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Diverse demonstrations for objects from train/test splits. We show
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Lifting trajectory from Dex1B dataset, essen a (a) Lifting task compatison on Dex¥CB [7] and Dex!B. = o i lon ARCTIC Eval on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Probability distribution of joint values from Dex!B and DexYCB/ARCTIC. The distribution of DexIB is more evenly spread, centering around the mean joint values,
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Qualitative results for both grasping and articulation tasks. We show only the contact frame for clarity
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Scaling the number of demonstrations used for training. For both tasks, our model consistently improves with more training data,

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We benchmark two methods for grasping and auticuation tasks on our datasets, and compare them with the | embodiment, simulator version and control stack | p. 7 (B. Dataset Analysis), p. 7 (B. Dataset Analysis) |
| Task/environment | ‘TABLE Ill: Benchmarks on (a) lifting tasks with Dex¥CB (7 and our datasets, and (b) articulation tasks with ARCTIC [16] and our datasets. | reset, timeout, object/scene variation | p. 7 (B. Dataset Analysis), p. 6 (A. Grasping Synthesis Evaluation) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (7 S65 69K- Graplt), p. 5 (0 4 © _ sminge) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 5 (IV. DEXSIMPLE MopEL), p. 2 (7 S65 69K- Graplt) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We adhere to the metrics established in the benchmark to ensure fair comparisons with baseline methods, which are divided into two categories: ‘quality (Success ... | definition/direction/unit from same section | p. 6 (A. Grasping Synthesis Evaluation) |
| Although LD slightly increases the penetration value, it significantly contributes to an improved success rate and Qi score, highlighting its importance in achieving reliable ... | definition/direction/unit from same section | p. 8 (B. Dataset Analysis) |
| Without Lea, the model lacks precise spatial awareness, leading to significant failures in grasp execution On the other hand, the distance loss £0 is ... | definition/direction/unit from same section | p. 8 (B. Dataset Analysis) |
| Opt, SR, and Pen are short for Optimization, Success Rate, and Penetration, respectively | definition/direction/unit from same section | p. 6 (A. Grasping Synthesis Evaluation) |
| Compared to DexGraspNet [45], our implementation of pure optimization-based grasp generation is 30 times faster, requiring only 2 minutes to generate 2000 grasps for ... | definition/direction/unit from same section | p. 7 (B. Dataset Analysis) |
| Fig. 1: The Dex1B benchmark consists of 1B generated high-quality demonstrations for grasping and articulation tasks. In the bottom row, we show the deployment ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: DexIB demonstration collection. ‘The engine takes object assets and hand pose initialization as input, using a control- based optimization algorithm to generate ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Finally, we collect a dataset with 950 million (around 1 billion) successful trajectories. | definition/direction/unit from same section | p. 7 (B. Dataset Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| :ple outperforms baseline with a higher | comparison identity and matched condition | p. 6 (A. Grasping Synthesis Evaluation) |
| The proposed generative model, DexSimple, significantly outperforms all baseline methods. | comparison identity and matched condition | p. 6 (A. Grasping Synthesis Evaluation) |
| Models trained on Dex B consi tently outperform those trained on DexYCB/ARCTIC across various tasks, baselines, and splits | comparison identity and matched condition | p. 7 (B. Dataset Analysis) |
| When comparing models trained on Dex1B to those trained on DexYCB/ARCTIC, we ‘consistently find that the former outperforms the latter across tasks, baselines and ... | comparison identity and matched condition | p. 8 (B. Dataset Analysis) |
| Compared to DexGraspNet [45], our implementation of pure optimization-based grasp generation is 30 times faster, requiring only 2 minutes to generate 2000 grasps for ... | comparison identity and matched condition | p. 7 (B. Dataset Analysis) |
| III also demonstrates that the proposed generative method, DexSimple, achieves better performance than the regression-based BC baselines on both the relatively small DexYCB/ARCTIC dataset ... | comparison identity and matched condition | p. 8 (B. Dataset Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To investigate the effect of training data size on performance, We reduce the amount of training data and analyze its impact on the success ... | component/input/data sensitivity | p. 8 (B. Dataset Analysis) |
| Finally, ablation studies are conducted to validate our design choices. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| It is worth noting, the success rate of DexSimple without post-optimization and filtering is slightly lower than that of DDG [22]; this is expected ... | component/input/data sensitivity | p. 6 (A. Grasping Synthesis Evaluation) |
| Without Lea, the model lacks precise spatial awareness, leading to significant failures in grasp execution On the other hand, the distance loss £0 is ... | component/input/data sensitivity | p. 8 (B. Dataset Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| ‘To address the feasibility issue, we propose incorporating geometric constraints into the generative model, which significantly improves its performance, We also integrate opti mization ... | Although LD slightly increases the penetration value, it significantly contributes to an improved success rate and Qi score, highlighting its importance in achieving reliable ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (B. Dataset Analysis), p. 6 (A. Grasping Synthesis Evaluation), p. 6 (A. Grasping Synthesis Evaluation), p. 8 (B. Dataset Analysis), p. 7 (B. Dataset Analysis), p. 7 (B. Dataset Analysis) |
| Primary metric/result | In terms of quality, DexSimple ¢with post-optimization) achieves the highest success rate (86.0%), the highest Qi soe (0.125), andthe lowest penetration (0.1) | numeric claim only at cited anchor | p. 6 (A. Grasping Synthesis Evaluation) |

- Numeric sentences retained from the body:
- **p. 6 / B. Dataset Analysis - extractive body cue:** For the grasping task, we utilize all 5751 object assets collected by DexGraspNet [45] and exclude all objects that cannot stand stably on the table.
- **p. 7 / B. Dataset Analysis - extractive body cue:** Compared to DexGraspNet [45], our implementation of pure optimization-based grasp generation is 30 times faster, requiring only 2 minutes to generate 2000 grasps for 6000 ...
- **p. 7 / B. Dataset Analysis - extractive body cue:** Comparison, We demonstrate the quality of Dex1B by comparing it to two large-scale, human-annotated, trajectory-level datasets: DexYCB [7] and ARCTIC [16] DexYCB includes 20 objects, ...
- **p. 7 / B. Dataset Analysis - extractive body cue:** ARCTIC includes 10 articualtion objects with a total of 301 trajectories, We follow [51, 10] to generate robot demonstrations from the DexYCB and ARCTIC
- **p. 8 / B. Dataset Analysis - extractive body cue:** This model takes the object point cloud, current hand joint values, and poses as input to predict chunked actions for the next n - 50 ...
- **p. 5 / 0 4 © _ sminge - extractive body cue:** where {go,91.-+-+9x} denotes the sequence of hand poses along the trajectory tgesocn and we are Weights for smoothness and collision avoidance respectively, and Eyae(gi) is ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Without Lea, the model lacks precise spatial awareness, leading to significant failures in grasp execution On the other hand, the distance loss £0 is ... | p. 8 (B. Dataset Analysis) |
| body limitation/failure cue | For the grasping task, we utilize all 5751 object assets collected by DexGraspNet [45] and exclude all objects that cannot stand stably on the ... | p. 6 (B. Dataset Analysis) |
| body limitation/failure cue | dataset, including retargeting human demonstrations to robot trajectories and adding noise to generate a larger number of physically plausible demonstrations. | p. 7 (B. Dataset Analysis) |
| body limitation/failure cue | Notably, we observe that performance degradation is more pronounced for the lifting task than for the articulation task as training data decreases. | p. 8 (B. Dataset Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow the implementations ! in [45, 26) We compare with DDG [22], GraspI'TA [20], the generation module in UniDexGrasp [49] (abbreviated as UDG), ... | p. 6 (A. Grasping Synthesis Evaluation) |
| Although the optimization process is wellengineered (1,000 grasps per minutes on a single GPU), generating one billion demonstrations remains computationally expensive, Therefore, we only ... | p. 3 (7 S65 69K- Graplt) |
| Compared to DexGraspNet [45], our implementation of pure optimization-based grasp generation is 30 times faster, requiring only 2 minutes to generate 2000 grasps for ... | p. 7 (B. Dataset Analysis) |
| ur approach begins with an optimization-based method to construct a small yet high-quality seed dataset of dexter- ‘ous manipulation demonstrations. | p. 2 (1. INrRopucTION) |
| This seed dataset serves as the foundation for training a generative model to learn | p. 3 (7 S65 69K- Graplt) |
| Then the Seed dataset is used as the training data for DexSimple, else for Dex1Bfor the last iteration. | p. 4 (0 4 © _ sminge) |
| The ‘optimized hand poses are evaluated using the simulator, and the successful ones are retained as a seed dataset Generative Models for Scaling-up Demonstrations. | p. 4 (0 4 © _ sminge) |
| A. sample is drawn from this distribution and passed to the MLP decoder to reconstruct the original hand pose. | p. 5 (IV. DEXSIMPLE MopEL) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / B. Dataset Analysis - extractive body cue:** Without Lea, the model lacks precise spatial awareness, leading to significant failures in grasp execution On the other hand, the distance loss £0 is responsible ...
- **p. 6 / B. Dataset Analysis - extractive body cue:** For the grasping task, we utilize all 5751 object assets collected by DexGraspNet [45] and exclude all objects that cannot stand stably on the table.
- **p. 7 / B. Dataset Analysis - extractive body cue:** dataset, including retargeting human demonstrations to robot trajectories and adding noise to generate a larger number of physically plausible demonstrations.
- **p. 8 / B. Dataset Analysis - extractive body cue:** Notably, we observe that performance degradation is more pronounced for the lifting task than for the articulation task as training data decreases.

- **PDF anchors reviewed:** datasets p. 7 (B. Dataset Analysis), p. 7 (B. Dataset Analysis), p. 6 (A. Grasping Synthesis Evaluation), p. 8 (B. Dataset Analysis), p. 6 (V. EXPERIMENTS), p. 8 (B. Dataset Analysis), metrics p. 6 (A. Grasping Synthesis Evaluation), p. 8 (B. Dataset Analysis), p. 8 (B. Dataset Analysis), p. 6 (A. Grasping Synthesis Evaluation), p. 7 (B. Dataset Analysis), p. 1 (Figure/Table caption), baselines p. 6 (A. Grasping Synthesis Evaluation), p. 6 (A. Grasping Synthesis Evaluation), p. 7 (B. Dataset Analysis), p. 8 (B. Dataset Analysis), p. 7 (B. Dataset Analysis), p. 8 (B. Dataset Analysis), results p. 8 (B. Dataset Analysis), p. 6 (A. Grasping Synthesis Evaluation), p. 6 (A. Grasping Synthesis Evaluation), p. 8 (B. Dataset Analysis), p. 7 (B. Dataset Analysis), p. 7 (B. Dataset Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
