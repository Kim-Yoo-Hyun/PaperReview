# Evaluation - G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kdPmsMVhZf; PDF retrieval source: https://openreview.net/pdf/b60a6180eda7d6c25e55daf8272250755abe4e62.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 10 (4.2 RESULTS), p. 25 (C.7 IMPLEMENTATION DETAILS), p. 8 (4 EXPERIMENTS), p. 1 (Figure/Table caption), p. 9 (4.2 RESULTS)): Our method significantly outperforms all baselines across both reconstruction and rendering metrics.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The real-world datasets include 6 scenes from ScanNet++ (Yeshwanth et al., 2023), 3 scenes from DeepBlending (Hedman et al., 2018) and 9 scenes from Mip-NeRF ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 SETTINGS Datasets We evaluate our method on both synthetic and real-world datasets.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As the Mip-NeRF 360 dataset lacks ground-truth meshes, we evaluate only the rendering performance for those scenes; for the remaining three datasets, we report the ...
- **p. 9 / 4.2 RESULTS - extractive PDF cue:** In addition to achieving superior results on indoor scenes, as shown in the quantitative and qualitative results on the Mip-NeRF 360 dataset (Tables 2 and ...
- **p. 26 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** We present results for all 5 outdoor scenes in the dataset.
- **p. 9 / 4.2 RESULTS - extractive PDF cue:** 4 and A7), our method also outperforms the baselines on outdoor, non-Manhattan, and less structured scenes.
- **p. 10 / 4.2 RESULTS - extractive PDF cue:** Experiments on the Mip-NeRF 360 dataset validate these advantages.
- **p. 10 / 4.2 RESULTS - extractive PDF cue:** Furthermore, our method maintains robust performance in non-planar or less structured scenes because it is a strict enhancement of the base model.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); 4.2 RESULTS (p. 9); A MORE EXPERIMENT RESULTS (p. 18); A.4 MORE QUALITATIVE RESULTS (p. 20); C.5 DATASET DETAILS (p. 24); C.6 EVALUATION METRICS (p. 24); C.7 IMPLEMENTATION DETAILS (p. 24).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method significantly outperforms all baselines across both reconstruction and rendering metrics. | p. 8 (4 EXPERIMENTS) |
| 4.2 RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Adding plane-aware geometry modeling (PM), either alone or in combination with generative prior (GP), significantly improves geometry reconstruction. | p. 10 (4.2 RESULTS) |
| C.7 IMPLEMENTATION DETAILS | EMPIRICAL / REAL-ROBOT OR HARDWARE | G4Splat outperforms baselines in both visible and unobserved regions, producing superior geometry with improved smoothness and minimal Gaussian artifacts. | p. 25 (C.7 IMPLEMENTATION DETAILS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, all baselines are augmented with MASt3R-SfM (Duisterhof et al., 2025) to provide robust geometric initialization and improve performance in sparse-view scenarios. | p. 8 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: We propose G4SPLAT, which integrates accurate geometry guidance with generative prior to enhance 3D scene reconstruction. Our method significantly improves geometry and ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The real-world datasets include 6 scenes from ScanNet++ (Yeshwanth et al., 2023), 3 scenes from DeepBlending (Hedman et al., 2018) and 9 scenes from Mip-NeRF ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 SETTINGS Datasets We evaluate our method on both synthetic and real-world datasets.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As the Mip-NeRF 360 dataset lacks ground-truth meshes, we evaluate only the rendering performance for those scenes; for the remaining three datasets, we report the ...
- **p. 9 / 4.2 RESULTS - extractive PDF cue:** In addition to achieving superior results on indoor scenes, as shown in the quantitative and qualitative results on the Mip-NeRF 360 dataset (Tables 2 and ...
- **p. 26 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** We present results for all 5 outdoor scenes in the dataset.
- **p. 9 / 4.2 RESULTS - extractive PDF cue:** 4 and A7), our method also outperforms the baselines on outdoor, non-Manhattan, and less structured scenes.
- **p. 10 / 4.2 RESULTS - extractive PDF cue:** Experiments on the Mip-NeRF 360 dataset validate these advantages.
- **p. 10 / 4.2 RESULTS - extractive PDF cue:** Furthermore, our method maintains robust performance in non-planar or less structured scenes because it is a strict enhancement of the base model.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: We propose G4SPLAT, which integrates accurate geometry guidance with generative prior to enhance 3D scene reconstruction. Our method significantly improves geometry and appearance ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of G4SPLAT. For each training loop (Section 3.4), we first extract global 3D planes from all training views and compute plane-aware depth ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Visualization of intermediate results. Our method addresses key issues in prior ap- proaches: (a) MAtCha produces noticeable errors in non-overlapping regions (highlighted by ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Qualitative comparison. Our approach achieves better appearance and geometry recon- struction with fewer Gaussian floaters in both observed and unobserved regions. The second ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparison from 5 input views. Our method significantly outperforms all baselines across both reconstruction and rendering metrics. Top-3 results are highlighted as ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Any-view scene reconstruction. Our method demonstrates strong generalization across diverse scenarios, including indoor and outdoor scenes, unposed scenes and even single-view scenes. 4.2
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative comparison from 9 input views on Mip-NeRF 360.
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation study. GP PM PP Reconstruction Rendering CD↓ F-Score↑ NC↑ PSNR↑

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The real-world datasets include 6 scenes from ScanNet++ (Yeshwanth et al., 2023), 3 scenes from DeepBlending (Hedman et al., 2018) and 9 scenes from ... | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Task/environment | 4.1 SETTINGS Datasets We evaluate our method on both synthetic and real-world datasets. | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.1 BACKGROUND), p. 6 (3.1 BACKGROUND) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.1 BACKGROUND), p. 5 (3.1 BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Metric Definition Chamfer Distance (CD) Accuracy+Completeness 2 Accuracy mean p∈P  min p∗∈P ∗//p -p∗//1  Completeness mean p∗∈P ∗  min p∈P//p -p∗//1 ... | definition/direction/unit from same section | p. 27 (C.7 IMPLEMENTATION DETAILS) |
| Metrics Reconstruction quality is quantified using Chamfer Distance (CD), F-Score, and Normal Consistency (NC), while rendering performance is measured via PSNR, SSIM, and LPIPS. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Moreover, in scenes with complex lighting, where existing baselines struggle to achieve accurate reconstruction even with dense input views, our approach leverages accurate geometry ... | definition/direction/unit from same section | p. 9 (4.2 RESULTS) |
| The accurate planar depth also enables linear alignment of monocular depth maps, improving depth accuracy of unobserved non-planar regions as well. | definition/direction/unit from same section | p. 10 (4.2 RESULTS) |
| LPIPS, F-Score, and NC even decline, as GP alone tends to produce averaged, blurry results for the unseen areas. | definition/direction/unit from same section | p. 10 (4.2 RESULTS) |
| Figure 3: Visualization of intermediate results. Our method addresses key issues in prior ap- proaches: (a) MAtCha produces noticeable errors in non-overlapping regions (highlighted ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Notably, all baselines are augmented with MASt3R-SfM (Duisterhof et al., 2025) to provide robust geometric initialization and improve performance in sparse-view scenarios. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Any-View Scene Reconstruction As demonstrated in Figs. | definition/direction/unit from same section | p. 9 (4.2 RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method significantly outperforms all baselines across both reconstruction and rendering metrics. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 4 and A7), our method also outperforms the baselines on outdoor, non-Manhattan, and less structured scenes. | comparison identity and matched condition | p. 9 (4.2 RESULTS) |
| As shown in Table A1, our method consistently outperforms all baselines regardless of the number of input views. | comparison identity and matched condition | p. 9 (4.2 RESULTS) |
| Our accelerated variant, Ours (DS), which downsamples the initial Gaussians, substantially reduces runtime while still outperforming all baselines. | comparison identity and matched condition | p. 10 (4.2 RESULTS) |
| G4Splat outperforms baselines in both visible and unobserved regions, producing superior geometry with improved smoothness and minimal Gaussian artifacts. | comparison identity and matched condition | p. 25 (C.7 IMPLEMENTATION DETAILS) |
| Baselines We compare our method with several representative baselines. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In addition, we implement a variant of 2DGS augmented with the See3D (Ma et al., 2025). | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| 4.3 ABLATION STUDIES We conduct ablation experiments on Replica dataset to evaluate the contributions of the generative prior (GP), plane-aware geometry modeling (PM), and ... | component/input/data sensitivity | p. 9 (4.2 RESULTS) |
| Published as a conference paper at ICLR 2026 Table 3: Ablation study. | component/input/data sensitivity | p. 10 (4.2 RESULTS) |
| Our accelerated variant, Ours (DS), which downsamples the initial Gaussians, substantially reduces runtime while still outperforming all baselines. | component/input/data sensitivity | p. 10 (4.2 RESULTS) |
| In addition, we evaluate a variant with a downsampled number of Gaussians, which further accelerates training while maintaining competitive performance, as reported in the ... | component/input/data sensitivity | p. 24 (C.7 IMPLEMENTATION DETAILS) |
| Figure 4: Qualitative comparison. Our approach achieves better appearance and geometry recon- struction with fewer Gaussian floaters in both observed and unobserved regions. The ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose a novel method that leverages the plane representation to derive scale-accurate geometric constraints, substantially ... | Our method significantly outperforms all baselines across both reconstruction and rendering metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 10 (4.2 RESULTS), p. 25 (C.7 IMPLEMENTATION DETAILS), p. 8 (4 EXPERIMENTS), p. 1 (Figure/Table caption), p. 9 (4.2 RESULTS) |
| Primary metric/result | Adding plane-aware geometry modeling (PM), either alone or in combination with generative prior (GP), significantly improves geometry reconstruction. | numeric claim only at cited anchor | p. 10 (4.2 RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The real-world datasets include 6 scenes from ScanNet++ (Yeshwanth et al., 2023), 3 scenes from DeepBlending (Hedman et al., 2018) and 9 scenes from Mip-NeRF ...
- **p. 24 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** We implement our model in PyTorch (Paszke et al., 2019) and conduct all experiments on a single NVIDIA A100 GPU, except for the dense-view reconstruction ...
- **p. 27 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** Metric Definition Chamfer Distance (CD) Accuracy+Completeness 2 Accuracy mean p∈P  min p∗∈P ∗//p -p∗//1  Completeness mean p∗∈P ∗  min p∈P//p -p∗//1  ...
- **p. 24 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** We implement our model in PyTorch (Paszke et al., 2019) and conduct all experiments on a single NVIDIA A100 GPU, except for the dense-view reconstruction ...
- **p. 27 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** Metric Definition Chamfer Distance (CD) Accuracy+Completeness 2 Accuracy mean p∈P  min p∗∈P ∗//p -p∗//1  Completeness mean p∗∈P ∗  min p∈P//p -p∗//1  ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, we present more experimental results in Appendix A, failure cases and discuss the method's limitations in Appendix D. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | D FAILURE CASES AND LIMITATIONS In this section, we present and analyze representative failure cases. | p. 24 (C.7 IMPLEMENTATION DETAILS) |
| body limitation/failure cue | Published as a conference paper at ICLR 2026 Input View Novel View Rendering Novel View Geometry (a) (b) Input View Novel View Rendering Novel ... | p. 25 (C.7 IMPLEMENTATION DETAILS) |
| body limitation/failure cue | In contrast, other methods that leverage generative prior exhibit notable limitations. | p. 9 (4.2 RESULTS) |
| body limitation/failure cue | For example, Difix3D+ attains relatively good quality in observed regions but fails to handle unobserved areas. | p. 9 (4.2 RESULTS) |
| body limitation/failure cue | This indicates that directly introducing generative prior fails to perform as expected and leads to shape-appearance ambiguities. | p. 10 (4.2 RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As shown in Table 4, our method achieves high-quality reconstruction with a runtime comparable to other approaches that employ generative prior. | p. 10 (4.2 RESULTS) |
| Our accelerated variant, Ours (DS), which downsamples the initial Gaussians, substantially reduces runtime while still outperforming all baselines. | p. 10 (4.2 RESULTS) |
| We implement our model in PyTorch (Paszke et al., 2019) and conduct all experiments on a single NVIDIA A100 GPU, except for the dense-view ... | p. 24 (C.7 IMPLEMENTATION DETAILS) |
| For each pixel u ∈P v i , we cast a ray from the camera center ov along the ray direction rv(u), and compute ... | p. 5 (3.1 BACKGROUND) |
| This relative map is aligned to an absolute scale using the already computed plane region depths {Dv i } via a linear transformation: Dv(u) ... | p. 5 (3.1 BACKGROUND) |
| From these depth maps, we estimate global 3D planes and compute planeaware depth maps, as described in Section 3.2. | p. 6 (3.1 BACKGROUND) |
| The final per-pixel visibility V v(u) is computed as V v(u) = Q Y q=1 vq, (6) indicating that a pixel is considered visible ... | p. 6 (3.1 BACKGROUND) |
| Subsequently, global 3D planes and plane-aware depths are recomputed, and the Gaussians are fine-tuned with updated supervision. | p. 7 (3.1 BACKGROUND) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Additionally, we present more experimental results in Appendix A, failure cases and discuss the method's limitations in Appendix D.
- **p. 24 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** D FAILURE CASES AND LIMITATIONS In this section, we present and analyze representative failure cases.
- **p. 25 / C.7 IMPLEMENTATION DETAILS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Input View Novel View Rendering Novel View Geometry (a) (b) Input View Novel View Rendering Novel View ...
- **p. 9 / 4.2 RESULTS - extractive PDF cue:** In contrast, other methods that leverage generative prior exhibit notable limitations.
- **p. 9 / 4.2 RESULTS - extractive PDF cue:** For example, Difix3D+ attains relatively good quality in observed regions but fails to handle unobserved areas.
- **p. 10 / 4.2 RESULTS - extractive PDF cue:** This indicates that directly introducing generative prior fails to perform as expected and leads to shape-appearance ambiguities.

- **PDF anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 26 (C.7 IMPLEMENTATION DETAILS), p. 9 (4.2 RESULTS), metrics p. 27 (C.7 IMPLEMENTATION DETAILS), p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 5 (Figure/Table caption), baselines p. 8 (4 EXPERIMENTS), p. 9 (4.2 RESULTS), p. 9 (4.2 RESULTS), p. 10 (4.2 RESULTS), p. 25 (C.7 IMPLEMENTATION DETAILS), p. 8 (4 EXPERIMENTS), results p. 8 (4 EXPERIMENTS), p. 10 (4.2 RESULTS), p. 25 (C.7 IMPLEMENTATION DETAILS), p. 8 (4 EXPERIMENTS), p. 1 (Figure/Table caption), p. 9 (4.2 RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
