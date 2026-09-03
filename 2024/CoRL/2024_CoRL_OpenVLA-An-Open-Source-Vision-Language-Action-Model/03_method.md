# Method - OpenVLA: An Open-Source Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/kim25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction), p. 3 (1 Introduction)): OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot manipulation trajectories from the Open-X ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...
- **p. 3 / 1 Introduction - extractive body cue:** of compute efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 25] and model quantization [26] to facilitate adapting OpenVLA models on consumer-grade GPUs instead of large ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new ...
- **p. 2 / 1 Introduction - extractive body cue:** More recently, they have been used for directly learning visionlanguage-action models [VLAs; 1, 7, 17, 18] for control.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.
- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...
- **p. 3 / 1 Introduction - extractive body cue:** of compute efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 25] and model quantization [26] to facilitate adapting OpenVLA models on consumer-grade GPUs instead of large ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation ... | p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update PDF body cue not selected; no claim inferred - inspect equations and algorithm boxes
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | OpenVLA, Grip, Multi-Robot, Control, Efficient, Fine-Tuning, Large-Scale, Robot, Training, Data, Fully, Weights, Code, Open-Source | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | OpenVLA, Grip, Multi-Robot, Control, Efficient, Fine-Tuning, Large-Scale, Robot, Training, Data | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | introduce, OpenVLA, B-parameter, open-source, VLA, establishes, state, generalist, robot, manipulation | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | not stated or recoverable in the selected PDF body | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new ...
- **p. 2 / 1 Introduction - extractive body cue:** More recently, they have been used for directly learning visionlanguage-action models [VLAs; 1, 7, 17, 18] for control.
- **p. 2 / 1 Introduction - extractive body cue:** VLAs provide a direct instantiation of using pretrained vision-and-language foundation models for robotics, directly fine-tuning visuallyconditioned language models (VLMs) such as PaLI [19, 20] to ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We also compare to Diffusion Policy (matched), a version of Diffusion Policy that matches the input and output specifications of OpenVLA (i.e., ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For narrower but highly dexterous tasks, Diffusion Policy still shows smoother and more precise trajectories; incorporating action chunking and temporal smoothing, as ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | We also compare to Diffusion Policy (matched), a version of Diffusion Policy that matches the input and output specifications of OpenVLA (i.e., ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Mean success ± StdErr computed across 99 and 30 rollouts per approach for Franka-Tabletop and Franka-DROID, respectively. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** OpenVLA consists of a pretrained visuallyconditioned language model backbone that captures visual features at multiple granularities, fine-tuned on a large, diverse dataset of 970k robot ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** OpenVLA: [ x, , Grip] = … Δ Δθ Δ Multi-Robot Control & Efficient Fine-Tuning Large-Scale Robot Training Data Fully Data Weights Code Open-Source Figure ...
- **p. 3 / 1 Introduction - extractive body cue:** As a final contribution, we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale, with the hope that ...
- **p. 3 / 1 Introduction - extractive body cue:** of compute efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 25] and model quantization [26] to facilitate adapting OpenVLA models on consumer-grade GPUs instead of large ...
- **p. 8 / 7.0 GB - extractive body cue:** 4-bit inference achieves higher throughput due to reduced GPU memory transfer and thus recovers performance of the original bfloat16 model, while requiring less than half ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** OpenVLA, consists, pretrained, visuallyconditioned, language, model, backbone, captures, visual, features, multiple, granularities, fine-tuned, large, diverse, dataset, robot, manipulation, trajectories, Open-X.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Qualitatively, both RT-2-X and OpenVLA exhibit markedly more robust behaviors than the other tested models, such as approaching the correct object when ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Action / skill decoding | (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation ... | p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Receding execution / feedback | Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a ... | p. 6 (Figure/Table caption), p. 25 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 31 / Figure/Table caption - extractive body cue:** Table 9: BridgeData V2 WidowX ablation experiment results. We evaluate various methods on a subset of 8 representative tasks to assess the importance of different ...
- **p. 7 / 4 Experiments - extractive body cue:** Finally, as an ablation, we compare to OpenVLA (scratch), which omits OpenX pretraining and directly fine-tunes our base Prismatic VLM on the target robot setup.
- **p. 7 / 4 Experiments - extractive body cue:** See Appendix F for ablation analyses of these components.
- **p. 5 / 4 Experiments - extractive body cue:** (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches?
- **p. 8 / 7.0 GB - extractive body cue:** We test various parameter-efficient fine-tuning approaches for OpenVLA2 across multiple FrankaTabletop tasks in Table 1: last layer only fine-tunes only the last layer of OpenVLA's ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 11: OpenVLA inference speed for various GPUs. Both bfloat16 and int4 quantization achieve high throughput, especially on GPUs with Ada Lovelace architecture (RTX 4090, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We present OpenVLA, a 7B-parameter open-source vision-language-action model (VLA), trained on 970k robot episodes from the Open X-Embodiment dataset [1]. OpenVLA sets a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction), p. 3 (1 Introduction), objective 본문 anchor 없음, temporal p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (7.0 GB).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (35 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Abstract: Large policies pretrained on a combination of Internet-scale visionlanguage data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new ... (p. 1, Body text (section boundary not confidently recovered)).
- **Objective/update evidence:** OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. (p. 1, Body text (section boundary not confidently recovered)).
- **Temporal/runtime evidence:** We also compare to Diffusion Policy (matched), a version of Diffusion Policy that matches the input and output specifications of OpenVLA (i.e., no history, no action chunking). (p. 7, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
