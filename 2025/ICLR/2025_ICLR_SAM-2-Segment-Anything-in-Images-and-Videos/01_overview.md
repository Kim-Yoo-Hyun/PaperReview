# SAM 2: Segment Anything in Images and Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2408.00714.
> PDF retrieval source: https://arxiv.org/pdf/2408.00714. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: segmentation, foundation model, prompting, video segmentation, memory
- Official paper: https://arxiv.org/abs/2408.00714
- Full-text retrieval: https://arxiv.org/pdf/2408.00714
- Code/Project: https://github.com/facebookresearch/sam2
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Further, efficient processing of a large number of frames is a key challenge.를 문제로 두고, We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Segment Anything (SA) introduced a foundation model for promptable segmentation in images (Kirillov et al., 2023).
- **p. 1 / 1 Introduction - extractive body cue:** However an image is only a static snapshot of the real world in which visual segments can exhibit complex motion, and with the rapid growth ...
- **p. 1 / 1 Introduction - extractive body cue:** Many important applications in AR/VR, robotics, autonomous vehicles, and video editing require temporal localization beyond image-level segmentation.
- **p. 1 / 1 Introduction - extractive body cue:** We believe a universal visual segmentation system should be applicable to both images and videos.
- **p. 1 / 1 Introduction - extractive body cue:** Segmentation in video aims to determine the spatio-temporal extent of entities, which presents unique challenges beyond those in images.
- **p. 1 / 1 Introduction - extractive body cue:** Further, efficient processing of a large number of frames is a key challenge.
- **p. 2 / 1 Introduction - extractive body cue:** Different from most existing video segmentation datasets, our data engine is not restricted to objects of specific categories, but instead targeted to provide training data ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video).
- **p. 2 / 1 Introduction - extractive body cue:** Our final Segment Anything Video (SA-V) dataset (§5.2) consists of 35.5M masks across 50.9K videos, 53× more masks than any existing video segmentation dataset.
- **p. 28 / Method - extractive body cue:** 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a mask in the ...
- **p. 1 / 1 Introduction - extractive body cue:** SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the ...
- **p. 27 / Method - extractive body cue:** The last two rows in Table 15 illustrate the benefits of training with our mix of image and video data, which boosts the average accuracy ...
- **p. 27 / Method - extractive body cue:** We compare SAM 2 to SAM and HQ-SAM with different model sizes in Table 15.
- **p. 28 / Method - extractive body cue:** Our model, however, is able to restrict the masklet to the target object.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The task takes as input points, boxes, or masks on any frame of the video to define a segment of interest for which the spatio-temporal mask (i.e., a ‘masklet') is to be ... | 논문이 명시한 observation과 task input | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | task, takes, input, points, boxes, masks, frame, video, define, segment, interest, spatio-temporal | task state 또는 decision variable | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 27 (Method) |
| Output/action | SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the video, and also effectively correct these based ... | paper-specific output/action | p. 1 (1 Introduction), p. 27 (Method), p. 27 (Method) |
| Objective/outcome | primary task objective와 closed-loop behavior | primary task objective와 closed-loop behavior | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video).
- **p. 2 / 1 Introduction - extractive body cue:** Our final Segment Anything Video (SA-V) dataset (§5.2) consists of 35.5M masks across 50.9K videos, 53× more masks than any existing video segmentation dataset.
- **p. 28 / Method - extractive body cue:** 16, we show a comparison between our baseline (Cutie-base+, top row) and our model (SAM 2, bottom row) when prompted with a mask in the ...
- **p. 1 / 1 Introduction - extractive body cue:** SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the ...
- **p. 31 / dataset - extractive body cue:** We report the performance of prior works as evaluated by the LVOSv2 authors.
- **p. 32 / dataset - extractive body cue:** Risks and harms In Section E.1.1 of the main text we analyze SAM 2 performance on people across demographic groups.
- **p. 32 / dataset - extractive body cue:** G: We use G for evaluation on YTVOS 2019 for the semi-supervised VOS task. mIoU: We evaluate performance using mIoU for the promptable image segmentation ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 31 (dataset), p. 32 (dataset) |
| Embodiment/environment | Sparse Validation videos on egocentric cameras 1185 1185 327,080 9,035 VIPSeg (Miao et al., 2022) VIPSeg Panoptic Large scale and real world scenarios for video panoptic segmentation Dense Validation 152 1,457 3,416 ... | hardware/simulator version and reset protocol | p. 30 (dataset), p. 32 (dataset) |
| Dataset/benchmark | Sparse All 12 12 4,012 412 LVOSv2 (Hong et al., 2024) LVOSv2 Long videos Long-term video object segmentation benchmark, on average 1.14 minutes Dense Validation 136 225 64,523 91,510 UVO (Wang et ... | role, split, size and leakage | p. 30 (dataset), p. 32 (dataset), p. 30 (dataset), p. 33 (dataset) |
| Metric | Sparse Validation 921 921 736,030 4,426 HT1080WT cells embedded in 3D collagen type I matrices (Gómez-de Mariscal et al., 2021) HT1080WT Microscopy; cells Timelapse videos of HT1080WT cell movement Sparse All 60 ... | definition, denominator, direction and uncertainty | p. 30 (dataset), p. 31 (dataset), p. 32 (dataset) |
| Baseline/ablation | We report the performance of prior works as evaluated by the LVOSv2 authors. | fair input/data/compute/action matching | p. 31 (dataset), p. 31 (dataset) |

## Explicit Limitations and Failure Boundary

- **p. 21 / C Limitations - extractive body cue:** We leveraged our online model in the loop setup to enable this, requesting annotators to use SAM 2 interactively to identify failure modes and then ...
- **p. 18 / C Limitations - extractive body cue:** If the ground-truth does not contain a mask for a frame, we do not supervise any of the mask outputs (but always supervise the occlusion ...
- **p. 16 / C Limitations - extractive body cue:** The model may fail to segment objects across shot changes and can lose track of or confuse objects in crowded scenes, after long occlusions or ...
- **p. 17 / C Limitations - extractive body cue:** Our memory encoder does not use an additional image encoder and instead reuses the image embeddings produced by the Hiera encoder, which are fused with ...
- **p. 23 / C Limitations - extractive body cue:** 3We note that this estimation does not account for the model's tracking FPS.
- **p. 24 / C Limitations - extractive body cue:** If a dataset does not follow the standard VOS format, we preprocess it into a format similar to MOSE (Ding et al., 2023).
- **p. 32 / dataset - extractive body cue:** Caveats and recommendations See Appendix C for limitations.

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Further, efficient processing of a large number of frames is a key challenge.를 문제로 두고, We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 28 (Method), p. 27 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
