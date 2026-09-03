# Evaluation - UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 5 (Figure/Table caption), p. 6 (4. Experiment Configuration)): For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS and Seathru-NeRF respectively, although it has the second-best ...

## Evaluation Body Digest

- **p. 7 / 4. Experiment Configuration - extractive body cue:** On the other hand, we will also use these three metrics in dynamic scenes after using motion mask provided from dataset to exclude moving objects.
- **p. 6 / 4. Experiment Configuration - extractive body cue:** We used their official implementation, but trained on the same sequence using the same dataset split strategy.
- **p. 8 / 5. Results and Discussion - extractive body cue:** We selected two challenging scenes from the IW dataset [39], which includes motion masks that aid in assessing reconstruction quality by excluding dynamic content.
- **p. 6 / 4. Experiment Configuration - extractive body cue:** The BMM, is applied to the scenes containing dynamic objects.
- **p. 7 / 4. Experiment Configuration - extractive body cue:** Novel view rendering comparison in Panama from Seathru-NeRF dataset [26] and Reef from S-UW.
- **p. 8 / 5. Results and Discussion - extractive body cue:** However, because BMM may imperfectly classify, the reconstruction quality in static areas is somewhat degraded, as seen in the objective results of IW dataset shown ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, respectively. ...
- **p. 7 / 5. Results and Discussion - extractive body cue:** Our approach illustrates effectiveness and robustness across various scenes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment Configuration (p. 6); 5. Results and Discussion (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Results and Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS and Seathru-NeRF ... | p. 7 (5. Results and Discussion) |
| 5. Results and Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results are shown in Table 2 verifies that our architecture can achieve the overall best performance while others suffer from performance degradation. | p. 8 (5. Results and Discussion) |
| 5. Results and Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface. | p. 7 (5. Results and Discussion) |
| 5. Results and Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be ... | p. 8 (5. Results and Discussion) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) that appear to be not cloned ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4. Experiment Configuration - extractive body cue:** On the other hand, we will also use these three metrics in dynamic scenes after using motion mask provided from dataset to exclude moving objects.
- **p. 6 / 4. Experiment Configuration - extractive body cue:** We used their official implementation, but trained on the same sequence using the same dataset split strategy.
- **p. 8 / 5. Results and Discussion - extractive body cue:** We selected two challenging scenes from the IW dataset [39], which includes motion masks that aid in assessing reconstruction quality by excluding dynamic content.
- **p. 6 / 4. Experiment Configuration - extractive body cue:** The BMM, is applied to the scenes containing dynamic objects.
- **p. 7 / 4. Experiment Configuration - extractive body cue:** Novel view rendering comparison in Panama from Seathru-NeRF dataset [26] and Reef from S-UW.
- **p. 8 / 5. Results and Discussion - extractive body cue:** However, because BMM may imperfectly classify, the reconstruction quality in static areas is somewhat degraded, as seen in the objective results of IW dataset shown ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Additionally, underwater scenes typically contain moving elements, such as fish and floating debris, increas- ing complexity. These elements are frequently referred to as ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, respectively. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The diagram of our proposed UW-GS approach, combining a novel color appearance model, physical-based density control and binary motion mask to 3DGS. Our ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) that appear to be not cloned or ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Sample images from S-UW dataset. dataset from [39], and iii) our dataset, S-UW. SeaThru- NeRF [26] comprises four image sequences captured in dif- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Qualitative results of the proposed method evaluated on SeaThru-NeRF and S-UW dataset. ↑refers larger values are better while ↓is opposite. Bold indicates the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Novel view rendering comparison in Panama from Seathru-NeRF dataset [26] and Reef from S-UW. We have shown details blow the images. Please note ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. The first row presents render images while the second row shows their corresponding estimated clean images ˆJ, which are obtained by solely using ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On the other hand, we will also use these three metrics in dynamic scenes after using motion mask provided from dataset to exclude moving ... | embodiment, simulator version and control stack | p. 7 (4. Experiment Configuration), p. 6 (4. Experiment Configuration) |
| Task/environment | We used their official implementation, but trained on the same sequence using the same dataset split strategy. | reset, timeout, object/scene variation | p. 6 (4. Experiment Configuration), p. 8 (5. Results and Discussion) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Overview of UW-GS), p. 4 (3.3. Color Appearance Model) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3.6. Loss Function), p. 6 (3.6. Loss Function) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Our approach illustrates effectiveness and robustness across various scenes. | definition/direction/unit from same section | p. 7 (5. Results and Discussion) |
| This dataset was used for evaluating the BMM performance. | definition/direction/unit from same section | p. 6 (4. Experiment Configuration) |
| Three datasets were used for performance evaluation: i) SeaThru-NeRF [26]; ii) the in-the-wild (IW) Figure 4. | definition/direction/unit from same section | p. 6 (4. Experiment Configuration) |
| In addition, our method demonstrates its capability to distinguish objects from the scattering medium. | definition/direction/unit from same section | p. 7 (5. Results and Discussion) |
| Demonstrate BMM combining three masks can best retain static content during training. | definition/direction/unit from same section | p. 8 (5. Results and Discussion) |
| Performance on different marks in BMM, training in Composite and Sardine scenes [39]. | definition/direction/unit from same section | p. 8 (5. Results and Discussion) |
| Figure 1. Additionally, underwater scenes typically contain moving elements, such as fish and floating debris, increas- ing complexity. These elements are frequently referred to ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We tested our method and compared with three state of the arts: Instant-NGP [33], SeaThru-NeRF [26], and original 3DGS [22]. | comparison identity and matched condition | p. 6 (4. Experiment Configuration) |
| The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface. | comparison identity and matched condition | p. 7 (5. Results and Discussion) |
| For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS and Seathru-NeRF ... | comparison identity and matched condition | p. 7 (5. Results and Discussion) |
| The average results of Composite and Sardine scenes [39] using and without a BMM during training. mentary materials. | comparison identity and matched condition | p. 8 (5. Results and Discussion) |
| Subjectively, our method eliminates dynamic distractors from scene renderings without any additional pre- or postprocessing. | comparison identity and matched condition | p. 8 (5. Results and Discussion) |
| Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 7. Examples of rendering results from Composite and Sar- dine scenes. From left to right: raw videos, results without and with BMM, respectively. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We isolate our contributions using a set of modified architectures: (V1) solely using spherical harmonics to represent view-dependent color (note that MLP will also ... | component/input/data sensitivity | p. 8 (5. Results and Discussion) |
| Figure 1. Additionally, underwater scenes typically contain moving elements, such as fish and floating debris, increas- ing complexity. These elements are frequently referred to ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this issue, we propose a novel approach for color appearance formation. | For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS and Seathru-NeRF ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 5 (Figure/Table caption), p. 6 (4. Experiment Configuration) |
| Primary metric/result | The results are shown in Table 2 verifies that our architecture can achieve the overall best performance while others suffer from performance degradation. | numeric claim only at cited anchor | p. 8 (5. Results and Discussion) |

- Numeric sentences retained from the body:
- **p. 5 / 3.5. Binary Motion Mask - extractive body cue:** For this reason, a 3×3 diffusion kernel B is applied to maintain spatial smoothness as shown in Equation 9.
- **p. 5 / 3.5. Binary Motion Mask - extractive body cue:** Moreover, to avoid high-frequency content being treated as outliers, every 8 × 8 patch R8×8 is classified according to the average value of its 16×16 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be ... | p. 8 (5. Results and Discussion) |
| body limitation/failure cue | The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface. | p. 7 (5. Results and Discussion) |
| body limitation/failure cue | Figure 2. The diagram of our proposed UW-GS approach, combining a novel color appearance model, physical-based density control and binary motion mask to 3DGS. ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) that appear to be not cloned ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Our approach illustrates effectiveness and robustness across various scenes. | p. 7 (5. Results and Discussion) |
| body limitation/failure cue | The results are shown in Table 2 verifies that our architecture can achieve the overall best performance while others suffer from performance degradation. | p. 8 (5. Results and Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For training, we carried out 15,000 iterations in a single RTX3090 GPU. | p. 6 (4. Experiment Configuration) |
| We used their official implementation, but trained on the same sequence using the same dataset split strategy. | p. 6 (4. Experiment Configuration) |
| In our implementation, ωt at the iteration of t is computed as follows: ωt 1 = ϵt ≤Tϵ, (8) where ϵt is a residual, ... | p. 5 (3.5. Binary Motion Mask) |
| Similar to [25], we use an additional MLP f with positon encoded depth and viewing direction input to estimate medium properties: (T D i ... | p. 4 (3.3. Color Appearance Model) |
| Our color appearance model uses view-direction R and depth z encoded by position encoding γ to estimate water condition parameters: attenuation factor T D ... | p. 4 (3.1. Problem formulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Results and Discussion - extractive body cue:** The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.
- **p. 7 / 5. Results and Discussion - extractive body cue:** The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The diagram of our proposed UW-GS approach, combining a novel color appearance model, physical-based density control and binary motion mask to 3DGS. Our ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) that appear to be not cloned or ...
- **p. 7 / 5. Results and Discussion - extractive body cue:** Our approach illustrates effectiveness and robustness across various scenes.
- **p. 8 / 5. Results and Discussion - extractive body cue:** The results are shown in Table 2 verifies that our architecture can achieve the overall best performance while others suffer from performance degradation.

- **Evidence anchors reviewed:** datasets p. 7 (4. Experiment Configuration), p. 6 (4. Experiment Configuration), p. 8 (5. Results and Discussion), p. 6 (4. Experiment Configuration), p. 7 (4. Experiment Configuration), p. 8 (5. Results and Discussion), metrics p. 2 (Figure/Table caption), p. 7 (5. Results and Discussion), p. 6 (4. Experiment Configuration), p. 6 (4. Experiment Configuration), p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), baselines p. 6 (4. Experiment Configuration), p. 7 (5. Results and Discussion), p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 2 (Figure/Table caption), results p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion), p. 5 (Figure/Table caption), p. 6 (4. Experiment Configuration).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
