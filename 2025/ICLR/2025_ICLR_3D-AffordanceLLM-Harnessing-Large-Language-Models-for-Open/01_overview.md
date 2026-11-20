# 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/b364c8cbb3f229f40d5873e877391bd2-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114156. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Hengshuo Chu, Xiang Deng, Qi Lv, Xiaoyang Chen, Yinchuan Li, Jianye HAO, Liqiang Nie
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Reinforcement Learning, semantic
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/b364c8cbb3f229f40d5873e877391bd2-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

문제 관련 발췌 — The IRAS task is designed to output an affordance mask region in response to complex, reasoning-based query text, overcoming the limitations of fixed affordance labels and the difficulty of understanding complex instructions.

방법 관련 발췌 — By reforming the label-based semantic segmentation task in the traditional affordance detection paradigm into a natural language-driven reasoning affordance segmentation task, our model enables more flexible and context-aware reasoning, ...

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** 3D Affordance detection is a challenging problem with broad applications on various robotic tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Existing methods typically formulate the detection paradigm as a label-based semantic segmentation task.
- **p. 1 / ABSTRACT - extractive body cue:** This paradigm relies on predefined labels and lacks the ability to comprehend complex natural language, resulting in limited generalization in open-world scene.
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we reformulate the traditional affordance detection paradigm into Instruction Reasoning Affordance Segmentation (IRAS) task.
- **p. 1 / ABSTRACT - extractive body cue:** This task is designed to output a affordance mask region given a query reasoning text, which avoids fixed categories of input labels.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The IRAS task is designed to output an affordance mask region in response to complex, reasoning-based query text, overcoming the limitations of fixed affordance labels ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, current affordance detection methods also heavily rely on the predefined labels and lack the ability to understand and reason over long contextual text.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** By reforming the label-based semantic segmentation task in the traditional affordance detection paradigm into a natural language-driven reasoning affordance segmentation task, our model enables more ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we introduce an additional token, <AFF>, into the original LLM vocabulary.
- **p. 3 / 3 METHOD - extractive body cue:** To address these limitations, we introduce a new paradigm formulated as an Instruction Reasoning Affordance Segmentation (IRAS) task as depicted in Fig.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework, 3D AffordanceLLM, as illustrated in Fig.
- **p. 4 / 3 METHOD - extractive body cue:** To harness this capability for 3D affordance perception, we introduce the 3D AffordanceLLM Model, aiming to improve affordance detection in previously unseen contexts.
- **p. 4 / 3 METHOD - extractive body cue:** 2, our 3D AffordanceLLM consists of the following modules: a pre-trained point cloud encoder fpe,a projector fproj, a point backbone fPB, an affordance decoder fAFD ...
- **p. 4 / 3 METHOD - extractive body cue:** 2, primarily consists of two main components: (1) a point cloud multimodal model which is trained to accept point cloud and text inputs and generate ...
- **p. 5 / 3 METHOD - extractive body cue:** Building on the success of learnable query-based methods in object segmentation, we introduce an Affordance Decoder Module (AFD) that leverages a set of learnable output ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given a complex reasoning instruction query Qaff and a point cloud input Pcloud, we feed them into the multimodal point clouds LLM F3D-ADLLM, which outputs a text response ˆytxt: "Sure, it is ... | image/video, language instruction, proprioception과 history | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| State/latent | Given, complex, reasoning, instruction, query, Qaff, point, cloud, input, Pcloud, feed, them | language-grounded task state와 action-policy context | p. 5 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Output/action | Given the input point cloud and query reasoning instruction, the point cloud multimodal model is trained with lora to predict special token <AFF>. | continuous action, pose 또는 action chunk | p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD) |
| Objective/outcome | The overall objective L is the weighted sum of these losses, determined by λtxt and λmask: L = λtxtLtxt + λmaskLmask. | instruction following, task success, generalization과 latency | p. 7 (3 METHOD), p. 7 (3 METHOD), p. 6 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** By reforming the label-based semantic segmentation task in the traditional affordance detection paradigm into a natural language-driven reasoning affordance segmentation task, our model enables more ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we introduce an additional token, <AFF>, into the original LLM vocabulary.
- **p. 3 / 3 METHOD - extractive body cue:** To address these limitations, we introduce a new paradigm formulated as an Instruction Reasoning Affordance Segmentation (IRAS) task as depicted in Fig.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework, 3D AffordanceLLM, as illustrated in Fig.
- **p. 4 / 3 METHOD - extractive body cue:** To harness this capability for 3D affordance perception, we introduce the 3D AffordanceLLM Model, aiming to improve affordance detection in previously unseen contexts.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** Notably, 3D AffordanceLLM significantly outperforms the runner-up model (LASO) in terms of mIoU, with improvements of 8.02% and 7.19% on the full and partial view ...
- **p. 10 / 4 EXPERIMENT - extractive body cue:** 4 (g), our model significantly outperforms other models.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** As is shown in Table 3, our approach achieved the best zero-shot performance on this ood data.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENT), p. 10 (4 EXPERIMENT) |
| Embodiment/environment | 3.3, our training data is made up of two types of task data: (1) Referring Object Part Segmentation Dataset: we build this dataset on PartNet (Mo et al., 2019), which contains 573,585 ... | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Dataset/benchmark | Compared to existing datasets, this new dataset includes different types of affordances as well as unique affordance-object pairs, such as (twist, faucet), (lever, faucet), (press, dispenser), etc. | role, split, size and leakage | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Metric | The specific evaluation metrics over all instances: mIoUi (mean IoU over all instance data), mAcci (mean accuracy of points over all instance data), mPreci (mean precision of points over all instance data), ... | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Baseline/ablation | Detailed baseline model explanation for experiments can be found in Appendix Sect. | fair input/data/compute/action matching | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 EXPERIMENT - extractive body cue:** 4.2.2 OUT-OF-DISTRIBUTION RESULTS The test in out-of-distribution (ood) datasets is essential to assess the generalization capability of the model.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Notably, the most substantial performance degradation with about 6% occurs in mIoU when the PC module is removed.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD)이다.
