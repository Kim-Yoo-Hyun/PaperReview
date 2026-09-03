# Evaluation - Mamba-3VL: Taming State Space Model for 3D Vision Language Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption), p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (4.3. Ablation Study and In-depth Analysis)): The model achieves landmark accuracies of 79.9% (Unique) and 48.9% (Multiple) on the ScanRefer [6], outperforming PQ3D [74] by 1.7% and 2.7%, respectively.

## Evaluation Body Digest

- **p. 5 / 4.1. Implementation Details - extractive body cue:** (2) 80-epoch full-task training on all benchmark datasets with promptable queries.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** Answer accuracy on the ScanQA [2] benchmark, with separate evaluations for "test w/ object" and "test w/o object".
- **p. 6 / 4.1. Implementation Details - extractive body cue:** For embodied AI tasks, we replace the T5-small [49] model of generation head with Vicuna-7B [13] using the instructionfollowing dataset [21].
- **p. 5 / 4.1. Implementation Details - extractive body cue:** We evaluate the Mamba-3VL on multiple 3D-VL datasets, i.e., ScanNet200 [51], Multi3DRefer [67], ScanRefer [6], Sr3D/Nr3D [1], SQA3D [42], ScanQA [2], Scan2Cap [11].
- **p. 7 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Results on CLIPort robot manipulation.
- **p. 7 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Embodied Navigation and Robotic Manipulation.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** Crossattention treats all tokens within a sequence equally, failing to capture the hierarchical dependencies within 3D scenes.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** When comparing (b) and (d), the relation-prioritized spatial scanning brings substantial gains on the SQA3D [42] (2.3%) and Multi3DRefer [67] (1.6%) datasets, underscoring capabilities to ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental Results (p. 5); 4.1. Implementation Details (p. 5); 4.2. Results on 3D Vision-Language Tasks (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results on 3D Vision-Language Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | The model achieves landmark accuracies of 79.9% (Unique) and 48.9% (Multiple) on the ScanRefer [6], outperforming PQ3D [74] by 1.7% and 2.7%, respectively. | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. Visualization results of the scene-aware task planning and embodied conversation on the 3RPlan [21] and 3RDialog [21] datasets. petitors on challenging unseen ... | p. 8 (Figure/Table caption) |
| 4.2. Results on 3D Vision-Language Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | On Multi3DRefer [67], Mamba3VL attains 69.5%, 45.7%, and 43.5% scores, showing a substantial improvement in different object referencing levels. | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| 4.2. Results on 3D Vision-Language Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | Impressively, Mamba-3VL achieves comparable performance, recording an AP of 22.4%, showcasing its potential as a versatile interface for 3D open-vocabulary instance segmentation. | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| 4.2. Results on 3D Vision-Language Tasks | EMPIRICAL / SOURCE-REPORTED EVALUATION | Further, our method surpasses other leading approaches in both Bleu-4 and Meteor scores, reflecting improved fluency and better semantic alignment with contextual details of ... | p. 7 (4.2. Results on 3D Vision-Language Tasks) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Implementation Details - extractive body cue:** (2) 80-epoch full-task training on all benchmark datasets with promptable queries.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** Answer accuracy on the ScanQA [2] benchmark, with separate evaluations for "test w/ object" and "test w/o object".
- **p. 6 / 4.1. Implementation Details - extractive body cue:** For embodied AI tasks, we replace the T5-small [49] model of generation head with Vicuna-7B [13] using the instructionfollowing dataset [21].
- **p. 5 / 4.1. Implementation Details - extractive body cue:** We evaluate the Mamba-3VL on multiple 3D-VL datasets, i.e., ScanNet200 [51], Multi3DRefer [67], ScanRefer [6], Sr3D/Nr3D [1], SQA3D [42], ScanQA [2], Scan2Cap [11].
- **p. 7 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Results on CLIPort robot manipulation.
- **p. 7 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Embodied Navigation and Robotic Manipulation.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** Crossattention treats all tokens within a sequence equally, failing to capture the hierarchical dependencies within 3D scenes.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** When comparing (b) and (d), the relation-prioritized spatial scanning brings substantial gains on the SQA3D [42] (2.3%) and Multi3DRefer [67] (1.6%) datasets, underscoring capabilities to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Mamba-3VL serves as an interactive and general-purpose interface for 3D vision-language tasks, including Referring Segmentation, Visual Grounding, Question Answering, Dense Captioning, while generalizing ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison of grounding accuracy and model efficiency. human commands in real scenarios. Towards this goal, nu- merous datasets and 3D foundation models for ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Preliminaries on pipeline of the proposed Mamba-3VL. (a) Our Mamba-3VL is a query-based decoding framework composed of stacked Mamba Mixer and IDPA layers. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Visualized examples for promptable segmentation tasks.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Grounding accuracy (%) on 3D-VG benchmarks. Results on ScanRefer and Multi3DRefer are reported under IoU@0.5. The ZT and ST results from Multi3DRefer are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Instance segmentation results on ScanNet200 [51], with w/cls indicating the closed-vocabulary classification head.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Answer accuracy on the SQA3D [42] by question types. ε is a small constant for numerical stability. α(T) and β(T) are learnable factors ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 4. Results of 3D dense captioning on Scan2Cap [11] under IoU@50, evaluated by text similarity scores. The output ¯xi of IDPA is incorporated into ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (2) 80-epoch full-task training on all benchmark datasets with promptable queries. | embodiment, simulator version and control stack | p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Task/environment | Answer accuracy on the ScanQA [2] benchmark, with separate evaluations for "test w/ object" and "test w/o object". | reset, timeout, object/scene variation | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (2.2. State Space Models and Visual Applications), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.1. Overall Framework) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6. Visualization results of the scene-aware task planning and embodied conversation on the 3RPlan [21] and 3RDialog [21] datasets. petitors on challenging unseen ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 5. Answer accuracy on the ScanQA [2] benchmark, with separate evaluations for "test w/ object" and "test w/o object". Metrics include top-1/top-10 exact ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 4. Results of 3D dense captioning on Scan2Cap [11] under IoU@50, evaluated by text similarity scores. The output ¯xi of IDPA is incorporated ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 1. Grounding accuracy (%) on 3D-VG benchmarks. Results on ScanRefer and Multi3DRefer are reported under IoU@0.5. The ZT and ST results from Multi3DRefer ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Further, our method surpasses other leading approaches in both Bleu-4 and Meteor scores, reflecting improved fluency and better semantic alignment with contextual details of ... | definition/direction/unit from same section | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| MP3D-val HD3M-val Methods Success SPL Success SPL Habitat (shortest) 4.4 2.2 - - Habitat (70k demo) 35.4 10.4 - - VC-1 (ViT-B) - - ... | definition/direction/unit from same section | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| On Multi3DRefer [67], Mamba3VL attains 69.5%, 45.7%, and 43.5% scores, showing a substantial improvement in different object referencing levels. | definition/direction/unit from same section | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| Figure 2. Comparison of grounding accuracy and model efficiency. human commands in real scenarios. Towards this goal, nu- merous datasets and 3D foundation models ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the SQA3D [42], Mamba3VL outperforms all existing state-of-the-arts across different challenging question types as illustrated in Tab. | comparison identity and matched condition | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| Figure 6. Visualization results of the scene-aware task planning and embodied conversation on the 3RPlan [21] and 3RDialog [21] datasets. petitors on challenging unseen ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| 1, our Mamba3VL dominates 3D visual grounding benchmarks, surpassing state-of-the-arts by significant margins. | comparison identity and matched condition | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| The model achieves landmark accuracies of 79.9% (Unique) and 48.9% (Multiple) on the ScanRefer [6], outperforming PQ3D [74] by 1.7% and 2.7%, respectively. | comparison identity and matched condition | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| Our findings are as follows: (1) For robotic manipulation, Mamba-3VL consistently outperforms com6279 | comparison identity and matched condition | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| Compared with Linear-complexity Methods. | comparison identity and matched condition | p. 8 (4.3. Ablation Study and In-depth Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 9. Ablation study of proposed modules' effectiveness, with average performance evaluated under IoU@0.5. in Tab. 2, Mamba-3VL establishes new competitive bench- marks for ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Our method exhibits view-invariant robustness with 3.9% and 6.2% improvements over PQ3D on VD subsets of Nr3D/Sr3D benchmarks. | component/input/data sensitivity | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| Ablations of the selection of scanning mechanism. | component/input/data sensitivity | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| A), more framework ablations of Mamba-3VL (Tab. | component/input/data sensitivity | p. 8 (4.3. Ablation Study and In-depth Analysis) |
| Removing either component (i.e., w/o. | component/input/data sensitivity | p. 8 (4.3. Ablation Study and In-depth Analysis) |
| For embodied AI tasks, we replace the T5-small [49] model of generation head with Vicuna-7B [13] using the instructionfollowing dataset [21]. | component/input/data sensitivity | p. 6 (4.1. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To capture spatial relationships of 3D object sequences while enhancing fine-grained interactions of 3D-VL interaction, we develop a Mamba Mixer module, which consists of ... | The model achieves landmark accuracies of 79.9% (Unique) and 48.9% (Multiple) on the ScanRefer [6], outperforming PQ3D [74] by 1.7% and 2.7%, respectively. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption), p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (4.3. Ablation Study and In-depth Analysis) |
| Primary metric/result | Figure 6. Visualization results of the scene-aware task planning and embodied conversation on the 3RPlan [21] and 3RDialog [21] datasets. petitors on challenging unseen ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / Method - extractive body cue:** Scan2Cap [11] 53.7 35.2 22.4 21.4 43.6 30.7 3DJCG [4] 60.8 47.7 31.5 24.3 51.1 38.7 3D-VisTA [73] 71.0 66.9 34.0 27.1 54.3 45.6 X-Trans2Cap ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method exhibits view-invariant robustness with 3.9% and 6.2% improvements over PQ3D on VD subsets of Nr3D/Sr3D benchmarks. | p. 6 (4.2. Results on 3D Vision-Language Tasks) |
| body limitation/failure cue | FIS/NIS) results in performance degradation, suggesting their complementary roles. | p. 8 (4.3. Ablation Study and In-depth Analysis) |
| body limitation/failure cue | Crossattention treats all tokens within a sequence equally, failing to capture the hierarchical dependencies within 3D scenes. | p. 8 (4.3. Ablation Study and In-depth Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We utilize AdamW [38] optimizer with a base learning rate of 1e-4 and a warm-up cosine scheduler. | p. 5 (4.1. Implementation Details) |
| The hidden dimension and query decoder layer is set to d=768, L=4. | p. 5 (4.1. Implementation Details) |
| In open-vocabulary setting, we integrate CLIP [48] text embeddings in a promptable way and compute class logits from the grounding head after full-category prompting. | p. 7 (4.2. Results on 3D Vision-Language Tasks) |
| Further, a mamba-based query decoder is introduced with the multi-modal Mamba-Mixer module (Sec. | p. 3 (3.1. Overall Framework) |
| We extract point cloud, multi-scale voxel, and multi-view image features with a point encoder, a voxel encoder, and an image encoder. | p. 3 (3.1. Overall Framework) |
| In each decoder layer l, instance queries Ql sequentially retrieve scene-relevant features and prompt-encoded knowledge with two successive Mamba Mixer modules, severally. | p. 4 (3.2. Multi-Modal Mamba Mixer Block) |
| Following PQ3D [74], a zero-initialized query Q0 centered on 3D object centroids, is inputted into the mambabased decoder, which guides instance queries to incorporate ... | p. 4 (3.2. Multi-Modal Mamba Mixer Block) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Results on 3D Vision-Language Tasks - extractive body cue:** Our method exhibits view-invariant robustness with 3.9% and 6.2% improvements over PQ3D on VD subsets of Nr3D/Sr3D benchmarks.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** FIS/NIS) results in performance degradation, suggesting their complementary roles.
- **p. 8 / 4.3. Ablation Study and In-depth Analysis - extractive body cue:** Crossattention treats all tokens within a sequence equally, failing to capture the hierarchical dependencies within 3D scenes.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 5 (4.1. Implementation Details), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), metrics p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), baselines p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption), p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (4.3. Ablation Study and In-depth Analysis), results p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 8 (Figure/Table caption), p. 6 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 7 (4.2. Results on 3D Vision-Language Tasks), p. 8 (4.3. Ablation Study and In-depth Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
