# Insights — Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p073.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** STAC does not require failure data, consists ofa score ‘computed post-hoc from a batch of predicted actions and a cconstant-time CP threshold to flag failures, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We show that FAIL-Detect identifies failures accurately and quickly on diverse robotic manipulation tasks, both in simulation and on robot hardware, outperforming SOTA failure detection ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The first A' <H actions Ave, sje are executed, after which the robot re-plans by generating a new sequence of HY actions attime t+-11'.
- **Contribution anchor:** p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION)

### Strongest assumption and failure boundary

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Detecting failures in robotic manipulation tasks poses several challenges.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** This poses significant challenges since collecting and annotating a comprehensive set of failure examples is often time-consuming, expensive, and even infeasible in many real-world scenarios.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** However, unlike FAIL-Detect, these methods require collecting failed trajectories a priori to detect failures.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** If the decision D(7;0) ~ 1, the rollout is flagged as a failure at time step ¢, For instance, in a pick-and-place task, a failure ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** This performance shows the capacity of failure-free failure detection methods to robustly identify failures across many scenarios.
- **Boundary to test:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the bottom during a policy rollout. We note ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference. | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Reported outcome | Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to compute the CP band: "setting-lependent" using successful ... | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Failure/limitation | Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the bottom during a policy rollout. We note ... | p. 5 (Figure/Table caption), p. 7 (C. Do failure detections align with human intuition?) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is a stochastic predictor of a ... (p. 3, III. PROBLEM FORMULATION).
- **Paper-specific mechanism:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data. (p. 1, 1. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to compute the CP band: "setting-lependent" ... (p. 7, Figure/Table caption); the relevant task/metric cue is {ask as both FM and DP policies achieve 100% soces, 5 for Can, which hes the shortest ask completion time. (p. 5, V. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as possible. (p. 6, V. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring`.
- **Reading predecessor in the generated track queue:** FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SAFE: Multitask Failure Detection for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the bottom during a policy rollout. We note ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is a stochastic predictor of a ... (p. 3, III. PROBLEM FORMULATION); preserve the objective/update rule: The first A' <H actions Ave, sje are executed, after which the robot re-plans by generating a new sequence of HY actions attime t+-11'. (p. 3, III. PROBLEM FORMULATION).
2. Use the paper-reported task/data/environment cue: significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts) (p. 7, V. EXPERIMENTS).
3. Compare against the reported or matched baseline: In comparison, the baselines STAC and PCA-kmeans reach top-1 performance in 3/16 and 0/16 cases, respectively. (p. 6, V. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: {ask as both FM and DP policies achieve 100% soces, 5 for Can, which hes the shortest ask completion time. (p. 5, V. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: {ask as both FM and DP policies achieve 100% soces, 5 for Can, which hes the shortest ask completion time. (p. 5, V. EXPERIMENTS); if none is reported, design one around: We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as possible. (p. 6, V. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), match the reported outcome at p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), and measure the boundary at p. 6 (V. EXPERIMENTS), p. 9 (C. Do failure detections align with human intuition?).

## Falsifiable research question

Under the paper's stated interface (Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, ...), does the paper-specific mechanism (A key novelty of our method is the ability to learn failure detection signals without access 10 failure data.) retain the reported evaluation outcome ({ask as both FM and DP policies achieve 100% soces, 5 for Can, which hes the shortest ask ...) when tested against the paper's strongest explicit boundary (We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric ({ask as both FM and DP policies achieve 100% soces, 5 for Can, which hes the shortest ask ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data. (p. 1, 1. INTRODUCTION).
- **Paper-supported outcome:** Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to compute the CP band: "setting-lependent" ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as possible. (p. 6, V. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
