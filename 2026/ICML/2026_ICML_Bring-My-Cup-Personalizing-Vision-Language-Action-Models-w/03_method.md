# Method - Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fm6Z3wfTae; PDF retrieval source: https://openreview.net/pdf/68e389cf48e82eb16b32f886139baddd9122f43d.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation)): We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V v=1 denotes multi-view RGB images ...

## Method Body Digest

- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We formulate this not merely as prompting, but as searching for a visual intervention that maximizes policy success.
- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** By explicitly overlaying the grounded mask with canonical visual attributes (e.g., solid colors), we bias the inputs toward simple attribute-language patterns (e.g., color adjectives) that ...
- **p. 2 / 1. Introduction - extractive body cue:** VAP therefore couples (1) Grounding, which localizes the user's object using a small set of reference images, with (2) Visual Prompting, which overlays a mask-aligned ...
- **p. 1 / 1. Introduction - extractive body cue:** However, general-purpose policies, such as VisionLanguage-Action (VLA) models, typically fail to meet this requirement.
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.

## Design Rationale

- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.

## Source Evidence Cues

- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where ... | p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation. | p. 4 (3.1. Problem Formulation) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where ... | p. 4 (3.1. Problem Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We formulate this not merely as prompting, but as searching for a visual intervention that maximizes policy success.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes, multi-view, RGB, images, cameras | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | main, contributions, follows, Personal, Object, Manipulation, introduce, personalization, task, VLAs | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | While, exact, gradientbased, optimization, would, computationally, prohibitive, VAP, zero-shot, approximation | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...
- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** By explicitly overlaying the grounded mask with canonical visual attributes (e.g., solid colors), we bias the inputs toward simple attribute-language patterns (e.g., color adjectives) that ...
- **p. 2 / 1. Introduction - extractive body cue:** VAP therefore couples (1) Grounding, which localizes the user's object using a small set of reference images, with (2) Visual Prompting, which overlays a mask-aligned ...
- **p. 1 / 1. Introduction - extractive body cue:** However, general-purpose policies, such as VisionLanguage-Action (VLA) models, typically fail to meet this requirement.
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 3 / 1. Introduction - extractive body cue:** Personalizing Vision-Language-Action Models with Visual Attentive Prompting signed to rigorously test instance-level identification among distractors (Figure 2, Top).
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The initialization runs once per episode, while tracking and policy inference execute at every control step. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | During online control, the computational bottleneck remains the VLA policy inference itself (0.20 s/step). | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | VAP integrates grounding with spatio-temporal memory to maintain stable target identity throughout the action sequence. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | During online control, the computational bottleneck remains the VLA policy inference itself (0.20 s/step). | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** We fine-tune the base checkpoint π0.5 solely for environment adaptation, using generic data that explicitly excludes personal objects and personalized instructions.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes, multi-view, RGB, images, cameras, represents, proprioceptive, state, While, exact, gradientbased.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware. | p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks) |
| Action / skill decoding | VAP outperforms other baselines across all scenarios. | p. 7 (5.1. Experimental Setup), p. 8 (5.3. Results on Simulation Benchmarks) |
| Receding execution / feedback | VAP improves average SR from 18.8% to 58.8%, significantly outperforming soft/hard prompts which remain in the 27.5-31.2% range. | p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup) |

## Failure and Ablation Link

- **p. 43 / Figure/Table caption - extractive body cue:** Table 14. Ablation of instruction rewriting on single-view Personalized-SIMPLER. "Mask-only" removes rewriting, while "Rewrite- only" removes the visual highlight but keeps the same tint-color rewrite ...
- **p. 45 / Figure/Table caption - extractive body cue:** Table 17. Ablation of visual prompt design on single-view Personalized-SIMPLER. The top block compares VAP's mask-aligned tint against alternative visual prompting strategies, including approaches adopted ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** Track 1 evaluates visual matching under unseen personal objects, and Track 2 aggregates performance across systematic visual variants.
- **p. 7 / 5.2. Baselines - extractive body cue:** We extract textual descriptions from the reference images and use an LLM to append these details to the instruction (generating Short or Long variants).
- **p. 8 / 5.3. Results on Simulation Benchmarks - extractive body cue:** Crucially, these gains persist under variant aggregation (SR 58.2%, CMR 87.3%), confirming robustness to visual perturbations.
- **p. 8 / 5.2. Baselines - extractive body cue:** Personalizing Vision-Language-Action Models with Visual Attentive Prompting These three baselines isolate distinct hypotheses about whether personalization can be achieved without retraining: whether VLAs already handle ...
- **p. 9 / 5.6. Efficiency of VAP - extractive body cue:** This confirms that VAP enhances performance without compromising the real-time responsiveness of the robotic system.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation), objective p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation), temporal p. 8 (5.3. Results on Simulation Benchmarks), p. 9 (5.6. Efficiency of VAP), p. 9 (5.7. Comparison to Visual Prompting Alternatives), p. 4 (3. Visual Attentive Prompting), p. 5 (3.3. Grounding and Prompting Details), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
