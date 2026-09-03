# Evaluation - Grounding Image Matching in 3D with MASt3R

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2406.09756; PDF retrieval source: https://arxiv.org/pdf/2406.09756. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization), p. 9 (4.4. Visual localization), p. 9 (4.5. Multiview 3D reconstruction), p. 8 (4.3. Relative pose estimation), p. 6 (Figure/Table caption)): Surprisingly, the performance significantly improves for intermediate values of subsampling.

## Evaluation Body Digest

- **p. 6 / 4.1. Training - extractive body cue:** These datasets feature diverse scene types: indoor, outdoor, synthetic, real-world, object-centric, etc.
- **p. 6 / 4. Experimental results - extractive body cue:** Then, we evaluate on several tasks, each time comparing with the state of the art, starting with visual camera pose estimation on the Map-Free Relocalization ...
- **p. 7 / 4.2. Map-free localization - extractive body cue:** We start our experiments with the Map-free relocalization benchmark [5], an extremely challenging dataset aiming at localizing the camera in metric space given a single ...
- **p. 9 / 4.4. Visual localization - extractive body cue:** We also include direct regression results, which are rather poor, showing a striking impact of the dataset scale on the localization error, i.e. small scenes ...
- **p. 7 / 4.2. Map-free localization - extractive body cue:** It comprises a training, validation and test sets of 460, 65 and 130 scenes resp., each featuring two video sequences.
- **p. 8 / 4.2. Map-free localization - extractive body cue:** (m,°) ↓ Precision ↑ AUC ↑ (I) DUSt3R 3d DPT 125.8 px 45.2% 0.704 1.10m 9.4° 17.0% 0.344 (II) MASt3R 3d DPT 112.0 px 49.9% ...
- **p. 8 / 4.2. Map-free localization - extractive body cue:** Grounding Image Matching in 3D with MASt3R Table 1: Results on the validation set of the Map-free dataset.
- **p. 9 / 4.5. Multiview 3D reconstruction - extractive body cue:** We evaluate our predictions on the DTU [3] dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Map-free localization | EMPIRICAL / REAL-ROBOT OR HARDWARE | Surprisingly, the performance significantly improves for intermediate values of subsampling. | p. 7 (4.2. Map-free localization) |
| 4.2. Map-free localization | EMPIRICAL / REAL-ROBOT OR HARDWARE | A large part of the improvement is of course due to MASt3R predicting metric depth, but note that our variant leveraging depth from DPT-KITTI ... | p. 7 (4.2. Map-free localization) |
| 4.4. Visual localization | EMPIRICAL / REAL-ROBOT OR HARDWARE | As expected, a greater number of retrieved images (top40) yields better performance, achieving competitive performance on Aachen and significantly outperforming the state of the ... | p. 9 (4.4. Visual localization) |
| 4.5. Multiview 3D reconstruction | EMPIRICAL / REAL-ROBOT OR HARDWARE | Data-driven approaches trained on this domain significantly outperform handcrafted ones, cutting the Chamfer error by half. | p. 9 (4.5. Multiview 3D reconstruction) |
| 4.3. Relative pose estimation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, on RealEstate our mAA score improves by at least 8.7 points over the best multi-view methods and 15.2 points over pairwise DUSt3R. | p. 8 (4.3. Relative pose estimation) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Training - extractive body cue:** These datasets feature diverse scene types: indoor, outdoor, synthetic, real-world, object-centric, etc.
- **p. 6 / 4. Experimental results - extractive body cue:** Then, we evaluate on several tasks, each time comparing with the state of the art, starting with visual camera pose estimation on the Map-Free Relocalization ...
- **p. 7 / 4.2. Map-free localization - extractive body cue:** We start our experiments with the Map-free relocalization benchmark [5], an extremely challenging dataset aiming at localizing the camera in metric space given a single ...
- **p. 9 / 4.4. Visual localization - extractive body cue:** We also include direct regression results, which are rather poor, showing a striking impact of the dataset scale on the localization error, i.e. small scenes ...
- **p. 7 / 4.2. Map-free localization - extractive body cue:** It comprises a training, validation and test sets of 460, 65 and 130 scenes resp., each featuring two video sequences.
- **p. 8 / 4.2. Map-free localization - extractive body cue:** (m,°) ↓ Precision ↑ AUC ↑ (I) DUSt3R 3d DPT 125.8 px 45.2% 0.704 1.10m 9.4° 17.0% 0.344 (II) MASt3R 3d DPT 112.0 px 49.9% ...
- **p. 8 / 4.2. Map-free localization - extractive body cue:** Grounding Image Matching in 3D with MASt3R Table 1: Results on the validation set of the Map-free dataset.
- **p. 9 / 4.5. Multiview 3D reconstruction - extractive body cue:** We evaluate our predictions on the DTU [3] dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Dense Correspondences. MASt3R extends DUSt3R as it predicts dense correspondences, even in regions where camera motion significantly degrades the visual similarity. Focal length ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the proposed approach. Given two input images to match, our network regresses for each image and each input pixel a 3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Fast reciprocal matching. Left: Illustration of the fast matching process, starting from an initial subset of pixels 𝑈0 and propagating it iteratively using ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results on the validation set of the Map-free dataset. (First and second best) match VCRE (<90px) Pose Error depth Reproj. ↓ Prec. ↑ ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Comparison with the state of the art on the test set of the Map-free dataset. VCRE (<90px) Pose Error depth Reproj. ↓ Prec. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative examples on the Map-free dataset. Top row: Pairs with strong viewpoint changes. Third one is a failure case. For clarity, we only ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Left: Multi-view pose regression on the CO3Dv2 [67] and RealEstate10K [121] with 10 random frames. Parenthesis () denote methods that do not report ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: Visual localization results on Aachen Day-Night and InLoc. We report our results for different number of retrieved database images (topN). Methods AachenDayNight[118] InLoc[84] ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These datasets feature diverse scene types: indoor, outdoor, synthetic, real-world, object-centric, etc. | embodiment, simulator version and control stack | p. 6 (4.1. Training), p. 6 (4. Experimental results) |
| Task/environment | Then, we evaluate on several tasks, each time comparing with the state of the art, starting with visual camera pose estimation on the Map-Free ... | reset, timeout, object/scene variation | p. 6 (4. Experimental results), p. 7 (4.2. Map-free localization) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 3 (3.1. The DUSt3R framework) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1. The DUSt3R framework), p. 4 (3.2. Matching prediction head and loss) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In table 3 we report the average accuracy, completeness and Chamfer distances error metrics as provided by the authors of the benchmarks. | definition/direction/unit from same section | p. 9 (4.5. Multiview 3D reconstruction) |
| Following the benchmark, we evaluate in term of Virtual Correspondence Reprojection Error (VCRE) and camera pose accuracy, see [5] for details. | definition/direction/unit from same section | p. 7 (4.2. Map-free localization) |
| In this case, the performance overall degrades compared to training with both 3D and matching losses (IV), in particular in term of pose estimation ... | definition/direction/unit from same section | p. 7 (4.2. Map-free localization) |
| This showcases the accuracy and robustness of our approach to few input view setups. | definition/direction/unit from same section | p. 8 (4.3. Relative pose estimation) |
| We also include direct regression results, which are rather poor, showing a striking impact of the dataset scale on the localization error, i.e. small ... | definition/direction/unit from same section | p. 9 (4.4. Visual localization) |
| VCRE (<90px) Pose Error depth Reproj. ↓ Prec. ↑ AUC ↑ Med. | definition/direction/unit from same section | p. 8 (4.2. Map-free localization) |
| To generate ground-truth correspondences necessary for the matching loss (eq. | definition/direction/unit from same section | p. 6 (4.1. Training) |
| Among the methods that operate in a zero-shot setting (e), MASt3R is the only one attaining reasonable performance. | definition/direction/unit from same section | p. 10 (4.5. Multiview 3D reconstruction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| MASt3R not only outperforms the DUSt3R baseline but also compete with the best methods, all without leveraging camera calibration nor poses for matching, neither ... | comparison identity and matched condition | p. 9 (4.5. Multiview 3D reconstruction) |
| Overall, MASt3R outperforms all state-of-the-art approaches by a large margin, achieving more than 93% in VCRE AUC. | comparison identity and matched condition | p. 7 (4.2. Map-free localization) |
| First, we note that all proposed methods significantly outperforms the DUSt3R baseline, probably because MASt3R is trained longer and with more data. | comparison identity and matched condition | p. 7 (4.2. Map-free localization) |
| This because images usually observe a small object, combined with the fact that many pairs have a wide baseline, sometimes up to 180◦. | comparison identity and matched condition | p. 8 (4.3. Relative pose estimation) |
| Data-driven approaches trained on this domain significantly outperform handcrafted ones, cutting the Chamfer error by half. | comparison identity and matched condition | p. 9 (4.5. Multiview 3D reconstruction) |
| Figure 2: Overview of the proposed approach. Given two input images to match, our network regresses for each image and each input pixel a ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablations on losses and matching modes. | component/input/data sensitivity | p. 7 (4.2. Map-free localization) |
| We also provide the results of direct regression with MASt3R, i.e. without matching, simply using PnP on the pointmap 𝑋2,1 of the second image. | component/input/data sensitivity | p. 7 (4.2. Map-free localization) |
| We remove spurious 3D points via geometric consistency post-processing [99]. | component/input/data sensitivity | p. 9 (4.5. Multiview 3D reconstruction) |
| Note that the matching is performed in full resolution without prior knowledge of cameras, and the latter are only used to triangulate matches in ... | component/input/data sensitivity | p. 9 (4.5. Multiview 3D reconstruction) |
| Figure 3: Fast reciprocal matching. Left: Illustration of the fast matching process, starting from an initial subset of pixels 𝑈0 and propagating it iteratively ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 6: Detailed hyper-parameters for the training Hyper-parameters fine-tuning Optimizer AdamW Base learning rate 1e-4 Weight decay | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| First, we propose MASt3R, a 3D-aware matching approach building on the recently released DUSt3R framework. | Surprisingly, the performance significantly improves for intermediate values of subsampling. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization), p. 9 (4.4. Visual localization), p. 9 (4.5. Multiview 3D reconstruction), p. 8 (4.3. Relative pose estimation), p. 6 (Figure/Table caption) |
| Primary metric/result | A large part of the improvement is of course due to MASt3R predicting metric depth, but note that our variant leveraging depth from DPT-KITTI ... | numeric claim only at cited anchor | p. 7 (4.2. Map-free localization) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Training - extractive body cue:** We train our network for 35 epoch with a cosine schedule and initial learning rate set to 0.0001.
- **p. 7 / 4.2. Map-free localization - extractive body cue:** It comprises a training, validation and test sets of 460, 65 and 130 scenes resp., each featuring two video sequences.
- **p. 7 / 4.2. Map-free localization - extractive body cue:** We do not resort to coarse-tofine matching for this dataset, as the image resolution is already close to MASt3R working resolution (720×540 vs.
- **p. 8 / 4.3. Relative pose estimation - extractive body cue:** CO3Dv2 contains 6 million frames extracted from approximately 37k videos, covering 51 MS-COCO categories.
- **p. 8 / 4.3. Relative pose estimation - extractive body cue:** Groundtruth camera poses are obtained using COLMAP [75] from 200 frames in each video.
- **p. 8 / 4.3. Relative pose estimation - extractive body cue:** Each sequence is 10 frames long, we evaluate relative camera poses between all possible 45 pairs, not using ground-truth focals.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A second cycle (or more) thus cannot exist in G𝑖. □ Lemma B.2. | p. 14 (5. Conclusion) |
| body limitation/failure cue | All nodes, i.e. pixels, belong to G since we add an edge for each pixel's nearest neighbor, but note that all pixels cannot reach ... | p. 14 (5. Conclusion) |
| body limitation/failure cue | 9, it is clearly visible that the FRM provides a sampling biased towards finding reciprocal matches with large basins (bottom), since a greater number ... | p. 16 (5. Conclusion) |
| body limitation/failure cue | Figure 4: Qualitative examples on the Map-free dataset. Top row: Pairs with strong viewpoint changes. Third one is a failure case. For clarity, we ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | If we cannot find enough correspondences, we pad with random false correspondences so that the likelihood of finding a true match remains constant. | p. 7 (4.1. Training) |
| body limitation/failure cue | We successfully improved DUSt3R with matching, getting the best of both worlds: enhanced robustness, while attaining and even surpassing what could be done with ... | p. 10 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our network for 35 epoch with a cosine schedule and initial learning rate set to 0.0001. | p. 6 (4.1. Training) |
| Similar to [102], we randomize the image aspect ratio at training time, ensuring that the largest image dimension is 512 pixels. | p. 6 (4.1. Training) |
| This confirms our initial analysis that regression is inherently unsuited to compute pixel correspondences, see section 3.2. | p. 7 (4.2. Map-free localization) |
| As mentioned in section 3.3, computing dense reciprocal matching is prohibitively slow even with optimized code for searching nearest neighbors. | p. 7 (4.2. Map-free localization) |
| While optimizing the nearest-neighbor (NN) search is possible, e.g. using K-d trees [1], this kind of optimization becomes typically very inefficient in high dimensional ... | p. 5 (3.3. Fast reciprocal matching) |
| The new representations augmented with this spatial information are denoted as 𝐻1 and 𝐻2: 𝐻′1, 𝐻′2 = Decoder(𝐻1, 𝐻2). | p. 4 (3.1. The DUSt3R framework) |
| Both images are first encoded in a Siamese manner with a ViT [23], yielding two representations 𝐻1 and 𝐻2: 𝐻1 = Encoder(𝐼1), (1) 𝐻2 ... | p. 4 (3.1. The DUSt3R framework) |
| Larger images would require significantly more compute power to train, and ViTs do not generalize yet to larger test-time resolutions [62,65]. | p. 5 (3.4. Coarse-to-fine matching) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5. Conclusion - extractive body cue:** A second cycle (or more) thus cannot exist in G𝑖. □ Lemma B.2.
- **p. 14 / 5. Conclusion - extractive body cue:** All nodes, i.e. pixels, belong to G since we add an edge for each pixel's nearest neighbor, but note that all pixels cannot reach all ...
- **p. 16 / 5. Conclusion - extractive body cue:** 9, it is clearly visible that the FRM provides a sampling biased towards finding reciprocal matches with large basins (bottom), since a greater number of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative examples on the Map-free dataset. Top row: Pairs with strong viewpoint changes. Third one is a failure case. For clarity, we only ...
- **p. 7 / 4.1. Training - extractive body cue:** If we cannot find enough correspondences, we pad with random false correspondences so that the likelihood of finding a true match remains constant.
- **p. 10 / 5. Conclusion - extractive body cue:** We successfully improved DUSt3R with matching, getting the best of both worlds: enhanced robustness, while attaining and even surpassing what could be done with pixel ...

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Training), p. 6 (4. Experimental results), p. 7 (4.2. Map-free localization), p. 9 (4.4. Visual localization), p. 7 (4.2. Map-free localization), p. 8 (4.2. Map-free localization), metrics p. 9 (4.5. Multiview 3D reconstruction), p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization), p. 8 (4.3. Relative pose estimation), p. 9 (4.4. Visual localization), p. 8 (4.2. Map-free localization), baselines p. 9 (4.5. Multiview 3D reconstruction), p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization), p. 8 (4.3. Relative pose estimation), p. 9 (4.5. Multiview 3D reconstruction), p. 4 (Figure/Table caption), results p. 7 (4.2. Map-free localization), p. 7 (4.2. Map-free localization), p. 9 (4.4. Visual localization), p. 9 (4.5. Multiview 3D reconstruction), p. 8 (4.3. Relative pose estimation), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
