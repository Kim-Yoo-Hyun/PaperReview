# Method - Factory: Fast Contact for Robotic Assembly

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.03532; PDF retrieval source: https://arxiv.org/pdf/2205.03532. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 6 (III. CONTACT-RICH SIMULATION METHODS)): Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.

## Method Body Digest

- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** In this work, we first build a module for PhysX [75] for efficient and robust contact-rich simulation.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** To generate an initial set of contacts, we use the method of [61], which generates one contact per triangle-mesh face.
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Implementation of Contact Reduction To implement contact reduction, we use the concept of contact patches, which are sets of contacts that are proximal and share ...
- **p. 6 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Although we defer to the tables for complete performance assessments, key observations include the following: • Contact reduction can reduce contact counts by over 2 ...
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** The contact position on each face is determined by performing iterative local minimization to find the closest point on the face to the opposing shape, ...
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** The gradient ∇φ(x) provides the normal at a point x on the surface.
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Generating and reducing contacts takes 11 ms, and solving contact constraints takes an additional 3 ms.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Specifically, given a triangle mesh representing the boundaries of the object, we generate an SDF for the mesh at initialization time and store it as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Meanwhile, physics simulation has become a powerful tool for robotics development.

## Source Evidence Cues

- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** In this work, we first build a module for PhysX [75] for efficient and robust contact-rich simulation.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** To generate an initial set of contacts, we use the method of [61], which generates one contact per triangle-mesh face.
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Implementation of Contact Reduction To implement contact reduction, we use the concept of contact patches, which are sets of contacts that are proximal and share ...
- **p. 6 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Although we defer to the tables for complete performance assessments, key observations include the following: • Contact reduction can reduce contact counts by over 2 ...
- **Detected method headings:** III. CONTACT-RICH SIMULATION METHODS (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL ... | p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | In this work, we first build a module for PhysX [75] for efficient and robust contact-rich simulation. | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | To generate an initial set of contacts, we use the method of [61], which generates one contact per triangle-mesh face. | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** The contact position on each face is determined by performing iterative local minimization to find the closest point on the face to the opposing shape, ...
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** The gradient ∇φ(x) provides the normal at a point x on the surface.
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Generating and reducing contacts takes 11 ms, and solving contact constraints takes an additional 3 ms.
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contact, forces, generated, during, policy, execution, compared, literature, values, real, world, strong, consistency, state-ofthe-art | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | contact, forces, generated, during, policy, execution, compared, literature, values, real | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | present, Factory, physics, simulation, methods, robot, learning, tools, interactions, Fig | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | contact, position, face, determined, performing, iterative, local, minimization, find, closest | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** The contact forces generated during policy execution are compared to literature values from the real world and show strong consistency.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Using a state-ofthe-art GPU, we can only simulate 20 nut-and-bolt assemblies in parallel (Table V).
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Specifically, we uniquely combine SDF collisions [61], contact reduction [72], and a Gauss-Seidel solver [60], allowing us to simulate interactions of highly-detailed models substantially faster ...
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** The input is two potentially contacting shapes (a, b).
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Applying the above procedure to the M4 nut-and-bolt interactions, we reduce the number of contacts from 16k to 300 (Fig.
- **p. 6 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Although we defer to the tables for complete performance assessments, key observations include the following: • Contact reduction can reduce contact counts by over 2 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Thus, memory bandwidth requirements for 16k contacts are approximately 1.28 GB per frame and 76.8 GB per second. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | The preceding contact reduction process is performed exclusively in GPU shared memory. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | Thus, memory bandwidth requirements for 16k contacts are approximately 1.28 GB per frame and 76.8 GB per second. | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Timestepping Simulation Stats Scene Substeps Pos Iterations Vel Iterations Time Real-time Peg-in-hole 1 4 1 3 ms 5689x Nut-and-bolt 1 20 1 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.
- **p. 8 / V. REINFORCEMENT LEARNING - extractive body cue:** However, these efforts are often limited to off-policy algorithms, require extensive training time or human demonstrations/corrections, and/or only address simple tasks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Solving, contact, constraints, longer, performance, bottleneck, achieve, level, parallelization, suitable, training, on-policy, algorithms, first, build, module, PhysX, efficient, robust, contact-rich.
- **Relevant PDF headings:** III. CONTACT-RICH SIMULATION METHODS (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We also provide 60 carefully-designed, ISO-standard or manufacturer-based assets from the NIST Assembly Task Board 1, suitable for high-accuracy simulation; 3 robotic ... | p. 10 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING) |
| Grasp / trajectory generation | THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s. | p. 7 (IV. ROBOT LEARNING TOOLS), p. 9 (V. REINFORCEMENT LEARNING) |
| Contact execution / correction | With the above approach, the Pick policy was able to achieve a 100% success rate within the randomization bounds. | p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING) |

## Failure and Ablation Link

- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** As a simplifying assumption, the joint limit of the end-effector was removed, allowing the Franka to avoid regrasping (akin to the Kinova Gen3).
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Rendering of a simulated NIST Task Board 1, demonstrating the provided assets. We provide simulation and RL training environments for all rigid components ...
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** Nevertheless, training was replete with a diverse range of pathologies, including high-energy collision with the bolt shank, roll-pitch misalignment of the nut when first engaging ...
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Within simulation, we plan to make 3 improvements to our SDF collision scheme: 1) the ability to robustly handle collisions of thin-shell meshes (e.g., thin-walled ...
- **p. 10 / VI. DISCUSSION - extractive body cue:** Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within robotics, ...
- **p. 11 / VIII. CONCLUSION - extractive body cue:** MM initially developed SDF collisions for FleX.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 6 (III. CONTACT-RICH SIMULATION METHODS), objective p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), temporal p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 7 (IV. ROBOT LEARNING TOOLS), p. 7 (IV. ROBOT LEARNING TOOLS), p. 4 (III. CONTACT-RICH SIMULATION METHODS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
