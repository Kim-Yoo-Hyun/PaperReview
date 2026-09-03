# Method - HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=H1KDMNOKQn; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245878. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT)): Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion generation within a unified token ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given these advantages and limitations, a question arises: "How can we elegantly construct a unified VLA model that integrates the strengths of both autoregressive and ...
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, a collaborative training recipe is proposed, incorporating diffusion denoising into the next-token prediction process and mitigating interference between the two generation paradigms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, we demonstrate that the autoregressive discrete action outputs of HybridVLA can be replaced with language-based task planning without compromising the stability of diffusion-based action ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Building on this success, several studies have extended VLMs into vision-language-action (VLA) models, enabling them to predict low-level action poses for robotic manipulation (Brohan et ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing intelligent robots capable of performing manipulation tasks demands robust policies (Driess et al., 2023; Huang et al., 2023).

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given these advantages and limitations, a question arises: "How can we elegantly construct a unified VLA model that integrates the strengths of both autoregressive and ...
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Given these advantages and limitations, a question arises: "How can we elegantly construct a unified VLA model that integrates the strengths of ... | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted ... | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, a collaborative training recipe is proposed, incorporating diffusion denoising into the next-token prediction process and mitigating interference between the two generation paradigms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 1 (ABSTRACT).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | central, objective, manipulation, policy, design, enable, robots, comprehend, human, instructions, predict, generalized, actions, unstructured | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | central, objective, manipulation, policy, design, enable, robots, comprehend, human, instructions | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, follows, HybridVLA, innovatively, leverages, single, LLM, backbone, iterative, action | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | contributions, follows, HybridVLA, innovatively, leverages, single, LLM, backbone, iterative, action | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, we demonstrate that the autoregressive discrete action outputs of HybridVLA can be replaced with language-based task planning without compromising the stability of diffusion-based action ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Building on this success, several studies have extended VLMs into vision-language-action (VLA) models, enabling them to predict low-level action poses for robotic manipulation (Brohan et ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | In addition to the acquired vision and language tokens, our framework also integrates the robot state, diffusion timestep, noisy actions, and the ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Note that all models are run with bfloat16 precision during inference, without employing action chunking. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Following the frame-sampling method used in previous works (Shridhar et al., 2022; Goyal et al., 2023; Jia et al., 2024), we construct ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 7 / 12.3 Hz - extractive body cue:** Our models are trained for 300 epochs on downstream tasks using mixed-precision.
- **p. 7 / 12.3 Hz - extractive body cue:** Note that all models are run with bfloat16 precision during inference, without employing action chunking.
- **p. 8 / 12.3 Hz - extractive body cue:** Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the diffusion-based ...
- **p. 9 / 12.3 Hz - extractive body cue:** For evaluation, we use the checkpoint from the latest epoch to perform 20 rollouts across diverse tabletop positions.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** contributions, follows, HybridVLA, innovatively, leverages, single, LLM, backbone, iterative, action, prediction, through, autoregressive, diffusion, generation, within, unified, token, sequence, harnessing.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | CAE indicates the collaborative action ensemble method, whereas LSP refers to large-scale pretraining on robotic datasets. | p. 8 (12.3 Hz), p. 8 (12.3 Hz) |
| Action / skill decoding | The results show that our method reduces the accuracy drop by approximately 5-16% compared to the baselines under generalization scenarios. | p. 10 (12.3 Hz), p. 7 (12.3 Hz) |
| Receding execution / feedback | As shown in Table 2, HybridVLA (7B) achieves an average success rate of 78% across 10 distinct tasks, outperforming the previous SOTA ... | p. 7 (12.3 Hz), p. 7 (12.3 Hz) |

## Failure and Ablation Link

- **p. 8 / 12.3 Hz - extractive body cue:** The above ablation studies corroborate our initial motivation that the two action-generation paradigms possess distinct advantages, and HybridVLA effectively integrates them during both training and ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 3: Respective strengths of diffusion-based and autoregressive action generation paradigms. We evaluate the performance of Our-ar and Our-dif across a variety of scenarios. actions ...
- **p. 7 / 12.3 Hz - extractive body cue:** 4.2 ABLATION STUDY The impact of each component.
- **p. 6 / 4 EXPERIMENT - extractive body cue:** The effectiveness of each component is validated in Section 4.2 and Appendix C.2.
- **p. 7 / 12.3 Hz - extractive body cue:** Note that all models are run with bfloat16 precision during inference, without employing action chunking.
- **p. 8 / 12.3 Hz - extractive body cue:** Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the diffusion-based ...
- **p. 9 / 12.3 Hz - extractive body cue:** Our method consistently outperforms previous VLA approaches across five distinct tasks, highlighting HybridVLA's ability to effectively leverage LLM's pretrained knowledge for dual-arm coordination in complex ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), objective p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), temporal p. 5 (2 RELATED WORK), p. 7 (12.3 Hz), p. 7 (12.3 Hz), p. 8 (12.3 Hz), p. 8 (12.3 Hz), p. 9 (12.3 Hz).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
