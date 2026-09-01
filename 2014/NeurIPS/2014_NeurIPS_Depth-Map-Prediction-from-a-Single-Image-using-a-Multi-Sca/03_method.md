# Method - Depth Map Prediction from a Single Image using a Multi-Scale Deep Network

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1406.2283; PDF retrieval source: https://arxiv.org/pdf/1406.2283. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3 Approach), p. 4 (3 Approach), p. 2 (3 Approach), p. 2 (3 Approach), p. 3 (3 Approach), p. 4 (3 Approach)): The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.

## Method Body Digest

- **p. 3 / 3 Approach - extractive PDF cue:** The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.
- **p. 4 / 3 Approach - extractive PDF cue:** We train the coarse network first against the ground-truth targets, then train the fine-scale network keeping the coarse-scale output fixed (i.e. when training the fine ...
- **p. 2 / 3 Approach - extractive PDF cue:** Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as additional first-layer image ...
- **p. 2 / 3 Approach - extractive PDF cue:** 3.1 Model Architecture Our network is made of two component stacks, shown in Fig.
- **p. 3 / 3 Approach - extractive PDF cue:** 1, the global, coarse-scale network contains five feature extraction layers of convolution and max-pooling, followed by two fully connected layers.
- **p. 4 / 3 Approach - extractive PDF cue:** 3, we set the per-sample training loss to 4
- **p. 5 / 3 Approach - extractive PDF cue:** Note the output of the network is log y; that is, the final linear layer predicts the log depth.
- **p. 4 / 3 Approach - extractive PDF cue:** 3.3 Training Loss In addition to performance evaluation, we also tried using the scale-invariant error as a training loss.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper we present a new approach for estimating depth from a single image.
- **p. 3 / 3 Approach - extractive PDF cue:** The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.
- **p. 4 / 3 Approach - extractive PDF cue:** In addition to the scale-invariant error, we also measure the performance of our method according to several error metrics have been proposed in prior works, ...

## Source Evidence Cues

- **p. 3 / 3 Approach - extractive PDF cue:** The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.
- **p. 4 / 3 Approach - extractive PDF cue:** We train the coarse network first against the ground-truth targets, then train the fine-scale network keeping the coarse-scale output fixed (i.e. when training the fine ...
- **p. 2 / 3 Approach - extractive PDF cue:** Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as additional first-layer image ...
- **p. 2 / 3 Approach - extractive PDF cue:** 3.1 Model Architecture Our network is made of two component stacks, shown in Fig.
- **p. 3 / 3 Approach - extractive PDF cue:** 1, the global, coarse-scale network contains five feature extraction layers of convolution and max-pooling, followed by two fully connected layers.
- **p. 4 / 3 Approach - extractive PDF cue:** 3, we set the per-sample training loss to 4
- **p. 5 / 3 Approach - extractive PDF cue:** Note the output of the network is log y; that is, the final linear layer predicts the log depth.
- **Detected method headings:** 3 Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features. | p. 3 (3 Approach), p. 4 (3 Approach) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We train the coarse network first against the ground-truth targets, then train the fine-scale network keeping the coarse-scale output fixed (i.e. when ... | p. 4 (3 Approach), p. 2 (3 Approach) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as ... | p. 2 (3 Approach), p. 2 (3 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Approach - extractive PDF cue:** 3, we set the per-sample training loss to 4
- **p. 4 / 3 Approach - extractive PDF cue:** 3.3 Training Loss In addition to performance evaluation, we also tried using the scale-invariant error as a training loss.
- **p. 5 / 3 Approach - extractive PDF cue:** We deal with these simply by masking them out and evaluating the loss only on valid points, i.e. we replace n in Eqn.
- **p. 5 / 3 Approach - extractive PDF cue:** 1. • Color: Input values are multiplied globally by a random RGB value c ∈[0.8, 1.2]3. • Flips: Input and target are horizontally flipped with ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 2 (3 Approach), p. 3 (3 Approach).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | stacks, applied, original, input, addition, coarse, network, output, passed, fine, additional, first-layer, image, features | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | stacks, applied, original, input, addition, coarse, network, output, passed, fine | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, estimating, depth, single, image, fine-scale, network, stack, consists, convolutional | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | per-sample, training, loss, addition, performance, evaluation, tried, scale-invariant, error, deal | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3 Approach - extractive PDF cue:** Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as additional first-layer image ...
- **p. 3 / 3 Approach - extractive PDF cue:** The input, feature map and output sizes are also given in Fig.
- **p. 3 / 3 Approach - extractive PDF cue:** The final output is at 1/4-resolution compared to the input (which is itself downsampled from the original dataset by a factor of 2), and corresponds ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our system achieves state-of-the art estimation rates on NYU Depth and KITTI, as well as improved qualitative outputs.
- **p. 5 / 3 Approach - extractive PDF cue:** 3.4 Data Augmentation We augment the training data with random online transformations (values shown for NYUDepth) 2: • Scale: Input and target images are scaled ...
- **p. 4 / 3 Approach - extractive PDF cue:** (a) (b) Figure 2: Weight vectors from layer Coarse 7 (coarse output), for (a) KITTI and (b) NYUDepth.
- **p. 4 / 3 Approach - extractive PDF cue:** 2 expresses the error by comparing relationships between pairs of pixels i, j in the output: to have low error, each pair of pixels in ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 4.1 NYU Depth The NYU Depth dataset [18] is composed of 464 indoor scenes, taken as video sequences using a Microsoft Kinect ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We use 56 scenes from the "city," "residential," and "road" 2For KITTI, s ∈[1, 1.2], and rotations are not performed (images are ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We use 56 scenes from the "city," "residential," and "road" 2For KITTI, s ∈[1, 1.2], and rotations are not performed (images are ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Approach - extractive PDF cue:** We train the coarse network first against the ground-truth targets, then train the fine-scale network keeping the coarse-scale output fixed (i.e. when training the fine ...
- **p. 4 / 3 Approach - extractive PDF cue:** 3, we set the per-sample training loss to 4
- **p. 5 / 4 Experiments - extractive PDF cue:** These ratios were found by trial-and-error on a validation set (folded back into the training set for our final evaluations), and the global scale of ...
- **p. 6 / 4 Experiments - extractive PDF cue:** As an additional reference, we also compare to the mean depth image computed across the training set.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** fine-scale, network, stack, consists, convolutional, layers, only, along, pooling, stage, first, layer, edge, features, train, coarse, against, ground-truth, targets, then.
- **Relevant PDF headings:** 3 Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We use the official train/test split, using 249 scenes for training and 215 for testing, and construct our training set using the ... | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Semantic / temporal fusion | 4.3 Baselines and Comparisons We compare our method against Make3D trained on the same datasets, as well as the published results of ... | p. 6 (4 Experiments), p. 6 (5 Results) |
| Robot query / planning handoff | Figure 3: Qualitative comparison of Make3D, our method trained with l2 loss (λ = 0), and our method trained with both l2 ... | p. 7 (Figure/Table caption), p. 6 (5 Results) |

## Failure and Ablation Link

- **p. 7 / 5 Results - extractive PDF cue:** 3 shows Make3D performing much better on this data, as expected, while using the scale-invariant error as a loss seems to have little effect in ...
- **p. 5 / 4 Experiments - extractive PDF cue:** To remove many invalid regions caused by windows, open doorways and specular surfaces we also mask out depths equal to the minimum or maximum recorded ...
- **p. 6 / 4 Experiments - extractive PDF cue:** We evaluate each method using several errors from prior works, as well as our scale-invariant metric: Threshold: % of yi s.t. max( yi y∗ i ...
- **p. 6 / 5 Results - extractive PDF cue:** 4, sorted top-to-bottom by scale-invariant MSE.
- **p. 7 / 5 Results - extractive PDF cue:** Just as importantly, there is a 25% gain in both the scale-dependent and scale-invariant RMSE errors, showing there is substantial improvement in the predicted structure.
- **p. 7 / 6 Discussion - extractive PDF cue:** In future work, we plan to extend our method to incorporate further 3D geometry information, such as surface normals.
- **p. 6 / 5 Results - extractive PDF cue:** Although the fine-scale network does not improve in the error measurements, its effect is clearly visible in the depth maps - surface boundaries have sharper ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3 Approach), p. 4 (3 Approach), p. 2 (3 Approach), p. 2 (3 Approach), p. 3 (3 Approach), p. 4 (3 Approach), objective p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach), temporal p. 5 (4 Experiments), p. 5 (4 Experiments), p. 2 (2 Related Work), p. 2 (2 Related Work), p. 6 (5 Results), p. 7 (5 Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
