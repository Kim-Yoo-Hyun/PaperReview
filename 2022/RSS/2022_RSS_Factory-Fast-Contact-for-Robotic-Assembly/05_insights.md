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

- **Paper-specific interface:** Specifically, we uniquely combine SDF collisions [61], contact reduction [72], and a Gauss-Seidel solver [60], allowing us to simulate interactions of highly-detailed models substantially faster than previous efforts. (p. 4, III. CONTACT-RICH SIMULATION METHODS).
- **Paper-specific mechanism:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING); the relevant task/metric cue is Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. (p. 9, V. REINFORCEMENT LEARNING).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, assembly, contact-rich manipulation, simulation, Reinforcement Learning, sim-to-real`.
- **Reading predecessor in the generated track queue:** Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Specifically, we uniquely combine SDF collisions [61], contact reduction [72], and a Gauss-Seidel solver [60], allowing us to simulate interactions of highly-detailed models substantially faster than previous efforts. (p. 4, III. CONTACT-RICH SIMULATION METHODS); preserve the objective/update rule: The gradient ∇φ(x) provides the normal at a point x on the surface. (p. 4, III. CONTACT-RICH SIMULATION METHODS).
2. Use the paper-reported task/data/environment cue: Each environment consists of a Franka robot and the gear assembly from NIST Task Board 1. (p. 7, IV. ROBOT LEARNING TOOLS).
3. Compare against the reported or matched baseline: THE BASELINE TIMESTEP SIZE (BEFORE SUBSTEPPING) IS 1 60 s. (p. 7, IV. ROBOT LEARNING TOOLS).
4. Report the body metric with its denominator and aggregation: Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING).
5. Re-run the reported ablation or stress/failure condition: As a simplifying assumption, the joint limit of the end-effector was removed, allowing the Franka to avoid regrasping (akin to the Kinova Gen3). (p. 9, V. REINFORCEMENT LEARNING); if none is reported, design one around: A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. (p. 9, V. REINFORCEMENT LEARNING).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), match the reported outcome at p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 8 (IV. ROBOT LEARNING TOOLS), and measure the boundary at p. 9 (V. REINFORCEMENT LEARNING), p. 11 (VII. LIMITATIONS).

## Falsifiable research question

Under the paper's stated interface (Specifically, we uniquely combine SDF collisions [61], contact reduction [72], and a Gauss-Seidel solver [60], allowing us to simulate interactions of highly-detailed ...), does the paper-specific mechanism (In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.) retain the reported evaluation outcome (Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a ...) when tested against the paper's strongest explicit boundary (A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Policy chaining can be challenging, as errors in each subpolicy can accumulate into poor overall performance; as a simple example, 3 perfectlycoupled subpolicies with 90% success rates can produce a ... (p. 10, V. REINFORCEMENT LEARNING).
- **Strongest explicit boundary:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. (p. 9, V. REINFORCEMENT LEARNING).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
