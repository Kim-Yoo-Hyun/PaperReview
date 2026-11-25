# Problem - PaLM-E: An Embodied Multimodal Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.03378; PDF retrieval source: https://arxiv.org/pdf/2303.03378. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations that relate ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large language models have been demonstrated to perform complex tasks.
- **p. 1 / Abstract - extractive body cue:** However, enabling general inference in the real world, e.g. for robotics problems, raises the challenge of grounding.
- **p. 1 / Abstract - extractive body cue:** We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
- **p. 1 / Abstract - extractive body cue:** Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings.
- **p. 1 / Abstract - extractive body cue:** We train these encodings end-to-end, in conjunction with a pretrained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, ...
- **p. 1 / 1. Introduction - extractive body cue:** However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may ...
- **p. 1 / 1. Introduction - extractive body cue:** Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typical vision-language tasks such as visual-question-answering (VQA) cannot directly solve robotic reasoning ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Inputs, images, state, estimates, embedded, same, latent, embedding, language, tokens | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | base, PaLM-E, pretrained, parameter, variants, PaLM, decoder-only, LLM | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Inputs, images, state, estimates, embedded, same, latent, embedding, language, tokens | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (5. Training Recipes) |
| Decision / output variable | action, pose, option or chunk a; body terms: embodied, language, models, arXiv, Mar, summarize, main, contributions | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: loss, function, therefore, crossentropy, averaged, over, individual, non-prefix | p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes) |
| Success / guarantee | instruction-conditioned task success | p. 6 (6.2. TAMP Environment), p. 7 (6.3. Language-Table Environment), p. 8 (6.4. Mobile Manipulation Environment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typical vision-language tasks such as visual-question-answering (VQA) cannot directly solve robotic reasoning ...
- **p. 3 / 1. Introduction - extractive body cue:** We show that, (2) while current state-ofthe-art general-purpose visual-language models out-of-thebox (zero-shot) do not well address embodied reasoning problems, it is possible to train a ...
- **p. 2 / 1. Introduction - extractive body cue:** PaLM-E also generalizes, zero-shot, to multi-image prompts despite only being trained on single-image prompts.
- **p. 2 / 1. Introduction - extractive body cue:** We scale PaLM-E up to 562B parameters, integrating the 540B PaLM (Chowdhery et al., 2022) LLM and the 22B Vision Transformer (ViT) (Dehghani et al., ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 5 (5. Training Recipes)): In this paper we propose embodied language models, which ...

- **p. 2 / 1. Introduction - extractive body cue:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate the approach in a variety of settings, comparing different input representations (e.g. standard vs. object-centric ViT encodings for visual input), freezing vs. finetuning ...
- **p. 3 / 1. Introduction - extractive body cue:** Finally, in addition to our focus on PaLM-E as an embodied reasoner we (4) show that PaLM-E is also a quantitatively competent vision and language ...
- **원문 대조:** 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Put down the sponge." Inspired by these tasks, we develop 3 use cases to test the embodied reasoning ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | For a robot to do closed-loop planning, it is also important to detect failures, as is shown in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This method has access to more information than our method, and was specifically designed to just solve failure ... | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (5. Training Recipes), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (5. Training Recipes), p. 2 (1. Introduction), objective p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations that relate ... (p. 1, 1. Introduction).
- **Formulation-changing contribution:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data into the training of a ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence ... (p. 6, 6. Experiments).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
