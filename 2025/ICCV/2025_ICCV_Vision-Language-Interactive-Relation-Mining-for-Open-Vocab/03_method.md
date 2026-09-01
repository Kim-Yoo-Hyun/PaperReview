# Method - Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Generative Relation Recognition), p. 5 (3.4. Training Objectives), p. 3 (3.1. OV-SGG Architecture), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method), p. 3 (3.1. OV-SGG Architecture)): As for the decoder, we use cross-attention layers to make the text embedding interface with the relation embedding from the encoder.

## Method Body Digest

- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** As for the decoder, we use cross-attention layers to make the text embedding interface with the relation embedding from the encoder.
- **p. 5 / 3.4. Training Objectives - extractive PDF cue:** Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c al {L } ...
- **p. 3 / 3.1. OV-SGG Architecture - extractive PDF cue:** 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a text encoder EncL ...
- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive PDF cue:** We use pre-trained GLIP [19] models to initialize our model and keep the visual backbone and text encoder frozen.
- **p. 3 / 3.1. OV-SGG Architecture - extractive PDF cue:** We first utilize a transformer-based interaction classifier to encode the scene graphs in I.
- **p. 5 / 3.3. Hierarchical Relation Extension - extractive PDF cue:** Then, the NWGM approximation for the model F(x) can be formulate as: \mathbb { E}(\op er at o rname { sigm oid}\l eft (F\left (\boldsymbol ...
- **p. 5 / 3.4. Training Objectives - extractive PDF cue:** Specifically, based on the relation logit ˆrdebias i , we can calculate a binary cross entropy loss with given ground truths: \b e gi n ...

## Design Rationale

- **p. 4 / 3.3. Hierarchical Relation Extension - extractive PDF cue:** To mitigate the overfitting of VLM to the base dataset from the semantical level, we propose to construct a semantic-unbiased VLM.
- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive PDF cue:** Our method achieves comparable performance to prior models, without requiring access to various instruction prompts or additional pretraining.

## Source Evidence Cues

- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** As for the decoder, we use cross-attention layers to make the text embedding interface with the relation embedding from the encoder.
- **p. 5 / 3.4. Training Objectives - extractive PDF cue:** Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c al {L } ...
- **p. 3 / 3.1. OV-SGG Architecture - extractive PDF cue:** 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a text encoder EncL ...
- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive PDF cue:** We use pre-trained GLIP [19] models to initialize our model and keep the visual backbone and text encoder frozen.
- **p. 3 / 3.1. OV-SGG Architecture - extractive PDF cue:** We first utilize a transformer-based interaction classifier to encode the scene graphs in I.
- **p. 5 / 3.3. Hierarchical Relation Extension - extractive PDF cue:** Then, the NWGM approximation for the model F(x) can be formulate as: \mathbb { E}(\op er at o rname { sigm oid}\l eft (F\left (\boldsymbol ...
- **Detected method headings:** 3. Method (p. 3); 3.1. OV-SGG Architecture (p. 3); Method (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | As for the decoder, we use cross-attention layers to make the text embedding interface with the relation embedding from the encoder. | p. 4 (3.2. Generative Relation Recognition), p. 5 (3.4. Training Objectives) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c ... | p. 5 (3.4. Training Objectives), p. 3 (3.1. OV-SGG Architecture) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a ... | p. 3 (3.1. OV-SGG Architecture), p. 4 (3.2. Generative Relation Recognition) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Training Objectives - extractive PDF cue:** Specifically, we use cross-entropy loss for each word in the generated text, and the language modeling loss is: \ma t h c al {L } ...
- **p. 5 / 3.4. Training Objectives - extractive PDF cue:** Specifically, based on the relation logit ˆrdebias i , we can calculate a binary cross entropy loss with given ground truths: \b e gi n ...
- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** The probability of the next word wi is predicted by the preceding words w1 i , ..., wt-1 i in text sequence, which can be ...
- **p. 6 / Method - extractive PDF cue:** The optimizer is AdamW [27] with a weight decay of 0.05.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.4. Training Objectives), p. 5 (3.3. Hierarchical Relation Extension).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Moreover, recent, advancements, instruction, prompt, sequence, thus, model, could, more, efficiently, utilize, image-text, pair | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Moreover, recent, advancements, instruction, prompt, sequence, thus, model, could, more | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | mitigate, overfitting, VLM, base, dataset, semantical, level, construct, semantic-unbiased, directly | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Specifically, cross-entropy, loss, word, generated, text, language, modeling, t/V_, goal | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** Moreover, recent advancements propose using an instruction prompt sequence, thus the model could more efficiently utilize the image-text pair knowledge of pre-trained VLMs or Large ...
- **p. 3 / 3.1. OV-SGG Architecture - extractive PDF cue:** 3, the OV-SGG architecture comprises three primary components: an image encoder EncI (e.g., Swin Transformer backbone [26]) for image feature extraction, a text encoder EncL ...
- **p. 4 / 3.1. OV-SGG Architecture - extractive PDF cue:** To further improve the performance of VLM on OV-SGG, we propose to address the existing challenge of OV-SGG by enhancing the visual-text modality interaction to ...
- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** Particularly, we employ an encoder-decoder-based conditional language generation model, where visual representation serves as input for the language encoder, and the associated text (i.e., the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** 3, our VL-IRM contains two major components: a relation encoder for visual relation feature extraction and a language model to generate relation names.
- **p. 3 / 3.1. OV-SGG Architecture - extractive PDF cue:** We first utilize a transformer-based interaction classifier to encode the scene graphs in I.
- **p. 6 / 4.2. Compared with State-of-the-arts - extractive PDF cue:** This result suggests that by enhancing the interaction 16760
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The probability of the next word wi is predicted by the preceding words w1 i , ..., wt-1 i in text sequence, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Different from distilling frozen vision encoder, OVSGTR [5] proposes a two-step framework for image-caption grounding pre-training and end-to-end detection fine-tuning, using a ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Generative Relation Recognition - extractive PDF cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive PDF cue:** We use pre-trained GLIP [19] models to initialize our model and keep the visual backbone and text encoder frozen.
- **p. 5 / 3.3. Hierarchical Relation Extension - extractive PDF cue:** Then, the NWGM approximation for the model F(x) can be formulate as: \mathbb { E}(\op er at o rname { sigm oid}\l eft (F\left (\boldsymbol ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** decoder, cross-attention, layers, make, text, embedding, interface, relation, encoder, Specifically, cross-entropy, loss, word, generated, language, modeling, t/V_, goal, minimize, negative.
- **Relevant PDF headings:** 3. Method (p. 3); 3.1. OV-SGG Architecture (p. 3); Method (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | As for VG dataset, We considered two different settings in the PGSG [21] and OVSGTR [5]. | p. 5 (4.1. Datasets and Experimental Settings), p. 5 (4.1. Datasets and Experimental Settings) |
| Global / local decision | Specifically, without the full supervision of novel categories, our model can provide novel relationship predictions (e.g., "from" and ‘part of'). | p. 8 (4.4. Qualitative Results), p. 7 (Figure/Table caption) |
| Motion execution / recovery | Figure 9. Comparison of qualitative results on VG test set. namic fitting module could alleviate the model's semantic bias towards the common ... | p. 8 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 7. Ablation study of pseudo labeling on VG150 test set. Relation Generation. We conduct ablation experiments to evaluate the effectiveness of the relation language ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Experimental results of open-vocabulary scene graph generation of the SGDet task on VG. * denotes the method is tested under the OVSGTR's setting ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Effect of the learning weight of the generative relation language model. of text-image modalities, VLM can directly generate open- vocabulary relations for OV-SGG ...
- **p. 8 / 4.4. Qualitative Results - extractive PDF cue:** Specifically, without the full supervision of novel categories, our model can provide novel relationship predictions (e.g., "from" and ‘part of').

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Generative Relation Recognition), p. 5 (3.4. Training Objectives), p. 3 (3.1. OV-SGG Architecture), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method), p. 3 (3.1. OV-SGG Architecture), objective p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method), temporal p. 4 (3.2. Generative Relation Recognition), p. 2 (2. Related Work), p. 4 (3.2. Generative Relation Recognition), p. 5 (3.3. Hierarchical Relation Extension), p. 8 (4.4. Qualitative Results), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
