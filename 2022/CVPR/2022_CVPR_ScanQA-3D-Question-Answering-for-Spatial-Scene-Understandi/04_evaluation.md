# Evaluation - ScanQA: 3D Question Answering for Spatial Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.10482; PDF retrieval source: https://arxiv.org/pdf/2112.10482. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis), p. 8 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (Figure/Table caption), p. 15 (Figure/Table caption)): The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics.

## Evaluation Body Digest

- **p. 4 / 3.3. Dataset Statistics - extractive PDF cue:** However, as the object IDs for the test set of ScanRefer are not publicly available, we further split the validation set of ScanRefer into two-holds ...
- **p. 3 / 3.2. Question-Answer Collection - extractive PDF cue:** First, we automatically generated question-answer pairs from the referring expressions to identify objects in 3D scenes obtained from the ScanRefer dataset [10].
- **p. 3 / 3.3. Dataset Statistics - extractive PDF cue:** Considering that our dataset contains not only question-answer pairs but also 3D object localization annotations, we assume that this is the largest dataset to specify ...
- **p. 4 / 3.3. Dataset Statistics - extractive PDF cue:** We presented scenes with object IDs and names to MTurk workers for the dataset collection. used in ScanRefer.
- **p. 2 / 3. ScanQA Dataset - extractive PDF cue:** We hereby define the 3D-QA task and describe the collection of the corresponding dataset.
- **p. 7 / 5.2. Quantitative Analysis - extractive PDF cue:** Although this suggests that accurate object identification for questions indeed boosts 3DQA results, this is an oracle setting for real-world applications.
- **p. 7 / 5.2. Quantitative Analysis - extractive PDF cue:** The performance of 3D-QA on the ScanQA dataset and image caption metrics are presented in Table 3.
- **p. 2 / 3.1. 3D-QA Task - extractive PDF cue:** 1, a 3D-QA task requires models to answer a question when given all the information of a 3D

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. ScanQA Dataset (p. 2); 3.3. Dataset Statistics (p. 3); 5. Experiments (p. 5); 5.1. Experimental Setup (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Quantitative Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics. | p. 7 (5.2. Quantitative Analysis) |
| 5.2. Quantitative Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Interestingly, VoteNet+MCAN, ScanRefer+MCAN (end-to-end), and ScanQA significantly outperformed ScanRefer+MCAN (pipeline), which detects target objects related to a question using a pretrained ScanRefer and then ... | p. 7 (5.2. Quantitative Analysis) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. Qualitative results. Predicted answers are described below each figure. Predicted boxes are marked blue and the ground truth is marked green. We ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 6. Object localization performance on the ScanQA dataset experiments. The results in Table 6 show that the shared and end-to-end learning of QA, ... | p. 13 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the ... | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 3.3. Dataset Statistics - extractive PDF cue:** However, as the object IDs for the test set of ScanRefer are not publicly available, we further split the validation set of ScanRefer into two-holds ...
- **p. 3 / 3.2. Question-Answer Collection - extractive PDF cue:** First, we automatically generated question-answer pairs from the referring expressions to identify objects in 3D scenes obtained from the ScanRefer dataset [10].
- **p. 3 / 3.3. Dataset Statistics - extractive PDF cue:** Considering that our dataset contains not only question-answer pairs but also 3D object localization annotations, we assume that this is the largest dataset to specify ...
- **p. 4 / 3.3. Dataset Statistics - extractive PDF cue:** We presented scenes with object IDs and names to MTurk workers for the dataset collection. used in ScanRefer.
- **p. 2 / 3. ScanQA Dataset - extractive PDF cue:** We hereby define the 3D-QA task and describe the collection of the corresponding dataset.
- **p. 7 / 5.2. Quantitative Analysis - extractive PDF cue:** Although this suggests that accurate object identification for questions indeed boosts 3DQA results, this is an oracle setting for real-world applications.
- **p. 7 / 5.2. Quantitative Analysis - extractive PDF cue:** The performance of 3D-QA on the ScanQA dataset and image caption metrics are presented in Table 3.
- **p. 2 / 3.1. 3D-QA Task - extractive PDF cue:** 1, a 3D-QA task requires models to answer a question when given all the information of a 3D

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce the new task of question answering for 3D modeling. Given inputs of an entire 3D modeling and a linguistic question, models ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of 3D question-answering datasets. scene. Here, models use the 3D spatial information, such as RGB-D scans or point cloud data. We also ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 2. ScanQA dataset statistics. embedded this site into the MTurk task page (Fig. 2). The filtering and editing of the seed questions were con- ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Underspecified and valid questions for an office room scene. We presented scenes with object IDs and names to MTurk workers for the dataset ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The distribution of the question types by the beginning of the question writing. Overview of network architecture. To solve the 3D-QA task, we ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. ScanQA model for answering 3D environments. Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Performance comparison of question answering with image captioning metrics. e2e represents an end-to-end model. ANS OBJ LOC EM@1 EM@10 BLEU-1 BLEU-2
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Performance comparison of different experimental conditions of the ScanQA model.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, as the object IDs for the test set of ScanRefer are not publicly available, we further split the validation set of ScanRefer into ... | embodiment, simulator version and control stack | p. 4 (3.3. Dataset Statistics), p. 3 (3.2. Question-Answer Collection) |
| Task/environment | First, we automatically generated question-answer pairs from the referring expressions to identify objects in 3D scenes obtained from the ScanRefer dataset [10]. | reset, timeout, object/scene variation | p. 3 (3.2. Question-Answer Collection), p. 3 (3.3. Dataset Statistics) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4. ScanQA Model), p. 4 (4. ScanQA Model) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (4. ScanQA Model), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| For example, the leftmost case shows that a whiteboard located above a backpack could not be answered by ScanRefer+MCAN (pipeline), which localized the backpack ... | definition/direction/unit from same section | p. 8 (5.4. Qualitative Analysis) |
| Figure 1. We introduce the new task of question answering for 3D modeling. Given inputs of an entire 3D modeling and a linguistic question, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| To train the ScanQA model, we used Adam [26], a batch size of 16, and an initial learning rate of 5e-4. | definition/direction/unit from same section | p. 5 (5.1. Experimental Setup) |
| We trained the model for 30 epochs until it converged and decreased the learning rate by 0.2 times after 15 epochs. | definition/direction/unit from same section | p. 5 (5.1. Experimental Setup) |
| Table 3. Performance comparison of question answering with image captioning metrics. e2e represents an end-to-end model. ANS OBJ LOC EM@1 EM@10 BLEU-1 BLEU-2 | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Finally, we demonstrated the excellent performance of our model by visualizing qualitative examples of ScanQA, ScanRefer+MCAN (pipeline), and ground truth. | definition/direction/unit from same section | p. 8 (5.4. Qualitative Analysis) |
| Auto-generated questions also include easy questions that can be answered with common sense. | definition/direction/unit from same section | p. 3 (3.2. Question-Answer Collection) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our ScanQA model with competitive baselines VoteNet+MCAN, ScanRefer+MCAN (pipeline), and ScanRefer+MCAN (end-to-end). | comparison identity and matched condition | p. 7 (5.2. Quantitative Analysis) |
| The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics. | comparison identity and matched condition | p. 7 (5.2. Quantitative Analysis) |
| Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 11. Performance comparison for the ScanQA model with difference hidden size d (Fig. 5). Fig. 9 shows the results of the object localization ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| 5 shows the representative QA results of a baseline method and ScanQA. | comparison identity and matched condition | p. 8 (5.4. Qualitative Analysis) |
| Figure 7. Example of mesh images about a question "What color is the bathroom door?" The upper panel is RandomImage, and the lower panel ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| We will clarify this point in the section on the ablation study. | component/input/data sensitivity | p. 7 (5.2. Quantitative Analysis) |
| In addition, we observed that our 3D-QA model, ScanQA, is superior to a 2D-QA model, RandomImage+MCAN, which uses an effective pretrained model. | component/input/data sensitivity | p. 7 (5.2. Quantitative Analysis) |
| Therefore, we decided to remove such questions as much as possible. | component/input/data sensitivity | p. 3 (3.2. Question-Answer Collection) |
| This prevents models from answering questions by relying on the textual priors of the trained questions without examining the scene. | component/input/data sensitivity | p. 3 (3.1. 3D-QA Task) |
| Therefore, the ScanQA dataset includes two test sets with and without object annotations. | component/input/data sensitivity | p. 4 (3.3. Dataset Statistics) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce the new task of question answering for 3D modeling. | The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis), p. 8 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Primary metric/result | Interestingly, VoteNet+MCAN, ScanRefer+MCAN (end-to-end), and ScanQA significantly outperformed ScanRefer+MCAN (pipeline), which detects target objects related to a question using a pretrained ScanRefer and then ... | numeric claim only at cited anchor | p. 7 (5.2. Quantitative Analysis) |

- Numeric sentences retained from the body:
- **p. 3 / 3.1. 3D-QA Task - extractive PDF cue:** 3D-QA Datasets Type Question Collection Answer Collection Environment Photorealistic # 3D Scenes IQUAD Interactive Template-based Template-based AI2THOR No 30 rooms EQA Navigation Template-based Template-based House3D ...
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** We trained the model for 30 epochs until it converged and decreased the learning rate by 0.2 times after 15 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To train the ScanQA model, we used Adam [26], a batch size of 16, and an initial learning rate of 5e-4. | p. 5 (5.1. Experimental Setup) |
| We trained the model for 30 epochs until it converged and decreased the learning rate by 0.2 times after 15 epochs. | p. 5 (5.1. Experimental Setup) |
| The filtering and editing of the seed questions were conducted as follows. | p. 3 (3.2. Question-Answer Collection) |
| First, we filtered the inadequate questions from the auto-generated seed questions using basic rules. | p. 3 (3.2. Question-Answer Collection) |
| The 3D & language encoder layer transforms the question into contextualized word representations and point clouds into object proposals. | p. 4 (4. ScanQA Model) |
| To solve the 3D-QA task, we developed a ScanQA model consisting of a 3D & language encoder, 3D & language fusion, and object localization ... | p. 4 (4. ScanQA Model) |
| We applied pretrained 2D-QA models to these images and computed the answer scores for each image. | p. 6 (Model) |
| The proposed method uses some of the modules used in MCAN, such as transformer encoder and decoder layers, to create 3D and language features. | p. 6 (Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions ...

- **PDF anchors reviewed:** datasets p. 4 (3.3. Dataset Statistics), p. 3 (3.2. Question-Answer Collection), p. 3 (3.3. Dataset Statistics), p. 4 (3.3. Dataset Statistics), p. 2 (3. ScanQA Dataset), p. 7 (5.2. Quantitative Analysis), metrics p. 13 (Figure/Table caption), p. 8 (5.4. Qualitative Analysis), p. 1 (Figure/Table caption), p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup), p. 6 (Figure/Table caption), baselines p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis), p. 6 (Figure/Table caption), p. 15 (Figure/Table caption), p. 8 (5.4. Qualitative Analysis), p. 12 (Figure/Table caption), results p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis), p. 8 (Figure/Table caption), p. 13 (Figure/Table caption), p. 13 (Figure/Table caption), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
