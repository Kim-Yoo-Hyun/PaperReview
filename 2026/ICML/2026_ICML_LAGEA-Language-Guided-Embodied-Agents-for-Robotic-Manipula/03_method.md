# Method - LAGEA: Language Guided Embodied Agents for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=watVfFbZGF; PDF retrieval source: https://openreview.net/pdf/28f8573440fbd9bb2ac48d0e31f3573d128fcf46.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.2. Reward Generation), p. 3 (3.1.2. KEY FRAME GENERATION), p. 3 (3. Methodology), p. 5 (3.2. Reward Generation), p. 5 (3.3. Dynamic Reward Shaping)): The first enforces absolute calibration: the diagonal cosine ψt = ⟨zt, zf⟩is treated as a logit (scaled by temperature τbce) and supervised with the per-step success label yt ∈ {0, ...

## Method Body Digest

- **p. 4 / 3.1.3. FEEDBACK ALIGNMENT - extractive PDF cue:** The first enforces absolute calibration: the diagonal cosine ψt = ⟨zt, zf⟩is treated as a logit (scaled by temperature τbce) and supervised with the per-step ...
- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** We define a goal potential ϕt by averaging instruction text- and image-goal affinities, then shape its temporal difference and get the goal-delta reward, rgoal t ...
- **p. 3 / 3.1.2. KEY FRAME GENERATION - extractive PDF cue:** To keep the gate deterministic and model-agnostic, we compute key frames from the goal-similarity trajectory using image embeddings.
- **p. 3 / 3. Methodology - extractive PDF cue:** Each episode, Qwen-2.5-VL-3B emits a compact, structured self-reflection, which we encode with a lightweight GPT-2 (Radford et al., 2019) model and pair it with keyframe-based ...
- **p. 5 / 3.2. Reward Generation - extractive PDF cue:** (a) A Goal Potential ϕt is formed by aligning the current state zt with the goal image zg and instruction zy.
- **p. 5 / 3.3. Dynamic Reward Shaping - extractive PDF cue:** We apply shaping only on failures using the mask mt = 1[ rtask t < 0 ], and we down-weight shaping as the policy improves.
- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** With the shared space in place, we convert progress toward the task and movement toward the feedback into dense, directional rewards.
- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** In parallel, we reward movement toward the feedback direction and concentrate credit to causal moments via the key-frame weights ˆwt.

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** For this purpose, we present our framework LAGEA, which addresses this by using VLMs to generate episodic natural-language reflections on a robot's 1 arXiv:2509.23155v3 [cs.RO] ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our core contributions are: • We present LAGEA, an embodied VLM-RL framework that generates causal episodic feedback which are localized in time to turn failures ...
- **p. 3 / 3. Methodology - extractive PDF cue:** Our framework overview is given in Figure 1.

## Source Evidence Cues

- **p. 4 / 3.1.3. FEEDBACK ALIGNMENT - extractive PDF cue:** The first enforces absolute calibration: the diagonal cosine ψt = ⟨zt, zf⟩is treated as a logit (scaled by temperature τbce) and supervised with the per-step ...
- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** We define a goal potential ϕt by averaging instruction text- and image-goal affinities, then shape its temporal difference and get the goal-delta reward, rgoal t ...
- **p. 3 / 3.1.2. KEY FRAME GENERATION - extractive PDF cue:** To keep the gate deterministic and model-agnostic, we compute key frames from the goal-similarity trajectory using image embeddings.
- **p. 3 / 3. Methodology - extractive PDF cue:** Each episode, Qwen-2.5-VL-3B emits a compact, structured self-reflection, which we encode with a lightweight GPT-2 (Radford et al., 2019) model and pair it with keyframe-based ...
- **p. 5 / 3.2. Reward Generation - extractive PDF cue:** (a) A Goal Potential ϕt is formed by aligning the current state zt with the goal image zg and instruction zy.
- **p. 5 / 3.3. Dynamic Reward Shaping - extractive PDF cue:** We apply shaping only on failures using the mask mt = 1[ rtask t < 0 ], and we down-weight shaping as the policy improves.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The first enforces absolute calibration: the diagonal cosine ψt = ⟨zt, zf⟩is treated as a logit (scaled by temperature τbce) and supervised ... | p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.2. Reward Generation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We define a goal potential ϕt by averaging instruction text- and image-goal affinities, then shape its temporal difference and get the goal-delta ... | p. 4 (3.2. Reward Generation), p. 3 (3.1.2. KEY FRAME GENERATION) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To keep the gate deterministic and model-agnostic, we compute key frames from the goal-similarity trajectory using image embeddings. | p. 3 (3.1.2. KEY FRAME GENERATION), p. 3 (3. Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** With the shared space in place, we convert progress toward the task and movement toward the feedback into dense, directional rewards.
- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** In parallel, we reward movement toward the feedback direction and concentrate credit to causal moments via the key-frame weights ˆwt.
- **p. 5 / 3.2. Reward Generation - extractive PDF cue:** The computation of our delta-based rewards.
- **p. 5 / 3.2. Reward Generation - extractive PDF cue:** The temporal difference of these potentials creates the fused feedback-VLM rewards.
- **p. 3 / 3.1.1. STRUCTURED FEEDBACK - extractive PDF cue:** The model is required to return only a schema-constrained JSON.
- **p. 3 / 3.1.2. KEY FRAME GENERATION - extractive PDF cue:** We therefore identify a small set of key frames and diffuse their influence locally in time, so learning focuses on causal moments (approach, contact, reversal).
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 3 (3.1.2. KEY FRAME GENERATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | project, images, instruction, text, feedback, unit-norm, embeddings, current, state, goal, image, episodic, Key-frame, weights | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | project, images, instruction, text, feedback, unit-norm, embeddings, current, state, goal | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | purpose, present, framework, LAGEA, addresses, VLMs, generate, episodic, natural-language, reflections | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | shared, space, place, convert, progress, toward, task, movement, feedback, dense | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Reward Generation - extractive PDF cue:** We project images, instruction text, and feedback with Ei, Et, Ef and use unit-norm embeddings for the current state zt, the goal image zg, the ...
- **p. 4 / 3.1.3. FEEDBACK ALIGNMENT - extractive PDF cue:** Key-frame weights ˆwt identify when gradients should matter; the remaining step is to make the episodic feedback f actionable by aligning it with visual states ...
- **p. 5 / 3.2. Reward Generation - extractive PDF cue:** (a) A Goal Potential ϕt is formed by aligning the current state zt with the goal image zg and instruction zy.
- **p. 1 / 1. Introduction - extractive PDF cue:** Prior self-reflection paradigms (Shinn et al., 2023) show that textual self-critique can improve decision making, but these demonstrations largely live in text-only environments such as ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The potential itself blends two agreements: how well the current state matches the instruction-defined goal, and how well the transition aligns with the VLM's diagnosis ...
- **p. 2 / 1. Introduction - extractive PDF cue:** As smaller VLMs can hallucinate or drift in free-form text (Guan et al., 2024; Chen et al., 2024b), feedback is structured and aligned with goal ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To reduce engineering overhead, a pragmatic trend is to treat VLMs as zero-shot reward models (Rocamonde et al., 2023), scoring progress from natural-language goals and ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We compute a proximity signal st and its temporal derivatives and convert them into a per-step saliency pt, which favours frames that ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We then form K keyframes by selecting up to M high-saliency indices with a minimum temporal spacing (endpoints always kept), yielding a ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 400 200 0 200 400 VLM Reward VLM Reward Signal Over Training 0.0M 0.2M 0.4M 0.6M 0.8M ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, enforces, absolute, calibration, diagonal, cosine, treated, logit, scaled, temperature, supervised, per-step, success, label, successful, steps, pull, image, feedback, together.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Setup: We evaluate LAGEA framework on ten robotics tasks from the Meta-world MT10 benchmark (Yu et al., 2020) and Robotic Fetch (Plappert ... | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Action / skill decoding | As summarized in Table 3, we report the average success rate where LAGEA consistently outperforms all baselines across the four Fetch tasks. | p. 6 (4.1.2. RESULTS ON FETCH TASKS), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| Receding execution / feedback | Table 8. Effect of different text encoders on observation-based manipulation tasks. Results are averaged over three random seeds (Standard Deviation is in ... | p. 15 (Figure/Table caption), p. 6 (4. Experiments) |

## Failure and Ablation Link

- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 13. Failure case with structured feedback for door-open-v2-goal-observable task. K. Ablation To quantify the contribution of each component in LAGEA, we run controlled ablations ...
- **p. 8 / 4.3.2. KEYFRAME EXTRACTION & CREDIT - extractive PDF cue:** LAGEA with keyframing learns the task efficiently, while the variant without keyframing catastrophically fails.
- **p. 6 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** To validate our design choices and disentangle the individual contributions of our core components, we conduct a series of comprehensive ablation studies.
- **p. 7 / 4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE - extractive PDF cue:** SHAPING To isolate the contributions of our key reward components, we performed a targeted ablation study on both observable random goal and hidden fixed goal ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We also include LIV (Ma et al., 2023), a robotics reward model pre-trained on large-scale datasets, and a variant, LIV-Proj, which utilizes randomly initialized and ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate LAGEA on a suite of simulated embodied manipulation tasks, comparing against baseline RL agents and ablated LAGEA variants to measure the contributions of ...
- **p. 7 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** No, rgoal t No, rfb t No, LaGEA 79% 80% 80% 99% 19% (b) Reward shaping ablation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.2. Reward Generation), p. 3 (3.1.2. KEY FRAME GENERATION), p. 3 (3. Methodology), p. 5 (3.2. Reward Generation), p. 5 (3.3. Dynamic Reward Shaping), objective p. 4 (3.2. Reward Generation), p. 4 (3.2. Reward Generation), p. 5 (3.2. Reward Generation), p. 5 (3.2. Reward Generation), p. 3 (3.1.1. STRUCTURED FEEDBACK), p. 3 (3.1.2. KEY FRAME GENERATION), temporal p. 3 (3.1.2. KEY FRAME GENERATION), p. 3 (3.1.2. KEY FRAME GENERATION), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 4 (3.1.3. FEEDBACK ALIGNMENT), p. 7 (4.1.2. RESULTS ON FETCH TASKS), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
