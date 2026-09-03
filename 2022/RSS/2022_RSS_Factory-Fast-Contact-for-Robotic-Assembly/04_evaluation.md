# Evaluation - Factory: Fast Contact for Robotic Assembly

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.03532; PDF retrieval source: https://arxiv.org/pdf/2205.03532. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 11 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING)): With the above approach, the Pick policy was able to achieve a 100% success rate within the randomization bounds.

## Evaluation Body Digest

- **p. 10 / VI. DISCUSSION - extractive body cue:** We also provide 60 carefully-designed, ISO-standard or manufacturer-based assets from the NIST Assembly Task Board 1, suitable for high-accuracy simulation; 3 robotic assembly scenes in ...
- **p. 8 / V. REINFORCEMENT LEARNING - extractive body cue:** The robotics community has demonstrated that RL can effectively solve simulated or real-world assembly tasks.
- **p. 8 / IV. ROBOT LEARNING TOOLS - extractive body cue:** This controller is immediately available on the real-world Franka robot via the libfranka library [24]. • Operational-space (OSC) motion controller, which uses the task-space inertia ...
- **p. 10 / VI. DISCUSSION - extractive body cue:** Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within robotics, ...
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** Each environment consists of a Franka robot and the gear assembly from NIST Task Board 1.
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Within our assets, environments, and controllers, we plan to add assets for additional industrial and home subassemblies (e.g., USB-C, power plugs, key-in-lock), scenes for additional ...
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** On the other hand, classical PD- or PID-style robot controllers have been used to solve contact-rich tasks in robotic assembly for several decades [69, 101].
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Furthermore, given that camera observations will be occluded during contact, we anticipate that integrating tactile sensing into our real-world system will be exceptionally critical for ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. REINFORCEMENT LEARNING | EMPIRICAL / REAL-ROBOT OR HARDWARE | With the above approach, the Pick policy was able to achieve a 100% success rate within the randomization bounds. | p. 9 (V. REINFORCEMENT LEARNING) |
| V. REINFORCEMENT LEARNING | EMPIRICAL / REAL-ROBOT OR HARDWARE | With this strategy, we achieved an end-to-end Pick, Place, and Screw success rate of 74.2%. | p. 10 (V. REINFORCEMENT LEARNING) |
| V. REINFORCEMENT LEARNING | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using the above configuration, a final Screw policy was trained over 4096 gradient updates and achieved an 85.6% success rate over 1024 episodes. | p. 10 (V. REINFORCEMENT LEARNING) |
| VI. DISCUSSION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Pose WAS QUICKEST; Pose, velocity EXHIBITED HIGHEST SUCCESS RATE; AND Pose, velocity, force, action ACHIEVED LOWEST MEAN REWARD, BUT DID NOT CONSISTENTLY COMPLETE THE ... | p. 11 (VI. DISCUSSION) |
| VI. DISCUSSION | EMPIRICAL / REAL-ROBOT OR HARDWARE | Observations Success Rate Env Steps to Success Reward Joint Torque (Nm) Pose 0.7708 2318 -0.1019 1.7319 Pose, velocity 0.7760 3015 -0.0941 1.7330 Pose, velocity, ... | p. 11 (VI. DISCUSSION) |

## Dataset / Benchmark Role

- **p. 10 / VI. DISCUSSION - extractive body cue:** We also provide 60 carefully-designed, ISO-standard or manufacturer-based assets from the NIST Assembly Task Board 1, suitable for high-accuracy simulation; 3 robotic assembly scenes in ...
- **p. 8 / V. REINFORCEMENT LEARNING - extractive body cue:** The robotics community has demonstrated that RL can effectively solve simulated or real-world assembly tasks.
- **p. 8 / IV. ROBOT LEARNING TOOLS - extractive body cue:** This controller is immediately available on the real-world Franka robot via the libfranka library [24]. • Operational-space (OSC) motion controller, which uses the task-space inertia ...
- **p. 10 / VI. DISCUSSION - extractive body cue:** Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within robotics, ...
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** Each environment consists of a Franka robot and the gear assembly from NIST Task Board 1.
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Within our assets, environments, and controllers, we plan to add assets for additional industrial and home subassemblies (e.g., USB-C, power plugs, key-in-lock), scenes for additional ...
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** On the other hand, classical PD- or PID-style robot controllers have been used to solve contact-rich tasks in robotic assembly for several decades [69, 101].
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Furthermore, given that camera observations will be occluded during contact, we anticipate that integrating tactile sensing into our real-world system will be exceptionally critical for ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Rendering of Franka robots interacting with nut-and-bolt assemblies in Isaac Gym using methods from Factory. The simulation contains 128 parallel environments and is ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Cross-sectional view of an aligned M16 nut-and-bolt assembly. Nuts and bolts have finite clearances between their threads, thus experiencing 6- DOF kinematics with ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Rendering of the M16 nut-and-bolt assemblies scene, consisting of 1024 parallel nut-and-bolt interactions executing in real-time. contact profiling, a 2e-6 m clearance is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Rendering of the Franka robot + M16 nut-and-bolt assemblies scene, consisting of 128 parallel Franka robots retrieving nuts from a vibratory feeder mechanism ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Rendering of a simulated NIST Task Board 1, demonstrating the provided assets. We provide simulation and RL training environments for all rigid components ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Visualization of FrankaInsertionEnv. Each environment consists of a Franka robot and an insertion assembly from NIST Task Board 1. Left: The default initial ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Visualization of FrankaGearsEnv. Each environment consists of a Franka robot and the gear assembly from NIST Task Board 1. Left: The default initial ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8. Rendering of achieved goal states of our trained subpolicies for FrankaNutBoltEnv. Left: Pick. Middle: Place. Right: Screw. • Joint-space inverse dynamics (ID) controller, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We also provide 60 carefully-designed, ISO-standard or manufacturer-based assets from the NIST Assembly Task Board 1, suitable for high-accuracy simulation; 3 robotic assembly scenes ... | embodiment, simulator version and control stack | p. 10 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING) |
| Task/environment | The robotics community has demonstrated that RL can effectively solve simulated or real-world assembly tasks. | reset, timeout, object/scene variation | p. 8 (V. REINFORCEMENT LEARNING), p. 8 (IV. ROBOT LEARNING TOOLS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with ... | definition/direction/unit from same section | p. 10 (V. REINFORCEMENT LEARNING) |
| Observations Success Rate Env Steps to Success Reward Joint Torque (Nm) Pose 0.7708 2318 -0.1019 1.7319 Pose, velocity 0.7760 3015 -0.0941 1.7330 Pose, velocity, ... | definition/direction/unit from same section | p. 11 (VI. DISCUSSION) |
| We now discuss our randomization, observations, rewards, success criterion, and success rate for each subpolicy. | definition/direction/unit from same section | p. 8 (V. REINFORCEMENT LEARNING) |
| Pose WAS QUICKEST; Pose, velocity EXHIBITED HIGHEST SUCCESS RATE; AND Pose, velocity, force, action ACHIEVED LOWEST MEAN REWARD, BUT DID NOT CONSISTENTLY COMPLETE THE ... | definition/direction/unit from same section | p. 11 (VI. DISCUSSION) |
| Success was defined as when the average keypoint distance was < 0.8 mm With the above approach, the Place policy was able to achieve ... | definition/direction/unit from same section | p. 9 (V. REINFORCEMENT LEARNING) |
| Then, 4 observation spaces were evaluated, and the space with the highest success rate was selected (Table IV). | definition/direction/unit from same section | p. 9 (V. REINFORCEMENT LEARNING) |
| With this strategy, we achieved an end-to-end Pick, Place, and Screw success rate of 74.2%. | definition/direction/unit from same section | p. 10 (V. REINFORCEMENT LEARNING) |
| Moreover, it is a common experience of simulation developers that model-free RL agents reveal and exploit any inaccuracies or instabilities in the simulator to ... | definition/direction/unit from same section | p. 8 (V. REINFORCEMENT LEARNING) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s. | comparison identity and matched condition | p. 7 (IV. ROBOT LEARNING TOOLS) |
| The procedure continued with 2 action spaces (Table XI) and 3 baseline rewards (Table XII). | comparison identity and matched condition | p. 9 (V. REINFORCEMENT LEARNING) |
| To overcome the preceding issues, a systematic exploration of controllers/gains, observation/action spaces, and baseline rewards was executed. | comparison identity and matched condition | p. 9 (V. REINFORCEMENT LEARNING) |
| The highest performing agents consistently used an OSC motion controller with low proportional gains, an observation space consisting of pose and velocity of the ... | comparison identity and matched condition | p. 10 (V. REINFORCEMENT LEARNING) |
| Furthermore, the contact force norms at the fingertips were compared to analogous real-world forces from the Daily Interactive Manipulation dataset [34], in which human ... | comparison identity and matched condition | p. 10 (V. REINFORCEMENT LEARNING) |
| However, we encourage the broader RL community to test and develop state-of-the-art RL algorithms around these complex tasks. | comparison identity and matched condition | p. 11 (VII. LIMITATIONS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| As a simplifying assumption, the joint limit of the end-effector was removed, allowing the Franka to avoid regrasping (akin to the Kinova Gen3). | component/input/data sensitivity | p. 9 (V. REINFORCEMENT LEARNING) |
| Fig. 5. Rendering of a simulated NIST Task Board 1, demonstrating the provided assets. We provide simulation and RL training environments for all rigid ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig. | With the above approach, the Pick policy was able to achieve a 100% success rate within the randomization bounds. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 11 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING) |
| Primary metric/result | With this strategy, we achieved an end-to-end Pick, Place, and Screw success rate of 74.2%. | numeric claim only at cited anchor | p. 10 (V. REINFORCEMENT LEARNING) |

- Numeric sentences retained from the body:
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** Contact Stats (Before) Contact Handling Contact Stats (After) Contact Solution Scene Contacts Per Pair (avg) Per Pair (max) Time Per Pair (avg) Patches Time Peg-in-hole ...
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** Timestepping Simulation Stats Scene Substeps Pos Iterations Vel Iterations Time Real-time Peg-in-hole 1 4 1 3 ms 5689x Nut-and-bolt 1 20 1 14 ms 1219x ...
- **p. 7 / IV. ROBOT LEARNING TOOLS - extractive body cue:** THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s.
- **p. 8 / V. REINFORCEMENT LEARNING - extractive body cue:** Typically, a batch of 3-4 policies were trained simultaneously on a single NVIDIA RTX 3090 GPU, with each policy using 128 parallel simulation environments.
- **p. 8 / V. REINFORCEMENT LEARNING - extractive body cue:** Each batch required a total of 1-1.5 hours for 1024 policy updates.
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** First, policies for 3 task-space controllers were evaluated over a wide range of gains, and the controllergain configuration with the highest success rate was chosen ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. | p. 9 (V. REINFORCEMENT LEARNING) |
| body limitation/failure cue | Nevertheless, training was replete with a diverse range of pathologies, including high-energy collision with the bolt shank, roll-pitch misalignment of the nut when first ... | p. 9 (V. REINFORCEMENT LEARNING) |
| body limitation/failure cue | Within simulation, we plan to make 3 improvements to our SDF collision scheme: 1) the ability to robustly handle collisions of thin-shell meshes (e.g., ... | p. 11 (VII. LIMITATIONS) |
| body limitation/failure cue | Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within ... | p. 10 (VI. DISCUSSION) |
| body limitation/failure cue | MM initially developed SDF collisions for FleX. | p. 11 (VIII. CONCLUSION) |
| body limitation/failure cue | For a small number of subpolicies, this strategy may be effective; however, the approach does not scale to long sequences, as Policy N must ... | p. 10 (V. REINFORCEMENT LEARNING) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The PPO implementation from [63] was used with a shared set of hyperparameters (Table IX). | p. 8 (V. REINFORCEMENT LEARNING) |
| EACH CELL IS COMPUTED FROM THE AVERAGE OF 3 SEEDS. | p. 11 (VI. DISCUSSION) |
| However, these efforts are often limited to off-policy algorithms, require extensive training time or human demonstrations/corrections, and/or only address simple tasks. | p. 8 (V. REINFORCEMENT LEARNING) |
| We generate the SDF for an object via sampling and compute gradients via finite-differencing. | p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| For a Jacobi solver with ∆t = 1 60s, we require 8 substeps and 64 iterations for stable simulation. | p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| S13), allowing us to simulate 1024 assemblies in realtime on an NVIDIA A5000 GPU. | p. 5 (III. CONTACT-RICH SIMULATION METHODS) |
| The preceding contact reduction process is performed exclusively in GPU shared memory. | p. 5 (III. CONTACT-RICH SIMULATION METHODS) |
| Timestepping Simulation Stats Scene Substeps Pos Iterations Vel Iterations Time Real-time Peg-in-hole 1 4 1 3 ms 5689x Nut-and-bolt 1 20 1 14 ms ... | p. 7 (IV. ROBOT LEARNING TOOLS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** Nevertheless, training was replete with a diverse range of pathologies, including high-energy collision with the bolt shank, roll-pitch misalignment of the nut when first engaging ...
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Within simulation, we plan to make 3 improvements to our SDF collision scheme: 1) the ability to robustly handle collisions of thin-shell meshes (e.g., thin-walled ...
- **p. 10 / VI. DISCUSSION - extractive body cue:** Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within robotics, ...
- **p. 11 / VIII. CONCLUSION - extractive body cue:** MM initially developed SDF collisions for FleX.
- **p. 10 / V. REINFORCEMENT LEARNING - extractive body cue:** For a small number of subpolicies, this strategy may be effective; however, the approach does not scale to long sequences, as Policy N must be ...

- **Evidence anchors reviewed:** datasets p. 10 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING), p. 8 (IV. ROBOT LEARNING TOOLS), p. 10 (VI. DISCUSSION), p. 7 (IV. ROBOT LEARNING TOOLS), p. 11 (VII. LIMITATIONS), metrics p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 9 (V. REINFORCEMENT LEARNING), p. 9 (V. REINFORCEMENT LEARNING), baselines p. 7 (IV. ROBOT LEARNING TOOLS), p. 9 (V. REINFORCEMENT LEARNING), p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VII. LIMITATIONS), results p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 11 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING).
- **Metric evidence:** Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING).
- **Baseline/ablation evidence:** THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s. (p. 7, IV. ROBOT LEARNING TOOLS).
- **Failure/negative evidence:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. (p. 9, V. REINFORCEMENT LEARNING).
