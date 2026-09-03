# Insights — FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.03655; PDF retrieval source: https://arxiv.org/pdf/2105.03655. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We ...
- **p. 4 / 3 Method - extractive body cue:** To make these constraints linear and independent, we propose an alternative 4-scalar parameterization, which consists of pixel position of the point C ∈R2 at the ...
- **p. 2 / 1 Introduction - extractive body cue:** To achieve this goal, we present FlingBot, a self-supervised algorithm that learns how to unfold cloths from arbitrary initial configurations using a pick, stretch, and ...
- **p. 5 / 3 Method - extractive body cue:** To this end, we propose to use spatial action maps [5, 6, 7].
- **p. 6 / 3 Method - extractive body cue:** Our real-world experiment setup consists of two UR5s, where one is equipped with a Schunk WSG50 and the other with an OnRobot RG2, facing each ...
- **p. 5 / 3 Method - extractive body cue:** Our value network is a fully convolutional neural network with nine residual blocks [21] and two convolutional layers in the first and last layer, and ...
- **p. 5 / 3 Method - extractive body cue:** From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 4 (3 Method), p. 2 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method), p. 5 (3 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by the robot arm's ...
- **p. 1 / 1 Introduction - extractive body cue:** From goal-conditioned folding [2] to fabric smoothing [3, 4], prior works have achieved success using exclusively single-arm quasistatic interactions (e.g., pick & place) for cloth ...
- **p. 2 / 1 Introduction - extractive body cue:** Our approach is flexible to large cloths whose dimensions exceed the robot arm's reach ranges and generalizes to T-shirts despite being trained on rectangular cloths.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- ...
- **p. 9 / 4.4 Results - extractive body cue:** We discuss more of real world grasp failures in Sec.
- **p. 9 / 4.4 Results - extractive body cue:** The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below).
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed
- **Boundary to test:** Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- tion) to maximize coverage assuming a good ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We propose a parameterization for the dual-arm grasp ... | p. 2 (1 Introduction), p. 4 (3 Method) |
| Reported outcome | While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve a final coverage lower than FlingBot's. | p. 7 (4 Evaluation), p. 9 (4.4 Results) |
| Failure/limitation | Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- tion) to maximize coverage assuming a good ... | p. 13 (Figure/Table caption), p. 9 (4.4 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the corresponding batch of value maps c).를 At each time step, the policy predicts value maps from its visual observation and picks actions greedily with respect to its value maps.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- tion) to maximize coverage assuming a good ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We propose a parameterization for the dual-arm grasp ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, deformable object, cloth manipulation, dynamic manipulation, vision-based control`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- tion) to maximize coverage assuming a good ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below)..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to the quasi-static baselines, [FlingBot] increases the coverage by +52.0%, which is roughly twice that of the quasi-static baselines ( +27.1%, +24.8%, +23.1%)..
4. Report the body metric and its denominator/aggregation: The average grasp success rate is 78.0%, 45.0%, and 75.8% for normal rectangular, large rectangular, and shirts respectively..
5. Re-run the body-reported ablation/failure condition: Figure 2: Action Primitives. The dynamic Fling primitive starts with a two-arm grasp at the left L and right R grasp locations with center point C, followed by a fixed stretch, fling, ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method); the primary result is directionally consistent at p. 7 (4 Evaluation), p. 9 (4.4 Results), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, main, contribution mechanism이 Compared to the quasi-static baselines, [FlingBot] increases the coverage by +52.0%, which is roughly twice that ... 대비 The average grasp success rate is 78.0%, 45.0%, and 75.8% for normal rectangular, large rectangular, and shirts respectively.을 개선하고, Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
