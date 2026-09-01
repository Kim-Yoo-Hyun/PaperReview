# Evaluation - WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=KWeX6tYno6; PDF retrieval source: https://openreview.net/pdf/26fbb3a9ef84175c8a2efe7918a32cd5a0082627.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION)): Figure 4: Comparison with MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). The top row shows real frames, the second row the corresponding sketches and bounding-box controls. ...

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We conduct experiments on the nuScenes benchmark (Caesar et al., 2020), which contains 1,000 urban driving scenes annotated at 2 Hz.
- **p. 16 / A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION - extractive PDF cue:** We compare against feed-forward 3D reconstruction methods on the nuScenes validation set, measuring PSNR, SSIM, and LPIPS to assess the geometric fidelity and multi-view consistency ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 EXPERIMENTAL SETUPS Dataset and Metrics.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 2, we compare WorldSplat with six baselines on nuScenes under viewpoint shifts of ±1, ±2, and ±4 meters.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Single-frame Gaussians are often too sparse, producing holes and aliasing in novel views, while 4D aggregation enhances spatiotemporal consistency by densifying the representation across time ...
- **p. 16 / A.2 TRAINING DETAILS - extractive PDF cue:** Stage 2: We continue for 40K iterations (10K steps on 32 GPUs) using mixed resolutions (144p, 240p, 360p) and varying frame lengths, aligning the model ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We systematically validate each component's contribution: (1) 3D Gaussians Representation (Version A →B): Introducing 3D Gaussians as explicit scene representation significantly improves performance with FVD ...
- **p. 15 / A.1 ARCHITECTURES - extractive PDF cue:** We further fuse 3D bounding boxes, ego-trajectory data, and scene captions via a single cross-attention layer.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); A IMPLEMENTATION DETAILS (p. 15); A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION (p. 16); C MORE VISUALIZATION RESULTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: Comparison with MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). The top row shows real frames, the second row ... | p. 8 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We systematically validate each component's contribution: (1) 3D Gaussians Representation (Version A →B): Introducing 3D Gaussians as explicit scene representation significantly improves performance with ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Red boxes indicate where our method achieves the greatest improvements. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As the results demonstrate, our approach produces more accurate shapes and positions for dynamic objects, and achieves much better consistency across multiple views. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | (2) 4D Gaussian Aggregation (Version B →C): Aggregating single-frame 3D Gaussians into a unified 4D representation further improves performance with FVD from 75.26 to ... | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We conduct experiments on the nuScenes benchmark (Caesar et al., 2020), which contains 1,000 urban driving scenes annotated at 2 Hz.
- **p. 16 / A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION - extractive PDF cue:** We compare against feed-forward 3D reconstruction methods on the nuScenes validation set, measuring PSNR, SSIM, and LPIPS to assess the geometric fidelity and multi-view consistency ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** 4.1 EXPERIMENTAL SETUPS Dataset and Metrics.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 2, we compare WorldSplat with six baselines on nuScenes under viewpoint shifts of ±1, ±2, and ±4 meters.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Single-frame Gaussians are often too sparse, producing holes and aliasing in novel views, while 4D aggregation enhances spatiotemporal consistency by densifying the representation across time ...
- **p. 16 / A.2 TRAINING DETAILS - extractive PDF cue:** Stage 2: We continue for 40K iterations (10K steps on 32 GPUs) using mixed resolutions (144p, 240p, 360p) and varying frame lengths, aligning the model ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We systematically validate each component's contribution: (1) 3D Gaussians Representation (Version A →B): Introducing 3D Gaussians as explicit scene representation significantly improves performance with FVD ...
- **p. 15 / A.1 ARCHITECTURES - extractive PDF cue:** We further fuse 3D bounding boxes, ego-trajectory data, and scene captions via a single cross-attention layer.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison of different driving world models. Previous driving world models (Jiang et al., 2024; Gao et al., 2023) focus on video generation, while ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The overview of our framework. (1) Employing a 4D-aware diffusion model to generate a multi-modal latent containing RGB, depth, and dynamic information. (2) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Effectiveness of the enhanced diffusion model. During novel-view video synthesis, rendering quality may degrade due to unobserved regions or high ego-vehicle speed, resulting ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Video generation comparison on the nuScenes (Caesar et al., 2020) validation set, with green and blue highlighting the best and second-best values, respectively.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison with MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). The top row shows real frames, the second row the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative results of novel-view synthesis, reporting FID and FVD under viewpoint shifts of ±1, ±2, and ±4 meters. Baseline metrics are taken from ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative comparison of our novel view synthesis against the state-of-the-art urban reconstruction method (Chen et al., 2024c). We translate the ego-vehicle by ±2 ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation study of novel-view generation: "C-Reprojection" reprojects boxes and sketches; "3D Gs" uses Gaussians from single-frame reconstructions; "4D Gs" uses Gaussians from multi- ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments on the nuScenes benchmark (Caesar et al., 2020), which contains 1,000 urban driving scenes annotated at 2 Hz. | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION) |
| Task/environment | We compare against feed-forward 3D reconstruction methods on the nuScenes validation set, measuring PSNR, SSIM, and LPIPS to assess the geometric fidelity and multi-view ... | reset, timeout, object/scene variation | p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 15 (A.1 ARCHITECTURES), p. 5 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Across all scenarios, our method consistently delivers the best scores on both the FVD and FID metrics. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| These results demonstrate the robustness and fidelity of our 4D Gaussian representation for novel-view synthesis under varying viewpoint shifts. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| 4, we compare our generated videos with two leading methods: MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Our renderings are sharper and more detailed: OmniRe often loses fine elements such as lane markings and railings, whereas our approach preserves these features ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| We translate the ego-vehicle by ±2 m to generate the novel viewpoints. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| As detailed in Section 3.4 and illustrated in Figure 3, this module addresses inherent limitations of Gaussian splatting-low-quality renderings in unobserved regions 9 | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| 6, our method achieves superior performance across all metrics, demonstrating strong geometric consistency and multi-view coherence. | definition/direction/unit from same section | p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION) |
| We compare against feed-forward 3D reconstruction methods on the nuScenes validation set, measuring PSNR, SSIM, and LPIPS to assess the geometric fidelity and multi-view ... | definition/direction/unit from same section | p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| WorldSplat consistently achieves the best FID/FVD across all shifts-for example, at ±1 m it outperforms DiST-4D and OmniRe, and even at ±4 m it ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2026 Real OmniRe Ours Figure 5: Qualitative comparison of our novel view synthesis against the state-of-the-art urban ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Baseline metrics are taken from DiST-4D (Guo et al., 2025). | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 0.237) compared to OmniScene indicate that our 4D Gaussian 16 | comparison identity and matched condition | p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION) |
| Figure 5: Qualitative comparison of our novel view synthesis against the state-of-the-art urban reconstruction method (Chen et al., 2024c). We translate the ego-vehicle by ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 1: Comparison of different driving world models. Previous driving world models (Jiang et al., 2024; Gao et al., 2023) focus on video generation, ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3, we report FID and FVD for novel-view synthesis with a ±2 m ego shift across six variants to systematically validate each component's contribution. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Figure 3: Effectiveness of the enhanced diffusion model. During novel-view video synthesis, rendering quality may degrade due to unobserved regions or high ego-vehicle speed, ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 7: Visualizations of our Gaussians representation. Further, our method produces fully controllable videos without relying on any reference frames, while simultaneously supporting high-quality ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| Without first-frame guidance, our model achieves 74.13 FVDmulti and 8.78 FIDmulti, surpassing DriveDreamer-2 (Zhao et al., 2024), MagicDrive-V2 (Gao et al., 2025), and Panacea ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| To enforce coherence across views without increasing parameter count, we replace standard self-attention with a cross-view attention mechanism. | component/input/data sensitivity | p. 15 (A.1 ARCHITECTURES) |
| We adopt the pretrained OpenSora-VAE-1.2 (hpcai tech, 2024) as the backbone, fine-tuning only the cross-view attention blocks (Gao et al., 2023) in the diffusion ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our framework creates a dynamic 4D Gaussian representation and renders the novel views along any user-defined camera trajectory without per-scene optimization. | Figure 4: Comparison with MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). The top row shows real frames, the second row ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION) |
| Primary metric/result | We systematically validate each component's contribution: (1) 3D Gaussians Representation (Version A →B): Introducing 3D Gaussians as explicit scene representation significantly improves performance with ... | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We conduct experiments on the nuScenes benchmark (Caesar et al., 2020), which contains 1,000 urban driving scenes annotated at 2 Hz.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We upsample the annotations (e.g., bounding boxes and road sketches) to 12 Hz following (Wang et al., 2023).
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The model is trained on 700 scenes and validated on 150.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 2, we compare WorldSplat with six baselines on nuScenes under viewpoint shifts of ±1, ±2, and ±4 meters.
- **p. 16 / A.2 TRAINING DETAILS - extractive PDF cue:** Stage Description Steps* Resolution (6 views) Time Stage 1 Fine-tune from OpenSora v1.2 with layout/sketch control 60K 256×256 ∼32h Stage 2 Mixed-resolution training with varying ...
- **p. 16 / A.2 TRAINING DETAILS - extractive PDF cue:** Stage 2: We continue for 40K iterations (10K steps on 32 GPUs) using mixed resolutions (144p, 240p, 360p) and varying frame lengths, aligning the model ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3: Effectiveness of the enhanced diffusion model. During novel-view video synthesis, rendering quality may degrade due to unobserved regions or high ego-vehicle speed, ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | As detailed in Section 3.4 and illustrated in Figure 3, this module addresses inherent limitations of Gaussian splatting-low-quality renderings in unobserved regions 9 | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 2: The overview of our framework. (1) Employing a 4D-aware diffusion model to generate a multi-modal latent containing RGB, depth, and dynamic information. ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | These results demonstrate the robustness and fidelity of our 4D Gaussian representation for novel-view synthesis under varying viewpoint shifts. | p. 8 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 4: Comparison with MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). The top row shows real frames, the second row ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | As discussed in Line 292 of our paper, novel-view renderings at inference often appear inferior to source views; by degrading training source view quality ... | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Steps are reported for 8-GPU training. | p. 16 (A.2 TRAINING DETAILS) |
| For 32-GPU training, divide by 4 (e.g., Stage 1: 15K steps). | p. 16 (A.2 TRAINING DETAILS) |
| Specifically, we translate the camera by offsets of ±1 m, ±2 m, and ±4 m, then compute FID and FVD between the generated RGB ... | p. 7 (4 EXPERIMENTS) |
| We project the 2D image-plane embeddings of each 3D box with a 3D convolution, encode the 15 | p. 15 (A.1 ARCHITECTURES) |
| In parallel, we introduce a dedicated ControlNet (Chen, 2023) branch to inject rendering and sketch guidance: the VAE encodes both signals into latent patches, ... | p. 15 (A.1 ARCHITECTURES) |
| (5) By integrating data from multiple time steps, our decoder captures the scene's complete geometry, appearance, and motion, enabling rendering from both new spatial ... | p. 5 (3 METHOD) |
| 3.2) for multi-modal latent generation, a latent Gaussian decoder (Sec. | p. 3 (3 METHOD) |
| Finally, we concatenate the three latents channel-wise to form the decoder input L = concate{Limg, Ldepth, Lseg}. | p. 3 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Effectiveness of the enhanced diffusion model. During novel-view video synthesis, rendering quality may degrade due to unobserved regions or high ego-vehicle speed, resulting ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** As detailed in Section 3.4 and illustrated in Figure 3, this module addresses inherent limitations of Gaussian splatting-low-quality renderings in unobserved regions 9
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The overview of our framework. (1) Employing a 4D-aware diffusion model to generate a multi-modal latent containing RGB, depth, and dynamic information. (2) ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** These results demonstrate the robustness and fidelity of our 4D Gaussian representation for novel-view synthesis under varying viewpoint shifts.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison with MagicDrive (Gao et al., 2023) and Panacea (Wen et al., 2024). The top row shows real frames, the second row the ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** As discussed in Line 292 of our paper, novel-view renderings at inference often appear inferior to source views; by degrading training source view quality through ...

- **PDF anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.2 TRAINING DETAILS), metrics p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.3 GEOMETRIC CONSISTENCY AND MULTI-VIEW COHERENCE EVALUATION).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
