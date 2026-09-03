# Evaluation - GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 3 (Figure/Table caption), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings)): 2), our method achieves the best performance across all no-reference metrics, including CLIPIQA, MUSIQ, and NIQE.

## Evaluation Body Digest

- **p. 5 / 5.1. Experiment Settings - extractive body cue:** We evaluate our method on two real-world benchmarks: Mip-NeRF360 [2] and Tanks&Temples [13].
- **p. 6 / 5.1. Experiment Settings - extractive body cue:** Quantitative comparison on the Mip-NeRF360 (1/8 →1/2) and Tanks&Temples (1/4 →1) datasets under the 4× superresolution setting.
- **p. 6 / 5.1. Experiment Settings - extractive body cue:** We follow their official implementations to generate SRenhanced images and train corresponding 3DGS models on the refined datasets.
- **p. 5 / 5.1. Experiment Settings - extractive body cue:** For the 4× super-resolution task, the original MipNeRF360 images (approximately 3000×4000) are downsampled to 1/8 resolution as low-resolution (LR) inputs and 1/2 resolution as high-resolution ...
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** These results demonstrate the robustness of our framework in reconstructing semantically coherent details under large magnification, validating its ability to generalize beyond supervised resolution scales.
- **p. 6 / 5.1. Experiment Settings - extractive body cue:** FID measures the distributional distance between rendered and ground-truth images in the perceptual feature space.
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** 2), our method achieves the best performance across all no-reference metrics, including CLIPIQA, MUSIQ, and NIQE.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Method overview. Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-of- Detail (LoD) representation to perform generative zoom-in reconstruction. Starting ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Experiment Settings (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Experiment Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2), our method achieves the best performance across all no-reference metrics, including CLIPIQA, MUSIQ, and NIQE. | p. 7 (5.1. Experiment Settings) |
| 5.1. Experiment Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | The lower FID further reflects the improved stability and coherence of the reconstructed high-frequency details. | p. 7 (5.1. Experiment Settings) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Comparison between flow-based and depth-based warp- ing. The proposed depth-guided alignment achieves geometri- cally consistent correspondences across views and effectively sup- presses ... | p. 3 (Figure/Table caption) |
| 5.1. Experiment Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | Qualitative comparison of 4× super-resolution results. | p. 6 (5.1. Experiment Settings) |
| 5.1. Experiment Settings | EMPIRICAL / REAL-ROBOT OR HARDWARE | We then render smooth camera trajectories with focal lengths varying continuously from 1× to 64× to evaluate performance across large magnification ranges. | p. 6 (5.1. Experiment Settings) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Experiment Settings - extractive body cue:** We evaluate our method on two real-world benchmarks: Mip-NeRF360 [2] and Tanks&Temples [13].
- **p. 6 / 5.1. Experiment Settings - extractive body cue:** Quantitative comparison on the Mip-NeRF360 (1/8 →1/2) and Tanks&Temples (1/4 →1) datasets under the 4× superresolution setting.
- **p. 6 / 5.1. Experiment Settings - extractive body cue:** We follow their official implementations to generate SRenhanced images and train corresponding 3DGS models on the refined datasets.
- **p. 5 / 5.1. Experiment Settings - extractive body cue:** For the 4× super-resolution task, the original MipNeRF360 images (approximately 3000×4000) are downsampled to 1/8 resolution as low-resolution (LR) inputs and 1/2 resolution as high-resolution ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GaussianZoom progressively magnifies 3D scenes from low-resolution inputs, reconstructing them into multi-view consistent and detail-rich representations. The expandable continuous Level-of-Detail hierarchy organizes primitive ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Comparison between flow-based and depth-based warp- ing. The proposed depth-guided alignment achieves geometri- cally consistent correspondences across views and effectively sup- presses ghosting ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Method overview. Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-of- Detail (LoD) representation to perform generative zoom-in reconstruction. Starting ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparison of 4× super-resolution results. Mip-Splatting reduces aliasing but lacks fine details; SuperGaussian, SRGS and Sequence Matters produces blurry textures; Our method ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison on the Mip-NeRF360 (1/8 →1/2) and Tanks&Temples (1/4 →1) datasets under the 4× super- resolution setting. The best, second best and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparison under extreme zoom-in across multiple focal levels and viewpoints. Competing methods exhibit blurry, textureless results as zoom increases, while our method ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison under the extreme zoom-in setting (magnification factors of 16, 32, and 64). The super-resolution involved methods including SRGS [6] and Sequence ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Fr´echet Video Distance (↓) of super-resolved images on Mip-NeRF360 and Tanks&Temples datasets. The best, second best, and third best entries are marked in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on two real-world benchmarks: Mip-NeRF360 [2] and Tanks&Temples [13]. | embodiment, simulator version and control stack | p. 5 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings) |
| Task/environment | Quantitative comparison on the Mip-NeRF360 (1/8 →1/2) and Tanks&Temples (1/4 →1) datasets under the 4× superresolution setting. | reset, timeout, object/scene variation | p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (4.1. Multi-View Consistent SR Module), p. 2 (1. Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (4.1. Multi-View Consistent SR Module), p. 5 (4.3. Training Objective) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These results demonstrate the robustness of our framework in reconstructing semantically coherent details under large magnification, validating its ability to generalize beyond supervised resolution ... | definition/direction/unit from same section | p. 7 (5.1. Experiment Settings) |
| FID measures the distributional distance between rendered and ground-truth images in the perceptual feature space. | definition/direction/unit from same section | p. 6 (5.1. Experiment Settings) |
| We follow their official implementations to generate SRenhanced images and train corresponding 3DGS models on the refined datasets. | definition/direction/unit from same section | p. 6 (5.1. Experiment Settings) |
| 2), our method achieves the best performance across all no-reference metrics, including CLIPIQA, MUSIQ, and NIQE. | definition/direction/unit from same section | p. 7 (5.1. Experiment Settings) |
| Figure 3. Method overview. Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-of- Detail (LoD) representation to perform generative zoom-in reconstruction. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 3. Fr´echet Video Distance (↓) of super-resolved images on Mip-NeRF360 and Tanks&Temples datasets. The best, second best, and third best entries are marked ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 6. Without prompt guidance, the reconstructed region exhibits semantic and material inconsistencies with the low- resolution inputs, producing mismatched textures or over- simplified ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the extreme zoom-in task, we compare only with SRGS [6] and Sequence Matters [14], as the remaining baselines already exhibit substantial performance gaps ... | comparison identity and matched condition | p. 6 (5.1. Experiment Settings) |
| Compared with 3DGS [10] and Mip-Splatting [39] which do not employ super-resolution, our approach can reconstruct richer fine-scale structures. | comparison identity and matched condition | p. 7 (5.1. Experiment Settings) |
| 4, MipSplatting [39] effectively suppresses aliasing artifacts compared with 3DGS [10], yet its renderings still exhibit limited fine-scale structural and textural detail. | comparison identity and matched condition | p. 7 (5.1. Experiment Settings) |
| Qualitative comparison of 4× super-resolution results. | comparison identity and matched condition | p. 6 (5.1. Experiment Settings) |
| Figure 2. Comparison between flow-based and depth-based warp- ing. The proposed depth-guided alignment achieves geometri- cally consistent correspondences across views and effectively sup- presses ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 6. Effectiveness of VLM guidance in detail synthsis. With- out prompt guidance, the region becomes visually sharper but se- mantically inconsistent with the ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct a series of ablation experiments to analyze the contribution of each component in our framework. | component/input/data sensitivity | p. 7 (5.2. Ablation Studies) |
| Figure 6. Effectiveness of VLM guidance in detail synthsis. With- out prompt guidance, the region becomes visually sharper but se- mantically inconsistent with the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 7. Effectiveness of continuous LoD. Without LoD, opti- mizing a single Gaussian set across scales causes aliasing and se- mantic inconsistency. A multi-view ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| 64, we compute the intersection of camera frustums as region of interest and perform zoom-in generation within this region, which simplifies the setup without ... | component/input/data sensitivity | p. 6 (5.1. Experiment Settings) |
| SRGS [6], which relies on a single-image super-resolution backbone, improves per-view sharpness but fails to maintain crossview coherence, since each frame is enhanced independently ... | component/input/data sensitivity | p. 7 (5.1. Experiment Settings) |
| DLoRAL [26] serves as our video SR backbone, in which the original flow-based warping is replaced by our depth-guided alignment. | component/input/data sensitivity | p. 6 (5.1. Experiment Settings) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Beyond iterative refinement, we introduce an expandable continuous Level-of-Detail (LoD) representation that elevates LoD from a discrete efficiency-oriented mechanism to a continuous generative scaffold. | 2), our method achieves the best performance across all no-reference metrics, including CLIPIQA, MUSIQ, and NIQE. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 3 (Figure/Table caption), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings) |
| Primary metric/result | The lower FID further reflects the improved stability and coherence of the reconstructed high-frequency details. | numeric claim only at cited anchor | p. 7 (5.1. Experiment Settings) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Experiment Settings - extractive body cue:** For the 4× super-resolution task, the original MipNeRF360 images (approximately 3000×4000) are downsampled to 1/8 resolution as low-resolution (LR) inputs and 1/2 resolution as high-resolution ...
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** All experiments are conducted on a single NVIDIA RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work will investigate more capable content creative zoomin approaches to enable seamless transitions from cosmicscale environments down to microscopic and molecular scenes. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 3. Method overview. Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-of- Detail (LoD) representation to perform generative zoom-in reconstruction. ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | SRGS [6], which relies on a single-image super-resolution backbone, improves per-view sharpness but fails to maintain crossview coherence, since each frame is enhanced independently ... | p. 7 (5.1. Experiment Settings) |
| body limitation/failure cue | The super-resolution involved methods including SRGS [6] and Sequence Matters [14] are chosen for comparsion, while SuperGaussian [24] fails to produce meaningful results under ... | p. 7 (5.1. Experiment Settings) |
| body limitation/failure cue | Fig. 6. Without prompt guidance, the reconstructed region exhibits semantic and material inconsistencies with the low- resolution inputs, producing mismatched textures or over- simplified ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow their official implementations to generate SRenhanced images and train corresponding 3DGS models on the refined datasets. | p. 6 (5.1. Experiment Settings) |
| 64, we compute the intersection of camera frustums as region of interest and perform zoom-in generation within this region, which simplifies the setup without ... | p. 6 (5.1. Experiment Settings) |
| All experiments are conducted on a single NVIDIA RTX 4090 GPU. | p. 7 (5.1. Experiment Settings) |
| Depth-based Feature Warping SR Model 𝝐𝜽 ❄ Training For 𝑳𝑵 GS x N steps Full View Pairs Rendering with Zoomed Focal Traverse Image Pairs ... | p. 4 (4.1. Multi-View Consistent SR Module) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** Future work will investigate more capable content creative zoomin approaches to enable seamless transitions from cosmicscale environments down to microscopic and molecular scenes.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Method overview. Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-of- Detail (LoD) representation to perform generative zoom-in reconstruction. Starting ...
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** SRGS [6], which relies on a single-image super-resolution backbone, improves per-view sharpness but fails to maintain crossview coherence, since each frame is enhanced independently without ...
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** The super-resolution involved methods including SRGS [6] and Sequence Matters [14] are chosen for comparsion, while SuperGaussian [24] fails to produce meaningful results under this ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Without prompt guidance, the reconstructed region exhibits semantic and material inconsistencies with the low- resolution inputs, producing mismatched textures or over- simplified surfaces. ...

- **Evidence anchors reviewed:** datasets p. 5 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 5 (5.1. Experiment Settings), metrics p. 7 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 4 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 6 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 3 (Figure/Table caption), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
