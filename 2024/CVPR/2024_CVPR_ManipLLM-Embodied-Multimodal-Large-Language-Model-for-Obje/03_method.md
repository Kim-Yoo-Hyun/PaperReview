# Method - ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.3. Sim-to-real Transfer), p. 3 (3.1. Fine-tuning Strategy), p. 3 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy)): Specifically, given the current test sample, we introduce an additional reasoning step to prompt the model to assess whether the predicted position can lead to a successful manipulation.

## Method Body Digest

- **p. 6 / 3.3. Sim-to-real Transfer - extractive body cue:** Specifically, given the current test sample, we introduce an additional reasoning step to prompt the model to assess whether the predicted position can lead to ...
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** 3.1.1 Model Architecture We adopt the MLLM, LLaMa-Adapter [38], as our backbone and follow its training strategy.
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** After aligning visual and text feature representation with the multi-modal projection module, LLaMa is required to conduct multi-modal understanding and give correct answers.
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** This is supervised under cross-entropy loss LA, enabling the model aware where of the object region can be manipulated and facilitating the model latter predict ...
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** In the simulator, when pre-collecting training data, if the manipulation is successful, we record the RGB image and the corresponding end-effector pose, which are used ...
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** During inference, we adopt chain-of-thought reasoning to simulate the model to generate a precise initial contact end-effector pose interpretively.
- **p. 5 / 3.2. Active Impedance Adaptation Policy - extractive body cue:** The chain-of-thought inference process of ManipLLM. trast with leveraging a model to predict each following pose, such a heuristic policy is much more efficient.
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** This is supervised by the unmasked answer under cross-entropy loss LM to stimulate the model's ability in pose prediction.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy.
- **p. 2 / 1. Introduction - extractive body cue:** Experiments show that in the simulator, our method achieves a promising manipulation success rate across 30 categories.

## Source Evidence Cues

- **p. 6 / 3.3. Sim-to-real Transfer - extractive body cue:** Specifically, given the current test sample, we introduce an additional reasoning step to prompt the model to assess whether the predicted position can lead to ...
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** 3.1.1 Model Architecture We adopt the MLLM, LLaMa-Adapter [38], as our backbone and follow its training strategy.
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** After aligning visual and text feature representation with the multi-modal projection module, LLaMa is required to conduct multi-modal understanding and give correct answers.
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** This is supervised under cross-entropy loss LA, enabling the model aware where of the object region can be manipulated and facilitating the model latter predict ...
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** In the simulator, when pre-collecting training data, if the manipulation is successful, we record the RGB image and the corresponding end-effector pose, which are used ...
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** During inference, we adopt chain-of-thought reasoning to simulate the model to generate a precise initial contact end-effector pose interpretively.
- **p. 5 / 3.2. Active Impedance Adaptation Policy - extractive body cue:** The chain-of-thought inference process of ManipLLM. trast with leveraging a model to predict each following pose, such a heuristic policy is much more efficient.
- **Detected method headings:** 2.2. Multimodal Large Language Models (p. 3); 3. Method (p. 3); 3.2. Active Impedance Adaptation Policy (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Specifically, given the current test sample, we introduce an additional reasoning step to prompt the model to assess whether the predicted position ... | p. 6 (3.3. Sim-to-real Transfer), p. 3 (3.1. Fine-tuning Strategy) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 3.1.1 Model Architecture We adopt the MLLM, LLaMa-Adapter [38], as our backbone and follow its training strategy. | p. 3 (3.1. Fine-tuning Strategy), p. 3 (3.1. Fine-tuning Strategy) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | After aligning visual and text feature representation with the multi-modal projection module, LLaMa is required to conduct multi-modal understanding and give correct ... | p. 3 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** This is supervised under cross-entropy loss LA, enabling the model aware where of the object region can be manipulated and facilitating the model latter predict ...
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** This is supervised by the unmasked answer under cross-entropy loss LM to stimulate the model's ability in pose prediction.
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** Updating the learning process in the simulator might lead to a loss of MLLMs's powerful object category identification ability and robust generalization capability.
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** During training, the aforementioned tasks are trained simultaneously under the total objective function: L = LA+LM+LF .
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** 2, we design fine-tuning tasks at the category level, region level, and pose level, allowing the model to progressively and reasonably predict poses for object-centric ...
- **p. 6 / 3.3. Sim-to-real Transfer - extractive body cue:** To determine which parameters to update for pose prediction during TTA, we analyze the outcomes of the reasoning steps during inference in Fig.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 6 (3.3. Sim-to-real Transfer).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | deal, difficulties, policy, aims, adjust, interact, things, impedance, force, feedback, handle, different, scenarios, effectively | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | deal, difficulties, policy, aims, adjust, interact, things, impedance, force, feedback | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Meanwhile, real-world, experiments, strong, generalization, ability, without, TTA, strategy, simulator | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | supervised, under, cross-entropy, loss, enabling, model, aware, where, object, region | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.2. Active Impedance Adaptation Policy - extractive body cue:** To deal with these difficulties, the proposed policy aims to adjust how we interact with things based on impedance force feedback, which can handle different ...
- **p. 5 / 3.2. Active Impedance Adaptation Policy - extractive body cue:** Thus, the best forward direction is generated as the following to determine the current end-effector's pose: dopt, opt = arg max j∈{0,1,...,N} ∥δj∥ By doing ...
- **p. 1 / 1. Introduction - extractive body cue:** Given the text prompt, RGB image, and depth map inputs, we obtain 3D contact point (x, y, z).
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** In the simulator, when pre-collecting training data, if the manipulation is successful, we record the RGB image and the corresponding end-effector pose, which are used ...
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** Inspired by Flowbot3D [6], we divide the action type of the object part into "REVOLUTE" and "PRISMATIC", and collect the affordance map in the simulator ...
- **p. 2 / 1. Introduction - extractive body cue:** This method relies on force feedback generated along the axes and the object to adaptively adjust the direction and predict the trajectory.
- **p. 2 / 1. Introduction - extractive body cue:** action trajectories (i.e. end-effector trajectories) [4, 40] poses challenges in generalization due to minimal low-level action samples in their pretraining data.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | 4, the reasoning process follows the three steps that are consistent with the training tasks. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | For example, when trying to open a door, the best way to do it often involves moving it in a very specific ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We finetuned LLaMA-Adapter [38] on a 40G A100 GPU for 10 epochs, with an epoch costs around an hour. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** 3.1.1 Model Architecture We adopt the MLLM, LLaMa-Adapter [38], as our backbone and follow its training strategy.
- **p. 4 / 3.1. Fine-tuning Strategy - extractive body cue:** In the simulator, when pre-collecting training data, if the manipulation is successful, we record the RGB image and the corresponding end-effector pose, which are used ...
- **p. 5 / 3.1. Fine-tuning Strategy - extractive body cue:** During inference, we adopt chain-of-thought reasoning to simulate the model to generate a precise initial contact end-effector pose interpretively.
- **p. 5 / 3.2. Active Impedance Adaptation Policy - extractive body cue:** The chain-of-thought inference process of ManipLLM. trast with leveraging a model to predict each following pose, such a heuristic policy is much more efficient.
- **p. 6 / 4.1. Training Details - extractive body cue:** It includes pre-trained CLIP [25] as the visual encoder, 7B LLaMA [26] model as the decoder, and multi-modal projection module of 32 transformer layers.
- **p. 3 / 3.1. Fine-tuning Strategy - extractive body cue:** While text prompts T are encoded into a text feature using the tokenizer of the pre-trained LLaMa [26].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, given, current, test, sample, introduce, additional, reasoning, step, prompt, model, assess, whether, predicted, position, lead, successful, manipulation, Architecture, adopt.
- **Relevant PDF headings:** 2.2. Multimodal Large Language Models (p. 3); 3. Method (p. 3); 3.2. Active Impedance Adaptation Policy (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 5, the devised TTA strategy addresses discrepancies arising from real-world hardware configurations. | p. 8 (4.4. Real-world Evaluation), p. 6 (4.1. Training Details) |
| Action / skill decoding | Table 1. Comparisons of our method against baseline methods. used to determine end-effector pose. Our current experimental settings involve training on a ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Receding execution / feedback | It thus significantly improves the manipulation success rate by +7%. | p. 7 (4.3. Ablation and Analysis), p. 6 (4.1. Training Details) |

## Failure and Ablation Link

- **p. 7 / 4.3. Ablation and Analysis - extractive body cue:** To elucidate the contribution and effectiveness of individual modules within our approach, we conduct extensive ablation studies.
- **p. 8 / 4.3. Ablation and Analysis - extractive body cue:** In the last row of Table 2 w/o AIA., we employ a straightforward control policy, which operates by moving directly to the desired position under ...
- **p. 7 / 4.3. Ablation and Analysis - extractive body cue:** Ablation analysis of each training task in the training paradigm and strategies in inference. fication, the first prompt in Fig.
- **p. 8 / 4.3. Ablation and Analysis - extractive body cue:** For comparison, we ask the model to generate the final pose prediction directly without the thinking process in Fig.
- **p. 8 / 4.4. Real-world Evaluation - extractive body cue:** Additionally, its head is relatively short, which presents a collision risk when interacting with the protruding handle.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.3. Sim-to-real Transfer), p. 3 (3.1. Fine-tuning Strategy), p. 3 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), objective p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 3 (3.1. Fine-tuning Strategy), p. 6 (3.3. Sim-to-real Transfer), temporal p. 5 (3.1. Fine-tuning Strategy), p. 5 (3.2. Active Impedance Adaptation Policy), p. 6 (3.3. Sim-to-real Transfer), p. 6 (3.3. Sim-to-real Transfer).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
