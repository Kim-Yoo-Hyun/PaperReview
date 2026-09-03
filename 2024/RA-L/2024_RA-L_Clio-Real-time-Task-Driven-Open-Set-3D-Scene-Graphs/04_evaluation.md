# Evaluation - Clio: Real-time Task-Driven Open-Set 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2404.13696; PDF retrieval source: https://arxiv.org/pdf/2404.13696. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS)): Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot failed to actually grasp a correctly identified object.

## Evaluation Body Digest

- **p. 8 / VI. EXPERIMENTS - extractive body cue:** During the experiments, the robot constructs a map with Clio in real-time while exploring a scene, and then is tasked to navigate to and pick ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** To test Clio in realistic and diverse scenes, we collect four datasets, in an office, an apartment, a cubicle, and a large-scale university building, which ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-set semantic segmentation experiments on 8 scenes from the Replica [17] dataset.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** For the Office, Apartment, and Cubicle datasets we manually annotate ground truth 3D bounding boxes for objects associated to the given set of tasks.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Results of locating objects of interest via open-set task queries for three datasets using CLIP ViT-L/14.
- **p. 8 / VI. EXPERIMENTS - extractive body cue:** 8 IEEE ROBOTICS AND AUTOMATION LETTERS.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated objects, ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** We use the precision and recall metrics presented in [7] to assess the geometric accuracy of the predicted rooms of our proposed CLIP embedding vector ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VI. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot failed to ... | p. 8 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once ... | p. 7 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Firstly, we observe that task-informed approaches (shaded blue rows in Table I) lead to improved open-set precision and retain a much smaller amount of ... | p. 6 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | To improve the reliability of CLIP given the low texture regions of the Replica dataset, we include global context CLIP vectors by incorporating dense ... | p. 7 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Breakdown of grasp results for the 21 object grasp attempts performed by Spot. "Wrong object" refers to the wrong Clio object being selected, "Detection ... | p. 8 (VI. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / VI. EXPERIMENTS - extractive body cue:** During the experiments, the robot constructs a map with Clio in real-time while exploring a scene, and then is tasked to navigate to and pick ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** To test Clio in realistic and diverse scenes, we collect four datasets, in an office, an apartment, a cubicle, and a large-scale university building, which ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-set semantic segmentation experiments on 8 scenes from the Replica [17] dataset.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** For the Office, Apartment, and Cubicle datasets we manually annotate ground truth 3D bounding boxes for objects associated to the given set of tasks.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Results of locating objects of interest via open-set task queries for three datasets using CLIP ViT-L/14.
- **p. 8 / VI. EXPERIMENTS - extractive body cue:** 8 IEEE ROBOTICS AND AUTOMATION LETTERS.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. We draw inspiration from the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Clio generates a 3D scene graph in real-time using a laptop carried by Spot. We show that Spot is able to execute grasping ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Clio's frontend takes in RGB-D sensor data and constructs the graph of object primitives, the graph of places, and the metric-semantic 3D mesh ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Examples of portions of the Cubicle dataset that require a task to provide rectification of how an object should be defined. The figure ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative examples of places clustering. The first figure shows regions that result from clustering by task prompts resembling room category labels. The second ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Breakdown of grasp results for the 21 object grasp attempts per- formed by Spot. "Wrong object" refers to the wrong Clio object being ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7. Custom open-vocabulary 3D datasets of an office floor, apartment, and cubicle. 11) something to put on a hot dog (1) 12) get can ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 8. Example 3D scene graphs for the self-collected Office, Apartment and Cubicle datasets. Scene graphs layers are drawn in the following order: objects (as ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | During the experiments, the robot constructs a map with Clio in real-time while exploring a scene, and then is tasked to navigate to and ... | embodiment, simulator version and control stack | p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Task/environment | To test Clio in realistic and diverse scenes, we collect four datasets, in an office, an apartment, a cubicle, and a large-scale university building, ... | reset, timeout, object/scene variation | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 2 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated ... | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTS) |
| We use the precision and recall metrics presented in [7] to assess the geometric accuracy of the predicted rooms of our proposed CLIP embedding ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTS) |
| Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot failed to ... | definition/direction/unit from same section | p. 8 (VI. EXPERIMENTS) |
| Results from this comparison are presented in Table III, which also includes the F1 score as a summary statistic. | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTS) |
| The second figure shows regions that result from clustering by task prompts that are a mix of potential rooms and objects. of F1 score ... | definition/direction/unit from same section | p. 8 (VI. EXPERIMENTS) |
| Since traditional metrics like precision and recall do not fully capture the performance of open-set object detection, we introduce two new metrics: open-set Recall ... | definition/direction/unit from same section | p. 6 (VI. EXPERIMENTS) |
| Fig. 2. Clio generates a 3D scene graph in real-time using a laptop carried by Spot. We show that Spot is able to execute ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ... | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| We observe task-aware baselines, Khronos-task and ConceptGraphs-task, have strictly worse open-set recall compared to their task-agnostic versions since both use awareness of the tasks ... | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once ... | comparison identity and matched condition | p. 7 (VI. EXPERIMENTS) |
| Baseline results reported from [9]. is changed to be "an image of {class}" following [9]. | comparison identity and matched condition | p. 7 (VI. EXPERIMENTS) |
| On the other hand, semantically similar regions that are connected, as present in the Office, lead to under-segmentation and lower recall compared to Hydra ... | comparison identity and matched condition | p. 8 (VI. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ... | component/input/data sensitivity | p. 6 (VI. EXPERIMENTS) |
| To show the importance of being task-driven, we further include task-aware versions of the baselines: Khronos-task and ConceptGraphs-task that take the results of Khronos ... | component/input/data sensitivity | p. 6 (VI. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. | Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot failed to ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Primary metric/result | First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once ... | numeric claim only at cited anchor | p. 7 (VI. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We use CLIP model ViT-L/14 and generate results with an RTX 3090 GPU and Intel i9-12900K CPU.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The Office, Apartment, and Cubicle datasets have 33, 28, and 18 objects of interest respectively.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-set semantic segmentation experiments on 8 scenes from the Replica [17] dataset.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Dataset Method Precision↑ Recall↑ F1↑ Apartment Hydra 0.93 ± 0.01 0.87 ± 0.01 0.90 ± 0.00 Clio (closest) 0.87 ± 0.06 0.78 ± 0.02 0.82 ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The results in Table III are averaged over 5 trials, and standard deviation of all metrics is reported.
- **p. 8 / VI. EXPERIMENTS - extractive body cue:** We perform 7 trials of a mobile manipulation experiment.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite the encouraging experimental results, our approach has multiple limitations. | p. 8 (VII. LIMITATIONS) |
| body limitation/failure cue | First, while our method is zero-shot and is not bound to any particular foundation model, it does inherit some limitations from the foundation models ... | p. 8 (VII. LIMITATIONS) |
| body limitation/failure cue | Closed-Set Object Evaluation While Clio is designed for open-set detection, we include results on the closed-set Replica [17] dataset using the evaluation method performed ... | p. 7 (VI. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run Clio on a laptop capable of being mounted on the robot that is equipped with an Intel i913950HX CPU with 24 cores, ... | p. 8 (VI. EXPERIMENTS) |
| We use CLIP model ViT-L/14 and generate results with an RTX 3090 GPU and Intel i9-12900K CPU. | p. 6 (VI. EXPERIMENTS) |
| As our queries do not include negation or multi-step affordances, we run ConceptGraphs with only CLIP in place of LLava+GPT, as CLIP was shown ... | p. 6 (VI. EXPERIMENTS) |
| The results in Table III are averaged over 5 trials, and standard deviation of all metrics is reported. | p. 7 (VI. EXPERIMENTS) |
| Third, we observe that Clio is able to run in a fraction of a second and is around 6 times faster than ConceptGraphs; Khronos ... | p. 7 (VI. EXPERIMENTS) |
| We present a breakdown of the 21 trials in Fig. | p. 8 (VI. EXPERIMENTS) |
| The third contribution is to integrate our task-driven clustering algorithm into a real-time pipeline, named Clio, that constructs a hierarchical 3D scene graph of ... | p. 2 (Abstract) |
| The pseudocode of the algorithm in given in Appendix A. | p. 4 (IV. TASK-DRIVEN CLUSTERING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VII. LIMITATIONS - extractive body cue:** Despite the encouraging experimental results, our approach has multiple limitations.
- **p. 8 / VII. LIMITATIONS - extractive body cue:** First, while our method is zero-shot and is not bound to any particular foundation model, it does inherit some limitations from the foundation models used ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-Set Object Evaluation While Clio is designed for open-set detection, we include results on the closed-set Replica [17] dataset using the evaluation method performed by ...

- **Evidence anchors reviewed:** datasets p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), metrics p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), baselines p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), results p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once on entire graph takes approximately 30 ... (p. 7, VI. EXPERIMENTS).
- **Metric evidence:** We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated objects, total number of estimated objects ... (p. 6, VI. EXPERIMENTS).
- **Baseline/ablation evidence:** In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, which is essentially Clio without ... (p. 6, VI. EXPERIMENTS).
- **Failure/negative evidence:** Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the "Wrong Object" failure category). (p. 8, VI. EXPERIMENTS).
