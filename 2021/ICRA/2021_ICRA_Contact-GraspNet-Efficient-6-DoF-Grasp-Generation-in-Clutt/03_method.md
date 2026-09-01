# Method - Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.14127; PDF retrieval source: https://arxiv.org/pdf/2103.14127. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD)): The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, from which we form our grasp representation.

## Method Body Digest

- **p. 4 / III. METHOD - extractive body cue:** The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, from which we ...
- **p. 3 / III. METHOD - extractive body cue:** In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in grasping [11] and ...
- **p. 4 / III. METHOD - extractive body cue:** Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given in Eq.
- **p. 3 / III. METHOD - extractive body cue:** Point Set Networks such as PointNet++ [34] effectively process point clouds and hierarchically aggregate points and their feature representations in local 3D neighborhoods.
- **p. 5 / III. METHOD - extractive body cue:** Predicted 6-DoF grasps are then associated to object segments by filtering their contact points.
- **p. 5 / III. METHOD - extractive body cue:** 0 0.1 0.2 0.3 0.4 0.5 0.6 0 0.2 0.4 0.6 0.8 1 Coverage Success Rate Simulator Success-Coverage Contact GraspNet w/o ladd-s w/o binned lwidth ...
- **p. 4 / III. METHOD - extractive body cue:** On the grasp width bin predictions, we optimize a weighted, multi-label binary cross entropy loss lwidth.
- **p. 4 / III. METHOD - extractive body cue:** Target Losses The contact grasp success predictions ˆs ∈R are evaluated at all output points pi ∈R3 : ∀i ∈[0, m] using binary cross entropy.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method is closely related to the work of Murali et al.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these issues, our method instead directly processes a full scene point cloud or a local region around a target object.
- **p. 3 / III. METHOD - extractive body cue:** We used the ACRONYM dataset [32], which consists of 8872 meshes from the Shapenet dataset [35] and 17.7 million

## Source Evidence Cues

- **p. 4 / III. METHOD - extractive body cue:** The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, from which we ...
- **p. 3 / III. METHOD - extractive body cue:** In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in grasping [11] and ...
- **p. 4 / III. METHOD - extractive body cue:** Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given in Eq.
- **p. 3 / III. METHOD - extractive body cue:** Point Set Networks such as PointNet++ [34] effectively process point clouds and hierarchically aggregate points and their feature representations in local 3D neighborhoods.
- **p. 5 / III. METHOD - extractive body cue:** Predicted 6-DoF grasps are then associated to object segments by filtering their contact points.
- **p. 5 / III. METHOD - extractive body cue:** 0 0.1 0.2 0.3 0.4 0.5 0.6 0 0.2 0.4 0.6 0.8 1 Coverage Success Rate Simulator Success-Coverage Contact GraspNet w/o ladd-s w/o binned lwidth ...
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive body cue:** On the grasp width bin predictions, we optimize a weighted, multi-label binary cross entropy loss lwidth.
- **p. 4 / III. METHOD - extractive body cue:** Target Losses The contact grasp success predictions ˆs ∈R are evaluated at all output points pi ∈R3 : ∀i ∈[0, m] using binary cross entropy.
- **p. 3 / III. METHOD - extractive body cue:** In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in grasping [11] and ...
- **p. 5 / III. METHOD - extractive body cue:** Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease.
- **p. 5 / III. METHOD - extractive body cue:** The ladd-s loss leads to increased success rates at high confidence contacts (Coverage ∈[0, 0.1]) and to slightly decreased success rate in the low-confidence regime.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | predictions, directly, associated, points, input, point, cloud, grasp, representation, exploits, ability, Network, employ, abstraction | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | predictions, directly, associated, points, input, point, cloud, grasp, representation, exploits | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | closely, related, Murali, address, issues, instead, directly, processes, full, scene | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | grasp, width, predictions, optimize, weighted, multi-label, binary, cross, entropy, loss | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** Their predictions can be directly associated to 3D points in the input point cloud and our proposed grasp representation exploits this ability.
- **p. 4 / III. METHOD - extractive body cue:** Network We employ the set abstraction and feature propagation layers proposed in PointNet++ [34] to build an asymmetric Ushaped network.
- **p. 3 / III. METHOD - extractive body cue:** Since visible contact points are bound to lie on surfaces that we can observe with a depth sensor, we can represent their 3D location by ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we tackle 6-DoF grasping of unknown objects in cluttered space from a partial point cloud observation of the scene.
- **p. 2 / III. METHOD - extractive body cue:** Furthermore, direct regression in high dimensional output spaces like SE(3) has
- **p. 4 / III. METHOD - extractive body cue:** Our set abstraction layers have 3 parallel branches with query ball radii [0.02,0.04,0.08], [0.04,0.08.0.16] and [0.08,0.16,0.32].
- **p. 2 / III. METHOD - extractive body cue:** Our approach takes in a raw depth image, optionally with object masks, and generates 6-DoF grasp proposals together with corresponding grasp widths.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Our grasp representation: c depicts an observed contact point. a and b constitute the 3-DoF rotation, w is the predicted grasp width, ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | An overview of our offline and online training data generation is given in Fig. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | We train with a batch size of 3 for 144.000 iterations which takes ∼40 hours on a single Nvidia V100 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - extractive body cue:** We train with a batch size of 3 for 144.000 iterations which takes ∼40 hours on a single Nvidia V100 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** network, four, heads, DConv, layers, per-point, outputs, R10, form, grasp, representation, pink, five, gripper, points, ladd-s, loss, been, difficult, grasping.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes. | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Grasp / trajectory generation | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods ... | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION) |
| Contact execution / correction | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods ... | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to increased ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly on ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** 5 we first investigate the effect of our loss targets.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Ablations Optimization Targets: In Fig.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. Grasp ...
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), objective p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), temporal p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 6 (V. CONCLUSIONS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
