# Method - Fully Convolutional Geometric Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_ICCV_2019/papers/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (5. Implementation), p. 8 (6.7. Runtime)): We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to train the network with normalization.

## Method Body Digest

- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to ...
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** For the contrastive loss, we use both normalized (denoted norm.) and unnormalized features.
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Then, we use the pairwise loss for the mined quadruplet (fi, fj, f - i , f - j ) and form the fully8960
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 4 / 5. Implementation - extractive PDF cue:** As the input to the network requires unique coordinates C and corresponding features F, we first downsample the input point cloud using a fast GPU-based ...
- **p. 8 / 6.7. Runtime - extractive PDF cue:** The reported times include data preprocessing and feature extraction.
- **p. 4 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Ii is short for I(i, ki, dt), which is an indicator function that returns 1 if the feature ki is located outside a sphere with ...
- **p. 4 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Traditional contrastive and triplet losses use random sampling.

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** If we use a 2D analogy, extracting 3D ∗Equal contribution.
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our approach is the most accurate and the fastest.

## Source Evidence Cues

- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to ...
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** For the contrastive loss, we use both normalized (denoted norm.) and unnormalized features.
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Then, we use the pairwise loss for the mined quadruplet (fi, fj, f - i , f - j ) and form the fully8960
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 4 / 5. Implementation - extractive PDF cue:** As the input to the network requires unique coordinates C and corresponding features F, we first downsample the input point cloud using a fast GPU-based ...
- **p. 8 / 6.7. Runtime - extractive PDF cue:** The reported times include data preprocessing and feature extraction.
- **p. 4 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Ii is short for I(i, ki, dt), which is an indicator function that returns 1 if the feature ki is located outside a sphere with ...
- **Detected method headings:** Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the ... | p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For the contrastive loss, we use both normalized (denoted norm.) and unnormalized features. | p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Then, we use the pairwise loss for the mined quadruplet (fi, fj, f - i , f - j ) and form ... | p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to ...
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** In this section, we propose metric learning losses for fully-convolutional feature learning.
- **p. 3 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Then, we use the pairwise loss for the mined quadruplet (fi, fj, f - i , f - j ) and form the fully8960
- **p. 4 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** Traditional contrastive and triplet losses use random sampling.
- **p. 4 / 4.2. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** The above equation finds the hardest negatives for both (i, j) ∈P (Fig.
- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** As the hardest-triplet loss tends to collapse Hardest-Triple Feature Match Recall STD Num.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | does, require, low-level, preprocessing, patches, input, rapidly, generate, high-resolution, features, state-ofthe-art, discriminative, power, network | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | does, require, low-level, preprocessing, patches, input, rapidly, generate, high-resolution, features | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | analogy, extracting, Equal, contribution, section, metric, learning, losses, fully-convolutional, feature | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | normalization, project, features, surface, hypersphere, pass, gradient, loss, through, layer | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** Our approach does not require low-level preprocessing or 3D patches as input, and can rapidly generate high-resolution features with state-ofthe-art discriminative power.
- **p. 4 / 5. Implementation - extractive PDF cue:** As the input to the network requires unique coordinates C and corresponding features F, we first downsample the input point cloud using a fast GPU-based ...
- **p. 8 / 6.7. Runtime - extractive PDF cue:** The reported times include data preprocessing and feature extraction.
- **p. 1 / 1. Introduction - extractive PDF cue:** A standard input representation for convolutional networks on 3D data is a dense 4D tensor: three spatial dimensions and one feature dimension.
- **p. 1 / 1. Introduction - extractive PDF cue:** Despite these advantages, fully-convolutional networks have not been widely used for 3D geometric feature extraction due to the characteristics of 3D data.
- **p. 2 / 1. Introduction - extractive PDF cue:** Our approach achieves state-of-the-art performance on the 3DMatch benchmark [36], while being nine times faster than the fastest learning-based method and 290 times faster than ...
- **p. 8 / 6.5. Effect of Margins for Hardest-contrastive - extractive PDF cue:** This is because a high-resolution point cloud increases the specificity of the registration, which leads to lower translation error.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We use hash-based filtering to efficiently remove false negatives from the hard negative mining step to implement I(i, ji). | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | All these preprocessing steps can be parallelized in data-loading parallel processes and consume a fraction of the training time. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | OOM denotes Out Of Memory under the same hyperparameters. tance thresholds, and inlier recall thresholds. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We train the networks for 100 epochs using Stochastic Gradient Descent starting with learning rate 0.1 with a Exponential learning rate schedule ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 6.4. Hardest-contrastive and Hardest-triplet Losses - extractive PDF cue:** We used L2 normalization to project features to the surface of a hypersphere and pass the gradient from the loss through the normalization layer to ...
- **p. 4 / 5. Implementation - extractive PDF cue:** All these preprocessing steps can be parallelized in data-loading parallel processes and consume a fraction of the training time.
- **p. 5 / 6.1. Datasets and Training - extractive PDF cue:** We train the networks for 100 epochs using Stochastic Gradient Descent starting with learning rate 0.1 with a Exponential learning rate schedule with γ = ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** normalization, project, features, surface, hypersphere, pass, gradient, loss, through, layer, train, network, contrastive, normalized, denoted, norm, unnormalized, Then, pairwise, mined.
- **Relevant PDF headings:** Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This training set contains 11 sequences, which we split into train/val/test sets as follows: sequence 0 to 5 for training, sequence 7 ... | p. 4 (6.1. Datasets and Training), p. 4 (6.1. Datasets and Training) |
| Semantic / temporal fusion | We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | p. 4 (6. Experiments), p. 5 (6.3. 3D Match Benchmark) |
| Robot query / planning handoff | We show that FCGF outperform all state-of-the-art methods in both accuracy and speed, and analyze the proposed hardestcontrastive and hardest-triplet losses. | p. 4 (6. Experiments), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 6.1. Datasets and Training - extractive PDF cue:** We found rotation augmentation to be a simple (SO(3) multiplication) and effective way to make FCGF invariant to relative camera pose change.
- **p. 5 / 6.1. Datasets and Training - extractive PDF cue:** If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset.
- **p. 4 / 5. Implementation - extractive PDF cue:** We use hash-based filtering to efficiently remove false negatives from the hard negative mining step to implement I(i, ji).
- **p. 8 / 7. Conclusion - extractive PDF cue:** An interesting avenue for future work is to extend the FCGF methodology to end-to-end registration.
- **p. 4 / 5. Implementation - extractive PDF cue:** Next, we find the hardest negatives for all positive pairs and filter out the hardest negatives that fall within the vicinity of positive pairs by ...
- **p. 4 / 5. Implementation - extractive PDF cue:** First, we create a matrix P that contains the indices of positive pairs (i, j) as well as an additional matrix Pdt that contains all ...
- **p. 5 / 6.1. Datasets and Training - extractive PDF cue:** If ICP fails or the number of overlapping voxels is less than 1k, we removed the pair from the dataset.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (5. Implementation), p. 8 (6.7. Runtime), objective p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 3 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 4 (4.2. Hardest-contrastive and Hardest-triplet Losses), p. 7 (6.4. Hardest-contrastive and Hardest-triplet Losses), temporal p. 4 (5. Implementation), p. 4 (5. Implementation), p. 5 (6.1. Datasets and Training), p. 5 (6.1. Datasets and Training), p. 7 (Method), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
