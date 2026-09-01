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

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and parameterized by a network with weights θ; ...를 An established approach for applying policy actions is sd t+1 = st ⊕at = st ⊕Π(ot), (2) where sd t+1 is the desired state, at is an action expressed as an incremental ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their corresponding sockets.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as a list of all purchased parts.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, assembly, contact-rich manipulation, Reinforcement Learning, sim-to-real, industrial robotics`.
- **Reading predecessor in the generated track queue:** Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Binding Touch to Everything: Learning Unified Multimodal Tactile Representations (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their corresponding sockets.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects before releasing them..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value at test time. Boxes indicate median and IQR. ....
4. Report the body metric and its denominator/aggregation: Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III)..
5. Re-run the body-reported ablation/failure condition: To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and insertion) without any policy adaptation phase in the ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION); the primary result is directionally consistent at p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 secondary, contributions, following mechanism이 Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum ... 대비 Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III).을 개선하고, Second, our primary failure cases on the real system were due to slip of the object ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
