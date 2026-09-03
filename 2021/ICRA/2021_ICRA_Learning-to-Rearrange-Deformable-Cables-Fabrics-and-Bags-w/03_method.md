# Method - Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.03385; PDF retrieval source: https://arxiv.org/pdf/2012.03385. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 1 (Abstract), p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 2 (III. BACKGROUND), p. 4 (V. SIMULATOR AND TASKS)): For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after the last action from the demonstration episode containing ...

## Method Body Digest

- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after the last action ...
- **p. 1 / Abstract - extractive body cue:** We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can ...
- **p. 3 / III. BACKGROUND - extractive body cue:** The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.
- **p. 2 / III. BACKGROUND - extractive body cue:** Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a ...
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on the ...
- **p. 4 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** Transporter Networks use three Fully Convolutional Networks (FCNs), fpick for the attention module, and Φquery and Φkey for the transport module.
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** Contact and friction constraints between soft bodies and multi bodies are solved in a unified constraint solver at the velocity level.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and ...
- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** Goal-Conditioned Transporter Networks We propose two goal-conditioned architectures based on Transporter Networks.

## Source Evidence Cues

- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after the last action ...
- **p. 1 / Abstract - extractive body cue:** We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can ...
- **p. 3 / III. BACKGROUND - extractive body cue:** The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.
- **p. 2 / III. BACKGROUND - extractive body cue:** Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a ...
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on the ...
- **p. 4 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** Transporter Networks use three Fully Convolutional Networks (FCNs), fpick for the attention module, and Φquery and Φkey for the transport module.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after ... | p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 1 (Abstract) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer ... | p. 1 (Abstract), p. 3 (III. BACKGROUND) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate ... | p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** Contact and friction constraints between soft bodies and multi bodies are solved in a unified constraint solver at the velocity level.
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** Implicit damping of the velocity uses a Krylov style method and soft body contact and friction is based on Conjugate Gradient for symmetric positive definite ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** The goal is to train a policy that executes a sequence of pick and place actions in the workspace to achieve an objective, learned from ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** The grasping motion primitive (introduced in Section III) is similar to the implementations in [28], [53] and approximates a pinch-grasp on a deformable by indexing ...
- **p. 3 / III. BACKGROUND - extractive body cue:** The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: ...
- **p. 3 / III. BACKGROUND - extractive body cue:** Both the second and third FCNs output dense feature embeddings, which are then cross-correlated with each other to output a dense per-pixel prediction of action-values ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (V. SIMULATOR AND TASKS), p. 4 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | first, FCN, fpick, takes, input, visual, observation, outputs, dense, per-pixel, prediction, action-values, Qpick, correlate | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | first, FCN, fpick, takes, input, visual, observation, outputs, dense, per-pixel | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | several, tasks, benchmark, tackle, them, novel, goal-conditioned, variants, Transporter, Network | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | Contact, friction, constraints, between, soft, bodies, multi, solved, unified, constraint | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. BACKGROUND - extractive body cue:** The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: ...
- **p. 2 / III. BACKGROUND - extractive body cue:** Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a ...
- **p. 3 / III. BACKGROUND - extractive body cue:** To train the policy, we assume access to a small dataset of N stochastic expert demonstrations D = {ξi}N i=1, where each episode ξi of ...
- **p. 2 / III. BACKGROUND - extractive body cue:** Since deformable objects may require more than a single pick and place action to reach a desired configuration, it is important that the policy π ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** The goal is to train a policy that executes a sequence of pick and place actions in the workspace to achieve an objective, learned from ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Example of a trained Transporter Network policy in action on the bag-items-1 task (see Table I).
- **p. 1 / I. INTRODUCTION - extractive body cue:** These types of tasks are especially challenging with diverse goal conditioning: the goal states of deformable objects are not easily specified, for example, by compact ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Episodes for fabric-cover are successful if the fabric covers the cube. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Episodes for cable-shape, cable-shapenotarget, and cable-line-notarget, are successful if all cable beads have reached designated target poses. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | We overlay arrows to indicate the movement of the robot's arm just before a given frame. one 1D deformable task, we show ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after the last action ...
- **p. 5 / VII. SIMULATION RESULTS - extractive body cue:** Models are trained for 20K iterations, with a batch size of 1 for the three Transporter models and 128 for the two ground truth models ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** goal-conditioned, Transporter, Networks, same, procedure, then, additionally, corresponding, observation, after, last, action, demonstration, episode, containing, training, sample, embedding, goal-conditioning, recently.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper. | p. 6 (VIII. PHYSICAL EXPERIMENTS AND RESULTS), p. 5 (VI. SIMULATION EXPERIMENTS) |
| Grasp / trajectory generation | Goal Conditioned Tasks Across all 4 dataset sizes for cable-line-notarget, cableshape-notarget, and fabric-flat-notarget, both TransporterGoal-Stack and Transporter-Goal-Split substantially outperform the two GT-State ... | p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS) |
| Contact execution / correction | Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters ... | p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Top row: examples of physical bags. The bags we use follow a design similar to the sack (top left) and drawstring (top middle). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering ...
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on the ...
- **p. 6 / VIII. PHYSICAL EXPERIMENTS AND RESULTS - extractive body cue:** Changes from Simulation Unlike in simulation, we cannot assume "perfect" grasping of deformable objects.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: The 12 tasks in the proposed DeformableRavens benchmark (see Table I) with suction cup gripper and deformable objects. Top row: (a) cable-ring, (b) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: The proposed Transporter-Goal-Split, applied to an example on bag-color-goal, where given the current image ot and goal og, the objective is to insert ...
- **p. 5 / V. SIMULATOR AND TASKS - extractive body cue:** Bags with handles (e.g., top right) or with more stiffness will be addressed in future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 1 (Abstract), p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 2 (III. BACKGROUND), p. 4 (V. SIMULATOR AND TASKS), objective p. 4 (V. SIMULATOR AND TASKS), p. 4 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 5 (V. SIMULATOR AND TASKS), p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND), temporal p. 5 (VI. SIMULATION EXPERIMENTS), p. 5 (VI. SIMULATION EXPERIMENTS), p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. BACKGROUND).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
