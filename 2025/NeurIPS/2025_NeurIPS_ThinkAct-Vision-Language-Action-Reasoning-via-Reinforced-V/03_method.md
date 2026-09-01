# Method - ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72UR53jN7T; PDF retrieval source: https://openreview.net/pdf/b35b0fc70612e191baced400f754db8ff1fae711.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 3 (3 Method)): Specifically, we build upon a Transformer-based action model πϕ (e.g., Diffusion Policy [9]), which predicts actions based on the current state composed of visual observations and language instructions.

## Method Body Digest

- **p. 5 / 3 Method - extractive PDF cue:** Specifically, we build upon a Transformer-based action model πϕ (e.g., Diffusion Policy [9]), which predicts actions based on the current state composed of visual observations ...
- **p. 5 / 3 Method - extractive PDF cue:** Thus, we solely update the state encoder, latent projector, and action model by imitation learning with annotated action demonstrations: LIL(ϕ) = E(oi,l,ai) [ℓ(πϕ(ct, oi, l), ...
- **p. 4 / 3 Method - extractive PDF cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...
- **p. 3 / 3 Method - extractive PDF cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM Fθ to reason the high-level plans while connecting with ...
- **p. 4 / 3 Method - extractive PDF cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 3 / 3 Method - extractive PDF cue:** This reasoned plan ct then guides the downstream action module πϕ to sequentially predict N executable actions [at]t+N t tailored to the target environment (Sec.
- **p. 4 / 3 Method - extractive PDF cue:** Thus, we optimize Fθ by maximizing the following objective: JGRPO(θ) = 1 M M X i=1 ( Fθ(zi/ot, l) Fθold(zi/ot, l)Ai -βDKL(Fθ(zi/ot, l) ∥Fθold(zi/ot, l))), ...
- **p. 5 / 3 Method - extractive PDF cue:** 3 that combines the QA-style reward with the format reward, and then optimize using GRPO.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visual-grounded embodied reasoning connected by ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose ThinkAct, which aims to enable MLLMs with the capability to reason before acting in physical environments.
- **p. 3 / 3 Method - extractive PDF cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM Fθ to reason the high-level plans while connecting with ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive PDF cue:** Specifically, we build upon a Transformer-based action model πϕ (e.g., Diffusion Policy [9]), which predicts actions based on the current state composed of visual observations ...
- **p. 5 / 3 Method - extractive PDF cue:** Thus, we solely update the state encoder, latent projector, and action model by imitation learning with annotated action demonstrations: LIL(ϕ) = E(oi,l,ai) [ℓ(πϕ(ct, oi, l), ...
- **p. 4 / 3 Method - extractive PDF cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...
- **p. 3 / 3 Method - extractive PDF cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM Fθ to reason the high-level plans while connecting with ...
- **p. 4 / 3 Method - extractive PDF cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 3 / 3 Method - extractive PDF cue:** This reasoned plan ct then guides the downstream action module πϕ to sequentially predict N executable actions [at]t+N t tailored to the target environment (Sec.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Specifically, we build upon a Transformer-based action model πϕ (e.g., Diffusion Policy [9]), which predicts actions based on the current state composed ... | p. 5 (3 Method), p. 5 (3 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Thus, we solely update the state encoder, latent projector, and action model by imitation learning with annotated action demonstrations: LIL(ϕ) = E(oi,l,ai) ... | p. 5 (3 Method), p. 4 (3 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual ... | p. 4 (3 Method), p. 3 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive PDF cue:** Thus, we optimize Fθ by maximizing the following objective: JGRPO(θ) = 1 M M X i=1 ( Fθ(zi/ot, l) Fθold(zi/ot, l)Ai -βDKL(Fθ(zi/ot, l) ∥Fθold(zi/ot, l))), ...
- **p. 4 / 3 Method - extractive PDF cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...
- **p. 5 / 3 Method - extractive PDF cue:** 3 that combines the QA-style reward with the format reward, and then optimize using GRPO.
- **p. 3 / 3 Method - extractive PDF cue:** Reward Shaping from Action-Aligned Visual Feedback To tackle this challenge, we design a novel action-aligned visual feedback that captures long-horizon goals and encourages visual 3
- **p. 3 / 3 Method - extractive PDF cue:** A straightforward way is to have the MLLM reason before generating low-level actions, while using the resulting task success rate in target environments (e.g., LIBERO ...
- **p. 5 / 3 Method - extractive PDF cue:** Once we obtain the QA reward rQA, we use the same approach as in Eq.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, build, upon, Transformer-based, action, model, Diffusion, Policy, predicts, actions, current, state, composed, visual | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Specifically, build, upon, Transformer-based, action, model, Diffusion, Policy, predicts, actions | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, ThinkAct, dual-system, framework, mutually, enhances, action | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Thus, optimize, maximizing, following, objective, JGRPO, zi/ot, DKL, then, picked | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive PDF cue:** Specifically, we build upon a Transformer-based action model πϕ (e.g., Diffusion Policy [9]), which predicts actions based on the current state composed of visual observations ...
- **p. 3 / 3 Method - extractive PDF cue:** At each timestep t, the model receives a visual observation ot and a textual instruction l, with the goal of predicting an action at, which ...
- **p. 4 / 3 Method - extractive PDF cue:** (a) Given observation ot and instruction l, ThinkAct advances action-aligned rewards derived from visual trajectory τ to incentivize embodied reasoning capability of Reasoning MLLM Fθ.
- **p. 5 / 3 Method - extractive PDF cue:** At inference time, given a visual observation ot and instruction l, ThinkAct produces a visual plan latent ct = Fθ(ot, l), which conditions the action ...
- **p. 4 / 3 Method - extractive PDF cue:** The overall reward is thus defined as the combination of our proposed action-aligned visual feedback and the format correctness score rformat following existing reasoning works ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Reinforcement Reasoning Action-Aligned Visual Feedback "Put the strawberry in the drawer." GRPO >> >> Let's start by analyzing the image and the task at hand. ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visual-grounded embodied reasoning connected by ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 2(a), given an observation ot at timestep t and a task instruction l, the MLLM Fθ autoregressively generates a sequence of latent ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Once the reinforced fine-tuning is complete, we are able to produce long CoT steps, while abstracting the textual reasoning into a compact ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4 Experiment - extractive PDF cue:** For reasoning-enhanced action adaptation, we connect the visual plan ct via a Q-Former [18] as the latent projector with 32 queries and fine-tune on 100K ...
- **p. 6 / 4 Experiment - extractive PDF cue:** LIBERO [24] tasks are further fine-tuned for 75K iterations with batch size 128.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, build, upon, Transformer-based, action, model, Diffusion, Policy, predicts, actions, current, state, composed, visual, observations, language, instructions, Thus, solely, update.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the ... | p. 7 (4 Experiment), p. 6 (4 Experiment) |
| Action / skill decoding | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA [54], verifying the ... | p. 6 (4 Experiment), p. 6 (4 Experiment) |
| Receding execution / feedback | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA [54], verifying the ... | p. 6 (4 Experiment), p. 9 (4 Experiment) |

## Failure and Ablation Link

- **p. 8 / 4 Experiment - extractive PDF cue:** Finally, the SFT cold-start model without RL yields the lowest scores, verifying the effectiveness of our RL fine-tuning for eliciting the reasoning capability in MLLMs.
- **p. 8 / 4 Experiment - extractive PDF cue:** When both rtraj and rgoal are removed, leaving only QA-style reward from QA datasets, the model shows only marginal improvements over the SFT baseline, confirming ...
- **p. 6 / 4 Experiment - extractive PDF cue:** SimplerEnv [20] includes Google-VM (Visual Matching), Google-VA (Variant Aggregation), and Bridge-VM setups, introducing variations in color, material, lighting, and camera pose to evaluate model robustness.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative ablation study for our proposed RL rewards in ThinkAct on SimplerEnv, EgoPlan- Bench2, and RoboVQA benchmarks.
- **p. 6 / 4 Experiment - extractive PDF cue:** LIBERO [24] tasks are further fine-tuned for 75K iterations with batch size 128.
- **p. 7 / 4 Experiment - extractive PDF cue:** Note that, Qwen2.5-VL* indicates fine-tuning the original Qwen2.5-VL using EgoPlan-IT [7] and RoboVQA [38] datasets.
- **p. 9 / 4 Experiment - extractive PDF cue:** We use 10 demonstrations per task for fine-tuning.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 3 (3 Method), objective p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method), temporal p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
