# Method - AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Adaptive Segmentation-Text Modeling), p. 5 (3.4. Adaptive Segmentation-Text Modeling)): To better adapt the text encoder to 3D scenarios, we introduce a small number of learnable tokens TOKENS at the input and every transformer layer in the text encoder ftext(·).

## Method Body Digest

- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** To better adapt the text encoder to 3D scenarios, we introduce a small number of learnable tokens TOKENS at the input and every transformer layer ...
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** During inference, we use the trainable tokens and the category names as the input of the text encoder ftext(·) to generate the category embedding C ...
- **p. 5 / 3.5. Training Objective - extractive PDF cue:** The training objective of our proposed AIDE is a weighted linear combination of segmentation loss (Eq.
- **p. 5 / 3.5. Training Objective - extractive PDF cue:** (2)), confidence calibration loss (Eq.
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** Sequentially, for each transformer layer, trainable tokens are merged with the output of the previous layer as the input of the current layer, i.e., concat([TOKENSi, ...
- **p. 4 / 3.1. Problem Definition - extractive PDF cue:** To automatically find the most suitable prompt for adapting text encoders into 3D scenarios, AIDE extends prompt tuning [38] by incorporating learnable tokens in the ...
- **p. 4 / 3.1. Problem Definition - extractive PDF cue:** We first generate numerous captions using the temperature-based generation strategy, then sample captions based on their similarity to the images (CLIP-rewarded sampling), and finally align ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Due to the lack of large-scale 3D-image-text pairs, instead of training a 3D-language model from scratch, recent works [13, 23, 57] propose to transfer the ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To address these issues, we propose a novel AlIgned 3D Open-Vocabulary SEmantic Segmentation framework, called AIDE.
- **p. 2 / 1. Introduction - extractive PDF cue:** Then, to encourage rich associations between 3D and text, we propose the CLIP-rewarded sampling method, which samples captions based on their similarity to the 3D-scene ...
- **p. 4 / 3.1. Problem Definition - extractive PDF cue:** Our solution: To generate aligned data, we propose the CLIP-rewarded alignment module in Sec.

## Source Evidence Cues

- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** To better adapt the text encoder to 3D scenarios, we introduce a small number of learnable tokens TOKENS at the input and every transformer layer ...
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** During inference, we use the trainable tokens and the category names as the input of the text encoder ftext(·) to generate the category embedding C ...
- **Detected method headings:** 3.4. Adaptive Segmentation-Text Modeling (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To better adapt the text encoder to 3D scenarios, we introduce a small number of learnable tokens TOKENS at the input and ... | p. 5 (3.4. Adaptive Segmentation-Text Modeling), p. 5 (3.4. Adaptive Segmentation-Text Modeling) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | During inference, we use the trainable tokens and the category names as the input of the text encoder ftext(·) to generate the ... | p. 5 (3.4. Adaptive Segmentation-Text Modeling) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To better adapt the text encoder to 3D scenarios, we introduce a small number of learnable tokens TOKENS at the input and ... | p. 5 (3.4. Adaptive Segmentation-Text Modeling) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.5. Training Objective - extractive PDF cue:** The training objective of our proposed AIDE is a weighted linear combination of segmentation loss (Eq.
- **p. 5 / 3.5. Training Objective - extractive PDF cue:** (2)), confidence calibration loss (Eq.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.5. Training Objective), p. 5 (3.4. Adaptive Segmentation-Text Modeling).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Sequentially, transformer, layer, trainable, tokens, merged, output, previous, input, current, concat, TOKENSi, Ftext, where | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Sequentially, transformer, layer, trainable, tokens, merged, output, previous, input, current | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | address, issues, novel, AlIgned, Open-Vocabulary, SEmantic, Segmentation, framework, called, AIDE | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | training, objective, AIDE, weighted, linear, combination, segmentation, loss, confidence, calibration | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** Sequentially, for each transformer layer, trainable tokens are merged with the output of the previous layer as the input of the current layer, i.e., concat([TOKENSi, ...
- **p. 4 / 3.1. Problem Definition - extractive PDF cue:** To automatically find the most suitable prompt for adapting text encoders into 3D scenarios, AIDE extends prompt tuning [38] by incorporating learnable tokens in the ...
- **p. 4 / 3.1. Problem Definition - extractive PDF cue:** We first generate numerous captions using the temperature-based generation strategy, then sample captions based on their similarity to the images (CLIP-rewarded sampling), and finally align ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Due to the lack of large-scale 3D-image-text pairs, instead of training a 3D-language model from scratch, recent works [13, 23, 57] propose to transfer the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, to adapt text encoders for 3D semantics, the adaptive segmentation module extends beyond the popular visual prompt tuning methods [31, 38, 86] by incorporating ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The adaptive segmentation module adapts the text encoder by integrating learnable prompts across the input space and each layer of text encoder. • Extensive experiments ...
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** Specifically, at the input layer, we directly concatenate the trainable tokens with the text as the input of the text encoder.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | In this paper, to address these issues and improve generalization performance, we propose an AlIgned 3D Open-Vocabulary SEmantic Segmentation framework, called AIDE, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We notice that, as AIDE only introduces sets of trainable tokens to adapt the text encoder, the additional parameters and latency are ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** During inference, we use the trainable tokens and the category names as the input of the text encoder ftext(·) to generate the category embedding C ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Four trainable tokens are used in adapting text encoders.
- **p. 5 / 3.4. Adaptive Segmentation-Text Modeling - extractive PDF cue:** One possible solution is fine-tuning VLMs to handle 3D data for better alignment between text encoders of VLMs and 3D models.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** better, adapt, text, encoder, scenarios, introduce, small, number, learnable, tokens, input, every, transformer, layer, ftext, During, inference, trainable, category, names.
- **Relevant PDF headings:** 3.4. Adaptive Segmentation-Text Modeling (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To validate the effectiveness of AIDE, we conducted extensive experiments on three popular 3D benchmarks: ScanNet [20], S3DIS [2], and one outdoor ... | p. 5 (4. Experiments), p. 6 (4.2. Quantative Results) |
| Global / local decision | Compared to our baseline, PLA, AIDE improves hIoU by 7.6 and 4.0 for each split. | p. 6 (4.2. Quantative Results), p. 8 (4.4. Qualitative Results-Generalization) |
| Motion execution / recovery | Qualitative results of segmentation compared between baseline and AIDE. achieves significant improvements in all metrics, with hIoU, mIoUB, and mIoUN increasing from ... | p. 8 (4.4. Qualitative Results-Generalization), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 4.3. Ablation Studies - extractive PDF cue:** In this part, we present the ablation studies on the effects of two proposed modules (Tab.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 7. Ablation studies on using different text encoders of AIDE on ScanNet (B15/N4). this phenomenon. As generating over 30 captions per tem- perature will ...
- **p. 6 / 4.3. Ablation Studies - extractive PDF cue:** Due to the space limitation, ablation studies on the choice of temperatures (Tab.
- **p. 7 / 4.3. Ablation Studies - extractive PDF cue:** Ablation studies on different numbers of learnable tokens of AIDE on ScanNet (B15/N4). conduct a series of experiments as shown in Tab.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Previous methods use misaligned paired data (e.g., image/point cloud 1 is closest to text 2) and freeze the text encoder trained on 2D ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Due to space limitations, the details of benchmarks and partitions are deferred to Appendix C.1.
- **p. 6 / 4.3. Ablation Studies - extractive PDF cue:** Due to the space limitation, ablation studies on the choice of temperatures (Tab.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Adaptive Segmentation-Text Modeling), p. 5 (3.4. Adaptive Segmentation-Text Modeling), objective p. 5 (3.5. Training Objective), p. 5 (3.5. Training Objective), temporal p. 1 (Abstract), p. 8 (4.4. Qualitative Results-Generalization).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
