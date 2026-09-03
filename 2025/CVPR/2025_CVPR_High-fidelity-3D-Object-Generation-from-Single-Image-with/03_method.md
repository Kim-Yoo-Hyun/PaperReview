# Method - High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Hybrid Voxel-Gaussian), p. 5 (3.4. Training Objective), p. 5 (3.4. Training Objective)): Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained RGBN volume, aligning both crucial semantic (RGB) and ...

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained RGBN volume, aligning ...
- **p. 3 / 3. Method - extractive body cue:** 2, GS-RGBN takes as input a single image of a 3D object into the MVD model Wonder3D [31] to obtain two sets of multi-view RGB ...
- **p. 4 / 3.1. Hybrid Voxel-Gaussian - extractive body cue:** RGB Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓 Normal Volume 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Voxel Residual Blockṡ 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓̇ 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Group RGBN Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓 Cross Attention Cross Attention Self Attention Q Q K V ...
- **p. 5 / 3.4. Training Objective - extractive body cue:** We train the full paradigm via color Lc and depth Ld loss supervision, optimizing reconstruction objectives between rendered and ground-truth RGB/depth images.
- **p. 5 / 3.4. Training Objective - extractive body cue:** L1 and Llp denote the L1 loss and VGG-based LPIPS loss [66].
- **p. 3 / 3. Method - extractive body cue:** Lastly, we will present the training objective, which includes the supervision of color, depth and regularization loss functions (Sec.
- **p. 5 / 3.4. Training Objective - extractive body cue:** Additionally, a regularization loss LReg, consisting of a selfsupervised distortion loss and a normal consistency loss [19], is used to improve the geometry reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** However, the direct learning of 3D Gaussians from 2D images for high-fidelity 3D object generation remains a challenge due to the spatially unstructured nature of ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a novel RGBN-volume Gaussian reconstruction model, called GS-RGBN, to generate high-quality 3D assets from single-view ...
- **p. 2 / 1. Introduction - extractive body cue:** GS-RGBN implements two key insights: first, unlike traditional methods that employ 2D convolutions to encode image features and decode corresponding per-pixel 3D Gaussian attributes in ...
- **p. 3 / 3. Method - extractive body cue:** Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained RGBN volume, aligning ...

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained RGBN volume, aligning ...
- **p. 3 / 3. Method - extractive body cue:** 2, GS-RGBN takes as input a single image of a 3D object into the MVD model Wonder3D [31] to obtain two sets of multi-view RGB ...
- **p. 4 / 3.1. Hybrid Voxel-Gaussian - extractive body cue:** RGB Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓 Normal Volume 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Voxel Residual Blockṡ 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓̇ 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Group RGBN Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓 Cross Attention Cross Attention Self Attention Q Q K V ...
- **p. 5 / 3.4. Training Objective - extractive body cue:** We train the full paradigm via color Lc and depth Ld loss supervision, optimizing reconstruction objectives between rendered and ground-truth RGB/depth images.
- **p. 5 / 3.4. Training Objective - extractive body cue:** L1 and Llp denote the L1 loss and VGG-based LPIPS loss [66].
- **Detected method headings:** 3. Method (p. 3); 3. The model performance demonstrates a significant im (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Then, we propose a simple but effective feature-level crossvolume fusion module that fuses the RGB and normal volumes to reproduce a fine-grained ... | p. 3 (3. Method), p. 3 (3. Method) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | 2, GS-RGBN takes as input a single image of a 3D object into the MVD model Wonder3D [31] to obtain two sets ... | p. 3 (3. Method), p. 4 (3.1. Hybrid Voxel-Gaussian) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | RGB Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓 Normal Volume 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Voxel Residual Blockṡ 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓̇ 𝑽𝑽𝒏𝒏𝒏𝒏𝒏𝒏 Group RGBN Volume 𝑽𝑽𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓 Cross Attention Cross Attention Self Attention Q ... | p. 4 (3.1. Hybrid Voxel-Gaussian), p. 5 (3.4. Training Objective) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. Method - extractive body cue:** Lastly, we will present the training objective, which includes the supervision of color, depth and regularization loss functions (Sec.
- **p. 5 / 3.4. Training Objective - extractive body cue:** We train the full paradigm via color Lc and depth Ld loss supervision, optimizing reconstruction objectives between rendered and ground-truth RGB/depth images.
- **p. 5 / 3.4. Training Objective - extractive body cue:** Additionally, a regularization loss LReg, consisting of a selfsupervised distortion loss and a normal consistency loss [19], is used to improve the geometry reconstruction.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3. Method), p. 5 (3.4. Training Objective), p. 5 (3.4. Training Objective).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | GS-RGBN, takes, input, single, image, object, MVD, model, Wonder3D, obtain, sets, multi-view, RGB, normal | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | GS-RGBN, takes, input, single, image, object, MVD, model, Wonder3D, obtain | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, contributions, follows, novel, RGBN-volume, Gaussian, reconstruction, model, called, GS-RGBN | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | Lastly, will, present, training, objective, includes, supervision, color, depth, regularization | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive body cue:** 2, GS-RGBN takes as input a single image of a 3D object into the MVD model Wonder3D [31] to obtain two sets of multi-view RGB ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the direct learning of 3D Gaussians from 2D images for high-fidelity 3D object generation remains a challenge due to the spatially unstructured nature of ...
- **p. 2 / 1. Introduction - extractive body cue:** The pioneering work (Dreamfusion) [43] and following works [6, 12, 35, 41, 44, 52, 53] propose score distillation sampling (SDS) and some variants, which directly ...
- **p. 3 / 3.1. Hybrid Voxel-Gaussian - extractive body cue:** 3D Gaussian splatting [22] offers good rendering speed and quality compared with previous 3D representations (e.g., mesh [56], point clouds [14], and NeRF [39]).
- **p. 5 / 3.4. Training Objective - extractive body cue:** We train the full paradigm via color Lc and depth Ld loss supervision, optimizing reconstruction objectives between rendered and ground-truth RGB/depth images.
- **p. 5 / 3.4. Training Objective - extractive body cue:** It can be formulated as: Ltotal = Lc + λdLd + λregLreg (7) Lc = λ1L1(Irgb, ˆIrgb) + λ2L1(Iα, ˆIα) + λ3Llp(Irgb, ˆIrgb) (8) Ld ...
- **p. 1 / 1. Introduction - extractive body cue:** However, the persisting challenge arises due to the inherent geometric ambiguity and limited information provided in single-view images.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | The optimization is performed using AdamW [33], with an initial learning rate of 1 × 10-5 and subsequently following a cosine annealing ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | We first use four voxel residual blocks (VRBs) with feature channels [512, 256, 128, 32], extended from the 2D residual blocks [16], ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | We first use four voxel residual blocks (VRBs) with feature channels [512, 256, 128, 32], extended from the 2D residual blocks [16], ... | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | The optimization is performed using AdamW [33], with an initial learning rate of 1 × 10-5 and subsequently following a cosine annealing ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Training Objective - extractive body cue:** We train the full paradigm via color Lc and depth Ld loss supervision, optimizing reconstruction objectives between rendered and ground-truth RGB/depth images.
- **p. 5 / 4.1. Experimental Settings - extractive body cue:** Our model is trained on four A100 (40G) GPUs for approximately 6.5 days, employing a batch size of four per GPU with bfloat16 precision, resulting ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, simple, effective, feature-level, crossvolume, fusion, module, fuses, RGB, normal, volumes, reproduce, fine-grained, RGBN, volume, aligning, crucial, semantic, geometric, cues.
- **Relevant PDF headings:** 3. Method (p. 3); 3. The model performance demonstrates a significant im (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | For evaluation, We adopt the most widely used Google Scanned Objects (GSO) dataset [13]. | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Denoiser / vector field | Our method significantly outperforms all recent methods by a large margin 21562 | p. 5 (4.2. Novel View Synthesis), p. 5 (4.2. Novel View Synthesis) |
| Sampling / downstream interface | Our method significantly outperforms all recent methods by a large margin 21562 | p. 5 (4.2. Novel View Synthesis), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Ablation study of different training models. Our full model achieves the best 3D object reconstruction with consistent details. Gaussian-based methods due to varying ...
- **p. 7 / 4.5. Ablation study - extractive body cue:** The whole paradigm can be supervised by employing only the L1 loss between RGB and alpha images to ensure a fundamental training process, while we ...
- **p. 7 / 4.5. Ablation study - extractive body cue:** The model performance decreases when the LPIPS, depth, and regularization loss terms are successively removed, as demonstrated in Table 2.
- **p. 8 / 4.5. Ablation study - extractive body cue:** As shown in Table 2, we first remove the whole CVF module and directly concatenate RGB and normal volumetric features into MLPs.
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** Besides, voxels cannot be directly used for representing large-scale scenes.
- **p. 7 / 4.5. Ablation study - extractive body cue:** Especially, the depth and regularization loss functions, which cannot be achieved by 3D 21564
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** The performance degradation occurs when the MVD models generate images with a higher level of view inconsistency.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.1. Hybrid Voxel-Gaussian), p. 5 (3.4. Training Objective), p. 5 (3.4. Training Objective), objective p. 3 (3. Method), p. 5 (3.4. Training Objective), p. 5 (3.4. Training Objective), temporal p. 5 (4.1. Experimental Settings), p. 4 (3.2. Cross-volume Fusion), p. 4 (3.2. Cross-volume Fusion), p. 8 (5. Conclusion and Limitations).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
