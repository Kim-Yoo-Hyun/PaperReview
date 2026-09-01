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

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 In the first stage, we extract scalar signals from policy inputs and/or outputs (e-g., robot states, visual features, generated future actions) that are discriminative between successes and failures during policy inference.를 Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is a stochastic predictor of a sequence of ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the bottom during a policy rollout. We note ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring`.
- **Reading predecessor in the generated track queue:** FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SAFE: Multitask Failure Detection for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the bottom during a policy rollout. We note ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts).
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to compute the CP band: "setting-lependent" using successful ....
4. Report the body metric and its denominator/aggregation: Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ‘and results on DP are in Fig. 12. ....
5. Re-run the body-reported ablation/failure condition: We did not employ the VLM component of the STAC failure detector to remain as real-time feasible as possible..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Aside, being, performant mechanism이 Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using ... 대비 Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR ...을 개선하고, Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
