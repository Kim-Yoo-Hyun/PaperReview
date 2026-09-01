# Evaluation - Heterogeneous Graph Learning for Scene Graph Prediction in 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3785_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03785.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments)): Compared to the baseline model KISGP [41], our method achieves a significant performance improvement.

## Evaluation Body Digest

- **p. 10 / 4 Experiments - extractive PDF cue:** For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the same ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Following KISGP, we also pretrain the multi-scale PointNet [15] on the 3DSSG dataset and utilize the pretrained PointNets to encode the point cloud into initial ...
- **p. 14 / 4 Experiments - extractive PDF cue:** Note that, typeacc denotes the accuracy of predicted type edges among existing type edges, edge-acc denotes the accuracy of edges among all objects in a ...
- **p. 13 / 4 Experiments - extractive PDF cue:** The line chart indicates the occurrence frequency ratio for each predicate in the test set.
- **p. 11 / 4 Experiments - extractive PDF cue:** The evaluation code of KISGP is utilized to reproduce the top-k recall of the PredCls and SGCls tasks.
- **p. 11 / 4 Experiments - extractive PDF cue:** Heterogeneous Graph Learning for 3D SGP 11 Table 2: Quantitative results of the evaluated methods in PredCls tasks.
- **p. 12 / 4 Experiments - extractive PDF cue:** Qualitative Results Figure 3 shows a predicted scene graph on 3DSSG [28].
- **p. 12 / 4 Experiments - extractive PDF cue:** Therefore, it is effective to treat the 3D scene graph as a heterogeneous graph and predict predicates separately according to their belonging types.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to the baseline model KISGP [41], our method achieves a significant performance improvement. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to KISGP, our 3DHetSGP achieves significant improvements on the proximity and comparative types of predicates. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, our method outperforms KISGP on many predicates, especially on body and tail predicates, including same as, same symmetry as, lying in, and cover. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 6, our model is iteratively updated to achieve optimal scene graph predictions step-by-step. | p. 14 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | For graph structure updating, we collect predicate score results and compute type weights after the first 40 epochs. | p. 10 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiments - extractive PDF cue:** For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the same ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Following KISGP, we also pretrain the multi-scale PointNet [15] on the 3DSSG dataset and utilize the pretrained PointNets to encode the point cloud into initial ...
- **p. 14 / 4 Experiments - extractive PDF cue:** Note that, typeacc denotes the accuracy of predicted type edges among existing type edges, edge-acc denotes the accuracy of edges among all objects in a ...
- **p. 13 / 4 Experiments - extractive PDF cue:** The line chart indicates the occurrence frequency ratio for each predicate in the test set.
- **p. 11 / 4 Experiments - extractive PDF cue:** The evaluation code of KISGP is utilized to reproduce the top-k recall of the PredCls and SGCls tasks.
- **p. 11 / 4 Experiments - extractive PDF cue:** Heterogeneous Graph Learning for 3D SGP 11 Table 2: Quantitative results of the evaluated methods in PredCls tasks.
- **p. 12 / 4 Experiments - extractive PDF cue:** Qualitative Results Figure 3 shows a predicted scene graph on 3DSSG [28].
- **p. 12 / 4 Experiments - extractive PDF cue:** Therefore, it is effective to treat the 3D scene graph as a heterogeneous graph and predict predicates separately according to their belonging types.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: (a) Three different types of relationships constitute the complex 3D scene graph. The colors of edges indicate the predicate super-categories: support, proximity, and ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: Three types of relationships defined in the 3DSSG dataset [28]. Types Example Categories Num Support supported by, attached to, hanging on, . . ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our 3D heterogeneous scene graph prediction(3D-HetSGP) framework. It con- sists of two stage: (a) The HGSL stage: the graph structure is learned by ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative results of the evaluated methods in PredCls tasks. The model with * represents the results we have reproduced.
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative results of the evaluated methods in SGCls tasks. The model with * represents the results we have reproduced.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Comparison results of no graph constraint Recall@20/50/100 for Support, Proximity, Comparative types. Type Support Proximity Comparative Mean Methods
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 3: Qualitative results between ours and KISGP [41] on no graph constraint Re- call@20 for the PredCls task. Red arrows: incorrect predictions by KISGP, ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 5: Comparison results of Recall@20/50 and mean Recall@20/50 for the head, body, tail predicate classes in 3DSSG [28]. Head Body Tail Methods R@20/50 mR@20/50

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the ... | embodiment, simulator version and control stack | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | Following KISGP, we also pretrain the multi-scale PointNet [15] on the 3DSSG dataset and utilize the pretrained PointNets to encode the point cloud into ... | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 14 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For graph structure updating, we collect predicate score results and compute type weights after the first 40 epochs. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| As shown in Table 7, the type edges updated from final predicate scores are more precise than the prediction of HGSL. | definition/direction/unit from same section | p. 14 (4 Experiments) |
| Note that, typeacc denotes the accuracy of predicted type edges among existing type edges, edge-acc denotes the accuracy of edges among all objects in ... | definition/direction/unit from same section | p. 14 (4 Experiments) |
| Fig. 2: Our 3D heterogeneous scene graph prediction(3D-HetSGP) framework. It con- sists of two stage: (a) The HGSL stage: the graph structure is learned ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| We set λ = 0.1, and the focal loss is the same as SGPN [28]. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Compared to the baseline model KISGP [41], our method achieves a significant performance improvement. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| The evaluation code of KISGP is utilized to reproduce the top-k recall of the PredCls and SGCls tasks. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| The mean results across all types show that our method increases the overall performance by a significant margin. | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the baseline model KISGP [41], our method achieves a significant performance improvement. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Compared to KISGP, our 3DHetSGP achieves significant improvements on the proximity and comparative types of predicates. | comparison identity and matched condition | p. 12 (4 Experiments) |
| Furthermore, the HeterGraph (Learned) structure leads to sub-optimal performance compared to | comparison identity and matched condition | p. 13 (4 Experiments) |
| 4, our method outperforms KISGP on many predicates, especially on body and tail predicates, including same as, same symmetry as, lying in, and cover. | comparison identity and matched condition | p. 13 (4 Experiments) |
| For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| 4.2 Comparison with Related Methods Since our model is developed based on KISGP [41], we evaluate our model in PredCls/SGCls tasks against both KISGP ... | comparison identity and matched condition | p. 10 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.4 Ablation Study Heterogeneous Graph Reasoning To investigate the effectiveness of our heterogeneous graph reasoning, we report the ablation results of different graph structures ... | component/input/data sensitivity | p. 13 (4 Experiments) |
| This demonstrates that our model alleviates the long-tail distribution issue without fusing prior knowledge into the models. | component/input/data sensitivity | p. 11 (4 Experiments) |
| HeterGraph denotes heterogeneous graph structure with different connection methods: FC (Fully-connected graph, i.e., without type edges), Learned (Learned type edges from HGSL for subsequent ... | component/input/data sensitivity | p. 13 (4 Experiments) |
| Table 6: Ablation results on heterogeneous graph reasoning. Graph Structure R@20 R@50 R@100 ngcR@20 ngcR@50 ngcR@100 mR@20 mR@50 mR@100 HomoGraph(KISGP) | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 7: Ablation study on heterogeneous graph structure learning. Note that, type- acc denotes the accuracy of predicted type edges among existing type edges, ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Subsequently, we replace the type edges in the heterogeneous graph with the updated edges and train it for another 40 epochs. | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Specifically, our method consists of two stages: a heterogeneous graph structure learning (HGSL) stage and a heterogeneous graph reasoning (HGR) stage. | Compared to the baseline model KISGP [41], our method achieves a significant performance improvement. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments) |
| Primary metric/result | Compared to KISGP, our 3DHetSGP achieves significant improvements on the proximity and comparative types of predicates. | numeric claim only at cited anchor | p. 12 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive PDF cue:** The 1,482 scene graphs have a total of 48k object nodes and 544k edges.
- **p. 10 / 4 Experiments - extractive PDF cue:** For a fair comparison, we split the 1,482 scenes into 3852 sub-scenes for the training set and 548 for the test set in the same ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Each scene has 9 object nodes on average.
- **p. 10 / 4 Experiments - extractive PDF cue:** Following RIO27 annotation [2], we utilize 160 object categories and 27 predicate classes, including ‘none' relation, in our experiments.
- **p. 10 / 4 Experiments - extractive PDF cue:** We train our model on an NVIDIA GTX TITAN GPU for 40 epochs using the ADAM optimizer.
- **p. 10 / 4 Experiments - extractive PDF cue:** The GNN modules are cascaded for 3 layers in the heterogeneous graph structure learning stage and 5 layers in the heterogeneous graph reasoning stage.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, it does not mean that we have to abandon HGSL. | p. 14 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We set the initial learning rate to 0.0001, and the weight decay is set to 0.7 every ten epochs. | p. 10 (4 Experiments) |
| We train our model on an NVIDIA GTX TITAN GPU for 40 epochs using the ADAM optimizer. | p. 10 (4 Experiments) |
| We only reproduce and compare with the results of models with open-sourced code. | p. 11 (4 Experiments) |
| The evaluation code of KISGP is utilized to reproduce the top-k recall of the PredCls and SGCls tasks. | p. 11 (4 Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 4 Experiments - extractive PDF cue:** However, it does not mean that we have to abandon HGSL.

- **PDF anchors reviewed:** datasets p. 10 (4 Experiments), p. 10 (4 Experiments), p. 14 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), metrics p. 10 (4 Experiments), p. 14 (4 Experiments), p. 14 (4 Experiments), p. 6 (Figure/Table caption), p. 10 (4 Experiments), p. 11 (4 Experiments), baselines p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), results p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
