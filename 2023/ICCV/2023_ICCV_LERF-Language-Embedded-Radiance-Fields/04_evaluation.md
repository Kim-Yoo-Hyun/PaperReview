# Evaluation - LERF: Language Embedded Radiance Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.09553; PDF retrieval source: https://arxiv.org/pdf/2303.09553. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Localization), p. 8 (4.4. Ablations), p. 7 (4. Experiments), p. 7 (4.1. Qualitative Results), p. 4 (Figure/Table caption), p. 12 (Figure/Table caption)): OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries.

## Evaluation Body Digest

- **p. 7 / 4. Experiments - extractive body cue:** Emphasizing the capability of LERF to handle real-world data, we collect 13 scenes containing a mixture of in-the-wild (grocery store, kitchen, bookstore) and posed long-tail ...
- **p. 7 / 4. Experiments - extractive body cue:** Refer to supplements for more details on scenes and text queries. quality NeRFs [12], and such simulated or scanned scenes contain few long-tail objects [34].
- **p. 8 / 4.3. Localization - extractive body cue:** To evaluate how well LERF can localize text prompts in a scene we render novel views and label bounding boxes for 72 objects across 5 ...
- **p. 8 / 4.1. Qualitative Results - extractive body cue:** LSeg performs similarly to LERF on in-distribution labels, but significantly suffers on long-tail labels of wild scenes. three different queries, demonstrating the ability of LERF ...
- **p. 8 / 4.2. Existence Determination - extractive body cue:** We report precision-recall curves over relevancy score thresholds in Fig.
- **p. 8 / 4.3. Localization - extractive body cue:** We also compare against the 2D open-vocab detector OWL-ViT by rendering full-HD NeRF views and selecting the bounding box with the highest confidence score for ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: LERF Optimization: Left: LERF represents a field of 3D volumes, parameterized by position x, y, z and scale s (orange cube). To render ...
- **p. 7 / 4.1. Qualitative Results - extractive body cue:** We visualize relevancy score by normalizing the colormap for each query from 50% (less relevant than canonical phrases) to the maximum relevancy.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.6. Implementation Details (p. 7); 4. Experiments (p. 7); 4.1. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Localization | EMPIRICAL / REAL-ROBOT OR HARDWARE | OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries. | p. 8 (4.3. Localization) |
| 4.4. Ablations | EMPIRICAL / REAL-ROBOT OR HARDWARE | We show two illustrative examples where DINO improves the quality of relevancy maps in Fig. | p. 8 (4.4. Ablations) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall performance is calculated by aggregating scene results. | p. 7 (4. Experiments) |
| 4.1. Qualitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We visualize relevancy score by normalizing the colormap for each query from 50% (less relevant than canonical phrases) to the maximum relevancy. | p. 7 (4.1. Qualitative Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: Results with LERF for 5 in-the-wild scenes. Each image shows a visual rendering of the LERF (Sec. 3), along with relevancy renderings ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4. Experiments - extractive body cue:** Emphasizing the capability of LERF to handle real-world data, we collect 13 scenes containing a mixture of in-the-wild (grocery store, kitchen, bookstore) and posed long-tail ...
- **p. 7 / 4. Experiments - extractive body cue:** Refer to supplements for more details on scenes and text queries. quality NeRFs [12], and such simulated or scanned scenes contain few long-tail objects [34].
- **p. 8 / 4.3. Localization - extractive body cue:** To evaluate how well LERF can localize text prompts in a scene we render novel views and label bounding boxes for 72 objects across 5 ...
- **p. 8 / 4.1. Qualitative Results - extractive body cue:** LSeg performs similarly to LERF on in-distribution labels, but significantly suffers on long-tail labels of wild scenes. three different queries, demonstrating the ability of LERF ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Language Embedded Radiance Fields (LERF). LERF grounds CLIP representations in a dense, multi-scale 3D field. A LERF can be reconstructed from a hand-held ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. We construct a LERF by optimizing a language field jointly with NeRF, which takes both position and physical scale as input and outputs ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: LERF Optimization: Left: LERF represents a field of 3D volumes, parameterized by position x, y, z and scale s (orange cube). To render ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Results with LERF for 5 in-the-wild scenes. Each image shows a visual rendering of the LERF (Sec. 3), along with relevancy renderings (Sec. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: 2D CLIP vs LERF: The left visualizes similarity inter- polated over patchwise CLIP embeddings, and the right rendered from LERF. Because volumetric language ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant λlang ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Localization comparison Qualitative comparison on lo- calizing long-tail objects from novel views with LSeg in 3D (DFF) and OWL-ViT (Tab. 1) cient views, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Comparison to LSeg in 3D: LSeg performs well on "glass of water" since cups are in the COCO dataset, but cannot locate an ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Emphasizing the capability of LERF to handle real-world data, we collect 13 scenes containing a mixture of in-the-wild (grocery store, kitchen, bookstore) and posed ... | embodiment, simulator version and control stack | p. 7 (4. Experiments), p. 7 (4. Experiments) |
| Task/environment | Refer to supplements for more details on scenes and text queries. quality NeRFs [12], and such simulated or scanned scenes contain few long-tail objects ... | reset, timeout, object/scene variation | p. 7 (4. Experiments), p. 8 (4.3. Localization) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3.4. Field Architecture), p. 6 (3.4. Field Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report precision-recall curves over relevancy score thresholds in Fig. | definition/direction/unit from same section | p. 8 (4.2. Existence Determination) |
| We also compare against the 2D open-vocab detector OWL-ViT by rendering full-HD NeRF views and selecting the bounding box with the highest confidence score ... | definition/direction/unit from same section | p. 8 (4.3. Localization) |
| Figure 2: LERF Optimization: Left: LERF represents a field of 3D volumes, parameterized by position x, y, z and scale s (orange cube). To ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We visualize relevancy score by normalizing the colormap for each query from 50% (less relevant than canonical phrases) to the maximum relevancy. | definition/direction/unit from same section | p. 7 (4.1. Qualitative Results) |
| Test Scene LSeg (3D) OWL-ViT LERF waldo kitchen 13.0% 42.6% 81.5% bouquet 50.0% 66.7% 91.7% ramen 15.0% 92.5% 62.5% teatime 28.1% 75.0% 93.8% figurines ... | definition/direction/unit from same section | p. 7 (4. Experiments) |
| Table 2: Maximum relevancy scores for each text query in Fig. 1 of main text, calculated from the displayed viewpoint. Highly specific queries have ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 11: LERF Convergence. We visualize rendered relevancy maps at 1k, 2k, 6k, and 30k optimization steps. Relatively speaking, regions with more common semantics ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 1: Language Embedded Radiance Fields (LERF). LERF grounds CLIP representations in a dense, multi-scale 3D field. A LERF can be reconstructed from a ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries. | comparison identity and matched condition | p. 8 (4.3. Localization) |
| 6, and suggest that language embeddings embedded in LERF strongly outperform LSeg in 3D for localizing relevant parts of a scene. | comparison identity and matched condition | p. 8 (4.3. Localization) |
| Though existing 3D scan datasets exist, they tend to be either of singulated objects [29, 13], or are RGB-D scans without enough views to ... | comparison identity and matched condition | p. 7 (4. Experiments) |
| Visual comparison with LSeg in 3D are presented in Fig 7. | comparison identity and matched condition | p. 7 (4.1. Qualitative Results) |
| Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 15: Geometric separation impacts quality: Queries without much geometric separation can blur between objects and foreground-background. In the toaster case, very few viewing ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Though existing 3D scan datasets exist, they tend to be either of singulated objects [29, 13], or are RGB-D scans without enough views to ... | component/input/data sensitivity | p. 7 (4. Experiments) |
| We remove scale as a parameter to Flang for LSeg since it outputs pixel-aligned features. | component/input/data sensitivity | p. 8 (4.2. Existence Determination) |
| Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 15: Geometric separation impacts quality: Queries without much geometric separation can blur between objects and foreground-background. In the toaster case, very few viewing ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| No DINO: Removing DINO results in a qualitative deterioration in the smoothness and boundaries of relevancy maps, especially in regions with few surrounding views ... | component/input/data sensitivity | p. 8 (4.4. Ablations) |
| Figure 2: LERF Optimization: Left: LERF represents a field of 3D volumes, parameterized by position x, y, z and scale s (orange cube). To ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose Language Embedded Radiance Fields (LERF), a novel approach that grounds language within NeRF by optimizing embeddings from an offthe-shelf ... | OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Localization), p. 8 (4.4. Ablations), p. 7 (4. Experiments), p. 7 (4.1. Qualitative Results), p. 4 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Primary metric/result | We show two illustrative examples where DINO improves the quality of relevancy maps in Fig. | numeric claim only at cited anchor | p. 8 (4.4. Ablations) |

- Numeric sentences retained from the body:
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** The hashgrid used for representing language features is much larger than a typical RGB hashgrid: it has 32 layers from a resolution of 16 to ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** The CLIP MLP used for Flang has 3 hidden layers with width 256 before the final 512 dimension CLIP output.
- **p. 7 / 3.6. Implementation Details - extractive body cue:** All models are trained to 30,000 steps (45 minutes), although good results can be obtained in as few as 6,000(8 minutes) as presented in the ...
- **p. 7 / 4. Experiments - extractive body cue:** Emphasizing the capability of LERF to handle real-world data, we collect 13 scenes containing a mixture of in-the-wild (grocery store, kitchen, bookstore) and posed long-tail ...
- **p. 7 / 4. Experiments - extractive body cue:** We capture scenes using the iPhone app Polycam, which runs on-board SLAM to find camera poses, and use images of resolution 994×738.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | LERF has limitations associated with both CLIP and NeRF; some are visualized in Fig. | p. 8 (5. Limitations) |
| body limitation/failure cue | Figure 7: Comparison to LSeg in 3D: LSeg performs well on "glass of water" since cups are in the COCO dataset, but cannot locate ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Failure cases: LERF struggles with identifying objects that appear visually similar to the query: "Zucchini" also acti- vates on other long, green-ish ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 10: Language and visual ambiguities from CLIP: Cases with incorrect relevancy renders. Some failures can be attributed to visual similarity to the query ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | Figure 15: Geometric separation impacts quality: Queries without much geometric separation can blur between objects and foreground-background. In the toaster case, very few viewing ... | p. 13 (Figure/Table caption) |
| body limitation/failure cue | Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 ... | p. 7 (3.6. Implementation Details) |
| We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = ... | p. 7 (3.6. Implementation Details) |
| We compare against distilling LSeg features into 3D as in DFF [20], but implemented in our own codebase for an apples-to-apples comparison. | p. 8 (4.2. Existence Determination) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Limitations - extractive body cue:** LERF has limitations associated with both CLIP and NeRF; some are visualized in Fig.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Comparison to LSeg in 3D: LSeg performs well on "glass of water" since cups are in the COCO dataset, but cannot locate an ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9: Failure cases: LERF struggles with identifying objects that appear visually similar to the query: "Zucchini" also acti- vates on other long, green-ish vegetables, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 10: Language and visual ambiguities from CLIP: Cases with incorrect relevancy renders. Some failures can be attributed to visual similarity to the query (eg ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 15: Geometric separation impacts quality: Queries without much geometric separation can blur between objects and foreground-background. In the toaster case, very few viewing an- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant λlang ...

- **Evidence anchors reviewed:** datasets p. 7 (4. Experiments), p. 7 (4. Experiments), p. 8 (4.3. Localization), p. 8 (4.1. Qualitative Results), metrics p. 8 (4.2. Existence Determination), p. 8 (4.3. Localization), p. 3 (Figure/Table caption), p. 7 (4.1. Qualitative Results), p. 7 (4. Experiments), p. 12 (Figure/Table caption), baselines p. 8 (4.3. Localization), p. 8 (4.3. Localization), p. 7 (4. Experiments), p. 7 (4.1. Qualitative Results), p. 6 (Figure/Table caption), p. 13 (Figure/Table caption), results p. 8 (4.3. Localization), p. 8 (4.4. Ablations), p. 7 (4. Experiments), p. 7 (4.1. Qualitative Results), p. 4 (Figure/Table caption), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
