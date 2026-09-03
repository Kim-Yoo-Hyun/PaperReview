# Evaluation - Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p135.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p135.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS)): While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance.

## Evaluation Body Digest

- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** By pursuing these future directions, we can unlock the full potential of our proposed framework, enabling robots with compliant membranes to perform even more versatile ...
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** For object-object interactions, we attach the object to the scene similar to the setup described in section V-A and have the robot perform object-object interactions.
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Tactile Elasticity Characterization To characterize the compliance of the tactile sensors, the robot collects data by attempting to manipulate an object fixed to the environment, ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Tactile Elasticity Identification: (Left) During the data collection, the robot grasps an object rigidly attached to the environment while moving the end effector.
- **p. 9 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Optimization Approach Bubble Pivoting Gelslim Pivoting Computation Time [s] Name #iters #samples Pose Error [mm] Wrench Error [N] Pose Error [mm] Wrench Error [N] Mean ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** The samples lie within a cone that defines the friction coefficient to be µ = 0.33 grasped object pose is constant w.r.t. to the robot ...
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We use the first object (hbox) for benchmarking primitives 1-4 while using the remaining more diverse and complex objects for extrinsic pivoting since it is ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** V. EXPERIMENTS AND RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. | p. 10 (V. EXPERIMENTS AND RESULTS) |
| V. EXPERIMENTS AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our experiments show that the closedloop controllers achieve superior performance tracking the desired trajectories than the other tested control approaches. | p. 7 (V. EXPERIMENTS AND RESULTS) |
| V. EXPERIMENTS AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error. | p. 8 (V. EXPERIMENTS AND RESULTS) |
| V. EXPERIMENTS AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Extrinsic Trajectory Optimization Benchmark To benchmark our method, we compare it with two trajectory optimization algorithms: 1) Model-Predictive Path Integral (MPPI) [40] and 2) ... | p. 8 (V. EXPERIMENTS AND RESULTS) |
| V. EXPERIMENTS AND RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves good tracking both for poses and wrenches. | p. 9 (V. EXPERIMENTS AND RESULTS) |

## Dataset / Benchmark Role

- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** By pursuing these future directions, we can unlock the full potential of our proposed framework, enabling robots with compliant membranes to perform even more versatile ...
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** For object-object interactions, we attach the object to the scene similar to the setup described in section V-A and have the robot perform object-object interactions.
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Tactile Elasticity Characterization To characterize the compliance of the tactile sensors, the robot collects data by attempting to manipulate an object fixed to the environment, ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Tactile Elasticity Identification: (Left) During the data collection, the robot grasps an object rigidly attached to the environment while moving the end effector.
- **p. 9 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Optimization Approach Bubble Pivoting Gelslim Pivoting Computation Time [s] Name #iters #samples Pose Error [mm] Wrench Error [N] Pose Error [mm] Wrench Error [N] Mean ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** The samples lie within a cone that defines the friction coefficient to be µ = 0.33 grasped object pose is constant w.r.t. to the robot ...
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We use the first object (hbox) for benchmarking primitives 1-4 while using the remaining more diverse and complex objects for extrinsic pivoting since it is ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Overview of Approach: First Panel: our general setup where the robot is grasping an object with tactile sensors and is tasked with manipulating ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Notation using a grasped tool. The main difference between this ap- proach and ours is that we consider different primitive motions beyond pivoting, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Tactile State Estimation: We show the state estimation for the grasped object for contact-free (left) and in-contact (right) configurations. We overlay the estimated ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Trajectory Optimization Overview: Given a desired trajectory of the extrinsic object {xeo,k}K k=1 as well as the contact modes {ck}K k=1, our method ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. In-Contact Manipulation Skills: We show our framework on a diverse set of in-contact skills. The first 3 are for manipulating a grasped object ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Tactile Elasticity Identification: (Left) During the data collection, the robot grasps an object rigidly attached to the environment while moving the end effector. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Fiction Cone Estimation: (Left) During the friction coefficient identification, the robot moves while maintaining the object in contact with the contact surface while ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8. Manipulation Shapes Shapes: We test our method on a diverse set of planar polygonal shapes. Note that our approach can handle convex as ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This expansion would significantly broaden the applicability of our method to real-world manipulation tasks involving intricate object shapes and diverse robot motions. | embodiment, simulator version and control stack | p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS) |
| Task/environment | By pursuing these future directions, we can unlock the full potential of our proposed framework, enabling robots with compliant membranes to perform even more ... | reset, timeout, object/scene variation | p. 10 (V. EXPERIMENTS AND RESULTS), p. 6 (V. EXPERIMENTS AND RESULTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 3 (IV. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 3 (IV. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS AND RESULTS) |
| While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. | definition/direction/unit from same section | p. 10 (V. EXPERIMENTS AND RESULTS) |
| These results demonstrate the efficacy of our approach and the successful completion of the manipulation skills. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS AND RESULTS) |
| In order to evaluate how well a skill is performed, we measure the error between the desired object pose and the transmitted wrenches to ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS AND RESULTS) |
| We evaluate the execution of the optimized trajectories using Soft Bubbles and measure pose and wrench errors. | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS AND RESULTS) |
| However, it is important to highlight that the sample-based methods exhibited higher errors compared to the bubbles. | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS AND RESULTS) |
| This would significantly enhance the accuracy and adaptability of our approach, enabling robots to handle objects with diverse and dynamic frictional characteristics. | definition/direction/unit from same section | p. 10 (V. EXPERIMENTS AND RESULTS) |
| 7 (left) illustrates the setup used. | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS AND RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: one with 100 QP queries and another with ... | comparison identity and matched condition | p. 9 (V. EXPERIMENTS AND RESULTS) |
| However, it is important to highlight that the sample-based methods exhibited higher errors compared to the bubbles. | comparison identity and matched condition | p. 9 (V. EXPERIMENTS AND RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We report the mean absolute error for each of the wrench and pose components. | component/input/data sensitivity | p. 8 (V. EXPERIMENTS AND RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The key contribution of our method is to formulate the contact trajectory optimization precisely to address these requirements while also being amenable to gradient-based ... | While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS) |
| Primary metric/result | Our experiments show that the closedloop controllers achieve superior performance tracking the desired trajectories than the other tested control approaches. | numeric claim only at cited anchor | p. 7 (V. EXPERIMENTS AND RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We note that opting for a dense matrix enables modeling of the crossinteraction between the 3 degrees of freedom.
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** For each primitive 1-4, we perform 3 trajectories of 20 steps.
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** To evaluate the extrinsic pivoting performance, for each of the objects we perform 3 pivoting trajectories of 40 steps each.
- **p. 9 / V. EXPERIMENTS AND RESULTS - extractive body cue:** For each method, we perform 5 offline trajectory optimizations with a horizon of 40 steps.
- **p. 6 / IV. METHODOLOGY - extractive body cue:** Lsmooth = 1 K -1 K-1 X k=1 ∥xgo,k+1 -xgo,k∥2 • Contact Force Loss (Lcontact force): The contact force loss incentivizes the contact forces to ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. | p. 10 (V. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | DISCUSSION, LIMITATIONS, AND FUTURE WORK In this paper, we proposed an approach to extrinsic object manipulation leveraging tactile sensor compliance, tactile sensor measurements, and ... | p. 10 (V. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | In this instance, the contacts between the object and the environment must be sticking, i.e. fc,i ∈int Fc,i. • Grasped Object Pivoting: The goal ... | p. 6 (V. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | We display the sticking contact points in red and the slipping contacts in green. | p. 7 (V. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | The desired contact mode is sticking contact between the grasped and extrinsic objects contacts, while the contact between the extrinsic object and the environment ... | p. 8 (V. EXPERIMENTS AND RESULTS) |
| body limitation/failure cue | Additionally, we observed instances of slippage between the sensor and the grasped object, which violates the assumption of sticking contact between them. | p. 9 (V. EXPERIMENTS AND RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each primitive 1-4, we perform 3 trajectories of 20 steps. | p. 8 (V. EXPERIMENTS AND RESULTS) |
| For each method, we perform 5 offline trajectory optimizations with a horizon of 40 steps. | p. 9 (V. EXPERIMENTS AND RESULTS) |
| Firstly, our current implementation assumes the provided object configurations are achievable and tracks them as closely as possible. | p. 10 (V. EXPERIMENTS AND RESULTS) |
| The SEED model relates a measured grasped object displacement xgocf ee = x y θ⊤obtained using the method described in Section IV-A, to a ... | p. 4 (IV. METHODOLOGY) |
| Here, we follow the SEED approach [22], where they showed that the compliance of the Soft Bubbles sensors can be exploited to turn a ... | p. 4 (IV. METHODOLOGY) |
| 2) Given the grasped object state xgo and the robot state xee use the tactile compliance model to compute the external wrench applied to ... | p. 5 (IV. METHODOLOGY) |
| 4) Given the object and robot poses, the external wrench, and the contact forces compute the loss function L and backpropagate the gradients through ... | p. 5 (IV. METHODOLOGY) |
| Lpenetration = 1 K K X k=1 ∥-1 10 log(-ϕk)∥2 Our implementation is based on cvxpylayers [39] to differentiate over the QP and pytorch ... | p. 6 (IV. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques.
- **p. 10 / V. EXPERIMENTS AND RESULTS - extractive body cue:** DISCUSSION, LIMITATIONS, AND FUTURE WORK In this paper, we proposed an approach to extrinsic object manipulation leveraging tactile sensor compliance, tactile sensor measurements, and contact ...
- **p. 6 / V. EXPERIMENTS AND RESULTS - extractive body cue:** In this instance, the contacts between the object and the environment must be sticking, i.e. fc,i ∈int Fc,i. • Grasped Object Pivoting: The goal is ...
- **p. 7 / V. EXPERIMENTS AND RESULTS - extractive body cue:** We display the sticking contact points in red and the slipping contacts in green.
- **p. 8 / V. EXPERIMENTS AND RESULTS - extractive body cue:** The desired contact mode is sticking contact between the grasped and extrinsic objects contacts, while the contact between the extrinsic object and the environment must ...
- **p. 9 / V. EXPERIMENTS AND RESULTS - extractive body cue:** Additionally, we observed instances of slippage between the sensor and the grasped object, which violates the assumption of sticking contact between them.

- **Evidence anchors reviewed:** datasets p. 10 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS), p. 6 (V. EXPERIMENTS AND RESULTS), p. 6 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), metrics p. 8 (V. EXPERIMENTS AND RESULTS), p. 10 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), baselines p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), results p. 10 (V. EXPERIMENTS AND RESULTS), p. 7 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 8 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS), p. 9 (V. EXPERIMENTS AND RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** While the current model yields satisfactory results, exploring higher-dimensional models with improved accuracy could further enhance performance. (p. 10, V. EXPERIMENTS AND RESULTS).
- **Metric evidence:** We observe that we achieve errors below 1N for force and in the order of a millimeter accuracy for the pose tracking error. (p. 8, V. EXPERIMENTS AND RESULTS).
- **Baseline/ablation evidence:** To ensure a fair comparison with the baseline methods, we evaluate two different versions of each: one with 100 QP queries and another with 1000 queries. (p. 9, V. EXPERIMENTS AND RESULTS).
- **Failure/negative evidence:** Furthermore, our approach does not reason about the physical limitations of the bubbles in terms of achievable forces and torques. (p. 10, V. EXPERIMENTS AND RESULTS).
