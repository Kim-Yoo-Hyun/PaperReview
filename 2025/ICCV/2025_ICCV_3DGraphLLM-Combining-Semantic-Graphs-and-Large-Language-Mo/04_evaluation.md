# Evaluation - 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Ablation Studies), p. 6 (4.1. Experimental Results), p. 6 (4.1. Experimental Results), p. 8 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 7 (4.2. Ablation Studies)): 4, incorporating a scene graph representation significantly improves the performance of the LLMs across all three 3D Vision-Language tasks: visual grounding, scene description, and question answering.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive body cue:** For 3RScan scenes, we use data from the RioRefer dataset [36] for object grounding, and the 3RQA dataset [26] for question answering.
- **p. 5 / 4. Experiments - extractive body cue:** For ScanNet scenes, we utilize data from five 3D vision-language benchmarks: visual grounding tasks (ScanRefer [5], Multi3DRefer [60]), scene description (Scan2Cap [9]), and 3D visual ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], as ...
- **p. 6 / 4. Experiments - extractive body cue:** The Multi3DRefer [60] dataset contains queries that may refer to multiple objects.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** It is worth noting that the n-gram-based evaluation metrics used in scene captioning and question answering benchmarks are not adequate for assessing the quality of ...
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** We compare two pre-training datasets for 3DGraphLLM using LLAMA3-8B-Instruct.
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** 6 shows that the object-centric graph representation using triplets improves the performance of the visual grounding task.
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** We include additional experimental results from ablation studies on scene captioning and visual question answering tasks in the Supplementary Materials.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, incorporating a scene graph representation significantly improves the performance of the LLMs across all three 3D Vision-Language tasks: visual grounding, scene description, and ... | p. 7 (4.2. Ablation Studies) |
| 4.1. Experimental Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], ... | p. 6 (4.1. Experimental Results) |
| 4.1. Experimental Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3DGraphLLM achieves results comparable to the state-of-the-art method GPT4Scene8890 | p. 6 (4.1. Experimental Results) |
| 4.2. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 6 shows that the object-centric graph representation using triplets improves the performance of the visual grounding task. | p. 8 (4.2. Ablation Studies) |
| 4.2. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Adding the NMS filter improves the performance of the visual grounding task when using Mask3D instance segmentation (see Tab. | p. 8 (4.2. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive body cue:** For 3RScan scenes, we use data from the RioRefer dataset [36] for object grounding, and the 3RQA dataset [26] for question answering.
- **p. 5 / 4. Experiments - extractive body cue:** For ScanNet scenes, we utilize data from five 3D vision-language benchmarks: visual grounding tasks (ScanRefer [5], Multi3DRefer [60]), scene description (Scan2Cap [9]), and 3D visual ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], as ...
- **p. 6 / 4. Experiments - extractive body cue:** The Multi3DRefer [60] dataset contains queries that may refer to multiple objects.
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** It is worth noting that the n-gram-based evaluation metrics used in scene captioning and question answering benchmarks are not adequate for assessing the quality of ...
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** We compare two pre-training datasets for 3DGraphLLM using LLAMA3-8B-Instruct.
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** 6 shows that the object-centric graph representation using triplets improves the performance of the visual grounding task.
- **p. 8 / 4.2. Ablation Studies - extractive body cue:** We include additional experimental results from ablation studies on scene captioning and visual question answering tasks in the Supplementary Materials.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The proposed 3DGraphLLM approach leverages 3D semantic scene graph learnable representation supplied as input to an LLM to perform various 3D vision-language tasks. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The overall architecture of our approach. We introduce trainable layers to map the extracted graph node and edge features into the token embedding ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Example of prompt for the language model containing scene graph. bors. The relationships between objects are encoded using features extracted from point clouds ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Performance comparison of 3DGraphLLM with state-of-the-art approaches for 3D vision-language tasks. "Expert models" use specialized heads to deal with different 3D vision-language tasks. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Input tokens and inference speed comparison (Mask3D instance segmentation). Evaluation metrics. For the visual grounding task on the ScanRefer [5]dataset, we use the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative examples of 3DGraphLLM performance on object grounding, dense captioning, and question answering tasks. We provide a visualization of the RGB point cloud ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on semantic edges role and training pipeline. C denotes the CIDEr metric. HDM [43], showing the importance of semantic relations for ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation study on semantic edges role depending on quality of instance segmentation. Instance Relations Number ScanRefer Multi3DRef Methods

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For 3RScan scenes, we use data from the RioRefer dataset [36] for object grounding, and the 3RQA dataset [26] for question answering. | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | For ScanNet scenes, we utilize data from five 3D vision-language benchmarks: visual grounding tasks (ScanRefer [5], Multi3DRefer [60]), scene description (Scan2Cap [9]), and 3D ... | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4.1. Experimental Results) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 3 (3. Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3.1. Model Architecture), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Therefore, we use the benchmark-standard F1 score at IoU thresholds of 0.25 and 0.5. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| For the visual question answering task, we follow the validation strategy from Chat-Scene[25], applying CIDEr [49] and BLEU4 [39] metrics for ScanQA [3], and ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| The most interpretable metrics for the role of semantic edges are the accuracy metrics in the 3D referred object grounding task, so we keep ... | definition/direction/unit from same section | p. 7 (4.2. Ablation Studies) |
| First, we add an NMS filter to remove duplicates between the potential neighbors for an object, using a threshold of IoU = 0.99. | definition/direction/unit from same section | p. 8 (4.2. Ablation Studies) |
| To assess 3DGraphLLM performance under realistic conditions, we perform fine-tuning on predicted instance segmentation using 3D vision-language benchmarks 8889 | definition/direction/unit from same section | p. 5 (4. Experiments) |
| In Supplementary Materials we provide more examples of 3DGraphLLM performance. | definition/direction/unit from same section | p. 7 (4.1. Experimental Results) |
| The additional minimum distance filter further enhances visual grounding quality. | definition/direction/unit from same section | p. 8 (4.2. Ablation Studies) |
| Figure 2. The overall architecture of our approach. We introduce trainable layers to map the extracted graph node and edge features into the token ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], ... | comparison identity and matched condition | p. 6 (4.1. Experimental Results) |
| Comparison with state-of-the-art approaches. | comparison identity and matched condition | p. 6 (4.1. Experimental Results) |
| The 3DGraphLLM version with zero nearest neighbors serves as a baseline, equivalent to the Chat-Scene approach, which uses the same LLM as 3DGraphLLM-2. | comparison identity and matched condition | p. 7 (4.2. Ablation Studies) |
| Therefore, in subsequent experiments, we use the Mask3D method to maintain consistency with the baseline Chat-Scene approach. | comparison identity and matched condition | p. 8 (4.2. Ablation Studies) |
| Ablation study on semantic edges role and training pipeline. | comparison identity and matched condition | p. 7 (4.1. Experimental Results) |
| Ablation study on subgraph representation. | comparison identity and matched condition | p. 8 (4.2. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In our experiments, we use LLAMA3-8BInstruct [2], a state-of-the-art large language model, as well as Vicuna-1.5-7B [62] for ablation. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Ablation study on semantic edges role and training pipeline. | component/input/data sensitivity | p. 7 (4.1. Experimental Results) |
| Ablation study on subgraph representation. | component/input/data sensitivity | p. 8 (4.2. Ablation Studies) |
| Ablation study on semantic edges role depending on quality of instance segmentation. | component/input/data sensitivity | p. 8 (4.2. Ablation Studies) |
| For pretraining 3DGraphLLM using GT instance segmentation, we employ a combined 3D VisionLanguage dataset for ScanNet [11] and 3RScan [50] scenes. | component/input/data sensitivity | p. 5 (4. Experiments) |
| To assess 3DGraphLLM performance under realistic conditions, we perform fine-tuning on predicted instance segmentation using 3D vision-language benchmarks 8889 | component/input/data sensitivity | p. 5 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are as follows: • We introduce 3DGraphLLM, the first method for creating a learnable 3D scene graph representation specifically designed ... | 4, incorporating a scene graph representation significantly improves the performance of the LLMs across all three 3D Vision-Language tasks: visual grounding, scene description, and ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Ablation Studies), p. 6 (4.1. Experimental Results), p. 6 (4.1. Experimental Results), p. 8 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 7 (4.2. Ablation Studies) |
| Primary metric/result | 2, our method significantly outperforms the baseline approach Chat-Scene [25] on the two ScanNet 3D referred object grounding benchmarks, ScanRefer [5] and Multi3DRefer [60], ... | numeric claim only at cited anchor | p. 6 (4.1. Experimental Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive body cue:** We use a batch size of 8 and train 3DGraphLLM for 3 epochs with an initial learning rate of 5 · 10-6, following a cosine ...
- **p. 6 / 4. Experiments - extractive body cue:** Training is performed on a server equipped with 4 NVIDIA A100 GPUs, and the entire training process takes approximately 24 hours.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** Here, mi is the number of points in the i-th object proposal of instance segmentation of scene point cloud, and 6 dimensions of each point ...
- **p. 4 / 3.1. Model Architecture - extractive body cue:** In our experiments, we assume a maximum of 200 objects per scene.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A limitation of the method is a significant increase in resource consumption with an increase in the edge number for each graph node. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Our approach falls into the category of "LLM-based models" that consider different tasks as different user queries to a generative model. | p. 6 (4. Experiments) |
| body limitation/failure cue | Another important aspect for further work is the creation of methods for generating semantic relations between objects that are robust to imperfections in the ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | It is worth noting that the n-gram-based evaluation metrics used in scene captioning and question answering benchmarks are not adequate for assessing the quality ... | p. 7 (4.2. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use a batch size of 8 and train 3DGraphLLM for 3 epochs with an initial learning rate of 5 · 10-6, following a ... | p. 6 (4. Experiments) |
| 4, increasing the number of nearest neighbors enhances visual grounding quality with a slight increase in inference time. | p. 8 (4.2. Ablation Studies) |
| We use the semantic relationships encoder [52] pretrained using ground-truth (GT) point cloud scene segmentation data. | p. 5 (3.3. Training Strategy) |
| We train a version of 3DGraphLLM (3DGraphLLM-0) where the scene is represented as a sequence of object identifiers and features extracted by the 2D ... | p. 7 (4.2. Ablation Studies) |
| We vary the number of nearest neighbors in powers of two, capping it at 4 due to GPU memory constraints during training. | p. 8 (4.2. Ablation Studies) |
| The relationships between an object and its neighbors are encoded as triplets (objecti, relationij, objectj). | p. 3 (3. Method) |
| The model architecture includes pre-trained encoders for 2D images, 3D point clouds, and point clouds semantic relationships, alongside a pre-trained LLM. | p. 3 (3.1. Model Architecture) |
| We extract vertex features using a pre-trained Uni3D [63] encoder, which generates point cloud features aligned with their textual descriptions. | p. 4 (3.1. Model Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** A limitation of the method is a significant increase in resource consumption with an increase in the edge number for each graph node.
- **p. 6 / 4. Experiments - extractive body cue:** Our approach falls into the category of "LLM-based models" that consider different tasks as different user queries to a generative model.
- **p. 8 / 5. Conclusion - extractive body cue:** Another important aspect for further work is the creation of methods for generating semantic relations between objects that are robust to imperfections in the instance ...
- **p. 7 / 4.2. Ablation Studies - extractive body cue:** It is worth noting that the n-gram-based evaluation metrics used in scene captioning and question answering benchmarks are not adequate for assessing the quality of ...

- **Evidence anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4.1. Experimental Results), p. 6 (4. Experiments), p. 7 (4.2. Ablation Studies), p. 7 (4.2. Ablation Studies), metrics p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 5 (4. Experiments), p. 7 (4.1. Experimental Results), baselines p. 6 (4.1. Experimental Results), p. 6 (4.1. Experimental Results), p. 7 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Studies), results p. 7 (4.2. Ablation Studies), p. 6 (4.1. Experimental Results), p. 6 (4.1. Experimental Results), p. 8 (4.2. Ablation Studies), p. 8 (4.2. Ablation Studies), p. 7 (4.2. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
