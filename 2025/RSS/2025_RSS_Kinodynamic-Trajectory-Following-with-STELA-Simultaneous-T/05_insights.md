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

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest robot pose incrementally.를 ‘An approach to deal with the model gap is to use feedback controllers for trajectory following, given the latest state estimate [12, 33].로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon of the planned trajectory. ‘The ‘combination of ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, trajectory following, state estimation, motion planning, online adaptation, mobile robot`.
- **Reading predecessor in the generated track queue:** FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying 9 and Xq. the approach ealls an asymptotically optimal kinodynamie ....
3. Compare against the body-reported baseline or a matched simpler baseline: The baseline comparison point is open-loop execution of the desired trajectory..
4. Report the body metric and its denominator/aggregation: Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is 100%). Trajectory ....
5. Re-run the body-reported ablation/failure condition: The ablation evaluation of the effect of the sliding window size, the use of the duration AT' as a factor variable, the impact of the obstacle factor, as well as the impact ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner); the primary result is directionally consistent at p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup), p. 11 (A. Experimemal setup); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 sliding, window, mechanism mechanism이 The baseline comparison point is open-loop execution of the desired trajectory. 대비 Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a ...을 개선하고, The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
