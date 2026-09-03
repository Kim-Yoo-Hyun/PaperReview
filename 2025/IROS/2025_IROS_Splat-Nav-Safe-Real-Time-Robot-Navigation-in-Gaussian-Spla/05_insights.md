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

- **Paper-specific interface:** Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for i ←0 to k do ... (p. 6, IV. PLANNING WITH SAFE POLYTOPES).
- **Paper-specific mechanism:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Lastly, we examine the performance of the pose estimation algorithms in problems with a larger error in the initial estimate of the pose, with δR = 30◦and δt = 0.5 ... (p. 11, VI. EXPERIMENTS); the relevant task/metric cue is We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation time (C.T.) per frame, and the overall success rate (S.R.). (p. 11, VI. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. (p. 12, VI. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, Navigation, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** SUGAR: Pre-training 3D Visual Representations for Robotics (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for i ←0 to k do ... (p. 6, IV. PLANNING WITH SAFE POLYTOPES); preserve the objective/update rule: There are four primary components: (1) feasible path seeding through graph-based search, (2) construction of a collision set around each part of the path, (3) generation of hyperplane constraints, and ... (p. 7, IV. PLANNING WITH SAFE POLYTOPES).
2. Use the paper-reported task/data/environment cue: Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, Flightroom, and Old Union. (p. 10, VI. EXPERIMENTS).
3. Compare against the reported or matched baseline: Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full scene geometry. (p. 11, VI. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation time (C.T.) per frame, and the overall success rate (S.R.). (p. 11, VI. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Number of Gaussians is reported for both dense and sparse variants of the same scene. (p. 11, VI. EXPERIMENTS); if none is reported, design one around: More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. (p. 12, VI. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 11 (VI. EXPERIMENTS), p. 10 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), and measure the boundary at p. 12 (VI. EXPERIMENTS), p. 16 (VIII. LIMITATIONS AND FUTURE WORK).

## Falsifiable research question

Under the paper's stated interface (Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, ...), does the paper-specific mechanism (The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe ...) retain the reported evaluation outcome (We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation ...) when tested against the paper's strongest explicit boundary (More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone navigation in GSplat maps. • ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Lastly, we examine the performance of the pose estimation algorithms in problems with a larger error in the initial estimate of the pose, with δR = 30◦and δt = 0.5 ... (p. 11, VI. EXPERIMENTS).
- **Strongest explicit boundary:** More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. (p. 12, VI. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
