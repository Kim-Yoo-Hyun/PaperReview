# Method - Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p150.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p150.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 18 (B. Pose Estimation Implementation)): where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use the mean

## Method Body Digest

- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use the mean
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** We then use this feature as input for the pose regressor MLP.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** We then inonicalize the point cloud using the same PCA algorithm, ensuring that the relative 6D pose of the same component remains consistent.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which ...
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** 3) Hyperparameters in Training of Pose Estimation: We train our pose estimation model on a single NVIDIA A100 40GB GPU with a batch size of ...
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** 3) Heuristic Grasping Policy: For general grasping tasks, pre-trained models such as GraspNet{11] are commonly used to generate grasping poses.
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** 1) Loss Functions for Pose Estimation:
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** Chamfer Distance Loss: This loss function minimizes the holistic distance between each point in the predicted and ground truth point clouds.

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- **p. 2 / I. INrRopuction - extractive body cue:** In this paper, we propose Manual2Skill, a novel robot learn
- **p. 2 / I. INrRopuction - extractive body cue:** + We propose Manual2Skill, a novel framework that leverages VLM to learn robotic skills from manuals, enabling 4 generalizable assembly pipeline for IKEA furniture

## Source Evidence Cues

- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use the mean
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** We then use this feature as input for the pose regressor MLP.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** We then inonicalize the point cloud using the same PCA algorithm, ensuring that the relative 6D pose of the same component remains consistent.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which ...
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** 3) Hyperparameters in Training of Pose Estimation: We train our pose estimation model on a single NVIDIA A100 40GB GPU with a batch size of ...
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** 3) Heuristic Grasping Policy: For general grasping tasks, pre-trained models such as GraspNet{11] are commonly used to generate grasping poses.
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** 1) Loss Functions for Pose Estimation:
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use ... | p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | We then use this feature as input for the pose regressor MLP. | p. 15 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We then inonicalize the point cloud using the same PCA algorithm, ensuring that the relative 6D pose of the same component remains ... | p. 17 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** Chamfer Distance Loss: This loss function minimizes the holistic distance between each point in the predicted and ground truth point clouds.
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** 1) Loss Functions for Pose Estimation:
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** Second, we remove the permutation mechanism for equivalent parts(Equation (12).
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** Otherwise, such masks are costly in real-world scenarios.
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** For furniture with 13 ‘or more parts (6 items), we performed manual verification due to the computational cost of permutations.
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** ‘TABLE V: Optimizer Corresponding to Each Component
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 14 (B. Pose Estimation Implementation), p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 16 (B. Pose Estimation Implementation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | triplet, format, enhances, interpretability, ensures, consistency, structuring, outputs, same, data, Image, Set, Text, Instructions | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | triplet, format, enhances, interpretability, ensures, consistency, structuring, outputs, same, data | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | present, Manual2Skill, novel, framework, enables, robots, perform, complex, assembly, tasks | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Chamfer, Distance, Loss, function, minimizes, holistic, between, point, predicted, ground | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2. Per-step Assembly Pose Estimation - extractive body cue:** This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set and Text Instructions ...
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which ...
- **p. 2 / B. VLM Guided Robot Learning - extractive body cue:** A potential direction is the development of the Vision Language ‘Action Model (VLA Model) that can generate actions based on the vision and language inputs ...
- **p. 3 / A. VLM Guided Hierarchical Assembly Graph Generation - extractive body cue:** All instructions incorporate in-context learning examples, specifying the required output format-be it JSON, Python code, or natural language. ‘This structure is essential to our malt ...
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** 12: The input consists of the scene image, the comesponding assembly steps from the manual, and the text instruction from prompt 3.b).
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** We show the quantitative results in Table VI and the qualitative results in Figure 10, First, we remove the image input and only use the ...
- **p. 1 / I. INrRopuction - extractive body cue:** This abstraction makes it difficult for robots to comprehend such instructions and derive actionable manipulation strategies (32, 49, 48].
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Manually inspecting each assembly plan reveals common failure modes: the VLM frequently misidentifies parts (e.g. labeling a bench seat as a "tabletop"), ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | ‘we need to align the camera frame in the manual page image, denoted as Pp... with the real-world camera frame, denoted aS ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We perform each task over 10 trials with varying initial 3D part poses. | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** 3) Hyperparameters in Training of Pose Estimation: We train our pose estimation model on a single NVIDIA A100 40GB GPU with a batch size of ...
- **p. 18 / B. Pose Estimation Implementation - extractive body cue:** 3) Heuristic Grasping Policy: For general grasping tasks, pre-trained models such as GraspNet{11] are commonly used to generate grasping poses.
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** 3) Hyperparameters in Training of Pose Estimation: We train our pose estimation model on a single NVIDIA A100 40GB GPU with a batch size of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** where, denotes, trace, matrix, transpose, Translation, MSE, Loss, Following, mean, then, feature, input, pose, regressor, MLP, inonicalize, point, cloud, same.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm ... | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Action / skill decoding | We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world ... | p. 9 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation) |
| Receding execution / feedback | We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world ... | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |

## Failure and Ablation Link

- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** To evaluate the effectiveness of each component in our pipeline, we conduct an ablation study on the chair category.
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** 1) Excluding Manual Pages Entirely: To explore whether «4 modified framework could perform the task without manual images by relying on the VLM's existing priors, ...
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** 10: Qualitative Results of Ablations.
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** E, Assembly Graph Generation Ablation Studies
- **p. 19 / B. Pose Estimation Implementation - extractive body cue:** Therefore, we report Stage If results as an intermediate measure of how effectively our approach aligns manual images with real components.
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** 3) We place a part that is not near any other components, causing it to suspend in midair after each assembly step.
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** Following this sequence and the predicted 6 poses of each component, we implement RRT-Connect [26] in simulation to plan feasible ‘motion paths for the 3D ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 18 (B. Pose Estimation Implementation), objective p. 14 (B. Pose Estimation Implementation), p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 16 (B. Pose Estimation Implementation), p. 16 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), temporal p. 16 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation), p. 5 (7 WO'T ry), p. 2 (I. INrRopuction), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** A potential direction is the development of the Vision Language ‘Action Model (VLA Model) that can generate actions based on the vision and language inputs [2, 23, 3, 44]. (p. 2, B. VLM Guided Robot Learning).
- **Objective/update evidence:** 1) Loss Functions for Pose Estimation: (p. 14, B. Pose Estimation Implementation).
- **Temporal/runtime evidence:** Manually inspecting each assembly plan reveals common failure modes: the VLM frequently misidentifies parts (e.g. labeling a bench seat as a "tabletop"), generates physically plausible sequences (e.g., attaching two chair ... (p. 16, B. Pose Estimation Implementation).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
