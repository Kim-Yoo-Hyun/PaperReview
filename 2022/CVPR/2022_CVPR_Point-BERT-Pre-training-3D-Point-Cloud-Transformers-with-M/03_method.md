# Method - Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2111.14819; PDF retrieval source: https://arxiv.org/pdf/2111.14819. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Masked Point Modeling), p. 5 (3.3. Masked Point Modeling), p. 4 (3.3. Masked Point Modeling)): With our point patch mixing technique, the optimization of contrastive loss encourages the model to pay attention to the high-level semantics of point clouds by making features of the virtual ...

## Method Body Digest

- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** With our point patch mixing technique, the optimization of contrastive loss encourages the model to pay attention to the high-level semantics of point clouds by ...
- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** Coupling MPM objective and contrastive loss enables our Point-BERT to simultaneously capture the local geometric structures and high-level semantic patterns, which are crucial in point ...
- **p. 4 / 3.3. Masked Point Modeling - extractive PDF cue:** Motivated by BERT [8] and BEiT [2], we extend the masked modeling strategy to point cloud learning and devise a masked point modeling (MPM) task ...
- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** The pre-training objective can be formalized as maximizing the log-likelihood of the correct point tokens zi given the masked input embeddings XM: max X X∈D ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Block Masking Input Masked Input Output Random Masking Input Masked Input Output Real Scans from ScanObjectNN Input Masked Input Output Input Masked Input Output Figure ...
- **p. 2 / 1. Introduction - extractive PDF cue:** 2) Masked Point Modeling: A ‘masked point modeling' (MPM) task is performed to pre-train Transformers, which masks a portion of input point cloud and learns ...
- **p. 3 / 1. Introduction - extractive PDF cue:** We also show that the representations learned by Point-BERT transfer well to new tasks and domains, where our models largely advance the state-of-the-art of few-shot ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Compared to conventional hand-crafted feature extraction methods, Convolutional Neural Networks (CNN) [20] is dependent on much less prior knowledge.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Driven by the above analysis, we present Point-BERT, a new scheme for learning point cloud Transformers.
- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, the structural superiority and versatility of standard Transformers are proved in both language [3, 8, 18, 25, 36] and *Equal contribution. †Corresponding author.
- **p. 2 / 1. Introduction - extractive PDF cue:** We hope that our model enables reasoning the geometric relations among different patches of the point cloud, capturing meaningful geometric features for point cloud understanding.

## Source Evidence Cues

- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** With our point patch mixing technique, the optimization of contrastive loss encourages the model to pay attention to the high-level semantics of point clouds by ...
- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** Coupling MPM objective and contrastive loss enables our Point-BERT to simultaneously capture the local geometric structures and high-level semantic patterns, which are crucial in point ...
- **p. 4 / 3.3. Masked Point Modeling - extractive PDF cue:** Motivated by BERT [8] and BEiT [2], we extend the masked modeling strategy to point cloud learning and devise a masked point modeling (MPM) task ...
- **Detected method headings:** 3.3. Masked Point Modeling (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | With our point patch mixing technique, the optimization of contrastive loss encourages the model to pay attention to the high-level semantics of ... | p. 5 (3.3. Masked Point Modeling), p. 5 (3.3. Masked Point Modeling) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Coupling MPM objective and contrastive loss enables our Point-BERT to simultaneously capture the local geometric structures and high-level semantic patterns, which are ... | p. 5 (3.3. Masked Point Modeling), p. 4 (3.3. Masked Point Modeling) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Motivated by BERT [8] and BEiT [2], we extend the masked modeling strategy to point cloud learning and devise a masked point ... | p. 4 (3.3. Masked Point Modeling) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** The pre-training objective can be formalized as maximizing the log-likelihood of the correct point tokens zi given the masked input embeddings XM: max X X∈D ...
- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** Coupling MPM objective and contrastive loss enables our Point-BERT to simultaneously capture the local geometric structures and high-level semantic patterns, which are crucial in point ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Masked Point Modeling), p. 5 (3.3. Masked Point Modeling).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Block, Masking, Input, Masked, Output, Random, Real, Scans, ScanObjectNN, Figure, Point, Modeling, MPM, task | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Block, Masking, Input, Masked, Output, Random, Real, Scans, ScanObjectNN, Figure | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Driven, above, analysis, present, Point-BERT, scheme, learning, point, cloud, Transformers | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | pre-training, objective, formalized, maximizing, log-likelihood, correct, point, tokens, given, masked | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** Block Masking Input Masked Input Output Random Masking Input Masked Input Output Real Scans from ScanObjectNN Input Masked Input Output Input Masked Input Output Figure ...
- **p. 2 / 1. Introduction - extractive PDF cue:** 2) Masked Point Modeling: A ‘masked point modeling' (MPM) task is performed to pre-train Transformers, which masks a portion of input point cloud and learns ...
- **p. 3 / 1. Introduction - extractive PDF cue:** We also show that the representations learned by Point-BERT transfer well to new tasks and domains, where our models largely advance the state-of-the-art of few-shot ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Compared to conventional hand-crafted feature extraction methods, Convolutional Neural Networks (CNN) [20] is dependent on much less prior knowledge.
- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** In practice, we directly apply such a block-wise masking strategy like [2] to the inputs of the Transformer.
- **p. 5 / 3.3. Masked Point Modeling - extractive PDF cue:** Finally, the corrupted input embeddings XM = {xi : i /∈M}g i=1 ∪{E[M] + posi : i ∈M}g i=1 are fed into the Transformer encoder.
- **p. 3 / 1. Introduction - extractive PDF cue:** We hope a neat and unified Transformer architecture across images and point clouds could facilitate both domains since it enables joint modeling of 2D and ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The learning rate is set to 0.0005 with a cosine learning schedule with 60,000 steps warming up. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We set the weight of KLD loss to 0 in the first 10,000 steps and gradually increased to 0.1 in the following ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In terms of MoCo, we set the memory bank size to 16,384, temperature to 0.07, and weight momentum to 0.999. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The learning rate is set to 0.0005 with a cosine learning schedule with 60,000 steps warming up. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.1. Pre-training Setups - extractive PDF cue:** The model is trained for 300 epochs with a batch size of 128.
- **p. 6 / 4.1. Pre-training Setups - extractive PDF cue:** We train dVAE for a total of 150,000 steps with a batch size of 64.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** point, patch, mixing, technique, optimization, contrastive, loss, encourages, model, attention, high-level, semantics, clouds, making, features, virtual, samples, closely, possible, corresponding.
- **Relevant PDF headings:** 3.3. Masked Point Modeling (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation ... | p. 8 (4.4. Visualization), p. 7 (4.2. Downstream Tasks) |
| Semantic / temporal fusion | Additionally, we compare with a recent pre-training strategy OcCo [52] as a strong baseline of our pre-training method. | p. 6 (4.2. Downstream Tasks), p. 6 (4.1. Pre-training Setups) |
| Robot query / planning handoff | As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both ... | p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation study. We investigate the effects of different designs and report the classification accuracy (%) after fine-tuning on ModelNet40. All models are trained ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We also conduct an ablation study for our Point-BERT.
- **p. 6 / 4.2. Downstream Tasks - extractive PDF cue:** We also observe that adding more points will not significantly improve the Transformer model without pre-training while Point-BERT models can be consistently improved by increasing ...
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** We follow previous works to conduct experiments on three main variants: OBJ-BG, OBJ-ONLY, and PB-T50-RS.
- **p. 5 / 4. Experiments - extractive PDF cue:** In this section, we first introduce the setups of our pretraining scheme.
- **p. 8 / 4.4. Visualization - extractive PDF cue:** As can be seen, features from different categories can be well separated by our method even before fine-tuning.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** We also consider another type of augmentations: randomly replace some input embeddings with those from other samples.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Masked Point Modeling), p. 5 (3.3. Masked Point Modeling), p. 4 (3.3. Masked Point Modeling), objective p. 5 (3.3. Masked Point Modeling), p. 5 (3.3. Masked Point Modeling), temporal p. 5 (4.1. Pre-training Setups), p. 5 (4.1. Pre-training Setups), p. 6 (4.1. Pre-training Setups), p. 6 (4.1. Pre-training Setups), p. 7 (4.2. Downstream Tasks), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
