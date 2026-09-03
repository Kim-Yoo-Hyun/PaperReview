# Evaluation - TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2603.02972. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (Figure/Table caption)): It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with significantly larger parameter counts.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For testing, we utilize 1,021 navigation paths from the val seen split and 2,349 paths from the val unseen split in the R2R dataset.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To rearrange the dataset into SAP task for training, 14,093 trajectories from the R2R training split are segmented into discrete navigation steps.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** All ablation experiments are conducted on the TagaVLM-0.5B model and the val unseen split of R2R dataset.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** By using the rich scene diversity provided by HM3D, an additional 500K augmented data samples are utilized for the first-stage fine-tuning, which improves the model's ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In these metrics, Trajectory Length (TL) denotes average path length in meters; Navigation Error (NE) represents the average distance in meters between the agent's final ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The global action space introduces backtracking capability that improves fault tolerance in navigation processes, enabling the agent to execute direct backtracking upon encountering navigation errors ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** II, the model achieves large performance gains of 12.26% in SR and 14.8 in SPL with the Interleaved Navigation Prompt, as shown in row (c).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Notably, compared to MapGPT[15], our approach achieves an absolute improvement of 3.39% in SR and 9.08 in SPL on the val unseen split.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with significantly larger ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, the text-based topological map achieves substantially lower performance improvements than the STAR-Att used in row (c), indicating significant challenges for understanding topological structures ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, compared to MapGPT[15], our approach achieves an absolute improvement of 3.39% in SR and 9.08 in SPL on the val unseen split. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, it is an accepted fact that training on largescale data can significantly improve model performance. | p. 7 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4. A successful case demonstrates TagaVLM's spatial topological awareness and path correction ability. (a) shows the navigation instruction containing two key landmarks: black ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For testing, we utilize 1,021 navigation paths from the val seen split and 2,349 paths from the val unseen split in the R2R dataset.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To rearrange the dataset into SAP task for training, 14,093 trajectories from the R2R training split are segmented into discrete navigation steps.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** All ablation experiments are conducted on the TagaVLM-0.5B model and the val unseen split of R2R dataset.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** By using the rich scene diversity provided by HM3D, an additional 500K augmented data samples are utilized for the first-stage fine-tuning, which improves the model's ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Motivation of the proposed method. Previous methods (c) usually employ a two-stage pipeline that uses VLMs to convert visual observations to text for ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Overview of the TagaVLM. The pretrained observation encoder and projector encode RGB observations from each node to the semantic space. Textual information containing ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. In the navigation process, if an unvisited candidate node is observed multiple times at different positions, it is represented by stitching the images ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. A successful case demonstrates TagaVLM's spatial topological awareness and path correction ability. (a) shows the navigation instruction containing two key landmarks: black chairs ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For testing, we utilize 1,021 navigation paths from the val seen split and 2,349 paths from the val unseen split in the R2R dataset. | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | To rearrange the dataset into SAP task for training, 14,093 trajectories from the R2R training split are segmented into discrete navigation steps. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (III. METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In these metrics, Trajectory Length (TL) denotes average path length in meters; Navigation Error (NE) represents the average distance in meters between the agent's ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| The global action space introduces backtracking capability that improves fault tolerance in navigation processes, enabling the agent to execute direct backtracking upon encountering navigation ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| II, the model achieves large performance gains of 12.26% in SR and 14.8 in SPL with the Interleaved Navigation Prompt, as shown in row ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Notably, compared to MapGPT[15], our approach achieves an absolute improvement of 3.39% in SR and 9.08 in SPL on the val unseen split. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 4. A successful case demonstrates TagaVLM's spatial topological awareness and path correction ability. (a) shows the navigation instruction containing two key landmarks: black ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 1. Motivation of the proposed method. Previous methods (c) usually employ a two-stage pipeline that uses VLMs to convert visual observations to text ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2. Overview of the TagaVLM. The pretrained observation encoder and projector encode RGB observations from each node to the semantic space. Textual information ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with significantly larger ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Compared with the baseline in row (b) of Tab. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| It prevents fair comparison between these methods, and therefore, NaviLLM is not compared in this work. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Notably, compared to MapGPT[15], our approach achieves an absolute improvement of 3.39% in SR and 9.08 in SPL on the val unseen split. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation Study To explore the effectiveness of key components in our approach and their impacts on navigation performance, we designed a series of ablation ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| II, all the essential components, including STAR-Att, are removed, and by solely finetuning the VLM to adapt the VLN task, it only achieves an ... | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| Cross-modal-based methods typically employ a smaller-scale LSTM or Transformer to either train from scratch or pretrain and then fine-tune for the VLN task. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| We perform full fine-tuning on the parameters of the multimodal projector and the Qwen2 [8] LLM backbone. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Fig. 1. Motivation of the proposed method. Previous methods (c) usually employ a two-stage pipeline that uses VLMs to convert visual observations to text ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 2. Overview of the TagaVLM. The pretrained observation encoder and projector encode RGB observations from each node to the semantic space. Textual information ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contribution can be summarized as follows: • We introduce TagaVLM, an end-to-end VLN framework that architecturally embeds topological structures into the VLM backbone. ... | It is worth noting that, our 0.5B parameter model already outperforms most largemodel-based methods and achieves comparable performance to state-of-the-art approaches with significantly larger ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (Figure/Table caption) |
| Primary metric/result | However, the text-based topological map achieves substantially lower performance improvements than the STAR-Att used in row (c), indicating significant challenges for understanding topological structures ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To rearrange the dataset into SAP task for training, 14,093 trajectories from the R2R training split are segmented into discrete navigation steps.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Furthermore, we leverage the data augmentation method [22] to generate 500K SAP samples (around 90K trajectories) across 800 scenes from the HM3D [39] dataset.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Our training employs a two-stage strategy: 1) pre-training for 12,500 steps on a mixture of R2R and augmented HM3D data, followed by 2) fine-tuning for ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work will build on this strong baseline by scaling training on larger datasets, enriching STAR-Att with more complex geometric priors, and extending our ... | p. 7 (V. CONCLUSIONS) |
| body limitation/failure cue | However, due to computational resource limitations, TagaVLM-7B is fine-tuned with only 200K augmented samples. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | However, owing to the limitation of computational resources, the amount of training data used for the proposed method is significantly smaller than that of ... | p. 7 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For both stages, the Adam optimizer is used with a learning rate of 1e-5 and a batch size of 16. | p. 6 (IV. EXPERIMENTS) |
| The projector consists of two fully-connected layers with a hidden dimension of 1024, while the SigLIP [40] visual encoder remains frozen. | p. 6 (IV. EXPERIMENTS) |
| Steps to form the proposed prompt are illustrated as follows. | p. 4 (III. METHOD) |
| First, the visual observations are encoded into visual tokens for further digesting in the LLM. | p. 4 (III. METHOD) |
| (b) Shows TagaVLM's 6 navigation steps from the starting node Node1 to the target destination. | p. 5 (III. METHOD) |
| Through the above steps, we obtain a token-wise affinity matrix where a higher value indicates a lower degree of correlation. | p. 5 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. CONCLUSIONS - extractive body cue:** Future work will build on this strong baseline by scaling training on larger datasets, enriching STAR-Att with more complex geometric priors, and extending our framework ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, due to computational resource limitations, TagaVLM-7B is fine-tuned with only 200K augmented samples.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** However, owing to the limitation of computational resources, the amount of training data used for the proposed method is significantly smaller than that of NaviLLM[16], ...

- **Evidence anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
