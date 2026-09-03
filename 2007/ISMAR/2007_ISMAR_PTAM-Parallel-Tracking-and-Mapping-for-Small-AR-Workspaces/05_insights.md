# Insights — PTAM: Parallel Tracking and Mapping for Small AR Workspaces

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.robots.ox.ac.uk/~gk/PTAM/; PDF retrieval source: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / ABSTRACT - extractive body cue:** While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The map consists of a collection of M point features located in a world coordinate frame W.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** While we adopt the stereo initialisation, and occasionally make use of local bundle updates, our method is different in that we attempt to build a ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose to split tracking and mapping into two separate tasks, processed in parallel threads on a dual-core computer: one thread deals with the task ...
- **p. 4 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** If the fraction falls below an even lower threshold for more than a few frames (during which the motion model might successfully bridge untrackable frames) ...
- **p. 3 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** We use a decaying velocity model; this is similar to a simple alpha-beta constant velocity model, but lacking any new measurements, the estimated camera slows ...
- **p. 5 / 3. A small number (50) of the coarsest-scale features are - extractive body cue:** Bundle adjustment iteratively adjusts the map so as to minimise the robust objective function: ˘ {µ2..µN}, {p′ 1..p′ M} ¯ = argmin {{µ},{p}} N X ...
- **Contribution anchor:** p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 4 (3. A small number (50) of the coarsest-scale features are), p. 3 (3. A small number (50) of the coarsest-scale features are)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Finally, in our hand-held camera scenario, we cannot rely on long 2D feature tracks being available to initialise features and we replace this with an ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Here, we argue that tracking a hand-held camera is more difficult than tracking a moving robot: firstly, a robot usually receives some form of odometry; ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The majority of Augmented Reality (AR) systems operate with prior knowledge of the user's environment - i.e, some form of map.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The logical extension of extensible tracking is to track in scenes without any prior map, and this is the focus of this paper.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Map points are projected into the image according to the frame's prior pose estimate.
- **p. 8 / 7 RESULTS - extractive body cue:** 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.
- **p. 8 / 7 RESULTS - extractive body cue:** AR applications are usable as soon as the map has been initialised from stereo; mapping proceeds in the background in a manner transparent to the ...
- **Boundary to test:** 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera in a small AR workspace. | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Reported outcome | At the same time, the use of a larger number of features reduces visible tracking jitter and improves performance when some features are occluded or otherwise corrupted. | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |
| Failure/limitation | 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented. | p. 8 (7 RESULTS), p. 8 (7 RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 For this reason, the tracking system estimates the quality of tracking at every frame, using the fraction of feature observations which have been successful.를 Writing the current state of the map as {EK1W, ...EKN W} and {p1, ...pM}, each image measurement also has an associated reprojection error eji calculated as for equation (9).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: While this has previously been attempted by adapting SLAM algorithms developed for robotic exploration, we propose a system specifically designed to track a hand-held camera in a small AR workspace.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, SLAM, geometry, camera pose`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system presented.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This system requires fairly powerful computing hardware and this has so far limited live experiments to a single office; we expect that with some optimisations we will be able to run at ....
3. Compare against the body-reported baseline or a matched simpler baseline: Compared with bundle adjustment, the processing time required for epipolar search and occasional data association refinement is small..
4. Report the body metric and its denominator/aggregation: This game demonstrates tracking accuracy..
5. Re-run the body-reported ablation/failure condition: This video represents the size of a typical working volume which the system can handle without great difficulty..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3. A small number (50) of the coarsest-scale features are), p. 1 (ABSTRACT), p. 1 (ABSTRACT); the primary result is directionally consistent at p. 8 (7 RESULTS), p. 8 (7 RESULTS), p. 6 (7 RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 While, previously, been mechanism이 Compared with bundle adjustment, the processing time required for epipolar search and occasional data association refinement ... 대비 This game demonstrates tracking accuracy.을 개선하고, 8 LIMITATIONS AND FUTURE WORK This section describes some of the known issues with the system ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
