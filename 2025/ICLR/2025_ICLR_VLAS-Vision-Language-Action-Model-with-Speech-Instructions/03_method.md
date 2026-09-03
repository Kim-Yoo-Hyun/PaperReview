# Method - VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4FAFNRpko; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/112658. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHOD), p. 3 (3 METHOD)): 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.

## Method Body Digest

- **p. 3 / 3 METHOD - extractive body cue:** 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.
- **p. 3 / 3 METHOD - extractive body cue:** As illustrated in Figure 2, we first provide an overview of the VLAS architecture (Section 3.1).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** VLAs, such as RT-2 (Brohan et al., 2023), which are fine-tuned from foundation VLMs like PaLM-E (Driess et al., 2023) using robotic trajectory data, can ...
- **p. 3 / 3 METHOD - extractive body cue:** The input image and speech instruction represented by frequency 3
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally, we further fine-tune VLAS-Base through behavior cloning (Ross et al., 2011) on our curated CSI dataset, which encompasses image observations, speech instructions, and robot ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Given these practical needs and existing technologies, a key question arises: How can we integrate visionlanguage-action models with speech modality to produce a simpler and ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Based on the above analysis, we propose guiding a robot's behavior through speech rather than text.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.

## Source Evidence Cues

- **p. 3 / 3 METHOD - extractive body cue:** 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.
- **p. 3 / 3 METHOD - extractive body cue:** As illustrated in Figure 2, we first provide an overview of the VLAS architecture (Section 3.1).
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot ... | p. 3 (3 METHOD), p. 3 (3 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | As illustrated in Figure 2, we first provide an overview of the VLAS architecture (Section 3.1). | p. 3 (3 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot ... | p. 3 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | ARCHITECTURE, VLAS, Overall, Framework, takes, human, speech, instructions, visual, observations, input, directly, generate, robot | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | ARCHITECTURE, VLAS, Overall, Framework, takes, human, speech, instructions, visual, observations | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, listed, follows, VLAS, first, vision-language-action, model, integrates, speech | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | not recovered | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHOD - extractive body cue:** 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** VLAs, such as RT-2 (Brohan et al., 2023), which are fine-tuned from foundation VLMs like PaLM-E (Driess et al., 2023) using robotic trajectory data, can ...
- **p. 3 / 3 METHOD - extractive body cue:** The input image and speech instruction represented by frequency 3
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally, we further fine-tune VLAS-Base through behavior cloning (Ross et al., 2011) on our curated CSI dataset, which encompasses image observations, speech instructions, and robot ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Given these practical needs and existing technologies, a key question arises: How can we integrate visionlanguage-action models with speech modality to produce a simpler and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For simplicity, the two images at each time step are concatenated together. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The input image and speech instruction represented by frequency 3 | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 1. I have a blue - extractive body cue:** Throughout this phase, all network components are updated, with the exception of the pre-trained image and speech encoders.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ARCHITECTURE, VLAS, Overall, Framework, takes, human, speech, instructions, visual, observations, input, directly, generate, robot, actions, illustrated, Figure, first, provide, overview.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 4.3 EXPERIMENTS WITH A REAL-WORLD UR5 ROBOT ARM We fine-tune our VLAS-Base by utilizing both the Berkeley UR5 demonstration dataset and our ... | p. 8 (1. I have a blue), p. 8 (1. I have a blue) |
| Action / skill decoding | Moreover, our VLAS is compared for speech modality input with the baseline VLA model and another powerful VLA model, Roboflamingo, both similarly ... | p. 7 (1. I have a blue), p. 7 (1. I have a blue) |
| Receding execution / feedback | Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to ... | p. 10 (Figure/Table caption), p. 8 (1. I have a blue) |

## Failure and Ablation Link

- **p. 8 / 1. I have a blue - extractive body cue:** Both of the ablation studies above demonstrate the effectiveness of the Voice RAG module.
- **p. 8 / 1. I have a blue - extractive body cue:** Ablation studies are conducted to further validate the effectiveness of our proposed Voice RAG module.
- **p. 7 / 1. I have a blue - extractive body cue:** We trained a traditional VLA model with the same configurations by directly fine-tuning the LLaVA backbone, without support for speech instructions, as the baseline.
- **p. 7 / 1. I have a blue - extractive body cue:** Finally, in Section 4.4, to verify whether our foundation model for robot manipulation truly understands speech instructions without compromising LLaVA's original performance, we evaluate VLAS-Base ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 5: Comparison with RoboFlamingo on the CALVIN Benchmark. The performance of RoboFlamingo without historical information is derived from results presented in their original pa- ...
- **p. 6 / 1. I have a blue - extractive body cue:** Stage I: Speech Alignment, where the model aligns speech with text through MLP fine-tuning.
- **p. 6 / 1. I have a blue - extractive body cue:** Throughout this phase, all network components are updated, with the exception of the pre-trained image and speech encoders.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 METHOD), p. 3 (3 METHOD), objective 본문 anchor 없음, temporal p. 7 (1. I have a blue), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 7 (1. I have a blue), p. 1 (ABSTRACT), p. 4 (1. I have a blue).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
