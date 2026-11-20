# Method - World Action Models are Zero-shot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.15922; PDF retrieval source: https://arxiv.org/pdf/2602.15922. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 6 (3.1. Model Architecture), p. 6 (3.1. Model Architecture), p. 8 (3.1. Model Architecture), p. 8 (3.1. Model Architecture)): To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders.

## Method Body Digest

- **p. 7 / 3.1. Model Architecture - extractive body cue:** To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders.
- **p. 7 / 3.1. Model Architecture - extractive body cue:** Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the visual observation history ...
- **p. 6 / 3.1. Model Architecture - extractive body cue:** DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past history o0:𝑙 where ...
- **p. 6 / 3.1. Model Architecture - extractive body cue:** Note that joint prediction of video and action is a decomposition of (1) autoregressive video prediction and (2) action prediction from an inverse-dynamics model (IDM): ...
- **p. 8 / 3.1. Model Architecture - extractive body cue:** To enable efficient training, we perform trajectory-level updates and apply attention masking (e.g., see Figure 14 for details) so that the current noisy chunk can ...
- **p. 8 / 3.1. Model Architecture - extractive body cue:** World Action Models are Zero-shot Policies where 𝑤(𝑡𝑘) > 0 is a predefined weight function for 𝑡𝑘, c is the text condition, q𝑘is the proprioceptive ...
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** During training, this exposes the model to configurations where it must predict clean actions from noisy visual context, directly matching the few-step or single-step inference ...
- **p. 8 / 3.2.3. System-level Optimizations - extractive body cue:** When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities, reducing effective DiT steps from 16 to 4 with minimal quality loss ...

## Design Rationale

- **p. 3 / 1. Introduction - extractive body cue:** Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-tovideo diffusion backbone (Team Wan, 2025).
- **p. 3 / 1. Introduction - extractive body cue:** To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: (1) algorithmic improvements, including decoupled video ...

## Source Evidence Cues

- **p. 7 / 3.1. Model Architecture - extractive body cue:** To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders.
- **p. 7 / 3.1. Model Architecture - extractive body cue:** Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the visual observation history ...
- **p. 6 / 3.1. Model Architecture - extractive body cue:** DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past history o0:𝑙 where ...
- **p. 6 / 3.1. Model Architecture - extractive body cue:** Note that joint prediction of video and action is a decomposition of (1) autoregressive video prediction and (2) action prediction from an inverse-dynamics model (IDM): ...
- **p. 8 / 3.1. Model Architecture - extractive body cue:** To enable efficient training, we perform trajectory-level updates and apply attention masking (e.g., see Figure 14 for details) so that the current noisy chunk can ...
- **p. 8 / 3.1. Model Architecture - extractive body cue:** World Action Models are Zero-shot Policies where 𝑤(𝑡𝑘) > 0 is a predefined weight function for 𝑡𝑘, c is the text condition, q𝑘is the proprioceptive ...
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** During training, this exposes the model to configurations where it must predict clean actions from noisy visual context, directly matching the few-step or single-step inference ...
- **Detected method headings:** 2.1. Vision Language Action Models (p. 4); 2.2. Video Model-based Robot Policies (p. 5); 3.1. Model Architecture (p. 6); 5.2. Model and Data Ablations (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders. | p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the ... | p. 7 (3.1. Model Architecture), p. 6 (3.1. Model Architecture) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past ... | p. 6 (3.1. Model Architecture), p. 6 (3.1. Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 3.2.3. System-level Optimizations - extractive body cue:** When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities, reducing effective DiT steps from 16 to 4 with minimal quality loss ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** Since pretrained video models are already optimized on the video prediction objective on diverse web-scale video data, DreamZero only needs to additionally learn to predict ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** World Action Models are Zero-shot Policies Instead of using two separate models (video prediction model and inverse dynamics model) to model the decomposed objective (Li ...
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** As a result, we reduce the diffusion steps from four to one, cutting inference from ∼350ms to ∼150ms with minimal performance loss (Table 3).
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** However, naively reducing steps degrades action quality because residual visual noise propagates into action predictions.
- **p. 8 / 3.2.3. System-level Optimizations - extractive body cue:** Given the asynchronous execution structure, we optimize inference throughput through parallelism and caching. • CFG Parallelism.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 8 (3.2.3. System-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 8 (3.1. Model Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | DreamZero, jointly, predicts, video, actions, conditioned, language, instruction, proprioceptive, state, visual, observation, including, current | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | DreamZero, jointly, predicts, video, actions, conditioned, language, instruction, proprioceptive, state | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Second, more, surprisingly, DreamZero, enables, few-shot, embodiment, adaptation, model, pretrained | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | When, cosine, similarity, between, successive, velocities, exceeds, threshold, reuse, cached | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.1. Model Architecture - extractive body cue:** DreamZero jointly predicts video o𝑙:𝑙+𝐻and actions a𝑙:𝑙+𝐻conditioned on language instruction c, proprioceptive state q𝑙and visual observation including the current and the past history o0:𝑙 where ...
- **p. 2 / 1. Introduction - extractive body cue:** Initialized from video diffusion models trained on web-scale video data, WAMs leverage rich spatiotemporal priors to jointly generate future frames and actions conditioned on language ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the visual observation history ...
- **p. 2 / 1. Introduction - extractive body cue:** This shifts action learning from dense state-action imitation to inverse dynamics-aligning motor commands with predicted visual futures.
- **p. 3 / 1. Introduction - extractive body cue:** Our architectural analysis reveals that larger pretrained video diffusion models produce higher-quality video predictions, which directly translates to superior downstream action execution-indicating that policy performance ...
- **p. 7 / 3.1. Model Architecture - extractive body cue:** To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders.
- **p. 8 / 3.1. Model Architecture - extractive body cue:** Unlike pure video generation, our closed-loop setting allows ground-truth observations to replace generated frames in the KV cache after each action execution (see Figure 14).
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | This structure transforms the latency constraint from "inference must complete before the robot moves" to "inference must complete before the current action ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | All frames within the same chunk share the same timestep 𝑡𝑘, while different chunks are assigned independent timesteps. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | This structure transforms the latency constraint from "inference must complete before the robot moves" to "inference must complete before the current action ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3.1. Model Architecture - extractive body cue:** Autoregressive generation possesses the following advantages: (1) it enables faster inference speed by utilizing KV-cache, (2) the policy model can leverage the visual observation history ...
- **p. 8 / 3.1. Model Architecture - extractive body cue:** To enable efficient training, we perform trajectory-level updates and apply attention masking (e.g., see Figure 14 for details) so that the current noisy chunk can ...
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** During training, this exposes the model to configurations where it must predict clean actions from noisy visual context, directly matching the few-step or single-step inference ...
- **p. 11 / 4.1. Pretraining - extractive body cue:** We open-source the checkpoint and inference code to run some DROID-sim evals in PolaRiS (Jain et al., 2025).6 Training.
- **p. 9 / 3.2.4. Implementation-level Optimizations - extractive body cue:** The key insight is that, at inference time, actions should denoise to their final values while being conditioned on a still-noisy video representation within the ...
- **p. 11 / 4.1. Pretraining - extractive body cue:** We train for 100K steps with a global batch size of 128 for AgiBot and 100K steps with a global batch size of 128 for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** retain, generalization, capability, video, models, introduce, minimal, additional, parameters, state, encoders, action, decoders, Autoregressive, generation, possesses, following, advantages, enables, faster.
- **Relevant PDF headings:** 2.1. Vision Language Action Models (p. 4); 2.2. Video Model-based Robot Policies (p. 5); 3.1. Model Architecture (p. 6); 5.2. Model and Data Ablations (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks-significantly longer-horizon than typical robotic manipulation datasets ... | p. 10 (4.1. Pretraining), p. 11 (4.1. Pretraining) |
| Filtering / recovery | Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with ... | p. 3 (Figure/Table caption), p. 13 (Figure/Table caption) |
| Monitoring / re-entry | Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training. ... | p. 15 (Figure/Table caption), p. 16 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 11 / 4.1. Pretraining - extractive body cue:** We also conduct some ablations (Section 5.2) where we initialize from Wan2.1-I2V-5B-480P to see the effect of model size (5B vs.
- **p. 10 / 4.1. Pretraining - extractive body cue:** We hypothesize that learning to only predict actions without encoding the knowledge about future world states makes it challenging to leverage highly heterogeneous, non-repetitive data ...
- **p. 10 / 4. Experimental Setup - extractive body cue:** For each baseline, we evaluate two initialization strategies: (1) from-scratch, using pretrained VLM weights without prior robot data training for a fair apple-to-apple comparison with ...
- **p. 12 / 4.1. Pretraining - extractive body cue:** For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 15: Data Collection Environments. We collect teleoperation data across 22 diverse real-world environ- ments, including offices, laboratories, restaurants, supermarkets, coffee shops, warehouses, homes, hotels, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 6: Distribution statistics for the AgiBot pretraining corpus: episode durations, subtask density, and skill coverage across 7.2K episodes (∼500 hours). interaction with objects at ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8: Seen Task Evaluation. DreamZero effectively learns from diverse data and generalizes to new environments, outperforming VLAs across all task categories. VLAs trained from ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 6 (3.1. Model Architecture), p. 6 (3.1. Model Architecture), p. 8 (3.1. Model Architecture), p. 8 (3.1. Model Architecture), objective p. 8 (3.2.3. System-level Optimizations), p. 7 (3.1. Model Architecture), p. 7 (3.1. Model Architecture), p. 9 (3.2.4. Implementation-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 8 (3.2.3. System-level Optimizations), temporal p. 8 (3.2.2. Asynchronous Closed-Loop Execution), p. 7 (3.1. Model Architecture), p. 8 (3.2.4. Implementation-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 9 (3.2.4. Implementation-level Optimizations), p. 10 (4.1. Pretraining).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
