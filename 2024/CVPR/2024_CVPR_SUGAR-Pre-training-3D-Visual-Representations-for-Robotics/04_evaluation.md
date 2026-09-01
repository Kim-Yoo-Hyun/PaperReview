# Evaluation - SUGAR: Pre-training 3D Visual Representations for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4. Evaluation on Robotic-related Tasks), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption)): Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over 30% improvement. We fur- ther provide results on ...

## Evaluation Body Digest

- **p. 5 / 4.1. Zero-shot Object Recognition - extractive body cue:** ScanObjectNN is one of the most challenging 3D datasets, consisting of 15 common categories and 587 real-world 3D scans in the test split.
- **p. 5 / 4. Evaluation on Robotic-related Tasks - extractive body cue:** To thoroughly evaluate the pre-trained representation, we resort to three robotic-related tasks including zero-shot object recognition, referring expression grounding, and languageguided robotic manipulation.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets on ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Network architecture of SUGAR. It consists of a point cloud encoder to generate point embeddings and a prompt-based decoder that takes task-specific prompt ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Left: Five pre-training tasks for SUGAR using single- and multi-object scenes. The modules of the same color are shared. Right: The pre-trained point ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance of referring expression detection (evaluated by Acc@0.5) and referring expression segmentation (evaluated by mIoU) on the RoboRefit dataset. We use Ne = ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over 30% improvement. We ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Evaluation on Robotic-related Tasks (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over 30% improvement. ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator. | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets ... | p. 6 (Figure/Table caption) |
| 4. Evaluation on Robotic-related Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | We present datasets, downstream adaptation and quantitative results for each task in the following three sections. | p. 5 (4. Evaluation on Robotic-related Tasks) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. The results of Acc@0.25 for referring expression detection on the testing split of OCIF-Ref dataset. | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Zero-shot Object Recognition - extractive body cue:** ScanObjectNN is one of the most challenging 3D datasets, consisting of 15 common categories and 587 real-world 3D scans in the test split.
- **p. 5 / 4. Evaluation on Robotic-related Tasks - extractive body cue:** To thoroughly evaluate the pre-trained representation, we resort to three robotic-related tasks including zero-shot object recognition, referring expression grounding, and languageguided robotic manipulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce SUGAR , a pre-training framework for robotic-related tasks, which learns semantic, geometry and affor- dance on both single- and multi-object scenes. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Network architecture of SUGAR. It consists of a point cloud encoder to generate point embeddings and a prompt-based decoder that takes task-specific prompt ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Left: Five pre-training tasks for SUGAR using single- and multi-object scenes. The modules of the same color are shared. Right: The pre-trained point ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Referring expression examples on the OCID-Ref and RoboRefit dataset. The green bounding box is the groundtruth annotation, and the red bounding box is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. The results of Acc@0.25 for referring expression detection on the testing split of OCIF-Ref dataset.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance of referring expression detection (evaluated by Acc@0.5) and referring expression segmentation (evaluated by mIoU) on the RoboRefit dataset. We use Ne = ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ScanObjectNN is one of the most challenging 3D datasets, consisting of 15 common categories and 587 real-world 3D scans in the test split. | embodiment, simulator version and control stack | p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4. Evaluation on Robotic-related Tasks) |
| Task/environment | To thoroughly evaluate the pre-trained representation, we resort to three robotic-related tasks including zero-shot object recognition, referring expression grounding, and languageguided robotic manipulation. | reset, timeout, object/scene variation | p. 5 (4. Evaluation on Robotic-related Tasks) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 7 (4.3. Language-guided Robotic Manipulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 7 (4.2. Referring Expression Grounding) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 2. Network architecture of SUGAR. It consists of a point cloud encoder to generate point embeddings and a prompt-based decoder that takes task-specific ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Left: Five pre-training tasks for SUGAR using single- and multi-object scenes. The modules of the same color are shared. Right: The pre-trained ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 3. Performance of referring expression detection (evaluated by Acc@0.5) and referring expression segmentation (evaluated by mIoU) on the RoboRefit dataset. We use Ne ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over 30% improvement. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The objects are synthetic 3D models without colors. | comparison identity and matched condition | p. 5 (4.1. Zero-shot Object Recognition) |
| The task aims to classify unseen 3D objects without training on those specific categories. | comparison identity and matched condition | p. 5 (4.1. Zero-shot Object Recognition) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The objects are synthetic 3D models without colors. | component/input/data sensitivity | p. 5 (4.1. Zero-shot Object Recognition) |
| The task aims to classify unseen 3D objects without training on those specific categories. | component/input/data sensitivity | p. 5 (4.1. Zero-shot Object Recognition) |
| Table 1. Zero-shot object recognition performance on three benchmarks. The Top1 accuracy is reported if not specified otherwise. The blue colored results in brackets ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of our work are three-fold: • We present SUGAR - a framework with versatile transformer architecture for 3D point cloud ... | Figure 5. Performance of training with 10 demonstrations. (Ens m) significantly boosts the performance of the model trained from scratch with over 30% improvement. ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4. Evaluation on Robotic-related Tasks), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Table 4. Success rates of multi-task policies on 10 tasks of RLBench simulator. | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Zero-shot Object Recognition - extractive body cue:** ModelNet40 contains 40 categories and 2,468 objects in the test split.
- **p. 6 / 1) OBJ ONLY which only includes ground truth segmented - extractive body cue:** We randomly sample 4,096 points for each object and set RGB values as -0.2 (gray color) if there is no color in the point cloud.
- **p. 6 / 4.2. Referring Expression Grounding - extractive body cue:** OCID-Ref is collected in clean lab environments and consists of 58 object categories, 2,298 RGB-D images and 259,839 referring expressions for training.
- **p. 7 / 4.2. Referring Expression Grounding - extractive body cue:** Method Clutter level Total Min Med Max R3M [51] 63.30 63.87 68.34 55.33 MVP [62] 49.58 50.98 53.83 41.94 CLIP [61] 68.35 67.01 76.61 60.33 ...
- **p. 7 / 4.2. Referring Expression Grounding - extractive body cue:** Two test splits are used for evaluation: testA shares similar scenes to the training split with 1,859 scenes and 8,523 sentences; scenes and objects of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Pretraining in existing work, however, is typically limited to single objects and complete point clouds, hence, ignoring This CVPR paper is the Open Access ... | p. 1 (1. Introduction) |
| To jointly train multiple properties, we propose a versatile transformer-based model comprising a point cloud encoder and a prompt-based decoder. | p. 2 (1. Introduction) |
| SUGAR (multi) deteriorates the performance on ModelNet40 and ObjaverseLVIS datasets where the point clouds are complete, but performs better on the ScanObjectNN dataset with ... | p. 6 (1) OBJ ONLY which only includes ground truth segmented) |
| For fair comparison with previous work [36], we fix the visual encoder and only finetune the decoder in SUGAR pre-trained on the ensembled multi-object ... | p. 7 (4.2. Referring Expression Grounding) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4. Evaluation on Robotic-related Tasks), metrics p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 5 (4.1. Zero-shot Object Recognition), p. 5 (4.1. Zero-shot Object Recognition), results p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4. Evaluation on Robotic-related Tasks), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
