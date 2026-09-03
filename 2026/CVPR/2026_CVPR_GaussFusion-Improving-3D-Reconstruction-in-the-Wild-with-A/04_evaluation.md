# Evaluation - GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (15.11 FPS), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (5.1. Results), p. 7 (5.1. Results)): The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with significantly improved runtime efficiency, reachin ...

## Evaluation Body Digest

- **p. 6 / 15.11 FPS - extractive body cue:** Testing scenes are drawn from the official test splits of each dataset, which remain unseen during training.
- **p. 7 / 5.1. Results - extractive body cue:** More importantly, we find our joint trained model has improved performance compared to training on a single dataset, indicating that exposure to diverse reconstruction artifacts ...
- **p. 6 / 15.11 FPS - extractive body cue:** Rendering Refinement Performance on DL3DV and RE10K Datasets.
- **p. 7 / 5.1. Results - extractive body cue:** We compare GaussFusion with baseline methods on diverse scenes from DL3DV [31] and RE10K [72].
- **p. 8 / 5.1. Results - extractive body cue:** Ablation on Input Modalities on DL3DV Dataset.
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** For efficiency, all models are trained on one-third of the full dataset.
- **p. 7 / 5.1. Results - extractive body cue:** A slightly higher FID score is observed, which we attribute to the reduced number of denoising steps and minor loss of high-frequency details.
- **p. 7 / 5.1. Results - extractive body cue:** From top to bottom, our model demonstrates strong generalization across various refinement scenarios: (1) inpainting missing regions, (2) outpainting beyond the original view, (3-4) correcting ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 15.11 FPS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with ... | p. 6 (15.11 FPS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4. Qualitative Comparison on 3D Reconstruction. We show the novel-view renderings from the improved 3D reconstruc- tion refined using enhanced views from different ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4. Ablation on Input Modalities on DL3DV Dataset. In- clusion of more geometric cues (depth, normal, alpha, covariance) improves reconstruction fidelity and perceptual ... | p. 8 (Figure/Table caption) |
| 5.1. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | GenFusion [57] and ExploreGS [25], though leveraging a video diffusion framework, achieve lower performance due to in15437 | p. 6 (5.1. Results) |

## Dataset / Benchmark Role

- **p. 6 / 15.11 FPS - extractive body cue:** Testing scenes are drawn from the official test splits of each dataset, which remain unseen during training.
- **p. 7 / 5.1. Results - extractive body cue:** More importantly, we find our joint trained model has improved performance compared to training on a single dataset, indicating that exposure to diverse reconstruction artifacts ...
- **p. 6 / 15.11 FPS - extractive body cue:** Rendering Refinement Performance on DL3DV and RE10K Datasets.
- **p. 7 / 5.1. Results - extractive body cue:** We compare GaussFusion with baseline methods on diverse scenes from DL3DV [31] and RE10K [72].
- **p. 8 / 5.1. Results - extractive body cue:** Ablation on Input Modalities on DL3DV Dataset.
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** For efficiency, all models are trained on one-third of the full dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization or ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian splatting (3DGS). A Gaussian primitive buffer-comprising color, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Rendering Refinement Performance on DL3DV and RE10K Datasets. We compare our method against state-of-the-art 3DGS refinement approaches. The joint training variant achieves the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Feed-forward View Synthesis Results on RE10K [72]. Our method consistently improves feed-forward 3DGS recon- struction on different backbones while baseline methods Difix3D and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Performance on Improving 3D Reconstruction. GaussFusion demonstrates superior performance on most metrics, showcasing the multi-view consistency in our enhanced frames. synthesis, as reported ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative Comparison on Novel-View Refinement. We compare GaussFusion with baseline methods on diverse scenes from DL3DV [31] and RE10K [72]. GaussFusion effectively removes ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative Comparison on 3D Reconstruction. We show the novel-view renderings from the improved 3D reconstruc- tion refined using enhanced views from different methods. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation on Input Modalities on DL3DV Dataset. In- clusion of more geometric cues (depth, normal, alpha, covariance) improves reconstruction fidelity and perceptual quality. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Testing scenes are drawn from the official test splits of each dataset, which remain unseen during training. | embodiment, simulator version and control stack | p. 6 (15.11 FPS), p. 7 (5.1. Results) |
| Task/environment | More importantly, we find our joint trained model has improved performance compared to training on a single dataset, indicating that exposure to diverse reconstruction ... | reset, timeout, object/scene variation | p. 7 (5.1. Results), p. 6 (15.11 FPS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.4. 3D Reconstruction Updating), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| A slightly higher FID score is observed, which we attribute to the reduced number of denoising steps and minor loss of high-frequency details. | definition/direction/unit from same section | p. 7 (5.1. Results) |
| From top to bottom, our model demonstrates strong generalization across various refinement scenarios: (1) inpainting missing regions, (2) outpainting beyond the original view, (3-4) ... | definition/direction/unit from same section | p. 7 (5.1. Results) |
| 4, adding geometric modalities (depth, normal, alpha, covariance) leads to consistent improvements in rendering accuracy and perceptual quality. | definition/direction/unit from same section | p. 8 (5.2. Ablation Studies) |
| GaussFusion demonstrates superior performance on most metrics, showcasing the multi-view consistency in our enhanced frames. synthesis, as reported in Table 1. | definition/direction/unit from same section | p. 6 (5.1. Results) |
| Performance on Improving 3D Reconstruction. | definition/direction/unit from same section | p. 6 (5.1. Results) |
| We find this strategy suboptimal: as shown in Tab. | definition/direction/unit from same section | p. 8 (5.2. Ablation Studies) |
| Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian splatting (3DGS). A Gaussian primitive buffer-comprising ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The model trained exclusively on DL3DV outperforms all baselines trained on the same dataset by a substantial margin in terms of image quality. | comparison identity and matched condition | p. 6 (5.1. Results) |
| GaussFusion consistently outperforms baseline methods. | comparison identity and matched condition | p. 8 (5.1. Results) |
| Figure 3. Qualitative Comparison on Novel-View Refinement. We compare GaussFusion with baseline methods on diverse scenes from DL3DV [31] and RE10K [72]. GaussFusion effectively ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| To ensure a fair comparison, we run all baselines on the same renderings and apply the same reconstruction update strategy described in Sec. | comparison identity and matched condition | p. 6 (15.11 FPS) |
| Our distilled model maintains comparable PSNR, SSIM, and LPIPS to the nondistilled version, while surpassing all baselines with a realtime speed of 16 FPS. | comparison identity and matched condition | p. 7 (5.1. Results) |
| Architecture PSNR↑ SSIM↑ LPIPS↓ FID↓ Baseline w/. | comparison identity and matched condition | p. 8 (5.2. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| GaussFusion effectively removes rendering artifacts such as blur, floaters, ghosting, and texture distortions, producing sharper geometry, cleaner reconstruction than Splatfacto [61], GenFusion [57], DiFiX3D+ ... | component/input/data sensitivity | p. 7 (5.1. Results) |
| We compare three variants of our model: Ours (Single), trained solely on DL3DV [31] with optimization-based data; Ours (Joint), jointly trained on all datasets ... | component/input/data sensitivity | p. 6 (5.1. Results) |
| The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with ... | component/input/data sensitivity | p. 6 (15.11 FPS) |
| Although our method is evaluated on MVSplat outputs without ever being trained on MVSplat predictions, it performs on par with MVSplat360, which is fully ... | component/input/data sensitivity | p. 7 (5.1. Results) |
| Ablation on Input Modalities on DL3DV Dataset. | component/input/data sensitivity | p. 8 (5.1. Results) |
| Ablation on Artifact Simulation and Architecture. | component/input/data sensitivity | p. 8 (5.2. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: • A geometry-informed video-to-video generation model, GaussFusion, conditioned on 3DGS geometric renders, effective for artifact removal across diverse ... | The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (15.11 FPS), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (5.1. Results), p. 7 (5.1. Results) |
| Primary metric/result | Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 15.11 FPS - extractive body cue:** The joint training variant achieves the best overall fidelity and perceptual quality (highest PSNR/SSIM, lowest LPIPS/FID), while the distilled model attains comparable performance with significantly ...
- **p. 6 / 15.11 FPS - extractive body cue:** We train our model on 8 H200 GPUs for 100K steps with a batch size of 8 and a frame resolution of 480×832.
- **p. 6 / 15.11 FPS - extractive body cue:** Training uses the AdamW optimizer with a linear learning rate (LR) warm-up over the first 1K steps, followed by a constant LR of 1×10-5.
- **p. 6 / 15.11 FPS - extractive body cue:** All methods are tested at their native operating resolution and resized to 480×832 for comparison.
- **p. 7 / 5.1. Results - extractive body cue:** Our distilled model maintains comparable PSNR, SSIM, and LPIPS to the nondistilled version, while surpassing all baselines with a realtime speed of 16 FPS.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We discuss our limitations and future work in Supp. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian splatting (3DGS). A Gaussian primitive buffer-comprising ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | 4), which combines optimization- and feed-forward degradations while injecting pose and coverage diversity. | p. 8 (5.2. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our model on 8 H200 GPUs for 100K steps with a batch size of 8 and a frame resolution of 480×832. | p. 6 (15.11 FPS) |
| Training uses the AdamW optimizer with a linear learning rate (LR) warm-up over the first 1K steps, followed by a constant LR of 1×10-5. | p. 6 (15.11 FPS) |
| 1, measuring the average frame rate based on end-to-end inference time on a single H200 GPU. | p. 7 (5.1. Results) |
| A slightly higher FID score is observed, which we attribute to the reduced number of denoising steps and minor loss of high-frequency details. | p. 7 (5.1. Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** We discuss our limitations and future work in Supp.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GaussFusion Overview. Given multi-view images as input, we first obtain an initial 3D Gaussian splatting (3DGS) [23] reconstruction using either per-scene optimization or ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. GaussFusion Video Generator Architecture. Our model refines video latents using geometry-aware conditioning derived from 3D Gaussian splatting (3DGS). A Gaussian primitive buffer-comprising color, ...
- **p. 8 / 5.2. Ablation Studies - extractive body cue:** 4), which combines optimization- and feed-forward degradations while injecting pose and coverage diversity.

- **Evidence anchors reviewed:** datasets p. 6 (15.11 FPS), p. 7 (5.1. Results), p. 6 (15.11 FPS), p. 7 (5.1. Results), p. 8 (5.1. Results), p. 8 (5.2. Ablation Studies), metrics p. 7 (5.1. Results), p. 7 (5.1. Results), p. 8 (5.2. Ablation Studies), p. 6 (5.1. Results), p. 6 (5.1. Results), p. 8 (5.2. Ablation Studies), baselines p. 6 (5.1. Results), p. 8 (5.1. Results), p. 7 (Figure/Table caption), p. 6 (15.11 FPS), p. 7 (5.1. Results), p. 8 (5.2. Ablation Studies), results p. 6 (15.11 FPS), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (5.1. Results), p. 7 (5.1. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
