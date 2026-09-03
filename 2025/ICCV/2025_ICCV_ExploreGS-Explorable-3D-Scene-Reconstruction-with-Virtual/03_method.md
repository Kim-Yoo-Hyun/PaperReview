# Method - ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. Scene initialization), p. 3 (3.1. Overview), p. 4 (3.3. Virtual view sampling), p. 4 (3.3. Virtual view sampling)): To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.

## Method Body Digest

- **p. 3 / 3.2. Scene initialization - extractive body cue:** To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.
- **p. 3 / 3.1. Overview - extractive body cue:** NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: Trn = {V ...
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (b) Based on the optimized 3DGS and training viewpoints, we generate virtual camera trajectories, and enhance the rendered views using our diffusion-based enhancement model.
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (c) Finally, the scene is further optimized using both the original training viewpoints and the newly generated virtual viewpoints.  - 1 1 1 - ...
- **p. 3 / 3.2. Scene initialization - extractive body cue:** Our pipeline begins by optimizing the initial set of 3D Gaussians with the given training set within the 3DGS optimization framework [11].
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (a) The scene is initially optimized using 3DGS on the given training viewpoints.
- **p. 3 / 3.1. Overview - extractive body cue:** Then, we determine the boundary of reconstructable scene based on the input observations and identify occupied regions for virtual viewpoints samplings.
- **p. 3 / 3.2. Scene initialization - extractive body cue:** As previously discussed, reconstructing content beyond this bounding box is highly challenging, as it lacks grounding in the input observations and increasingly resembles unconstrained content ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering of ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we introduce ExploreGS, a pipeline that enables explorable scene reconstruction using diffusion priors and 3DGS.
- **p. 3 / 3.2. Scene initialization - extractive body cue:** To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.

## Source Evidence Cues

- **p. 3 / 3.2. Scene initialization - extractive body cue:** To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S.
- **p. 3 / 3.1. Overview - extractive body cue:** NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: Trn = {V ...
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (b) Based on the optimized 3DGS and training viewpoints, we generate virtual camera trajectories, and enhance the rendered views using our diffusion-based enhancement model.
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (c) Finally, the scene is further optimized using both the original training viewpoints and the newly generated virtual viewpoints.  - 1 1 1 - ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | To this end, we introduce a simple rasterization-based algorithm to construct the occupancy grid O ∈RS×S×S. | p. 3 (3.2. Scene initialization), p. 3 (3.1. Overview) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: ... | p. 3 (3.1. Overview), p. 4 (3.3. Virtual view sampling) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | (b) Based on the optimized 3DGS and training viewpoints, we generate virtual camera trajectories, and enhance the rendered views using our diffusion-based ... | p. 4 (3.3. Virtual view sampling), p. 4 (3.3. Virtual view sampling) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Overview - extractive body cue:** NT r camera trajectories that maximizes the information gain are sampled, and each trajectory Trn consists of L progressively shifting virtual viewpoints: Trn = {V ...
- **p. 3 / 3.2. Scene initialization - extractive body cue:** Our pipeline begins by optimizing the initial set of 3D Gaussians with the given training set within the 3DGS optimization framework [11].
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (a) The scene is initially optimized using 3DGS on the given training viewpoints.
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (b) Based on the optimized 3DGS and training viewpoints, we generate virtual camera trajectories, and enhance the rendered views using our diffusion-based enhancement model.
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, determine, boundary, reconstructable, scene, input, observations, identify, occupied, regions, virtual, viewpoints, samplings, previously | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | Then, determine, boundary, reconstructable, scene, input, observations, identify, occupied, regions | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, contributions, organized, follows, pipeline, explorable, scene, reconstruction, incorporates, real-time | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | camera, trajectories, maximizes, information, gain, sampled, trajectory, Trn, consists, progressively | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Overview - extractive body cue:** Then, we determine the boundary of reconstructable scene based on the input observations and identify occupied regions for virtual viewpoints samplings.
- **p. 3 / 3.2. Scene initialization - extractive body cue:** As previously discussed, reconstructing content beyond this bounding box is highly challenging, as it lacks grounding in the input observations and increasingly resembles unconstrained content ...
- **p. 2 / 1. Introduction - extractive body cue:** Unfortunately, such an experience is yet to be fully realized, as existing methods suffer from severe degradations in rendering quality when viewpoints deviate significantly from ...
- **p. 2 / 1. Introduction - extractive body cue:** To avoid generating arbitrary contents in regions far beyond the input observations-which would not reflect actual user experiences-we define the target areas as a bounding ...
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (c) Finally, the scene is further optimized using both the original training viewpoints and the newly generated virtual viewpoints.  - 1 1 1 - ...
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** Overview of the proposed framework for scene exploration.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Our pipeline begins by optimizing the initial set of 3D Gaussians with the given training set within the 3DGS optimization framework [11]. | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | Overview of the proposed framework for scene exploration. | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (b) Based on the optimized 3DGS and training viewpoints, we generate virtual camera trajectories, and enhance the rendered views using our diffusion-based enhancement model.
- **p. 4 / 3.3. Virtual view sampling - extractive body cue:** (c) Finally, the scene is further optimized using both the original training viewpoints and the newly generated virtual viewpoints.  - 1 1 1 - ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, simple, rasterization-based, algorithm, construct, occupancy, grid, camera, trajectories, maximizes, information, gain, sampled, trajectory, Trn, consists, progressively, shifting, virtual, viewpoints.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | To address the lack of an appropriate benchmark for scene exploration, we introduce WildExplore, a new dataset comprising four indoor and four ... | p. 6 (4.1. WildExplore), p. 6 (4.2. Curated Nerfbusters) |
| Denoiser / vector field | 6 show qualitative comparisons among our method and baseline methods. | p. 7 (5.2. Results), p. 6 (5.2. Results) |
| Sampling / downstream interface | Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, ... | p. 6 (5.2. Results), p. 7 (5.2. Results) |

## Failure and Ablation Link

- **p. 6 / 5.2. Results - extractive body cue:** Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in PSNR ...
- **p. 7 / 5.2. Results - extractive body cue:** In contrast, our method fills missing regions and removes artifacts more effectively, producing images that align closely with the ground truth.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. (a) Viewpoint candidates for virtual camera viewpoint generation. (b) Information gain of each viewpoint. Simplified 2D examples of both are presented for clarity. ...
- **p. 7 / 5.2. Results - extractive body cue:** 3DGS [11] suffers from artifacts, and its variants with depth regularization also meet the same problem, as they lack the capability to fill missing information.
- **p. 8 / 5.3. Ablation study - extractive body cue:** Ablation study on information gain.
- **p. 8 / 5.3. Ablation study - extractive body cue:** Ablations study on finetuning methods.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** After generating the pseudo observation set, we fine-tune 3D Gaussians for 15K iterations, applying densification until 9K, with the same scheduling as 3DGS.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.2. Scene initialization), p. 3 (3.1. Overview), p. 4 (3.3. Virtual view sampling), p. 4 (3.3. Virtual view sampling), objective p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization), p. 4 (3.3. Virtual view sampling), p. 4 (3.3. Virtual view sampling), temporal p. 3 (3.2. Scene initialization), p. 4 (3.3. Virtual view sampling), p. 6 (5.1. Experimental Setup), p. 1 (Body text (section not recovered)), p. 1 (Abstract), p. 2 (2.1. Novel view synthesis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
