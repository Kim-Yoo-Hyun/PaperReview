# Method - VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.21445; PDF retrieval source: https://arxiv.org/pdf/2602.21445. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon), p. 5 (3.3. VLA Knows Its Limits), p. 3 (3.1. Preliminary), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 3 (3.1. Preliminary)): Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively "looks ahead." Our objective is to identify the ...

## Method Body Digest

- **p. 6 / 3.4. AutoHorizon - extractive body cue:** Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively "looks ahead." Our ...
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics.
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** We infer that, due to the strong vision-language pretraining of the backbone model, most linguistic semantics are already embedded within the visual representations during action ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Within a standard transformer-based attention mechanism, the attention weight matrix S is defined as the post-softmax similarity between the query and key embeddings: S = ...
- **p. 4 / 3.2. Existence of Optimal Execution Horizon - extractive body cue:** Conversely, when the policy struggles to accurately model the implicit environment dynamics and the intra-chunk divergence loss δd(e) dominates, a shorter execution horizon becomes more ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** During execution, the agent typically performs the first e actions from the predicted chunk before re-sampling new input observations and generating the next action chunk, ...
- **p. 6 / 3.4. AutoHorizon - extractive body cue:** We then compute the incremental change ∆µt[i] = µt[i] -µt[i -1], which tracks the evolution of the attention trajectory.
- **p. 4 / 3.2. Existence of Optimal Execution Horizon - extractive body cue:** Let δc denote the loss in final task reward incurred at each chunk transition, assumed to be independent of e.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we introduce a bidirectional soft-pointer mechanism that locates the first turning points where the attention mass ceases to advance and begins to plateau.
- **p. 3 / 3.1. Preliminary - extractive body cue:** Building on these insights, we introduce an efficient strategy for execution 3

## Source Evidence Cues

- **p. 6 / 3.4. AutoHorizon - extractive body cue:** Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively "looks ahead." Our ...
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics.
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** We infer that, due to the strong vision-language pretraining of the backbone model, most linguistic semantics are already embedded within the visual representations during action ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Within a standard transformer-based attention mechanism, the attention weight matrix S is defined as the post-softmax similarity between the query and key embeddings: S = ...
- **p. 4 / 3.2. Existence of Optimal Execution Horizon - extractive body cue:** Conversely, when the policy struggles to accurately model the implicit environment dynamics and the intra-chunk divergence loss δd(e) dominates, a shorter execution horizon becomes more ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** During execution, the agent typically performs the first e actions from the predicted chunk before re-sampling new input observations and generating the next action chunk, ...
- **p. 6 / 3.4. AutoHorizon - extractive body cue:** We then compute the incremental change ∆µt[i] = µt[i] -µt[i -1], which tracks the evolution of the attention trajectory.
- **Detected method headings:** 2.1. Vision-Language-Action Models (p. 2); 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively ... | p. 6 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics. | p. 5 (3.4. AutoHorizon), p. 5 (3.3. VLA Knows Its Limits) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We infer that, due to the strong vision-language pretraining of the backbone model, most linguistic semantics are already embedded within the visual ... | p. 5 (3.3. VLA Knows Its Limits), p. 3 (3.1. Preliminary) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Existence of Optimal Execution Horizon - extractive body cue:** Let δc denote the loss in final task reward incurred at each chunk transition, assumed to be independent of e.
- **p. 6 / 3.4. AutoHorizon - extractive body cue:** Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively "looks ahead." Our ...
- **p. 6 / 3.4. AutoHorizon - extractive body cue:** For the forward pointer qs, the expected predictive horizon for each row i is computed as µt[i] = max   p-1 X j=0 j ...
- **p. 4 / 3.2. Existence of Optimal Execution Horizon - extractive body cue:** (2) Proposition 1 (Unique Error Minimizer).
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** Second, because the policies are trained on expert demonstrations with randomly sampled starting timestamps, both the initial and terminal actions play a role in preserving ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** In the following, we first show that flow-matching policy performance exhibits a peaked trend with respect to the execution horizon, underscoring the need and feasibility ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (3.4. AutoHorizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 5 (3.3. VLA Knows Its Limits), p. 6 (3.4. AutoHorizon).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Denote, pretrained, diffusion-/flow-based, VisionLanguage-Action, VLA, model, At/ot, where, represents, input, visual, observations, time, step | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Denote, pretrained, diffusion-/flow-based, VisionLanguage-Action, VLA, model, At/ot, where, represents, input | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Building, insights, AutoHorizon, novel, attention-guided, strategy, dynamically, estimates, execution, horizon | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Let, denote, loss, final, task, reward, incurred, chunk, transition, assumed | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Preliminary - extractive body cue:** Denote the pretrained diffusion-/flow-based VisionLanguage-Action (VLA) model as π(At/ot, c), where ot represents the input visual observations at time step t, and c denotes the ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** During execution, the agent typically performs the first e actions from the predicted chunk before re-sampling new input observations and generating the next action chunk, ...
- **p. 1 / 1. Introduction - extractive body cue:** Instead of predicting a single action at each step, the policy outputs a sequence of actions-an action chunk.
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** The first 768 tokens correspond to visual input, followed by 200 language tokens, and the remaining correspond to action tokens.
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** In contrast, as these attention weights decline, the model increasingly conditions on its own previously generated actions rather than grounded sensory inputs.
- **p. 1 / 1. Introduction - extractive body cue:** Within this paradigm, Vision-Language-Action (VLA) models [3, 12, 16, 19, 26, 27, 40] have emerged as a promising direction for their ability to ground visual ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | (3) indicates that when the policy is trained on a diverse set of the underlying action distributions and the chunk transition loss ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Adopting a per-chunk horizon is intuitive: as task difficulty and environmental dynamics fluctuate throughout the policy rollout, the optimal execution horizon should ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 Static Oracle e = 1 92.7 ± 0.9 94.7 ± 3.4 82.7 ± 0.9 74.7 ± ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** We infer that, due to the strong vision-language pretraining of the backbone model, most linguistic semantics are already embedded within the visual representations during action ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For GR00T N1.5, we adopt the publicly released pretrained checkpoints with the default prediction horizon of p = 16.
- **p. 4 / 3.1. Preliminary - extractive body cue:** This invariance is consistently observed across different sampling steps, task rollouts, and pretrained models.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Intuitively, quantifies, strongly, i-th, query, action, attends, j-th, revealing, model, effectively, looks, ahead, objective, identify, first, turning, point, attention, trajectory-where.
- **Relevant PDF headings:** 2.1. Vision-Language-Action Models (p. 2); 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Our experiments leverage two benchmark datasets: the LIBERO dataset [20], which offers a diverse suite of single-arm manipulation tasks, and the RoboTwin ... | p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results) |
| Action / skill decoding | Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices. | p. 8 (4.2. Simulation Results), p. 6 (4.1. Experimental Settings) |
| Receding execution / feedback | 8, and find that AutoHorizon consistently achieves higher success rates. | p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4.1. Experimental Settings - extractive body cue:** Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 Static Oracle e = 1 92.7 ± 0.9 94.7 ± 3.4 82.7 ± 0.9 74.7 ± 3.4 e = ...
- **p. 8 / 4.2. Simulation Results - extractive body cue:** We also examine the effect of hyperparameters in Sec.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For π0.5, we conduct experiments with two variants using prediction horizons of p = 10 and p = 50 to examine horizon-dependent behavior.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 8. Effect of language tokens on LIBERO benchmark. Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 p = 10 e = 10
- **p. 14 / Figure/Table caption - extractive body cue:** Table 9. Hyper-parameter sensitivity analysis. L = 2 L = 3 L = 4 L = 5 L = 6 89.9±1.2 92.1±1.0
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For GR00T N1.5, we adopt the publicly released pretrained checkpoints with the default prediction horizon of p = 16.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Visualization of average attention weights in π0.5 across different stages of task execution. Intra-chunk actions consistently attend to the same vision and language ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon), p. 5 (3.3. VLA Knows Its Limits), p. 3 (3.1. Preliminary), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 3 (3.1. Preliminary), objective p. 4 (3.2. Existence of Optimal Execution Horizon), p. 6 (3.4. AutoHorizon), p. 6 (3.4. AutoHorizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 5 (3.3. VLA Knows Its Limits), p. 3 (3.1. Preliminary), temporal p. 4 (3.2. Existence of Optimal Execution Horizon), p. 5 (3.4. AutoHorizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 6 (4.1. Experimental Settings), p. 7 (4.1. Experimental Settings), p. 3 (3.1. Preliminary).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
