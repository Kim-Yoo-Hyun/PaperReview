# Method - ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=72UR53jN7T; PDF retrieval source: https://arxiv.org/pdf/2507.16815. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.4. Learning Strategy and Inference), p. 6 (3.4. Learning Strategy and Inference), p. 4 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 5 (3.3. Reasoning-Enhanced Action Adaptation)): During reasoning-enhanced action adaptation, we freeze ℱ𝜃while updating the action model 𝜋𝜑with state encoder and latent projector on the target environment by conditioning on the latent visual plan 𝑐𝑡.

## Method Body Digest

- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** During reasoning-enhanced action adaptation, we freeze ℱ𝜃while updating the action model 𝜋𝜑with state encoder and latent projector on the target environment by conditioning on the ...
- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** At inference time, given a visual observation 𝑜𝑡and instruction 𝑙, ThinkAct produces a visual plan latent 𝑐𝑡= ℱ𝜃(𝑜𝑡, 𝑙), which conditions the action module 𝜋𝜑to ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...
- **p. 4 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 5 / 3.3. Reasoning-Enhanced Action Adaptation - extractive body cue:** Thus, we solely update the state encoder, latent projector, and action 5
- **p. 5 / 3.3. Reasoning-Enhanced Action Adaptation - extractive body cue:** Specifically, we build upon a Transformerbased action model 𝜋𝜑(e.g., Diffusion Policy Chi et al.
- **p. 5 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** Thus, we optimize ℱ𝜃by maximizing the following objective: 𝒥GRPO(𝜃) = 1 𝑀 𝑀 ∑︁ 𝑖=1 ( ℱ𝜃(𝑧𝑖/𝑜𝑡, 𝑙) ℱ𝜃old(𝑧𝑖/𝑜𝑡, 𝑙)𝐴𝑖-𝛽𝐷𝐾𝐿(ℱ𝜃(𝑧𝑖/𝑜𝑡, 𝑙) ‖ ℱ𝜃old(𝑧𝑖/𝑜𝑡, 𝑙))), (4) ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose ThinkAct, which aims to enable MLLMs with the capability to reason before acting in physical environments.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...

## Source Evidence Cues

- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** During reasoning-enhanced action adaptation, we freeze ℱ𝜃while updating the action model 𝜋𝜑with state encoder and latent projector on the target environment by conditioning on the ...
- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** At inference time, given a visual observation 𝑜𝑡and instruction 𝑙, ThinkAct produces a visual plan latent 𝑐𝑡= ℱ𝜃(𝑜𝑡, 𝑙), which conditions the action module 𝜋𝜑to ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...
- **p. 4 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 5 / 3.3. Reasoning-Enhanced Action Adaptation - extractive body cue:** Thus, we solely update the state encoder, latent projector, and action 5
- **p. 5 / 3.3. Reasoning-Enhanced Action Adaptation - extractive body cue:** Specifically, we build upon a Transformerbased action model 𝜋𝜑(e.g., Diffusion Policy Chi et al.
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 3); 2.2. Reasoning in Vision-Language-(Action) Models (p. 3); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | During reasoning-enhanced action adaptation, we freeze ℱ𝜃while updating the action model 𝜋𝜑with state encoder and latent projector on the target environment by ... | p. 6 (3.4. Learning Strategy and Inference), p. 6 (3.4. Learning Strategy and Inference) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | At inference time, given a visual observation 𝑜𝑡and instruction 𝑙, ThinkAct produces a visual plan latent 𝑐𝑡= ℱ𝜃(𝑜𝑡, 𝑙), which conditions the ... | p. 6 (3.4. Learning Strategy and Inference), p. 4 (3.1. Problem Formulation) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual ... | p. 4 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** Thus, we optimize ℱ𝜃by maximizing the following objective: 𝒥GRPO(𝜃) = 1 𝑀 𝑀 ∑︁ 𝑖=1 ( ℱ𝜃(𝑧𝑖/𝑜𝑡, 𝑙) ℱ𝜃old(𝑧𝑖/𝑜𝑡, 𝑙)𝐴𝑖-𝛽𝐷𝐾𝐿(ℱ𝜃(𝑧𝑖/𝑜𝑡, 𝑙) ‖ ℱ𝜃old(𝑧𝑖/𝑜𝑡, 𝑙))), (4) ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...
- **p. 5 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning the trajectory reward is proposed to regularize the predicted 𝜏to match the distribution of demonstrated trajectory ˆ𝜏.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** Reward acts at every step (a) (b) Latent Projector State Encoder reasons every N steps Figure 2: Overview of our ThinkAct.
- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** After SFT cold-start, our MLLM ℱ𝜃is tuned with action-aligned rewards guiding the generation of effective latent plans.
- **p. 6 / 3.3. Reasoning-Enhanced Action Adaptation - extractive body cue:** This asynchronous design highlights a key advantage of our dual-system architecture, allowing the reasoning MLLM to perform slow thinking while the action model executes fast ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 5 (3.3. Reasoning-Enhanced Action Adaptation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | predicts, actions, current, state, composed, visual, observations, language, instructions, timestep, model, receives, observation, textual | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | predicts, actions, current, state, composed, visual, observations, language, instructions, timestep | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, ThinkAct, dual-system, framework, mutually, enhances, action | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Thus, optimize, maximizing, following, objective, GRPO, where, mean, then, picked | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.3. Reasoning-Enhanced Action Adaptation - extractive body cue:** (2023)), which predicts actions based on the current state composed of visual observations and language instructions.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At each timestep 𝑡, the model receives a visual observation 𝑜𝑡and a textual instruction 𝑙, with the goal of predicting an action 𝑎𝑡, which can ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** (a) Given observation 𝑜𝑡and instruction 𝑙, ThinkAct advances actionaligned rewards derived from visual trajectory 𝜏to incentivize embodied reasoning capability of Reasoning MLLM ℱ𝜃.
- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** At inference time, given a visual observation 𝑜𝑡and instruction 𝑙, ThinkAct produces a visual plan latent 𝑐𝑡= ℱ𝜃(𝑜𝑡, 𝑙), which conditions the action module 𝜋𝜑to ...
- **p. 2 / 1. Introduction - extractive body cue:** Reinforcement Reasoning Action-Aligned Visual Feedback "Put the strawberry in the drawer." GRPO >> >> Let's start by analyzing the image and the task at hand. ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by ...
- **p. 4 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** Reward Shaping from Action-Aligned Visual Feedback To tackle this challenge, we design a novel action-aligned visual feedback that captures long-horizon goals and encourages visual grounding ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 2(a), given an observation 𝑜𝑡at timestep 𝑡and a task instruction 𝑙, the MLLM ℱ𝜃autoregressively generates a sequence of latent embeddings for reasoning ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Once the reinforced fine-tuning is complete, we are able to produce long CoT steps, while abstracting the textual reasoning into a compact ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We fine-tune the action model on just 10 demonstrations per task and evaluate performance over 100 trials. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** At inference time, given a visual observation 𝑜𝑡and instruction 𝑙, ThinkAct produces a visual plan latent 𝑐𝑡= ℱ𝜃(𝑜𝑡, 𝑙), which conditions the action module 𝜋𝜑to ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** (2024) for 6K iterations, using batch size 64, learning rate 1e-6, and rollout size 5.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** (2023) tasks are further fine-tuned for 75K iterations with batch size 128.
- **p. 10 / 4.5. Analysis of ThinkAct - extractive body cue:** We fine-tune the action model on just 10 demonstrations per task and evaluate performance over 100 trials.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** During, reasoning-enhanced, action, adaptation, freeze, while, updating, model, state, encoder, latent, projector, target, environment, conditioning, visual, plan, inference, time, given.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 3); 2.2. Reasoning in Vision-Language-(Action) Models (p. 3); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the ... | p. 8 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup) |
| Action / skill decoding | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | p. 7 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation) |
| Receding execution / feedback | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct) |

## Failure and Ablation Link

- **p. 9 / 4.4. Ablation Study - extractive body cue:** Finally, the SFT cold-start model without RL yields the lowest scores, verifying the effectiveness of our RL fine-tuning for eliciting the reasoning capability in MLLMs.
- **p. 9 / 4.4. Ablation Study - extractive body cue:** When both 𝑟traj and 𝑟goal are removed, leaving only QA-style reward from QA datasets, the model shows only marginal improvements over the SFT baseline, confirming ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** (2024) includes Google-VM (Visual Matching), Google-VA (Variant Aggregation), and Bridge-VM setups, introducing variations in color, material, lighting, and camera pose to evaluate model robustness.
- **p. 10 / 4.4. Ablation Study - extractive body cue:** ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning Table 3: Quantitative ablation study for our proposed RL rewards in ThinkAct on SimplerEnv, EgoPlan-Bench2, and RoboVQA ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** (2023) tasks are further fine-tuned for 75K iterations with batch size 128.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** (2023) as the latent projector with 32 queries and fine-tune on 100K OXE samples for 120K iterations using batch size 256 and learning rate 2e-5.
- **p. 8 / 4.2. Quantitative Evaluation - extractive body cue:** Note that, Qwen2.5-VL* indicates fine-tuning the original Qwen2.5-VL using EgoPlan-IT Chen et al.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.4. Learning Strategy and Inference), p. 6 (3.4. Learning Strategy and Inference), p. 4 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 5 (3.3. Reasoning-Enhanced Action Adaptation), objective p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.1. Problem Formulation), p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference), p. 6 (3.3. Reasoning-Enhanced Action Adaptation), temporal p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 3 (3.1. Problem Formulation), p. 7 (4.2. Quantitative Evaluation), p. 1 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
