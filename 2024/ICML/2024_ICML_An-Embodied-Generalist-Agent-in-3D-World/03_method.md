# Method - An Embodied Generalist Agent in 3D World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.12871; PDF retrieval source: https://arxiv.org/pdf/2311.12871. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2. Model), p. 3 (2.3. Training & Inference), p. 4 (2.3. Training & Inference), p. 4 (2.3. Training & Inference), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World)): Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings.

## Method Body Digest

- **p. 3 / 2. Model - extractive body cue:** Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings.
- **p. 3 / 2.3. Training & Inference - extractive body cue:** During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, and the LoRA ...
- **p. 4 / 2.3. Training & Inference - extractive body cue:** For tasks that require action commands, we map the textual outputs to action commands as discussed in Sec.
- **p. 4 / 2.3. Training & Inference - extractive body cue:** More details on the model and training can be found in Appendix D.
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** Notably, all baselines are equipped with recurrent modules while LEO only incorporates truncated past actions, which could account for a lower success rate (see discussion ...
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** 3RScan ScanNet (0-shot) Yes No Overall Yes No Overall w/o Aug 1.00 0.01 0.34 0.98 0.16 0.43 w/ Aug 0.72 0.91 0.85 0.88 0.81 0.83 ...
- **p. 6 / 4.2. Scene-grounded Dialogue and Planning - extractive body cue:** A.1, LEO is capable of generating high-quality responses, which encompass two features: 1) Precisely grounded to the 3D scenes.
- **p. 3 / 2.3. Training & Inference - extractive body cue:** We formulate the learning objective of LEO following (Brown et al., 2020; Raffel et al., 2020) in a prefix language modeling fashion.

## Design Rationale

- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** We present the results of CLIPort manipulation and object navigation in Tabs.
- **p. 1 / 1. Introduction - extractive body cue:** The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, large-scale unified pretraining and efficient finetuning are under-explored by previous 3D VL models, which are often designed with strong priors (Zhao et al., 2021; ...

## Source Evidence Cues

- **p. 3 / 2. Model - extractive body cue:** Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings.
- **p. 3 / 2.3. Training & Inference - extractive body cue:** During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, and the LoRA ...
- **p. 4 / 2.3. Training & Inference - extractive body cue:** For tasks that require action commands, we map the textual outputs to action commands as discussed in Sec.
- **p. 4 / 2.3. Training & Inference - extractive body cue:** More details on the model and training can be found in Appendix D.
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** Notably, all baselines are equipped with recurrent modules while LEO only incorporates truncated past actions, which could account for a lower success rate (see discussion ...
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** 3RScan ScanNet (0-shot) Yes No Overall Yes No Overall w/o Aug 1.00 0.01 0.34 0.98 0.16 0.43 w/ Aug 0.72 0.91 0.85 0.88 0.81 0.83 ...
- **p. 6 / 4.2. Scene-grounded Dialogue and Planning - extractive body cue:** A.1, LEO is capable of generating high-quality responses, which encompass two features: 1) Precisely grounded to the 3D scenes.
- **Detected method headings:** 2. Model (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings. | p. 3 (2. Model), p. 3 (2.3. Training & Inference) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, ... | p. 3 (2.3. Training & Inference), p. 4 (2.3. Training & Inference) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | For tasks that require action commands, we map the textual outputs to action commands as discussed in Sec. | p. 4 (2.3. Training & Inference), p. 4 (2.3. Training & Inference) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2.3. Training & Inference - extractive body cue:** We formulate the learning objective of LEO following (Brown et al., 2020; Raffel et al., 2020) in a prefix language modeling fashion.
- **p. 3 / 2. Model - extractive body cue:** Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings.
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** 3RScan ScanNet (0-shot) Yes No Overall Yes No Overall w/o Aug 1.00 0.01 0.34 0.98 0.16 0.43 w/ Aug 0.72 0.91 0.85 0.88 0.81 0.83 ...
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** Test Loss (104) #Data 1.5 2.0 3 6 12 1.6 1.2 0.8 Aligned OPT-1.3B Scratch Vicuna-7B Aligned Vicuna-7B Aligned Vicuna-13B ditionally, we test generalization to ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (2. Model), p. 3 (2.3. Training & Inference), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | leading, design, principles, LEO, two-fold, should, handle, multi-modal, input, egocentric, global, textual, instruction, output | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | leading, design, principles, LEO, two-fold, should, handle, multi-modal, input, egocentric | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, CLIPort, manipulation, object, navigation, Tabs, development, generalist, agents, encounters | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | formulate, learning, objective, LEO, following, Brown, Raffel, prefix, language, modeling | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2. Model - extractive body cue:** The leading design principles of LEO are two-fold: 1) It should handle the multi-modal input of egocentric 2D, global 3D, and textual instruction, and the ...
- **p. 4 / 2.3. Training & Inference - extractive body cue:** For tasks that require action commands, we map the textual outputs to action commands as discussed in Sec.
- **p. 6 / 4.2. Scene-grounded Dialogue and Planning - extractive body cue:** Upon the 3D VL understanding and reasoning, we anticipate LEO to support more sophisticated interaction with humans, e.g., responding to complex multi-round user instructions in ...
- **p. 3 / 2.1. Tokenization - extractive body cue:** We use SentencePiece tokenizer (Kudo & Richardson, 2018) to encode text with 32k subwords; 2D image tokens for egocentric 2D images; and object-centric 3D tokens ...
- **p. 6 / 4.2. Scene-grounded Dialogue and Planning - extractive body cue:** The task plan proposed by LEO involves concrete objects related to the 3D scene, as well as plausible actions regarding these objects.
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** In particular, LEO directly produces motor commands without inductive bias (e.g., heatmap) that benefit previous methods, showcasing LEO's considerable capacity for learning embodied actions.
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** 2) In ObjNav, LEO achieves a success rate that is comparable to the baselines and has a better SPL on MP3D-val, suggesting that LEO can ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Consequently, all the tasks are formulated as sequence prediction, thereby accommodating a unified training objective. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | It takes egocentric 2D images, 3D point clouds, and texts as input and formulates comprehensive 3D tasks as autoregressive sequence prediction. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 2. Model - extractive body cue:** Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings.
- **p. 3 / 2.3. Training & Inference - extractive body cue:** During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, and the LoRA ...
- **p. 4 / 2.3. Training & Inference - extractive body cue:** More details on the model and training can be found in Appendix D.
- **p. 3 / 2.3. Training & Inference - extractive body cue:** During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, and the LoRA ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Next, will, detail, tokenization, multimodal, data, model, architecture, training, loss, inference, settings, During, freeze, pretrained, point, cloud, encoder, LLM, finetune.
- **Relevant PDF headings:** 2. Model (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Next, we manually design some examples as seed tasks (Liu et al., 2023b), including scene and object captioning, QA, dialogue, and planning, ... | p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 4 (3. Datasets) |
| Semantic / temporal fusion | Compared to counterparts that utilize object boxes (Yin et al., 2023; Hong et al., 2023; Wang et al., 2023e), it offers both ... | p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 6 (Figure/Table caption) |
| Robot query / planning handoff | Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and ... | p. 5 (Figure/Table caption), p. 8 (4.5. Scaling Law Analysis) |

## Failure and Ablation Link

- **p. 5 / 3.3. LLM-assisted 3D-language Data Generation - extractive body cue:** Clean the floor by sweeping to remove any dirt.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 7: Quantitative results of LEO trained with differ- ent data configurations. w/o Align: without alignment stage. ScanNet: tuned on ScanNet scenes only. w/o Act: ...
- **p. 4 / 3. Datasets - extractive body cue:** Due to the space limit, we defer details including data source and components to Appendix B.1.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The proposed embodied generalist agent LEO. It takes egocentric 2D images, 3D point clouds, and texts as input and formulates comprehensive 3D tasks ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2. Model), p. 3 (2.3. Training & Inference), p. 4 (2.3. Training & Inference), p. 4 (2.3. Training & Inference), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World), objective p. 3 (2.3. Training & Inference), p. 3 (2. Model), p. 7 (4.3. Embodied Action in 3D World), p. 7 (4.3. Embodied Action in 3D World), temporal p. 2 (3. Fold and organize …), p. 2 (3. Fold and organize …), p. 3 (2. Model), p. 3 (2.2. Token Embedding & LLM), p. 7 (4.3. Embodied Action in 3D World).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
