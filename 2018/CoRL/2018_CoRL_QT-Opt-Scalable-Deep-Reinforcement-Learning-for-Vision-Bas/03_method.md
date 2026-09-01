# Method - QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1806.10293; PDF retrieval source: https://arxiv.org/pdf/1806.10293. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (Method), p. 7 (Method), p. 7 (Method), p. 8 (Method)): 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm called QT-Opt, a distributed optimization ...

## Method Body Digest

- **p. 8 / Method - extractive PDF cue:** 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm ...
- **p. 7 / Method - extractive PDF cue:** Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.
- **p. 7 / Method - extractive PDF cue:** Dataset Test Bin emptying first 10 first 20 first 30 QT-Opt (ours) 580k off-policy + 28k on-policy 96% 88% 88% 76% Levine et al.
- **p. 8 / Method - extractive PDF cue:** Although the training data included no more than ten objects at a time, the policy can still grasp in dense clutter, as shown in Fig.
- **p. 7 / Method - extractive PDF cue:** This prior method does not reason about long-horizon rewards: although it can be used in closed-loop, the policy greedily optimizes for grasp success at the ...
- **p. 8 / Method - extractive PDF cue:** All of these behaviors emerge automatically from optimizing the grasp success probability via QT-Opt.
- **p. 7 / Method - extractive PDF cue:** Notably, all of these examples emerge automatically from training the policy to optimize grasp success.
- **p. 2 / 1 Introduction - extractive PDF cue:** To make maximal use of this diverse dataset, we propose an off-policy training method based on a continuous-action generalization of Q-learning, which we call QTOpt.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** We show that our method attains a high success rate across a range of objects not seen during training, and our qualitative experiments show that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Each cell (left) consists of a KUKA LBR IIWA arm with a two-finger gripper and an over-theshoulder RGB camera.
- **p. 7 / Method - extractive PDF cue:** The performance of our method is shown in Table 1.

## Source Evidence Cues

- **p. 8 / Method - extractive PDF cue:** 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm ...
- **p. 7 / Method - extractive PDF cue:** Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.
- **p. 7 / Method - extractive PDF cue:** Dataset Test Bin emptying first 10 first 20 first 30 QT-Opt (ours) 580k off-policy + 28k on-policy 96% 88% 88% 76% Levine et al.
- **p. 8 / Method - extractive PDF cue:** Although the training data included no more than ten objects at a time, the policy can still grasp in dense clutter, as shown in Fig.
- **Detected method headings:** Method (p. 7); C.1 Effect of Off-Policy Training on Performance (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based ... | p. 8 (Method), p. 7 (Method) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection. | p. 7 (Method), p. 7 (Method) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Dataset Test Bin emptying first 10 first 20 first 30 QT-Opt (ours) 580k off-policy + 28k on-policy 96% 88% 88% 76% Levine ... | p. 7 (Method), p. 8 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / Method - extractive PDF cue:** This prior method does not reason about long-horizon rewards: although it can be used in closed-loop, the policy greedily optimizes for grasp success at the ...
- **p. 8 / Method - extractive PDF cue:** All of these behaviors emerge automatically from optimizing the grasp success probability via QT-Opt.
- **p. 7 / Method - extractive PDF cue:** Notably, all of these examples emerge automatically from training the policy to optimize grasp success.
- **p. 8 / Method - extractive PDF cue:** 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Discussion, Future, presented, framework, scalable, robotic, reinforcement, learning, sensory, inputs, images, algorithm, called, QT-Opt | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Discussion, Future, presented, framework, scalable, robotic, reinforcement, learning, sensory, inputs | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | attains, high, success, rate, across, range, objects, seen, during, training | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | prior, does, reason, about, long-horizon, rewards, although, closed-loop, policy, greedily | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / Method - extractive PDF cue:** 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To make maximal use of this diverse dataset, we propose an off-policy training method based on a continuous-action generalization of Q-learning, which we call QTOpt.
- **p. 2 / 1 Introduction - extractive PDF cue:** This kind of dynamic closed-loop grasping is likely to be much more robust to unpredictable object physics, limited sensory information (e.g., monocular camera inputs instead ...
- **p. 7 / Method - extractive PDF cue:** In contrast to most grasping systems, our method performs general closed-loop control with image observations, and can choose to reposition, open, or close the gripper ...
- **p. 8 / Method - extractive PDF cue:** Our results demonstrate that reinforcement learning with vision-based inputs can scale to large datasets and very large models, and can enable policies that generalize effectively ...
- **p. 7 / Method - extractive PDF cue:** What types of strategies does this policy adopt?
- **p. 1 / 1 Introduction - extractive PDF cue:** It thus serves as a microcosm of the larger robotic manipulation problem, providing a challenging and practically applicable model problem for experimenting with generalization and ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | At each time step, the policy observes the image from the robot's camera (see Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | At each time step t, the algorithm chooses an action, transitions to a new state, and receives a reward r(st, at). | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | On the bin emptying experiment, our method emptied the bin in 30 grasps or less in 2 of the 5 trials, while ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / Method - extractive PDF cue:** 7 Discussion and Future Work We presented a framework for scalable robotic reinforcement learning with raw sensory inputs such as images, based on an algorithm ...
- **p. 7 / Method - extractive PDF cue:** Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.
- **p. 8 / Method - extractive PDF cue:** Although the training data included no more than ten objects at a time, the policy can still grasp in dense clutter, as shown in Fig.
- **p. 7 / Method - extractive PDF cue:** Effective off-policy training is valuable as it allows for rapid iteration on hyperparameters and architecture design without any data collection.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Discussion, Future, presented, framework, scalable, robotic, reinforcement, learning, sensory, inputs, images, algorithm, called, QT-Opt, distributed, optimization, combination, off-policy, on-policy, training.
- **Relevant PDF headings:** Method (p. 7); C.1 Effect of Off-Policy Training on Performance (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Our results demonstrate that reinforcement learning with vision-based inputs can scale to large datasets and very large models, and can enable policies ... | p. 8 (Method), p. 8 (Method) |
| Grasp / trajectory generation | Table 5: Off-policy performance with and without clipped Double-Q Learning. Data efficiency As discussed in Section 5 we collected 580k grasp attempts ... | p. 14 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Contact execution / correction | Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without ... | p. 7 (Figure/Table caption), p. 7 (Method) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative results in terms of grasp success rate on test objects. Policies are evaluated with object replacement (test) and without (bin emptying), with ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Off-policy and on-policy ablation of termination condition. Quantitative experiments The performance of our algorithm is evaluated empirically in a set of grasping experiments. ...
- **p. 7 / Method - extractive PDF cue:** The results show both a variant of our method that is trained entirely using off-policy data, without any additional data collection from the latest policy, ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Table 8: Data efficiency comparison in simulation. We argue that the algorithm from Levine et al. [27] is less data efficient because it optimizes a ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 2: Off-policy ablation over state representation. Discount and Reward Definition To encourage faster grasps, we experimented with decreasing discount and adding a small reward ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 5: Off-policy performance with and without clipped Double-Q Learning. Data efficiency As discussed in Section 5 we collected 580k grasp attempts across 7 robots ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 5: Illustrations of the bin emptying experiment (a). The (a, right) shows a very small object getting stuck in the corner and requiring a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (Method), p. 7 (Method), p. 7 (Method), p. 8 (Method), objective p. 7 (Method), p. 8 (Method), p. 7 (Method), p. 8 (Method), temporal p. 3 (2 Related Work), p. 4 (2 Related Work), p. 6 (2 Related Work), p. 6 (2 Related Work), p. 7 (Method), p. 7 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
