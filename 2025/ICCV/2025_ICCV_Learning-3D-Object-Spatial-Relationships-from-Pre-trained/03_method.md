# Method - Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion), p. 4 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion), p. 2 (3. Method)): We use an offthe-shelf text-to-image model [2] to generate images that are aligned to the OOR context in text prompt c.

## Method Body Digest

- **p. 3 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** We use an offthe-shelf text-to-image model [2] to generate images that are aligned to the OOR context in text prompt c.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** To account for the shape deviations, we use several template meshes as candidates and select the best via DINO features [7, 41].
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** The model architecture and training process of our OOR diffusion are shown in Fig.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** Then, we lift pixel features to obtain 3D point features.
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** To address these issues, we present an approach to infer all multi-object OORs Φ = {ϕpi t }n i=1 simultaneously, by including our novel inference-loss ...
- **p. 2 / 3. Method - extractive PDF cue:** We model OOR based on relative poses and scales of a pair of objects in canonical space.
- **p. 2 / 3. Method - extractive PDF cue:** 3.3, we present our OOR diffusion model trained on the generated 3D OOR dataset to learn the distribution of object-object relationships.
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** The inconsistency loss minimizes the variance among OOR cues for the same object from different base object paths.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our main contributions are as follows: (1) We formulate a novel representation for object-object spatial relationships (OOR); (2) We introduce an effective pipeline ...
- **p. 3 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** We present a novel pipeline that synthesizes diverse 3D samples by leveraging pre-trained 2D diffusion models and an advanced 3D uplifting process.
- **p. 2 / 1. Introduction - extractive PDF cue:** Through extensive experiments, we demonstrate the robustness of our method across various object-object spatial relationships.

## Source Evidence Cues

- **p. 3 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** We use an offthe-shelf text-to-image model [2] to generate images that are aligned to the OOR context in text prompt c.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** To account for the shape deviations, we use several template meshes as candidates and select the best via DINO features [7, 41].
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** The model architecture and training process of our OOR diffusion are shown in Fig.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** Then, we lift pixel features to obtain 3D point features.
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** To address these issues, we present an approach to infer all multi-object OORs Φ = {ϕpi t }n i=1 simultaneously, by including our novel inference-loss ...
- **p. 2 / 3. Method - extractive PDF cue:** We model OOR based on relative poses and scales of a pair of objects in canonical space.
- **p. 2 / 3. Method - extractive PDF cue:** 3.3, we present our OOR diffusion model trained on the generated 3D OOR dataset to learn the distribution of object-object relationships.
- **Detected method headings:** 3. Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data / condition representation | data와 condition을 generation state로 바꾼다 | data, text/image/task condition | encoder, noise/path parameterization 또는 latent representation을 구성 | conditioned generation state | We use an offthe-shelf text-to-image model [2] to generate images that are aligned to the OOR context in text prompt c. | p. 3 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation) |
| Denoiser / vector field | data distribution을 복원하는 방향을 학습한다 | noisy/interpolated state와 time | score, noise, velocity, flow 또는 autoregressive objective를 optimize | denoising/velocity prediction | To account for the shape deviations, we use several template meshes as candidates and select the best via DINO features [7, 41]. | p. 4 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion) |
| Sampling / downstream interface | learned field를 sample·action으로 변환한다 | base noise와 condition | iterative denoising, ODE integration, decoding 또는 filtering을 수행 | sample/action/trajectory | The model architecture and training process of our OOR diffusion are shown in Fig. | p. 5 (3.3. OOR Diffusion), p. 4 (3.2. 3D OOR Samples Generation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** The inconsistency loss minimizes the variance among OOR cues for the same object from different base object paths.
- **p. 3 / 3.1. Formulating Object-Object Relationship - extractive PDF cue:** Note that we can consider either object as the base object without loss of generality.
- **p. 3 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** We design the prompt with specific strategies to facilitate the later 3D lifting process, including: (1) appending "white background" to the end of the prompt ...
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** Mat. for details of inconsistency loss.
- **p. 4 / 3.3. OOR Diffusion - extractive PDF cue:** According to Denoising Score Matching(DSM) [60], by optimizing the following 8421
- **Formal bridge:** data x₀, noisy state x_t, condition c -> sample/action x̂ or trajectory -> distribution/denoising/flow objective -> sample quality, diversity and latency.
- **Equation/algorithm anchors:** p. 3 (3.1. Formulating Object-Object Relationship), p. 3 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion), p. 5 (3.3. OOR Diffusion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | output, SfM, obtain, point, cloud, corresponding, keypoints, where, denotes, number, points, j-th, Given, image | conditioning observation와 noisy/intermediate sample | body cue; exact tensor/frame verify |
| State/latent | output, SfM, obtain, point, cloud, corresponding, keypoints, where, denotes, number | latent/noise variable와 conditional distribution | body cue; notation verify |
| Action/output | summary, main, contributions, follows, formulate, novel, representation, object-object, spatial, relationships | generated sample, action chunk 또는 trajectory | body cue; unit/decoder verify |
| Objective/constraint | inconsistency, loss, minimizes, variance, among, OOR, cues, same, object, different | distribution/denoising/flow objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** As the output of SfM, we obtain the 3D point cloud P = {Pj}N j=1, Pj ∈R3, and their corresponding 2D keypoints, {pk j }mj ...
- **p. 3 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** Given an image containing the OOR cues for the object pair, we produce pseudo-multi-view images using an off-the-shelf novel view synthesis method, SV3D [61], which ...
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** Pose and Scale Extraction through Mesh Registration.
- **p. 4 / 3.2. 3D OOR Samples Generation - extractive PDF cue:** "A pizza cutter cuts a pizza" Find Relative Pose and Scale Pseudo Multi-view Generation & SfM Feature Extraction Figure 3.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our method is inspired by recent approaches that pursue humanobject interaction and affordances through synthetic images generated by pre-trained image diffusion models [17, 25], where ...
- **p. 2 / 3. Method - extractive PDF cue:** We model OOR based on relative poses and scales of a pair of objects in canonical space.
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** Pose and Scale T5 Encoder Text Prompt Base Category Target Category MLP MLP MLP MLP MLP MLP Figure 4.
- **Normalized interface:** observation=conditioning observation와 noisy/intermediate sample; state=latent/noise variable와 conditional distribution; output/action=generated sample, action chunk 또는 trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | noise/time schedule 또는 action sample horizon; exact denoising steps 확인 필요. | Then Ψθ models the noised score function at time step t of the pT →B c : Ψθ(ϕt, t/c, B, T ) ... | episode/sequence/action-chunk boundary |
| Rate / latency | training update와 iterative sampling/inference rate가 분리된다. | (c) adding a pan and a salt shaker to the original scene and applying "A salt shaker sprinkles salt into a pan." ... | Hz/fps, inference time and control rate |
| Memory | current noisy sample, condition과 time/noise embedding. | not recovered | window and reset |
| Compute | number of denoising/ODE steps와 network evaluation이 latency를 결정한다. | In practice, optimization is completed within 50 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** The model architecture and training process of our OOR diffusion are shown in Fig.
- **p. 5 / 3.3. OOR Diffusion - extractive PDF cue:** To address these issues, we present an approach to infer all multi-object OORs Φ = {ϕpi t }n i=1 simultaneously, by including our novel inference-loss ...
- **p. 2 / 3. Method - extractive PDF cue:** 3.3, we present our OOR diffusion model trained on the generated 3D OOR dataset to learn the distribution of object-object relationships.
- **p. 4 / 3.3. OOR Diffusion - extractive PDF cue:** Specifically, we take c, B, and T as text input and encode them with the pre-trained T5 text encoder [46].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** offthe-shelf, text-to-image, model, generate, images, aligned, OOR, context, text, prompt, account, shape, deviations, several, template, meshes, candidates, select, best, DINO.
- **Relevant PDF headings:** 3. Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data / condition representation | We evaluate 20 scenes where 3 to 5 objects have spatial relations with each other. | p. 7 (4.2. Multi-object OOR Generation), p. 7 (4.3. Applications of OOR) |
| Denoiser / vector field | In contrast, our OOR diffusion demonstrates superior sampling capabilities compared to the baselines, leveraging its effective learning of 8423 | p. 6 (4.1. Pairwise OOR Generation), p. 7 (4.1. Pairwise OOR Generation) |
| Sampling / downstream interface | 4.2 demonstrates our advanced sampling approach produces significantly better results compared to text-to-3D models. | p. 6 (4. Experiments), p. 7 (4.1. Pairwise OOR Generation) |

## Failure and Ablation Link

- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** However, due to the inherent limitation of estimating 3D information without direct 3D data, it lacks fine-grained control.
- **p. 6 / 4.1. Pairwise OOR Generation - extractive PDF cue:** However, due to the inherent limitation of estimating 3D information without direct 3D data, it lacks fine-grained control.
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** 7, GraphDreamer often fails to capture OOR (e.g., "A knife cuts an apple.").
- **p. 7 / 4.2. Multi-object OOR Generation - extractive PDF cue:** Since SMC and SceneTeller cannot be directly extended to multi-object OOR using only pairwise OOR data, we compare our model to another baseline GraphDreamer [13], ...
- **p. 8 / 4.3. Applications of OOR - extractive PDF cue:** (a) adding random noise to the original scene and then rearranging it.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.2. 3D OOR Samples Generation), p. 4 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion), p. 4 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion), p. 2 (3. Method), objective p. 5 (3.3. OOR Diffusion), p. 3 (3.1. Formulating Object-Object Relationship), p. 3 (3.2. 3D OOR Samples Generation), p. 5 (3.3. OOR Diffusion), p. 4 (3.3. OOR Diffusion), temporal p. 4 (3.3. OOR Diffusion), p. 8 (4.3. Applications of OOR), p. 3 (3.2. 3D OOR Samples Generation), p. 3 (3.2. 3D OOR Samples Generation), p. 7 (4.3. Applications of OOR), p. 8 (4.3. Applications of OOR).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
