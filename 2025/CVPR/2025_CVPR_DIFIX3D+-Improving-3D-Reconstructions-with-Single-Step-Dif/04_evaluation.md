# Evaluation - DIFIX3D+: Improving 3D Reconstructions with Single-Step Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DIFIX3D_Improving_3D_Reconstructions_with_Single-Step_Diffusion_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_DIFIX3D_Improving_3D_Reconstructions_with_Single-Step_Diffusion_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.3. Diagnostics), p. 8 (5.3. Diagnostics), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (5.1. In-the-Wild Artifact Removal), p. 7 (5.1. In-the-Wild Artifact Removal)): We note that simply decreasing the noise level from 1000 to 200 noticeably improves LPIPS and FID significantly, validating our findings in Fig.

## Evaluation Body Digest

- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** We train DIFIX on a random selection of 80% of scenes (112 out of a total of 140) from the DL3DV [23] benchmark dataset.
- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** We evaluate DIFIX3D+ with Nerfacto [58] and 3DGS [20] backbones on the 28 held out scenes from the DL3DV [23] benchmark and the 12 captures ...
- **p. 6 / 5. Experiments - extractive PDF cue:** We further evaluate the generality of our solution by enhancing automotive scenes (Sec.
- **p. 6 / 5. Experiments - extractive PDF cue:** We first evaluate DIFIX3D+ on in-the-wild scenes against several baselines and show its ability to enhance both NeRF and 3DGS-based pipelines (Sec.
- **p. 8 / 5.3. Diagnostics - extractive PDF cue:** 4 averaged over the Nerfbusters [70] dataset.
- **p. 8 / 5.2. Automotive Scene Enhancement - extractive PDF cue:** Ablation study of DIFIX3D+ on Nerfbusters dataset.
- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** We calculate PSNR, SSIM [67], LPIPS [19] as well as FID score [15] on novel views.
- **p. 8 / 5.2. Automotive Scene Enhancement - extractive PDF cue:** Qualitative ablation of real-time post-render processing: DIFIX3D+ uses an additional neural enhancer step that effectively removes residual artifacts, resulting in higher PSNR and lower LPIPS ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Diagnostics | SYSTEM / EVALUATION SCOPE UNRESOLVED | We note that simply decreasing the noise level from 1000 to 200 noticeably improves LPIPS and FID significantly, validating our findings in Fig. | p. 8 (5.3. Diagnostics) |
| 5.3. Diagnostics | SYSTEM / EVALUATION SCOPE UNRESOLVED | Distilling diffusion outputs via 3D updates improves quality significantly but our incremental update strategy is essential, as evidenced by the degradation in LPIPS and ... | p. 8 (5.3. Diagnostics) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 5. In-the-wild artifact removal. We show comparisons on held-out scenes from the DL3DV dataset [23] (top, above the dashed line) and the Nerfbusters ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. DIFIX3D+ pipeline. The overall pipeline of the DIFIX3D+ model involves the following stages: Step 1: Given a pretrained 3D representation, we render ... | p. 2 (Figure/Table caption) |
| 5.1. In-the-Wild Artifact Removal | SYSTEM / EVALUATION SCOPE UNRESOLVED | Both DIFIX3D+ variants reduce LPIPS by 0.1 and FID by almost 3× relative to their respective NeRF and 3DGS backbones, highlighting a significant improvement ... | p. 7 (5.1. In-the-Wild Artifact Removal) |

## Dataset / Benchmark Role

- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** We train DIFIX on a random selection of 80% of scenes (112 out of a total of 140) from the DL3DV [23] benchmark dataset.
- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** We evaluate DIFIX3D+ with Nerfacto [58] and 3DGS [20] backbones on the 28 held out scenes from the DL3DV [23] benchmark and the 12 captures ...
- **p. 6 / 5. Experiments - extractive PDF cue:** We further evaluate the generality of our solution by enhancing automotive scenes (Sec.
- **p. 6 / 5. Experiments - extractive PDF cue:** We first evaluate DIFIX3D+ on in-the-wild scenes against several baselines and show its ability to enhance both NeRF and 3DGS-based pipelines (Sec.
- **p. 8 / 5.3. Diagnostics - extractive PDF cue:** 4 averaged over the Nerfbusters [70] dataset.
- **p. 8 / 5.2. Automotive Scene Enhancement - extractive PDF cue:** Ablation study of DIFIX3D+ on Nerfbusters dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We demonstrate DIFIX3D+ on both in-the-wild scenes (top) and driving scenes (bottom). Recent Novel-View Synthesis methods struggle in sparse-input settings or when rendering ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. DIFIX3D+ pipeline. The overall pipeline of the DIFIX3D+ model involves the following stages: Step 1: Given a pretrained 3D representation, we render novel ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. DIFIX architecture. DIFIX takes a noisy rendered image and a reference views as input (left), and outputs an enhanced version of the input ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Noise level. To validate our hypothesis that the distribution of images with NeRF/3DGS artifacts is similar to the distribution of noisy images used ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Data curation. We curate a paired dataset featuring common artifacts in novel-view synthesis. For DL3DV scenes [23], we employ sparse reconstruction and model ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. In-the-wild artifact removal. We show comparisons on held-out scenes from the DL3DV dataset [23] (top, above the dashed line) and the Nerfbusters [70] ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparison on Nerfbusters and DL3DV datasets. The best result is highlighted in bold, and the second-best is underlined.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Qualitative results on the RDS dataset. DIFIX for RDS was trained on 40 scenes and 100,000 paired data samples.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We train DIFIX on a random selection of 80% of scenes (112 out of a total of 140) from the DL3DV [23] benchmark dataset. | embodiment, simulator version and control stack | p. 7 (5.1. In-the-Wild Artifact Removal), p. 7 (5.1. In-the-Wild Artifact Removal) |
| Task/environment | We evaluate DIFIX3D+ with Nerfacto [58] and 3DGS [20] backbones on the 28 held out scenes from the DL3DV [23] benchmark and the 12 ... | reset, timeout, object/scene variation | p. 7 (5.1. In-the-Wild Artifact Removal), p. 6 (5. Experiments) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (4. Boosting 3D Reconstruction with DM priors), p. 4 (4. Boosting 3D Reconstruction with DM priors) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (4. Boosting 3D Reconstruction with DM priors), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We calculate PSNR, SSIM [67], LPIPS [19] as well as FID score [15] on novel views. | definition/direction/unit from same section | p. 7 (5.1. In-the-Wild Artifact Removal) |
| Qualitative ablation of real-time post-render processing: DIFIX3D+ uses an additional neural enhancer step that effectively removes residual artifacts, resulting in higher PSNR and lower ... | definition/direction/unit from same section | p. 8 (5.2. Automotive Scene Enhancement) |
| We validate our DIFIX training strategy by comparing to pix2pix-Turbo [40], which uses the same SD-Turbo backbone with a higher noise value (τ = ... | definition/direction/unit from same section | p. 8 (5.3. Diagnostics) |
| We generate 80,000 noisy-clean image pairs using the dataset curation strategies listed in Tab. | definition/direction/unit from same section | p. 7 (5.1. In-the-Wild Artifact Removal) |
| Figure 1. We demonstrate DIFIX3D+ on both in-the-wild scenes (top) and driving scenes (bottom). Recent Novel-View Synthesis methods struggle in sparse-input settings or when ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. DIFIX3D+ pipeline. The overall pipeline of the DIFIX3D+ model involves the following stages: Step 1: Given a pretrained 3D representation, we render ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Table 1. Data curation. We curate a paired dataset featuring common artifacts in novel-view synthesis. For DL3DV scenes [23], we employ sparse reconstruction and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 3. DIFIX architecture. DIFIX takes a noisy rendered image and a reference views as input (left), and outputs an enhanced version of the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5.1, our method outperforms its baselines across all metrics (Tab. | comparison identity and matched condition | p. 8 (5.2. Automotive Scene Enhancement) |
| Our method outperforms all comparison methods by a signifi1Nerfbusters [70] uses a visibility map extracted from a NeRF model trained on a combination of ... | comparison identity and matched condition | p. 7 (5.1. In-the-Wild Artifact Removal) |
| We compare a Nerfacto baseline to: (a) directly running DIFIX on rendered views without 3D updates, (b) distilling DIFIX outputs via 3D updates in ... | comparison identity and matched condition | p. 8 (5.2. Automotive Scene Enhancement) |
| We first evaluate DIFIX3D+ on in-the-wild scenes against several baselines and show its ability to enhance both NeRF and 3DGS-based pipelines (Sec. | comparison identity and matched condition | p. 6 (5. Experiments) |
| We use the gsplat library2 for 3DGS-based experiments and the official implementation for all other methods and baselines. | comparison identity and matched condition | p. 7 (5.1. In-the-Wild Artifact Removal) |
| Figure 5. In-the-wild artifact removal. We show comparisons on held-out scenes from the DL3DV dataset [23] (top, above the dashed line) and the Nerfbusters ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Qualitative ablation of real-time post-render processing: DIFIX3D+ uses an additional neural enhancer step that effectively removes residual artifacts, resulting in higher PSNR and lower ... | component/input/data sensitivity | p. 8 (5.2. Automotive Scene Enhancement) |
| Figure 4. Noise level. To validate our hypothesis that the distribution of images with NeRF/3DGS artifacts is similar to the distribution of noisy images ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 4. Ablation study of DIFIX3D+ on Nerfbusters dataset. We compare a Nerfacto baseline to: (a) directly running DIFIX on rendered views without 3D ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We compare our Nerfacto and 3DGS DIFIX3D+ variants to their base methods. | component/input/data sensitivity | p. 7 (5.1. In-the-Wild Artifact Removal) |
| Both DIFIX3D+ variants reduce LPIPS by 0.1 and FID by almost 3× relative to their respective NeRF and 3DGS backbones, highlighting a significant improvement ... | component/input/data sensitivity | p. 7 (5.1. In-the-Wild Artifact Removal) |
| Figure 2. DIFIX3D+ pipeline. The overall pipeline of the DIFIX3D+ model involves the following stages: Step 1: Given a pretrained 3D representation, we render ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| (ii) We propose an update pipeline that progressively refines the 3D representation by distilling back the improved novel views, thus ensuring multi-view consistency and ... | We note that simply decreasing the noise level from 1000 to 200 noticeably improves LPIPS and FID significantly, validating our findings in Fig. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.3. Diagnostics), p. 8 (5.3. Diagnostics), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (5.1. In-the-Wild Artifact Removal), p. 7 (5.1. In-the-Wild Artifact Removal) |
| Primary metric/result | Distilling diffusion outputs via 3D updates improves quality significantly but our incremental update strategy is essential, as evidenced by the degradation in LPIPS and ... | numeric claim only at cited anchor | p. 8 (5.3. Diagnostics) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** DIFIX for RDS was trained on 40 scenes and 100,000 paired data samples.
- **p. 7 / 5.2. Automotive Scene Enhancement - extractive PDF cue:** The automotive capture rig contains three cameras with 40 degree overlaps between each camera.
- **p. 7 / 5.2. Automotive Scene Enhancement - extractive PDF cue:** We train DIFIX with 40 scenes and generate 100,000 image pairs using the augmentation strategies listed in Tab.
- **p. 7 / 5.2. Automotive Scene Enhancement - extractive PDF cue:** We evaluate DIFIX3D+ with a Nerfacto backbone on 20 scenes (none of which are used during 26030
- **p. 5 / 4. Boosting 3D Reconstruction with DM priors - extractive PDF cue:** In nearly linear trajectories, such as those found in autonomous driving datasets, we first train a NeRF on the original path, and then render views ...
- **p. 6 / 4. Boosting 3D Reconstruction with DM priors - extractive PDF cue:** Since DIFIX is a single-step model, the additional rendering time is only 76 ms on a NVIDIA A100 GPU, over 10× faster than standard diffusion ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method outperforms all comparison methods by a signifi1Nerfbusters [70] uses a visibility map extracted from a NeRF model trained on a combination of ... | p. 7 (5.1. In-the-Wild Artifact Removal) |
| body limitation/failure cue | Figure 4. Noise level. To validate our hypothesis that the distribution of images with NeRF/3DGS artifacts is similar to the distribution of noisy images ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | We note that simply decreasing the noise level from 1000 to 200 noticeably improves LPIPS and FID significantly, validating our findings in Fig. | p. 8 (5.3. Diagnostics) |
| body limitation/failure cue | The primary reason is that high noise level causes the model to generate more hallucinated pixels that contradict the ground truth, resulting in poorer ... | p. 8 (5.3. Diagnostics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We also compare to Nerfbusters [70], which uses a 3D diffusion model to remove artifacts from NeRF1, GANeRF [46], which train per-scene GAN that ... | p. 7 (5.1. In-the-Wild Artifact Removal) |
| We use the gsplat library2 for 3DGS-based experiments and the official implementation for all other methods and baselines. | p. 7 (5.1. In-the-Wild Artifact Removal) |
| Since DIFIX is a single-step model, the additional rendering time is only 76 ms on a NVIDIA A100 GPU, over 10× faster than standard ... | p. 6 (4. Boosting 3D Reconstruction with DM priors) |
| We fine-tune SD-Turbo [49] in a similar manner to Pix2pix-Turbo [40], using a frozen VAE encoder and a LoRA fine-tuned decoder. | p. 4 (4. Boosting 3D Reconstruction with DM priors) |
| We start from concatenating novel view ˜I and reference views Iref on an additional view dimension and frame-wise encoded into latent space E((˜I, Iref)) ... | p. 4 (4. Boosting 3D Reconstruction with DM priors) |
| To generate more salient artifacts than those obtained by merely holding out views, we underfit our reconstruction by training it with a reduced number ... | p. 5 (4. Boosting 3D Reconstruction with DM priors) |
| DIFIX is fine-tuned from SD-Turbo, using a frozen VAE encoder and a LoRA fine-tuned decoder. = 200 Input = 600 = 400 = 10 ... | p. 5 (4. Boosting 3D Reconstruction with DM priors) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.1. In-the-Wild Artifact Removal - extractive PDF cue:** Our method outperforms all comparison methods by a signifi1Nerfbusters [70] uses a visibility map extracted from a NeRF model trained on a combination of training ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Noise level. To validate our hypothesis that the distribution of images with NeRF/3DGS artifacts is similar to the distribution of noisy images used ...
- **p. 8 / 5.3. Diagnostics - extractive PDF cue:** We note that simply decreasing the noise level from 1000 to 200 noticeably improves LPIPS and FID significantly, validating our findings in Fig.
- **p. 8 / 5.3. Diagnostics - extractive PDF cue:** The primary reason is that high noise level causes the model to generate more hallucinated pixels that contradict the ground truth, resulting in poorer generalization ...

- **PDF anchors reviewed:** datasets p. 7 (5.1. In-the-Wild Artifact Removal), p. 7 (5.1. In-the-Wild Artifact Removal), p. 6 (5. Experiments), p. 6 (5. Experiments), p. 8 (5.3. Diagnostics), p. 8 (5.2. Automotive Scene Enhancement), metrics p. 7 (5.1. In-the-Wild Artifact Removal), p. 8 (5.2. Automotive Scene Enhancement), p. 8 (5.3. Diagnostics), p. 7 (5.1. In-the-Wild Artifact Removal), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 8 (5.2. Automotive Scene Enhancement), p. 7 (5.1. In-the-Wild Artifact Removal), p. 8 (5.2. Automotive Scene Enhancement), p. 6 (5. Experiments), p. 7 (5.1. In-the-Wild Artifact Removal), p. 6 (Figure/Table caption), results p. 8 (5.3. Diagnostics), p. 8 (5.3. Diagnostics), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (5.1. In-the-Wild Artifact Removal), p. 7 (5.1. In-the-Wild Artifact Removal).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
