# Insights — PaLM-E: An Embodied Multimodal Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.03378; PDF retrieval source: https://arxiv.org/pdf/2303.03378. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** In this paper we propose embodied language models, which ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate the approach in a variety of settings, comparing different input representations (e.g. standard vs. object-centric ViT encodings for visual input), freezing vs. finetuning ...
- **p. 3 / 1. Introduction - extractive body cue:** Finally, in addition to our focus on PaLM-E as an embodied reasoner we (4) show that PaLM-E is also a quantitatively competent vision and language ...
- **원문 대조:** 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes).
- **p. 5 / 5. Training Recipes - extractive body cue:** Despite being a decoder-only model, the text consists of a prefix part up to index ni that is formed from multi-modal sentences, and the prediction ...
- **p. 6 / 5. Training Recipes - extractive body cue:** In our experiments, we investigate the effects of co-training our models on a variety of diverse data.
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 5 (5. Training Recipes), p. 5 (5. Training Recipes)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may ...
- **p. 1 / 1. Introduction - extractive body cue:** Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typical vision-language tasks such as visual-question-answering (VQA) cannot directly solve robotic reasoning ...
- **p. 3 / 1. Introduction - extractive body cue:** We show that, (2) while current state-ofthe-art general-purpose visual-language models out-of-thebox (zero-shot) do not well address embodied reasoning problems, it is possible to train a ...
- **p. 2 / 1. Introduction - extractive body cue:** PaLM-E also generalizes, zero-shot, to multi-image prompts despite only being trained on single-image prompts.
- **p. 2 / 1. Introduction - extractive body cue:** We scale PaLM-E up to 562B parameters, integrating the 540B PaLM (Chowdhery et al., 2022) LLM and the 22B Vision Transformer (ViT) (Dehghani et al., ...
- **p. 6 / 6. Experiments - extractive body cue:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to ...
- **p. 7 / 6.4. Mobile Manipulation Environment - extractive body cue:** Put down the sponge." Inspired by these tasks, we develop 3 use cases to test the embodied reasoning abilities of PaLM-E: affordance prediction, failure detection, ...
- **Boundary to test:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence of external ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper we propose embodied language models, which | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples for p1, p2 each) of total training ... | p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks) |
| Failure/limitation | For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence of external ... | p. 6 (6. Experiments), p. 7 (6.4. Mobile Manipulation Environment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a Transformer-based LLM in the same ... (p. 2, 1. Introduction).
- **Paper-specific mechanism:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data into the training of a ... (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples for p1, p2 each) of ... (p. 8, Figure/Table caption); the relevant task/metric cue is 7 (appendix) shows planning success rates and VQA performance for the TAMP environment. (p. 6, 6.2. TAMP Environment). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence ... (p. 6, 6. Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- 현재 등급·주 트랙·태그는 [논문 개요](./01_overview.md)에서 확인한다.
- **Reading predecessor in the generated track queue:** CLIPort: What and Where Pathways for Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RT-1: Robotics Transformer for Real-World Control at Scale (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence of external ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a Transformer-based LLM in the same ... (p. 2, 1. Introduction); preserve the objective/update rule: When training PaLM-E, one way is to update the parameters of all these components. (p. 5, 5. Training Recipes).
2. Use the paper-reported task/data/environment cue: 1) include a Task and Motion Planning (TAMP) domain where a robot has to manipulate (grasp and stack) objects, a table-top pushing environment, and a mobile manipulation domain. (p. 6, 6. Experiments).
3. Compare against the reported or matched baseline: As baselines, we consider the state-of-the art visual language model PaLI (Chen et al., 2022), which has not been trained on embodiment robot data, as well as the SayCan algorithm ... (p. 6, 6. Experiments).
4. Report the body metric with its denominator and aggregation: 7 (appendix) shows planning success rates and VQA performance for the TAMP environment. (p. 6, 6.2. TAMP Environment).
5. Re-run the reported ablation or stress/failure condition: Furthermore, we show that a 62B LLM shows better out-of-distribution generalization compared to the 8B variant, while a non-pretrained LLM shows basically no outof-distribution generalization. (p. 7, 6.2. TAMP Environment); if none is reported, design one around: For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence ... (p. 6, 6. Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 1 (1. Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks), p. 8 (6.4. Mobile Manipulation Environment), and measure the boundary at p. 6 (6. Experiments), p. 7 (6.4. Mobile Manipulation Environment).

## Falsifiable research question

Under the paper's stated interface (Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention ...), does the paper-specific mechanism (To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing ...) retain the reported evaluation outcome (7 (appendix) shows planning success rates and VQA performance for the TAMP environment.) when tested against the paper's strongest explicit boundary (For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (7 (appendix) shows planning success rates and VQA performance for the TAMP environment.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data into the training of a ... (p. 2, 1. Introduction).
- **Paper-supported outcome:** Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples for p1, p2 each) of ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence ... (p. 6, 6. Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
