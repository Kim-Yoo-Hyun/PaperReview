# Method - ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p156.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p156.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 8 (B. Is a Hierarchical Policy Needed?), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 6 (B. Policy Learning with a Hierarchical Policy Representation)): Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the scene points, and the goal end-effector points to ...

## Method Body Digest

- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the scene points, and ...
- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- **p. 7 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as ...
- **p. 8 / B. Is a Hierarchical Policy Needed? - extractive body cue:** takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in DP3 ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Middle: We propose a weighted displacement model for the high-level policy, which predicts the sub-goal end-effector pose.
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Specifically, instead of representing the sub-goal endeffector pose as a position and an SO(3) orientation (e.g., 4 quaternion or a 6D orientation representation [65}) and ...
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** As in DP3, the network has two parts: a point cloud encoder that encodes the point cloud observation into a latent embedding, and a diffusion ...
- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Formally, the high-level policy 7! is learned via minimizing the following loss:

## Design Rationale

- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘+ We present a weighted displacement policy representation that scales up well with the number of demonstrations, outperforming alternative policy representations.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 1 for a visualization of some of the different real-world articulated objects that our policy is able to open, In summary, our contributions are:

## Source Evidence Cues

- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the scene points, and ...
- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy.
- **p. 7 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as ...
- **p. 8 / B. Is a Hierarchical Policy Needed? - extractive body cue:** takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in DP3 ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Middle: We propose a weighted displacement model for the high-level policy, which predicts the sub-goal end-effector pose.
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Specifically, instead of representing the sub-goal endeffector pose as a position and an SO(3) orientation (e.g., 4 quaternion or a 6D orientation representation [65}) and ...
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** As in DP3, the network has two parts: a point cloud encoder that encodes the point cloud observation into a latent embedding, and a diffusion ...
- **Detected method headings:** 2. Hierarchical Policy Learning (p. 1); B. Sim2real Policy Learning (p. 3); 2. Hierarchical Policy Learning -- High-level Policy Architecture (p. 4); 2. Hierarchical Policy Learning -- Low-level Policy Architecture (p. 4); B. Policy Learning with a Hierarchical Policy Representation (p. 5); B. Is a Hierarchical Policy Needed? (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the ... | p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Instead, we propose to use a hilrarchical policy representation, which consists of 4 high-level policy and a low-level policy. | p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding ... | p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 8 (B. Is a Hierarchical Policy Needed?) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Formally, the high-level policy 7! is learned via minimizing the following loss:
- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Our goal is to find a neural network policy =, parameterized by 8, t0 minimize the following imitation learning loss:
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Among the collision-free solutions, we choose the one solution that has the shortest distance in the joint angle space to the current joint configuration, so ...
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** We train it with the following two losses, which supervises the per-point displacement prediction, and the weighted average prediction:
- **p. 7 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** We perform cross tention between the current end-effector points and the goal end-effector points, also with Rotary Position Embedding (RoPE) (4), which produces another set ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 6 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, point, cloud, input, outputs, delta, endeffector, transformations, actions, DP3, Transformer, replaces, simplified, PointNet | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | takes, point, cloud, input, outputs, delta, endeffector, transformations, actions, DP3 | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | Instead, hilrarchical, policy, representation, consists, high-level, low-level, present, weighted, displacement | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Formally, high-level, policy, learned, minimizing, following, loss, goal, find, neural | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / B. Is a Hierarchical Policy Needed? - extractive body cue:** takes 3D point cloud as input and outputs delta endeffector transformations as the actions. + DP3 Transformer, which replaces the simplified PointNet encoder in DP3 ...
- **p. 7 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding is used ‘as ...
- **p. 4 / 2. Hierarchical Policy Learning -- Low-level Policy Architecture - extractive body cue:** Bottom: We propose a goal-conditioned 3D diffusion policy for the low-level policy, which first applies attention between the current end-effector points, the scene points, and ...
- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** Specifically, the high-level policy 7}! learns to predict the sub-goal end-effector pose given an observation.
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** We note that the low-level policy is not trained to reach the sub-goal end-effector pose; it is trained to solve the task, and the sub-goal ...
- **p. 1 / 2. Hierarchical Policy Learning - extractive body cue:** simulator, and distill them into a hierarchical policy with point cloud observations.
- **p. 5 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** We use the robot base frame as our reference frame, ie. all point cloud observations, and robot actions, are expressed inthe robot base frame.
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | The final latent embedding used for diffusion is the concatenation of the above two features: [fpoo™, fom"! yess, po This latent embedding ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | After the high-level and low-level policies are trained in simulation, we transfer them zero-shot to real-world robotic systems, During inference, at each ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** At inference time, the final predicted subgoal endheffector pose is the averaged prediction from all points in the scene: e¢,(0) = 31 (p;-+8)(0)).
- **p. 6 / B. Policy Learning with a Hierarchical Policy Representation - extractive body cue:** At inference time, the final prediction of the sub-goal end-effector Points is then the weighted average of the displacement from each point: €€,(0) = 2)", ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Bottom, goal-conditioned, diffusion, policy, low-level, first, applies, attention, between, current, end-effector, points, scene, goal, obtain, latent, embedding, then, performs, generate.
- **Relevant PDF headings:** 2. Hierarchical Policy Learning (p. 1); B. Sim2real Policy Learning (p. 3); 2. Hierarchical Policy Learning -- High-level Policy Architecture (p. 4); 2. Hierarchical Policy Learning -- Low-level Policy Architecture (p. 4); B. Policy Learning with a Hierarchical Policy Representation (p. 5); B. Is a Hierarchical Policy Needed? (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | Although our training data includes multi-door objects, demonstrations are generated for opening the closest door to the initial pose of the robot. | p. 13 (C. Mobile X-Arm Results), p. 7 (V. SIMULATION RESULTS) |
| Base-arm task decision | ‘The results forall test objects and compared methods in lab A are shown in Fig. | p. 12 (B. Table-Top Franka Arm Results), p. 12 (B. Table-Top Franka Arm Results) |
| Execution / correction | If we compute the normalized opening performance for ArticuBot only in cases where the grasp is successful (Le., the same starting conditions ... | p. 12 (B. Table-Top Franka Arm Results), p. 12 (C. Mobile X-Arm Results) |

## Failure and Ablation Link

- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** We think adding a force-torque sensor on the X-Arm to enable impedance control could help alleviate this issue; fine-tuning the policy in the real-world via ...
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** See Appendix L for visualizations of some of the failure cases of ArticuBot, and some basic failure recovery abilities of ArticuBot.
- **p. 13 / C. Mobile X-Arm Results - extractive body cue:** We leave addressing these limitations as important future work.
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** Common failure ceases for table-top experiments include: 1, The robot arm runs to joint limits while opening the object, due to the limited space of ...
- **p. 12 / B. Table-Top Franka Arm Results - extractive body cue:** The major failure case for FlowBot3D is that the predicted flow is in the wrong direction, e.g., it predicts upwards flows for ‘opening a microwave ...
- **p. 11 / A. Setups - extractive body cue:** We do not input the optional segmentation mask for the target link to open for FlowBot3D, as such masks are not readily available in the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 8 (B. Is a Hierarchical Policy Needed?), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 6 (B. Policy Learning with a Hierarchical Policy Representation), objective p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 4 (2. Hierarchical Policy Learning -- Low-level Policy Architecture), p. 6 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (B. Policy Learning with a Hierarchical Policy Representation), temporal p. 7 (B. Policy Learning with a Hierarchical Policy Representation), p. 7 (C. Zerv-shot Transfer 10 Real Robotic Systems), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 5 (B. Policy Learning with a Hierarchical Policy Representation), p. 3 (A. Demonstration Generation in Simulation), p. 3 (A. Demonstration Generation in Simulation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
