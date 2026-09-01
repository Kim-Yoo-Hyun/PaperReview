# Insights — Hybrid Position/Force Control of Manipulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3139652; PDF retrieval source: https://doi.org/10.1115/1.3139652. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Front matter - extractive body cue:** Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.
- **p. 3 / Front matter - extractive body cue:** The transformation form (C) to the joints of the manipulator is such that, for the general case, control of one manipulator joint involves every dimension ...
- **p. 1 / Front matter - extractive body cue:** Such techniques are just now being developed.
- **p. 3 / Front matter - extractive body cue:** The present control methodology was designed to address this low-level control problem.
- **p. 4 / Front matter - extractive body cue:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin ...
- **p. 5 / Front matter - extractive body cue:** The model includes a simplified static friction term plus the Coulomb force: r-sgn(<7,.)[min(Ti];,lT,-l)] L-sgn(<7i)[Tc,i] where: TS = static friction constant TC = Coulomb friction constant ...
- **p. 1 / Front matter - extractive body cue:** The first two of these techniques are limited by the accuracy and availability of manipulator models that compensate for the complicated inertial, frictional, and gravitational ...
- **Contribution anchor:** p. 1 (Front matter), p. 3 (Front matter), p. 1 (Front matter), p. 3 (Front matter), p. 4 (Front matter), p. 5 (Front matter)

### Strongest assumption and failure boundary

- **p. 1 / Front matter - extractive body cue:** The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.
- **p. 1 / Front matter - extractive body cue:** But perhaps more important is the lack of adequate controller architectures and computing techniques needed to take advantage of such sensory information, where it available.
- **p. 2 / Front matter - extractive body cue:** In general, for each task configuration a generalized surface can be defined in a constraint space having N degrees of freedom, with position constraints along ...
- **p. 2 / Front matter - extractive body cue:** These constraints also occur along the tangents and normals to the generalized surface, but, unlike natural constraints, artificial force constraints are specified along surface normals, ...
- **p. 3 / Front matter - extractive body cue:** The present control methodology was designed to address this low-level control problem.
- **p. 4 / Front matter - extractive body cue:** A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.
- **p. 6 / Front matter - extractive body cue:** As motion begins force control degrades somewhat, although contact with the reaction surface is never lost.
- **Boundary to test:** A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors. | p. 1 (Front matter), p. 3 (Front matter) |
| Reported outcome | To improve thermal immunity, gauges mounted on opposite faces are operated as voltage divider pairs [9J. | p. 4 (Front matter), p. 5 (Front matter) |
| Failure/limitation | A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing. | p. 4 (Front matter), p. 6 (Front matter) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], and one for each position controlled degree of freedom: (2) ...를 A number of methods for obtaining force information exist: motor currents may be measured or programmed, [6, 11], motor output torques may be measured [7], and wrist or hand mounted sensors may ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, force control, contact, manipulation`.
- **Reading predecessor in the generated track queue:** A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Impedance Control: An Approach to Manipulation: Part I—Theory (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 5 Model used for simulation of hybrid control task 1 1 l-Kwwt -Acosfa,)] w2 = TT \-~K^w7. +Asin(<?i)l M3 Reaction surface model: fx=K,.(Cx CXf) Cx = ^cosfa,) + /sinfa,) (7) (8) (9) ....
3. Compare against the body-reported baseline or a matched simpler baseline: Without this term the system was stable only when heavily overdamped..
4. Report the body metric and its denominator/aggregation: As the manipulator moves, irregularities in the reaction surface and small errors in the accuracy of the position servo will look like surface motion to the force controller..
5. Re-run the body-reported ablation/failure condition: Without this term the system was stable only when heavily overdamped..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (Front matter), p. 5 (Front matter), p. 1 (Front matter); the primary result is directionally consistent at p. 4 (Front matter), p. 5 (Front matter), p. 6 (Front matter); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Note, here, does mechanism이 Without this term the system was stable only when heavily overdamped. 대비 As the manipulator moves, irregularities in the reaction surface and small errors in the accuracy of the position ...을 개선하고, A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
