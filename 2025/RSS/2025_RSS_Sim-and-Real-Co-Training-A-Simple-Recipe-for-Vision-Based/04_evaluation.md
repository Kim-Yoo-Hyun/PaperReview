# Evaluation - Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p109.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p109.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (datasets), p. 6 (V. EXPERIMENTS), p. 8 (datasets)): This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% and 80%.

## Evaluation Body Digest

- **p. 6 / C. Building Task-Aware Simulation Datasets - extractive body cue:** The term "digital cousin" was recently introduced by Dai et al, [26] to describe simulation environments that are close to, but not perfectly aligned with, ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** It is important to feal-world policies with minimal real-world data note that DC data is generated in task-aware digital cousin To explore this, we evaluate ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** ‘To understand how simulation data enhances real-world Policy performance, we investigate whether exposure to diA, Effectiveness of Sim-and-Real Co-Training verse situations in simulation-ones not explicitly ...
- **p. 6 / C. Building Task-Aware Simulation Datasets - extractive body cue:** ‘The tasks and datasets presented in the previous section may have a number of large discrepancies with the real-world tasks, potentially limiting their utility.
- **p. 8 / datasets - extractive body cue:** During evaluation, we place the objects in the center of the sampling region, which are unseen positions in the real demonstrations.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We select the Countertosink?n? task on Panda and the CupPaP task on the humanoid and evaluate the policies' performance when the abject is ‘changed and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** As shown in Table Il, the policy trained without manual alignment of the simulation environment, co- solely on Rea achieves a success rate of only ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** C. Building Task-Aware Simulation Datasets (p. 6); V. EXPERIMENTS (p. 6); datasets (p. 8); 1. Generalization Experiment Details (p. 15).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% ... | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in the task, we evaluate on eight new object categories (carrot, ladle, third row of Table I policies trained on Rea? and ... | p. 7 (V. EXPERIMENTS) |
| datasets | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Tuble Il policies co-trained with DC achieve a twice higher success rate ‘compared with the policies trained solely on Real for ... | p. 8 (datasets) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Specifically, we demonstrate how co-training with simulation data enhances the real-world policy's in-domain performance (Section V-A) and improves its generalization to novel scenarios (Section ... | p. 6 (V. EXPERIMENTS) |
| datasets | EMPIRICAL / REAL-ROBOT OR HARDWARE | This result indicates that diverse simulation data substantially improve policy robustness to spatial variations. | p. 8 (datasets) |

## Dataset / Benchmark Role

- **p. 6 / C. Building Task-Aware Simulation Datasets - extractive body cue:** The term "digital cousin" was recently introduced by Dai et al, [26] to describe simulation environments that are close to, but not perfectly aligned with, ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** It is important to feal-world policies with minimal real-world data note that DC data is generated in task-aware digital cousin To explore this, we evaluate ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** ‘To understand how simulation data enhances real-world Policy performance, we investigate whether exposure to diA, Effectiveness of Sim-and-Real Co-Training verse situations in simulation-ones not explicitly ...
- **p. 6 / C. Building Task-Aware Simulation Datasets - extractive body cue:** ‘The tasks and datasets presented in the previous section may have a number of large discrepancies with the real-world tasks, potentially limiting their utility.
- **p. 8 / datasets - extractive body cue:** During evaluation, we place the objects in the center of the sampling region, which are unseen positions in the real demonstrations.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We select the Countertosink?n? task on Panda and the CupPaP task on the humanoid and evaluate the policies' performance when the abject is ‘changed and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Sim-and-Real Co-Training We show how co-training policies on real-world and simulation data can attain superior per formance in the real-robot deployment, compared to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Method Overview. Our workflow consists of three components: (1) We start with a real-world target task in mind and some prior simulation data: ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Effect of the quantity of real demonstrations. We use 8 oal of 4,000 simulation 2¢ demos and vary the total number of real ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Effect of the different co-training ratios. The co-training ratio, cis the probability of sampling from simulation data in each rminibatch. We experiment on ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: Camera alignment visualization. We visualize the
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7: Visualization of start states for our experiments. 7) We visualize the starting states of the Panda and GR-1 for our ‘experiments, including initialization ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 8: Visualization of novel object experiment set tings. We show the picture of train objects and test ob- jects of the generalization experiment conducted ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 10: MultitaskPnP visualization. We show the real- world scene setup of the four tasks in Mult iTaskPa.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The term "digital cousin" was recently introduced by Dai et al, [26] to describe simulation environments that are close to, but not perfectly aligned ... | embodiment, simulator version and control stack | p. 6 (C. Building Task-Aware Simulation Datasets), p. 7 (V. EXPERIMENTS) |
| Task/environment | It is important to feal-world policies with minimal real-world data note that DC data is generated in task-aware digital cousin To explore this, we ... | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (A. Learning Manipulation from Demonstration Data), p. 3 (B. Sim-to-Real and Sim-Real Co-Training) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 6 (1) The same robot and action spa), p. 4 (IV. Srupy Serur) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| As shown in Table Il, the policy trained without manual alignment of the simulation environment, co- solely on Rea achieves a success rate of ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| As shown in Tuble Il policies co-trained with DC achieve a twice higher success rate ‘compared with the policies trained solely on Real for ... | definition/direction/unit from same section | p. 8 (datasets) |
| Specifically, we demonstrate how co-training with simulation data enhances the real-world policy's in-domain performance (Section V-A) and improves its generalization to novel scenarios (Section ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| We select the Countertosink?n? task on Panda and the CupPaP task on the humanoid and evaluate the policies' performance when the abject is ‘changed ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| This question is particularly important because generating ‘ond row, compared to policies trained only on Rea, those roal-Coverage data in simulation is relatively easy, ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Fig. 1: Sim-and-Real Co-Training We show how co-training policies on real-world and simulation data can attain superior per formance in the real-robot deployment, compared ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| As shown in Tuble Il policies co-trained with DC achieve a twice higher success rate ‘compared with the policies trained solely on Real for ... | comparison identity and matched condition | p. 8 (datasets) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| ‘TABLE I: Effect of different simulation data in the co-training mix. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| 4: Effect of the quantity of real demonstrations. | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| As shown in Table Il, the policy trained without manual alignment of the simulation environment, co- solely on Rea achieves a success rate of ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We define these parameters in more detail and quantify them in Section IV, when we introduce the domains and tasks, and we study how ... | This on novel objects, whereas the co-tained policy significantly finding highlights the potential of leveraging readily available outperforms it with success rates of 50% ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (datasets), p. 6 (V. EXPERIMENTS), p. 8 (datasets) |
| Primary metric/result | As shown in the task, we evaluate on eight new object categories (carrot, ladle, third row of Table I policies trained on Rea? and ... | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Extending our approach to a broader set of manipulation tasks, such as high-precision insertion, and longer-horizon tasks, is left for future work. | p. 9 (VI. Limtrarions) |
| body limitation/failure cue | Applying this cotraining strategy to such tasks presents a challenge, Future work could explore the use of co-training data produced by video generation models ... | p. 9 (VI. Limtrarions) |
| body limitation/failure cue | Next, we delve into the systematic experiments that guided further investigate the robustness of this gap by training the the development of our recipe ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | The diversimulation data to enhance real-world policy performance. sity in simulation data contributes to improved generalizability Finally, in the last row of Table 1, ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | This result indicates that diverse simulation data substantially improve policy robustness to spatial variations. | p. 8 (datasets) |
| body limitation/failure cue | Fig. 12: Examples of the Video2Video model outputs with different noise strength, Left: An example video frame from the simulation | p. 17 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VI. Limtrarions - extractive body cue:** Extending our approach to a broader set of manipulation tasks, such as high-precision insertion, and longer-horizon tasks, is left for future work.
- **p. 9 / VI. Limtrarions - extractive body cue:** Applying this cotraining strategy to such tasks presents a challenge, Future work could explore the use of co-training data produced by video generation models and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Next, we delve into the systematic experiments that guided further investigate the robustness of this gap by training the the development of our recipe (Section ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The diversimulation data to enhance real-world policy performance. sity in simulation data contributes to improved generalizability Finally, in the last row of Table 1, policies ...
- **p. 8 / datasets - extractive body cue:** This result indicates that diverse simulation data substantially improve policy robustness to spatial variations.
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Examples of the Video2Video model outputs with different noise strength, Left: An example video frame from the simulation

- **PDF anchors reviewed:** datasets p. 6 (C. Building Task-Aware Simulation Datasets), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (C. Building Task-Aware Simulation Datasets), p. 8 (datasets), p. 8 (V. EXPERIMENTS), metrics p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (datasets), p. 6 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), baselines p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 8 (datasets), results p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (datasets), p. 6 (V. EXPERIMENTS), p. 8 (datasets).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
