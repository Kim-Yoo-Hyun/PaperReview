# Method - FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.03655; PDF retrieval source: https://arxiv.org/pdf/2105.03655. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method)): Our value network is a fully convolutional neural network with nine residual blocks [21] and two convolutional layers in the first and last layer, and takes as input 64 × ...

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** Our value network is a fully convolutional neural network with nine residual blocks [21] and two convolutional layers in the first and last layer, and ...
- **p. 5 / 3 Method - extractive body cue:** From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the ...
- **p. 3 / 3 Method - extractive body cue:** It predicts the value of each action with a value network (Sec.
- **p. 3 / 3 Method - extractive body cue:** After training in simulation, we finetune and evaluate the model in the real world (Sec.
- **p. 4 / 3 Method - extractive body cue:** We also fix the fling speed and trajectory from the observation that the real world system could robustly unfold the cloth using a wide range ...
- **p. 4 / 3 Method - extractive body cue:** Without loss of generality for the purposes of grasping from a top-down RGB-D input, the third dimension could be specified by depth information.
- **p. 6 / 3 Method - extractive body cue:** We further apply brightness, contrast, and hue jittering on observations to help with the transfer to real.
- **p. 4 / 3 Method - extractive body cue:** However, to minimize collisions between two arms, we wish to impose a constraint that L is always left of R, and vice versa (Fig 9a).

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We ...
- **p. 4 / 3 Method - extractive body cue:** To make these constraints linear and independent, we propose an alternative 4-scalar parameterization, which consists of pixel position of the point C ∈R2 at the ...
- **p. 2 / 1 Introduction - extractive body cue:** To achieve this goal, we present FlingBot, a self-supervised algorithm that learns how to unfold cloths from arbitrary initial configurations using a pick, stretch, and ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** Our value network is a fully convolutional neural network with nine residual blocks [21] and two convolutional layers in the first and last layer, and ...
- **p. 5 / 3 Method - extractive body cue:** From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the ...
- **p. 3 / 3 Method - extractive body cue:** It predicts the value of each action with a value network (Sec.
- **p. 3 / 3 Method - extractive body cue:** After training in simulation, we finetune and evaluate the model in the real world (Sec.
- **p. 4 / 3 Method - extractive body cue:** We also fix the fling speed and trajectory from the observation that the real world system could robustly unfold the cloth using a wide range ...
- **p. 4 / 3 Method - extractive body cue:** Without loss of generality for the purposes of grasping from a top-down RGB-D input, the third dimension could be specified by depth information.
- **p. 6 / 3 Method - extractive body cue:** We further apply brightness, contrast, and hue jittering on observations to help with the transfer to real.
- **Detected method headings:** 3 Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Our value network is a fully convolutional neural network with nine residual blocks [21] and two convolutional layers in the first and ... | p. 5 (3 Method), p. 5 (3 Method) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) ... | p. 5 (3 Method), p. 3 (3 Method) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | It predicts the value of each action with a value network (Sec. | p. 3 (3 Method), p. 3 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Method - extractive body cue:** However, to minimize collisions between two arms, we wish to impose a constraint that L is always left of R, and vice versa (Fig 9a).
- **p. 3 / 3 Method - extractive body cue:** Concretely, this amounts to maximizing the cloth's coverage on the workspace surface.
- **p. 3 / 3 Method - extractive body cue:** 3.2) by picking the highest value action which satisfies the system's constraints (Sec.
- **p. 4 / 3 Method - extractive body cue:** Without loss of generality for the purposes of grasping from a top-down RGB-D input, the third dimension could be specified by depth information.
- **p. 5 / 3 Method - extractive body cue:** While our simulation environment does not support loading URDFs of robots, we found it sufficient to represent only the arms' end effectors, and apply appropriate ...
- **p. 5 / 3 Method - extractive body cue:** The network is trained using the Adam optimizer with a learning rate of 1e-3 and a weight decay of 1e-6.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | top-down, RGB, image, policy, evaluates, batch, different, action, rotations, scales, transforming, observation, then, predicting | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | top-down, RGB, image, policy, evaluates, batch, different, action, rotations, scales | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | summary, main, contribution, demonstrating, effectiveness, dynamic, manipulation, cloth, unfolding, through | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | However, minimize, collisions, between, arms, wish, impose, constraint, always, left | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive body cue:** From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the ...
- **p. 2 / 1 Introduction - extractive body cue:** At each time step, the policy predicts value maps from its visual observation and picks actions greedily with respect to its value maps.
- **p. 3 / 3 Method - extractive body cue:** From a top-down RGB image of the workspace with the cloth, our policy decides the next fling action (Sec.
- **p. 5 / 3 Method - extractive body cue:** Each pixel in each value map contains the value of the action parameterized by that pixel's location, giving C, and its observation's rotation and scaling, ...
- **p. 4 / 3 Method - extractive body cue:** Without loss of generality for the purposes of grasping from a top-down RGB-D input, the third dimension could be specified by depth information.
- **p. 2 / 1 Introduction - extractive body cue:** To provide the supervision signal, the system computes the difference in coverage of the cloth before and after each action - the delta-coverage - from ...
- **p. 3 / 3 Method - extractive body cue:** Meanwhile, dynamic actions largely rely on cloths' mass combined with a high-velocity throw to do most of its work.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | The policy interacts with the cloth until it reaches 10 timesteps or predicts grasps on the workspace. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | In real, the simulation policy is deployed to collect real world experience on 150 Normal Rect episodes (257 steps), optimized on both ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | In real, the simulation policy is deployed to collect real world experience on 150 Normal Rect episodes (257 steps), optimized on both ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 Method - extractive body cue:** After training in simulation, we finetune and evaluate the model in the real world (Sec.
- **p. 5 / 3 Method - extractive body cue:** The network is trained using the Adam optimizer with a learning rate of 1e-3 and a weight decay of 1e-6.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** value, network, fully, convolutional, neural, nine, residual, blocks, layers, first, last, layer, takes, input, RGB, images, top-down, image, policy, evaluates.
- **Relevant PDF headings:** 3 Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below). | p. 9 (4.4 Results), p. 7 (4 Evaluation) |
| Grasp / trajectory generation | Compared to the quasi-static baselines, [FlingBot] increases the coverage by +52.0%, which is roughly twice that of the quasi-static baselines ( +27.1%, ... | p. 8 (4.4 Results), p. 9 (4.4 Results) |
| Contact execution / correction | While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps ... | p. 7 (4 Evaluation), p. 9 (4.4 Results) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Action Primitives. The dynamic Fling primitive starts with a two-arm grasp at the left L and right R grasp locations with center point ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- ...
- **p. 9 / 4.4 Results - extractive body cue:** We discuss more of real world grasp failures in Sec.
- **p. 9 / 4.4 Results - extractive body cue:** The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below).
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed
- **p. 8 / 4 Evaluation - extractive body cue:** 1, [Fling-Reg] completely fails to perform the task, demonstrating the advantage of encoding inductive biases which leverage equivariances in the problem structure.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 9: To minimize collisions, arms should grasp points closer to their side (a) and be a reasonable distance away from each other (b). 6.6 ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 4 (3 Method), objective p. 4 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), temporal p. 5 (3 Method), p. 7 (4 Evaluation), p. 8 (4 Evaluation), p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
