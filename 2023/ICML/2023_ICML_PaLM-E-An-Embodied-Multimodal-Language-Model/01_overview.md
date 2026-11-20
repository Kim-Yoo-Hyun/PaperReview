# PaLM-E: An Embodied Multimodal Language Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2303.03378.
> PDF retrieval source: https://arxiv.org/pdf/2303.03378. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICML
- Authors: Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, Wenlong Huang, Yevgen Chebotar, Pierre Sermanet, Daniel Duckworth, Sergey Levine, Vincent Vanhoucke, Karol Hausman, Marc Toussaint, Klaus Greff, Andy Zeng, Igor Mordatch, Pete Florence
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: LLM, Vision-Language, Robotics
- Official paper: https://arxiv.org/abs/2303.03378
- Full-text retrieval: https://arxiv.org/pdf/2303.03378
- Code/Project: https://palm-e.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

PaLM-E는 영상·상태 등 연속 관측을 언어 모델 입력에 넣어 로봇 계획과 시각언어 과제에 쓸 텍스트를 생성한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large language models have been demonstrated to perform complex tasks.
- **p. 1 / Abstract - extractive body cue:** However, enabling general inference in the real world, e.g. for robotics problems, raises the challenge of grounding.
- **p. 1 / Abstract - extractive body cue:** We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
- **p. 1 / Abstract - extractive body cue:** Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings.
- **p. 1 / Abstract - extractive body cue:** We train these encodings end-to-end, in conjunction with a pretrained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, ...
- **p. 1 / 1. Introduction - extractive body cue:** However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may ...
- **p. 1 / 1. Introduction - extractive body cue:** Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typical vision-language tasks such as visual-question-answering (VQA) cannot directly solve robotic reasoning ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper we propose embodied language models, which ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate the approach in a variety of settings, comparing different input representations (e.g. standard vs. object-centric ViT encodings for visual input), freezing vs. finetuning ...
- **p. 3 / 1. Introduction - extractive body cue:** Finally, in addition to our focus on PaLM-E as an embodied reasoner we (4) show that PaLM-E is also a quantitatively competent vision and language ...
- **원문 대조:** 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes).
- **p. 5 / 5. Training Recipes - extractive body cue:** Despite being a decoder-only model, the text consists of a prefix part up to index ni that is formed from multi-modal sentences, and the prediction ...
- **p. 6 / 5. Training Recipes - extractive body cue:** In our experiments, we investigate the effects of co-training our models on a variety of diverse data.
- **p. 6 / 5. Training Recipes - extractive body cue:** PaLM-E: An Embodied Multimodal Language Model input encoders, and if so, how different-modality encoders compare.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a Transformer-based LLM in the same way as ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | Inputs, images, state, estimates, embedded, same, latent, embedding, language, tokens, processed, self-attention | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (5. Training Recipes) |
| Output/action | Previous work (Ahn et al., 2022) interfaces the output of LLMs with learned robotic policies and affordance functions to make decisions, but is limited in that the LLM itself is only provided ... | continuous action, pose 또는 action chunk | p. 1 (1. Introduction), p. 5 (5. Training Recipes), p. 2 (1. Introduction) |
| Objective/outcome | The loss function is therefore a crossentropy loss averaged over the individual non-prefix tokens wi ni+1:Li. | instruction following, task success, generalization과 latency | p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes) |

## Main Claims and Actual Contribution

- 연속 센서 표현을 언어 임베딩과 함께 처리한다.
- 로봇 과제와 일반 시각언어 과제를 함께 학습했을 때의 전이를 평가한다.

[저자 원문](https://proceedings.mlr.press/v202/driess23a.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks) |
| Embodiment/environment | 7, c) and to tasks involving objects that were unseen in either the original robot dataset or the finetuning datasets, e.g. a toy turtle (Fig. | hardware/simulator version and reset protocol | p. 7 (6.3. Language-Table Environment), p. 6 (6. Experiments) |
| Dataset/benchmark | 7, the input representations are trained on a dataset containing 96,000 training scenes of solely the TAMP environment, i.e. no other data is part of the mixture. | role, split, size and leakage | p. 7 (6.3. Language-Table Environment), p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 6 (6. Experiments) |
| Metric | 7 (appendix) shows planning success rates and VQA performance for the TAMP environment. | definition, denominator, direction and uncertainty | p. 6 (6.2. TAMP Environment), p. 7 (6.3. Language-Table Environment), p. 8 (6.4. Mobile Manipulation Environment) |
| Baseline/ablation | As baselines, we consider the state-of-the art visual language model PaLI (Chen et al., 2022), which has not been trained on embodiment robot data, as well as the SayCan algorithm (Ahn et ... | fair input/data/compute/action matching | p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 9 (6.5. Performance on General Visual-Language Tasks) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 6. Experiments - extractive body cue:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to ...
- **p. 7 / 6.4. Mobile Manipulation Environment - extractive body cue:** Put down the sponge." Inspired by these tasks, we develop 3 use cases to test the embodied reasoning abilities of PaLM-E: affordance prediction, failure detection, ...
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** For a robot to do closed-loop planning, it is also important to detect failures, as is shown in (Huang et al., 2022c).
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** This method has access to more information than our method, and was specifically designed to just solve failure detection on this dataset.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Mobile manipulation environment: failure detection and affordance prediction (F1 score). VQAv2 OK-VQA COCO
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Task prompts for Tab. 2. Baselines Failure det. Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022)
- **p. 18 / Figure/Table caption - extractive body cue:** Table 9: Mobile manipulation environment: failure detection, showing individual precision and recall scores.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 5 (5. Training Recipes)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations that relate ... (p. 1, 1. Introduction).
- **Actual contribution:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data into the training of a ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples for p1, p2 each) of ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence ... (p. 6, 6. Experiments).
