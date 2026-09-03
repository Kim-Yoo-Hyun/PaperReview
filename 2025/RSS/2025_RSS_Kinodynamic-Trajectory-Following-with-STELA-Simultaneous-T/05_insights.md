# Insights — Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p008.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p008.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1. INTRODUCTION - extractive body cue:** The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Proposed Method and Contribution: ‘The proposed 'STELA framework first calls an asymptotically optimal SEXP for kinodynamic systems (23, 27] in order to acquire a feasible, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** This allows the optimizer to stretch or contract edges depending oon the estimated state of the system.
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X ...
- **Contribution anchor:** p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner)

### Strongest assumption and failure boundary

- **p. 2 / 1. INTRODUCTION - extractive body cue:** They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions
- **p. 2 / 1. INTRODUCTION - extractive body cue:** While system identification [16, 3, 44] can reduce the model gap. it does not fully address it.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** challenge convergence and may require careful definition of parameters, such as obstacle potentials [36].
- **p. 3 / 1. INTRODUCTION - extractive body cue:** An interleaving approach uses a graph to generate suggestions used by an optimizer [31] ‘Simultaneous localization and planning (SLAP) [1] models the challenge as a ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** Due to the gap between the true dynamics J and the planning model ,, the executed robot trajectory 77(rj,pr) does not match the planned trajectory ...
- **p. 12 / A. Experimemal setup - extractive body cue:** The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.
- **p. 12 / A. Experimemal setup - extractive body cue:** The second environment considers a set of movable boxes that are not present during planning, and the robot ‘can collide online without considering a failure, ...
- **Boundary to test:** The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon of the planned trajectory. ‘The ‘combination of ... | p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| Reported outcome | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is 100%). Trajectory ... | p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup) |
| Failure/limitation | The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures. | p. 12 (A. Experimemal setup), p. 12 (A. Experimemal setup) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest robot pose incrementally. (p. 2, 1. INTRODUCTION).
- **Paper-specific mechanism:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without collisions. (p. 3, 1. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is ... (p. 11, Figure/Table caption); the relevant task/metric cue is Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is ... (p. 11, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The extreme noise level oj results mostly in failures, where 24% of failures arise from Indeterminant Linear System Exception, i. the accumulation of numerical errors, which does not occur for ... (p. 12, A. Experimemal setup).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, trajectory following, state estimation, motion planning, online adaptation, mobile robot`.
- **Reading predecessor in the generated track queue:** FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest robot pose incrementally. (p. 2, 1. INTRODUCTION); preserve the objective/update rule: Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X : Xp), a state prio ... (p. 5, B. Trajectory Optimization as a Motion Planner).
2. Use the paper-reported task/data/environment cue: Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying 9 and Xq. the approach ealls an asymptotically ... (p. 5, V. SIMULTANEOUS TRAIECTORY ESTIMATION).
3. Compare against the reported or matched baseline: The baseline comparison point is open-loop execution of the desired trajectory. (p. 10, A. Experimemal setup).
4. Report the body metric with its denominator and aggregation: Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is ... (p. 11, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: The ablation evaluation of the effect of the sliding window size, the use of the duration AT' as a factor variable, the impact of the obstacle factor, as well as ... (p. 12, A. Experimemal setup); if none is reported, design one around: The extreme noise level oj results mostly in failures, where 24% of failures arise from Indeterminant Linear System Exception, i. the accumulation of numerical errors, which does not occur for ... (p. 12, A. Experimemal setup).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), match the reported outcome at p. 11 (Figure/Table caption), p. 11 (A. Experimemal setup), p. 9 (Figure/Table caption), and measure the boundary at p. 12 (A. Experimemal setup), p. 12 (A. Experimemal setup).

## Falsifiable research question

Under the paper's stated interface (However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest ...), does the paper-specific mechanism (Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired ...) retain the reported evaluation outcome (Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a ...) when tested against the paper's strongest explicit boundary (The extreme noise level oj results mostly in failures, where 24% of failures arise from Indeterminant Linear System ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without collisions. (p. 3, 1. INTRODUCTION).
- **Paper-supported outcome:** Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is ... (p. 11, Figure/Table caption).
- **Strongest explicit boundary:** The extreme noise level oj results mostly in failures, where 24% of failures arise from Indeterminant Linear System Exception, i. the accumulation of numerical errors, which does not occur for ... (p. 12, A. Experimemal setup).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
