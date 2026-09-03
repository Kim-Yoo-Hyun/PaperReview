# Insights — Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1410.7284; PDF retrieval source: https://arxiv.org/pdf/1410.7284. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).
- **p. 1 / 1 Introduction - extractive body cue:** Recent contributions have also demonstrated the relevance of torque control approaches for humanoid robots [13,28,36].
- **p. 2 / 1 Introduction - extractive body cue:** It has been shown in several contributions [39,21] that the regulation of momentum could be very powerful for control on humanoids.
- **p. 2 / 1 Introduction - extractive body cue:** In a recent contribution [11], we have demonstrated that hierarchical inverse dynamics controllers could be efficiently used on a torquecontrolled humanoid robot.
- **p. 3 / 1 Introduction - extractive body cue:** Contribution In this contribution, we extend our preliminary work and present extensive experimental evaluations.
- **p. 17 / 6.2 Relation to other balancing approaches - extractive body cue:** However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then desired accelerations and ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive body cue:** In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use.
- **Contribution anchor:** p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 17 (6.2 Relation to other balancing approaches)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** However, the quasi-static assumption can be a limitation for dynamic motions.
- **p. 2 / 1 Introduction - extractive body cue:** However, pseudo-inverse-based controllers are limited as they cannot properly handle inequality constraints such as torque limits or friction cone constraints.
- **p. 3 / 1 Introduction - extractive body cue:** We also proposed a method to simplify the optimization problem by factoring the dynamics equations of the robot such that we could significantly reduce computational ...
- **p. 3 / 1 Introduction - extractive body cue:** Balancing experiments in various conditions demonstrate performances that are comparable to, if not better than, current state of the art balancing algorithms, even when the ...
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive body cue:** Desired contact forces can be directly expressed as equalities on the generalized forces λ.
- **p. 17 / 6.2 Relation to other balancing approaches - extractive body cue:** Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept ...
- **p. 17 / 6.3 Relations to other hierarchical inverse dynamics - extractive body cue:** On the other hand, it allows for prioritization of inequality constraints, which we exploit e.g. to give more importance to hardware limitations than to contact ...
- **Boundary to test:** Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept stationary.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5). | p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | This controller design allowed us to achieve good torque tracking performance. | p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control) |
| Failure/limitation | Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept stationary. | p. 17 (6.2 Relation to other balancing approaches), p. 17 (6.3 Relations to other hierarchical inverse dynamics) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Therefore it is not possible to directly control interaction forces during multi-contact tasks or to close a feedback loop directly around the tasks of interests, for example the center of gravity (CoG), ...를 This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept stationary.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, momentum control, inverse dynamics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept stationary.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In the following, however, we construct a more complex stepping task in simulation for the full 25 DoF robot..
3. Compare against the body-reported baseline or a matched simpler baseline: It is worth mentioning again that the foot size of the robot is rather small compared to other humanoids..
4. Report the body metric and its denominator/aggregation: It can be seen that overall the CoG error remains lower with the LQR controller, while the angular momentum behaves similarly. disturbance..
5. Re-run the body-reported ablation/failure condition: We expect to have even better performance once we perform a good identification of the dynamics [1,24] but it is interesting to note that good results with hierarchical inverse dynamics can be ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 17 (6.2 Relation to other balancing approaches), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation); the primary result is directionally consistent at p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control), p. 13 (5.3 Tracking Experiments in Double Support); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 leads, main, contribution mechanism이 It is worth mentioning again that the foot size of the robot is rather small compared ... 대비 It can be seen that overall the CoG error remains lower with the LQR controller, while the angular ...을 개선하고, Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
