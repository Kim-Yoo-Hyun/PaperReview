# Method - Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p036.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p036.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (B. Learning-Based Deformable Modeling), p. 5 (B. Model Components), p. 3 (B. Learning-Based Deformable Modeling), p. 4 (B. Model Components), p. 2 (A. Physics-Based Deformable Modeling), p. 2 (B. Learning-Based Deformable Modeling)): Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ‘encoder to extract particle features ...

## Method Body Digest

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ...
- **p. 5 / B. Model Components - extractive body cue:** We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** A detailed description of the model is provided in Section IIL-A and III-B, We introduce the data collection pipeline and the models training method in ...
- **p. 4 / B. Model Components - extractive body cue:** We use PointNet [36] as the encoder for its efficiency and strong performance in extracting 3D point features.
- **p. 2 / A. Physics-Based Deformable Modeling - extractive body cue:** While our method uses a hybrid particle-grid representation similar to MPM, we leverage neural networks as message integrators and reduce dependence on full-state information as ...
- **p. 2 / B. Learning-Based Deformable Modeling - extractive body cue:** Learning-based dynamics models, which use deep neural networks to model the future evolution of dynamical systems, have demonstrated effectiveness across various robotic tasks [1 1, ...
- **p. 4 / B. Model Components - extractive body cue:** GVE is inspired from MPM approaches and we use it for grasped interactions and object-ground interaction.
- **p. 5 / B. Model Components - extractive body cue:** With a specified cost function, the MPC framework rolls out the dynamics model using sampled actions and optimizes the total cost.

## Design Rationale

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By combining object particles with spatial grids, our framework parameterizes dynamics in both Lagrangian and Eulerian coordinates, drawing an analogy to physics-based deformable object simulation ...

## Source Evidence Cues

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ...
- **p. 5 / B. Model Components - extractive body cue:** We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** A detailed description of the model is provided in Section IIL-A and III-B, We introduce the data collection pipeline and the models training method in ...
- **p. 4 / B. Model Components - extractive body cue:** We use PointNet [36] as the encoder for its efficiency and strong performance in extracting 3D point features.
- **p. 2 / A. Physics-Based Deformable Modeling - extractive body cue:** While our method uses a hybrid particle-grid representation similar to MPM, we leverage neural networks as message integrators and reduce dependence on full-state information as ...
- **p. 2 / B. Learning-Based Deformable Modeling - extractive body cue:** Learning-based dynamics models, which use deep neural networks to model the future evolution of dynamical systems, have demonstrated effectiveness across various robotic tasks [1 1, ...
- **p. 4 / B. Model Components - extractive body cue:** GVE is inspired from MPM approaches and we use it for grasped interactions and object-ground interaction.
- **Detected method headings:** A. Physics-Based Deformable Modeling (p. 2); B. Learning-Based Deformable Modeling (p. 2); B. Model Components (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first ... | p. 3 (B. Learning-Based Deformable Modeling), p. 5 (B. Model Components) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions. | p. 5 (B. Model Components), p. 3 (B. Learning-Based Deformable Modeling) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | A detailed description of the model is provided in Section IIL-A and III-B, We introduce the data collection pipeline and the models ... | p. 3 (B. Learning-Based Deformable Modeling), p. 4 (B. Model Components) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. Model Components - extractive body cue:** We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions.
- **p. 5 / B. Model Components - extractive body cue:** With a specified cost function, the MPC framework rolls out the dynamics model using sampled actions and optimizes the total cost.
- **p. 4 / B. Model Components - extractive body cue:** Simply put, the operator g®™' changes the velocities on the grid to match physical constraints.
- **p. 4 / B. Learning-Based Deformable Modeling - extractive body cue:** Empirically, we set lo, ly,ls to 100 ‘or 50 and 5 to Lem or 2cm to balance computational cost and resolution.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (B. Model Components), p. 5 (B. Model Components), p. 5 (B. Model Components), p. 3 (B. Learning-Based Deformable Modeling).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, kinematic, states, particles, input, predicts, spatial, velocity, field, fixed, grid, points, Given, particle | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | takes, kinematic, states, particles, input, predicts, spatial, velocity, field, fixed | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | model, updates, particle, positions, predicted, velocities, perform, iterative, rollouts, framework | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | apply, Model-Predictive, Path, Integral, MPPD, trajectory, optimization, algorithm, minimize, cost | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** It takes the kinematic states Of the particles as input and predicts a spatial velocity field at fixed grid points.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ...
- **p. 2 / A. Physics-Based Deformable Modeling - extractive body cue:** While our method uses a hybrid particle-grid representation similar to MPM, we leverage neural networks as message integrators and reduce dependence on full-state information as ...
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The core of this framework is a dynamics function that predicts the future motion of each particle based on its current and historical states, as ...
- **p. 4 / B. Model Components - extractive body cue:** This injects action information into particle features but does not explicitly force particles to move at a prescribed velocity, thus supporting nonprehensile ‘manipulation.
- **p. 4 / B. Model Components - extractive body cue:** Here, we represent the robot gripper with additional particles that carry gripper action information, and fuse this into the object point cloud.
- **p. 5 / B. Model Components - extractive body cue:** The poiats X can either be sampled from Xcq_ or obtained from additional point cloud observations within the same coordinate frame with X¢s.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | and standard deviation of the prediction error over a 3-second horizon, The best results are highlighted | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | and the LPIPS score measures appearance-wise similarities between predicted frames and ground truth video recordings. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** A detailed description of the model is provided in Section IIL-A and III-B, We introduce the data collection pipeline and the models training method in ...
- **p. 5 / B. Model Components - extractive body cue:** Model training begins from a given point cloud at time t, followed by iterative dynamics model rollouts for K° steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, particle, positions, velocities, fused, multi-view, depth, images, input, model, predicts, dense, per-particle, motion, first, point, encoder, extract, features, predict.
- **Relevant PDF headings:** A. Physics-Based Deformable Modeling (p. 2); B. Learning-Based Deformable Modeling (p. 2); B. Model Components (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | ‘€) Box: Two robot arms are used to open and close shipping boxes. | p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup) |
| Filtering / recovery | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Monitoring / re-entry | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | p. 5 (IV. EXPERIMENTS), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (B. Learning-Based Deformable Modeling), p. 5 (B. Model Components), p. 3 (B. Learning-Based Deformable Modeling), p. 4 (B. Model Components), p. 2 (A. Physics-Based Deformable Modeling), p. 2 (B. Learning-Based Deformable Modeling), objective p. 5 (B. Model Components), p. 5 (B. Model Components), p. 4 (B. Model Components), p. 4 (B. Learning-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling), temporal p. 7 (A. Experiment Setup), p. 7 (A. Experiment Setup), p. 3 (B. Learning-Based Deformable Modeling), p. 5 (B. Model Components), p. 8 (C. Sparse-View Dynamics Prediction), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
