# Method - LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=KhjlXNbYea&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Feature Subspace Learning), p. 5 (3.4. Feature Subspace Learning), p. 3 (3.2. Model Architecture), p. 4 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture), p. 4 (3.3. Volume Rendering Supervision)): While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like CLIP imposes a significant computational and memory over ...

## Method Body Digest

- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like CLIP imposes a ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** Prior to training of our proposed model, we train a single linear transformation U ∈RL×L′ that maps from the original feature space L to the ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture.
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** During inference, the model just takes the 2D images as input and outputs the scene geometry and 3D vision-language features.
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** The 3D features are then pooled to a common 3D voxel grid of features Vf ∈RX×Y ×Z×C, where X, Y, Z represent the resolution of ...
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** A set of images is first transformed to 3D voxel features via BEVStereo [24] and a 3D CNN decoder.
- **p. 2 / 3.1. Problem Definition - extractive PDF cue:** Given a set of RGB images I = {I1, I2, ..., IN}, the objective is to estimate the surrounding environment as a 3D 2
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** We have found that the MSE loss function has a much easier-tooptimize loss landscape, while the cosine similarity gives a better notion of how close ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations of ...
- **p. 1 / 1. Introduction - extractive PDF cue:** In summary, our contributions are: • Open vocabulary occupancy: A novel vision-only architecture to model arbitrary geometries and semantics by aligning the semantic feature space ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our model generalizes to estimate geometry and semantics in a zero-shot manner, without per-scene optimization like NeRF-approaches. • Feature subspace learning: In addition we introduce ...

## Source Evidence Cues

- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like CLIP imposes a ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** Prior to training of our proposed model, we train a single linear transformation U ∈RL×L′ that maps from the original feature space L to the ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture.
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** During inference, the model just takes the 2D images as input and outputs the scene geometry and 3D vision-language features.
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** The 3D features are then pooled to a common 3D voxel grid of features Vf ∈RX×Y ×Z×C, where X, Y, Z represent the resolution of ...
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** A set of images is first transformed to 3D voxel features via BEVStereo [24] and a 3D CNN decoder.
- **p. 2 / 3.1. Problem Definition - extractive PDF cue:** Given a set of RGB images I = {I1, I2, ..., IN}, the objective is to estimate the surrounding environment as a 3D 2
- **Detected method headings:** 3. Methodology (p. 2); 3.2. Model Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like ... | p. 5 (3.4. Feature Subspace Learning), p. 5 (3.4. Feature Subspace Learning) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Prior to training of our proposed model, we train a single linear transformation U ∈RL×L′ that maps from the original feature space ... | p. 5 (3.4. Feature Subspace Learning), p. 3 (3.2. Model Architecture) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture. | p. 3 (3.2. Model Architecture), p. 4 (3.3. Volume Rendering Supervision) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** We have found that the MSE loss function has a much easier-tooptimize loss landscape, while the cosine similarity gives a better notion of how close ...
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** Therefore, we optimize the MSE loss weighted by the cosine distance C for each ray, so that features already estimated well have less influence, while ...
- **p. 2 / 3.1. Problem Definition - extractive PDF cue:** Given a set of RGB images I = {I1, I2, ..., IN}, the objective is to estimate the surrounding environment as a 3D 2
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** 3.3, this separation is required to enable training via volume rendering, which automatically supervises geometry without any explicit loss.
- **p. 3 / 3.3. Volume Rendering Supervision - extractive PDF cue:** Given this weight, the final rendered 2D vision-language features can be computed by summing up the point features multiplied by their rendering weight. ˆΨ(r) = ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** The same loss as in [21] is used to train U. t′ i = tiU //tiU// ˆti = t′ iU T //t′ iU T // ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (3.1. Problem Definition), p. 3 (3.2. Model Architecture), p. 3 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 5 (3.4. Feature Subspace Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | During, inference, model, just, takes, images, input, outputs, scene, geometry, vision-language, features, Volume, Render | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | During, inference, model, just, takes, images, input, outputs, scene, geometry | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | novel, self-supervised, occupancy, estimation, aligns, geometric, estimations, open, vocabulary, natural | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | have, found, MSE, loss, function, much, easier-tooptimize, landscape, while, cosine | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** During inference, the model just takes the 2D images as input and outputs the scene geometry and 3D vision-language features.
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** 3.3.) ℒ𝑙𝑎𝑛𝑔 2D vision-language features Volume Render (CLIP) Image Encoder Input images Reducer Feature Subspace Learning (Sec.
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture.
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** Initially, the input images I are transformed into 3D voxel features Vf using the prominent 2D-to-3D transformation network BEVStereo [24], similar to previous works.
- **p. 5 / 3.3. Volume Rendering Supervision - extractive PDF cue:** As this affects only a fraction of voxels, we accept the false supervisory signals from temporal inconsistencies in this work and leave this problem for ...
- **p. 5 / 3.5. Inference - extractive PDF cue:** Given the outputs Vσ and Vψ of our model, we compute the similarity between each voxel feature with each query feature, and assign every voxel ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our model generalizes to estimate geometry and semantics in a zero-shot manner, without per-scene optimization like NeRF-approaches. • Feature subspace learning: In addition we introduce ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For each frame during training, we also generate rays for all temporal frames in a predefined time horizon, and compute the same ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We use a time horizon of 12 (to the future and past) for temporal rendering, and generate 32, 786 rays per sample, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train each network with a batch size of 4 for 18 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like CLIP imposes a ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive PDF cue:** Prior to training of our proposed model, we train a single linear transformation U ∈RL×L′ that maps from the original feature space L to the ...
- **p. 3 / 3.2. Model Architecture - extractive PDF cue:** 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture.
- **p. 4 / 3.3. Volume Rendering Supervision - extractive PDF cue:** During inference, the model just takes the 2D images as input and outputs the scene geometry and 3D vision-language features.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** We train each network with a batch size of 4 for 18 epochs.
- **p. 7 / 4.5. Ablations - extractive PDF cue:** 4.4 for all models to train the autoencoder, but modify the target dimension size (with 512 being the full space).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, vision-language, features, offer, strong, representational, power, scene, semantics, training, model, high-dimensional, embedding, space, encoders, like, CLIP, imposes, significant, computational.
- **Relevant PDF headings:** 3. Methodology (p. 2); 3.2. Model Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For zero-shot occupancy estimation, we evaluate on the widely known Occ3D-nuScenes benchmark [41], which provides semantic voxel labels for the nuScenes dataset. | p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description) |
| Semantic / temporal fusion | As is visible, our method outperforms both baselines, even though we use just vision-based supervision. | p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation) |
| Robot query / planning handoff | Adding 4 future and past frames during rendering supervision already improves all scores significantly, such that LangOcc achieves a better open vocabulary ... | p. 7 (4.5. Ablations), p. 6 (4.3. 3D Open Vocabulary Retrieval) |

## Failure and Ablation Link

- **p. 6 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive PDF cue:** Even though our model is trained without any explicit class definition, we outperform both competitors also in terms of semantic mIoU, highlighting the power of ...
- **p. 6 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive PDF cue:** LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any photometric ...
- **p. 7 / 4.5. Ablations - extractive PDF cue:** Ablation on the loss function used for Llang.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation on the temporal horizon. Horizon 0 4 8 12 16 20
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation on the subspace dimensionality L′. L' 16 32 64 128 256 512
- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive PDF cue:** As mentioned above, the reducer U finishes training within a second and thus does not impose any notable overhead.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Feature Subspace Learning), p. 5 (3.4. Feature Subspace Learning), p. 3 (3.2. Model Architecture), p. 4 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture), p. 4 (3.3. Volume Rendering Supervision), objective p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 2 (3.1. Problem Definition), p. 3 (3.2. Model Architecture), p. 3 (3.3. Volume Rendering Supervision), p. 5 (3.4. Feature Subspace Learning), temporal p. 4 (3.3. Volume Rendering Supervision), p. 6 (4.2. Implementation Details), p. 5 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture), p. 7 (4.5. Ablations), p. 7 (4.5. Ablations).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
