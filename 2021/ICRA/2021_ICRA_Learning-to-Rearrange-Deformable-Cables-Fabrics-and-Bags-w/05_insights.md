# Insights — Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.03385; PDF retrieval source: https://arxiv.org/pdf/2012.03385. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and ...
- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** Goal-Conditioned Transporter Networks We propose two goal-conditioned architectures based on Transporter Networks.
- **p. 3 / III. BACKGROUND - extractive body cue:** To train the policy, we assume access to a small dataset of N stochastic expert demonstrations D = {ξi}N i=1, where each episode ξi of ...
- **p. 4 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** [53], [54]. with rotations and translations, this enables data augmentation by randomizing a rotation and translation for each training image.
- **p. 3 / IV. GOAL-CONDITIONED TRANSPORTER NETWORKS - extractive body cue:** For the goal-conditioned Transporter Networks, we use the same procedure to get (ok, ak), then additionally use the corresponding observation og after the last action ...
- **p. 1 / Abstract - extractive body cue:** We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 3 (III. BACKGROUND), p. 4 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast to rigid object manipulation, deformable object manipulation presents additional challenges due to more complex configuration spaces, dynamics, and sensing.
- **p. 3 / III. BACKGROUND - extractive body cue:** While this discrete-time planar action parameterization has its limitations, we find that it remains sufficiently expressive for a number of tabletop tasks involving manipulation of ...
- **p. 2 / III. BACKGROUND - extractive body cue:** We first describe the problem formulation, followed by background on Transporter Networks [68].
- **p. 2 / III. BACKGROUND - extractive body cue:** Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering ...
- **p. 4 / V. SIMULATOR AND TASKS - extractive body cue:** While prior work with soft bodies in PyBullet [18], [19], [44] use position-based dynamics solvers, we use new soft body physics simulation based on the ...
- **Boundary to test:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering up the bag opening; these are hard ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve 100% success rates ... | p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS) |
| Failure/limitation | Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering up the bag opening; these are hard ... | p. 6 (Figure/Table caption), p. 4 (V. SIMULATOR AND TASKS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 The first FCN fpick takes as input the visual observation ot, and outputs a dense per-pixel prediction of action-values Qpick that correlate with picking success: Tpick = arg max(u,v) Qpick((u, v)/ot) where ...를 Problem Formulation We formulate the problem of rearranging deformable objects as learning a policy π that sequences pick and place actions at ∈A with a robot from visual observations ot ∈O: π(ot) ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering up the bag opening; these are hard ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned variants of Transporter Network [68] architectures.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, deformable object, cable manipulation, cloth manipulation, goal-conditioned learning, vision-based control`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all bag tasks, a failure case may result from covering up the bag opening; these are hard ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We next validate experiments on physical hardware using a Franka Panda robot with a standard parallel-jaw gripper..
3. Compare against the body-reported baseline or a matched simpler baseline: Goal Conditioned Tasks Across all 4 dataset sizes for cable-line-notarget, cableshape-notarget, and fabric-flat-notarget, both TransporterGoal-Stack and Transporter-Goal-Split substantially outperform the two GT-State baselines..
4. Report the body metric and its denominator/aggregation: Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, since both goal-conditioned Transporters each achieve 100% success rates ....
5. Re-run the body-reported ablation/failure condition: Fig. 4: Top row: examples of physical bags. The bags we use follow a design similar to the sack (top left) and drawstring (top middle). Bags with handles (e.g., top right) or ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (IV. GOAL-CONDITIONED TRANSPORTER NETWORKS), p. 1 (Abstract), p. 3 (III. BACKGROUND); the primary result is directionally consistent at p. 6 (VII. SIMULATION RESULTS), p. 6 (VII. SIMULATION RESULTS), p. 5 (VII. SIMULATION RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 several, tasks, benchmark mechanism이 Goal Conditioned Tasks Across all 4 dataset sizes for cable-line-notarget, cableshape-notarget, and fabric-flat-notarget, both TransporterGoal-Stack and ... 대비 Transporter-Goal-Stack achieves slightly higher performance among the cable-related tasks, though the gap narrows with more demonstrations in cable-line-notarget, ...을 개선하고, Fig. 5: Failure cases we observe from trained Transporter policies on bag tasks. Left: in all ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
