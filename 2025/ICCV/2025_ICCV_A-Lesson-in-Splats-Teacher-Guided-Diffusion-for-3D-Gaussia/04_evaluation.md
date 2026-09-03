# Evaluation - A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Peng_A_Lesson_in_Splats_Teacher-Guided_Diffusion_for_3D_Gaussian_Splats_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Peng_A_Lesson_in_Splats_Teacher-Guided_Diffusion_for_3D_Gaussian_Splats_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption)): While PixelNeRF has a smaller model size, our approach achieves lower GPU memory consumption on the ShapeNet-SRN dataset.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setups - extractive body cue:** We conduct experiments using two datasets: the object-level ShapeNet-SRN [6, 51] and the scene-level RealEstate10k [73].
- **p. 5 / 4.1. Experimental Setups - extractive body cue:** RealEstate10k consists of real-world video data captured in both indoor and outdoor environments.
- **p. 5 / 4.2. Implementation Details - extractive body cue:** The computational efficiency is demonstrated in Tab.
- **p. 5 / 4.1. Experimental Setups - extractive body cue:** In our ablation studies, we train a Splatter Image using our "Medium" U-Net and report its performance.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed framework for noisy-teacher-guided training of a 3D Gaussian Splat (3DGS) diffusion model. Using a pre-trained deterministic predictor network for 3DGS, which ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Novel View Synthesis. Our model shows superior performance on RealEstate10k on small, medium and large baseline ranges.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablations Studies on Single view Reconstruction, evaluated on the validation set of ShapeNet-SRN Cars. In (b) and (c) rows, we use Splatter Image ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results. (a) Qualitative comparison on the ShapeNet-SRN dataset. Our model produces views that are more faithful to the source image and better ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setups (p. 5); 4.2. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experimental Setups | EMPIRICAL / REAL-ROBOT OR HARDWARE | While PixelNeRF has a smaller model size, our approach achieves lower GPU memory consumption on the ShapeNet-SRN dataset. | p. 5 (4.1. Experimental Setups) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. ShapeNet-SRN: Single-View Reconstruction (test split). Our method achieves better quality on all metrics on the Car split and Chair dataset, while performing ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Ablations Studies on Single view Reconstruction, evaluated on the validation set of ShapeNet-SRN Cars. In (b) and (c) rows, we use Splatter ... | p. 7 (Figure/Table caption) |
| 4.1. Experimental Setups | EMPIRICAL / REAL-ROBOT OR HARDWARE | In our ablation studies, we train a Splatter Image using our "Medium" U-Net and report its performance. | p. 5 (4.1. Experimental Setups) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Novel View Synthesis. Our model shows superior performance on RealEstate10k on small, medium and large baseline ranges. | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setups - extractive body cue:** We conduct experiments using two datasets: the object-level ShapeNet-SRN [6, 51] and the scene-level RealEstate10k [73].
- **p. 5 / 4.1. Experimental Setups - extractive body cue:** RealEstate10k consists of real-world video data captured in both indoor and outdoor environments.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (Left) Standard diffusion training is constrained to same-modality supervision. We break this barrier by decoupling the sources of noised samples and supervision. Leveraging ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed framework for noisy-teacher-guided training of a 3D Gaussian Splat (3DGS) diffusion model. Using a pre-trained deterministic predictor network for 3DGS, which ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. ShapeNet-SRN: Single-View Reconstruction (test split). Our method achieves better quality on all metrics on the Car split and Chair dataset, while performing reconstruction ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Novel View Synthesis. Our model shows superior performance on RealEstate10k on small, medium and large baseline ranges.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Memory Footprint and Model Size. sampler with 10 inference steps. To manage the increased computational complexity during this phase, the batch size is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablations Studies on Single view Reconstruction, evaluated on the validation set of ShapeNet-SRN Cars. In (b) and (c) rows, we use Splatter Image ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Additional-view guidance. Evaluated on a subset of the car split, our diffusion-based model better utilizes an additional view through guidance compared to 3DGS ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results. (a) Qualitative comparison on the ShapeNet-SRN dataset. Our model produces views that are more faithful to the source image and better ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments using two datasets: the object-level ShapeNet-SRN [6, 51] and the scene-level RealEstate10k [73]. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setups), p. 5 (4.1. Experimental Setups) |
| Task/environment | RealEstate10k consists of real-world video data captured in both indoor and outdoor environments. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setups) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3.3. Cycle Consistency Regularization), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.1. Decoupling Noised Samples from Supervision), p. 6 (4.3. Image Conditioned Reconstruction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The computational efficiency is demonstrated in Tab. | definition/direction/unit from same section | p. 5 (4.2. Implementation Details) |
| In our ablation studies, we train a Splatter Image using our "Medium" U-Net and report its performance. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setups) |
| Figure 2. Our proposed framework for noisy-teacher-guided training of a 3D Gaussian Splat (3DGS) diffusion model. Using a pre-trained deterministic predictor network for 3DGS, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 2. Novel View Synthesis. Our model shows superior performance on RealEstate10k on small, medium and large baseline ranges. | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 4. Ablations Studies on Single view Reconstruction, evaluated on the validation set of ShapeNet-SRN Cars. In (b) and (c) rows, we use Splatter ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 3. Qualitative results. (a) Qualitative comparison on the ShapeNet-SRN dataset. Our model produces views that are more faithful to the source image and ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our model exhibits a significantly smaller size compared to VisionNeRF and Splatter Image. | comparison identity and matched condition | p. 5 (4.1. Experimental Setups) |
| Due to limited computational resources, our diffusion model utilizes a smaller U-Net architecture (Medium) compared to the original Splatter Image model (Large). | comparison identity and matched condition | p. 5 (4.1. Experimental Setups) |
| Table 2. Novel View Synthesis. Our model shows superior performance on RealEstate10k on small, medium and large baseline ranges. | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 5. Additional-view guidance. Evaluated on a subset of the car split, our diffusion-based model better utilizes an additional view through guidance compared to ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 4. Ablations Studies on Single view Reconstruction, evaluated on the validation set of ShapeNet-SRN Cars. In (b) and (c) rows, we use Splatter ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 3. Qualitative results. (a) Qualitative comparison on the ShapeNet-SRN dataset. Our model produces views that are more faithful to the source image and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In our ablation studies, we train a Splatter Image using our "Medium" U-Net and report its performance. | component/input/data sensitivity | p. 5 (4.1. Experimental Setups) |
| Table 4. Ablations Studies on Single view Reconstruction, evaluated on the validation set of ShapeNet-SRN Cars. In (b) and (c) rows, we use Splatter ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Although the bootstrapping stage precedes finetuning in the pipeline, we present it second in this manuscript to facilitate a smoother explanation of our core ... | While PixelNeRF has a smaller model size, our approach achieves lower GPU memory consumption on the ShapeNet-SRN dataset. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Table 1. ShapeNet-SRN: Single-View Reconstruction (test split). Our method achieves better quality on all metrics on the Car split and Chair dataset, while performing ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / Method - extractive body cue:** 5 frames 10 frames U[-30, 30] frames Model PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ↓ PSNR ↑ SSIM ↑ LPIPS ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work could address this limitation by adapting our framework to support alternative 3D representations, further enhancing its robustness and generalizability. | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | Our framework is flexible and could extend to various 3D representations; however, the current implementation relies on pixel-aligned 3D GS, inheriting certain limitations. | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | Figure 1. (Left) Standard diffusion training is constrained to same-modality supervision. We break this barrier by decoupling the sources of noised samples and supervision. ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Our proposed framework for noisy-teacher-guided training of a 3D Gaussian Splat (3DGS) diffusion model. Using a pre-trained deterministic predictor network for 3DGS, ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During the bootstrapping stage (stage 1), a batch size of 100 per GPU is employed to train the diffusion model under the guidance of ... | p. 5 (4.2. Implementation Details) |
| This is due to the increased memory costs of maintaining gradients over multiple denoising steps in 3D space, which limits batch sizes and reduces ... | p. 5 (3.2. Noisy Teacher Bootstrapping) |
| To manage the increased computational complexity during this phase, the batch size is reduced to 10. | p. 6 (Method) |
| Sampling smaller timesteps is not ideal, as the model would then be trained on noisy samples from the incorrect distribution. | p. 4 (3.1. Decoupling Noised Samples from Supervision) |
| Please refer to the implementation details 4.2 for a discussion regarding the computational efficiency of this unrolled optimization. | p. 4 (3.1. Decoupling Noised Samples from Supervision) |
| Further implementation details are provided in the appendix. | p. 6 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** Future work could address this limitation by adapting our framework to support alternative 3D representations, further enhancing its robustness and generalizability.
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** Our framework is flexible and could extend to various 3D representations; however, the current implementation relies on pixel-aligned 3D GS, inheriting certain limitations.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (Left) Standard diffusion training is constrained to same-modality supervision. We break this barrier by decoupling the sources of noised samples and supervision. Leveraging ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed framework for noisy-teacher-guided training of a 3D Gaussian Splat (3DGS) diffusion model. Using a pre-trained deterministic predictor network for 3DGS, which ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setups), p. 5 (4.1. Experimental Setups), metrics p. 5 (4.2. Implementation Details), p. 5 (4.1. Experimental Setups), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 5 (4.1. Experimental Setups), p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4.1. Experimental Setups), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
