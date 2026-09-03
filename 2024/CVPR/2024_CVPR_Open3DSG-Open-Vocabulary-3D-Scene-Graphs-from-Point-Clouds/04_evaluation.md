# Evaluation - Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption)): We also evaluate the performance of NegCLIP [52] which is supposed to have improved compositional understanding.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** However, since 3DSSG is the only dataset to provide ground truth scene graph labels, we evaluate our distilled model quantitatively on it.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The 3DSSG dataset [44] is at the time of writing this paper, the only dataset that provides semantic scene graph labels aligned with a 3D ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** 1 we compare our new zero-shot openvocabulary 3D scene graph prediction approach with both fully-supervised as well as other zero-shot baselines on the 3DSSG [44] ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** Even though the fully-supervised approaches are trained specifically on this dataset, we can handle the less-common / long-tail classes much better.
- **p. 8 / 4.4. Qualitative Results - extractive body cue:** 4, we provide qualitative results from our openvocabulary 3D scene graph prediction approach for two different scenes from ScanNet [6].
- **p. 8 / 4.5. Limitations - extractive body cue:** 3D scene graph prediction with different input modalities, object VLM, privileged ground-truth information and supervised fine-tuning. potential and advantages of open-vocabulary 3D scene graph methods.
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** We observe that while fully supervised methods demonstrate impressive accuracy on common object and predicate classes, their recall drops drastically for rare tail classes.
- **p. 8 / 4.3. Ablation studies - extractive body cue:** The nodes are queried using the 3DSSG [44] 160 class label set, while the edges are generated directly from the graph-conditioned LLM. enced by the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.4. Qualitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also evaluate the performance of NegCLIP [52] which is supposed to have improved compositional understanding. | p. 6 (4.1. Experimental Setup) |
| 4.2. Closed-set 3D scene graph prediction | EMPIRICAL / SOURCE-REPORTED EVALUATION | The caption-based approach also achieves considerably lower performances compared to our method. | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| 4.2. Closed-set 3D scene graph prediction | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, Open3DSG achieves comparable results to the first supervised 3D scene graph prediction method 3DSSG. | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| 4.3. Ablation studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3, we observe that finetuning on 3DSSG improves predicate prediction with our model. | p. 8 (4.3. Ablation studies) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Open3DSG overview. Given a point cloud and RGB-D images with their poses, we distill the knowledge of two vision-language models into our ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** However, since 3DSSG is the only dataset to provide ground truth scene graph labels, we evaluate our distilled model quantitatively on it.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The 3DSSG dataset [44] is at the time of writing this paper, the only dataset that provides semantic scene graph labels aligned with a 3D ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** 1 we compare our new zero-shot openvocabulary 3D scene graph prediction approach with both fully-supervised as well as other zero-shot baselines on the 3DSSG [44] ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** Even though the fully-supervised approaches are trained specifically on this dataset, we can handle the less-common / long-tail classes much better.
- **p. 8 / 4.4. Qualitative Results - extractive body cue:** 4, we provide qualitative results from our openvocabulary 3D scene graph prediction approach for two different scenes from ScanNet [6].
- **p. 8 / 4.5. Limitations - extractive body cue:** 3D scene graph prediction with different input modalities, object VLM, privileged ground-truth information and supervised fine-tuning. potential and advantages of open-vocabulary 3D scene graph methods.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Open3DSG. We present Open3DSG the first approach for learning to predict open-vocabulary 3D scene graphs from 3D point clouds. The advantage of our ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Open3DSG overview. Given a point cloud and RGB-D images with their poses, we distill the knowledge of two vision-language models into our GNN. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Supervision feature extraction. For each instance in the 3D point cloud, we select the top k frames for object and predicate supervision. For ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Relationship feature computation. Similar to extracting per-object features, we also want to extract a global language-aligned feature embedding for relationships between two objects. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Closed-vocabulary evaluation on 3DSSG. We com- pare our method with both zero-shot and fully-supervised base- lines for 3D scene graph prediction. Overall, the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Frequency based class evaluation. Here we compare the prediction performances for objects and predicates based on their frequency in the training set. Even ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative open-vocabulary 3D scene graph predictions. We show the top-1 predictions on ScanNet [6] from Open3DSG. The nodes are queried using the 3DSSG ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study. 3D scene graph prediction with different input modalities, object VLM, privileged ground-truth information and supervised fine-tuning. potential and advantages of open-vocabulary ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, since 3DSSG is the only dataset to provide ground truth scene graph labels, we evaluate our distilled model quantitatively on it. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | The 3DSSG dataset [44] is at the time of writing this paper, the only dataset that provides semantic scene graph labels aligned with a ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 3 (3. Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We observe that while fully supervised methods demonstrate impressive accuracy on common object and predicate classes, their recall drops drastically for rare tail classes. | definition/direction/unit from same section | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| The nodes are queried using the 3DSSG [44] 160 class label set, while the edges are generated directly from the graph-conditioned LLM. enced by ... | definition/direction/unit from same section | p. 8 (4.3. Ablation studies) |
| We also evaluate the performance of NegCLIP [52] which is supposed to have improved compositional understanding. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| To map this to the fixed label set, we employ BERT [8], a small language model with well-structured word embeddings. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| The caption-based approach also achieves considerably lower performances compared to our method. | definition/direction/unit from same section | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| Hence, our VLM distillation training can also be an effective pre-training strategy when labels are scarce. | definition/direction/unit from same section | p. 8 (4.3. Ablation studies) |
| Figure 2. Open3DSG overview. Given a point cloud and RGB-D images with their poses, we distill the knowledge of two vision-language models into our ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We outperform all our supervised baselines on object, predicate and relationship prediction. | comparison identity and matched condition | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| Additionally, we devise some openvocabulary baseline methods for a fair comparison of our method. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| For further insights into our devised baselines, the reader is referred to our supplementary work. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| The caption-based approach also achieves considerably lower performances compared to our method. | comparison identity and matched condition | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| 3 we show experimentally that using OpenSeg as the 2D object feature extractor yields better results compared to CLIP. | comparison identity and matched condition | p. 8 (4.3. Ablation studies) |
| Table 3. Ablation study. 3D scene graph prediction with different input modalities, object VLM, privileged ground-truth information and supervised fine-tuning. potential and advantages of ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablation study. 3D scene graph prediction with different input modalities, object VLM, privileged ground-truth information and supervised fine-tuning. potential and advantages of ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Therefore, given the comparably small vocabulary of predicates, we choose to fine-tune our model on 27 fixed predicate classes with only a few labels ... | component/input/data sensitivity | p. 8 (4.3. Ablation studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We highlight the following three contributions: • We are the first to present a method to create an interactive graph representation of a scene ... | We also evaluate the performance of NegCLIP [52] which is supposed to have improved compositional understanding. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | The caption-based approach also achieves considerably lower performances compared to our method. | numeric claim only at cited anchor | p. 7 (4.2. Closed-set 3D scene graph prediction) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While closed-vocabulary evaluations are valuable, they cannot highlight the huge potential of open-vocabulary methods such as ours. | p. 8 (4.5. Limitations) |
| body limitation/failure cue | In future work, we see potential in improving relationship prediction even further to achieve even better and more reliable openvocabulary 3D scene graph predictions ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | However, since we predict relationships in a generative manner, we cannot provide fixed queries for our relationship prediction. | p. 6 (4.1. Experimental Setup) |
| body limitation/failure cue | We demonstrate that a naive CLIP-based approach is ill-suited for relationship prediction, but also a two-step approach similar to our method by combining OpenSeg ... | p. 7 (4.2. Closed-set 3D scene graph prediction) |
| body limitation/failure cue | This demonstrates the core advantage of our zero-shot open-vocabulary approach that it performs robustly on a wide variety of objects and predicates. | p. 7 (4.2. Closed-set 3D scene graph prediction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It encodes the output of the LLM and the target relationship labels set and computes the cosine similarity from which we select the top-k ... | p. 6 (4.1. Experimental Setup) |
| We compute the cosine similarity and choose the top-k predictions based on their cosine similarities. | p. 6 (4.1. Experimental Setup) |
| At inference time, we perform a two-step prediction for objects and relationships. | p. 3 (3. Method) |
| First, we predict object classes via a cosine similarity between the distilled features and open-vocabulary queries encoded by CLIP [33]. | p. 3 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.5. Limitations - extractive body cue:** While closed-vocabulary evaluations are valuable, they cannot highlight the huge potential of open-vocabulary methods such as ours.
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we see potential in improving relationship prediction even further to achieve even better and more reliable openvocabulary 3D scene graph predictions that ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** However, since we predict relationships in a generative manner, we cannot provide fixed queries for our relationship prediction.
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** We demonstrate that a naive CLIP-based approach is ill-suited for relationship prediction, but also a two-step approach similar to our method by combining OpenSeg [11] ...
- **p. 7 / 4.2. Closed-set 3D scene graph prediction - extractive body cue:** This demonstrates the core advantage of our zero-shot open-vocabulary approach that it performs robustly on a wide variety of objects and predicates.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.4. Qualitative Results), p. 8 (4.5. Limitations), metrics p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), baselines p. 7 (4.2. Closed-set 3D scene graph prediction), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 8 (Figure/Table caption), results p. 6 (4.1. Experimental Setup), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 7 (4.2. Closed-set 3D scene graph prediction), p. 8 (4.3. Ablation studies), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
