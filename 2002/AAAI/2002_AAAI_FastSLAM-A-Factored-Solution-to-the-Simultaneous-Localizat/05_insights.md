# Insights — FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/~thrun/papers/montemerlo.fastslam-tr.html; PDF retrieval source: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / Abstract - extractive body cue:** We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to ...
- **p. 4 / Abstract - extractive body cue:** Our approach makes it possible to execute a FastSLAM iteration in O(M log K) time.
- **p. 1 / Abstract - extractive body cue:** This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps.
- **p. 2 / Abstract - extractive body cue:** We develop a tree-based data structure that reduces the running time of FastSLAM to O(M log K), making it significantly faster than existing EKF-based SLAM ...
- **p. 3 / Abstract - extractive body cue:** This will allows us to silently "forget" all other pose estimates, rendering the size of each particle independent of the time index t.
- **p. 3 / Abstract - extractive body cue:** First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ∼ p(st / ...
- **p. 1 / Abstract - extractive body cue:** Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM.
- **Contribution anchor:** p. 2 (Abstract), p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 3 (Abstract)

### Strongest assumption and failure boundary

- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 1 / Abstract - extractive body cue:** A key limitation of EKF-based approaches is their computational complexity.
- **p. 1 / Abstract - extractive body cue:** The resulting algorithm is an instance of the Rao-Blackwellized particle filter [5, 14].
- **p. 2 / Abstract - extractive body cue:** We are now ready to formulate the SLAM problem.
- **p. 2 / Abstract - extractive body cue:** In mobile robotics, the motion model is usually a time-invariant probabilistic generalization of robot kinematics [1].
- **p. 5 / Abstract - extractive body cue:** Unfortunately, the physical testbed does not allow for systematic experiments regarding the scaling properties of the approach.
- **p. 2 / Abstract - extractive body cue:** Many measurement models in the literature assume that the robot can measure range and bearing to landmarks, confounded by measurement noise.
- **Boundary to test:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to the full range of SLAM problems discussed ... | p. 2 (Abstract), p. 4 (Abstract) |
| Reported outcome | Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. Large number of landmarks reduce the robot localization ... | p. 6 (Figure/Table caption), p. 2 (Abstract) |
| Failure/limitation | Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above. | p. 4 (Abstract), p. 5 (Abstract) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation.를 Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to the full range of SLAM problems discussed ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Robotics, SLAM, particle filter, state estimation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: To map its environment, the robot can sense landmarks..
3. Compare against the body-reported baseline or a matched simpler baseline: FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map..
4. Report the body metric and its denominator/aggregation: Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. Large number of landmarks reduce the robot localization ....
5. Re-run the body-reported ablation/failure condition: In mobile robotics, the motion model is usually a time-invariant probabilistic generalization of robot kinematics [1]..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (Abstract), p. 1 (Abstract), p. 1 (Abstract); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 2 (Abstract), p. 5 (Abstract); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 extend, FastSLAM, algorithm mechanism이 FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually ... 대비 Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and ...을 개선하고, Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
