# 3D Question Answering via only 2D Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=IkhJApkJQ3.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168051. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://openreview.net/forum?id=IkhJApkJQ3
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/168051
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, both approaches have significant limitations, either being inefficient or failing to capture critical views.를 문제로 두고, We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views based on their potential to provide answer-specific ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large vision-language models (LVLMs) have significantly advanced numerous fields.
- **p. 1 / Abstract - extractive body cue:** In this work, we explore how to harness their potential to address 3D scene understanding tasks, using 3D question answering (3D-QA) as a representative example.
- **p. 1 / Abstract - extractive body cue:** Due to the limited training data in 3D, we do not train LVLMs but infer in a zero-shot manner.
- **p. 1 / Abstract - extractive body cue:** Specifically, we sample 2D views from a 3D point cloud and feed them into 2D models to answer a given question.
- **p. 1 / Abstract - extractive body cue:** When the 2D model is chosen, e.g., LLAVA-OV, the quality of sampled views matters the most.
- **p. 2 / 1. Introduction - extractive body cue:** However, both approaches have significant limitations, either being inefficient or failing to capture critical views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views ...
- **p. 1 / 1. Introduction - extractive body cue:** All of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning. a4 is our method that leverages pre-trained LVLMs operating ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) We introduce cdViews that integrates a viewSelector with a viewNMS to capture critical and diverse views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D ...
- **p. 2 / 1. Introduction - extractive body cue:** To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into descriptive captions.
- **p. 6 / 3. Preliminaries - extractive body cue:** Views are classified as "uncertain" when the model chooses the option of "Uncertain, insufficient or unclear information" or outputs none of the given options, and ...
- **p. 2 / 1. Introduction - extractive body cue:** 2D features extracted from LVLMs are already well-aligned with language, but further alignment with 3D features requires careful model design and advanced training techniques.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes the question embedding Q and the visual embedding set {Vi}N i=1 as input and outputs a binary label ˆSi (0 or 1) for each visual embedding. | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3. Preliminaries), p. 3 (3. Preliminaries) |
| State/latent | takes, question, embedding, visual, input, outputs, binary, label, Since, LVLMs, fundamentally, designed | geometry, map, object/relationship state | p. 6 (3. Preliminaries), p. 3 (3. Preliminaries), p. 1 (1. Introduction) |
| Output/action | Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D scenes. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Preliminaries), p. 1 (1. Introduction), p. 4 (3. Preliminaries) |
| Objective/outcome | The mismatch loss is used to optimize the parameters of viewSelector. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3. Preliminaries), p. 6 (3. Preliminaries), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views ...
- **p. 1 / 1. Introduction - extractive body cue:** All of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning. a4 is our method that leverages pre-trained LVLMs operating ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) We introduce cdViews that integrates a viewSelector with a viewNMS to capture critical and diverse views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Performance comparison of view selection methods on the validation set of ScanQA (Azuma et al., 2022). It can be observed that: 1) performance ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). For ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Embodiment/environment | ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects). | hardware/simulator version and reset protocol | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Dataset/benchmark | ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects). | role, split, size and leakage | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Metric | Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). For ScanQA, scores are presented in the format ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (5. Experiments) |
| Baseline/ablation | Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In Step 1, LVLMs processes question-answer pairs to ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.1. Comparisons with the State-of-the-Arts - extractive body cue:** The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, both approaches have significant limitations, either being inefficient or failing to capture critical views.를 문제로 두고, We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views based on their potential to provide answer-specific ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Preliminaries), p. 5 (3. Preliminaries), p. 4 (3. Preliminaries), p. 2 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
