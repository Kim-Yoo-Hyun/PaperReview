# Method - VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 8 (Method), p. 8 (Method)): To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.

## Method Body Digest

- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** The pose generation model adopts a transformer-based architecture [69, 71], explicitly conditioned on textual prompts and pose-specific timestep to generate camera rays [87], forming a ...
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To address this, we propose an asynchronous timestep strategy, decoupling the timesteps of pose and multi-view generation modules and enabling one modality to denoise faster, ...
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To enable this, we use the following loss: ~\l ab el {eq : time ste p_ los s } \math cal {L }_{ ours} := ...
- **p. 8 / Method - extractive body cue:** For evaluation, we use 1000 sequences from RealEstate10K [93] with extracted camera trajectories and captions to generate images.
- **p. 8 / Method - extractive body cue:** VideoRFSplat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and then compared their multi-view results.
- **p. 7 / Method - extractive body cue:** We attribute these strong results, achieved without SDS-based refinement, to three key factors: (1) leveraging a powerful pre-trained video generation model, (2) adopting a more ...
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** This loss enables vector field prediction even with different timesteps for pose and image modalities.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose an asynchronous adaptation of Classifier-Free Guidance (CFG) that enables the clearer pose to better guide multi-view image generation.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, to eliminate external dependency, we present VideoRFSplat, a direct 3DGS generation model that introduces an architecture and sampling strategy for jointly generating ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.

## Source Evidence Cues

- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers (see Fig.
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** The pose generation model adopts a transformer-based architecture [69, 71], explicitly conditioned on textual prompts and pose-specific timestep to generate camera rays [87], forming a ...
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To address this, we propose an asynchronous timestep strategy, decoupling the timesteps of pose and multi-view generation modules and enabling one modality to denoise faster, ...
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To enable this, we use the following loss: ~\l ab el {eq : time ste p_ los s } \math cal {L }_{ ours} := ...
- **p. 8 / Method - extractive body cue:** For evaluation, we use 1000 sequences from RealEstate10K [93] with extracted camera trajectories and captions to generate images.
- **p. 8 / Method - extractive body cue:** VideoRFSplat can perform camera-conditioned generation. models under identical conditions for 60K iterations with Mochi [69] and then compared their multi-view results.
- **p. 7 / Method - extractive body cue:** We attribute these strong results, achieved without SDS-based refinement, to three key factors: (1) leveraging a powerful pre-trained video generation model, (2) adopting a more ...
- **Detected method headings:** 2.1. Diffusion Models and Rectified Flow (p. 3); 2.2. 3D Generative Models (p. 3); 4.1. Dual-Stream Pose-Video Joint Model (p. 4); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | To reduce interference, we propose a dual-stream architecture with dedicated submodules for pose and image generation, communicating via cross-attention at intermediate layers ... | p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | The pose generation model adopts a transformer-based architecture [69, 71], explicitly conditioned on textual prompts and pose-specific timestep to generate camera rays ... | p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | To address this, we propose an asynchronous timestep strategy, decoupling the timesteps of pose and multi-view generation modules and enabling one modality ... | p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** This loss enables vector field prediction even with different timesteps for pose and image modalities.
- **p. 5 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** To enable this, we use the following loss: ~\l ab el {eq : time ste p_ los s } \math cal {L }_{ ours} := ...
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** We concatenate the pose timestep embedding and hR, as well as the video timestep embedding and hI, then update them bidirectionally via cross-attention: hR ←CrossAttention(hI, ...
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | hypothesize, uncertainty, early, sampling, leads, unstable, pose-image, interactions, destabilizing, camera, pose, generation, ultimately, degrading | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | hypothesize, uncertainty, early, sampling, leads, unstable, pose-image, interactions, destabilizing, camera | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | Furthermore, asynchronous, adaptation, Classifier-Free, Guidance, CFG, enables, clearer, pose, better | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | loss, enables, vector, field, prediction, even, different, timesteps, pose, image | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / Method - extractive body cue:** We hypothesize that uncertainty in early sampling leads to unstable pose-image interactions, destabilizing camera pose generation and ultimately degrading multi-view image quality.
- **p. 2 / 1. Introduction - extractive body cue:** This approach is motivated by our observation that synchronized denoising of multi-view images and camera poses, particularly at early timesteps, leads to mutual ambiguity, increasing ...
- **p. 8 / Method - extractive body cue:** For evaluation, we use 1000 sequences from RealEstate10K [93] with extracted camera trajectories and captions to generate images.
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** Specifically, let hR and hI be the intermediate outputs of the pose and video models, respectively.
- **p. 2 / 1. Introduction - extractive body cue:** We train VideoRFSplat on RealEstate10K [93], MVImgNet [84], DL3DV-10K [41], and ACID [43] datasets.
- **p. 7 / Method - extractive body cue:** Specifically, Director3D often produces blurry outputs, lacking sharpness and detail for realism.
- **p. 4 / 4.1. Dual-Stream Pose-Video Joint Model - extractive body cue:** This exchange enables controlled interaction between the two models while preserving their specialized forward paths and reducing interference between pose and multi-view modalities.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Our proposed training scheme, which divides timesteps, demonstrates slightly better results. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | 4 Additionally, we evaluate performance when the training scheme does not employ timestep division as outlined in Eq. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | We resize all frames to 320×512 during training, setting K = 8, as in SplatFlow [20] and Director3D [35]. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / Method - extractive body cue:** We attribute these strong results, achieved without SDS-based refinement, to three key factors: (1) leveraging a powerful pre-trained video generation model, (2) adopting a more ...
- **p. 8 / Method - extractive body cue:** Our proposed training scheme, which divides timesteps, demonstrates slightly better results.
- **p. 8 / Method - extractive body cue:** This suggests that our approach of dividing timesteps during training is not detrimental and achieves comparable or marginally improved performance.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** reduce, interference, dual-stream, architecture, dedicated, submodules, pose, image, generation, communicating, cross-attention, intermediate, layers, Fig, model, adopts, transformer-based, explicitly, conditioned, textual.
- **Relevant PDF headings:** 2.1. Diffusion Models and Rectified Flow (p. 3); 2.2. 3D Generative Models (p. 3); 4.1. Dual-Stream Pose-Video Joint Model (p. 4); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | Following previous works [20, 35], we evaluate our model on the MVImgNet and DL3DV validation datasets, as well as the T3Bench benchmark ... | p. 6 (5.1. Experimental Setups), p. 6 (5.1. Experimental Setups) |
| Denoiser / vector field | Table 1. Quantitative results on T3Bench [23]. VideoRFSplat outperforms all baselines without SDS++ refinement. | p. 7 (Figure/Table caption), p. 5 (5. Experimental Results) |
| Sampling / downstream interface | Table 2. Quantitative results on MVImgNet [84] and DL3DV [41] validation sets. VideoRFSplat achieves the higher performance across all metrics without SDS++ ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5.1. Experimental Setups - extractive body cue:** As both methods use SDS++ [35] as a refinement step, we compare two variants for each method: with and without SDS++.
- **p. 5 / 5. Experimental Results - extractive body cue:** Our primary result is that VideoRFSplat, without SDS optimization, outperforms previous direct text-to-3DGS methods that employ SDS optimization.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Generated 3D Gaussian Splattings and rendered views from diverse texts by VideoRFSplat. VideoRFSplat directly generates realistic 3D scenes from text without SDS [35, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results on T3Bench [23]. VideoRFSplat outperforms all baselines without SDS++ refinement.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on asynchronous sampling. We also report CLIP scores on multi-view images to assess text alignment of not lifted images to 3DGS. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Failure analysis of synchronized sampling and the effectiveness of asynchronous sampling. (Left) Early in sampling (t > 0.85), synchronous sampling induces excessive oscillations ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Architecture Comparison. For each example, Left: chan- nel concat architecture (SplatFlow). Right: our architecture. framed key objects. We hypothesize that uncertainty in early ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 8 (Method), p. 8 (Method), objective p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 5 (4.1. Dual-Stream Pose-Video Joint Model), p. 4 (4.1. Dual-Stream Pose-Video Joint Model), temporal p. 8 (Method), p. 8 (Method), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (5.1. Experimental Setups), p. 6 (5.1. Experimental Setups).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
