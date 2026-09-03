# Method - SeaLion: Semantic Part-Aware Latent Point Diffusion Models for 3D Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.2. Model Architecture of SeaLion), p. 5 (3.2. Model Architecture of SeaLion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 3 (3. Methodology), p. 5 (3.3. Part-aware 3D Shape Edition Tool)): Inspired by the insight that DDPMs can serve as powerful representation learners for discriminative tasks like segmentation [2], we propose semantic part-aware latent point diffusion technique for generating labeled point ...

## Method Body Digest

- **p. 3 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Inspired by the insight that DDPMs can serve as powerful representation learners for discriminative tasks like segmentation [2], we propose semantic part-aware latent point diffusion ...
- **p. 4 / 3.2. Model Architecture of SeaLion - extractive body cue:** Based on the semantic part-aware latent point diffusion technique, we introduce a novel point cloud generative model named SeaLion.
- **p. 5 / 3.2. Model Architecture of SeaLion - extractive body cue:** The global encoder ϕz consists of PVConv blocks, set abstraction layers, a max pooling layer, and a multi-layer perceptron.
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Compared to the traditional twostep method, which first generates unlabeled point clouds and then assigns pseudo segmentation labels using a pretrained segmentation model, our approach ...
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce the architecture of SeaLion, and illustrate its usage as a part-aware 3D edition tool.
- **p. 5 / 3.3. Part-aware 3D Shape Edition Tool - extractive body cue:** In this process, the unfrozen latent points are perturbed for τ steps (τ < T) and then denoised for the same number of steps.
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** In the first stage, we train the components of hierarchical VAE, including ϕz, ϕh, and ξh, to maximize a variational lower bound on the data ...
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** The training objectives for ϵz and ϵh are: \la b el {eq:latent_dd pm _ glob al} \mathcal {L}(\epsilon _z) = \mathbb {E}_{t, z_0, \epsilon } ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel evaluation metric named part-aware Chamfer distance (p-CD) to address these limitations and to quantify the pairwise distance between two segmentation-labeled point ...
- **p. 4 / 3.2. Model Architecture of SeaLion - extractive body cue:** Based on the semantic part-aware latent point diffusion technique, we introduce a novel point cloud generative model named SeaLion.

## Source Evidence Cues

- **p. 3 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Inspired by the insight that DDPMs can serve as powerful representation learners for discriminative tasks like segmentation [2], we propose semantic part-aware latent point diffusion ...
- **p. 4 / 3.2. Model Architecture of SeaLion - extractive body cue:** Based on the semantic part-aware latent point diffusion technique, we introduce a novel point cloud generative model named SeaLion.
- **p. 5 / 3.2. Model Architecture of SeaLion - extractive body cue:** The global encoder ϕz consists of PVConv blocks, set abstraction layers, a max pooling layer, and a multi-layer perceptron.
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Compared to the traditional twostep method, which first generates unlabeled point clouds and then assigns pseudo segmentation labels using a pretrained segmentation model, our approach ...
- **p. 3 / 3. Methodology - extractive body cue:** Next, we introduce the architecture of SeaLion, and illustrate its usage as a part-aware 3D edition tool.
- **p. 5 / 3.3. Part-aware 3D Shape Edition Tool - extractive body cue:** In this process, the unfrozen latent points are perturbed for τ steps (τ < T) and then denoised for the same number of steps.
- **Detected method headings:** 3. Methodology (p. 3); 3.2. Model Architecture of SeaLion (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | Inspired by the insight that DDPMs can serve as powerful representation learners for discriminative tasks like segmentation [2], we propose semantic part-aware ... | p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.2. Model Architecture of SeaLion) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | Based on the semantic part-aware latent point diffusion technique, we introduce a novel point cloud generative model named SeaLion. | p. 4 (3.2. Model Architecture of SeaLion), p. 5 (3.2. Model Architecture of SeaLion) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The global encoder ϕz consists of PVConv blocks, set abstraction layers, a max pooling layer, and a multi-layer perceptron. | p. 5 (3.2. Model Architecture of SeaLion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** In the first stage, we train the components of hierarchical VAE, including ϕz, ϕh, and ξh, to maximize a variational lower bound on the data ...
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** The training objectives for ϵz and ϵh are: \la b el {eq:latent_dd pm _ glob al} \mathcal {L}(\epsilon _z) = \mathbb {E}_{t, z_0, \epsilon } ...
- **p. 3 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** The training loss function is: \ma t hcal {L}(\epsilo n _{ \ thet a }) = \mathbb {E}_{t, x_0, \epsilon } [{// \epsilon _{\theta } ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 5 (3.2. Model Architecture of SeaLion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, contributions, novel, generative, model, named, SeaLion, capable, generating, high-quality, diverse, point, clouds, accurate | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | summary, contributions, novel, generative, model, named, SeaLion, capable, generating, high-quality | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, contributions, novel, generative, model, named, SeaLion, capable, generating, high-quality | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | first, stage, train, components, hierarchical, VAE, including, maximize, variational, lower | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the contributions of this work are: • We propose a novel generative model named SeaLion, capable of generating high-quality and diverse point clouds ...
- **p. 3 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** The generative model acquires semantic part awareness by being trained to reconstruct input point clouds guided by segmentation encodings, forming a basis for extracting segmentation ...
- **p. 4 / 3.2. Model Architecture of SeaLion - extractive body cue:** PVCNN, a U-Net style architecture for point cloud data, uses the set abstraction layer [26] and feature propagation layer [26] for downsampling and up-sampling the ...
- **p. 1 / 1. Introduction - extractive body cue:** Current state-of-the-art diffusion-based point cloud generative models [21, 37, 40] have achieved impressive performance.
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Given the input ht, the data flow in the down-sampling path is as follows:
- **p. 5 / 3.2. Model Architecture of SeaLion - extractive body cue:** The global encoder ϕz consists of PVConv blocks, set abstraction layers, a max pooling layer, and a multi-layer perceptron.
- **p. 3 / 3. Methodology - extractive body cue:** Finally, we discuss the limitation of current metrics for evaluating generated labeled point clouds and propose novel metrics based on part-aware Chamfer distance (p-CD).
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | The training loss function is: \ma t hcal {L}(\epsilo n _{ \ thet a }) = \mathbb {E}_{t, x_0, \epsilon } [{// ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | The diffusion model [13] generates data by simulating a stochastic T-step process. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | We conduct the experiments using an NVIDIA RTX 3090 GPU with 24GB of VRAM. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** Compared to the traditional twostep method, which first generates unlabeled point clouds and then assigns pseudo segmentation labels using a pretrained segmentation model, our approach ...
- **p. 4 / 3.1. Semantic Part-Aware Latent Point Diffusion - extractive body cue:** As illustrated in Figure 2 (b), the inference process consists of three steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Inspired, insight, DDPMs, serve, powerful, representation, learners, discriminative, tasks, like, segmentation, semantic, part-aware, latent, point, diffusion, technique, generating, labeled, cloud.
- **Relevant PDF headings:** 3. Methodology (p. 3); 3.2. Model Architecture of SeaLion (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | IntrA [34] is a real-world dataset containing 3D intracranial aneurysm point clouds reconstructed from MRI. | p. 6 (4.1. Experimental Setup), p. 5 (3.4. Evaluation Metrics) |
| Denoiser / vector field | The results demonstrate that SeaLion outperforms both DiffFacto and the two-step approach, which combines the state-of-the-art generative and segmentation models, Lion and ... | p. 6 (4.2. Experimental Results), p. 6 (4.2. Experimental Results) |
| Sampling / downstream interface | The results show that SeaLion outperforms DiffFacto on the primary metric 1-NNA-P and achieves competitive performance on the other metrics. | p. 7 (4.2. Experimental Results), p. 8 (4.3. Experimental Analysis) |

## Failure and Ablation Link

- **p. 8 / 4.3. Experimental Analysis - extractive body cue:** Additional ablation studies are provided in the supplementary materials.
- **p. 8 / 4.3. Experimental Analysis - extractive body cue:** L refers to the use of 10% data with segmentation labels, while U refers to the remaining data without segmentation labels.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) Training: The generative model develops semantic part awareness by being trained to reconstruct input point clouds x guided by segmentation encodings y, ...
- **p. 6 / 4.2. Experimental Results - extractive body cue:** DiffFacto [23] provides pretrained weights for four categories in ShapeNet: airplane, car, chair, and lamp.
- **p. 6 / 4.2. Experimental Results - extractive body cue:** Additionally, we use a pretrained PointNet++ [26] and SPoTr [25], an open-source and state-of-the-art model on ShapeNet part segmentation benchmark [24], to assign pseudo segmentation ...
- **p. 7 / 4.2. Experimental Results - extractive body cue:** Note that certain data is missing because DiffFacto [23] only provides pretrained models for airplane, car, chair, and lamp categories, while Lion [37] only releases ...
- **p. 5 / 3.4. Evaluation Metrics - extractive body cue:** However, both intra-part and inter-part scores have limitations in evaluating the generation of segmentation-labeled point clouds.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.2. Model Architecture of SeaLion), p. 5 (3.2. Model Architecture of SeaLion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 3 (3. Methodology), p. 5 (3.3. Part-aware 3D Shape Edition Tool), objective p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), temporal p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 3 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 4 (3.1. Semantic Part-Aware Latent Point Diffusion), p. 5 (3.3. Part-aware 3D Shape Edition Tool), p. 6 (4.2. Experimental Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
