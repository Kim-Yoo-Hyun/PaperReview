# Method - Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Rollout-Filter-Label Counterfactual Pipeline), p. 3 (3.1. Self-Reflective Counterfactual Reasoning), p. 5 (3.4. Implementation Details), p. 4 (3.2. Meta-Actions), p. 5 (3.4. Implementation Details), p. 3 (3.1. Self-Reflective Counterfactual Reasoning)): For each scene, two sets of trajectories are generated: 1) Free generation xfree: the model first predicts meta-actions and then decodes the trajectory conditioned on its own meta-actions.

## Method Body Digest

- **p. 4 / 3.3. Rollout-Filter-Label Counterfactual Pipeline - extractive body cue:** For each scene, two sets of trajectories are generated: 1) Free generation xfree: the model first predicts meta-actions and then decodes the trajectory conditioned on ...
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** First, the model needs an intermediate representation that is both interpretable to the language backbone and tightly coupled to action.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** For counterfactual samples in DCF, the loss on the first (uncorrected) meta-action block is also masked to prevent the model from learning from prior mistakes.
- **p. 4 / 3.2. Meta-Actions - extractive body cue:** We use trajectory disagreement between trajectories that are free-generated and those induced by the ground-truth meta-actions to filter data.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** Meta-actions are then introduced by fine-tuning on Dtraj ∪Dmeta, yielding the meta-act model used in the initial rollout (Sec.
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** 3(A), we use the same instruction for the model and allow it to implicitly decide whether to generate the reasoning traces.
- **p. 2 / 2) Meta-actions and counterfactual data pipeline. We use - extractive body cue:** time-segmented meta-actions for action-language alignment and propose the rollout-filter-label pipeline to automatically curate counterfactual data from the rollout of the model, forming a self-improving loop ...
- **p. 5 / 3.4. Implementation Details - extractive body cue:** The model is optimized with cross-entropy loss over assistant-generated tokens only; tokens from system or user prompts are masked.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Second, standard training pipelines rarely teach models to answer counterfactual questions such as: "Given the plan I just proposed, what will happen, and how should ...
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** To prepare data to fine-tune the model, we develop a rolloutfilter-label pipeline (Sec.
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** Adaptive reasoning allows a model to decide dynamically when to conduct reasoning and when to respond directly.

## Source Evidence Cues

- **p. 4 / 3.3. Rollout-Filter-Label Counterfactual Pipeline - extractive body cue:** For each scene, two sets of trajectories are generated: 1) Free generation xfree: the model first predicts meta-actions and then decodes the trajectory conditioned on ...
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** First, the model needs an intermediate representation that is both interpretable to the language backbone and tightly coupled to action.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** For counterfactual samples in DCF, the loss on the first (uncorrected) meta-action block is also masked to prevent the model from learning from prior mistakes.
- **p. 4 / 3.2. Meta-Actions - extractive body cue:** We use trajectory disagreement between trajectories that are free-generated and those induced by the ground-truth meta-actions to filter data.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** Meta-actions are then introduced by fine-tuning on Dtraj ∪Dmeta, yielding the meta-act model used in the initial rollout (Sec.
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** 3(A), we use the same instruction for the model and allow it to implicitly decide whether to generate the reasoning traces.
- **p. 2 / 2) Meta-actions and counterfactual data pipeline. We use - extractive body cue:** time-segmented meta-actions for action-language alignment and propose the rollout-filter-label pipeline to automatically curate counterfactual data from the rollout of the model, forming a self-improving loop ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | For each scene, two sets of trajectories are generated: 1) Free generation xfree: the model first predicts meta-actions and then decodes the ... | p. 4 (3.3. Rollout-Filter-Label Counterfactual Pipeline), p. 3 (3.1. Self-Reflective Counterfactual Reasoning) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | First, the model needs an intermediate representation that is both interpretable to the language backbone and tightly coupled to action. | p. 3 (3.1. Self-Reflective Counterfactual Reasoning), p. 5 (3.4. Implementation Details) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | For counterfactual samples in DCF, the loss on the first (uncorrected) meta-action block is also masked to prevent the model from learning ... | p. 5 (3.4. Implementation Details), p. 4 (3.2. Meta-Actions) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Implementation Details - extractive body cue:** The model is optimized with cross-entropy loss over assistant-generated tokens only; tokens from system or user prompts are masked.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** Within the assistant response, different token groups (meta-actions, reasoning, or trajectory tokens) have different loss weights.
- **p. 3 / 3. Method - extractive body cue:** End-to-end Vision-Language-Action (VLA) models have demonstrated promising progress in mapping visual context directly to control output.
- **p. 3 / 3.1. Self-Reflective Counterfactual Reasoning - extractive body cue:** 2, instead of mapping meta-actions to trajectories (meta→traj), CFVLA performs a self-reflective loop: meta-actions →CF reasoning →updated meta-actions →trajectory.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (3.4. Implementation Details), p. 5 (3.4. Implementation Details), p. 3 (3.1. Self-Reflective Counterfactual Reasoning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | End-to-end, Vision-Language-Action, VLA, models, have, demonstrated, promising, progress, mapping, visual, context, directly, control, output | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | End-to-end, Vision-Language-Action, VLA, models, have, demonstrated, promising, progress, mapping, visual | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Second, standard, training, pipelines, rarely, teach, models, answer, counterfactual, questions | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | model, optimized, cross-entropy, loss, over, assistant-generated, tokens, only, system, user | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive body cue:** End-to-end Vision-Language-Action (VLA) models have demonstrated promising progress in mapping visual context directly to control output.
- **p. 1 / 1. Introduction - extractive body cue:** In these systems, a large visionlanguage backbone engages in a slower, more deliberative form of "thinking", spending additional compute to verbalize the observation and justify ...
- **p. 4 / 3.3. Rollout-Filter-Label Counterfactual Pipeline - extractive body cue:** The output is a single paragraph that: 1) diagnoses why the predicted meta-actions are less preferable than the expert plan, and 2) indicates how they ...
- **p. 2 / 1. Introduction - extractive body cue:** To realize such behavior in practice, CF-VLA combines meta-actions with a rollout-filter-label pipeline: 1) the current policy is rolled out to generate candidate meta-actions and ...
- **p. 2 / 2) Meta-actions and counterfactual data pipeline. We use - extractive body cue:** time-segmented meta-actions for action-language alignment and propose the rollout-filter-label pipeline to automatically curate counterfactual data from the rollout of the model, forming a self-improving loop ...
- **p. 3 / 3.2. Meta-Actions - extractive body cue:** Meta-actions provide a language-native intermediate abstraction between reasoning and low-level action.
- **p. 4 / 3.2. Meta-Actions - extractive body cue:** This temporal format allows the model to reason compositionally about action transitions and to capture temporal intent and directly align language reasoning with the structure ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Second, CF reasoning must relate meta-actions to their future consequences. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | To prepare data to fine-tune the model, we develop a rolloutfilter-label pipeline (Sec. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | The model takes text prompts, two front-facing videos, and the ego-trajectory history as inputs. | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | A wide (120°) and a telephoto (30°) cameras provide 2 videos at 2 Hz over the past 2 s. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.4. Implementation Details - extractive body cue:** Meta-actions are then introduced by fine-tuning on Dtraj ∪Dmeta, yielding the meta-act model used in the initial rollout (Sec.
- **p. 2 / 2) Meta-actions and counterfactual data pipeline. We use - extractive body cue:** time-segmented meta-actions for action-language alignment and propose the rollout-filter-label pipeline to automatically curate counterfactual data from the rollout of the model, forming a self-improving loop ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** scene, sets, trajectories, generated, Free, generation, xfree, model, first, predicts, meta-actions, then, decodes, trajectory, conditioned, needs, intermediate, representation, interpretable, language.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | The counterfactual reasoning dataset DCF comes from the training set of Dmeta. | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Filtering / recovery | With route information, meta-act (w/ route) provides an even stronger baseline. | p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments) |
| Monitoring / re-entry | Figure 1. Counterfactual Vision-Language-Action (CF-VLA) Model. Top: CF-VLA conducts reasoning adaptively. The model engages in reasoning more frequently and achieves more signifi- ... | p. 1 (Figure/Table caption), p. 6 (4.2. Main Experiments) |

## Failure and Ablation Link

- **p. 6 / 4.2. Main Experiments - extractive body cue:** Within each setting (with / without route), CF-VLA variants consistently achieve the lowest or near-lowest collision and off-road rates, indicating that counterfactual self-reflection translates into ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We prepare two variants of the models to train with or without route information, which contain 20 waypoints spanning the future 80m with equal spacing. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablations on meta-trajectory alignment and adaptive counterfactual reasoning. We train models without route information.
- **p. 7 / 4.2. Main Experiments - extractive body cue:** Effect of our proposed data filtering pipeline.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The framework of CF-VLA. A base VLA is fine- tuned on a counterfactual reasoning dataset generated by a roll- out-filter-label pipeline. The resulting ...
- **p. 5 / 3.4. Implementation Details - extractive body cue:** We unfreeze all parameters during training.
- **p. 5 / 3.4. Implementation Details - extractive body cue:** Finally, the full CF-VLA is obtained by further fine-tuning on the mixture Dtraj ∪Dmeta ∪DCF.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.3. Rollout-Filter-Label Counterfactual Pipeline), p. 3 (3.1. Self-Reflective Counterfactual Reasoning), p. 5 (3.4. Implementation Details), p. 4 (3.2. Meta-Actions), p. 5 (3.4. Implementation Details), p. 3 (3.1. Self-Reflective Counterfactual Reasoning), objective p. 5 (3.4. Implementation Details), p. 5 (3.4. Implementation Details), p. 3 (3. Method), p. 3 (3.1. Self-Reflective Counterfactual Reasoning), temporal p. 3 (3.1. Self-Reflective Counterfactual Reasoning), p. 3 (3.1. Self-Reflective Counterfactual Reasoning), p. 4 (3.2. Meta-Actions), p. 4 (3.2. Meta-Actions), p. 5 (3.4. Implementation Details), p. 5 (3.4. Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Within the assistant response, different token groups (meta-actions, reasoning, or trajectory tokens) have different loss weights. (p. 5, 3.4. Implementation Details).
- **Objective/update evidence:** The model is optimized with cross-entropy loss over assistant-generated tokens only; tokens from system or user prompts are masked. (p. 5, 3.4. Implementation Details).
- **Temporal/runtime evidence:** Second, CF reasoning must relate meta-actions to their future consequences. (p. 3, 3.1. Self-Reflective Counterfactual Reasoning).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
