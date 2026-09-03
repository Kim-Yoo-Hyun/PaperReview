# Method - ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction)): A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: We perform max-pooling over the ...

## Method Body Digest

- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: ...
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** All tokens are concatenated and passed through an MLP head to predict rotation, gripper, and collision actions.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** This global-local fusion allows the model to combine overall scene understanding with fine spatial precision, enabling accurate and safe manipulation in complex environments.
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** The translation target is determined as \ m ath bf {t} ^* = \arg \max _{\mathbf {g} \in \mathcal {G}} S(\mathbf {g}) .
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...
- **p. 2 / 1. Introduction - extractive body cue:** This closed-loop, coarse-to-fine perception-action pipeline allows ActiveVLA to dynamically adapt its sensory inputs and maintain high effectiveness across complex, multi-step, and long-horizon manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose ActiveVLA, a novel vision-language-action framework that explicitly integrates active perception into robotic manipulation.
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...

## Source Evidence Cues

- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: ...
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** All tokens are concatenated and passed through an MLP head to predict rotation, gripper, and collision actions.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** This global-local fusion allows the model to combine overall scene understanding with fine spatial precision, enabling accurate and safe manipulation in complex environments.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • ... | p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps. | p. 5 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | All tokens are concatenated and passed through an MLP head to predict rotation, gripper, and collision actions. | p. 6 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** The translation target is determined as \ m ath bf {t} ^* = \arg \max _{\mathbf {g} \in \mathcal {G}} S(\mathbf {g}) .
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | framework, equips, robots, active, perception, capabilities, enabling, adaptive, viewpoint, selection, zoomin, mechanisms, precise, fine-grained | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | framework, equips, robots, active, perception, capabilities, enabling, adaptive, viewpoint, selection | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, summarized, Active, Perception, Vision-Language-Action, Models, ActiveVLA, novel, address, limitation | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | translation, target, determined, mathbf, mathcal, hierarchical, feature, fusion, module, then | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...
- **p. 2 / 1. Introduction - extractive body cue:** This closed-loop, coarse-to-fine perception-action pipeline allows ActiveVLA to dynamically adapt its sensory inputs and maintain high effectiveness across complex, multi-step, and long-horizon manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action.
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: ...
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** All tokens are concatenated and passed through an MLP head to predict rotation, gripper, and collision actions.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | This closed-loop, coarse-to-fine perception-action pipeline allows ActiveVLA to dynamically adapt its sensory inputs and maintain high effectiveness across complex, multi-step, and long-horizon ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We evaluate ActiveVLA on three simulation benchmarks for long-horizon and finegrained manipulation. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We report the success rate (%) and inference time (s) over 100 trials. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4.2. Ablation Study - extractive body cue:** We report the success rate (%) and inference time (s) over 100 trials.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** hierarchical, feature, fusion, module, then, integrates, global, local, context, predict, rotation, gripper, state, binary, collision, flag, Encoding, perform, max-pooling, over.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks. | p. 6 (4. Experiments), p. 7 (4.1. Experimental Results) |
| Action / skill decoding | We compare ActiveVLA with state-of-the-art baselines. | p. 6 (4. Experiments), p. 7 (4.1. Experimental Results) |
| Receding execution / feedback | Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of ... | p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results) |

## Failure and Ablation Link

- **p. 7 / 4.1. Experimental Results - extractive body cue:** Results are reported as mean success rates without confidence intervals.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** Overall, ActiveVLA surpasses BridgeVLA in most categories, confirming its stronger visual generalization and invariant representation learning capability.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on key components. We report the suc- cess rate (%) and inference time (s) over 100 trials. A-VS (Active View Selection) ...
- **p. 6 / 4. Experiments - extractive body cue:** Our ActiveVLA adopts the pretrained VLM backbone from BridgeVLA [33], built on PaliGemma [3] with a SigLIP encoder [63] and Gemma decoder [53], pre-trained on ...
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 6 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction), objective p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction), temporal p. 2 (1. Introduction), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 1 (Abstract), p. 2 (Abstract), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA designs a novel coarse-to-fin ... (p. 3, 1. Introduction).
- **Objective/update evidence:** After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps. (p. 5, 3.3. 3D Action Prediction).
- **Temporal/runtime evidence:** We evaluate ActiveVLA on three simulation benchmarks for long-horizon and finegrained manipulation. (p. 6, 4. Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
