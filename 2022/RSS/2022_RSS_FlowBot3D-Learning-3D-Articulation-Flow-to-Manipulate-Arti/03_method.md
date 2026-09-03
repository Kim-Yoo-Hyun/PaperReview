# Method - FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.04382; PDF retrieval source: https://arxiv.org/pdf/2205.04382. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE)): A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial observation ˆF0 ←fθ(O0, [M0]), Predict ...

## Method Body Digest

- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a new supervised pair ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Our objective is to choose a contact point and force direction (p∗, F∗) that maximizes the acceleration a of the articulation's child link.
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** For robot control, we use a sampling-based planner, MoveIt!
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We first present the theoretical grounding behind the intuition of our method, and we slowly relax assumptions and approximations to create a system that articulates ...
- **p. 3 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** First, our representation describes the instantaneous motion of a link, whereas the FormNet formulation predicts the current absolute displacement of a part from a reference ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** The system then chooses the point that has the maximum flow vector magnitude and deploys motion planning to make contact with the chosen point using ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We define the objective of minimizing the L2 error of the predicted flow: LMSE = X i //Ft,i -fθ(Ot)i//2 (4) where i indexes over the ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present FlowBot3D, a deep 3D visionbased robotic system that predicts dense per-point motion of an articulated object in 3D space, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose to separate this problem into one of "affordance learning" and "motion planning." If a robot can predict the potential ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We first present the theoretical grounding behind the intuition of our method, and we slowly relax assumptions and approximations to create a system that articulates ...

## Source Evidence Cues

- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a new supervised pair ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Our objective is to choose a contact point and force direction (p∗, F∗) that maximizes the acceleration a of the articulation's child link.
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** For robot control, we use a sampling-based planner, MoveIt!
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We first present the theoretical grounding behind the intuition of our method, and we slowly relax assumptions and approximations to create a system that articulates ...
- **p. 3 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** First, our representation describes the instantaneous motion of a link, whereas the FormNet formulation predicts the current absolute displacement of a part from a reference ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** The system then chooses the point that has the maximum flow vector magnitude and deploys motion planning to make contact with the chosen point using ...
- **Detected method headings:** 2) A novel 3D vision neural network architecture (which (p. 1); III. METHOD - FROM THEORY TO PRACTICE (p. 2); Method (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction ... | p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 5 (III. METHOD - FROM THEORY TO PRACTICE) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a ... | p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Our objective is to choose a contact point and force direction (p∗, F∗) that maximizes the acceleration a of the articulation's child ... | p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Our objective is to choose a contact point and force direction (p∗, F∗) that maximizes the acceleration a of the articulation's child link.
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We define the objective of minimizing the L2 error of the predicted flow: LMSE = X i //Ft,i -fθ(Ot)i//2 (4) where i indexes over the ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We know that the ideal attachment point is the location on a part where the flow has the highest magnitude in order to achieve the ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a new supervised pair ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Each joint connects a parent link (often the fixedworld link) and a child link, which can move freely subject to the articulation constraints.
- **p. 3 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Without loss of accuracy, we choose to omit a rigorous screw-theoretic treatment of articulated objects in favor of an explanation that requires only basic knowledge ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | General, Policy, Articulation, Flow, Algorithm, FlowBot3D, manipulation, Require, parameters, trained, prediction, network, Initial, observation | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | General, Policy, Articulation, Flow, Algorithm, FlowBot3D, manipulation, Require, parameters, trained | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, FlowBot3D, deep, visionbased, robotic, system, predicts, dense, per-point, motion | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | objective, choose, contact, point, force, direction, maximizes, acceleration, articulation, child | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** Given the estimate of the 3D articulation flow ˆF0, we now describe a general, closed-loop policy which takes flow as input and actuates an articulated ...
- **p. 3 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We assume that the robot has a depth camera and records point cloud observations
- **p. 3 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** However, for the purposes of this work, we apply this representation to 3D point clouds produced from depth images.
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** We first present the theoretical grounding behind the intuition of our method, and we slowly relax assumptions and approximations to create a system that articulates ...
- **p. 2 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** At this point, the policy can apply a 3D force F, with constant magnitude //F// = C to the object at that point.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The system first observes the initial configuration of the object of interest, estimates the per-point articulation flow of the point cloud (3DAF), then executes the ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Thus, the optimal policy to articulate a prismatic joint is to select any point on the surface and apply a force parallel ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 2) Articulation Execution: At each time step t, we record a new observation Ot and estimate the current flow ˆFt. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | An Idealized Policy Based On Dynamics and Kinematics The articulated objects we consider in this work are generally objects that 1) consist ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial ...
- **p. 5 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a new supervised pair ...
- **p. 4 / III. METHOD - FROM THEORY TO PRACTICE - extractive body cue:** While contact selection for suction-based grasping is a well-studied problem [3, 23, 24], we find that a simple heuristic performs acceptably; we choose the point ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** General, Policy, Articulation, Flow, Algorithm, FlowBot3D, manipulation, Require, parameters, trained, prediction, network, Initial, observation, Predict, SelectContact, Select, contact, pose, False.
- **Relevant PDF headings:** 2) A novel 3D vision neural network architecture (which (p. 1); III. METHOD - FROM THEORY TO PRACTICE (p. 2); Method (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Real-World Experiments To evaluate the performance of FlowBot3D when executed in a real robotic environment, we design a set of of realworld ... | p. 7 (IV. RESULTS), p. 2 (4) Simulated experiments to test the performance of our) |
| Semantic / temporal fusion | The best BC baseline, DAgger Oracle + F, is only able to fully articulate objects 33% of the time. | p. 7 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Robot query / planning handoff | Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow ... | p. 8 (IV. RESULTS), p. 7 (IV. RESULTS) |

## Failure and Ablation Link

- **p. 6 / IV. RESULTS - extractive body cue:** Baseline Comparisons: We compare our proposed method with several baseline methods: • UMP-DI: We implement a variant4 of UMPNet's Direction Inference network (DistNet) [39], where ...
- **p. 7 / IV. RESULTS - extractive body cue:** Second, none of the Behavior Cloning and DAgger policies, nor their flow-based variants, perform well.
- **p. 8 / IV. RESULTS - extractive body cue:** In experiments, we use an ArtFlowNet trained without a part mask in the observation space.
- **p. 8 / IV. RESULTS - extractive body cue:** As in our simulated experiments, we use a single model trained in simulation across multiple object categories without any further finetuning. # Objects 2 1 ...
- **p. 8 / IV. RESULTS - extractive body cue:** Notice that even with occlusions, such as in the intermediate mini-fridge observation, the network is able to predict reasonable 3D articulation flow vectors for downstream ...
- **p. 7 / IV. RESULTS - extractive body cue:** UMPNet Pybullet Environment: The simulation environment used in the original UMPNet evaluations [39] is a PyBullet-based environment with different physical and collision parameters.
- **p. 8 / IV. RESULTS - extractive body cue:** Each object falls into one of either the training or test classes we selected from the PartNet-Mobility.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE), objective p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE), temporal p. 3 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 5 (III. METHOD - FROM THEORY TO PRACTICE), p. 4 (III. METHOD - FROM THEORY TO PRACTICE), p. 2 (III. METHOD - FROM THEORY TO PRACTICE), p. 3 (III. METHOD - FROM THEORY TO PRACTICE).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** A General Policy using 3D Articulation Flow Algorithm 1 The FlowBot3D articulation manipulation policy Require: θ ←parameters of a trained flow prediction network (O0) ←Initial observation ˆF0 ←fθ(O0, [M0]), Predict ... (p. 4, III. METHOD - FROM THEORY TO PRACTICE).
- **Objective/update evidence:** During each step of training, we select an object in the dataset, randomize the state S of the object, and compute a new supervised pair (OS, FS), which we use ... (p. 5, III. METHOD - FROM THEORY TO PRACTICE).
- **Temporal/runtime evidence:** This process repeats in a closed loop fashion until the object has been fully-articulated, a max number of steps has been exceeded, or the episode is otherwise terminated. (p. 4, III. METHOD - FROM THEORY TO PRACTICE).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
