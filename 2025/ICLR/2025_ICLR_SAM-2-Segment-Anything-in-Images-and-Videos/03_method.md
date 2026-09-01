# Method - SAM 2: Segment Anything in Images and Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2408.00714; PDF retrieval source: https://arxiv.org/pdf/2408.00714. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 28 (Method), p. 27 (Method), p. 27 (Method), p. 28 (Method)): 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a mask in the first frame.

## Method Body Digest

- **p. 28 / Method - extractive PDF cue:** 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a mask in the ...
- **p. 27 / Method - extractive PDF cue:** The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts the average accuracy ...
- **p. 27 / Method - extractive PDF cue:** We compare SAM 2 to SAM and HQ-SAM with different model sizes in Table 15.
- **p. 28 / Method - extractive PDF cue:** Our model, however, is able to restrict the masklet to the target object.
- **p. 1 / 1 Introduction - extractive PDF cue:** The task takes as input points, boxes, or masks on any frame of the video to define a segment of interest for which the spatio-temporal ...
- **p. 1 / 1 Introduction - extractive PDF cue:** SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the ...
- **p. 27 / Method - extractive PDF cue:** For SAM 2, we use clicks as inputs following the click sampling strategy from CiVOS (Vujasinović et al., 2022).
- **p. 27 / Method - extractive PDF cue:** The results are shown in Table 14, where SAM 2 (based on click inputs) outperforms both baselines under click inputs.

## Design Rationale

- **p. 1 / 1 Introduction - extractive PDF cue:** We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video).
- **p. 2 / 1 Introduction - extractive PDF cue:** Our final Segment Anything Video (SA-V) dataset (§5.2) consists of 35.5M masks across 50.9K videos, 53× more masks than any existing video segmentation dataset.
- **p. 28 / Method - extractive PDF cue:** 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a mask in the ...

## Source Evidence Cues

- **p. 28 / Method - extractive PDF cue:** 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a mask in the ...
- **p. 27 / Method - extractive PDF cue:** The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts the average accuracy ...
- **p. 27 / Method - extractive PDF cue:** We compare SAM 2 to SAM and HQ-SAM with different model sizes in Table 15.
- **p. 28 / Method - extractive PDF cue:** Our model, however, is able to restrict the masklet to the target object.
- **Detected method headings:** A Data and model ablations (p. 12); A.2 Model architecture ablations (p. 13); A.2.3 Memory architecture ablations (p. 15); Method (p. 27)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a ... | p. 28 (Method), p. 27 (Method) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts ... | p. 27 (Method), p. 27 (Method) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | We compare SAM 2 to SAM and HQ-SAM with different model sizes in Table 15. | p. 27 (Method), p. 28 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | task, takes, input, points, boxes, masks, frame, video, define, segment, interest, spatio-temporal, mask, masklet | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | task, takes, input, points, boxes, masks, frame, video, define, segment | task state 또는 decision variable | body cue; notation verify |
| Action/output | introduce, Segment, Anything, Model, SAM, unified, video, image, segmentation, consider | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive PDF cue:** The task takes as input points, boxes, or masks on any frame of the video to define a segment of interest for which the spatio-temporal ...
- **p. 1 / 1 Introduction - extractive PDF cue:** SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the ...
- **p. 27 / Method - extractive PDF cue:** For SAM 2, we use clicks as inputs following the click sampling strategy from CiVOS (Vujasinović et al., 2022).
- **p. 27 / Method - extractive PDF cue:** The results are shown in Table 14, where SAM 2 (based on click inputs) outperforms both baselines under click inputs.
- **p. 28 / Method - extractive PDF cue:** G Details on comparison to state-of-the-art in semi-supervised VOS We provide additional details on the comparison to the previous state-of-the-art in semi-supervised VOS (§7).
- **p. 28 / Method - extractive PDF cue:** 15, where the per-dataset delta in 1-click mIoU relative to SAM is color-coded to indicate the data type (image or video).
- **p. 29 / Method - extractive PDF cue:** Datasets derived from video distribution are highlighted in red, while those from image distribution are highlighted in blue. ours baseline Figure 16 Comparison between our ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | We fine-tune for 50k iterations (1/3 of the original schedule) using half of the original learning rate and freeze the image encoder ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | Our model is a simple transformer architecture with streaming memory for real-time video processing. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | We fine-tune for 50k iterations (1/3 of the original schedule) using half of the original learning rate and freeze the image encoder ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | Cost and impact of compute The released SAM 2 was trained on 256 A100 GPUs for 108 hours. | hardware, batch and throughput |

## Training vs Inference

- **p. 27 / Method - extractive PDF cue:** The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts the average accuracy ...
- **p. 27 / Method - extractive PDF cue:** The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts the average accuracy ...
- **p. 28 / Method - extractive PDF cue:** We include results from SAM 2 trained only on SA-1B, SA-V and Internal data, for different encoder sizes.
- **p. 32 / dataset - extractive PDF cue:** Cost and impact of compute The released SAM 2 was trained on 256 A100 GPUs for 108 hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** comparison, between, baseline, Cutie-base, model, SAM, bottom, when, prompted, mask, first, frame, last, rows, Table, illustrate, benefits, training, image, video.
- **Relevant PDF headings:** A Data and model ablations (p. 12); A.2 Model architecture ablations (p. 13); A.2.3 Memory architecture ablations (p. 15); Method (p. 27).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | Sparse Validation videos on egocentric cameras 1185 1185 327,080 9,035 VIPSeg (Miao et al., 2022) VIPSeg Panoptic Large scale and real world ... | p. 30 (dataset), p. 32 (dataset) |
| Core objective / transformation | We report the performance of prior works as evaluated by the LVOSv2 authors. | p. 31 (dataset), p. 31 (dataset) |
| Downstream transfer boundary | We report the performance of prior works as evaluated by the LVOSv2 authors. | p. 31 (dataset), p. 32 (dataset) |

## Failure and Ablation Link

- **p. 21 / C Limitations - extractive PDF cue:** We leveraged our online model in the loop setup to enable this, requesting annotators to use SAM 2 interactively to identify failure modes and then ...
- **p. 18 / C Limitations - extractive PDF cue:** If the ground-truth does not contain a mask for a frame, we do not supervise any of the mask outputs (but always supervise the occlusion ...
- **p. 16 / C Limitations - extractive PDF cue:** The model may fail to segment objects across shot changes and can lose track of or confuse objects in crowded scenes, after long occlusions or ...
- **p. 17 / C Limitations - extractive PDF cue:** Our memory encoder does not use an additional image encoder and instead reuses the image embeddings produced by the Hiera encoder, which are fused with ...
- **p. 23 / C Limitations - extractive PDF cue:** 3We note that this estimation does not account for the model's tracking FPS.
- **p. 24 / C Limitations - extractive PDF cue:** If a dataset does not follow the standard VOS format, we preprocess it into a format similar to MOSE (Ding et al., 2023).
- **p. 32 / dataset - extractive PDF cue:** Caveats and recommendations See Appendix C for limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 28 (Method), p. 27 (Method), p. 27 (Method), p. 28 (Method), objective 본문 anchor 없음, temporal p. 18 (C Limitations), p. 1 (Front matter), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 27 (Method), p. 28 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
