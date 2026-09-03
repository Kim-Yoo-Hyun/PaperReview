# Method - Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/fan25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/fan25a/fan25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method)): Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking move to the top side ...

## Method Body Digest

- **p. 4 / 3 Method - extractive body cue:** Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking ...
- **p. 5 / 3 Method - extractive body cue:** 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection input dt associated ...
- **p. 3 / 3 Method - extractive body cue:** To enable training and inference within a unified end-to-end VLA framework, we extend the original action representation by adding a one-dimensional phase identifier sp, which ...
- **p. 5 / 3 Method - extractive body cue:** The multi-modal encoder in our model is based on a GPT-2-style Transformer architecture.
- **p. 3 / 3 Method - extractive body cue:** To address this limitation, we propose Long-VLA, a unified end-to-end VLA model that leverages phase-specific data more effectively.
- **p. 4 / 3 Method - extractive body cue:** Based on these observations, we propose an input-level adaptation strategy that dynamically adjusts visual inputs according to the current task phase.
- **p. 4 / 3 Method - extractive body cue:** Using the decomposition dataset, the model is trained with a single score matching loss that jointly supervises both the moving and interaction phases: LDiff = ...
- **p. 4 / 3 Method - extractive body cue:** As a result, the total training loss is formulated as: L = LDiff + αLGoal.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose Long-VLA, the first end-to-end VLA model specifically designed for longhorizon robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Finally, we present L-CALVIN and show that Long-VLA outperforms state-of-the-art methods on simulated and real-world robotic tasks, with robust performance on diverse long-horizon tasks.
- **p. 3 / 3 Method - extractive body cue:** To address this limitation, we propose Long-VLA, a unified end-to-end VLA model that leverages phase-specific data more effectively.

## Source Evidence Cues

- **p. 4 / 3 Method - extractive body cue:** Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking ...
- **p. 5 / 3 Method - extractive body cue:** 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection input dt associated ...
- **p. 3 / 3 Method - extractive body cue:** To enable training and inference within a unified end-to-end VLA framework, we extend the original action representation by adding a one-dimensional phase identifier sp, which ...
- **p. 5 / 3 Method - extractive body cue:** The multi-modal encoder in our model is based on a GPT-2-style Transformer architecture.
- **p. 3 / 3 Method - extractive body cue:** To address this limitation, we propose Long-VLA, a unified end-to-end VLA model that leverages phase-specific data more effectively.
- **p. 4 / 3 Method - extractive body cue:** Based on these observations, we propose an input-level adaptation strategy that dynamically adjusts visual inputs according to the current task phase.
- **Detected method headings:** 3 Method (p. 3); A.1 Definition of VLA Models (p. 12); C Model Details (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … ... | p. 4 (3 Method), p. 5 (3 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection ... | p. 5 (3 Method), p. 3 (3 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To enable training and inference within a unified end-to-end VLA framework, we extend the original action representation by adding a one-dimensional phase ... | p. 3 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive body cue:** Using the decomposition dataset, the model is trained with a single score matching loss that jointly supervises both the moving and interaction phases: LDiff = ...
- **p. 4 / 3 Method - extractive body cue:** As a result, the total training loss is formulated as: L = LDiff + αLGoal.
- **p. 3 / 3 Method - extractive body cue:** To assess the feasibility of phase-level decomposition, a preliminary study is conducted on the CALVIN dataset [40].
- **p. 5 / 3 Method - extractive body cue:** We employ a conditional diffusion model to generate actions at by progressively denoising from Gaussian noise, with the reverse process implemented using DDIM sampling: xt-1 ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3 Method), p. 4 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Static, Cam, Gripper, Multimodal, Transformer, Encoder, Noise, Detection, Action, masking, move, side, blue, button | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Static, Cam, Gripper, Multimodal, Transformer, Encoder, Noise, Detection, Action, masking | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Long-VLA, first, end-to-end, VLA, model, specifically, designed, longhorizon, robotic, manipulation | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | decomposition, dataset, model, trained, single, score, matching, loss, jointly, supervises | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Method - extractive body cue:** Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking ...
- **p. 5 / 3 Method - extractive body cue:** 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection input dt associated ...
- **p. 5 / 3 Method - extractive body cue:** To leverage the unlabeled play data, we follow a strategy similar to [52], where the future observation st+n is used as a visual goal in ...
- **p. 4 / 3 Method - extractive body cue:** Based on these observations, we propose an input-level adaptation strategy that dynamically adjusts visual inputs according to the current task phase.
- **p. 2 / 1 Introduction - extractive body cue:** Vision-Language-Action (VLA) models [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] have achieved widespread adoption in robotic control, owing to their ...
- **p. 3 / 3 Method - extractive body cue:** The interaction phase is handled by a pre-trained VLA model, while a separate moving policy is trained on on movementphase data.
- **p. 3 / 3 Method - extractive body cue:** Language instructions are augmented with movement-specific commands based on detected objects and locations.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | As described in Section 3.1, each language-annotated trajectory is decomposed into τ =  (sM t , aM t )t ∈[0, d], ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Method - extractive body cue:** Static Cam 𝒔𝒔𝒃𝒃 𝒕𝒕 Gripper Cam 𝒔𝒔𝒈𝒈𝒕𝒕 … … Multimodal Transformer Encoder … Noise 𝝈𝝈 𝛥𝛥𝑇𝑇 𝛥𝛥𝑅𝑅 𝑠𝑠𝑔𝑔 𝑠𝑠𝑝𝑝 Detection 𝒅𝒅𝒕𝒕 … Action 𝒂𝒂𝒕𝒕 masking ...
- **p. 3 / 3 Method - extractive body cue:** To enable training and inference within a unified end-to-end VLA framework, we extend the original action representation by adding a one-dimensional phase identifier sp, which ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Static, Cam, Gripper, Multimodal, Transformer, Encoder, Noise, Detection, Action, masking, move, side, blue, button, table, Decomposed, Dataset, Diffusion, Policy, Moving.
- **Relevant PDF headings:** 3 Method (p. 3); A.1 Definition of VLA Models (p. 12); C Model Details (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task. | p. 7 (4 Experiment), p. 6 (4 Experiment) |
| Action / skill decoding | In real-world robotic experiments, our method consistently outperforms the state-of-the-art algorithm π0 across the generalization task. | p. 7 (4 Experiment), p. 5 (4 Experiment) |
| Receding execution / feedback | As shown in Figure 4, our model achieves performance improvements in the D→D and ABCD→D of the L-CALVIN benchmark. | p. 6 (4 Experiment), p. 6 (4 Experiment) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of Long-VLA. (a) Task decomposition with aligned visual observations and language annotations. (b) Phase-aware masking enables the model to selectively attend to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Real-world Performance on Sorting. inputs, as demonstrated by its performance in the CALVIN environments. In real-world settings, this decision is further supported by ...
- **p. 7 / 4 Experiment - extractive body cue:** 4.4 Ablation Analyses We validate the key design elements of Long-VLA -decomposition strategy, input-level adaptation, and unified model-in Table 3.
- **p. 8 / 4 Experiment - extractive body cue:** Real (Sorting) Real (Cleaning) Sim (D-D) ✗ ✗ ✓ 2.3 1.4 4.11 ✓ ✗ ✓ 3.6 (1.3 ↑) 1.7 (0.3 ↑) 4.42 (0.31 ↑) ✓ ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 9: (a) Illustration of skill-chaining challenges like state mismatch in CALVIN benchmark. In the independent setting, each subtask starts from a state within the ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 6: Ablation on Input Modality on CALVIN(D-D). d denotes detection information, s denotes static camera views, g denotes gripper camera views. Setting Moving Interaction ...
- **p. 5 / 4 Experiment - extractive body cue:** RQ3: What are the key design components of our Long-VLA?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method), objective p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 5 (3 Method), temporal p. 5 (4 Experiment), p. 3 (3 Method), p. 1 (Abstract), p. 3 (3 Method), p. 5 (3 Method), p. 7 (4 Experiment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 3.2.2 Model Achitecture Long-VLA policy πθ(at / st, dt, g) predicts the action at conditioned on the current observation st, the detection input dt associated with st, and the latent ... (p. 5, 3 Method).
- **Objective/update evidence:** As a result, the total training loss is formulated as: L = LDiff + αLGoal. (p. 4, 3 Method).
- **Temporal/runtime evidence:** We select CALVIN as our simulation platform due to its focus on long-horizon tasks, and introduce LCALVIN, a new benchmark that extends task sequences from 5 to 10 steps based ... (p. 5, 4 Experiment).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
