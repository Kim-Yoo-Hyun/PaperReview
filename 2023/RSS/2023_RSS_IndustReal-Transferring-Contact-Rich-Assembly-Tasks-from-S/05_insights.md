# Insights — IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.17110; PDF retrieval source: https://arxiv.org/pdf/2305.17110. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** IndustRealKit allows the research community to easily replicate our experimental hardware and benchmark their performance. • Software: We present IndustRealLib, a lightweight Python library that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We present IndustReal, a set of algorithms, systems, and tools for solving contact-rich assembly tasks in simulation and transferring behaviors to reality (Figure 1).
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** In addition, for the Insert policies, we introduced observation noise.
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and ...
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Joint Evaluation As described in Sections IV-E-IV-G, we proposed three algorithms for improving learning of contact-rich Insert policies: Simulation-Aware Policy Update to adapt to simulator ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 3 (IV. POLICY LEARNING IN SIMULATION)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Robotic assembly is a longstanding challenge [70, 26].
- **p. 2 / I. INTRODUCTION - extractive body cue:** To our knowledge, this is the first system for sim-to-real of all phases of the assembly problem: from detection, to grasping, to part alignment, to ...
- **p. 2 / III. PROBLEM DESCRIPTION - extractive body cue:** Problem Setup Our problem setup is as follows: a Franka robot is mounted to a work surface.
- **p. 3 / III. PROBLEM DESCRIPTION - extractive body cue:** 2: Problem setup and decomposition.
- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their ...
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this ...
- **Boundary to test:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their corresponding sockets.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as a list of all purchased parts. | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value at test time. Boxes indicate median and IQR. ... | p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| Failure/limitation | Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their corresponding sockets. | p. 9 (VIII. LIMITATIONS & FUTURE WORK), p. 8 (VI. REAL-WORLD EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** In summary, we developed the IndustRealLib library, which accepts trained policy checkpoints from Isaac Gym as input, and outputs targets for a Franka robot controlled via a taskspace impedance (TSI) ... (p. 6, V. POLICY DEPLOYMENT IN REAL WORLD).
- **Paper-specific mechanism:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a simulator: a simulation-aware policy update ... (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 9/10 7/10 7/10 Round peg 16 ... (p. 9, VI. REAL-WORLD EXPERIMENTS); the relevant task/metric cue is Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). (p. 8, VI. REAL-WORLD EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this issue. (p. 8, VI. REAL-WORLD EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, assembly, contact-rich manipulation, Reinforcement Learning, sim-to-real, industrial robotics`.
- **Reading predecessor in the generated track queue:** Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Binding Touch to Everything: Learning Unified Multimodal Tactile Representations (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their corresponding sockets.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: In summary, we developed the IndustRealLib library, which accepts trained policy checkpoints from Isaac Gym as input, and outputs targets for a Franka robot controlled via a taskspace impedance (TSI) ... (p. 6, V. POLICY DEPLOYMENT IN REAL WORLD); preserve the objective/update rule: The objective was to learn a policy π : O →P(A) that maximized the expected sum of discounted rewards Eπ[ΣT -1 t=0 γtr(st)]. (p. 3, IV. POLICY LEARNING IN SIMULATION).
2. Use the paper-reported task/data/environment cue: The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects before releasing them. (p. 8, VI. REAL-WORLD EXPERIMENTS).
3. Compare against the reported or matched baseline: To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and insertion) without any policy adaptation phase ... (p. 8, VI. REAL-WORLD EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). (p. 8, VI. REAL-WORLD EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and insertion) without any policy adaptation phase ... (p. 8, VI. REAL-WORLD EXPERIMENTS); if none is reported, design one around: Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this issue. (p. 8, VI. REAL-WORLD EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 9 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), and measure the boundary at p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 9 (VIII. LIMITATIONS & FUTURE WORK).

## Falsifiable research question

Under the paper's stated interface (In summary, we developed the IndustRealLib library, which accepts trained policy checkpoints from Isaac Gym as input, and outputs targets for a ...), does the paper-specific mechanism (Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich ...) retain the reported evaluation outcome (Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III).) when tested against the paper's strongest explicit boundary (Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III).) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a simulator: a simulation-aware policy update ... (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Asset Pick Insert Pick-Place-Insert Success Success Engage Success Engage Round peg 8 mm 19/20 7/10 7/10 7/10 7/10 Round peg 12 mm 19/20 7/10 9/10 7/10 7/10 Round peg 16 ... (p. 9, VI. REAL-WORLD EXPERIMENTS).
- **Strongest explicit boundary:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this issue. (p. 8, VI. REAL-WORLD EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
