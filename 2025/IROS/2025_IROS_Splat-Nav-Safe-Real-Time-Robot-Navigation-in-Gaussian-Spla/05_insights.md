# Insights — Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.02751; PDF retrieval source: https://arxiv.org/pdf/2403.02751. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce Splat-Nav, a pipeline for drone navigation in GSplat maps with a monocular camera.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Additionally, the proposed system enables both open-loop trajectory generation and closed-loop re-planning.
- **p. 4 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Now, we present Splat-Plan, our planner for GSplat maps.
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** We propose to solve maxs∈[0,1] K(s) using Algorithm 1.
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** While there are many ways one could convert the ellipsoidal representation into a conservative occupancy grid, we propose the following method that is parallelizable and ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** NeRFs generate photorealistic scene reconstructions, addressing the fundamental limitations of explicit representations; however, NeRFs require running inference on a deep neural network to render the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Similarly, we find that Splat-Loc is more accurate, faster, and fails less often compared to baselines.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We use a language-embedded GSplat to enable open-vocabulary specification of goal locations like "go to the microwave." of the existing localization module or used as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The latter is important in long trajectories, where existing onboard localization may drift or be subject to noise, impacting the overall safety of the executed ...
- **p. 16 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate.
- **p. 16 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless regions of the scene where the PnP-RANSAC ...
- **Boundary to test:** Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • We develop ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate. | p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS) |
| Failure/limitation | Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation. | p. 16 (VIII. LIMITATIONS AND FUTURE WORK), p. 12 (VI. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for i ←0 to k do // Test ...를 Splat-Nav comprises a lightweight pose estimation module, Splat-Loc, coupled with a planning module, Splat-Plan, to enable safe navigation from RGB-only (monocular) camera observations, as illustrated in Figure 1.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • We develop ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, Navigation, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** SUGAR: Pre-training 3D Visual Representations for Robotics (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, Flightroom, and Old Union..
3. Compare against the body-reported baseline or a matched simpler baseline: Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full scene geometry..
4. Report the body metric and its denominator/aggregation: We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation time (C.T.) per frame, and the overall success rate (S.R.)..
5. Re-run the body-reported ablation/failure condition: Number of Gaussians is reported for both dense and sparse variants of the same scene..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES); the primary result is directionally consistent at p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, develop mechanism이 Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when ... 대비 We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation ...을 개선하고, Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
