# Evaluation - NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.3. Qualitative Results), p. 7 (5.4. Computational Efficiency Analysis), p. 6 (5.2. Quantitative Results), p. 8 (5.6. Hyper-parameter Analysis), p. 8 (5.6. Hyper-parameter Analysis), p. 3 (Figure/Table caption)): Red bounding boxes highlight key areas where our method has achieved significant improvements in boundary segmentation and spatial continuity.

## Evaluation Body Digest

- **p. 6 / 5.1. Implementation Details - extractive PDF cue:** NVOS consists of eight scenes picked from the LLFF [21] dataset.
- **p. 6 / 5.1. Implementation Details - extractive PDF cue:** Performance comparison (%) on NVOS dataset.
- **p. 7 / 5.2. Quantitative Results - extractive PDF cue:** Qualitative result on NVOS and LERF-OVS datasets.
- **p. 7 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** However, their segmentation accuracy is limited for complex scenes.
- **p. 8 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** Ablation results in trex and orchid scenes.
- **p. 8 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** Ablation study of different components on NVOS dataset.
- **p. 8 / 5.5. Ablation Studies - extractive PDF cue:** The results underscore the critical role of RBF interpolation in providing continuous feature representation, which effectively regulates the NeRF continuous modeling through interpolation features and ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustrate the mutated Gaussian at the boundaries by using the mask of the object. Our method leverages the contin- uous representation capacity of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Implementation Details (p. 6); 5.2. Quantitative Results (p. 6); 5.3. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Red bounding boxes highlight key areas where our method has achieved significant improvements in boundary segmentation and spatial continuity. | p. 7 (5.3. Qualitative Results) |
| 5.4. Computational Efficiency Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves similar computational efficiency to COB-GS and outperforms other maskbased methods in both training and inference efficiency. | p. 7 (5.4. Computational Efficiency Analysis) |
| 5.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The quantitative results (Table 1-Table 3) show that our method outperforms all baselines across all metrics on the NVOS, LERF-OVS, and ScanNet datasets. | p. 6 (5.2. Quantitative Results) |
| 5.6. Hyper-parameter Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | It is shown that τ=0.6 achieves the best balance between maintaining structural integrity and controlling background noise, resulting in excellent visual coherence and detail ... | p. 8 (5.6. Hyper-parameter Analysis) |
| 5.6. Hyper-parameter Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results presented in Table 6 quantitatively confirm the visual finding, where τ=0.6 produces peak performance in both mIoU and B-mIoU. | p. 8 (5.6. Hyper-parameter Analysis) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Implementation Details - extractive PDF cue:** NVOS consists of eight scenes picked from the LLFF [21] dataset.
- **p. 6 / 5.1. Implementation Details - extractive PDF cue:** Performance comparison (%) on NVOS dataset.
- **p. 7 / 5.2. Quantitative Results - extractive PDF cue:** Qualitative result on NVOS and LERF-OVS datasets.
- **p. 7 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** However, their segmentation accuracy is limited for complex scenes.
- **p. 8 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** Ablation results in trex and orchid scenes.
- **p. 8 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** Ablation study of different components on NVOS dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustrate the mutated Gaussian at the boundaries by using the mask of the object. Our method leverages the contin- uous representation capacity of ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overall pipeline of our NG-GS framework. It takes a trained 3DGS model as input, and identifies boundary Gaussian points with the help ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Performance comparison (%) on NVOS dataset.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Performance comparison (%) on LERF-OVS dataset.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Performance comparison (%) on ScanNet dataset.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative result on NVOS and LERF-OVS datasets. The results show that our method segments the boundaries of the object more clearly, without blurred ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Time consumption comparison in the fortress scene.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation study of different components on NVOS dataset. Components Performance Bd. Sp. RBF. MRHE. NeRF. Lalign. Lsmth. B-mIoU mAcc mIoU ✓ ✓ ✓ ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | NVOS consists of eight scenes picked from the LLFF [21] dataset. | embodiment, simulator version and control stack | p. 6 (5.1. Implementation Details), p. 6 (5.1. Implementation Details) |
| Task/environment | Performance comparison (%) on NVOS dataset. | reset, timeout, object/scene variation | p. 6 (5.1. Implementation Details), p. 7 (5.2. Quantitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 5 (4.2. NeRF-GS Joint Optimization) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. NeRF), p. 3 (4. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, their segmentation accuracy is limited for complex scenes. | definition/direction/unit from same section | p. 7 (5.4. Computational Efficiency Analysis) |
| The results underscore the critical role of RBF interpolation in providing continuous feature representation, which effectively regulates the NeRF continuous modeling through interpolation features ... | definition/direction/unit from same section | p. 8 (5.5. Ablation Studies) |
| Figure 1. Illustrate the mutated Gaussian at the boundaries by using the mask of the object. Our method leverages the contin- uous representation capacity ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Performance comparison (%) on NVOS dataset. | definition/direction/unit from same section | p. 6 (5.1. Implementation Details) |
| The optimizers for both 3DGS and NeRF employ Adam, with an initial learning rate of 1.6e-4. | definition/direction/unit from same section | p. 6 (5.1. Implementation Details) |
| In the scene fern, it accurately preserves the fine structures of leaves and stems, whereas SAGA and FlashSplat produce fragmented results, and COB-GS introduces ... | definition/direction/unit from same section | p. 7 (5.3. Qualitative Results) |
| 3) in both quantitative performance and visual quality. | definition/direction/unit from same section | p. 8 (5.6. Hyper-parameter Analysis) |
| Figure 2. The overall pipeline of our NG-GS framework. It takes a trained 3DGS model as input, and identifies boundary Gaussian points with the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The proposed method is compared against a range of state-of-the-art baselines, which are categorized into mask-based and feedforward-based approaches. | comparison identity and matched condition | p. 6 (5.1. Implementation Details) |
| The quantitative results (Table 1-Table 3) show that our method outperforms all baselines across all metrics on the NVOS, LERF-OVS, and ScanNet datasets. | comparison identity and matched condition | p. 6 (5.2. Quantitative Results) |
| Our method achieves similar computational efficiency to COB-GS and outperforms other maskbased methods in both training and inference efficiency. | comparison identity and matched condition | p. 7 (5.4. Computational Efficiency Analysis) |
| A qualitative comparison in Figure 4 between our method and reduced (without RBF+MRHE) methods on the trex and orchid scenes visually confirms this analysis. | comparison identity and matched condition | p. 8 (5.5. Ablation Studies) |
| Time consumption comparison in the fortress scene. | comparison identity and matched condition | p. 7 (5.4. Computational Efficiency Analysis) |
| Ablation results in trex and orchid scenes. | comparison identity and matched condition | p. 8 (5.4. Computational Efficiency Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study of different components on NVOS dataset. | component/input/data sensitivity | p. 8 (5.4. Computational Efficiency Analysis) |
| It shows the performance changes on the NOVS dataset when different components are gradually removed from the original network. | component/input/data sensitivity | p. 8 (5.5. Ablation Studies) |
| The results show that our method segments the boundaries of the object more clearly, without blurred Gaussians. | component/input/data sensitivity | p. 7 (5.2. Quantitative Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation ... | Red bounding boxes highlight key areas where our method has achieved significant improvements in boundary segmentation and spatial continuity. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.3. Qualitative Results), p. 7 (5.4. Computational Efficiency Analysis), p. 6 (5.2. Quantitative Results), p. 8 (5.6. Hyper-parameter Analysis), p. 8 (5.6. Hyper-parameter Analysis), p. 3 (Figure/Table caption) |
| Primary metric/result | Our method achieves similar computational efficiency to COB-GS and outperforms other maskbased methods in both training and inference efficiency. | numeric claim only at cited anchor | p. 7 (5.4. Computational Efficiency Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Implementation Details - extractive PDF cue:** Quantitative experiments are conducted on an NVIDIA RTX 3090 GPU with PyTorch, focusing on metrics including mIoU, mAcc, and boundary mIoU (B-mIoU).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Addressing current limitations, our future directions include extending the framework to dynamic scenes and real-time interactive applications, further bridging the gap between representation learning ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | It is shown that τ=0.6 achieves the best balance between maintaining structural integrity and controlling background noise, resulting in excellent visual coherence and detail ... | p. 8 (5.6. Hyper-parameter Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The optimizers for both 3DGS and NeRF employ Adam, with an initial learning rate of 1.6e-4. | p. 6 (5.1. Implementation Details) |
| Method B-mIoU mAcc mIoU COB-GS [37] 52.8 80.2 61.6 Ours 59.6 84.1 64.3 Implementation details. | p. 6 (5.1. Implementation Details) |
| To efficiently encode multi-scale spatial information, we incorporate multi-resolution hash encoding (MRHE), which enhances the representation capacity while maintaining computational efficiency. • NeRF-GS Joint ... | p. 3 (4. Method) |
| After obtaining boundary Gaussian points, we compute their distribution range [Bmin, Bmax] on the image plane. | p. 4 (4.1. Edge Gaussian Continuity) |
| Subsequently, we employ RBF to compute the spatial correlation weight between the query point and its neighbor Gaussian points: wi,j = exp  -∥qi ... | p. 4 (4.1. Edge Gaussian Continuity) |
| 2 2 + wα  αgs i -αnerf i 2 + wv Var (Ri) i , (16) where B represents the set of pixels in ... | p. 5 (4.2. NeRF-GS Joint Optimization) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** Addressing current limitations, our future directions include extending the framework to dynamic scenes and real-time interactive applications, further bridging the gap between representation learning and ...
- **p. 8 / 5.6. Hyper-parameter Analysis - extractive PDF cue:** It is shown that τ=0.6 achieves the best balance between maintaining structural integrity and controlling background noise, resulting in excellent visual coherence and detail preservation.

- **PDF anchors reviewed:** datasets p. 6 (5.1. Implementation Details), p. 6 (5.1. Implementation Details), p. 7 (5.2. Quantitative Results), p. 7 (5.4. Computational Efficiency Analysis), p. 8 (5.4. Computational Efficiency Analysis), p. 8 (5.4. Computational Efficiency Analysis), metrics p. 7 (5.4. Computational Efficiency Analysis), p. 8 (5.5. Ablation Studies), p. 1 (Figure/Table caption), p. 6 (5.1. Implementation Details), p. 6 (5.1. Implementation Details), p. 7 (5.3. Qualitative Results), baselines p. 6 (5.1. Implementation Details), p. 6 (5.2. Quantitative Results), p. 7 (5.4. Computational Efficiency Analysis), p. 8 (5.5. Ablation Studies), p. 7 (5.4. Computational Efficiency Analysis), p. 8 (5.4. Computational Efficiency Analysis), results p. 7 (5.3. Qualitative Results), p. 7 (5.4. Computational Efficiency Analysis), p. 6 (5.2. Quantitative Results), p. 8 (5.6. Hyper-parameter Analysis), p. 8 (5.6. Hyper-parameter Analysis), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
