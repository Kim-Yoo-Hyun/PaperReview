# Evaluation - GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.3. Main results), p. 5 (4.3. Main results), p. 6 (Figure/Table caption)): In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD.

## Evaluation Body Digest

- **p. 4 / 4. Experiment - extractive PDF cue:** Tasks, datasets, and metric nuScenes [3]: For 3D occupancy estimation, we utilize annotations from Occ3D [40].
- **p. 5 / 4.3. Main results - extractive PDF cue:** In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD.
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** We train the models for 12 epochs on both the nuScenes and DDAD.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing type ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 7. Comparison of rendering efficiency between volume ren- dering (VR) [53] and splatting rendering (SR, Ours) on 3D occu- pancy estimation task [3]. The ...
- **p. 5 / 4.3. Main results - extractive PDF cue:** 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. The comparison of the depth map and its synthesis over- lap image with (1) direct bilinear interpolation cross-view synthe- sis [43] and (2) ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Comparison of pose type for stage 2 training on depth estimation task [3]. One stage training directly uses the cross-view loss to the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 4); 4.2. Implementation details (p. 5); 4.3. Main results (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Main results | EMPIRICAL / SOURCE-REPORTED EVALUATION | In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD. | p. 5 (4.3. Main results) |
| 4.3. Main results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods. | p. 5 (4.3. Main results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Comparisons for self-supervised multi-camera depth estimation on the nuScenes [3] and DDAD datasets [13]. The results are averaged over all views without ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 4. Experiment - extractive PDF cue:** Tasks, datasets, and metric nuScenes [3]: For 3D occupancy estimation, we utilize annotations from Occ3D [40].
- **p. 5 / 4.3. Main results - extractive PDF cue:** In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD.
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** We train the models for 12 epochs on both the nuScenes and DDAD.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Problem setting of GaussianOcc. Given a surround image sequence, the spatial camera extrinsic and its correspond- ing 2D semantic annotation, GaussianOcc is able ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. GaussianOcc is a two-stage method. In Stage 1, we train a scale-aware 6D pose network, using a U-Net architecture to predict Gaussian attributes ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Overlap mask in nuScenes [3] and DDAD [13]. though we have the vertices at that region during the splat- ting rendering, after the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. 3D occupancy comparison on the Occ3D dataset with mIoU metric. Since ‘other' and ‘other flat' classes are the invalid prompts for open-vocabulary models, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2. In stage 1, we jointly train the depth estimation network and the 6D pose net, where we train the models for 8 epochs ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparisons for self-supervised multi-camera depth estimation on the nuScenes [3] and DDAD datasets [13]. The results are averaged over all views without median ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of the render depth map and 3D occupancy prediction on the nuScenes and DDAD datasets. 28985
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study for scale-aware depth estimation on the nuScenes dataset [3]. ✓* means the result from the original paper and ✓means the result ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Tasks, datasets, and metric nuScenes [3]: For 3D occupancy estimation, we utilize annotations from Occ3D [40]. | embodiment, simulator version and control stack | p. 4 (4. Experiment), p. 5 (4.3. Main results) |
| Task/environment | In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD. | reset, timeout, object/scene variation | p. 5 (4.3. Main results), p. 5 (4.2. Implementation details) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4.2. Implementation details), p. 5 (4.2. Implementation details) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 7 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 7. Comparison of rendering efficiency between volume ren- dering (VR) [53] and splatting rendering (SR, Ours) on 3D occu- pancy estimation task [3]. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD. | definition/direction/unit from same section | p. 5 (4.3. Main results) |
| 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods. | definition/direction/unit from same section | p. 5 (4.3. Main results) |
| Figure 5. The comparison of the depth map and its synthesis over- lap image with (1) direct bilinear interpolation cross-view synthe- sis [43] and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 4. Comparison of pose type for stage 2 training on depth estimation task [3]. One stage training directly uses the cross-view loss to ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 2. GaussianOcc is a two-stage method. In Stage 1, we train a scale-aware 6D pose network, using a U-Net architecture to predict Gaussian ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4. Visualization of the render depth map and 3D occupancy prediction on the nuScenes and DDAD datasets. 28985 | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods. | comparison identity and matched condition | p. 5 (4.3. Main results) |
| In stage 2, which involves depth estimation from rendering, our method also achieves competitive results compared to those trained with ground truth poses. | comparison identity and matched condition | p. 5 (4.3. Main results) |
| Figure 5. The comparison of the depth map and its synthesis over- lap image with (1) direct bilinear interpolation cross-view synthe- sis [43] and ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 7. Comparison of rendering efficiency between volume ren- dering (VR) [53] and splatting rendering (SR, Ours) on 3D occu- pancy estimation task [3]. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 2. Comparisons for self-supervised multi-camera depth estimation on the nuScenes [3] and DDAD datasets [13]. The results are averaged over all views without ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 5. Comparison of the render result between the volume ren- dering (VR) [53] and splatting rendering (SR, Ours) on depth es- timation task ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. Problem setting of GaussianOcc. Given a surround image sequence, the spatial camera extrinsic and its correspond- ing 2D semantic annotation, GaussianOcc is ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 2. Comparisons for self-supervised multi-camera depth estimation on the nuScenes [3] and DDAD datasets [13]. The results are averaged over all views without ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 3. Ablation study for scale-aware depth estimation on the nuScenes dataset [3]. ✓* means the result from the original paper and ✓means the ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 5. Comparison of the render result between the volume ren- dering (VR) [53] and splatting rendering (SR, Ours) on depth es- timation task ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our core contributions are as follows: • We introduce the first fully self-supervised method for efficient surrounding-view 3D occupancy estimation, featuring the ... | In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.3. Main results), p. 5 (4.3. Main results), p. 6 (Figure/Table caption) |
| Primary metric/result | 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods. | numeric claim only at cited anchor | p. 5 (4.3. Main results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16.
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** In our Gaussian splatting setting, we further upsample the final output to 512×512×32 for improved performance since we observe that a finer voxel grid leads ...
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** In stage 1, we jointly train the depth estimation network and the 6D pose net, where we train the models for 8 epochs on the ...
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** We train the models for 12 epochs on both the nuScenes and DDAD.
- **p. 5 / 4.3. Main results - extractive PDF cue:** This discrepancy might be attributed to differences in perception range-80 meters in nuScenes versus 200 meters in DDAD.
- **p. 5 / 4.2. Implementation details - extractive PDF cue:** In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | As highlighted by the red rectangle, the sky region has a short-range depth value, but this does not appear in the rendered 3D occupancy ... | p. 5 (4.3. Main results) |
| body limitation/failure cue | Note that RenderOcc [36] does not require the 3D occupancy label, but it is not a self-supervised method since it uses the ground truth ... | p. 5 (4.3. Main results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The optimizer and learning rate adjustment strategy follow those used in SimpleOcc [11] and OccNeRF [53]. | p. 5 (4.2. Implementation details) |
| We train the models for 12 epochs on both the nuScenes and DDAD. | p. 5 (4.2. Implementation details) |
| Erode means the erode process to the binary overlap mask and Refine is the refinement of depth estimation network with 2 epochs by fixing ... | p. 7 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing type ...
- **p. 5 / 4.3. Main results - extractive PDF cue:** As highlighted by the red rectangle, the sky region has a short-range depth value, but this does not appear in the rendered 3D occupancy estimation ...
- **p. 5 / 4.3. Main results - extractive PDF cue:** Note that RenderOcc [36] does not require the 3D occupancy label, but it is not a self-supervised method since it uses the ground truth depth ...

- **PDF anchors reviewed:** datasets p. 4 (4. Experiment), p. 5 (4.3. Main results), p. 5 (4.2. Implementation details), metrics p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (4.3. Main results), p. 5 (4.3. Main results), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 5 (4.3. Main results), p. 5 (4.3. Main results), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 5 (4.3. Main results), p. 5 (4.3. Main results), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
