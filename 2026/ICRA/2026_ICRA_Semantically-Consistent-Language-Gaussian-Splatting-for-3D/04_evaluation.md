# Evaluation - Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2503.21767. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS)): We observe that Ours consistently outperforms LangSplat-m and, on average, is better than OpenGaussian, achieving an improvement of +4.14 in mIoU and +10.66 in mAcc.

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** Following LangSplat [23], we conduct experiments on the further annotated LERF [12] dataset that contains a set of in-the-wild scenes and on the 3D-OVS [18] ...
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Acc because the dataset is relatively easy with ≤30 frames and ≤7 objects in each scene, leading to effective segmentation and tracking from SAM2.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** 6: Qualitative results on 3D-OVS dataset for scene "lawn".
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** 7 visualizes the queried points for a scene in the Replica dataset given the query "cloth".
- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** Additionally, we report results on the Replica [28] dataset, which has labeled point clouds
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** I, we show the results on the LERF dataset.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** We also report mIoU accuracy (mAcc↑), a 2D metric proposed by OpenGaussian [29], where a query is considered correct if its IoU is greater than ...
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Note that all four methods encounter a common failure mode of empty query, i.e., no valid Gaussians are returned for a text query, resulting in ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that Ours consistently outperforms LangSplat-m and, on average, is better than OpenGaussian, achieving an improvement of +4.14 in mIoU and +10.66 in ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Acc, significantly outperforming baseline methods. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also see that our proposed GT-anchored query significantly outperforms the canonical query. | p. 7 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent ... | p. 2 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Additionally, we report results on the Replica [28] dataset, which has labeled point clouds | p. 5 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** Following LangSplat [23], we conduct experiments on the further annotated LERF [12] dataset that contains a set of in-the-wild scenes and on the 3D-OVS [18] ...
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Acc because the dataset is relatively easy with ≤30 frames and ≤7 objects in each scene, leading to effective segmentation and tracking from SAM2.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** 6: Qualitative results on 3D-OVS dataset for scene "lawn".
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** 7 visualizes the queried points for a scene in the Replica dataset given the query "cloth".
- **p. 5 / V. EXPERIMENTS - extractive PDF cue:** Additionally, we report results on the Replica [28] dataset, which has labeled point clouds
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** I, we show the results on the LERF dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Visualization of the language embedding supervision. For the "red bag" circled in yellow, the ground-truth constructed by LangSplat [23] is inconsistent across frames, ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent optimal ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Overview of the proposed method. In Sec. IV-A, we present a masklet extraction algorithm (Alg. 1) that leverages Segment Anything Models to generate ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualization of the ground-truth Lt constructed by LangSplat [23]. We observed that the semantics are not consistent across viewpoints, e.g., the circled bag ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 5: Qualitative results on LERF dataset of scene"ramen" and "figurines". For each scene, the first row contains rendered language embeddings, and the second row ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Qualitative results on 3D-OVS dataset for scene "lawn". The first row contains rendered language embeddings, and the second row contains 3D query results ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Qualitative results on Replica dataset. Yellow points are the queried points of "cloth". language Gaussians 5 times with different seeds has a small ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following LangSplat [23], we conduct experiments on the further annotated LERF [12] dataset that contains a set of in-the-wild scenes and on the 3D-OVS ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Task/environment | Acc because the dataset is relatively easy with ≤30 frames and ≤7 objects in each scene, leading to effective segmentation and tracking from SAM2. | reset, timeout, object/scene variation | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (III. PRELIMINARIES), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We also report mIoU accuracy (mAcc↑), a 2D metric proposed by OpenGaussian [29], where a query is considered correct if its IoU is greater ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Note that all four methods encounter a common failure mode of empty query, i.e., no valid Gaussians are returned for a text query, resulting ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| This includes mean Intersection over Union (mIoU ↑) and localization accuracy (Loc. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Formally, for each language embedding li and each text query q, the relevancy score is defined as mini exp(li·q) exp(li·q)+exp(q·ϕicanon) where ϕi canon is ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 3: Overview of the proposed method. In Sec. IV-A, we present a masklet extraction algorithm (Alg. 1) that leverages Segment Anything Models to ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Acc, significantly outperforming baseline methods. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| We observe that Ours consistently outperforms LangSplat-m and, on average, is better than OpenGaussian, achieving an improvement of +4.14 in mIoU and +10.66 in ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| To further benchmark the performance, we included more baseline methods modified (m) for direct 3D querying: LangSplatm [23], which also trains a language 3D ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| We also see that our proposed GT-anchored query significantly outperforms the canonical query. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also studied the effectiveness of our method without DBSCAN [5] and evaluated the performance of canonical querying from LERF [12] on the task ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| We conduct ablation studies to validate the efficacy of each proposed component of our method and report the performance in Tab. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| Pretraining the standard 3D Gaussian Splatting takes 30,000 steps. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We introduce tracking for generating semantic and 3DarXiv:2503.21767v2 [cs.CV] 26 Sep 2025 | We observe that Ours consistently outperforms LangSplat-m and, on average, is better than OpenGaussian, achieving an improvement of +4.14 in mIoU and +10.66 in ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Primary metric/result | Acc, significantly outperforming baseline methods. | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Pretraining the standard 3D Gaussian Splatting takes 30,000 steps.
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** This is followed by training the language embeddings for an additional 30,000 steps, skipping the densification stage.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Acc because the dataset is relatively easy with ≤30 frames and ≤7 objects in each scene, leading to effective segmentation and tracking from SAM2.
- **p. 5 / IV. METHOD - extractive PDF cue:** Ground Truth (GT)-anchored 3D Querying With the text query vector q, the standard approach is to directly compares the CLIP features q of the query ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Note that all four methods encounter a common failure mode of empty query, i.e., no valid Gaussians are returned for a text query, resulting ... | p. 7 (V. EXPERIMENTS) |
| body limitation/failure cue | Acc, a query is considered correct if the center of the queried mask's exterior bounding box falls within the bounding box of the ground-truth. | p. 6 (V. EXPERIMENTS) |
| body limitation/failure cue | Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | (11) As ¯ϕr is obtained as a weighted average of CLIP image embeddings and q comes from CLIP text embeddings, a direct comparison between ... | p. 5 (IV. METHOD) |
| body limitation/failure cue | Therefore, any high threshold works well, which improves the queries' reliability and robustness. | p. 5 (IV. METHOD) |
| body limitation/failure cue | We observe that LangSplat-m and GaussianGrouping-m failed to retrieve the correct object, and OpenGaussian only retrieves part of the cloth with noisy points from ... | p. 7 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Experiments are conducted on an NVIDIA A100 GPU. | p. 6 (V. EXPERIMENTS) |
| Pretraining the standard 3D Gaussian Splatting takes 30,000 steps. | p. 6 (V. EXPERIMENTS) |
| There exists 0.00 in GaussianGrouping-m's results because their query implementation only uses the first frame's semantics. | p. 7 (V. EXPERIMENTS) |
| Yellow points are the queried points of "cloth". language Gaussians 5 times with different seeds has a small standard deviation, e.g., on figurines the ... | p. 7 (V. EXPERIMENTS) |
| As in LangSplat, to reduce the GPU memory usage, we train a light-weight autoencoder consisting of an encoder E and a decoder D. | p. 5 (IV. METHOD) |
| If the proposed region has not been tracked, we run the tracking model and add the output masklets to the set of tracked masklets ... | p. 4 (IV. METHOD) |
| This is done by masking out the image It using the extracted masklet and then passing it to CLIP's image encoder: ¯ϕr = T ... | p. 4 (IV. METHOD) |
| With the retrieved GT ¯ϕ∗ r, we compress it into lower dimension with the pretrained encoder E. | p. 5 (IV. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** Note that all four methods encounter a common failure mode of empty query, i.e., no valid Gaussians are returned for a text query, resulting in ...
- **p. 6 / V. EXPERIMENTS - extractive PDF cue:** Acc, a query is considered correct if the center of the queried mask's exterior bounding box falls within the bounding box of the ground-truth.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: IoU metric per query vs. cosine similarity thresholds for the standard querying method. We observe that it does not have a consistent optimal ...
- **p. 5 / IV. METHOD - extractive PDF cue:** (11) As ¯ϕr is obtained as a weighted average of CLIP image embeddings and q comes from CLIP text embeddings, a direct comparison between them ...
- **p. 5 / IV. METHOD - extractive PDF cue:** Therefore, any high threshold works well, which improves the queries' reliability and robustness.
- **p. 7 / V. EXPERIMENTS - extractive PDF cue:** We observe that LangSplat-m and GaussianGrouping-m failed to retrieve the correct object, and OpenGaussian only retrieves part of the cloth with noisy points from other ...

- **PDF anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), metrics p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), results p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 2 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
