# Method - Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=P64X2q1n1H; PDF retrieval source: https://openreview.net/pdf/d1d48bb8ae32dab3bc513e65d14fb7fc84c438ea.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Training Procedures), p. 4 (3.2. Model Architecture), p. 5 (3.3. Training Procedures), p. 4 (3. Method), p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures)): Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit CoT to compact text latents, ...

## Method Body Digest

- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit ...
- **p. 4 / 3.2. Model Architecture - extractive PDF cue:** Specifically, action generation is performed by a 16-layer Diffusion Transformer composed of alternating self-attention and cross-attention layers, which conditions on the learned latent representations to ...
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Embodied reasoning is modeled as a sequence of continuous latent states, and discrete CoT tokens are progressively replaced by latent representations during training.
- **p. 4 / 3. Method - extractive PDF cue:** We then introduce the model architecture of LaRA-VLA and detail its training procedures in Sections 3.2 and 3.3, respectively.
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** We introduce an attention mechanism tailored to our three-stage training paradigm, as illustrated in Figure 3.
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** The model is lastly optimized using 0.2 Lvis + Lact-dis, which promotes latent-space reasoning while maintaining accurate action semantics.
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Concretely, action tokens are trained using an autoregressive objective, similar to Equation 1, yielding the action-token loss Lact-dis.
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Formally, we adopt the same training objectives as in Stage I, including the textual CoT likelihood and the visual latent prediction loss.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are threefold: • We introduce a latent-reasoning paradigm for VisionLanguage-Action models, in which chain-of-thought reasoning is internalized into continuous latent representations across textual ...
- **p. 4 / 3.2. Model Architecture - extractive PDF cue:** To predict visual goal information, we introduce a dedicated <img next> token to represent predicted visual latents, which enables explicit supervision and alignment during early-stage ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose Latent Reasoning VLA (LaRA-VLA), a unified latent-reasoning VLA framework that performs reasoning and prediction entirely in latent space for ...

## Source Evidence Cues

- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit ...
- **p. 4 / 3.2. Model Architecture - extractive PDF cue:** Specifically, action generation is performed by a 16-layer Diffusion Transformer composed of alternating self-attention and cross-attention layers, which conditions on the learned latent representations to ...
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Embodied reasoning is modeled as a sequence of continuous latent states, and discrete CoT tokens are progressively replaced by latent representations during training.
- **p. 4 / 3. Method - extractive PDF cue:** We then introduce the model architecture of LaRA-VLA and detail its training procedures in Sections 3.2 and 3.3, respectively.
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** We introduce an attention mechanism tailored to our three-stage training paradigm, as illustrated in Figure 3.
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** The model is lastly optimized using 0.2 Lvis + Lact-dis, which promotes latent-space reasoning while maintaining accurate action semantics.
- **Detected method headings:** 2.1. Vision Language Action Models (p. 3); 3. Method (p. 4); 3.2. Model Architecture (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based ... | p. 5 (3.3. Training Procedures), p. 4 (3.2. Model Architecture) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Specifically, action generation is performed by a 16-layer Diffusion Transformer composed of alternating self-attention and cross-attention layers, which conditions on the learned ... | p. 4 (3.2. Model Architecture), p. 5 (3.3. Training Procedures) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Embodied reasoning is modeled as a sequence of continuous latent states, and discrete CoT tokens are progressively replaced by latent representations during ... | p. 5 (3.3. Training Procedures), p. 4 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Concretely, action tokens are trained using an autoregressive objective, similar to Equation 1, yielding the action-token loss Lact-dis.
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Formally, we adopt the same training objectives as in Stage I, including the textual CoT likelihood and the visual latent prediction loss.
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** The training objective is defined as the negative log-likelihood of the ground-truth CoT sequence: Lcot = - TCoT X t=1 log pθ(ct / c<t, v, ...
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** In Stage II, we progressively anneal the explicit CoT supervision loss Lcot to zero.
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** In Stage I, we jointly optimize the CoT supervision loss, the visual alignment loss, and the discrete action loss, i.e., Lcot + 0.1Lvis + Lact-dis, ...
- **p. 4 / 3.2. Model Architecture - extractive PDF cue:** In the final stage, we remove explicit action token prediction and instead activate a dedicated action expert, decoupling action generation from token-level autoregressive decoding.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Vision-Language-Action, VLA, models, have, emerged, promising, direction, scalable, general-purpose, robotic, manipulation, Kim, Bai, they | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Vision-Language-Action, VLA, models, have, emerged, promising, direction, scalable, general-purpose, robotic | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, threefold, introduce, latent-reasoning, paradigm, VisionLanguage-Action, models, chain-of-thought, reasoning, internalized | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Concretely, action, tokens, trained, autoregressive, objective, similar, Equation, yielding, action-token | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** Vision-Language-Action (VLA) models have emerged as a promising direction for scalable, general-purpose robotic manipulation (Kim et al., 2025b; Bai et al., 2025b), as they aim ...
- **p. 4 / 3.3. Training Procedures - extractive PDF cue:** Given input images and a language instruction, the image encoder first maps the visual observation to a sequence of visual tokens, denoted as v, while ...
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Specifically, we employ an inverse dynamics function f(vt, vt+1 / x, c) = at, which estimates the action that induces the transition between consecutive visual ...
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit ...
- **p. 3 / 1. Introduction - extractive PDF cue:** Specifically, we categorize models by whether their textual CoT is represented as explicit discrete tokens or continuous latent states, whether their visual CoT aligns with ...
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** Here, text tokens serve as a unified abstraction that corresponds to language instructions and textual chain-of-thought in Stages I and II, and to text latents ...
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** Attention mechanism used in LaRA-VLA. of the current visual observation and language instruction, the intermediate text-based reasoning latent, and the predicted future visual latent produced ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Let at denote the ground-truth action at time step t, and let ϵ ∼N(0, I) be Gaussian noise. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The flow matching loss is defined as Lact-con = Eat, ϵ, τ h ∥vθa(aτ, τ / ht) -(at -ϵ)∥2 2 i , ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | During evaluation, each task is executed for 12 rollout trials. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit ...
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Embodied reasoning is modeled as a sequence of continuous latent states, and discrete CoT tokens are progressively replaced by latent representations during training.
- **p. 4 / 3. Method - extractive PDF cue:** We then introduce the model architecture of LaRA-VLA and detail its training procedures in Sections 3.2 and 3.3, respectively.
- **p. 6 / 3.3. Training Procedures - extractive PDF cue:** We introduce an attention mechanism tailored to our three-stage training paradigm, as illustrated in Figure 3.
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** Training proceeds in three stages: (i) explicit CoT fine-tuning with aligned visual prediction latents and inverse-dynamics supervision for actions; (ii) a curriculum-based transition from explicit ...
- **p. 5 / 3.3. Training Procedures - extractive PDF cue:** To stabilize visual latent learning and prevent representation collapse, we follow prior work (Chen et al., 2025a) and update the parameters used to compute target ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Training, proceeds, three, stages, explicit, CoT, fine-tuning, aligned, visual, prediction, latents, inverse-dynamics, supervision, actions, curriculum-based, transition, compact, text, gradually, reducing.
- **Relevant PDF headings:** 2.1. Vision Language Action Models (p. 3); 3. Method (p. 4); 3.2. Model Architecture (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We evaluate the effectiveness of LaRA-VLA and the overall system through a comprehensive set of experiments spanning both simulation benchmarks and real-world ... | p. 6 (4. Experiments), p. 7 (4.1. Simulation Experiments) |
| Action / skill decoding | (Section 4.1) • How well does LaRA-VLA perform on long-horizon real-world manipulation tasks compared to state-of-the-art approaches? | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Receding execution / feedback | As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and ... | p. 8 (4.2. Real-World Experiments), p. 7 (4.1. Simulation Experiments) |

## Failure and Ablation Link

- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 9. Effect of CoT supervision and inference-time reasoning on SimplerEnv. We compare models trained with or without CoT supervision and evaluate whether CoT-related tokens ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Table 8. Effect of action pretraining on SimplerEnv. We compare models with and without discrete action supervision during the pretraining stages, while keeping all other ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 11. Prompt for object identification. D. Additional Experiments D.1. Additional Analysis Effect of Action Pretraining. We further study the effect of action supervision during ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Figure 13. Effect of EMA on latent text token distributions. Without EMA, bounding-box and motion-related latent tokens exhibit stronger overlap, indicating greater semantic entanglement. EMA ...
- **p. 6 / 4. Experiments - extractive PDF cue:** (Section 4.2) • How effective are the latent reasoning components in LaRA-VLA, and what additional advantages does our ap6
- **p. 8 / 4.1. Simulation Experiments - extractive PDF cue:** Ablation study of different forms of CoT supervision on SimplerEnv.
- **p. 8 / 4.3. Analysis - extractive PDF cue:** We further compare LaRA-VLA with Qwen-GR00T (Community, 2026), which serves as a no-CoT baseline without latent reasoning.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Training Procedures), p. 4 (3.2. Model Architecture), p. 5 (3.3. Training Procedures), p. 4 (3. Method), p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), objective p. 5 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 4 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 4 (3.2. Model Architecture), temporal p. 5 (3.3. Training Procedures), p. 6 (3.3. Training Procedures), p. 4 (3.1. Data Collection), p. 4 (3.3. Training Procedures), p. 5 (3.3. Training Procedures), p. 8 (4.2. Real-World Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
