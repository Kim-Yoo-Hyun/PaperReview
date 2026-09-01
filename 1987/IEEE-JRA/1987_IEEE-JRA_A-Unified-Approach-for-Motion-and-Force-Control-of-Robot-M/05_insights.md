# Insights — A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://cs.stanford.edu/group/manips/publications.html; PDF retrieval source: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 3 / I. Inrropucrion - extractive body cue:** This allows a more efficient implementation of the control system for real-time operations.
- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that of the mechanism ...
- **p. 1 / I. Inrropucrion - extractive body cue:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.
- **p. 1 / I. Inrropucrion - extractive body cue:** ‘The issue of end-effector dynamic modeling and control is yet more acute for tasks that involve combined motion and ‘contact forces of the end-effector.
- **p. 3 / I. Inrropucrion - extractive body cue:** However, the control of end-effector motion and contact forces, or the analysis and characterization of endeffector dynamic performance requires the construction of the model describing ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (Abstract), p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion)

### Strongest assumption and failure boundary

- **p. 1 / I. Inrropucrion - extractive body cue:** The magnitude of these dynamic forces cannot be ignored when large accelerations and fast motions are considered.
- **p. 1 / I. Inrropucrion - extractive body cue:** Obviously, these characteristics cannot be found in the manipulator joint space dynamic model, which only provides a description of the interaction between joint motions.
- **p. 2 / I. Inrropucrion - extractive body cue:** Tl, GeneRALizeD Task SpEciricaTion MarRices
- **p. 2 / I. Inrropucrion - extractive body cue:** In this paper, a new approach for dealing with the problem of kinematic singularities within the operational space framework is presented.
- **p. 3 / I. Inrropucrion - extractive body cue:** First, let us consider the case of nonredundant manipulators, where a set of operational coordinates can be selected asa system of generalized coordinates for the ...
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]
- **p. 7 / VI. ReDunpaNT MANIPULATORS - extractive body cue:** ‘The configuration of a redundant manipulator cannot be specified by a set of parameters that only describes the endeffector position and orientation.
- **Boundary to test:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn | p. 1 (Abstract), p. 1 (Abstract) |
| Reported outcome | The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ‘operational forces acting on it. | p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt) |
| Failure/limitation | This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15] | p. 5 (IV. Exp-Errecror Morton Controt), p. 7 (VI. ReDunpaNT MANIPULATORS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.를 The description of the dynamic interaction between end-effector motions and the effects of these motions on the end-effector's behavior in the direction of force control are basic requirements for the analysis and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, operational space control, force control, manipulation`.
- **Reading predecessor in the generated track queue:** Planning and Acting in Partially Observable Stochastic Domains (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Hybrid Position/Force Control of Manipulators (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This command vector is particularly useful when Used in conjunction with the gradient of an artificial potential field for collision avoidance (15]; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 46 IEEE JOURNAL OF ROBOTICS AND AUTOMATION, VOL..
3. Compare against the body-reported baseline or a matched simpler baseline: baseline not recovered.
4. Report the body metric and its denominator/aggregation: In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related to manipulator tasks..
5. Re-run the body-reported ablation/failure condition: These forces can be selected to actin the null space of the Jacobian matrix [16] This precludes any effect of the additional forces on the endeffector and maintains its dynamic decoupling..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion); the primary result is directionally consistent at p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt), p. 6 (V. Constnainep Motion Operarions); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 development, dealing, problems mechanism이 a matched simpler baseline 대비 In operational space control systeins, however, errors, performance, dynamics, simplifications, characteriza tions, and controlled variables are directly related ...을 개선하고, This command vector is particularly useful when Used in conjunction with the gradient of an artificial ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
