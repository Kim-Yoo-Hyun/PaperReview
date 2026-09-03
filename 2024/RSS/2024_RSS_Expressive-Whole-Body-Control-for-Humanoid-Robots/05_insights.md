# Insights — Expressive Whole-Body Control for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p107.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p107.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** The root movement goal gm can also be intuitively given by joystick commands, enabling convenient deployment in the real world. methods on both of these ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While our current results focus on expressive humanoid control, we hope our approach can also shed some light on studying generalizable humanoid whole-body manipulation
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** Specifically, in this work, we work with a relaxed problem where we exclude the joints and key points from the lower half of the body ...
- **p. 9 / VII. LIMITATIONS - extractive body cue:** Auto recovery and initialization could be explored to reduce the cost of doing experiments.
- **p. 9 / VI. DISCUSSIONS - extractive body cue:** We introduce a method designed to enable a humanoid robot to track expressive upper body motions while ensuring the maintenance of robust locomotion capabilities in ...
- **p. 5 / IV. RESULTS - extractive body cue:** Note that although Random Sample looks better than Motion Sample, the heatmap does not consider the sample density.
- **Boundary to test:** Auto recovery and initialization could be explored to reduce the cost of doing experiments.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that relaxes the constraints indeed leads to better ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | V, our method achieves the best linear velocity tracking performance (MELV). | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Failure/limitation | Auto recovery and initialization could be explored to reduce the cost of doing experiments. | p. 9 (VII. LIMITATIONS), p. 9 (VI. DISCUSSIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the behavior, S is the observation space, and ...를 However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: We aim to produce a robust control ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Auto recovery and initialization could be explored to reduce the cost of doing experiments.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that relaxes the constraints indeed leads to better ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, motion imitation, sim-to-real`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Auto recovery and initialization could be explored to reduce the cost of doing experiments.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How well does ExBody perform on tracking ge and gm? • ....
3. Compare against the body-reported baseline or a matched simpler baseline: We compare with baselines to show that our approach ExBody is superior compared with other design choices..
4. Report the body metric and its denominator/aggregation: However, it has even worse performance, demonstrating a high-frequency jittery movement that is not feasible for sim-to-real transfer, indicating for such a complex system, AMP reward itself is not sufficient..
5. Re-run the body-reported ablation/failure condition: We can see that our policy can track roll, pitch and root height well without being affected by walking velocity..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION); the primary result is directionally consistent at p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 9 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 compare, applying, more mechanism이 We compare with baselines to show that our approach ExBody is superior compared with other design ... 대비 However, it has even worse performance, demonstrating a high-frequency jittery movement that is not feasible for sim-to-real transfer, ...을 개선하고, Auto recovery and initialization could be explored to reduce the cost of doing experiments. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
