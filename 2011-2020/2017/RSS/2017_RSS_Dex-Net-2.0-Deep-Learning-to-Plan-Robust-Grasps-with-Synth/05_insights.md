# Insights — Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.09312; PDF retrieval source: https://arxiv.org/pdf/1703.09312. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that the Dex-Net 2.0 grasp planner is 3× faster than the registration-based method, 93% successful on objects seen in training (the highest of ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Learning Q rather than directly learning the policy allows us to enforce task-specific constraints without having to update the learned model.
- **p. 5 / V. GRASP PLANNING - extractive body cue:** The Dex-Net 2.0 grasp planner uses the robust grasping policy πθ(y) = argmaxu∈CQθ(u, y) illustrated in Fig.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 5 (V. GRASP PLANNING)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Reliable robotic grasping is challenging due to imprecision in sensing and actuation, which leads to uncertainty about properties such as object shape, pose, material properties, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** (Right) The GQ-CNN rapidly determines the most robust grasp candidate, which is executed with the ABB YuMi robot. not generalize well to new objects, and ...
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We consider the problem of planning a robust planar parallel-jaw grasp for a singulated rigid object resting on a table based on point clouds from ...
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, 56], or probability ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Let the robustness of a grasp given an observation [5, 56] be the expected value of the metric, or probability of success under uncertainty in ...
- **p. 8 / I. Failure Modes - extractive body cue:** The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of ...
- **p. 8 / I. Failure Modes - extractive body cue:** A second type of failure occured due to collisions with the object.
- **Boundary to test:** The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of the object surface, and (right) collisions with ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps planned using robust quasi-static GWS analysis on ... | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | We found that GQ planned grasps 3× faster than REG and achieved a high 93% success rate and 94% precision. | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Failure/limitation | The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of the object surface, and (right) collisions with ... | p. 8 (I. Failure Modes), p. 8 (I. Failure Modes) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 We learn a function that takes as input a candidate grasp and a depth image and outputs an estimate of robustness [27, 56], or probability of success under uncertainty in sensing and ...를 Let y = RH×W + be a 2.5D point cloud represented as a depth image with height H and width W taken by a camera with known intrinsics [18], and let Tc ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of the object surface, and (right) collisions with ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our primary contributions are: 1) the Dexterity Network (Dex-Net) 2.0, a dataset associating 6.7 million point clouds and analytic grasp quality metrics with parallel-jaw grasps planned using robust quasi-static GWS analysis on ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, grasping, synthetic data, analytic grasp metric`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The most common failure modes were related to: (left) missing sensor data for an important part of the object geometry, such as thin parts of the object surface, and (right) collisions with ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To benchmark the architecture outside of our datasets, we trained on the Cornell Grasping Dataset [31] (containing 8,019 examples) and achieved a 93.0% recognition rate using grayscale images and an 80-20 imagewise ....
3. Compare against the body-reported baseline or a matched simpler baseline: Grasp Planning Methods Used for Comparison We compared a number of grasp planning methods on simulated and real data..
4. Report the body metric and its denominator/aggregation: Comparions of Methods GQ-CNN Parameter Sensitivity Random IGQ ML-RF ML-SVM REG GQ-L-Adv GQ-S-Adv GQ-Adv GQ-Adv-Phys GQ-Adv-FC GQ-Adv-LowU GQ-Adv-HighU Success Rate (%) 58±11 70±10 75±9 80±9 95±5 93±6 85±8 83±8 80±9 83±8 78±9 ....
5. Re-run the body-reported ablation/failure condition: We also trained several variants to evaluate sensitivity to several parameters: Dataset Size..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (V. GRASP PLANNING); the primary result is directionally consistent at p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 primary, contributions, Dexterity mechanism이 Grasp Planning Methods Used for Comparison We compared a number of grasp planning methods on simulated ... 대비 Comparions of Methods GQ-CNN Parameter Sensitivity Random IGQ ML-RF ML-SVM REG GQ-L-Adv GQ-S-Adv GQ-Adv GQ-Adv-Phys GQ-Adv-FC GQ-Adv-LowU GQ-Adv-HighU ...을 개선하고, The most common failure modes were related to: (left) missing sensor data for an important part ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
