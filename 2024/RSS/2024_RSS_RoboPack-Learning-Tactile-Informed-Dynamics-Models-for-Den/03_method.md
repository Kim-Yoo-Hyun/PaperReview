# Method - RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p130.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD)): For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.

## Method Body Digest

- **p. 5 / III. METHOD - extractive body cue:** For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 4 / III. METHOD - extractive body cue:** F x, F y are the mean of local force vectors across spatial dimensions, and /Q/ is defined as /Q/ = r max i,j /qx ...
- **p. 5 / III. METHOD - extractive body cue:** Concretely, we use Model Predictive Path Integral (MPPI) to perform this optimization [58].
- **p. 3 / III. METHOD - extractive body cue:** To efficiently learn dynamics from real-world multi-object interaction data, we would like to extract lower-dimensional representations of observations like keypoints.
- **p. 3 / III. METHOD - extractive body cue:** They are used together in the following way: First, the perception system extracts particles from the scene as a visual representation ovis and encodes tactile ...
- **p. 6 / III. METHOD - extractive body cue:** After execution, it performs state estimation with the history of observations and re-plans for the next execution.
- **p. 4 / III. METHOD - extractive body cue:** The objective is to find a sequence of actions a0, ..., aH-1 to minimize a cost function J between the final states and a given ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction ...
- **p. 4 / III. METHOD - extractive body cue:** For multi-object packing settings with significant occlusion, we introduce an objective that constrains tracked points to be near the corresponding object masks, providing more consistent ...

## Source Evidence Cues

- **p. 5 / III. METHOD - extractive body cue:** For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 4 / III. METHOD - extractive body cue:** F x, F y are the mean of local force vectors across spatial dimensions, and /Q/ is defined as /Q/ = r max i,j /qx ...
- **p. 5 / III. METHOD - extractive body cue:** Concretely, we use Model Predictive Path Integral (MPPI) to perform this optimization [58].
- **p. 3 / III. METHOD - extractive body cue:** To efficiently learn dynamics from real-world multi-object interaction data, we would like to extract lower-dimensional representations of observations like keypoints.
- **p. 3 / III. METHOD - extractive body cue:** They are used together in the following way: First, the perception system extracts particles from the scene as a visual representation ovis and encodes tactile ...
- **p. 6 / III. METHOD - extractive body cue:** After execution, it performs state estimation with the history of observations and re-plans for the next execution.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining ... | p. 5 (III. METHOD), p. 4 (III. METHOD) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge ... | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | F x, F y are the mean of local force vectors across spatial dimensions, and /Q/ is defined as /Q/ = r ... | p. 4 (III. METHOD), p. 5 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive body cue:** The objective is to find a sequence of actions a0, ..., aH-1 to minimize a cost function J between the final states and a given ...
- **p. 5 / III. METHOD - extractive body cue:** (9) Previous works [48, 50, 49] use the earth mover's distance (EMD) or chamfer distance (CD) as the training loss, but these provide noisier gradients ...
- **p. 5 / III. METHOD - extractive body cue:** Model-Predictive Control With the learned state estimator and dynamics predictor, we perform planning toward a particular goal by optimizing a cost function on predicted states ...
- **p. 4 / III. METHOD - extractive body cue:** We optimize a translation and rotation transformation for each object with this objective.
- **p. 3 / III. METHOD - extractive body cue:** Overview The objective of RoboPack is to manipulate objects with unknown physical properties in environments with heavy occlusions like dense packing.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 5 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | formulate, problem, define, observation, space, state, action, Secondly, estimator, infers, object, states, prior, interactions | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | formulate, problem, define, observation, space, state, action, Secondly, estimator, infers | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | tackle, challenges, learn, dynamics, directly, real, physical, interaction, data, powerful | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | objective, find, sequence, actions, aH-1, minimize, cost, function, between, final | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** To formulate this problem, we define the observation space as O, the state space as S, and the action space as A.
- **p. 3 / III. METHOD - extractive body cue:** Secondly, the state estimator g infers object states s from any prior interactions, which includes a single visual frame ovis 0 , the subsequent tactile ...
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 5 / III. METHOD - extractive body cue:** We train the state estimator and dynamics predictor jointly end-to-end on trajectories of sequential interaction data containing observations and robot actions.
- **p. 5 / III. METHOD - extractive body cue:** The dynamics predictor f is constructed similarly to the state estimator g, with two key differences: (i) it does not use tactile observations as input, ...
- **p. 4 / III. METHOD - extractive body cue:** 2) Tactile Perception: As shown in the top right of Figure 2, our tactile perception module takes global force-torque and local force vectors as input ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | The classifier's improving accuracy across timesteps underscores the state estimator's proficiency in extracting and integrating box-specific information from the tactile observation history. | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize ... | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / III. METHOD - extractive body cue:** For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize to sequences four ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, trajectory, length, state, estimator, estimates, first, states, dynamics, predictor, predicts, remaining, Estimation, Latent, Physics, Vector, Inference, real-world, robotic, manipulation.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks. | p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP) |
| Contact / dynamics inference | Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline methods in the Non-prehensile Box Pushing ... | p. 8 (Figure/Table caption), p. 8 (V. EXPERIMENTS) |
| Force-aware action correction | Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii. | p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTS - extractive body cue:** RoboPack (no tactile): To study the effects of using tactile sensing in state estimation and dynamics prediction, we evaluate this ablation of our method, which ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** In contrast, when using tactile and visual observations directly as the state representation (RoboCook + tactile), the performance is even worse than RoboPack without tactile ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** However, this is impractical for this task, because it is infeasible to obtain corresponding object models for the diverse and complex objects in this task ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** This can be viewed as an adaptation of previous work [29, 48, 50, 49] to include an additional tactile observation component.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** To qualitatively inspect the learned representations, we perform principal component analysis, reducing the learned latent vectors from R16 to R2.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), objective p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), temporal p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 4 (III. METHOD), p. 5 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics requires interactive feedback. (p. 4, III. METHOD).
- **Objective/update evidence:** We optimize a translation and rotation transformation for each object with this objective. (p. 4, III. METHOD).
- **Temporal/runtime evidence:** Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize to sequences four times longer in this case. (p. 8, V. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
