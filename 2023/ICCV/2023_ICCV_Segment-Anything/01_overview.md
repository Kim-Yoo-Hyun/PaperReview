# Segment Anything

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.02643.
> PDF retrieval source: https://arxiv.org/pdf/2304.02643. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: segmentation, foundation model, prompting
- Official paper: https://arxiv.org/abs/2304.02643
- Full-text retrieval: https://arxiv.org/pdf/2304.02643
- Code/Project: https://github.com/facebookresearch/segment-anything
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 These "foundation models" [8] can generalize to tasks and data distributions beyond those seen during training.를 문제로 두고, We introduce each interconnected component next, followed by the dataset we created and the experiments that demonstrate the effectiveness of our approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation.
- **p. 1 / Abstract - extractive body cue:** Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on ...
- **p. 1 / Abstract - extractive body cue:** The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks.
- **p. 1 / Abstract - extractive body cue:** We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive - often competitive with or even superior to prior fully ...
- **p. 1 / 1. Introduction - extractive body cue:** Large language models pre-trained on web-scale datasets are revolutionizing NLP with strong zero-shot and few-shot generalization [10].
- **p. 1 / 1. Introduction - extractive body cue:** These "foundation models" [8] can generalize to tasks and data distributions beyond those seen during training.
- **p. 1 / 1. Introduction - extractive body cue:** Once trained, engineered text prompts enable zero-shot generalization to novel visual concepts and data distributions.

## Core Idea

- **p. 2 / 3. What data can power this task and model? - extractive body cue:** We introduce each interconnected component next, followed by the dataset we created and the experiments that demonstrate the effectiveness of our approach.
- **p. 1 / 1. Introduction - extractive body cue:** That is, we seek to develop a promptable model and pre-train it on a broad dataset using a task that enables powerful generalization.
- **p. 2 / 3. What data can power this task and model? - extractive body cue:** Inspired by this line of work, we propose the promptable segmentation task, where the goal is to return a valid segmentation mask given any segmentation ...
- **p. 5 / 3. Segment Anything Model - extractive body cue:** This runtime performance enables seamless, real-time interactive prompting of our model.
- **p. 1 / 1. Introduction - extractive body cue:** To develop them, we address the following questions about image segmentation:
- **p. 2 / 3. What data can power this task and model? - extractive body cue:** We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering.
- **p. 5 / 3. Segment Anything Model - extractive body cue:** Motivated by scalability and powerful pretraining methods, we use an MAE [47] pre-trained Vision Transformer (ViT) [33] minimally adapted to process high resolution inputs [62].
- **p. 2 / 3. What data can power this task and model? - extractive body cue:** Surprisingly, we find that a simple design satisfies all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The mask decoder efficiently maps the image embedding, prompt embeddings, and an output token to a mask. | 논문이 명시한 observation과 task input | p. 5 (3. Segment Anything Model), p. 5 (3. Segment Anything Model) |
| State/latent | mask, decoder, efficiently, maps, image, embedding, prompt, embeddings, output, token, After, running | task state 또는 decision variable | p. 5 (3. Segment Anything Model), p. 5 (3. Segment Anything Model), p. 2 (3. What data can power this task and model?) |
| Output/action | After running two blocks, we upsample the image embedding and an MLP maps the output token to a dynamic linear classifier, which then computes the mask foreground probability at each image location. | paper-specific output/action | p. 5 (3. Segment Anything Model), p. 2 (3. What data can power this task and model?), p. 2 (3. What data can power this task and model?) |
| Objective/outcome | The promptable segmentation task and the goal of real-world use impose constraints on the model architecture. | primary task objective와 closed-loop behavior | p. 2 (3. What data can power this task and model?), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model) |

## Main Claims and Actual Contribution

- **p. 2 / 3. What data can power this task and model? - extractive body cue:** We introduce each interconnected component next, followed by the dataset we created and the experiments that demonstrate the effectiveness of our approach.
- **p. 1 / 1. Introduction - extractive body cue:** That is, we seek to develop a promptable model and pre-train it on a broad dataset using a task that enables powerful generalization.
- **p. 2 / 3. What data can power this task and model? - extractive body cue:** Inspired by this line of work, we propose the promptable segmentation task, where the goal is to return a valid segmentation mask given any segmentation ...
- **p. 5 / 3. Segment Anything Model - extractive body cue:** This runtime performance enables seamless, real-time interactive prompting of our model.
- **p. 1 / 1. Introduction - extractive body cue:** To develop them, we address the following questions about image segmentation:
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** SAM significantly outperforms prior interactive segmenters with 1 point and is on par with more points.
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** We observe that the gap between SAM and the baselines grows and SAM is able to achieve comparable results under either sampling method.
- **p. 12 / 7.6. Ablations - extractive body cue:** (Left) Each data engine stage leads to improvements on our 23 dataset suite, and training with only the automatic data (our default) yields similar results ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation) |
| Embodiment/environment | 5 we plot the spatial distribution of object centers in SA-1B compared to the largest existing segmentation datasets. | hardware/simulator version and reset protocol | p. 7 (5. Segment Anything Dataset), p. 8 (7. Zero-Shot Transfer Experiments) |
| Dataset/benchmark | We compare SA-1B with existing datasets and analyze mask quality and properties. | role, split, size and leakage | p. 7 (5. Segment Anything Dataset), p. 8 (7. Zero-Shot Transfer Experiments), p. 6 (5. Segment Anything Dataset), p. 6 (5. Segment Anything Dataset) |
| Metric | SAM's mean ratings fall between 7 and 9, which corresponds to the qualitative rating guideline: "A high score (7-9): The object is identifiable and errors are small and rare (e.g., missing a ... | definition, denominator, direction and uncertainty | p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 5 (Figure/Table caption) |
| Baseline/ablation | We compare mainly to RITM [92], a strong interactive segmenter that performs best on our benchmark compared to other strong baselines [67, 18]. | fair input/data/compute/action matching | p. 8 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (7.1. Zero-Shot Single Point Valid Mask Evaluation), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 8. Discussion - extractive body cue:** It can miss fine structures, hallucinates small disconnected components at times, and does not produce boundaries as crisply as more computationally intensive methods that "zoom-in", ...
- **p. 9 / 7.1. Zero-Shot Single Point Valid Mask Evaluation - extractive body cue:** SAM's mean ratings fall between 7 and 9, which corresponds to the qualitative rating guideline: "A high score (7-9): The object is identifiable and errors ...
- **p. 11 / 7.5. Zero-Shot Text-to-Mask - extractive body cue:** When SAM fails to make a correct prediction, an additional point prompt can help.
- **p. 11 / 7.5. Zero-Shot Text-to-Mask - extractive body cue:** When SAM fails to pick the right object from a text prompt only, an additional point often fixes the prediction, similar to [31].
- **p. 12 / 8. Discussion - extractive body cue:** Our foray into the text-to-mask task is exploratory and not entirely robust, although we believe it can be improved with more effort.
- **p. 8 / 6. Segment Anything RAI Analysis - extractive body cue:** As MIAP does not contain perceived skin tone annotations, we use a proprietary dataset that contains annotations for the perceived Fitzpatrick skin type [36], which ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 16: Zero-shot instance segmentation on LVIS v1. SAM produces higher quality masks than ViTDet. As a zero-shot model, SAM does not have the opportunity ...

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 These "foundation models" [8] can generalize to tasks and data distributions beyond those seen during training.를 문제로 두고, We introduce each interconnected component next, followed by the dataset we created and the experiments that demonstrate the effectiveness of our approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model), p. 2 (3. What data can power this task and model?), p. 5 (3. Segment Anything Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
