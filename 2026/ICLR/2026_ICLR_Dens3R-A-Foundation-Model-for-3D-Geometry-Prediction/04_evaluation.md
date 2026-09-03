# Evaluation - Dens3R: A Foundation Model for 3D Geometry Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kxVjQhkAWz; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247872. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 10 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 19 (Figure/Table caption), p. 29 (Figure/Table caption)): Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded scenes,. Our method is capable of ...

## Evaluation Body Digest

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.1 NORMAL AND MATCHING PREDICTION We evaluate our Dens3R on several surface normal prediction datasets that include both indoor and outdoor scenes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.2 POINTMAP AND DEPTH PREDICTION For monocular depth prediction and pointmap prediction, we evaluate our model on several datasets containing both indoor and outdoor scenes.
- **p. 19 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** The dataset includes indoor scenes, outdoor scenes, and object-level data.
- **p. 20 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** We also showcase the training objectives we apply during training, the number of image pairs and the corresponding dataset ratio. dataset to attain the optimal ...
- **p. 19 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** To train the visual foundation model, we collect and reorganize a large-scale training dataset containing various data types.
- **p. 20 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** We summarize and present this dataset information in Tab.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** It can be seen that our method yields higher accuracy and surpasses previous methods across nearly all datasets, demonstrating our superior performance across various evaluation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded scenes,. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 9); A.3 IMPLEMENTATION DETAILS (p. 19).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. ... | p. 24 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Qualitative comparison of depth maps and pointmaps. We compare our method with previous DUSt3R-based methods and demonstrate high-quality depth prediction results. Dens3R ... | p. 10 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, where Dens3R outperforms other methods across multiple benchmarks. | p. 9 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: Ablation and downstream applications. A.2 DOWNSTREAM APPLICATIONS Segmentation Head Training. Dens3R serves as a visual foundation model that can be finetuned for ... | p. 19 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.1 NORMAL AND MATCHING PREDICTION We evaluate our Dens3R on several surface normal prediction datasets that include both indoor and outdoor scenes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.2 POINTMAP AND DEPTH PREDICTION For monocular depth prediction and pointmap prediction, we evaluate our model on several datasets containing both indoor and outdoor scenes.
- **p. 19 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** The dataset includes indoor scenes, outdoor scenes, and object-level data.
- **p. 20 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** We also showcase the training objectives we apply during training, the number of image pairs and the corresponding dataset ratio. dataset to attain the optimal ...
- **p. 19 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** To train the visual foundation model, we collect and reorganize a large-scale training dataset containing various data types.
- **p. 20 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** We summarize and present this dataset information in Tab.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Dens3R is a feed-forward visual foundation model that takes unposed images as input and outputs high-quality 3D pointmap with unified geometric dense prediction. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of Dens3R. We propose Dens3R, a dense visual transformer backbone featuring a shared encoder-decoder architecture and multiple task-specific heads for geometric prediction. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Normal comparison. We demonstrate that the normal derived directly from the scale- invariant pointmap and MoGe both are not accurate enough. tasks-particularly surface ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded scenes,. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparison of normal prediction. We report the mean and median angular errors with each cell colored to indicate the best and the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Benchmark on image matching on ZEB dataset. We report the AUC values with each cell colored to indicate the best and the second ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative comparison of depth maps and pointmaps. We compare our method with previous DUSt3R-based methods and demonstrate high-quality depth prediction results. Dens3R also ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Normal quantitative metrics for ablation. We demonstrate that both the intrinsic-invariant training and coarse-to-fine strategy contributes to accurate normal predictions.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 NORMAL AND MATCHING PREDICTION We evaluate our Dens3R on several surface normal prediction datasets that include both indoor and outdoor scenes. | embodiment, simulator version and control stack | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Task/environment | 4.2 POINTMAP AND DEPTH PREDICTION For monocular depth prediction and pointmap prediction, we evaluate our model on several datasets containing both indoor and outdoor ... | reset, timeout, object/scene variation | p. 9 (4 EXPERIMENTS), p. 19 (A.3 IMPLEMENTATION DETAILS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (3 METHOD), p. 5 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| It can be seen that our method yields higher accuracy and surpasses previous methods across nearly all datasets, demonstrating our superior performance across various ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 1: Quantitative comparison of normal prediction. We report the mean and median angular errors with each cell colored to indicate the best and ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 5: Qualitative comparison of depth maps and pointmaps. We compare our method with previous DUSt3R-based methods and demonstrate high-quality depth prediction results. Dens3R ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 7: Quantitative comparison on monocular depth prediction. We report the relative point error (REL), root mean square error (RMSE) and the percentage of ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 3: Normal comparison. We demonstrate that the normal derived directly from the scale- invariant pointmap and MoGe both are not accurate enough. tasks-particularly ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 6: High-quality geometric predictions for high-resolution (2K) inputs. Please zoom in to better observe the fine-grained details. Position-Interpolated Rotary Positional Encoding. Dens3R can ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| 1, where Dens3R outperforms other methods across multiple benchmarks. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Table 9: Two-view matching comparison on ScanNet-1500 Dataset. We report the AUC values with each cell colored to indicate the best and the second ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| The qualitative comparison is shown in Fig. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| Figure 3: Normal comparison. We demonstrate that the normal derived directly from the scale- invariant pointmap and MoGe both are not accurate enough. tasks-particularly ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 3: Normal quantitative metrics for ablation. We demonstrate that both the intrinsic-invariant training and coarse-to-fine strategy contributes to accurate normal predictions. | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Our method achieves high-quality pointmap prediction and depth estimation with the intrinsic-invariant pointmap and the novel training strategy. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Figure 2: Overview of Dens3R. We propose Dens3R, a dense visual transformer backbone featuring a shared encoder-decoder architecture and multiple task-specific heads for geometric ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 3: Normal comparison. We demonstrate that the normal derived directly from the scale- invariant pointmap and MoGe both are not accurate enough. tasks-particularly ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For the training strategy, we propose a novel two-staged approach. | Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 10 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 19 (Figure/Table caption), p. 29 (Figure/Table caption) |
| Primary metric/result | Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. ... | numeric claim only at cited anchor | p. 24 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | We compare our depth prediction results with VGGT and Dens3R demonstrates more robust and accurate predictions. | p. 28 (A.8 LIMITATION) |
| body limitation/failure cue | Figure 1: Dens3R is a feed-forward visual foundation model that takes unposed images as input and outputs high-quality 3D pointmap with unified geometric dense ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | As for pointmap prediction, MoGe and VGGT often fail to recover depth for reflective surfaces and tend to produce flattened pointmaps in background regions. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 6: High-quality geometric predictions for high-resolution (2K) inputs. Please zoom in to better observe the fine-grained details. Position-Interpolated Rotary Positional Encoding. Dens3R can ... | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared ... | p. 18 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As for model inference, our model only requires a single Nvidia RTX3090 GPU for 1024-resolution image inputs. | p. 20 (A.3 IMPLEMENTATION DETAILS) |
| (2025a;b), we first employ a sharedweight encoder to process input image sequences and extract image features Feai, which are then fed into the decoder. | p. 5 (3 METHOD) |
| Unlike previous works, our approach introduces a novel weight-sharing mechanism within the decoders, allowing the backbone to better capture spatial relationships across viewpoints and ... | p. 5 (3 METHOD) |
| For detailed implementation, we explicitly connect normal to the pointmap representation, that is P n i = Pi ⊕n, (9) where ⊕represents feature concatenation ... | p. 7 (3 METHOD) |
| Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and ... | p. 7 (3 METHOD) |
| (2024) by using a shared decoder rather than separate decoders for a main and a reference view. | p. 8 (3 METHOD) |
| In practice, we first compute matches in a one-versus-all strategy using our model, and then triangulate these matches to obtain multi-view point clouds, following ... | p. 8 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. inputs ...
- **p. 28 / A.8 LIMITATION - extractive body cue:** We compare our depth prediction results with VGGT and Dens3R demonstrates more robust and accurate predictions.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Dens3R is a feed-forward visual foundation model that takes unposed images as input and outputs high-quality 3D pointmap with unified geometric dense prediction. ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As for pointmap prediction, MoGe and VGGT often fail to recover depth for reflective surfaces and tend to produce flattened pointmaps in background regions.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 6: High-quality geometric predictions for high-resolution (2K) inputs. Please zoom in to better observe the fine-grained details. Position-Interpolated Rotary Positional Encoding. Dens3R can support ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared encoder-decoder ...

- **Evidence anchors reviewed:** datasets p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3 IMPLEMENTATION DETAILS), p. 20 (A.3 IMPLEMENTATION DETAILS), p. 19 (A.3 IMPLEMENTATION DETAILS), p. 20 (A.3 IMPLEMENTATION DETAILS), metrics p. 9 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 24 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 23 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 24 (Figure/Table caption), p. 10 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 19 (Figure/Table caption), p. 29 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
