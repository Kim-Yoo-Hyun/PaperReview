# Evaluation - SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1407_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01407.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), p. 10 (5 Experiments), p. 12 (5 Experiments)): However, when presented with extensive training data in SceneVerse, the results of our model without additional fine-tuning, i.e., Ours (pre-train), significantly improves and already achieves state-of-the-art results on benchmarks like ...

## Evaluation Body Digest

- **p. 11 / 5 Experiments - extractive body cue:** We mainly consider 2 specific transfer settings in our experiments: (i) zero-shot: models trained by removing all the scenes from the target dataset, tested on ...
- **p. 11 / 5 Experiments - extractive body cue:** We create SceneVerse-val using 8.5K annotated object referrals of 271 scenes in MultiScan, and randomly split the scenes following a 4:1 train / test split ...
- **p. 10 / 5 Experiments - extractive body cue:** Initially, when GPS is trained directly on the training sets of benchmark datasets, labeled as Ours (scratch), it underperforms compared to existing models that employ ...
- **p. 12 / 5 Experiments - extractive body cue:** We pre-train GPS on SceneVerse and fine-tune the model on the 3D-QA dataset to compare with state-of-the-art models. ‚ In the OV-Seg task, as GPS ...
- **p. 12 / 5 Experiments - extractive body cue:** As SceneVerse currently contains only descriptions of objects and scenes, we believe involving more types of language descriptions (e.g., question-answer pairs, dialogues) is a promising ...
- **p. 14 / 5 Experiments - extractive body cue:** 8, models trained on synthetic subsets demonstrate remarkable performance on their corresponding test sets while suffering when transferred to real or other synthetic scenes.
- **p. 10 / 5 Experiments - extractive body cue:** 2, GPS trained on SceneVerse achieves state-of-the-art results on all existing 3D-VL grounding benchmarks.
- **p. 13 / 5 Experiments - extractive body cue:** We assess the performance of models trained using various scene-text sources, specifically focusing on their performance in the ScanRefer dataset without additional fine-tuning.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, when presented with extensive training data in SceneVerse, the results of our model without additional fine-tuning, i.e., Ours (pre-train), significantly improves and already ... | p. 10 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5, our model achieves state-of-the-art results on both benchmarks, outperforming recent strong pre-training-based baselines like 3D-VisTA and 3D-LLM. | p. 12 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | This contributes significantly to the substantial improvement over the zero-shot performance. | p. 11 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, there is a significantly improved performance when comparing models trained on SceneVerse in a zero-shot manner to those trained from scratch. | p. 11 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, GPS trained on SceneVerse achieves state-of-the-art results on all existing 3D-VL grounding benchmarks. | p. 10 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 11 / 5 Experiments - extractive body cue:** We mainly consider 2 specific transfer settings in our experiments: (i) zero-shot: models trained by removing all the scenes from the target dataset, tested on ...
- **p. 11 / 5 Experiments - extractive body cue:** We create SceneVerse-val using 8.5K annotated object referrals of 271 scenes in MultiScan, and randomly split the scenes following a 4:1 train / test split ...
- **p. 10 / 5 Experiments - extractive body cue:** Initially, when GPS is trained directly on the training sets of benchmark datasets, labeled as Ours (scratch), it underperforms compared to existing models that employ ...
- **p. 12 / 5 Experiments - extractive body cue:** We pre-train GPS on SceneVerse and fine-tune the model on the 3D-QA dataset to compare with state-of-the-art models. ‚ In the OV-Seg task, as GPS ...
- **p. 12 / 5 Experiments - extractive body cue:** As SceneVerse currently contains only descriptions of objects and scenes, we believe involving more types of language descriptions (e.g., question-answer pairs, dialogues) is a promising ...
- **p. 14 / 5 Experiments - extractive body cue:** 8, models trained on synthetic subsets demonstrate remarkable performance on their corresponding test sets while suffering when transferred to real or other synthetic scenes.
- **p. 10 / 5 Experiments - extractive body cue:** 2, GPS trained on SceneVerse achieves state-of-the-art results on all existing 3D-VL grounding benchmarks.
- **p. 13 / 5 Experiments - extractive body cue:** We assess the performance of models trained using various scene-text sources, specifically focusing on their performance in the ScanRefer dataset without additional fine-tuning.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of SceneVerse. A million-scale 3D vision-language dataset that comprises over 68K various 3D indoor scenes and 2.5M aligned scene-language pairs in the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison of SceneVerse with existing 3DVL Datasets. Scen- eVerse expands the data scale of prior work by order of magnitude. "VG" stands for ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: SceneVerse collection and statistics. Given a 3D scene (a), our automated pipeline (c) generates three types of description including scene caption, object caption ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of GPS model. We use contrastive alignment at three levels Lobj, Lscene, and Lref and a masked language modeling objective LMLM for ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: 3D visual grounding results on Nr3D, Sr3D, and ScanRefer. We use "pre-train" for our model trained on SceneVerse w/o additional fine-tuning, and "fine-tune" ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Zero-shot transfer on existing benchmarks. "SR" stands for ScanRefer.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 4: Zero-shot transfer on Scen- eVerse-val. Evaluation uses GT object proposals following Nr3D/Sr3D.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5: 3D question answering re- sults on ScanQA and SQA3D. We re- port EM@1 score on ScanQA and SQA3D evaluation sets.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We mainly consider 2 specific transfer settings in our experiments: (i) zero-shot: models trained by removing all the scenes from the target dataset, tested ... | embodiment, simulator version and control stack | p. 11 (5 Experiments), p. 11 (5 Experiments) |
| Task/environment | We create SceneVerse-val using 8.5K annotated object referrals of 271 scenes in MultiScan, and randomly split the scenes following a 4:1 train / test ... | reset, timeout, object/scene variation | p. 11 (5 Experiments), p. 10 (5 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 7 (3. A bed with a striped comforter. (0.83)) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Body text (section not recovered)), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This result underscores the dataintensive nature of the contrastive alignment paradigm. | definition/direction/unit from same section | p. 10 (5 Experiments) |
| These results underscore the strong potential of both the SceneVerse and GPS for 3D-VL tasks. | definition/direction/unit from same section | p. 10 (5 Experiments) |
| Consequently, this underscores its potential as a go-to pre-training dataset for 3D-VL tasks. ‚ The impact of our extensive collection and scalable generation of ... | definition/direction/unit from same section | p. 11 (5 Experiments) |
| [94] and report the mIoU and mAcc score. | definition/direction/unit from same section | p. 12 (5 Experiments) |
| 8, models trained on synthetic subsets demonstrate remarkable performance on their corresponding test sets while suffering when transferred to real or other synthetic scenes. | definition/direction/unit from same section | p. 14 (5 Experiments) |
| Table 5: 3D question answering re- sults on ScanQA and SQA3D. We re- port EM@1 score on ScanQA and SQA3D evaluation sets. | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| In the following sections, we describe in detail the model performance regarding these key topics. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| This contributes significantly to the substantial improvement over the zero-shot performance. | definition/direction/unit from same section | p. 11 (5 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5, our model achieves state-of-the-art results on both benchmarks, outperforming recent strong pre-training-based baselines like 3D-VisTA and 3D-LLM. | comparison identity and matched condition | p. 12 (5 Experiments) |
| More importantly, these variants of our model already achieve state-of-the-art results compared with previous baselines. | comparison identity and matched condition | p. 13 (5 Experiments) |
| Moreover, the dataset-specific fine-tuned model, i.e., Ours (fine-tuned), consistently outperforms existing baselines with only a simple projection MLP added on top of the pretrained ... | comparison identity and matched condition | p. 10 (5 Experiments) |
| For comparisons, we compare with existing baselines by providing the results of pre-trained GPS and dataset-specific fine-tuned GPS. | comparison identity and matched condition | p. 10 (5 Experiments) |
| In zero-shot transfer scenarios, our model consistently outperforms 3D-VisTA across established benchmarks and SceneVerse-val. | comparison identity and matched condition | p. 11 (5 Experiments) |
| 4 with the following key observations: ‚ Our GPS model demonstrates superior generalization to unseen scenes compared to the 3D-VisTA model. | comparison identity and matched condition | p. 11 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Moreover, the dataset-specific fine-tuned model, i.e., Ours (fine-tuned), consistently outperforms existing baselines with only a simple projection MLP added on top of the pretrained ... | component/input/data sensitivity | p. 10 (5 Experiments) |
| However, when presented with extensive training data in SceneVerse, the results of our model without additional fine-tuning, i.e., Ours (pre-train), significantly improves and already ... | component/input/data sensitivity | p. 10 (5 Experiments) |
| We assess the performance of models trained using various scene-text sources, specifically focusing on their performance in the ScanRefer dataset without additional fine-tuning. | component/input/data sensitivity | p. 13 (5 Experiments) |
| 9, we test different models on the SceneVerse-val without additional fine-tuning. | component/input/data sensitivity | p. 14 (5 Experiments) |
| When removing the object-level alignment objective, we learn the object point cloud encoder with the referral-object-level alignment and without pre-training. | component/input/data sensitivity | p. 14 (5 Experiments) |
| We pre-train GPS on SceneVerse and fine-tune the model on the 3D-QA dataset to compare with state-of-the-art models. ‚ In the OV-Seg task, as ... | component/input/data sensitivity | p. 12 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To confront these challenges, we propose SceneVerse, the first millionscale dataset aimed at advancing 3D vision-language (3D-VL) learning for grounded scene understanding. | However, when presented with extensive training data in SceneVerse, the results of our model without additional fine-tuning, i.e., Ours (pre-train), significantly improves and already ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), p. 10 (5 Experiments), p. 12 (5 Experiments) |
| Primary metric/result | 5, our model achieves state-of-the-art results on both benchmarks, outperforming recent strong pre-training-based baselines like 3D-VisTA and 3D-LLM. | numeric claim only at cited anchor | p. 12 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 11 / 5 Experiments - extractive body cue:** We create SceneVerse-val using 8.5K annotated object referrals of 271 scenes in MultiScan, and randomly split the scenes following a 4:1 train / test split ...
- **p. 7 / 3. A bed with a striped comforter. (0.83) - extractive body cue:** Scaling 3D Vision-Language Learning for Grounded Scene Understanding 7 Scene Captioning The scene-level captions emphasize global information, portraying the key objects in the scene along ...
- **p. 7 / 3. A bed with a striped comforter. (0.83) - extractive body cue:** The dataset contains 1.5M object instances ranging in 2290 object categories.
- **p. 7 / 3. A bed with a striped comforter. (0.83) - extractive body cue:** 4.1 Object-level Grounding Given a 3D scene point cloud S, we use an off-the-shelf 3D object segmentation model to decompose it into a bag of ...
- **p. 8 / 3. A bed with a striped comforter. (0.83) - extractive body cue:** 4.2 Scene-level Grounding With aligned object features, we encode the scene by incorporating object spatial locations into the extracted object features.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Due to the page limit, we direct readers to the supplementary for implementation details, qualitative results, and more experimental analyses. | p. 9 (5 Experiments) |
| When removing the object-level alignment objective, we learn the object point cloud encoder with the referral-object-level alignment and without pre-training. | p. 14 (5 Experiments) |
| 4.2 Scene-level Grounding With aligned object features, we encode the scene by incorporating object spatial locations into the extracted object features. | p. 8 (3. A bed with a striped comforter. (0.83)) |
| We use contrastive alignment at three levels Lobj, Lscene, and Lref and a masked language modeling objective LMLM for model learning. object features tf ... | p. 8 (3. A bed with a striped comforter. (0.83)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 11 (5 Experiments), p. 11 (5 Experiments), p. 10 (5 Experiments), p. 12 (5 Experiments), p. 12 (5 Experiments), p. 14 (5 Experiments), metrics p. 10 (5 Experiments), p. 10 (5 Experiments), p. 11 (5 Experiments), p. 12 (5 Experiments), p. 14 (5 Experiments), p. 12 (Figure/Table caption), baselines p. 12 (5 Experiments), p. 13 (5 Experiments), p. 10 (5 Experiments), p. 10 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), results p. 10 (5 Experiments), p. 12 (5 Experiments), p. 11 (5 Experiments), p. 11 (5 Experiments), p. 10 (5 Experiments), p. 12 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
