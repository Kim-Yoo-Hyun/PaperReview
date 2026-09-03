# Evaluation - CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 8 (4.5. Ablation Study), p. 7 (4.3. Comparisons with SOTA Methods on Close-Set), p. 7 (4.4. Predicting Novel Classes), p. 5 (4. Experiments)): Despite introducing additional information, our model achieves a significant performance boost without a substantial increase in time (24 to 30).

## Evaluation Body Digest

- **p. 5 / 4.1. Task Description - extractive body cue:** The training set of 3DSSG [47] contains 3582 scenes, while the testing set comprises 548 scenes.
- **p. 5 / 4.1. Task Description - extractive body cue:** The dataset includes 160 object classes and 27 predicate classes.
- **p. 6 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** Head-tail and Unseen Triple with Supervised: As evidenced in Table 2, our approach achieves SOTA performance when benchmarked against SGFN and VL-SAT for the infrequent ...
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Comparisons with state-of-the-arts on the 3DSSG dataset.
- **p. 7 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** Qualitative Results with Supervised: Figure 3 depicts four challenging scenes from diverse indoor rooms, including bedrooms, living rooms, and toilets.
- **p. 7 / 4.4. Predicting Novel Classes - extractive body cue:** This approach gleans substantial knowledge from realistic open-world scenarios, culminating in transferable 3DSG representations that outperform supervised methods on the more constrained 3DSSG dataset.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** In this section, we show the ablation performance on the 3DSSG dataset in Table 5.
- **p. 8 / 4.4. Predicting Novel Classes - extractive body cue:** Qualitative results are drawn from both VL-SAT [48] and our method utilizing the ScanNet dataset [8].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.2. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Comparisons with SOTA Methods on Close-Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite introducing additional information, our model achieves a significant performance boost without a substantial increase in time (24 to 30). | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| 4.3. Comparisons with SOTA Methods on Close-Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | Head-tail and Unseen Triple with Supervised: As evidenced in Table 2, our approach achieves SOTA performance when benchmarked against SGFN and VL-SAT for the ... | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | In EXP 11, fine-tuning the prediction head in VL-SAT with a limited dataset enhanced the performance, making them comparable to those achieved with supervised ... | p. 8 (4.5. Ablation Study) |
| 4.3. Comparisons with SOTA Methods on Close-Set | EMPIRICAL / SOURCE-REPORTED EVALUATION | Qualitative examples of the improvement in supervised 3DSGG. | p. 7 (4.3. Comparisons with SOTA Methods on Close-Set) |
| 4.4. Predicting Novel Classes | EMPIRICAL / SOURCE-REPORTED EVALUATION | This approach gleans substantial knowledge from realistic open-world scenarios, culminating in transferable 3DSG representations that outperform supervised methods on the more constrained 3DSSG dataset. | p. 7 (4.4. Predicting Novel Classes) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Task Description - extractive body cue:** The training set of 3DSSG [47] contains 3582 scenes, while the testing set comprises 548 scenes.
- **p. 5 / 4.1. Task Description - extractive body cue:** The dataset includes 160 object classes and 27 predicate classes.
- **p. 6 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** Head-tail and Unseen Triple with Supervised: As evidenced in Table 2, our approach achieves SOTA performance when benchmarked against SGFN and VL-SAT for the infrequent ...
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Comparisons with state-of-the-arts on the 3DSSG dataset.
- **p. 7 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** Qualitative Results with Supervised: Figure 3 depicts four challenging scenes from diverse indoor rooms, including bedrooms, living rooms, and toilets.
- **p. 7 / 4.4. Predicting Novel Classes - extractive body cue:** This approach gleans substantial knowledge from realistic open-world scenarios, culminating in transferable 3DSG representations that outperform supervised methods on the more constrained 3DSSG dataset.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** In this section, we show the ablation performance on the 3DSSG dataset in Table 5.
- **p. 8 / 4.4. Predicting Novel Classes - extractive body cue:** Qualitative results are drawn from both VL-SAT [48] and our method utilizing the ScanNet dataset [8].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (a) Difference in training: Previous 3DSGG models trained on closed-set classes by fully supervised [12, 48, 61]. Our method trains a 3DSG feature ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Architecture of the CCL-3DSGG. The CCL-3DSGG architecture begins with inputting image-text pairs and unlabeled 3D point clouds, aiming to train the 3DSG feature ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparisons with state-of-the-arts on the 3DSSG dataset. Because the 3DSGG task inputs the instance segmentation, we only compute the mean of the two ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Following the VL-SAT, the 26 predicate classes in the 3DSSG dataset are categorized into head, body, and tail parts based on the predicate ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Unsupervised experimental results of mR on the 3DSSG dataset. w/o CL means without classification losses.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative examples of the improvement in supervised 3DSGG. On the right side of each scene, the result of the VL-SAT [48] is at ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Open-vocabulary 3DSGG and Zero-shot 3DSGG of R@{50/100} on the 3DSSG dataset.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Ablation studies on CCL-3DSGG with unsupervised. Exp Module PREDCLS Object mR@20 mR@50 mR@100 A@1 A@5 1 our full method

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The training set of 3DSSG [47] contains 3582 scenes, while the testing set comprises 548 scenes. | embodiment, simulator version and control stack | p. 5 (4.1. Task Description), p. 5 (4.1. Task Description) |
| Task/environment | The dataset includes 160 object classes and 27 predicate classes. | reset, timeout, object/scene variation | p. 5 (4.1. Task Description), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3. Methods), p. 4 (3.1. Cross-modality Features Extraction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3.2. Cross-Modality Contrastive Losses), p. 3 (3.1. Cross-modality Features Extraction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These findings underscore the efficacy of our pretraining strategy, leveraging naturally occurring free-form captions and images. | definition/direction/unit from same section | p. 7 (4.4. Predicting Novel Classes) |
| Table 2. Following the VL-SAT, the 26 predicate classes in the 3DSSG dataset are categorized into head, body, and tail parts based on the ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Our approach demonstrates SOTA even in unsupervised, achieving an average Recall of 53.85 when compared to supervised methods on OV settings. | definition/direction/unit from same section | p. 7 (4.4. Predicting Novel Classes) |
| In EXP 4, when we eliminated the I3D loss, we observed a performance dip. | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| Influence of Object and Predicate Annotation: In both EXP 8 and EXP 9, we incorporated the object loss L3d obj and predicate loss L3d ... | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| The initial learning rate for the backbone is 0.001. | definition/direction/unit from same section | p. 5 (4.2. Implementation Details) |
| In this section, we evaluate the performance of CCL3DSGG on two datasets: 3DSSG [47] and ScanNet [8]. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Specifically, for SGPN, only the object loss was retained. | definition/direction/unit from same section | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparisons with state-of-the-arts on the 3DSSG dataset. | comparison identity and matched condition | p. 6 (4.2. Implementation Details) |
| Our approach demonstrates SOTA even in unsupervised, achieving an average Recall of 53.85 when compared to supervised methods on OV settings. | comparison identity and matched condition | p. 7 (4.4. Predicting Novel Classes) |
| This approach gleans substantial knowledge from realistic open-world scenarios, culminating in transferable 3DSG representations that outperform supervised methods on the more constrained 3DSSG dataset. | comparison identity and matched condition | p. 7 (4.4. Predicting Novel Classes) |
| We provide a detailed account of the task description and experimental settings, compare our model to SOTA methods, and conduct ablation studies to emphasize ... | comparison identity and matched condition | p. 5 (4. Experiments) |
| Moreover, we reproduce the VL-SAT [48], KISGP [61], and SGPN [47] for comparison in this study. | comparison identity and matched condition | p. 5 (4.2. Implementation Details) |
| Unsupervised experimental results of mR on the 3DSSG dataset. w/o CL means without classification losses. | comparison identity and matched condition | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We provide a detailed account of the task description and experimental settings, compare our model to SOTA methods, and conduct ablation studies to emphasize ... | component/input/data sensitivity | p. 5 (4. Experiments) |
| Unsupervised experimental results of mR on the 3DSSG dataset. w/o CL means without classification losses. | component/input/data sensitivity | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| Despite introducing additional information, our model achieves a significant performance boost without a substantial increase in time (24 to 30). | component/input/data sensitivity | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| Ablation studies on CCL-3DSGG with unsupervised. | component/input/data sensitivity | p. 7 (4.4. Predicting Novel Classes) |
| In this section, we show the ablation performance on the 3DSSG dataset in Table 5. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| In EXP 10, we employed the prediction head from VL-SAT to infer features without prompts during the testing phase. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The primary contributions are summarized as: • We propose the new and practical tasks of OV 3DSGG. | Despite introducing additional information, our model achieves a significant performance boost without a substantial increase in time (24 to 30). | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 8 (4.5. Ablation Study), p. 7 (4.3. Comparisons with SOTA Methods on Close-Set), p. 7 (4.4. Predicting Novel Classes), p. 5 (4. Experiments) |
| Primary metric/result | Head-tail and Unseen Triple with Supervised: As evidenced in Table 2, our approach achieves SOTA performance when benchmarked against SGFN and VL-SAT for the ... | numeric claim only at cited anchor | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Task Description - extractive body cue:** The training set of 3DSSG [47] contains 3582 scenes, while the testing set comprises 548 scenes.
- **p. 5 / 4.1. Task Description - extractive body cue:** The dataset includes 160 object classes and 27 predicate classes.
- **p. 5 / 4.2. Implementation Details - extractive body cue:** Training is conducted using the Adam optimizer [24], with a batch size of 8, over 100 epochs.
- **p. 5 / 4.2. Implementation Details - extractive body cue:** The training of our full method takes approximately 48-50 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations: There are several limitations of our work and still much to do to realize the full potential of the proposed approach. | p. 8 (5. Conclusion) |
| body limitation/failure cue | For better viewing, we only show failure cases. | p. 7 (4.3. Comparisons with SOTA Methods on Close-Set) |
| body limitation/failure cue | In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for 3DSGG where ground truth is ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. (a) Difference in training: Previous 3DSGG models trained on closed-set classes by fully supervised [12, 48, 61]. Our method trains a 3DSG ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | These results substantiate that our model furnishes more robust 3DSG feature representations, enhancing its generalization Table 3. | p. 6 (4.3. Comparisons with SOTA Methods on Close-Set) |
| body limitation/failure cue | Meanwhile, both unseen and seen triplets from the validation set are used to evaluate the robustness of our trained 3DSG feature extractor. | p. 6 (4.2. Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is conducted using the Adam optimizer [24], with a batch size of 8, over 100 epochs. | p. 5 (4.2. Implementation Details) |
| The initial learning rate for the backbone is 0.001. | p. 5 (4.2. Implementation Details) |
| Because the 3DSGG task inputs the instance segmentation, we only compute the mean of the two tasks of SGCLS and PREDCLS. | p. 6 (4.2. Implementation Details) |
| Subsequently, the text is processed by text encoder Tθ of CLIP to obtain text feature FT . | p. 4 (3.1. Cross-modality Features Extraction) |
| Drawing from the VL-SAT method described in [48], we use a pretrained CLIP vision encoder Iθ to produce features for multi-view images. | p. 4 (3.1. Cross-modality Features Extraction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations: There are several limitations of our work and still much to do to realize the full potential of the proposed approach.
- **p. 7 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** For better viewing, we only show failure cases.
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for 3DSGG where ground truth is not ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. (a) Difference in training: Previous 3DSGG models trained on closed-set classes by fully supervised [12, 48, 61]. Our method trains a 3DSG feature ...
- **p. 6 / 4.3. Comparisons with SOTA Methods on Close-Set - extractive body cue:** These results substantiate that our model furnishes more robust 3DSG feature representations, enhancing its generalization Table 3.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Meanwhile, both unseen and seen triplets from the validation set are used to evaluate the robustness of our trained 3DSG feature extractor.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Task Description), p. 5 (4.1. Task Description), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.2. Implementation Details), p. 7 (4.3. Comparisons with SOTA Methods on Close-Set), p. 7 (4.4. Predicting Novel Classes), metrics p. 7 (4.4. Predicting Novel Classes), p. 6 (Figure/Table caption), p. 7 (4.4. Predicting Novel Classes), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 5 (4.2. Implementation Details), baselines p. 6 (4.2. Implementation Details), p. 7 (4.4. Predicting Novel Classes), p. 7 (4.4. Predicting Novel Classes), p. 5 (4. Experiments), p. 5 (4.2. Implementation Details), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), results p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 6 (4.3. Comparisons with SOTA Methods on Close-Set), p. 8 (4.5. Ablation Study), p. 7 (4.3. Comparisons with SOTA Methods on Close-Set), p. 7 (4.4. Predicting Novel Classes), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
