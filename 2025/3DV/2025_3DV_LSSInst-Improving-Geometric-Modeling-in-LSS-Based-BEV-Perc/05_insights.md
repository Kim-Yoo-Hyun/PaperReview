# Insights — LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://arxiv.org/pdf/2411.06173.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with ...
- **p. 2 / 1. Introduction - extractive body cue:** With this in mind, we propose the instance adaptor module to establish semantic coherence between the scene and instances and an instance branch for detection.
- **p. 3 / 3. Methodology - extractive body cue:** The overview of our framework is shown in Fig.
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive body cue:** Then we introduce five separated linear projections {Ej l3}2 j=1 ∈R3×C, {Ej l2}2 j=1 ∈R2×C and Eg ∈RC×C for comprehensive encoding, of which the former ...
- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 4 / 3. Methodology - extractive body cue:** BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 5 (3. Methodology), p. 4 (3. Methodology)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.
- **p. 2 / 1. Introduction - extractive body cue:** However, this collaboration also poses challenges, as the most straightforward solution of naively sharing the bounding box proposal is intuitively and experimentally failed 1.
- **p. 2 / 1. Introduction - extractive body cue:** On the nuScenes dataset, our LSSInst method demonstrates strong generalization ability.
- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive body cue:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries ...
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive body cue:** In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors.
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive body cue:** The noise resistance results for robustness.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here ...
- **Boundary to test:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries yielded mediocre performance, which shows the slow ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with instance representations; ii) We proposed the instance ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | The table reveals that our LSSInst achieves notable improvements in mAP and NDS compared to standalone BEV detectors at a minor cost. | p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results) |
| Failure/limitation | We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries yielded mediocre performance, which shows the slow ... | p. 7 (4.5. Multiplicate Queries Ablations), p. 7 (4.4. Noise Resistance for Practical Robustness) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network for feature extraction.를 Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence Feature Extraction Net Voxel Pooling ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries yielded mediocre performance, which shows the slow ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with instance representations; ii) We proposed the instance ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `sensor fusion, LiDAR, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries yielded mediocre performance, which shows the slow ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene..
3. Compare against the body-reported baseline or a matched simpler baseline: We compared our approach with LSS-based and two-stage state-of-the-art methods on the nuScenes val and test sets..
4. Report the body metric and its denominator/aggregation: Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here we use * to denote this) by ....
5. Re-run the body-reported ablation/failure condition: On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3. Methodology), p. 4 (3. Methodology), p. 3 (3. Methodology); the primary result is directionally consistent at p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results), p. 7 (4.5. Multiplicate Queries Ablations); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, concluded mechanism이 We compared our approach with LSS-based and two-stage state-of-the-art methods on the nuScenes val and test ... 대비 Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E ...을 개선하고, We can observe that on the one hand, relying solely on the potential queries cannot play ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
