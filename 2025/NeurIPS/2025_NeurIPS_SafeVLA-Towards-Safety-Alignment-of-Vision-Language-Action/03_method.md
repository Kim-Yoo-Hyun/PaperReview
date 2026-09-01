# Method - SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=dt940loCBT; PDF retrieval source: https://openreview.net/pdf/050ee02bf65d6e2e7aa5ba14d172add1b64f86fa.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection), p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection), p. 31 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training)): 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions.

## Method Body Digest

- **p. 32 / C.3 Model Selection - extractive PDF cue:** 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions.
- **p. 33 / C.3 Model Selection - extractive PDF cue:** We use AllenAct [85] and OmniSafe [39] as the training framework.
- **p. 32 / C.3 Model Selection - extractive PDF cue:** 2) Visual Encoder: A goal-conditioned transformer encoder fuses RGB observations from dual cameras (navigation and manipulation views) with language embeddings, enabling cross-modal fusion.
- **p. 33 / C.3 Model Selection - extractive PDF cue:** This combination of architectural strengths and training scalability makes SPOC an optimal base model for this work.
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The corresponding surrogate losses are defined as follows: LR(θ; Dtask) = -El∼Dtask,τ∼πθ h Et h min  ρt(θ) ˆArt, clip (ρt(θ), 1 -ϵ, 1 + ...
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate ...
- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** The combined loss L balances reward maximization and constraint satisfaction Lagrangian multiplier λ, where λ →0 prioritizes reward and λ →∞enforces strict constraint adherence.
- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** This formulation ensures that λk increases when constraints are violated (i.e., when JC > b, where b is the threshold) and decreases otherwise, thereby enforcing ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our study details how these interconnected aspects contribute to a more holistic safety alignment. • Environment: Addressing the gap in comprehensive VLA safety assessment, we ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, these safety mechanisms cannot be directly applied to VLAs, as there is a substantial gap between the abstract safety concerns at the model intention ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are: • Integrated Safety Approach (ISA) Exploration: We conduct a comprehensive investigation into an ISA for VLA safety alignment.

## Source Evidence Cues

- **p. 32 / C.3 Model Selection - extractive PDF cue:** 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions.
- **p. 33 / C.3 Model Selection - extractive PDF cue:** We use AllenAct [85] and OmniSafe [39] as the training framework.
- **p. 32 / C.3 Model Selection - extractive PDF cue:** 2) Visual Encoder: A goal-conditioned transformer encoder fuses RGB observations from dual cameras (navigation and manipulation views) with language embeddings, enabling cross-modal fusion.
- **p. 33 / C.3 Model Selection - extractive PDF cue:** This combination of architectural strengths and training scalability makes SPOC an optimal base model for this work.
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The corresponding surrogate losses are defined as follows: LR(θ; Dtask) = -El∼Dtask,τ∼πθ h Et h min  ρt(θ) ˆArt, clip (ρt(θ), 1 -ϵ, 1 + ...
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate ...
- **Detected method headings:** B.3 Automatic Trajectory Analysis by Large Language Models (p. 27); B.7 ISA with Alternative SafeRL Algorithms (p. 30); B.9 The Integrated Safety Approach (ISA) Pipeline (p. 30); C.3 Model Selection (p. 32)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions. | p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We use AllenAct [85] and OmniSafe [39] as the training framework. | p. 33 (C.3 Model Selection), p. 32 (C.3 Model Selection) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 2) Visual Encoder: A goal-conditioned transformer encoder fuses RGB observations from dual cameras (navigation and manipulation views) with language embeddings, enabling cross-modal ... | p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** The combined loss L balances reward maximization and constraint satisfaction Lagrangian multiplier λ, where λ →0 prioritizes reward and λ →∞enforces strict constraint adherence.
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The corresponding surrogate losses are defined as follows: LR(θ; Dtask) = -El∼Dtask,τ∼πθ h Et h min  ρt(θ) ˆArt, clip (ρt(θ), 1 -ϵ, 1 + ...
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate ...
- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** This formulation ensures that λk increases when constraints are violated (i.e., when JC > b, where b is the threshold) and decreases otherwise, thereby enforcing ...
- **p. 33 / C.3 Model Selection - extractive PDF cue:** 3) Sim-to-Real Compatibility: SPOC's sim-to-real capability, as evidenced by its 56% real-world success rate (Table 9 in SPOC), can facilitate the generalization of our safety ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 33 (C.3 Model Selection).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reward, function, current, state, language, instruction, total, immediate, cost, aggregation, distinct, types, dependent, action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | reward, function, current, state, language, instruction, total, immediate, cost, aggregation | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | study, details, interconnected, aspects, contribute, more, holistic, safety, alignment, Environment | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | combined, loss, balances, reward, maximization, constraint, satisfaction, Lagrangian, multiplier, where | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate ...
- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** At each time step t, the policy considers a temporal context window defined by ht = {(ot-n, at-n), (ot-n+1, at-n+1), . . . , (ot-1, ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Building on the emergence of large language models (LLMs) and vision-language models (VLMs), vision-language-action models (VLAs) [2, 3, 4, 5] advance this field by enabling ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Embodied AI aims to develop a generalist policy that can perform perception, interaction, reasoning, and adaptation in the physical world [1].
- **p. 32 / C.3 Model Selection - extractive PDF cue:** 3) Action Decoder: A causal transformer decoder with 100-step context windows predicts discrete actions by attending to historical observations and actions.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our proposed pipeline employs multifaceted framework for the systematic safety alignment of vision-language-action (VLA) models. challenges posed by the complex and unpredictable physical world [27].
- **p. 2 / 1 Introduction - extractive PDF cue:** By incorporating large-scale procedurally generated scenes and specifically targeting safety critical components, Safety-CHORES more effectively surfaces VLA vulnerabilities than conventional benchmarks. • Empirical Validation and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | At each time step t, the policy considers a temporal context window defined by ht = {(ot-n, at-n), (ot-n+1, at-n+1), . . ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | 2) Long-Horizon Reasoning: The 100-frame transformer context window (Table 6 in SPOC) allows modeling temporal dependencies critical for anticipating and avoiding cumulative ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | At each time step t, the policy considers a temporal context window defined by ht = {(ot-n, at-n), (ot-n+1, at-n+1), . . ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 33 / C.3 Model Selection - extractive PDF cue:** We use AllenAct [85] and OmniSafe [39] as the training framework.
- **p. 33 / C.3 Model Selection - extractive PDF cue:** This combination of architectural strengths and training scalability makes SPOC an optimal base model for this work.
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The corresponding surrogate losses are defined as follows: LR(θ; Dtask) = -El∼Dtask,τ∼πθ h Et h min  ρt(θ) ˆArt, clip (ρt(θ), 1 -ϵ, 1 + ...
- **p. 31 / C.1 Details of SafeRL Training - extractive PDF cue:** The reward rt is a function of the current state st and the language instruction l: rt = r(st+1/st, at, l) (4) The total immediate ...
- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** At iteration k, the policy parameter θk is adjusted by a gradient step on the combined objective LR -λkLC, scaled by a learning rate η ...
- **p. 7 / 5 Experiments - extractive PDF cue:** For simpler tasks like Safety-ObjNav and Safety-PickUp, we train for 15 million steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Action, Decoder, causal, transformer, step, context, windows, predicts, discrete, actions, attending, historical, observations, AllenAct, OmniSafe, training, framework, Visual, Encoder, goal-conditioned.
- **Relevant PDF headings:** B.3 Automatic Trajectory Analysis by Large Language Models (p. 27); B.7 ISA with Alternative SafeRL Algorithms (p. 30); B.9 The Integrated Safety Approach (ISA) Pipeline (p. 30); C.3 Model Selection (p. 32).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 0.0 0.2 0.4 0.6 0.8 1.0 +0.031 -0.038 +0.067 -0.011 Safety-CHORES - SR 0 10 20 30 40 =-23.95 =-36.06 =-26.50 =-29.97 ... | p. 7 (5 Experiments), p. 10 (5 Experiments) |
| Action / skill decoding | ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching or exceeding other RL-based methods. | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Receding execution / feedback | Figure 5: Comparative performance of VLA models on multiple benchmarks. Left: SR of each model per benchmark. Right: CC incurred by each ... | p. 8 (Figure/Table caption), p. 9 (5 Experiments) |

## Failure and Ablation Link

- **p. 9 / 5 Experiments - extractive PDF cue:** 0.86 0.64 0.75 1.85 5.01 4.75 0.00 0.25 0.50 0.75 1.00 0 1 2 3 4 5 ISA ISA without eliciting FLaRe-RS SR 0.82 0.86 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: ISA with fixed penalty coefficients. Importance of Risk Elicitation. The impor- tance of risk elicitation is demonstrated by an ablation study in Figure ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We also evaluate ISA on other VLA models (i.e., EmbCLIP [76], Embodied-Codebook [77] and their variants with different vision encoders).
- **p. 7 / 5 Experiments - extractive PDF cue:** IL+RL (Reward Shaping): FLaRe-RS, a variant of FLaRe where safety costs are directly used as penalties on reward, representing a common heuristic for addressing safety.
- **p. 8 / 5 Experiments - extractive PDF cue:** 5.2.3 Ablation Studies: Impact of Key ISA Design Choices To understand the contribution of specific design choices in ISA, we conduct several ablation studies. mean ...
- **p. 9 / 5 Experiments - extractive PDF cue:** Middle: Ablation on cost thresholds bi.
- **p. 32 / C.1 Details of SafeRL Training - extractive PDF cue:** The JC(θk) measures the expected constraint violation under policy πθk, and α is a dual step-size controlling the sensitivity to constraint violations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection), p. 32 (C.3 Model Selection), p. 33 (C.3 Model Selection), p. 31 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), objective p. 32 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 33 (C.3 Model Selection), temporal p. 32 (C.1 Details of SafeRL Training), p. 33 (C.3 Model Selection), p. 31 (C.1 Details of SafeRL Training), p. 31 (C.1 Details of SafeRL Training), p. 32 (C.1 Details of SafeRL Training), p. 35 (C.4 Experimental Environment and Costs).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
