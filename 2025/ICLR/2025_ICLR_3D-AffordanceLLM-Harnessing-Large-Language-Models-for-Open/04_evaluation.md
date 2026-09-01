# Evaluation - 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GThTiuXgDC; PDF retrieval source: https://openreview.net/pdf/1f24613d0aac799415d36944a307d85a27ba53fa.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 14 (A.2 COMPARISON RESULTS ON CLOSE SET), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT)): Notably, 3D AffordanceLLM significantly outperforms the runner-up model (LASO) in terms of mIoU, with improvements of 8.02% and 7.19% on the full and partial view tasks, respectively.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** 3.3, our training data is made up of two types of task data: (1) Referring Object Part Segmentation Dataset: we build this dataset on PartNet ...
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We divide the IRAS dataset following the split of OpenAD and evaluate the close-set and open-set of IRAS.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Compared to existing datasets, this new dataset includes different types of affordances as well as unique affordance-object pairs, such as (twist, faucet), (lever, faucet), (press, ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Thus, we constructed a new test dataset consisting of approximately 559 entries by filtering out some combinations of affordance-object that already existed in our IRAS ...
- **p. 15 / A.3 DATA ANALYSIS - extractive PDF cue:** Building the IRAS dataset based on the 3D AffordanceNet (OpenAD) Dataset (Nguyen et al., 2023).
- **p. 15 / A.3 DATA ANALYSIS - extractive PDF cue:** Partial-view: in real-world application scenarios, we can only expect partial view of 3D shapes, represented as partial point cloud.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Effects of Different Learning Objectives.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** In the IRAS task, the average Arr is approximately 18%.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 7); A.2 COMPARISON RESULTS ON CLOSE SET (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, 3D AffordanceLLM significantly outperforms the runner-up model (LASO) in terms of mIoU, with improvements of 8.02% and 7.19% on the full and partial ... | p. 8 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4 (g), our model significantly outperforms other models. | p. 10 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | As is shown in Table 3, our approach achieved the best zero-shot performance on this ood data. | p. 8 (4 EXPERIMENT) |
| A.2 COMPARISON RESULTS ON CLOSE SET | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8, our 3D-ADLLM achieves optimal performance on nearly all metrics in both the overall-classes and over-all-instances settings. | p. 14 (A.2 COMPARISON RESULTS ON CLOSE SET) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 5, the model utilizing Dice Loss achieves superior mIoU metrics in both seen and unseen settings. | p. 9 (4 EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** 3.3, our training data is made up of two types of task data: (1) Referring Object Part Segmentation Dataset: we build this dataset on PartNet ...
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We divide the IRAS dataset following the split of OpenAD and evaluate the close-set and open-set of IRAS.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Compared to existing datasets, this new dataset includes different types of affordances as well as unique affordance-object pairs, such as (twist, faucet), (lever, faucet), (press, ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Thus, we constructed a new test dataset consisting of approximately 559 entries by filtering out some combinations of affordance-object that already existed in our IRAS ...
- **p. 15 / A.3 DATA ANALYSIS - extractive PDF cue:** Building the IRAS dataset based on the 3D AffordanceNet (OpenAD) Dataset (Nguyen et al., 2023).
- **p. 15 / A.3 DATA ANALYSIS - extractive PDF cue:** Partial-view: in real-world application scenarios, we can only expect partial view of 3D shapes, represented as partial point cloud.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Effects of Different Learning Objectives.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** In the IRAS task, the average Arr is approximately 18%.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1: The comparison of the affordance detection paradigm based on our IRAS or traditional label-based segmentation tasks. (a) shows that label-based paradigm can only ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The Pipeline of 3D-ADLLM. Given the input point cloud and query reasoning instruction, the point cloud multimodal model is trained with lora to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Multi-stage training strategy. Illustration of transferring general segmentation knowledge to affordance detection. (a) depicts the process of extracting general segmentation knowledge, while (b) ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Main results of 3D-ADLLM on zero-short open vocabulary detection. The result is calcu- lated over all classes. The overall results of all comparative ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Zero-shot Open-vocabulary detection results on over all instances.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Zero-shot Open-vocabulary detection results on AffordPose data over all instances.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: The efforts with different point encoder fpe in 3D-ADLLM.(Full- View) fpe mIoUc Accc mAccc
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 5: The comparison results regarding differ- ent settings of loss.(full-view) Openset-mIoUc Closeset-mIoUc DICE & BCE 30.43 42.35 DICE

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 3.3, our training data is made up of two types of task data: (1) Referring Object Part Segmentation Dataset: we build this dataset on ... | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Task/environment | We divide the IRAS dataset following the split of OpenAD and evaluate the close-set and open-set of IRAS. | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3 METHOD), p. 3 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The specific evaluation metrics over all instances: mIoUi (mean IoU over all instance data), mAcci (mean accuracy of points over all instance data), mPreci ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| (2023), we use three metrics to evaluate the results over all classes: mIoUc (mean IoU over all classes), Accc (overall accuracy over all 7 | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| Method Full-view Partial-view mIoUc Accc mAccc mIoUc Accc mAccc TZSLPC (Cheraghian et al., 2020) 3.86 - 10.37 4.14 - 8.49 3DGenZ (Michele et al., ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENT) |
| Full-view: Given an object as 3D point cloud without knowing the affordances supported by the object, the full-shape affordance estimation task aims to estimate ... | definition/direction/unit from same section | p. 15 (A.3 DATA ANALYSIS) |
| Once it is removed, the performance, there is a noticeable reduction in the model's performance. | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| Dice Loss, a segmentation loss function, measures the similarity between predictions and ground truth. | definition/direction/unit from same section | p. 9 (4 EXPERIMENT) |
| 4, our model demonstrates the capacity to accurately comprehend object affordance given the complex reasoning instruction. | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| Moreover, our 3D-ADLLM surpasses other models by employing a multi-stage training strategy that facilitates knowledge transfer and extraction of world knowledge from LLMs. | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Detailed baseline model explanation for experiments can be found in Appendix Sect. | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| Compared to OpenAD, which predicts regions based on a fixed set of affordance labels, our method utilizes longcontext understanding and reasoning for segmentation. | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| Notably, 3D AffordanceLLM significantly outperforms the runner-up model (LASO) in terms of mIoU, with improvements of 8.02% and 7.19% on the full and partial ... | comparison identity and matched condition | p. 8 (4 EXPERIMENT) |
| However, in the partial-view setting, the performance of Phi shows no significant difference compared to Qwen. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| 4 (g), our model significantly outperforms other models. | comparison identity and matched condition | p. 10 (4 EXPERIMENT) |
| (c) (e) (f) (g) (h) OpenAD (DGCNN) Ours 3D-ADLLM GT LASO OpenAD (PointNet++) Figure 4: The visualization results of our 3D-ADLLM compared with others. | comparison identity and matched condition | p. 10 (4 EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.3 ABLATION STUDY Effects of Different Components. | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |
| To investigate the effectiveness of each component in 3DADLLM, we conduct experiments with different variants of 3D-ADLLM. | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |
| Published as a conference paper at ICLR 2025 Table 5: The comparison results regarding different settings of loss.(full-view) Openset-mIoUc Closeset-mIoUc DICE & BCE 30.43 ... | component/input/data sensitivity | p. 10 (4 EXPERIMENT) |
| Method mIoUi mAcci mPreci mReci mAPi 50 OpenAD-PointNet++ 7.61 65.13 22.47 13.01 0.37 OpenAD-DGCNN 8.02 66.76 15.83 13.52 0.39 LASO 34.49 77.12 56.04 37.88 ... | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| Once it is removed, the performance, there is a noticeable reduction in the model's performance. | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| Full-view: Given an object as 3D point cloud without knowing the affordances supported by the object, the full-shape affordance estimation task aims to estimate ... | component/input/data sensitivity | p. 15 (A.3 DATA ANALYSIS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| By reforming the label-based semantic segmentation task in the traditional affordance detection paradigm into a natural language-driven reasoning affordance segmentation task, our model enables ... | Notably, 3D AffordanceLLM significantly outperforms the runner-up model (LASO) in terms of mIoU, with improvements of 8.02% and 7.19% on the full and partial ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 14 (A.2 COMPARISON RESULTS ON CLOSE SET), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Primary metric/result | 4 (g), our model significantly outperforms other models. | numeric claim only at cited anchor | p. 10 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** 3.3, our training data is made up of two types of task data: (1) Referring Object Part Segmentation Dataset: we build this dataset on PartNet ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** Method Full-view Partial-view mIoUc Accc mAccc mIoUc Accc mAccc TZSLPC (Cheraghian et al., 2020) 3.86 - 10.37 4.14 - 8.49 3DGenZ (Michele et al., 2021) ...
- **p. 5 / 3 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2025 Point Encoder.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4.2.2 OUT-OF-DISTRIBUTION RESULTS The test in out-of-distribution (ood) datasets is essential to assess the generalization capability of the model. | p. 8 (4 EXPERIMENT) |
| body limitation/failure cue | Notably, the most substantial performance degradation with about 6% occurs in mIoU when the PC module is removed. | p. 9 (4 EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The projector layer (fproj) between the point encoder fpe and the LLM fllm is a linear layer. | p. 7 (4 EXPERIMENT) |
| For the point encoder (fpe), we adopt Point-BERT (Yu et al., 2022), pre-trained with ULIP-2 (Xue et al., 2024) in the ModelNet dataset (Vishwanath ... | p. 7 (4 EXPERIMENT) |
| However, unlike OpenAD, which includes the "none" category in the calculation of metrics, we only compute the 36 affordance types, excluding "none," as it ... | p. 8 (4 EXPERIMENT) |
| In particular, we compare 2 different implementations: (1) w/o PC removes the pre-trained weights fPB and fAFD, directly training our 3D-ADLLM; (2) w/o UL ... | p. 8 (4 EXPERIMENT) |
| In addition to testing different LLM backbones, we also explored different point encoders. | p. 9 (4 EXPERIMENT) |
| Alternatively, they leverage a text encoder like CLIP (Radford et al., 2021) to associate point-wise features with text embeddings of affordance labels using cosine ... | p. 3 (3 METHOD) |
| PointNet + Head Predefined Label grasp pour contain (a) Label-based (b) IRAS Affordance Decoder 3D AffordanceLLM Handle of mug. | p. 4 (3 METHOD) |
| Finally, the special token and dense point features from fPB is fed into our designed affordance decoder to generate the final affordance mask. | p. 4 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** 4.2.2 OUT-OF-DISTRIBUTION RESULTS The test in out-of-distribution (ood) datasets is essential to assess the generalization capability of the model.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Notably, the most substantial performance degradation with about 6% occurs in mIoU when the PC module is removed.

- **PDF anchors reviewed:** datasets p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 15 (A.3 DATA ANALYSIS), p. 15 (A.3 DATA ANALYSIS), metrics p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 15 (A.3 DATA ANALYSIS), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), baselines p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), results p. 8 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 14 (A.2 COMPARISON RESULTS ON CLOSE SET), p. 9 (4 EXPERIMENT), p. 9 (4 EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
