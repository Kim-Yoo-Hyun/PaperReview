# Method - PaLM-E: An Embodied Multimodal Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.03378; PDF retrieval source: https://arxiv.org/pdf/2303.03378. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes), p. 6 (5. Training Recipes)): Despite being a decoder-only model, the text consists of a prefix part up to index ni that is formed from multi-modal sentences, and the prediction target, which only contains text ...

## Method Body Digest

- **p. 5 / 5. Training Recipes - extractive body cue:** Despite being a decoder-only model, the text consists of a prefix part up to index ni that is formed from multi-modal sentences, and the prediction ...
- **원문 대조:** 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes).
- **p. 6 / 5. Training Recipes - extractive body cue:** In our experiments, we investigate the effects of co-training our models on a variety of diverse data.
- **p. 6 / 5. Training Recipes - extractive body cue:** PaLM-E: An Embodied Multimodal Language Model input encoders, and if so, how different-modality encoders compare.
- **p. 5 / 5. Training Recipes - extractive body cue:** The loss function is therefore a crossentropy loss averaged over the individual non-prefix tokens wi ni+1:Li.
- **p. 5 / 5. Training Recipes - extractive body cue:** When training PaLM-E, one way is to update the parameters of all these components.
- **p. 6 / 5. Training Recipes - extractive body cue:** In experiments with φOSRT, we also freeze the slot representation, i.e. we only update the small projector ψ which serves as the interface between OSRT ...
- **p. 2 / 1. Introduction - extractive body cue:** Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** In this paper we propose embodied language models, which ...
- **p. 2 / 1. Introduction - extractive body cue:** To summarize our main contributions, we (1) propose and demonstrate that a generalist, transfer-learned, multiembodiment decision-making agent can be trained via mixing in embodied data ...
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate the approach in a variety of settings, comparing different input representations (e.g. standard vs. object-centric ViT encodings for visual input), freezing vs. finetuning ...

## Source Evidence Cues

- **p. 5 / 5. Training Recipes - extractive body cue:** Despite being a decoder-only model, the text consists of a prefix part up to index ni that is formed from multi-modal sentences, and the prediction ...
- **원문 대조:** 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes).
- **p. 6 / 5. Training Recipes - extractive body cue:** In our experiments, we investigate the effects of co-training our models on a variety of diverse data.
- **p. 6 / 5. Training Recipes - extractive body cue:** PaLM-E: An Embodied Multimodal Language Model input encoders, and if so, how different-modality encoders compare.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Despite being a decoder-only model, the text consists of a prefix part up to index ni that is formed from multi-modal sentences, ... | p. 5 (5. Training Recipes), p. 5 (5. Training Recipes) |
| Language-target training | Multimodal prefix 뒤 text를 예측 | Continuous observations, text, prefix index | Non-prefix token cross-entropy | Text target; 이 문단은 continuous robot-action decoder의 근거가 아님 | 원문 대조: 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes) | [PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In our experiments, we investigate the effects of co-training our models on a variety of diverse data. | p. 6 (5. Training Recipes), p. 6 (5. Training Recipes) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 5. Training Recipes - extractive body cue:** The loss function is therefore a crossentropy loss averaged over the individual non-prefix tokens wi ni+1:Li.
- **p. 5 / 5. Training Recipes - extractive body cue:** When training PaLM-E, one way is to update the parameters of all these components.
- **p. 6 / 5. Training Recipes - extractive body cue:** In experiments with φOSRT, we also freeze the slot representation, i.e. we only update the small projector ψ which serves as the interface between OSRT ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inputs, images, state, estimates, embedded, same, latent, embedding, language, tokens, processed, self-attention, layers, Transformer-based | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Inputs, images, state, estimates, embedded, same, latent, embedding, language, tokens | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | embodied, language, models, arXiv, Mar, summarize, main, contributions, demonstrate, generalist | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | loss, function, therefore, crossentropy, averaged, over, individual, non-prefix, tokens, When | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a ...
- **p. 1 / 1. Introduction - extractive body cue:** Previous work (Ahn et al., 2022) interfaces the output of LLMs with learned robotic policies and affordance functions to make decisions, but is limited in ...
- **p. 5 / 5. Training Recipes - extractive body cue:** We base PaLM-E on the pretrained 8B, 62B, and 540B parameter variants of PaLM as the decoder-only LLM into which we inject the continuous observations ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, the model can perform, zero-shot, question and answering on temporally-annotated egocentric vision, similar to what was shown in (Zeng et al., 2022) but ...
- **p. 3 / 1. Introduction - extractive body cue:** We show that, (2) while current state-ofthe-art general-purpose visual-language models out-of-thebox (zero-shot) do not well address embodied reasoning problems, it is possible to train a ...
- **p. 1 / 1. Introduction - extractive body cue:** Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typical vision-language tasks such as visual-question-answering (VQA) cannot directly solve robotic reasoning ...
- **p. 6 / 5. Training Recipes - extractive body cue:** PaLM-E: An Embodied Multimodal Language Model input encoders, and if so, how different-modality encoders compare.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Given the observed image and a long-horizon goal, e.g. "sort the blocks by colors into corners", PaLM-E outputs language subgoals at 1 ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The prompt structure for this task is Human: <instruction> Robot: <step history>. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | The prompt structure for this task is Human: <instruction> Robot: <step history>. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Given the observed image and a long-horizon goal, e.g. "sort the blocks by colors into corners", PaLM-E outputs language subgoals at 1 ... | hardware, batch and throughput |

## Training vs Inference

- **원문 대조:** 각 학습 예시는 연속 관측들, text sequence, prefix 경계 index로 구성된다. Multimodal prefix 뒤의 text target에 대해 non-prefix token cross-entropy를 평균하며, 연속 관측의 encoder 출력은 prefix의 지정 위치에 삽입한다. ([PDF p. 5](https://arxiv.org/pdf/2303.03378#page=5), §5 Training Recipes).
- **p. 6 / 5. Training Recipes - extractive body cue:** In our experiments, we investigate the effects of co-training our models on a variety of diverse data.
- **p. 5 / 5. Training Recipes - extractive body cue:** Those encoders are either pre-trained or trained from scratch, see Sec.
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** PaLM-E is trained to generate the next step of the plan, conditioned on the history of taken steps and the current image observation of the ...

## Method-Specific Formal Details

- **Body-defined terms:** Despite, being, decoder-only, model, text, consists, prefix, part, index, formed, multi-modal, sentences, prediction, target, only, contains, tokens, PaLM-E, trained, dataset.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 7, c) and to tasks involving objects that were unseen in either the original robot dataset or the finetuning datasets, e.g. a ... | p. 7 (6.3. Language-Table Environment), p. 6 (6. Experiments) |
| Action / skill decoding | As baselines, we consider the state-of-the art visual language model PaLI (Chen et al., 2022), which has not been trained on embodiment ... | p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment) |
| Receding execution / feedback | Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% ... | p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks) |

## Failure and Ablation Link

- **p. 7 / 6.3. Language-Table Environment - extractive body cue:** 0% LLM finetune (full mixture) LLM finetune (single robot) without pretraining LLM frozen (full mixture) LLM frozen (single robot) 20% 40% 60% 80% 100% 94.9% ...
- **p. 7 / 6.2. TAMP Environment - extractive body cue:** Furthermore, we show that a 62B LLM shows better out-of-distribution generalization compared to the 8B variant, while a non-pretrained LLM shows basically no outof-distribution generalization.
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** The non-object centric ViT-4B variant utilizes color to reference objects, hence q1 cannot be evaluated here.
- **p. 9 / 6.5. Performance on General Visual-Language Tasks - extractive body cue:** Q: How to push all the blocks that are on the {left/right} side together, without bringing over any of the blocks that are on the ...
- **p. 9 / 6.5. Performance on General Visual-Language Tasks - extractive body cue:** Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022) 0.65 - CLIP-FT-hindsight (Xiao et al., 2022) 0.89 - QT-OPT (Kalashnikov ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of transfer learning demonstrated by PaLM- E: across three different robotics domains, using PaLM and ViT pretraining together with the full mixture ...
- **p. 6 / 6. Experiments - extractive body cue:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes), p. 6 (5. Training Recipes), objective p. 5 (5. Training Recipes), p. 5 (5. Training Recipes), p. 6 (5. Training Recipes), temporal p. 7 (6.3. Language-Table Environment), p. 8 (6.4. Mobile Manipulation Environment), p. 8 (6.4. Mobile Manipulation Environment), p. 6 (6. Experiments), p. 6 (6. Experiments), p. 7 (6.3. Language-Table Environment).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a Transformer-based LLM in the same ... (p. 2, 1. Introduction).
- **Objective/update evidence:** When training PaLM-E, one way is to update the parameters of all these components. (p. 5, 5. Training Recipes).
- **Temporal/runtime evidence:** Given the observed image and a long-horizon goal, e.g. "sort the blocks by colors into corners", PaLM-E outputs language subgoals at 1 Hz to the policies from Lynch et al. (p. 7, 6.3. Language-Table Environment).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
