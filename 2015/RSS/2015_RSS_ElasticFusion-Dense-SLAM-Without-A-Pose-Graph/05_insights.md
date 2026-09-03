# Insights — ElasticFusion: Dense SLAM Without A Pose Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss11/p01.html; PDF retrieval source: https://www.roboticsproceedings.org/rss11/p01.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / II. APPROACH OVERVIEW - extractive body cue:** In the following, we summarise the key elements of our method.
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** This component of our method is inspired by the surfelbased fusion system of Keller et al.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.
- **p. 2 / II. APPROACH OVERVIEW - extractive body cue:** We adopt an architecture which is typically found in realtime dense visual SLAM systems that alternates between tracking and mapping [15, 25, 9, 8, 2, ...
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** If registration is successful, a loop has been closed to the older inactive model and the entire model is non-rigidly deformed into place to reflect ...
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** In the following section we describe our fused map representation and method for predictive tracking.
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive body cue:** If a match is detected, register the views together and check if the registration is globally consistent with the model's geometry.
- **Contribution anchor:** p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 1 (I. INTRODUCTION), p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, existing dense SLAM methods suitable for incremental, real-time operation struggle when the sensor makes movements which are both of extended duration and often criss-cross ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on ...
- **p. 8 / VIII. CONCLUSION - extractive body cue:** In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM ...
- **p. 7 / VII. EVALUATION - extractive body cue:** We evaluate our approach on all four trajectories in the living room scene (including synthetic noise) providing surface reconstruction accuracy results in comparison to the ...
- **Boundary to test:** In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM as t →∞.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In the following, we summarise the key elements of our method. | p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment) |
| Reported outcome | Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive model deformations are used, proving their efficacy in trajectory estimation. | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Failure/limitation | In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM as t →∞. | p. 8 (VIII. CONCLUSION), p. 7 (VII. EVALUATION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on par with or better than existing dense ...를 We mainly use CUDA to implement our tracking reduction process and the OpenGL Shading Language for view prediction and map management.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM as t →∞.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In the following, we summarise the key elements of our method.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, SLAM, RGB-D, 3D reconstruction`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM as t →∞.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The Lab dataset contains a very loopy trajectory around a large office environment with many global and local loop closures..
3. Compare against the body-reported baseline or a matched simpler baseline: These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig..
4. Report the body metric and its denominator/aggregation: We evaluate the performance of our system both quantitatively and qualitatively in terms of trajectory estimation, surface reconstruction accuracy and computational performance..
5. Re-run the body-reported ablation/failure condition: Points more than 0.1m from ground truth have been removed for visualisation purposes..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment); the primary result is directionally consistent at p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION), p. 8 (VII. EVALUATION); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 following, summarise, elements mechanism이 These results show that our trajectory estimation performance is on par with or better than existing ... 대비 We evaluate the performance of our system both quantitatively and qualitatively in terms of trajectory estimation, surface reconstruction ...을 개선하고, In future work we wish to address the problem of map scalability beyond whole rooms and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
