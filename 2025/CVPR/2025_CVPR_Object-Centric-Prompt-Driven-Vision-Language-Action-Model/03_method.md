# Method - Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 3 (3.3.1. Model Architecture), p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning), p. 5 (3.4.2. Interaction Strategy)): Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual and linguistic input, making sure ...

## Method Body Digest

- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** The objective of the model is to generate an action 푎0 = (푎푝′ 0 , 푎푍 0 , 푎푌 0 , 푎푀 0 ), where ...
- **p. 3 / 3.3.1. Model Architecture - extractive PDF cue:** Observing the robust language understanding and visual processing capabilities of Vision Language Action Models (VLAs) and inspired by their applications in prior robotic manipulation tasks ...
- **p. 5 / 3.4.1. Model Inference - extractive PDF cue:** Given the visual and language input, the model outputs the predicted action 푎0.
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...
- **p. 5 / 3.4.2. Interaction Strategy - extractive PDF cue:** If provided with 푎푚 0 , we then follow the predicted moving direction 푎푀 0 to determine the subsequent movements after contact.
- **p. 6 / 3.4.2. Interaction Strategy - extractive PDF cue:** Meanwhile, regarding each key-frame step as compositions, we can group them into arbitrary combinations, enabling the model to handle diverse manipulation tasks.
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** The aforementioned losses are trained simultaneously under the total objective function: L = 휆1 ∗L푇+휆2 ∗L푂+휆3 ∗L푃.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey the task objectives ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our experimental setup includes a diverse range of manipulation tasks, both familiar and novel, where our method achieves a promising success rate in manipulation.
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...

## Source Evidence Cues

- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** The objective of the model is to generate an action 푎0 = (푎푝′ 0 , 푎푍 0 , 푎푌 0 , 푎푀 0 ), where ...
- **p. 3 / 3.3.1. Model Architecture - extractive PDF cue:** Observing the robust language understanding and visual processing capabilities of Vision Language Action Models (VLAs) and inspired by their applications in prior robotic manipulation tasks ...
- **p. 5 / 3.4.1. Model Inference - extractive PDF cue:** Given the visual and language input, the model outputs the predicted action 푎0.
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...
- **p. 5 / 3.4.2. Interaction Strategy - extractive PDF cue:** If provided with 푎푚 0 , we then follow the predicted moving direction 푎푀 0 to determine the subsequent movements after contact.
- **p. 6 / 3.4.2. Interaction Strategy - extractive PDF cue:** Meanwhile, regarding each key-frame step as compositions, we can group them into arbitrary combinations, enabling the model to handle diverse manipulation tasks.
- **Detected method headings:** 3. Method (p. 3); 3.3.1. Model Architecture (p. 3); 3.3.2. Policy Learning (p. 3); 3.4.1. Model Inference (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of ... | p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The objective of the model is to generate an action 푎0 = (푎푝′ 0 , 푎푍 0 , 푎푌 0 , 푎푀 ... | p. 3 (3.1. Problem Formulation), p. 3 (3.3.1. Model Architecture) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Observing the robust language understanding and visual processing capabilities of Vision Language Action Models (VLAs) and inspired by their applications in prior ... | p. 3 (3.3.1. Model Architecture), p. 5 (3.4.1. Model Inference) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** The aforementioned losses are trained simultaneously under the total objective function: L = 휆1 ∗L푇+휆2 ∗L푂+휆3 ∗L푃.
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** We formulate pose prediction as a classification task by discretizing the continuous numbers in the normalized 3D direction vector into 100 discrete bins [-50,50], with ...
- **p. 3 / 3.1. Problem Formulation - extractive PDF cue:** The objective of the model is to generate an action 푎0 = (푎푝′ 0 , 푎푍 0 , 푎푌 0 , 푎푀 0 ), where ...
- **p. 3 / 3.3.2. Policy Learning - extractive PDF cue:** This gradual progression enables the model to develop a deeper understanding of the physical significance 27640
- **p. 6 / 3.4.2. Interaction Strategy - extractive PDF cue:** The benefit of this approach revolves around breaking down the complexity of long-horizon tasks and allowing us to optimize the success rate of each key-frame ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 4 (3.3.2. Policy Learning).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, visual, language, input, model, outputs, predicted, action, Therefore, introduce, following, losses, guide, policy | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Given, visual, language, input, model, outputs, predicted, action, Therefore, introduce | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, employing, sequence, key-frames, presented, prompts, explicitly, convey | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | aforementioned, losses, trained, simultaneously, under, total, objective, function, formulate, pose | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.4.1. Model Inference - extractive PDF cue:** Given the visual and language input, the model outputs the predicted action 푎0.
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Execution Input end effector pose: z-axis y-axis contact point t1 t2 CrayonRobo(ours) t1 t1 t2 t2 initial state end state next moving direction: RT-trajectory t ...
- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** To establish an explicit connection between the input 2D directional prompt and the output 3D directions, we introduce a projection loss designed to guide their ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Since key-frames represent important or bottleneck steps of the gripper during the task execution [18, 19, 26, 46, 58], we propose CrayonRobo, an approach that ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Based on the input goal prompt, the model determines the 6 DoF contact pose, enabling it to interact with the object as required.
- **p. 3 / 3.2. Data Collection - extractive PDF cue:** These are then served as information embedded in the input language prompt.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For the long-horizon tasks, we leverage a sequence of keyframes with visual prompts to serve as high-level planning, with each frame representing ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | In summary, our contributions are as follows: • 1) We propose employing a sequence of key-frames presented with prompts to explicitly convey ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | The model is finetuned for 20 epochs using key frames and the corresponding predicted 3D poses from successful trials in the previous ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.3.2. Policy Learning - extractive PDF cue:** Therefore, we introduce the following losses to guide the policy training: Text Supervision Loss L푇: This loss ensures the effective alignment of the model's visual ...
- **p. 3 / 3.3.1. Model Architecture - extractive PDF cue:** This approach aims to preserve the inherent existing pre-trained knowledge, particularly in simto-real transfer, while enhancing the model's ability to comprehend visual prompts and perform ...
- **p. 3 / 3.3.1. Model Architecture - extractive PDF cue:** Simultaneously, text prompts 푃are encoded into text features using LLaMa's pre-trained tokenizer [51].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Therefore, introduce, following, losses, guide, policy, training, Text, Supervision, Loss, ensures, effective, alignment, model, visual, linguistic, input, making, sure, output.
- **Relevant PDF headings:** 3. Method (p. 3); 3.3.1. Model Architecture (p. 3); 3.3.2. Policy Learning (p. 3); 3.4.1. Model Inference (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Simulator visualizations are shown in the left of Figure 4, illustrating the prompt input, the robot's contact state with the object, and ... | p. 6 (4.2. Comparisons with Baselines), p. 6 (4.1. Setup Details) |
| Action / skill decoding | For automatically generated prompts, the results are 0.64/0.62 on seen and unseen tasks, still outperforming the baselines. | p. 6 (4.2. Comparisons with Baselines), p. 7 (4.3. Ablation Study) |
| Receding execution / feedback | Beginning with Ex1, where only a 2D position prompt is provided, the model achieves impressive performance with scores of 0.42/0.37. | p. 6 (4.3. Ablation Study), p. 8 (4.3.2. Tolerance Analysis of Prompt Noise) |

## Failure and Ablation Link

- **p. 6 / 4. Experiment - extractive PDF cue:** In our experiments, we mainly focus on exploring the following questions: • Section 4.3.1: What is the effect of different types of prompts on model ...
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Additionally, to investigate the differential effects of visual and language prompts, in the last row of Table 2, we enable the model to learn from ...
- **p. 8 / 4.3.2. Tolerance Analysis of Prompt Noise - extractive PDF cue:** Ablation experiments regarding the effectiveness of each loss and failure case analysis are shown in Appendix.5 and Appendix.6.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation Study. dict rotation given the same pixel coordinate, which results in lower scores of 0.35/0.31. This shows even without direc- tional prompts, ...
- **p. 8 / 4.4. Real-world Experiment - extractive PDF cue:** 3, we further explore whether it is possible to fine-tune the model using prompts provided during the first set of executions for a specific task, ...
- **p. 6 / 4.3. Ablation Study - extractive PDF cue:** Analysis on The Effect of Different Types of Prompt In Table 2 Ex1-Ex3, since our model is able to handle various input patterns thanks to ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. We design training pairs that convey varying levels of information to enable the model to comprehend each type of prompt and introduce loss ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 3 (3.3.1. Model Architecture), p. 5 (3.4.1. Model Inference), p. 4 (3.3.2. Policy Learning), p. 5 (3.4.2. Interaction Strategy), objective p. 4 (3.3.2. Policy Learning), p. 4 (3.3.2. Policy Learning), p. 3 (3.1. Problem Formulation), p. 3 (3.3.2. Policy Learning), p. 6 (3.4.2. Interaction Strategy), temporal p. 5 (3.4.2. Interaction Strategy), p. 2 (1. Introduction), p. 6 (3.4.2. Interaction Strategy), p. 6 (3.4.2. Interaction Strategy), p. 1 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
