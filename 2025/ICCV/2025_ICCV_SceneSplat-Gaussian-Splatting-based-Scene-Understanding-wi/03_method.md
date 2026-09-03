# Method - SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining), p. 6 (4.3. Self Supervised Pretraining), p. 4 (4.1. 3DGS Language Label Collection), p. 5 (4.3. Self Supervised Pretraining)): We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels.

## Method Body Digest

- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels.
- **p. 5 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** To enforce feature similarity in Euclidean space, we use L2 loss: \ m ath c al {L }_{ 2 } = \ frac {1}{/\mathcal {V}/} ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** We propose to mitigate the decoder collapse issues by multitask reconstruction LMGM, as coding rate regularization stabilizes only the hierarchical encoder.
- **p. 4 / 4.1. 3DGS Language Label Collection - extractive body cue:** We then use Occam's LGS [4] to efficiently lift these 2D feature maps to a 3D Gaussian feature field in an optimization-free manner.
- **p. 5 / 4.3. Self Supervised Pretraining - extractive body cue:** It incorporates multiple losses with different objectives into SceneSplat's large-scale pretraining.
- **p. 7 / Method - extractive body cue:** 3 comparing against the state-ofthe-art Point Transformer method.
- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** The cosine similarity loss minimizes the angular difference be4964

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene ...
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we propose GaussSSL, a self-supervised learning scheme that unlocks rich 3D feature learning from unlabeled scenes.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** We propose to mitigate the decoder collapse issues by multitask reconstruction LMGM, as coding rate regularization stabilizes only the hierarchical encoder.

## Source Evidence Cues

- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels.
- **p. 5 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** To enforce feature similarity in Euclidean space, we use L2 loss: \ m ath c al {L }_{ 2 } = \ frac {1}{/\mathcal {V}/} ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** We propose to mitigate the decoder collapse issues by multitask reconstruction LMGM, as coding rate regularization stabilizes only the hierarchical encoder.
- **p. 4 / 4.1. 3DGS Language Label Collection - extractive body cue:** We then use Occam's LGS [4] to efficiently lift these 2D feature maps to a 3D Gaussian feature field in an optimization-free manner.
- **p. 5 / 4.3. Self Supervised Pretraining - extractive body cue:** It incorporates multiple losses with different objectives into SceneSplat's large-scale pretraining.
- **p. 7 / Method - extractive body cue:** 3 comparing against the state-ofthe-art Point Transformer method.
- **Detected method headings:** 4. Methodology (p. 4); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We first adapt the transformer encoder-decoder backbone from [51] to efficiently predict high-dimensional perprimitive features corresponding to collected 3DGS language labels. | p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To enforce feature similarity in Euclidean space, we use L2 loss: \ m ath c al {L }_{ 2 } = \ ... | p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute ... | p. 6 (4.3. Self Supervised Pretraining), p. 6 (4.3. Self Supervised Pretraining) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** The cosine similarity loss minimizes the angular difference be4964
- **p. 5 / 4.3. Self Supervised Pretraining - extractive body cue:** It incorporates multiple losses with different objectives into SceneSplat's large-scale pretraining.
- **p. 5 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** Hence, we compute a cross-entropy loss in both directions: \mathca l
- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** We apply three training objectives for supervision.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** However, the high dimensionality of these language features (dimension N × dL ) can substantially increase the computational cost of supervision.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Self Supervised Pretraining), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining), p. 7 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | output, tokens, mapped, input, Gaussian, space, reconstruction, projector, SceneSplat, introduces, DGS, encoder, takes, parameters | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | output, tokens, mapped, input, Gaussian, space, reconstruction, projector, SceneSplat, introduces | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, present, SceneSplat-7K, high-quality, large-scale, Gaussian, splats, dataset | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | cosine, similarity, loss, minimizes, angular, difference, be4964, incorporates, multiple, losses | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4.3. Self Supervised Pretraining - extractive body cue:** (5) The output tokens ˆ Tm are mapped to the input Gaussian space with the reconstruction projector ˆGm = Φ( ˆTm) ∈RN′×F .
- **p. 2 / 1. Introduction - extractive body cue:** SceneSplat introduces a 3DGS encoder that takes as input the parameters of a Gaussian-splat scene (center, scale, color, opacity) and outputs semantic features in a ...
- **p. 4 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** More specifically, our model g(·), parameterized by θ, maps the input Gaussians to their language features: \ hat {F} = g_ \theta (\{G_i\}_{i=1}^N) \enspace , ...
- **p. 5 / 4.2. Vision-Language 3DGS Pretraining - extractive body cue:** Through this training, our model learns to predict semantically rich language features for each Gaussian primitive, enabling downstream open-vocabulary scene understanding task without requiring additional ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We present SceneSplat-7K, a high-quality large-scale Gaussian splats dataset spanning 7K indoor scenes, which boosts 3DGS scene ...
- **p. 4 / 4.1. 3DGS Language Label Collection - extractive body cue:** 1, we employ SAMv2 [40] for object-level segmentation and SigLIP2 [47] for feature extraction.
- **p. 6 / 4.3. Self Supervised Pretraining - extractive body cue:** For a batch of Gaussian scenes {Gn}B n=1 (global/local views Gb g, Gb l), we extract tokenized bottleneck features z ∈RM×de, compute global representations ¯z ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Furthermore, for self-supervised pretraining, we employ a multi-objective self-supervised training framework that integrates reconstruction and selfdistillation alignment (Sec. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To address this, we replace the original features with a compressed representation learned via an autoencoder [19], drastically reducing the memory overhead ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | To address this, we replace the original features with a compressed representation learned via an autoencoder [19], drastically reducing the memory overhead ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Starting with the training views, we select scenes with at least 400 frames to ensure sufficient multi-view coverage. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Self Supervised Pretraining - extractive body cue:** It incorporates multiple losses with different objectives into SceneSplat's large-scale pretraining.
- **p. 8 / 5.3. Further Statistical Evaluation - extractive body cue:** 6 presents scaling results Method Steps Required Runtime / Scene Occam's LGS 2D fusion + lifting 107 min SceneSplat single inference 0.24 min Table 9.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, adapt, transformer, encoder-decoder, backbone, efficiently, predict, high-dimensional, perprimitive, features, corresponding, collected, DGS, language, labels, enforce, feature, similarity, Euclidean, space.
- **Relevant PDF headings:** 4. Methodology (p. 4); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset contains about seven thousand scenes, including both real-world and synthetic environments. | p. 3 (3. SceneSplat Dataset), p. 8 (5.3. Further Statistical Evaluation) |
| Semantic / temporal fusion | Table 4. Supervised Semantic Segmentation Experiments. We report our best results from Tab. 3 comparing against the state-of- the-art Point Transformer method. ... | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | Our method achieves a +0.1% improvement over supervised-only baselines on ScanNet20 and +0.5% on ScanNet200, while observing a performance drop on ScanNet++ ... | p. 6 (5.2. Label-free 3DGS Pretraining), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 5.3. Further Statistical Evaluation - extractive body cue:** Ablation on Contrastive Loss in the Vision-Language Pretraining.
- **p. 8 / 5.3. Further Statistical Evaluation - extractive body cue:** Ablation on Contrastive Loss During VisionLanguage Pretraining Using Subsets.
- **p. 6 / 5. Experiments - extractive body cue:** We further justify our design choices through ablation studies.
- **p. 6 / 5.1. Vision-Language Pretraining - extractive body cue:** Our visionlanguage pretraining enables the effective localization of complex objects within the scene.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. SceneSplat Overview. The SceneSplat-7K dataset enables Vision-Language Pretraining and Self-Supervised Pretrain- ing. For vision-language pretraining, we associate each 3D Gaussian primitive with semantic ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. GaussianSSL Ablation Experiments. We adopt the pre- training on the SceneSplat-7K dataset and report fine-tuning mIoU and mAcc on indoor semantic segmentation tasks. ...
- **p. 4 / 3.1. Data Processing - extractive body cue:** We remove blurry frames by using the variance of the Laplacian as a sharpness metric.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining), p. 6 (4.3. Self Supervised Pretraining), p. 4 (4.1. 3DGS Language Label Collection), p. 5 (4.3. Self Supervised Pretraining), objective p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 5 (4.3. Self Supervised Pretraining), p. 5 (4.2. Vision-Language 3DGS Pretraining), p. 4 (4.2. Vision-Language 3DGS Pretraining), p. 6 (4.3. Self Supervised Pretraining), p. 6 (4.3. Self Supervised Pretraining), temporal p. 4 (4. Methodology), p. 6 (4.3. Self Supervised Pretraining), p. 8 (5.3. Further Statistical Evaluation), p. 3 (3.1. Data Processing), p. 3 (2. Related Work), p. 4 (3.1. Data Processing).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
