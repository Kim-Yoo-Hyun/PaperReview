# Insights — Impedance Control: An Approach to Manipulation: Part I—Theory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3140702; PDF retrieval source: https://doi.org/10.1115/1.3140702. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Front matter - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / Front matter - extractive body cue:** The approach developed encompasses and includes the simple positioning or transporting tasks typically performed by robots and/or prostheses.
- **p. 2 / Front matter - extractive body cue:** In the following it is developed from some simple and physically reasonable assumptions.
- **p. 6 / 1 Y - extractive body cue:** Several simple but fundamental observations may then be made: Command and control of a vector such as position or force is not enough to control ...
- **p. 5 / 1 Y - extractive body cue:** That network depicts the separation of the controller action into two distinct components, one (the flow source) representing the control of motion, the other (the ...
- **p. 6 / 1 Y - extractive body cue:** By assuming that no control algorithm may make a physical system behave like anything other than a physical system the network concepts of bond graphs ...
- **p. 5 / 1 Y - extractive body cue:** The manipulator behavior (assumed to be nodic) is then characterized by a static relation between force and position (modulated by the command set).
- **Contribution anchor:** p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 6 (1 Y), p. 5 (1 Y), p. 6 (1 Y)

### Strongest assumption and failure boundary

- **p. 4 / Front matter - extractive body cue:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as ...
- **p. 3 / Front matter - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...
- **p. 3 / Front matter - extractive body cue:** The kinematic transformation equations are: X1=Ll cos 6{+L2 cos d2+L3 cos d3 (3) X2=Lt smdl+L2smd2+L3sm61 (4) Again, joint angles uniquely define end-point position but the ...
- **p. 1 / Front matter - extractive body cue:** It will be shown (in Parts II and III) that the approach can lead to a simplification of some problems in manipulator control.
- **p. 1 / Front matter - extractive body cue:** It is shown that as manipulation is a fundamentally nonlinear problem, the distinction between impedance and admittance is essential, and given the environment contains inertial ...
- **p. 5 / 1 Y - extractive body cue:** The behavior of the manipulator may now be written as follows (assuming a state-determined system): V 0=V 0:jc) Virtual Source (10) f = V 0 ...
- **p. 2 / Front matter - extractive body cue:** The high-level supervisor, while it may have access to sensory data, does not use that data in an immediate feedback control mode to modulate its ...
- **Boundary to test:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In Part I this approach is developed by considering the mechanics of interaction between physical systems. | p. 1 (Front matter), p. 1 (Front matter) |
| Reported outcome | The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) can be achieved for a general class of nonlinear controlled ... | p. 5 (1 Y) |
| Failure/limitation | Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable. | p. 3 (Front matter), p. 4 (Front matter) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 As the constitutive equation for a point mass is invertible the equations may also be written with Nomenclature W = mechanical work F,F, ,F2 = force TL,XX ,X2 = position Li,L2,L3 = ...를 For example, the constitutive equation for a point mass is fundamentally written with velocity as the output variable, defined as a function of momentum; momentum in turn is the integral of the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, Impedance Control, contact, manipulation`.
- **Reading predecessor in the generated track queue:** Hybrid Position/Force Control of Manipulators (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output variable.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and there is some evidence that the mammalian ....
3. Compare against the body-reported baseline or a matched simpler baseline: The superposition properties of the Norton equivalent network have been retained without restriction to linear systems..
4. Report the body metric and its denominator/aggregation: Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate as they are insufficient to control the mechanical work exchanged between the manipulator and ....
5. Re-run the body-reported ablation/failure condition: In fact, linearized components of the impedance such as the stiffness and the viscosity are second-rank twice covariant tensors..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (1 Y), p. 5 (1 Y), p. 6 (1 Y); the primary result is directionally consistent at p. 5 (1 Y); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Part, developed, considering mechanism이 The superposition properties of the Norton equivalent network have been retained without restriction to linear systems. 대비 Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate ...을 개선하고, Real physical elastic devices exist which cannot be described in the derivative causal form with force ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
