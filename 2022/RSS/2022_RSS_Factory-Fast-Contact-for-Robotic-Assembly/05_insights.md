# Insights — Factory: Fast Contact for Robotic Assembly

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.03532; PDF retrieval source: https://arxiv.org/pdf/2205.03532. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Specifically, given a triangle mesh representing the boundaries of the object, we generate an SDF for the mesh at initialization time and store it as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Meanwhile, physics simulation has become a powerful tool for robotics development.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The suite includes 60 carefully-designed assets, 3 robotic assembly environments, and 7 classical robot controllers.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We aim for Factory to greatly accelerate research and development in robotic assembly, as well as serve as a powerful tool for contact-rich simulation of ...
- **p. 5 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Solving contact constraints is no longer a performance bottleneck, and we can achieve a level of parallelization suitable for training on-policy RL algorithms.
- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** In this work, we first build a module for PhysX [75] for efficient and robust contact-rich simulation.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (III. CONTACT-RICH SIMULATION METHODS)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In research, methods for robotic assembly often use lessexpensive equipment, require fewer custom fixtures, achieve increased robustness to variation, and may recover from failure [35, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** As an example, we simulate 1000 simultaneous nut-and-bolt assemblies in real-time on a single GPU, whereas the prior state-ofthe-art was a single nut-and-bolt assembly at ...
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.
- **p. 9 / V. REINFORCEMENT LEARNING - extractive body cue:** Nevertheless, training was replete with a diverse range of pathologies, including high-energy collision with the bolt shank, roll-pitch misalignment of the nut when first engaging ...
- **p. 11 / VII. LIMITATIONS - extractive body cue:** Within simulation, we plan to make 3 improvements to our SDF collision scheme: 1) the ability to robustly handle collisions of thin-shell meshes (e.g., thin-walled ...
- **p. 10 / VI. DISCUSSION - extractive body cue:** Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our methods for entirely different tasks within robotics, ...
- **Boundary to test:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig. | p. 1 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| Reported outcome | With the above approach, the Pick policy was able to achieve a 100% success rate within the randomization bounds. | p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING) |
| Failure/limitation | A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. | p. 9 (V. REINFORCEMENT LEARNING), p. 9 (V. REINFORCEMENT LEARNING) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 The contact forces generated during policy execution are compared to literature values from the real world and show strong consistency.를 Using a state-ofthe-art GPU, we can only simulate 20 nut-and-bolt assemblies in parallel (Table V).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, assembly, contact-rich manipulation, simulation, Reinforcement Learning, sim-to-real`.
- **Reading predecessor in the generated track queue:** Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We also provide 60 carefully-designed, ISO-standard or manufacturer-based assets from the NIST Assembly Task Board 1, suitable for high-accuracy simulation; 3 robotic assembly scenes in Isaac Gym where a robot can interact ....
3. Compare against the body-reported baseline or a matched simpler baseline: THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s..
4. Report the body metric and its denominator/aggregation: Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a combined policy ....
5. Re-run the body-reported ablation/failure condition: As a simplifying assumption, the joint limit of the end-effector was removed, allowing the Franka to avoid regrasping (akin to the Kinova Gen3)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS); the primary result is directionally consistent at p. 9 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING), p. 10 (V. REINFORCEMENT LEARNING); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, Factory, physics mechanism이 THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s. 대비 Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a ...을 개선하고, A common initial failure case during training was collision between the gripper and the bolt, dislodging ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
