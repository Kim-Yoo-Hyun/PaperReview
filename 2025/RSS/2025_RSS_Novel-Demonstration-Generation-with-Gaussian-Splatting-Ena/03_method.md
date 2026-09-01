# Method - Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p146.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p146.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (A. Generalizable Policy in Robot Manipulation), p. 6 (C. Policy Training), p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY)): Instead of adopting generalizable policy architecture, auxiliary learning objectives ‘and powerful foundation models, our work is concentrated on generating high-quality, diverse, and realistic data to instill, generalization abilities ...

## Method Body Digest

- **p. 2 / A. Generalizable Policy in Robot Manipulation - extractive body cue:** Instead of adopting generalizable policy architecture, auxiliary learning objectives ‘and powerful foundation models, our work is concentrated on generating high-quality, diverse, and realistic data to ...
- **p. 6 / C. Policy Training - extractive body cue:** The latent of images and robot state is fed into a transformer encoder.
- **p. 6 / C. Policy Training - extractive body cue:** We employ a modem, widely adopted transformer-based architecture [18, 51, 38, 55] to serve as the policy network, which is detailed in Appendix C.
- **p. 2 / B. Data Augmentation for Policy Learning - extractive body cue:** Given limited training data, data augmentation emerges as a way to improve the robustness of the policy.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** With all the Gaussian models ready, we generate novel demonstrations and perform data augmentation in terms of object
- **p. 3 / IV. METHODOLOGY - extractive body cue:** To generate high-fidelity and diverse data from a single expert trajectory, we present RoboSplat, a novel demonstration generation approach based on 3DGS.
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Finally, a visuomotor policy is trained on the augmented demonstrations and directly deployed on real robots, as detailed in Sec.
- **p. 5 / A. Reconstruction and Preprocessing - extractive body cue:** The camera extrinsies are optimized through gradient descent, with the optimization objective:

## Design Rationale

- **p. 3 / C. Gaussian planting in Roboties - extractive body cue:** Our method enables autonomous editing of the reconstructed scene to generate diverse demonstrations with various configurations.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** To generate high-fidelity and diverse data from a single expert trajectory, we present RoboSplat, a novel demonstration generation approach based on 3DGS.
- **p. 2 / 1. INrRopucTION - extractive body cue:** Thanks t0 its explicit representation of the scene, 3DGS enables interpretable editing ofthe reconstructed scene, which paves the way for generating novel manipulation configurations, Furthermore, ...

## Source Evidence Cues

- **p. 2 / A. Generalizable Policy in Robot Manipulation - extractive body cue:** Instead of adopting generalizable policy architecture, auxiliary learning objectives ‘and powerful foundation models, our work is concentrated on generating high-quality, diverse, and realistic data to ...
- **p. 6 / C. Policy Training - extractive body cue:** The latent of images and robot state is fed into a transformer encoder.
- **p. 6 / C. Policy Training - extractive body cue:** We employ a modem, widely adopted transformer-based architecture [18, 51, 38, 55] to serve as the policy network, which is detailed in Appendix C.
- **p. 2 / B. Data Augmentation for Policy Learning - extractive body cue:** Given limited training data, data augmentation emerges as a way to improve the robustness of the policy.
- **p. 3 / IV. METHODOLOGY - extractive body cue:** With all the Gaussian models ready, we generate novel demonstrations and perform data augmentation in terms of object
- **p. 3 / IV. METHODOLOGY - extractive body cue:** To generate high-fidelity and diverse data from a single expert trajectory, we present RoboSplat, a novel demonstration generation approach based on 3DGS.
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Finally, a visuomotor policy is trained on the augmented demonstrations and directly deployed on real robots, as detailed in Sec.
- **Detected method headings:** A. Generalizable Policy in Robot Manipulation (p. 2); B. Data Augmentation for Policy Learning (p. 2); IV. METHODOLOGY (p. 3); C. Policy Training (p. 6); 2) How does the policy trained on generated demonstrations (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | Instead of adopting generalizable policy architecture, auxiliary learning objectives ‘and powerful foundation models, our work is concentrated on generating high-quality, diverse, and ... | p. 2 (A. Generalizable Policy in Robot Manipulation), p. 6 (C. Policy Training) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | The latent of images and robot state is fed into a transformer encoder. | p. 6 (C. Policy Training), p. 6 (C. Policy Training) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We employ a modem, widely adopted transformer-based architecture [18, 51, 38, 55] to serve as the policy network, which is detailed in ... | p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / A. Reconstruction and Preprocessing - extractive body cue:** The camera extrinsies are optimized through gradient descent, with the optimization objective:
- **p. 6 / C. Policy Training - extractive body cue:** The policy is trained with Behavioural Cloning (BC) in an end-to-end manner, aiming to maximize the likelihood of expert actions in demonstrations.
- **p. 6 / C. Policy Training - extractive body cue:** The loss function can then be expressed as
- **p. 4 / A. Reconstruction and Preprocessing - extractive body cue:** Subsequently, backpropagation and gradient descent are used to optimize the translation, rotation, and scale, which are then applied to the 3D Gaussians.
- **p. 2 / A. Generalizable Policy in Robot Manipulation - extractive body cue:** Instead of adopting generalizable policy architecture, auxiliary learning objectives ‘and powerful foundation models, our work is concentrated on generating high-quality, diverse, and realistic data to ...
- **p. 4 / A. Reconstruction and Preprocessing - extractive body cue:** The loss is calculated between the mask rendered using Gaussian Splatting and the mask rendered with URDE.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 5 (A. Reconstruction and Preprocessing), p. 2 (A. Generalizable Policy in Robot Manipulation), p. 4 (A. Reconstruction and Preprocessing), p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | images, camera, poses, depth, prior, serve, inputs, DGS, returns, Gaussians, representing, entire, scene, Gucene | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | images, camera, poses, depth, prior, serve, inputs, DGS, returns, Gaussians | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | enables, autonomous, editing, reconstructed, scene, generate, diverse, demonstrations, various, configurations | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | camera, extrinsies, optimized, through, gradient, descent, optimization, objective, policy, trained | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / A. Reconstruction and Preprocessing - extractive body cue:** The images. camera poses, and depth prior serve as inputs to 3DGS [25], which returns 3D. ‘Gaussians representing the entire scene Gucene, Which contains 3D ...
- **p. 6 / C. Policy Training - extractive body cue:** We denote 0, # (Ii, 4x) as the observation at the k-th frame of demonstrations D, and as our policy.
- **p. 6 / C. Policy Training - extractive body cue:** The policy is trained with Behavioural Cloning (BC) in an end-to-end manner, aiming to maximize the likelihood of expert actions in demonstrations.
- **p. 2 / B. Data Augmentation for Policy Learning - extractive body cue:** Nonetheless, these studies mainly augment task demonstrations on 2D images, which lack spatial information, Hence, only limited augmentation can be achieved, and the ‘augmented demonstrations ...
- **p. 1 / Front matter - extractive body cue:** 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust performance across ...
- **p. 1 / Abstract - extractive body cue:** Visuomotor policies learned from teleoperated, demonstrations face challenges such as lengthy data collection, high costs, and ting approaches address these issues by augmenting image observations ...
- **p. 2 / 1. INrRopucTION - extractive body cue:** Another line of work sheds light on augmenting image observations for better visual generalization.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | We employ a 3D SpaceMouse to collect teleoperated demonstrations at a frequency of 10 Hz, Policy inference is carried out on an ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Whenever the gripper action toggles or joint velocities approach zero, we consider the current time step as 4 keyframe and record the ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | We employ a 3D SpaceMouse to collect teleoperated demonstrations at a frequency of 10 Hz, Policy inference is carried out on an ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / B. Data Augmentation for Policy Learning - extractive body cue:** Given limited training data, data augmentation emerges as a way to improve the robustness of the policy.
- **p. 4 / IV. METHODOLOGY - extractive body cue:** Finally, a visuomotor policy is trained on the augmented demonstrations and directly deployed on real robots, as detailed in Sec.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Instead, adopting, generalizable, policy, architecture, auxiliary, learning, objectives, powerful, foundation, models, concentrated, generating, high-quality, diverse, realistic, data, instill, generalization, abilities.
- **Relevant PDF headings:** A. Generalizable Policy in Robot Manipulation (p. 2); B. Data Augmentation for Policy Learning (p. 2); IV. METHODOLOGY (p. 3); C. Policy Training (p. 6); 2) How does the policy trained on generated demonstrations (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | We design five manipulation tasks for real-world evaluation: Pick Object, Close Drawer, Pick-PlaceClose, Dual Pick-Place and Sweep, whose details are elaborated in ... | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Policy fitting | Fig. 3: Comparison of frame alignment results between ICP and fine-grained optimization with differentiable ren- dering. The semi-transparent orange overlay represents the ... | p. 4 (Figure/Table caption) |
| Closed-loop rollout | Fig. 11: Performance on cross embodiment experiments. We evaluate the learned policy directly on the URSe robot and achieve a nearly 100% ... | p. 10 (Figure/Table caption), p. 7 (A. Experimental Setup) |

## Failure and Ablation Link

- **p. 6 / A. Experimental Setup - extractive body cue:** The drawer is placed in a Sem%Sem workspace, with a fixed orientation, The target object is located in a 1em> 10em workspace, whose rotation falls ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust performance ...
- **p. 7 / B. Eficiency of Augmenting Demonstrations - extractive body cue:** Robustness when Facing Various Deployment Settings
- **p. 8 / 2) Scene Appearance - extractive body cue:** In particular, our policy achieves 100% success rate on the Pick Object task, showcasing strong robustness against various background appearance.
- **p. 8 / 4) 3200 generated demonstrations with camera view aug - extractive body cue:** Notably, our policy achieves nearly 100% success rate (on Close Drawer task, manifesting strong robustness against novel camera views and moving cameras,
- **p. 9 / 3) 6400 demonstrations generated by our pipeline with ob - extractive body cue:** The data is collected in the original setting, ‘When deploying the trained policy, we modify object poses, lighting conditions, scene appearance, camera views, object types, ...
- **p. 9 / 5) Embodiment Type - extractive body cue:** To prove that, based on one demonstration collected with the Franka Research 3, we generate novel demonstrations for a URSe robot equipped with a Robotiq ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (A. Generalizable Policy in Robot Manipulation), p. 6 (C. Policy Training), p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning), p. 3 (IV. METHODOLOGY), p. 3 (IV. METHODOLOGY), objective p. 5 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training), p. 6 (C. Policy Training), p. 4 (A. Reconstruction and Preprocessing), p. 2 (A. Generalizable Policy in Robot Manipulation), p. 4 (A. Reconstruction and Preprocessing), temporal p. 6 (A. Experimental Setup), p. 5 (1) Object Pose), p. 5 (4) Embodiment Type), p. 3 (IV. METHODOLOGY), p. 6 (A. Experimental Setup), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
