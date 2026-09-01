# Insights — Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.14127; PDF retrieval source: https://arxiv.org/pdf/2103.14127. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method is closely related to the work of Murali et al.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these issues, our method instead directly processes a full scene point cloud or a local region around a target object.
- **p. 3 / III. METHOD - extractive body cue:** We used the ACRONYM dataset [32], which consists of 8872 meshes from the Shapenet dataset [35] and 17.7 million
- **p. 4 / III. METHOD - extractive body cue:** Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given in Eq.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we ...
- **p. 4 / III. METHOD - extractive body cue:** The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, from which we ...
- **p. 3 / III. METHOD - extractive body cue:** In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in grasping [11] and ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Grasping objects from cluttered scenes with structure introduces extra challenges.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our representation has only 4-DoF which facilitates the learning problem significantly. • Comprehensive ablation studies in a physics simulator to evaluate the effects of different ...
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps are ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. Grasp ...
- **Boundary to test:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method is closely related to the work of Murali et al. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Failure/limitation | Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes. | p. 6 (V. CONCLUSIONS), p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 Their predictions can be directly associated to 3D points in the input point cloud and our proposed grasp representation exploits this ability.를 Network We employ the set abstraction and feature propagation layers proposed in PointNet++ [34] to build an asymmetric Ushaped network.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method is closely related to the work of Murali et al.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, grasping, contact prediction, 6-DoF grasp`.
- **Reading predecessor in the generated track queue:** GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Factory: Fast Contact for Robotic Assembly (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes..
3. Compare against the body-reported baseline or a matched simpler baseline: We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines..
4. Report the body metric and its denominator/aggregation: The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the first decimal of coverage..
5. Re-run the body-reported ablation/failure condition: Fig. 5. Loss Ablations: Without weighted binning in the grasp width loss lwidth both, success rate and coverage decrease. The ladd-s loss leads to increased success rates at high confidence contacts (Coverage ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 closely, related, Murali mechanism이 We observe a significantly higher grasp success rate of our method compared to [11] and [12] ... 대비 The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most ...을 개선하고, Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
