# Insights — Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2510.19974; PDF retrieval source: https://arxiv.org/pdf/2510.19974. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.
- **p. 3 / IV. METHODS - extractive body cue:** Our framework operates in two phases.
- **p. 3 / IV. METHODS - extractive body cue:** We present the Push Anything framework (Fig.
- **p. 4 / IV. METHODS - extractive body cue:** (4d) Our method, C3+, seeks a more efficient solution than solving with an MIQP.
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** Hybrid models capture these behaviors by switching dynamics depending on the active contact mode.
- **p. 4 / IV. METHODS - extractive body cue:** While using linearized terms, this model preserves the multi-modal nature of contact dynamics through the complementarity constraint (3b).
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this limitation, Venkatesh, Bianchini et al.
- **p. 7 / VI. LIMITATIONS AND FUTURE WORK - extractive body cue:** Another limitation is we model all objects with identical mass and inertia.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive body cue:** All failures occurred when an object moved beyond the robot's reach.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** We predefine contact geometries, but contact point pairs and their corresponding normals are determined dynamically via collision detection at each control loop.
- **Boundary to test:** Another limitation is we model all objects with identical mass and inertia.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes. | p. 1 (I. INTRODUCTION), p. 3 (IV. METHODS) |
| Reported outcome | The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Failure/limitation | Another limitation is we model all objects with identical mass and inertia. | p. 7 (VI. LIMITATIONS AND FUTURE WORK), p. 6 (V. HARDWARE EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input bounds (5e).를 A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx is the state, uk ∈Rnu the control ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Another limitation is we model all objects with identical mass and inertia.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, model predictive control, non-prehensile manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Another limitation is we model all objects with identical mass and inertia.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained..
3. Compare against the body-reported baseline or a matched simpler baseline: For the Push T task, our framework achieves a mean time-to-goal of 26.9 s, improving upon prior work [4] at 30.5 s by 3.5 s (about 11.5%) while being more broadly applicable..
4. Report the body metric and its denominator/aggregation: Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon to enable precise multi-object manipulation. • Hardware validation: ....
5. Re-run the body-reported ablation/failure condition: Fig. 7. Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup. As defined below and illustrated in Fig. 5, the optimal value for each component of ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS); the primary result is directionally consistent at p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Push, Anything mechanism이 For the Push T task, our framework achieves a mean time-to-goal of 26.9 s, improving upon ... 대비 Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), ...을 개선하고, Another limitation is we model all objects with identical mass and inertia. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
