# Factory: Fast Contact for Robotic Assembly

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2205.03532.
> PDF retrieval source: https://arxiv.org/pdf/2205.03532. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, assembly, contact-rich manipulation, simulation, Reinforcement Learning, sim-to-real
- Official paper: https://arxiv.org/abs/2205.03532
- Full-text retrieval: https://arxiv.org/pdf/2205.03532
- Code/Project: https://github.com/NVIDIA-Omniverse/IsaacGymEnvs
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42].를 문제로 두고, In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic assembly is one of the oldest and most challenging applications of robotics.
- **p. 1 / Abstract - extractive body cue:** In other areas of robotics, such as perception and grasping, simulation has rapidly accelerated research progress, particularly when combined with modern deep learning.
- **p. 1 / Abstract - extractive body cue:** However, accurately, efficiently, and robustly simulating the range of contact-rich interactions in assembly remains a longstanding challenge.
- **p. 1 / Abstract - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such applications.
- **p. 1 / Abstract - extractive body cue:** We achieve real-time or faster simulation of a wide range of contact-rich scenes, including simultaneous simulation of 1000 nut-and-bolt interactions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In research, methods for robotic assembly often use lessexpensive equipment, require fewer custom fixtures, achieve increased robustness to variation, and may recover from failure [35, ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Specifically, given a triangle mesh representing the boundaries of the object, we generate an SDF for the mesh at initialization time and store it as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Meanwhile, physics simulation has become a powerful tool for robotics development.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The suite includes 60 carefully-designed assets, 3 robotic assembly environments, and 7 classical robot controllers.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We aim for Factory to greatly accelerate research and development in robotic assembly, as well as serve as a powerful tool for contact-rich simulation of ...
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** In this work, we first build a module for PhysX [75] for efficient and robust contact-rich simulation.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** To generate an initial set of contacts, we use the method of [61], which generates one contact per triangle-mesh face.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The contact forces generated during policy execution are compared to literature values from the real world and show strong consistency. | RGB-D/point cloud, object state와 contact/task observation | p. 2 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| State/latent | contact, forces, generated, during, policy, execution, compared, literature, values, real, world, strong | object geometry, affordance, contact mode 또는 end-effector state | p. 2 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| Output/action | Using a state-ofthe-art GPU, we can only simulate 20 nut-and-bolt assemblies in parallel (Table V). | grasp, pose, force 또는 end-effector trajectory | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS) |
| Objective/outcome | The contact position on each face is determined by performing iterative local minimization to find the closest point on the face to the opposing shape, using projected gradient descent with adaptive stepping. | task completion, contact success, pose/force error와 generalization | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Specifically, given a triangle mesh representing the boundaries of the object, we generate an SDF for the mesh at initialization time and store it as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Meanwhile, physics simulation has become a powerful tool for robotics development.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The suite includes 60 carefully-designed assets, 3 robotic assembly environments, and 7 classical robot controllers.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We aim for Factory to greatly accelerate research and development in robotic assembly, as well as serve as a powerful tool for contact-rich simulation of ...
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** With the above approach, the Pick policy was able to achieve a 100% success rate within the randomization bounds.
- **p. 10 / V. REINFORCEMENT LEARNING - extractive body cue:** With this strategy, we achieved an end-to-end Pick, Place, and Screw success rate of 74.2%.
- **p. 10 / V. REINFORCEMENT LEARNING - extractive body cue:** Using the above configuration, a final Screw policy was trained over 4096 gradient updates and achieved an 85.6% success rate over 1024 episodes.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING) |
| Embodiment/environment | We also provide 60 carefully-designed, ISO-standard or manufacturer-based assets from the NIST Assembly Task Board 1, suitable for high-accuracy simulation; 3 robotic assembly scenes in Isaac Gym where a robot can interact ... | hardware/simulator version and reset protocol | p. 10 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING) |
| Dataset/benchmark | This controller is immediately available on the real-world Franka robot via the libfranka library [24]. • Operational-space (OSC) motion controller, which uses the task-space inertia matrix and gravity compensation to generate joint ... | role, split, size and leakage | p. 10 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING), p. 8 (IV. ROBOT LEARNING TOOLS), p. 10 (VI. DISCUSSION) |
| Metric | Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a combined policy ... | definition, denominator, direction and uncertainty | p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING) |
| Baseline/ablation | THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s. | fair input/data/compute/action matching | p. 7 (IV. ROBOT LEARNING TOOLS), p. 9 (V. REINFORCEMENT LEARNING), p. 9 (V. REINFORCEMENT LEARNING) |

## Explicit Limitations and Failure Boundary

- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** Nevertheless, training was replete with a diverse range of pathologies, including high-energy collision with the bolt shank, roll-pitch misalignment of the nut when first engaging ...
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Within simulation, we plan to make 3 improvements to our SDF collision scheme: 1) the ability to robustly handle collisions of thin-shell meshes (e.g., thin-walled ...
- **p. 10 / VI. DISCUSSION - extractive body cue:** Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within robotics, ...
- **p. 11 / VIII. CONCLUSION - extractive body cue:** MM initially developed SDF collisions for FleX.
- **p. 10 / V. REINFORCEMENT LEARNING - extractive body cue:** For a small number of subpolicies, this strategy may be effective; however, the approach does not scale to long sequences, as Policy N must be ...
- **p. 8 / V. REINFORCEMENT LEARNING - extractive body cue:** Moreover, it is a common experience of simulation developers that model-free RL agents reveal and exploit any inaccuracies or instabilities in the simulator to maximize ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42].를 문제로 두고, In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING).
- **Explicit failure boundary:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. (p. 9, V. REINFORCEMENT LEARNING).
