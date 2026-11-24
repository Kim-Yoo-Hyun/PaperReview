# Visual Instruction Tuning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2304.08485.
> PDF retrieval source: https://arxiv.org/pdf/2304.08485. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / NeurIPS
- Authors: Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision-Language Model, LLM, instruction tuning
- Official paper: https://arxiv.org/abs/2304.08485
- Full-text retrieval: https://arxiv.org/pdf/2304.08485
- Code/Project: https://github.com/haotian-liu/LLaVA
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

LLaVA는 이미지 설명과 상자 정보를 바탕으로 만든 시각 지시 데이터를 사용해 비전 인코더와 언어모형을 연결한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Instruction tuning large language models (LLMs) using machine-generated instruction-following data has been shown to improve zero-shot capabilities on new tasks, but the idea is less ...
- **p. 1 / Abstract - extractive body cue:** We present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data.
- **p. 1 / Abstract - extractive body cue:** By instruction tuning on such generated data, we introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision ...
- **p. 1 / Abstract - extractive body cue:** To facilitate future research on visual instruction following, we construct two evaluation benchmarks with diverse and challenging application-oriented tasks.
- **p. 1 / Abstract - extractive body cue:** Our experiments show that LLaVA demonstrates impressive multimodal chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative ...
- **p. 2 / 1 Introduction - extractive body cue:** One key challenge is the lack of vision-language instruction-following data.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We present LLaVA-Bench with two challenging benchmarks, with a diverse selection of paired images, instructions and detailed annotations. • Open-source.
- **p. 2 / 1 Introduction - extractive body cue:** We present a data reformation perspective and pipeline to convert image-text pairs into an appropriate instruction-following format, using ChatGPT/GPT-4. • Large multimodal models.
- **p. 1 / 1 Introduction - extractive body cue:** For example, the recent success of ChatGPT [35] and GPT-4 [36] have demonstrated the power of aligned LLMs in following human instructions, and have stimulated ...
- **p. 1 / 1 Introduction - extractive body cue:** One of the core aspirations in artificial intelligence is to develop a general-purpose assistant that can effectively follow multi-modal vision-and-language instructions, aligned with human intent ...
- **p. 9 / Method - extractive body cue:** Our novel model ensembling with the text-only GPT-4 consistently improves the model's performance under all categories, setting the new SoTA performance. this is the first ...
- **p. 9 / Method - extractive body cue:** Visual features Before Last Best variant 90.92 89.96 (-0.96) Predict answer first - 89.77 (-1.15) Training from scratch 85.81 (-5.11) - 7B model size 89.84 ...
- **p. 9 / Method - extractive body cue:** To decide the order between the answer and reasoning process in the model prediction, we run both variants and observe that answer-first reports the best ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this paper, we present visual instruction-tuning, the first attempt to extend instruction-tuning to the language-image multimodal space, to pave the way towards building a general-purpose visual assistant. | 논문이 명시한 observation과 task input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | present, visual, instruction-tuning, first, attempt, extend, language-image, multimodal, space, pave, towards, building | task state 또는 decision variable | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | One of the core aspirations in artificial intelligence is to develop a general-purpose assistant that can effectively follow multi-modal vision-and-language instructions, aligned with human intent to complete various real-world tasks in ... | paper-specific output/action | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | primary task objective와 closed-loop behavior | primary task objective와 closed-loop behavior | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 텍스트만 받는 GPT-4에 이미지의 기호화된 설명을 제시해 대화·상세 설명·추론 예시를 만든다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf#page=4)
- 먼저 투영층을 학습해 시각 특징을 언어 임베딩에 맞춘 뒤 시각 지시 데이터로 응답 생성을 미세조정한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf#page=5)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Embodiment/environment | The benchmark dataset is split into training, validation, and test splits with 12726, 4241, and 4241 examples, respectively. | hardware/simulator version and reset protocol | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | We assess the performance of LLaVA in instruction-following and visual reasoning capabilities with two primary experimental settings: multimodal chatbot and the ScienceQA dataset, respectively. | role, split, size and leakage | p. 8 (5 Experiments), p. 7 (5 Experiments), p. 5 (5 Experiments), p. 5 (5 Experiments) |
| Metric | It evaluates the helpfulness, relevance, accuracy, and level of detail of the responses from the assistants, and gives an overall score on a scale of 1 to 10, where a higher score ... | definition, denominator, direction and uncertainty | p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Baseline/ablation | Compared to BLIP-2 [28] and OpenFlamingo [5], LLaVA accurately follows the user's instructions, instead of simply describing the scene. | fair input/data/compute/action matching | p. 6 (5 Experiments), p. 7 (5 Experiments), p. 7 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 Experiments - extractive body cue:** We also observed an interesting failure of LLaVA, as it responds with yes when asked if strawberry-flavored yogurt is present, even though the fridge contains ...
- **p. 6 / 5 Experiments - extractive body cue:** Additionally, it is not clear how the man is able to maintain balance and stability while ironing clothes in such an unstable environment.
- **p. 8 / 5 Experiments - extractive body cue:** Whenever GPT-4 fails to provide answers, we use the prediction from our method.
- **p. 8 / 5 Experiments - extractive body cue:** For a substantial number of questions, we note that GPT-4 fails simply because it reports that there is insufficient context such as images or plots.
- **p. 7 / 5 Experiments - extractive body cue:** We hope LLaVA serves as a solid baseline on the benchmarks, on which our findings can inspire future work in developing more capable LMMs.
- **p. 6 / 5 Experiments - extractive body cue:** The scene depicted in the image is peculiar as it involves a makeshift ironing setup on a vehicle, which can be both unsafe and unconventional.
- **p. 15 / Figure/Table caption - extractive body cue:** Table 9: Example prompt comparing LLaVA, GPT-4, BLIP-2, and OpenFlamingo's visual reasoning capabilities in understanding the humor. BLIP-2 and OpenFlamingo fail to follow the user's ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 9 (Method), p. 8 (5 Experiments), p. 7 (5 Experiments)이다.
