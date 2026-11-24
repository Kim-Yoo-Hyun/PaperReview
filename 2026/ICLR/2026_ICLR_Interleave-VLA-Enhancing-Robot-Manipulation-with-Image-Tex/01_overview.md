# Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/444876e32cba0408c63f5295481cfe20-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245105. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Cunxin Fan, Xiaosong Jia, Yihang Sun, Yixiao Wang, Jianglan Wei, Ziyang Gong, Xiangyu Zhao, Masayoshi Tomizuka, Xue Yang, Junchi Yan, Mingyu Ding
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Robotics, Reinforcement Learning
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/444876e32cba0408c63f5295481cfe20-Abstract-Conference.html
- PDF title variant: Interleave-VLA: Enhancing Robot Manipulation with Interleaved Image-Text Instructions [게재본 표제면](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=1)
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

Interleave-VLA는 문장에 대상의 참조 이미지를 끼워 넣은 지시를 받아 연속 로봇 행동을 생성한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=1) · [PDF 2쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=2)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** The rise of foundation models paves the way for generalist robot policies in the physical world.
- **p. 1 / ABSTRACT - extractive body cue:** Existing methods relying on text-only instructions often struggle to generalize to unseen scenarios.
- **p. 1 / ABSTRACT - extractive body cue:** We argue that interleaved image-text inputs offer richer and less biased context and enable robots to better handle unseen tasks with in-context visual grounding.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...
- **p. 1 / ABSTRACT - extractive body cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to bridge the gap of the lack of image-text interleaved datasets in robotic manipulation, we develop a pipeline to automatically construct interleaved instructions ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, current VLA models (Brohan et al., 2023; Kim et al., 2024; Black et al., 2024) remain predominantly trained on text-only instructions-a setting we refer ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The interleaved format enables robust zeroshot generalization to novel objects and user-provided sketches unseen during training.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** (1) We introduce Interleave-VLA: a lightweight, transferable paradigm that enhances the generalization capability of current text input VLA models with interleaved image-text instructions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This enables training Interleave-VLA with real-world interaction data and diverse visual instruction types.
- **p. 1 / ABSTRACT - extractive body cue:** Building on this insight, we introduce Interleave-VLA, a robot learning paradigm extending interleaved image-text instructions from digital world to directly generating continuous action sequences in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this limitation, we first build a high-quality interleaved image-text datasets, crucial for training multimodal models.
- **p. 1 / ABSTRACT - extractive body cue:** It offers a natural, flexible, and model-agnostic paradigm that extends state-of-the-art vision-language-action (VLA) models with minimal modifications while achieving strong zero-shot generalization.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We summarize our key takeaways below: • Generalization failures in VLAs often stem from attentional hallucinations, which we summarized as attentional bias, diffused attention, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To develop a general and practical robot policy capable of acting on interleaved image-text instructions in the real world, a straightforward solution is to build upon VLA (Kim et al., 2024; O'Neill ... | image/video, language instruction, proprioception과 history | p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |
| State/latent | develop, general, practical, robot, policy, capable, acting, interleaved, image-text, instructions, real, world | language-grounded task state와 action-policy context | p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 1 (ABSTRACT) |
| Output/action | (c) It enables flexible, zero-shot instruction following with cropped images, web photos, and hand-drawn sketches for practical and intuitive human-robot interaction. | continuous action, pose 또는 action chunk | p. 1 (Body text (section not recovered)), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Objective/outcome | As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, enabling existing VLAs to process interleaved inputs without ... | instruction following, task success, generalization과 latency | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- Open X-Embodiment의 텍스트 지시를 참조 이미지와 텍스트가 섞인 지시로 자동 변환해 기존 로봇 시연을 재사용했다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=3) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=6)
- 낯선 물체의 조작에서 텍스트만 제공한 정책과 비교하고, 사진 이외에 손그림처럼 훈련과 다른 형태의 지시도 시험했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS) |
| Embodiment/environment | Notably, although the pretraining dataset does not include FANUC robot arm data, it still enables strong cross-embodiment transfer to FANUC. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Dataset/benchmark | 4.2 REAL ROBOT COMPARISON Task setup. | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | Table 8: Performance across sketch styles. Success Rate and Intention Accuracy (in %) of Interleave-VLA when the target object is specified by sketches with different levels of clarity and ambiguity. subsequently corrects ... | definition, denominator, direction and uncertainty | p. 18 (Figure/Table caption), p. 18 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Baseline/ablation | In contrast, Interleave-VLA outperforms Text-VLA baselines by leveraging in-context visual grounding and cross-modality training to reduce attentional hallucinations. | fair input/data/compute/action matching | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** (2) What are the common failure modes of Text-VLA, and how does Interleave-VLA address them?
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For quantitative breakdown of failure modes, please refer to Figure 11.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** These failures can be attributed to semantic ambiguity in cluttered visual contexts and distributional bias in the training data.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For more styles of sketches and potential failure modes, please refer to Table 8 and 9 in Apppendix C.
- **p. 19 / Figure/Table caption - extractive body cue:** Table 9: Example sketches for each style. Yellow-cube and green-cube sketches representing each drawing style. The examples are sourced from multiple individuals and are designed ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Interleave-VLA data-pipeline failure analysis. We expand the evaluation to 400 exam- ples and quantify failures across the pipeline stages, from command parsing to ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)이다.
