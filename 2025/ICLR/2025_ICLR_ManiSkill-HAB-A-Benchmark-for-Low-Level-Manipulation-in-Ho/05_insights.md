# Insights — ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6bKEWevgSd; PDF retrieval source: https://arxiv.org/pdf/2412.13211. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Summary of Contributions: The contributions of MS-HAB are summarized as follows: 1) GPUaccelerated HAB implementation which supports realistic low-level control and achieves over 4300 SPS ...
- **p. 8 / 5 METHODOLOGY - extractive body cue:** (2016), then concatenated with state observations.
- **p. 8 / 5 METHODOLOGY - extractive body cue:** First, we define "events" which occur at any timestep t: 1) Contact: nonzero robot/target pairwise force, 2) Grasped: object not grasped at step t-1 and ...
- **p. 6 / 5 METHODOLOGY - extractive body cue:** Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the ...
- **p. 6 / 5 METHODOLOGY - extractive body cue:** 5.1 TRAINING REINFORCEMENT LEARNING POLICIES We choose Reinforcement Learning (RL) to learn our subtask policies as RL does not require prior demonstration data, and it ...
- **p. 7 / 5 METHODOLOGY - extractive body cue:** Visual observations are encoded by a NatureCNN (Mnih et al., 2015) and concatenated with state observations.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 8 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Using these events lists, we define mutually exclusive, collectively exhaustive success and failure modes.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, we provide trajectory categorization statistics for all baselines in Appendix A.6 so future work can gear its methodology to solve frequent failure modes discovered ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Each subtask also fails if the robot cumulative force reaches beyond a set threshold.
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** It is important to note that running the exact same episode in different simulators is exceedingly difficult since different simulation backends will result in interactions ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** However, their experiments suggest that concurrent rendering can negatively impact train performance (Szot et al., 2021), so we enable auto-sleep and disable concurrent rendering.
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive ...
- **p. 24 / A.6.2 DEFINITIONS - extractive body cue:** Eplace = () ∧eexcessive collisions̸ ∈Eplace viii Didn't reach goal failure: Agent grasps x, but cannot manipulate x to within 15cm of gpos. /Eplace/ > ...
- **Boundary to test:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive collision failure (F-Col), cannot grasp failure (F-Grasp), ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for efficient training, evaluation, and da ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the most direct way to improve overall task completion ... | p. 8 (6 RESULTS), p. 10 (6 RESULTS) |
| Failure/limitation | Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive collision failure (F-Col), cannot grasp failure (F-Grasp), ... | p. 10 (Figure/Table caption), p. 24 (A.6.2 DEFINITIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 We provide brief descriptions of the subtasks below: • Pick[a, optional](xpose): pick object x (from articulation a, if provided). • Place[a, optional](xpose , gpos): place object x in goal g (in articulation ...를 Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the robot under the cumulative collision force limit.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive collision failure (F-Col), cannot grasp failure (F-Grasp), ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for efficient training, evaluation, and da ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Benchmark, home rearrangement, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive collision failure (F-Col), cannot grasp failure (F-Grasp), ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 place_0 pick_1 place_1 pick_2 place_2 pick_3 place_3 pick_4 place_4 0 ....
3. Compare against the body-reported baseline or a matched simpler baseline: Second, TidyHouse and SetTable RL baselines have some gap between upper bound and real completion rate, indicating potential handoff issues or disturbance to prior target objects in success states..
4. Report the body metric and its denominator/aggregation: Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate is the most direct way to improve overall task completion ....
5. Re-run the body-reported ablation/failure condition: We remove all collision requirements, and allow placing on the full target receptacle surface..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 8 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 6 (5 METHODOLOGY); the primary result is directionally consistent at p. 8 (6 RESULTS), p. 10 (6 RESULTS), p. 19 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, MS-HAB1, holistic mechanism이 Second, TidyHouse and SetTable RL baselines have some gap between upper bound and real completion rate, ... 대비 Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and ...을 개선하고, Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
