# Method - Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.3. Untargeted Position-aware Attack)): Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient optimization and stable attack performance.

## Method Body Digest

- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient ...
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** By categorizing action values into discrete class labels, the model converts continuous probability outputs into discrete signals, this simplification facilitates quicker convergence and faster training ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** To define UADA's objective, we first identify the most distant action yi adv, which maximizes the discrepancy from the i-th DoF ground truth action yi.
- **p. 4 / 3.3. Untargeted Position-aware Attack - extractive PDF cue:** Recognizing the importance of Ap = DT(yp) in controlling the end-effector's path, we introduce a position-aware attack to disrupt the intended movement trajectory.
- **p. 4 / 3.4. Targeted Manipulation Attack - extractive PDF cue:** The objective of the targeted manipulation attack is: LTMA = E(x,y)∼X [CE(F(x + δ)I, yI T )], (6) where yI T = {yi T = ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** To exacerbate action discrepancies, we introduce the Untargeted Action Discrepancy Attack (UADA), which aims to maximize deviations in robot actions.
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** 2) are built on large language models integrated with visual encoders, enabling robots to interpret human instructions and process visual input from a camera to ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** This attack is based on the observation that larger robot actions usually correlate with intense physical movements, which, in turn, may amplify the potential for ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom.
- **p. 3 / 3. Methodology - extractive PDF cue:** Finally, we introduce the Normalized Action Discrepancy (NAD) metric in §3.5.
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** To exacerbate action discrepancies, we introduce the Untargeted Action Discrepancy Attack (UADA), which aims to maximize deviations in robot actions.

## Source Evidence Cues

- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient ...
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** By categorizing action values into discrete class labels, the model converts continuous probability outputs into discrete signals, this simplification facilitates quicker convergence and faster training ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** To define UADA's objective, we first identify the most distant action yi adv, which maximizes the discrepancy from the i-th DoF ground truth action yi.
- **p. 4 / 3.3. Untargeted Position-aware Attack - extractive PDF cue:** Recognizing the importance of Ap = DT(yp) in controlling the end-effector's path, we introduce a position-aware attack to disrupt the intended movement trajectory.
- **Detected method headings:** 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ... | p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.1. Preliminary) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | By categorizing action values into discrete class labels, the model converts continuous probability outputs into discrete signals, this simplification facilitates quicker convergence ... | p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To define UADA's objective, we first identify the most distant action yi adv, which maximizes the discrepancy from the i-th DoF ground ... | p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.3. Untargeted Position-aware Attack) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient ...
- **p. 4 / 3.4. Targeted Manipulation Attack - extractive PDF cue:** The objective of the targeted manipulation attack is: LTMA = E(x,y)∼X [CE(F(x + δ)I, yI T )], (6) where yI T = {yi T = ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** To define UADA's objective, we first identify the most distant action yi adv, which maximizes the discrepancy from the i-th DoF ground truth action yi.
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** To exacerbate action discrepancies, we introduce the Untargeted Action Discrepancy Attack (UADA), which aims to maximize deviations in robot actions.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | built, large, language, models, integrated, visual, encoders, enabling, robots, interpret, human, instructions, process, input | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | built, large, language, models, integrated, visual, encoders, enabling, robots, interpret | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Additionally, introduce, Geometry-Aware, Objective, considers, robot, movement, three-dimensional, space, characterized | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Instead, directly, misclassification, target, introduce, soft, attack, objective, capture, discrepancy | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Preliminary - extractive PDF cue:** 2) are built on large language models integrated with visual encoders, enabling robots to interpret human instructions and process visual input from a camera to ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** This attack is based on the observation that larger robot actions usually correlate with intense physical movements, which, in turn, may amplify the potential for ...
- **p. 4 / 3.4. Targeted Manipulation Attack - extractive PDF cue:** (7) We next calculate the applied action discrepancy di applied(x, y) = /DT(F(x)i) -DT(yi gt)/ to measure the deviation between the model's output and ground ...
- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive PDF cue:** Specifically, due to the physical action magnitude information contains in bin labels, we reweight the output probability F(x)i bins ∈R1×bins using normalized bin labels yi ...
- **p. 1 / 1. Introduction - extractive PDF cue:** A notable realization of this potential can be seen in Vision-Language-Action (VLA) models [16, 34, 73, 74], which integrate LVLMs into robotic systems to enable ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Adversarial Threats BV2 LIBERO Instruction: Put the bowl on the plate.
- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, we formulate an Action Discrepancy Objective aimed at maximizing the action discrepancy within VLA-based robotic systems.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | By steering the robot toward an adversarial target across successive time steps, our approach manipulates the trajectory and undermines task performance, ultimately ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We visualize the overall 3D trajectories and 2D trajectories of benign • and adversarial • scenarios at each time step to compare ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Each suite consists of 10 tasks, with each task executed for 50 trials, resulting in a total of 500 rollouts, following Kim ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3.1. Preliminary - extractive PDF cue:** By categorizing action values into discrete class labels, the model converts continuous probability outputs into discrete signals, this simplification facilitates quicker convergence and faster training ...
- **p. 6 / 4.2. Experiment Setup - extractive PDF cue:** Each suite consists of 10 tasks, with each task executed for 50 trials, resulting in a total of 500 rollouts, following Kim et al.
- **p. 6 / 4.2. Experiment Setup - extractive PDF cue:** Regarding the task execution evaluation, we take the maximum steps of each task suite in the LIBERO training dataset as the timeout failure condition to ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Instead, directly, misclassification, target, introduce, soft, attack, objective, capture, discrepancy, between, actions, ensuring, smooth, gradient, optimization, stable, performance, categorizing, action.
- **Relevant PDF headings:** 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The increased variability in real-world data, including environmental complexity, object diversity, and task difficulty, allows the robot more opportunities to generate larger ... | p. 6 (4.3. Main Result), p. 6 (4.2. Experiment Setup) |
| Action / skill decoding | Therefore, we adapt prior work in adversarial learning as one of our baseline methods [66]. | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Receding execution / feedback | Specifically, while attacking DoF1 and DoF1∼3 in the Simulation setup, UADA and UPA achieve NAD of 21.0% and 14.5%, significantly outperforming UMA ... | p. 6 (4.3. Main Result), p. 8 (4.3. Main Result) |

## Failure and Ablation Link

- **p. 6 / 4.2. Experiment Setup - extractive PDF cue:** Subsequently, we evaluate the performance of generated adversarial patches on victim models (i.e., OpenVLA LIBERO variants) trained on different tasks suites to rigorously prove the ...
- **p. 6 / 4.2. Experiment Setup - extractive PDF cue:** To evaluate the effectiveness of our methods, we craft adversarial patches using three distinct generating setups: Simulation Setting involves a model trained in a simulated ...
- **p. 8 / 4.3. Main Result - extractive PDF cue:** Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as well ...
- **p. 8 / 4.3. Main Result - extractive PDF cue:** (a) Impact of Inner-loop, (b) Impact of Patch Size and (c-f) the effect of four different defenses on failure rates. generated with UADA demonstrated the ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We then conduct diagnostic experiments (§4.4) to analyze the impact of key components.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ...
- **p. 6 / 4.3. Main Result - extractive PDF cue:** Both UADA and UPA effectively disrupt robot execution, yielding maximum average failure rates of 100% and 89.7%, respectively.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.3. Untargeted Position-aware Attack), objective p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack), temporal p. 4 (3.4. Targeted Manipulation Attack), p. 5 (4. Experiments), p. 6 (4.2. Experiment Setup), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3.1. Preliminary).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
