# Method - DextAIRity: Deformable Manipulation Can be a Breeze

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.01197; PDF retrieval source: https://arxiv.org/pdf/2203.01197. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD)): We use the same blowing network architecture as in the unfolding task, but with a few modifications in action parameterization, reward signal, and directly train this policy on real-world data.

## Method Body Digest

- **p. 5 / IV. METHOD - extractive body cue:** We use the same blowing network architecture as in the unfolding task, but with a few modifications in action parameterization, reward signal, and directly train ...
- **p. 4 / IV. METHOD - extractive body cue:** The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP to produce the ...
- **p. 4 / IV. METHOD - extractive body cue:** We use DeepLabv3 [5] with random initialization as network architecture.
- **p. 5 / IV. METHOD - extractive body cue:** In total, we collected 4,400 (4,000 for training, 400 for validation) interactions over the course of 10 hours and trained the blowing network 50 epochs ...
- **p. 3 / IV. METHOD - extractive body cue:** Crucially, while controlled airflow provides the system with additional control over out-of-contact object regions, the deformation on the object also provides visual feedback about the ...
- **p. 3 / IV. METHOD - extractive body cue:** The key idea of DextAIRity is to leverage the interactions between active airflow and deformable objects to achieve efficient manipulation.
- **p. 4 / IV. METHOD - extractive body cue:** We found this constraint significantly reduced the chance of grasping multiple layers of the fabric, which is a typical failure case for Flingbot.
- **p. 4 / IV. METHOD - extractive body cue:** From these parameters, the two grasping positions L,R are computed, allowing efficient computation grasping positions while satisfying collision-avoidance constraints.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our system setup consists of (a) three UR5 robot arms, two of which are equipped with parallel-jaw grippers and one with a commodity centrifugal air ...
- **p. 4 / IV. METHOD - extractive body cue:** The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP to produce the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This property particularly is useful when the target object has a large volume or surface area - spreading a large piece of cloth for instance ...

## Source Evidence Cues

- **p. 5 / IV. METHOD - extractive body cue:** We use the same blowing network architecture as in the unfolding task, but with a few modifications in action parameterization, reward signal, and directly train ...
- **p. 4 / IV. METHOD - extractive body cue:** The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP to produce the ...
- **p. 4 / IV. METHOD - extractive body cue:** We use DeepLabv3 [5] with random initialization as network architecture.
- **p. 5 / IV. METHOD - extractive body cue:** In total, we collected 4,400 (4,000 for training, 400 for validation) interactions over the course of 10 hours and trained the blowing network 50 epochs ...
- **p. 3 / IV. METHOD - extractive body cue:** Crucially, while controlled airflow provides the system with additional control over out-of-contact object regions, the deformation on the object also provides visual feedback about the ...
- **p. 3 / IV. METHOD - extractive body cue:** The key idea of DextAIRity is to leverage the interactions between active airflow and deformable objects to achieve efficient manipulation.
- **Detected method headings:** IV. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | We use the same blowing network architecture as in the unfolding task, but with a few modifications in action parameterization, reward signal, ... | p. 5 (IV. METHOD), p. 4 (IV. METHOD) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | The blowing network consists of an image encoder (7-layer convolution network) and an action encoder (3-layer MLP), followed by a 3-layer MLP ... | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | We use DeepLabv3 [5] with random initialization as network architecture. | p. 4 (IV. METHOD), p. 5 (IV. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. METHOD - extractive body cue:** In total, we collected 4,400 (4,000 for training, 400 for validation) interactions over the course of 10 hours and trained the blowing network 50 epochs ...
- **p. 4 / IV. METHOD - extractive body cue:** We found this constraint significantly reduced the chance of grasping multiple layers of the fabric, which is a typical failure case for Flingbot.
- **p. 4 / IV. METHOD - extractive body cue:** From these parameters, the two grasping positions L,R are computed, allowing efficient computation grasping positions while satisfying collision-avoidance constraints.
- **p. 5 / IV. METHOD - extractive body cue:** Both networks are supervised via MSE Loss between predicted and real coverage.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Observation, Blowing, Scores, Network, Execution, Cloth, unfolding, Grasp, Grasping, Policy, Stretch, Place, Initial, State | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Observation, Blowing, Scores, Network, Execution, Cloth, unfolding, Grasp, Grasping, Policy | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | system, setup, consists, three, UR5, robot, arms, equipped, parallel-jaw, grippers | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | total, collected, training, validation, interactions, over, course, hours, trained, blowing | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / IV. METHOD - extractive body cue:** Observation Blowing Scores Blowing Network max Execution Cloth unfolding Grasp (a) Grasping Policy (Cloth Unfolding) Stretch Place Initial State Bag opening ×8 rotations Observation Grasping ...
- **p. 5 / IV. METHOD - extractive body cue:** At each blowing step, a top-down depth observation as input and the blowing action with the highest score will be executed.
- **p. 4 / IV. METHOD - extractive body cue:** (b) At each blowing step, the blowing network takes the top-down observation as input and infers blowing scores for each action candidate (blower position and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** By combining this information with a closed-loop policy, the system can continually adjust its blowing action based on visual feedback.
- **p. 3 / IV. METHOD - extractive body cue:** Crucially, while controlled airflow provides the system with additional control over out-of-contact object regions, the deformation on the object also provides visual feedback about the ...
- **p. 5 / IV. METHOD - extractive body cue:** To reduce noise in reward computation, at the beginning of each blowing action the blower turns on for 2 s after movement to ensure the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By controlling the blower's direction, the system can apply dense forces on out-of-contact surfaces (A and B) to efficiently achieve its goal. • High-speed interactions ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Each epoch contains 32 episodes and 64 optimization steps with a batch size of 16 for the grasping network and 128 for ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Each episode contains at most 5 interaction steps, where each step includes both grasping and blowing actions, and the policy terminates an ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Each epoch contains 32 episodes and 64 optimization steps with a batch size of 16 for the grasping network and 128 for ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. METHOD - extractive body cue:** We use the same blowing network architecture as in the unfolding task, but with a few modifications in action parameterization, reward signal, and directly train ...
- **p. 5 / IV. METHOD - extractive body cue:** In total, we collected 4,400 (4,000 for training, 400 for validation) interactions over the course of 10 hours and trained the blowing network 50 epochs ...
- **p. 7 / V. EVALUATION - extractive body cue:** Training of [FlingBot+] takes only 300 epochs, while [FlingBot] requires over 2,000 epochs to converge.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** same, blowing, network, architecture, unfolding, task, modifications, action, parameterization, reward, signal, directly, train, policy, real-world, data, consists, image, encoder, layer.
- **Relevant PDF headings:** IV. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | For both tasks, we evaluate task completion rate and ability to generalize to unseen cloths and bags on a real-world robot platform. | p. 5 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Grasp / trajectory generation | As a result, coverage of X-Large Rect increases +23.0%, +13.3%, +1.6%, and +0.3% at each blow step compared to the fixed-policy ablation. | p. 6 (V. EVALUATION), p. 6 (V. EVALUATION) |
| Contact execution / correction | II shows performance averaged over 10 test episodes; our policy achieves over 80% on all cloth types, outperforming [FlingBot] and [Pick&Place] by ... | p. 7 (V. EVALUATION), p. 8 (V. EVALUATION) |

## Failure and Ablation Link

- **p. 6 / V. EVALUATION - extractive body cue:** As a result, coverage of X-Large Rect increases +23.0%, +13.3%, +1.6%, and +0.3% at each blow step compared to the fixed-policy ablation.
- **p. 6 / V. EVALUATION - extractive body cue:** Our experimental evaluation suggests that DextAIRity is a promising approach for quickly and efficiently unfolding for large cloth items without the need of high-speed movements ...
- **p. 7 / V. EVALUATION - extractive body cue:** Ablations: We compare our system with the following alternative approaches for bag opening: • Shake: moves the bag back-and-forth by rotating last joint and records ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DextAIRity manipulates deformable objects by controlling an active airflow. We demonstrate DextAIRity with two tasks that are particularly challenging for traditional contact-based manipulation: ...
- **p. 8 / VI. LIMITATIONS AND PRACTICAL CONSIDERATIONS - extractive body cue:** While in this paper we demonstrate the effectiveness of directed air to manipulate deformable objects, we discuss a few limitations and practical considerations of deploying ...
- **p. 6 / V. EVALUATION - extractive body cue:** The failure of [FlingBot] is due to its limited move speed, which needs to Large Rect X-Large Rect Shirt Dress Pick&Place 36.2 / 13.1 38.0 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Cases. (a) A corner is inadvertently rolled up due to Eddy effects. (b) Multiple layers of the fabric are mistakenly grasped. (c) ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), objective p. 5 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), temporal p. 5 (IV. METHOD), p. 5 (V. EVALUATION), p. 6 (V. EVALUATION), p. 8 (V. EVALUATION), p. 1 (Abstract), p. 4 (IV. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
