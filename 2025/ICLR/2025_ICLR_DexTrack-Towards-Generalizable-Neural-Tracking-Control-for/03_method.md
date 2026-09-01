# Method - DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ajSmXqgS24; PDF retrieval source: https://arxiv.org/pdf/2502.09614. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD)): Dexterous manipulation "tracking" involves controlling a robotic hand to mimic a kinematic hand-object state sequence, the goal trajectory, denoted as {ˆsn}N n=0.

## Method Body Digest

- **p. 3 / 3 METHOD - extractive body cue:** Dexterous manipulation "tracking" involves controlling a robotic hand to mimic a kinematic hand-object state sequence, the goal trajectory, denoted as {ˆsn}N n=0.
- **p. 4 / 3 METHOD - extractive body cue:** Published as a conference paper at ICLR 2025 Expert Action Trajectory {𝒂!", … , 𝒂#", … } t Robot Tracking Demonstrations Kinematic
- **p. 3 / 3 METHOD - extractive body cue:** A "tracking demonstration" pairs a kinematic reference {ˆsn} with an expert action sequence {aL n}, guiding the robot from s0 = ˆs0 to 3
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve the challenging goal above, we draw three key observations: 1) learning is crucial for handling heterogeneous reference motion noises and transferring data prior ...
- **p. 3 / 3 METHOD - extractive body cue:** These "kinematic references" are retargeted from human manipulation trajectories, with ˆsn representing the robot hand state and object pose at timestep n.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Based upon the previous observations, we propose DexTrack, a novel neural tracking controller for dexterous manipulation, guided by human references.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Robotic dexterous manipulation refers to the ability of a robot hand skillfully handling and manipulating objects for various target states with precision and adaptability.

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are threefold: • We present a generalizable neural tracking controller that progressively improves its performance through iterative mining and incorporating high-quality tracking demonstrations. ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Based upon the previous observations, we propose DexTrack, a novel neural tracking controller for dexterous manipulation, guided by human references.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To make sure the data flywheel functions effectively, we introduce two key designs.

## Source Evidence Cues

- **p. 3 / 3 METHOD - extractive body cue:** Dexterous manipulation "tracking" involves controlling a robotic hand to mimic a kinematic hand-object state sequence, the goal trajectory, denoted as {ˆsn}N n=0.
- **p. 4 / 3 METHOD - extractive body cue:** Published as a conference paper at ICLR 2025 Expert Action Trajectory {𝒂!", … , 𝒂#", … } t Robot Tracking Demonstrations Kinematic
- **p. 3 / 3 METHOD - extractive body cue:** A "tracking demonstration" pairs a kinematic reference {ˆsn} with an expert action sequence {aL n}, guiding the robot from s0 = ˆs0 to 3
- **Detected method headings:** 3 METHOD (p. 3); A.2 TRACKING CONTROLLER TRAINING (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Dexterous manipulation "tracking" involves controlling a robotic hand to mimic a kinematic hand-object state sequence, the goal trajectory, denoted as {ˆsn}N n=0. | p. 3 (3 METHOD), p. 4 (3 METHOD) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Published as a conference paper at ICLR 2025 Expert Action Trajectory {𝒂!", … , 𝒂#", … } t Robot Tracking Demonstrations Kinematic | p. 4 (3 METHOD), p. 3 (3 METHOD) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | A "tracking demonstration" pairs a kinematic reference {ˆsn} with an expert action sequence {aL n}, guiding the robot from s0 = ˆs0 ... | p. 3 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | achieve, challenging, goal, above, draw, three, observations, learning, crucial, handling, heterogeneous, reference, motion, noises | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | achieve, challenging, goal, above, draw, three, observations, learning, crucial, handling | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | contributions, threefold, present, generalizable, neural, tracking, controller, progressively, improves, performance | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | not recovered | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve the challenging goal above, we draw three key observations: 1) learning is crucial for handling heterogeneous reference motion noises and transferring data prior ...
- **p. 3 / 3 METHOD - extractive body cue:** These "kinematic references" are retargeted from human manipulation trajectories, with ˆsn representing the robot hand state and object pose at timestep n.
- **p. 3 / 3 METHOD - extractive body cue:** Dexterous manipulation "tracking" involves controlling a robotic hand to mimic a kinematic hand-object state sequence, the goal trajectory, denoted as {ˆsn}N n=0.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Based upon the previous observations, we propose DexTrack, a novel neural tracking controller for dexterous manipulation, guided by human references.
- **p. 4 / 3 METHOD - extractive body cue:** Published as a conference paper at ICLR 2025 Expert Action Trajectory {𝒂!", … , 𝒂#", … } t Robot Tracking Demonstrations Kinematic
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Robotic dexterous manipulation refers to the ability of a robot hand skillfully handling and manipulating objects for various target states with precision and adaptability.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | These "kinematic references" are retargeted from human manipulation trajectories, with ˆsn representing the robot hand state and object pose at timestep n. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Thus, we primarily compare our method with model-free approaches: 1) DGrasp (Christen et al., 2022): Adapted to track by dividing sequences into ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Thus, we primarily compare our method with model-free approaches: 1) DGrasp (Christen et al., 2022): Adapted to track by dividing sequences into ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In simulation, we use the Allegro hand, with URDF adapted from IsaacGymEnvs (Makoviychuk et al., 2021), and in real-world experiments, the LEAP hand (Shaw et ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Dexterous, manipulation, tracking, involves, controlling, robotic, hand, mimic, kinematic, hand-object, state, sequence, goal, trajectory, denoted, Published, conference, ICLR, Expert, Action.
- **Relevant PDF headings:** 3 METHOD (p. 3); A.2 TRACKING CONTROLLER TRAINING (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Tested on two HOI datasets featuring complex daily manipulation tasks, our method is assessed through both simulation and real-world evaluations (see Sec. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Grasp / trajectory generation | As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across ... | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Contact execution / correction | As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across ... | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We ablate these strategies by creating two variants: "Ours (w/o data, w/o homotopy)", where the dataset is built by optimizing each trajectory without prior knowledge, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 5 ABLATION STUDIES Diversity and quality of robot tracking demonstrations.
- **p. 17 / B.1 DEXTEROUS MANIPULATION TRACKING CONTROL - extractive body cue:** In Table 6, we present the full evaluation results on all five types of metrics of each model traiend in the ablation study regarding the ...
- **p. 22 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** All the models are trained in a single card without multi-gpu parallelization.
- **p. 22 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** Directly training PPO without any supervision is the most efficient approach while the performance lagged behind due to no proper guidance.
- **p. 15 / Figure/Table caption - extractive body cue:** Table 3: Weights of different reward components. wo,p wo,q wwrist · wtrans wwrist · wornt wfinger Weight 1.0
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 10: Failure cases in real-world experiments. Please refer to our website for animated

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD), objective 본문 anchor 없음, temporal p. 3 (3 METHOD), p. 8 (4 EXPERIMENTS), p. 18 (B.2 REAL-WORLD EVALUATIONS), p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS), p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS), p. 22 (C ADDITIONAL EXPERIMENTAL DETAILS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
