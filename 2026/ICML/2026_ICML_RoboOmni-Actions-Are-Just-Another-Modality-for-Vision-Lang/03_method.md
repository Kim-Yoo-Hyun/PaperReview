# Method - RoboOmni: Actions Are Just Another Modality for Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=qdXOfyGMuB; PDF retrieval source: https://openreview.net/pdf/b090562c668703f4568061335c66e0e592e16d9d.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.3. Training VLA as VLM), p. 5 (3.3. Training VLA as VLM)): Each state zk is then passed through a shared language model head (LMHead) to produce logits for the future action 3

## Method Body Digest

- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** Each state zk is then passed through a shared language model head (LMHead) to produce logits for the future action 3
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A).
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** Therefore, we employ MTAP primarily as an auxiliary training objective to facilitate backbone modeling of the complex frequency tokens, rather than solely for inference acceleration.
- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** By jointly optimizing for these diverse objectives alongside the primary action prediction task, the model learns more robust and generalizable representations.
- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** One of the core advantages of RoboOmni is its unified representation of action and all other modalities, which allows for the seamless integration of VLM ...
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** The loss function reflects this token-index-based objective: L = X j H-1 X k=0 LCE(LMHead(zj,k), y∗ j+k+1) (2) where zj,k is the k-th hidden state ...
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** By abstracting the prediction objective, MTAP serves as a unified solution capable of accommodating both of these distinct tokenizer archetypes.

## Design Rationale

- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.
- **p. 2 / 1. Introduction - extractive body cue:** This design enables long-context, multimodal co-training and allows the model to explicitly reason over historical observations and actions.
- **p. 1 / 1. Introduction - extractive body cue:** To overcome these limitations, we present RoboOmni, a 1

## Source Evidence Cues

- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** Each state zk is then passed through a shared language model head (LMHead) to produce logits for the future action 3
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A).
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** Therefore, we employ MTAP primarily as an auxiliary training objective to facilitate backbone modeling of the complex frequency tokens, rather than solely for inference acceleration.
- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** By jointly optimizing for these diverse objectives alongside the primary action prediction task, the model learns more robust and generalizable representations.
- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** One of the core advantages of RoboOmni is its unified representation of action and all other modalities, which allows for the seamless integration of VLM ...
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Each state zk is then passed through a shared language model head (LMHead) to produce logits for the future action 3 | p. 3 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified ... | p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A). | p. 4 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** By jointly optimizing for these diverse objectives alongside the primary action prediction task, the model learns more robust and generalizable representations.
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** The loss function reflects this token-index-based objective: L = X j H-1 X k=0 LCE(LMHead(zj,k), y∗ j+k+1) (2) where zj,k is the k-th hidden state ...
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** By abstracting the prediction objective, MTAP serves as a unified solution capable of accommodating both of these distinct tokenizer archetypes.
- **p. 5 / 3.2. Multi-Modal Action Co-Training - extractive body cue:** We incorporate VQAstyle objectives to preserve and enhance general image understanding, multimodal reasoning, and instructionfollowing.
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** For Bin tokenization, the raw action sequence is lossless but long.
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, processes, multi-modal, interleaved, input, sequences, comprising, visual, observations, text, instructions, robot, states, actions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | model, processes, multi-modal, interleaved, input, sequences, comprising, visual, observations, text | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | overcome, challenges, introduce, versatile, Multi-Token, Action, Prediction, MTAP, framework, enables | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | jointly, optimizing, diverse, objectives, alongside, primary, action, prediction, task, model | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A).
- **p. 5 / 3.2. Multi-Modal Action Co-Training - extractive body cue:** RoboOmni: Actions Are Just Another Modality for Vision-Language Models clude Visual inputs, Text inputs, Bounding Box and Pixel Point, as well as Robot State and ...
- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** RoboOmni preserves a standard VLM-style next-token prediction backbone, where each trajectory is represented as an interleaved sequence of past observations (ot-T :t), robot states (st-T ...
- **p. 2 / 1. Introduction - extractive body cue:** RoboOmni is approximately 27x faster than the unified approach OpenVLA and 6.6x faster than the decoupled approach RoboFlamingo. generalist robotic policy model that interleaves vision, ...
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** Each state zk is then passed through a shared language model head (LMHead) to produce logits for the future action 3
- **p. 1 / 1. Introduction - extractive body cue:** As a result, unified approaches often run with a single-step history and fail to fully utilize the rich information of past observations and actions.
- **p. 1 / 1. Introduction - extractive body cue:** Most VLAs apply VLMs as their feature extractors and feed representations into a decoupled continuous policy head, e.g., diffusion or flow policies (Team et al., ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Key distinctions include whether models utilize temporal history (Li et al., 2023) or operate on single frames (Intelligence et al., 2025), how ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | However, unified discrete frameworks lag behind decoupled continuous designs due to limitations in action chunking and temporal modeling. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Key distinctions include whether models utilize temporal history (Li et al., 2023) or operate on single frames (Intelligence et al., 2025), how ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | As shown in Figure 1, RoboOmni achieves an inference speed of 82.6 Hz with an action chunk size of 10 and a ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** Therefore, we employ MTAP primarily as an auxiliary training objective to facilitate backbone modeling of the complex frequency tokens, rather than solely for inference acceleration.
- **p. 5 / 3.3. Training VLA as VLM - extractive body cue:** One of the core advantages of RoboOmni is its unified representation of action and all other modalities, which allows for the seamless integration of VLM ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** By enabling parallel decoding over the action chunk, MTAP provides a near-linear speedup, slashing the inference time to just 12.1 7
- **p. 4 / 3.2. Multi-Modal Action Co-Training - extractive body cue:** To support multi-modal co-training, we build a unified tokenization scheme that encodes all modalities.
- **p. 7 / 4.2. Evaluation on SimplerEnv - extractive body cue:** Second, the model's dominance in the Visual Matching setting indicates exceptional robustness to sim-to-real visual shifts, suggesting that preserving the VLM's pre-trained visual representations enables ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** state, then, passed, through, shared, language, model, head, LMHead, produce, logits, future, action, overcome, challenges, introduce, versatile, Multi-Token, Prediction, MTAP.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We evaluate RoboOmni across three complementary settings: (1) long-horizon multi-task manipulation on the CALVIN benchmark, (2) Google Robot tasks in the SimplerEnv ... | p. 5 (4. Experiment), p. 6 (4.2. Evaluation on SimplerEnv) |
| Action / skill decoding | Figure 3. Comparison of success rates in the real-world setting. RoboOmni consistently outperforms baselines, including π0-FAST and RoboVLMs, particularly in the challenging ... | p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on SimplerEnv) |
| Receding execution / feedback | On average, RoboOmni achieves a 91% success rate, significantly surpassing π0-FAST (68%) and RoboVLMs (60%). | p. 7 (4.3. Real Robot Experiments), p. 7 (4.4. Ablation Study) |

## Failure and Ablation Link

- **p. 8 / 4.4. Ablation Study - extractive body cue:** Default Configuration RoboOmni(Bin) 0.997 0.940 0.834 4.64 Ablation on Window Size Window Size = 1 0.973 0.897 0.813 4.49 Window Size = 10 0.985 0.914 ...
- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** Notably, the FAST variant exhibits superior out-of-distribution generalization (ABC→D), suggesting the frequency-domain representation effectively offloads temporal modeling pressure from the backbone.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** We conduct a series of ablation studies to evaluate the contributions of key components in our framework on Calvin Benchmark.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ablation on Architectural and Training Components.
- **p. 5 / 4. Experiment - extractive body cue:** In our reproduction, the model is trained exclusively on manipulation data to align with the setting without VLM described in the original paper.
- **p. 5 / 4. Experiment - extractive body cue:** Across all settings, we compare RoboOmni against three representative and widely adopted unified VLA baselines: OpenVLA (Kim et al., 2024) is an autoregressive visionlanguage-action (VLA) ...
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** Ablation study of MTAP and different tokenizers.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.3. Training VLA as VLM), p. 5 (3.3. Training VLA as VLM), objective p. 5 (3.3. Training VLA as VLM), p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), temporal p. 2 (2.1. Vision-Language-Action Models), p. 1 (Abstract), p. 2 (1. Introduction), p. 6 (4.1. Evaluation on Calvin), p. 6 (4.1. Evaluation on Calvin), p. 7 (4.2. Evaluation on SimplerEnv).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
