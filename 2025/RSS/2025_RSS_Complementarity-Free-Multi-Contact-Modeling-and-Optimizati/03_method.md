# Method - Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p111.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p111.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 5 (B. New Complementarty-Free Multi-Contact Model), p. 5 (C. Physical Interpretation of the New Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model)): First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs [59], we approximate the complementarity ...

## Method Body Digest

- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** 1) Nonconvex Complementarity Contact Models: Rigid body contact dynamics is traditionally formulated using complermentarity models [S1, 49, 52]: it enforces no interpenetration and no contact ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 5 / C. Physical Interpretation of the New Model - extractive body cue:** The total force consists of two components: (i) the non-contact force b (e.g., gravity and actuation forces) shown in green arrows in Fig.
- **p. 3 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** For simplicity, we model a manipulation system using the quasi-dynamic formulation (34, 14, 1, 41], which primarily captures the positional displacement of a contact-rich system ...
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system state qf encountered ...
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** Directly using the QP-based contact ‘model (7) in MPC (8) leads to a nested optimization, which is difficult to solve due to the non-smooth behavior ...
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** With qo, (8) searches for the optimal input sequence (ty and Us, are control bounds), by minimizing the path c(-) and final cost V(-).

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 1 / Front matter - extractive body cue:** 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols.
- **p. 2 / Abstract - extractive body cue:** Our method sets a new benchmark for model-based contact-rich dexterous manipulation: « Highly versatile dexterity: 96.5% average success rate across all objects and environments « ...

## Source Evidence Cues

- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** 1) Nonconvex Complementarity Contact Models: Rigid body contact dynamics is traditionally formulated using complermentarity models [S1, 49, 52]: it enforces no interpenetration and no contact ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 5 / C. Physical Interpretation of the New Model - extractive body cue:** The total force consists of two components: (i) the non-contact force b (e.g., gravity and actuation forces) shown in green arrows in Fig.
- **p. 3 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** For simplicity, we model a manipulation system using the quasi-dynamic formulation (34, 14, 1, 41], which primarily captures the positional displacement of a contact-rich system ...
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system state qf encountered ...
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** Directly using the QP-based contact ‘model (7) in MPC (8) leads to a nested optimization, which is difficult to solve due to the non-smooth behavior ...
- **Detected method headings:** A. Rigid Body Multi-contact Models (p. 2); A. Optimization-based Quasi-Dynamic Contact Model (p. 3); IV. COMPLEMENTARITY-FREE MULTI-CONTACT MODEL (p. 4); A. Duality of Optimization-based Contact Model (p. 4); B. New Complementarty-Free Multi-Contact Model (p. 5); C. Physical Interpretation of the New Model (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] ... | p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | 1) Nonconvex Complementarity Contact Models: Rigid body contact dynamics is traditionally formulated using complermentarity models [S1, 49, 52]: it enforces no interpenetration ... | p. 2 (A. Rigid Body Multi-contact Models), p. 5 (B. New Complementarty-Free Multi-Contact Model) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1. | p. 5 (B. New Complementarty-Free Multi-Contact Model), p. 5 (C. Physical Interpretation of the New Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** With qo, (8) searches for the optimal input sequence (ty and Us, are control bounds), by minimizing the path c(-) and final cost V(-).
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** A shared feature is that those methods ultimately need 0 solve a residual equation for contact constraint resolution, and differentiablity is obtained via implicit function ...
- **p. 3 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** The first equation is the motion of the object with «ML, & R"*" the regularized mass matrix for the object (¢ > 0 is the ...
- **p. 4 / A. Duality of Optimization-based Contact Model - extractive body cue:** The dual solution to the regularized dual problem (12) satisfies the following dual complementarity constraints
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** [58] proposed implicit complementarity, converting all Constraints to unconstrained optimization with intermediate variables.
- **p. 3 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** The time-stepping equation of the quasi-dynamic model is
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (B. Planning and Control with Contact Dynamics), p. 4 (A. Duality of Optimization-based Contact Model), p. 4 (A. Duality of Optimization-based Contact Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | implementation, creates, closed-loop, control, effect, real, system, feedback, state, input, manipulation, MPC, policy, implemented | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | implementation, creates, closed-loop, control, effect, real, system, feedback, state, input | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | consistently, achieves, state-of-the, average, success, rate, across, objects, complementarty-free, multi-contact | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | searches, optimal, input, sequence, control, bounds, minimizing, path, final, cost | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** This implementation creates « closed-loop control effect on the real system, ie., feedback from system state qf to control input 1 (qi
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system state qf encountered ...
- **p. 3 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** For simplicity, we model a manipulation system using the quasi-dynamic formulation (34, 14, 1, 41], which primarily captures the positional displacement of a contact-rich system ...
- **p. 2 / Abstract - extractive body cue:** (I) Closed-form and differentiable timestepping: the next system state is a closed-form differentiable function of the current state and input, thus avoiding solving complementarity problems ...
- **p. 2 / Abstract - extractive body cue:** (II) Automatic satisfaction with Coulomb's friction law in a single term: the new model resolves the normal and frictional contact forces using a single term ...
- **p. 3 / C. Reinforcement Learning for Dexterous Manipulation - extractive body cue:** Our proposed method aims to bridge this gap and even surpass state-of-the-art RL in suecess rate and manipulation accuracy.
- **p. 1 / Front matter - extractive body cue:** Wanxin Jin Arizona State University
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Fortunately, in a receding horizon framework, one can do once collision detection foreach encountered realsystem state qy = af! | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | 1s closed-form time stepping, uutomatic satisfaction with Coulomb's friction | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs ...
- **p. 4 / A. Optimization-based Quasi-Dynamic Contact Model - extractive body cue:** In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system state qf encountered ...
- **p. 10 / B. MPC Setting and Results - extractive body cue:** Final errors are computed using the last 20 rollout steps in succesful ils,
- **p. 9 / B. MPC Setting and Results - extractive body cue:** both calculated using the last 20 steps of a MPC rollout.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, closed-form, contact, constraint, resolution, model, builds, optimization-based, dynamics, instead, solving, primal, dual, programs, approximate, complementarity, constraints, space, explicit, form.
- **Relevant PDF headings:** A. Rigid Body Multi-contact Models (p. 2); A. Optimization-based Quasi-Dynamic Contact Model (p. 3); IV. COMPLEMENTARITY-FREE MULTI-CONTACT MODEL (p. 4); A. Duality of Optimization-based Contact Model (p. 4); B. New Complementarty-Free Multi-Contact Model (p. 5); C. Physical Interpretation of the New Model (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | ABLE Il: The model setting for all objects and tasks. | p. 9 (B. MPC Setting and Results), p. 9 (B. MPC Setting and Results) |
| Grasp / trajectory generation | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | p. 10 (B. MPC Setting and Results), p. 8 (Figure/Table caption) |
| Contact execution / correction | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |

## Failure and Ablation Link

- **p. 10 / B. MPC Setting and Results - extractive body cue:** Without ground support, the three fingertips
- **p. 9 / B. MPC Setting and Results - extractive body cue:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 17: An failure case for stick reorientation,
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical velocity trajectories, respectively. Compared to MuloCo, our ...
- **p. 9 / A. Environment and Task Setup - extractive body cue:** The fingertips must coordinate to prevent the object from falling while moving it to the target.
- **p. 10 / B. MPC Setting and Results - extractive body cue:** Fil postion Vial quaeiion MPC soe Succes ust prevent the object from falling while moving it to 8% Shor 8) ere 8) ng time te ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 5 (B. New Complementarty-Free Multi-Contact Model), p. 5 (C. Physical Interpretation of the New Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), objective p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Duality of Optimization-based Contact Model), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), temporal p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 6 (V. COMPLEMENTARITY-FREE CONTACT-IMPLICIT MPC), p. 1 (Abstract), p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 5 (C. Physical Interpretation of the New Model).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
