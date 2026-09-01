# Method - 3D-LLM: Injecting the 3D World into Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.12981; PDF retrieval source: https://arxiv.org/pdf/2307.12981. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 5 (5. Facing the mirror and dress)): To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs that could take 3D representations (i.e., 3D point ...

## Method Body Digest

- **p. 2 / 5. Facing the mirror and dress - extractive PDF cue:** To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs that could take ...
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Then, we use pretrained 2D VLMs as our backbones, input the aligned 3D features to train 3D-LLMs with our collected 3D-language dataset.
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** We introduce a 3D localization mechanism for training the 3D-LLMs to better capture 3D spatial information. • Experiments on held-out evaluation dataset, ScanQA, outperform state-of-the-art ...
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** To sum up, our paper has the following contributions: • We introduce a new family of 3D-based Large Language models (3D-LLMs) that can take 3D ...
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Therefore, we use the 3D feature extractor to extract the 3D features in the same feature space as the features of the frozen image encoders.
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** We first render a few multi-view images from the 3D scene, extract 2D dense features, and then construct 3D features from these multi-view images using ...
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** Using these alignment methods, we could use pretrained image encoders to extract image features, and then map the features to the 3D data.
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Then we align 3D features in the rays and 2D features in the pixels using MSE loss.

## Design Rationale

- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** To sum up, our paper has the following contributions: • We introduce a new family of 3D-based Large Language models (3D-LLMs) that can take 3D ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we propose to inject the 3D world into large language models and introduce a whole new family of 3D-LLMs.
- **p. 2 / 5. Facing the mirror and dress - extractive PDF cue:** To address this, we propose a set of unique data generation pipelines that could generate large-scale 3D data paired with language.

## Source Evidence Cues

- **p. 2 / 5. Facing the mirror and dress - extractive PDF cue:** To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs that could take ...
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Then, we use pretrained 2D VLMs as our backbones, input the aligned 3D features to train 3D-LLMs with our collected 3D-language dataset.
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** We introduce a 3D localization mechanism for training the 3D-LLMs to better capture 3D spatial information. • Experiments on held-out evaluation dataset, ScanQA, outperform state-of-the-art ...
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** To sum up, our paper has the following contributions: • We introduce a new family of 3D-based Large Language models (3D-LLMs) that can take 3D ...
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Therefore, we use the 3D feature extractor to extract the 3D features in the same feature space as the features of the frozen image encoders.
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** We first render a few multi-view images from the 3D scene, extract 2D dense features, and then construct 3D features from these multi-view images using ...
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** Using these alignment methods, we could use pretrained image encoders to extract image features, and then map the features to the 3D data.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs ... | p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then, we use pretrained 2D VLMs as our backbones, input the aligned 3D features to train 3D-LLMs with our collected 3D-language dataset. | p. 6 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We introduce a 3D localization mechanism for training the 3D-LLMs to better capture 3D spatial information. • Experiments on held-out evaluation dataset, ... | p. 3 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Then we align 3D features in the rays and 2D features in the pixels using MSE loss.
- **p. 2 / 5. Facing the mirror and dress - extractive PDF cue:** By taking the 3D representations of scenes as input, LLMs are blessed with twofold advantages: (1) long-term memories about the entire scene can be stored ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (5. Facing the mirror and dress).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | inject, world, large, language, models, introduce, whole, family, D-LLMs, could, take, representations, point, clouds | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | inject, world, large, language, models, introduce, whole, family, D-LLMs, could | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | following, contributions, introduce, family, D-based, Large, Language, models, D-LLMs, take | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Then, align, features, rays, pixels, MSE, loss, taking, representations, scenes | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 5. Facing the mirror and dress - extractive PDF cue:** To this end, we propose to inject the 3D world into large language models, and introduce a whole new family of 3D-LLMs that could take ...
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** The 2D image features, output from frozen image encoders, are flattened and sent to the perceiver to generate a fixed-sized input.
- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** After adding these additional location tokens, we unfreeze the weights for these tokens in the input and output embeddings of language models.
- **p. 2 / 5. Facing the mirror and dress - extractive PDF cue:** By taking the 3D representations of scenes as input, LLMs are blessed with twofold advantages: (1) long-term memories about the entire scene can be stored ...
- **p. 1 / Abstract - extractive PDF cue:** Specifically, 3D-LLMs can take 3D point clouds and their features as input and perform a diverse set of 3D-related tasks, including captioning, dense captioning, 3D ...
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** In addition, we append a series of location tokens to the 3D-LLMs, and localization can be trained via outputting location tokens given the language descriptions ...
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** To better align these LLMs' predictions to human instructions, improve the models' generalization abilities on unseen tasks, a series of instruction tuning methods [35, 44] ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Using Pretrained BLIP-2 as backbones, we train 3D-LLMs for 100K steps, and validate every 1K step. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Additionally, we apply a linear warmup of the learning rate during the initial 1K steps, increasing from 10-8 to 10-5, followed by ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The learning rate is increased linearly from 0 to 10-4 up over the first 5000 steps then held constant for the duration ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5. Facing the mirror and dress - extractive PDF cue:** Then, we use pretrained 2D VLMs as our backbones, input the aligned 3D features to train 3D-LLMs with our collected 3D-language dataset.
- **p. 3 / 5. Facing the mirror and dress - extractive PDF cue:** We introduce a 3D localization mechanism for training the 3D-LLMs to better capture 3D spatial information. • Experiments on held-out evaluation dataset, ScanQA, outperform state-of-the-art ...
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** Using these alignment methods, we could use pretrained image encoders to extract image features, and then map the features to the 3D data.
- **p. 14 / B.1 Implementation Details - extractive PDF cue:** The learning rate is increased linearly from 0 to 10-4 up over the first 5000 steps then held constant for the duration of training.
- **p. 5 / 5. Facing the mirror and dress - extractive PDF cue:** Furthermore, for 3D scenes, there are no available pretrained encoders like those for 2D images (e.g., CLIP ViT encoders).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** inject, world, large, language, models, introduce, whole, family, D-LLMs, could, take, representations, point, clouds, features, input, perform, series, D-related, tasks.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Specifically, our 3D-language data generation pipeline generates the held-in datasets of multiple tasks. we split the datasets into train/val/test sets (8:1:1). | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Semantic / temporal fusion | Table 2. We observe a significant increase in the evaluation metrics. For example, for BLEU-1, our model outperforms the state-of-the-art ScanQA model ... | p. 7 (Figure/Table caption), p. 8 (5 Experiments) |
| Robot query / planning handoff | Our model outperforms all baseline models for most of the evaluation metrics. they have much lower performances compared to 3D-LLMs, probably because ... | p. 8 (5 Experiments), p. 14 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive PDF cue:** This shows that our model could perform visual reasoning about objects and their relationships even without explicit object representations.
- **p. 7 / 5 Experiments - extractive PDF cue:** Furthermore, 3D-based baselines use object detectors like VoteNet to segment the objects, and then send per-object features into their models, while our inputs are holistic ...
- **p. 8 / 5 Experiments - extractive PDF cue:** We add one language-only baseline: FlanT5, which examines LLMs' ability to complete these tasks without any visual input.
- **p. 13 / B.1 Implementation Details - extractive PDF cue:** Using Pretrained BLIP-2 as backbones, we train 3D-LLMs for 100K steps, and validate every 1K step.
- **p. 13 / B.1 Implementation Details - extractive PDF cue:** 3D-LLMs based on pretrained flamingo are trained using the AdamW optimizer with global norm clipping of 1, no weight decay for the perceiver resampler and ...
- **p. 9 / 6 Conclusion - extractive PDF cue:** A limitation is that the 3D feature extractor relies on 2D multi-view images, and thus all 3D scenes need to be rendered so that they ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We report BLEU, ROUGE-L, METEOR, CIDEr for robust answer matching.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress), p. 3 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress), p. 5 (5. Facing the mirror and dress), objective p. 6 (5. Facing the mirror and dress), p. 2 (5. Facing the mirror and dress), temporal p. 13 (B.1 Implementation Details), p. 13 (B.1 Implementation Details), p. 14 (B.1 Implementation Details), p. 5 (5. Facing the mirror and dress), p. 5 (5. Facing the mirror and dress), p. 6 (5. Facing the mirror and dress).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
