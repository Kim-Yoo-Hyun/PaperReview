# Method - MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2511.09516v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 5 (III. METHODOLOGY)): Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an overview image I1 t, a ...

## Method Body Digest

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** To identify meaningful task stage boundaries, we first select a well-performed demonstration as reference and extract its key poses that mark salient transitions such as ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Instead, we use it as an action prior to guide the dynamic weighting between Abase t and Amem t .
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** To encode the stage-specific memory, we optimize Vk by aligning the model's predicted action tokens with expert actions using the flow matching loss: V∗ k ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** (7) This prompt ensemble mechanism encourages the policy to favor the action prediction that is closer to the retrieved expert action, effectively leveraging the future-action ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Using the computed αt, the final memory-augmented action for execution is given by: AMemAug t = αtAmem t + (1 -αt)Abase t .
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Then, we select the reference index j∗and trajectory i∗minimizing the distance: i∗, j∗= arg min i,j Ci,j.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Furthermore, to ensure stage consistency across demonstrations of the same task, we employ the Dynamic Time Warping (DTW) algorithm [24], a technique that non-linearly aligns ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** The main contributions of this work can be summarized as follows: • We propose MAP-VLA, a novel framework that augments a pre-trained VLA model with ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We also develop MemoryAugmented Action Generation (MAAG), which enables memory retrieval and dynamic memory-aware prompt ensembling to augment action generation during realtime task execution. • ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this paper, we present the Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), bridging the gap in current VLA models by enabling dynamic access to demonstration-derived ...

## Source Evidence Cues

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** To identify meaningful task stage boundaries, we first select a well-performed demonstration as reference and extract its key poses that mark salient transitions such as ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Instead, we use it as an action prior to guide the dynamic weighting between Abase t and Amem t .
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** To encode the stage-specific memory, we optimize Vk by aligning the model's predicted action tokens with expert actions using the flow matching loss: V∗ k ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** (7) This prompt ensemble mechanism encourages the policy to favor the action prediction that is closer to the retrieved expert action, effectively leveraging the future-action ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** Using the computed αt, the final memory-augmented action for execution is given by: AMemAug t = αtAmem t + (1 -αt)Abase t .
- **Detected method headings:** III. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, ... | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To identify meaningful task stage boundaries, we first select a well-performed demonstration as reference and extract its key poses that mark salient ... | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Instead, we use it as an action prior to guide the dynamic weighting between Abase t and Amem t . | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** To encode the stage-specific memory, we optimize Vk by aligning the model's predicted action tokens with expert actions using the flow matching loss: V∗ k ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Then, we select the reference index j∗and trajectory i∗minimizing the distance: i∗, j∗= arg min i,j Ci,j.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Furthermore, to ensure stage consistency across demonstrations of the same task, we employ the Dynamic Time Warping (DTW) algorithm [24], a technique that non-linearly aligns ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The learning objective can be summarized as follows: Lτ(θ) = Ep(At/ot), q(Aτ t /At) ∥fθ(Aτ t , ot) -u(Aτ t /At)∥2 , (1) where τ ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** (7) This prompt ensemble mechanism encourages the policy to favor the action prediction that is closer to the retrieved expert action, effectively leveraging the future-action ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | demonstration, consists, sequence, observation-action, pairs, where, observation, includes, overview, image, wrist, language, token, robot | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | demonstration, consists, sequence, observation-action, pairs, where, observation, includes, overview, image | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, MAP-VLA, novel, framework, augments, pre-trained, VLA | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | encode, stage-specific, memory, optimize, aligning, model, predicted, action, tokens, expert | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Each demonstration consists of a sequence of observation-action pairs {ot, at}n t=1, where each observation ot = [I1 t, I2 t, ℓt, st] includes an ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** VLA models acquire broad knowledge about the world from vision-language pre-training and learn to map raw visual observations and natural language instructions directly to robot ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** At each timestep t, the observation ot is processed by the image and language encoders to generate a base prompt with m base token embeddings ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** VLA models are policies pre-trained on large-scale demonstrations to map multi-modal observations to robot actions.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Once a VLA model is trained, it relies solely on immediate sensory inputs to decide the subsequent actions.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We also develop MemoryAugmented Action Generation (MAAG), which enables memory retrieval and dynamic memory-aware prompt ensembling to augment action generation during realtime task execution. • ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Conversely, the base prompt, derived solely from current observations and task instructions, is not affected by such errors but lacks historical grounding and long-horizon memory.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The online execution loop then proceeds with (a) observing, (b) retrieving memory, (c) executing dual forward passes, and (d) prompt ensembling via ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To overcome this, we introduce a memory-augmented framework that enhances VLA models for better long-horizon task performance. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | The online execution loop then proceeds with (a) observing, (b) retrieving memory, (c) executing dual forward passes, and (d) prompt ensembling via ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | All real-world computations are conducted on a system with an NVIDIA RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** demonstration, consists, sequence, observation-action, pairs, where, observation, includes, overview, image, wrist, language, token, robot, state, identify, meaningful, task, stage, boundaries.
- **Relevant PDF headings:** III. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | To validate the real-world effectiveness of MAP-VLA, we conduct evaluations on a physical robotic platform and compare its performance with the strongest ... | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Action / skill decoding | As summarized in Table II, MAPVLA again outperforms the baseline policy. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Receding execution / feedback | On average, MAP-VLA achieves an 83.4% success rate, whereas the baseline OpenVLA and π0 achieve 54.0% and 76.4%, respectively. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Overall, MAP-VLA achieves an average relative gain of 9.6%, slightly above the 9.2% relative gain without visual variations.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We first follow [4] to fine-tune the π0 model on the finetuning dataset using LoRA [25] on a server with 6 NVIDIA RTX 6000 Ada ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1. Simplified execution pipeline of existing VLA methods and MAP-VLA. specific memory prompts and the generalized base prompts. This whole framework, shown in Fig. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 6. Performance comparison with visual variations on LIBERO-Long. TABLE III ABLATION STUDY ON LIBERO-LONG. Metric Base VLA Universal Prompt Task Prompt
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** However, the memoryless baseline policy π0 exhibits inconsistent and ambiguous object alignment behavior, especially during critical pick-and-place phases (as circled in the figure), often leading ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** By dynamically balancing the task-level generalization of the base prompt with the stage-specificity of the retrieved prompt, the model maintains robustness to retrieval inaccuracies, improves ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** This reduced variability suggests improved robustness and reliability, as a result of encoding additional contextual memory into the prompt and dynamic prompt ensembling as we ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), objective p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), temporal p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 1 (Abstract), p. 4 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
