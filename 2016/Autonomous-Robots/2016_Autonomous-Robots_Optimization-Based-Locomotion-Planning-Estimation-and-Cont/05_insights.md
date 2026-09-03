# Insights — Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/; PDF retrieval source: https://www.cs.cmu.edu/~cga/z/Kuindersma_AURO_2016.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain ...
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we describe our approach to addressing these problems with Atlas.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach to walking combines an efficient footstep planner with a simple dynamic model of the robot to efficiently compute desired walking trajectories.
- **p. 2 / 1 Introduction - extractive body cue:** We show that the robot is capable of walking over nontrivial terrain while maintaining extremely low drift from the desired footstep trajectory-a critically important capability ...
- **p. 2 / 1 Introduction - extractive body cue:** 6 we describe several experiments performed on the physical robot evaluatingthestateestimationandcontrolalgorithmsinpractice.We also describe recent simulation results of controlled highly dynamic motions that are currently being ...
- **p. 5 / 3.1.1 Convex decomposition - extractive body cue:** We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be represented as a ...
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** As will be discussed below, we use a redundant multiple-force description of the total wrench acting on a rigid body because it permits the use ...
- **Contribution anchor:** p. 4 (3.1 Footstep planning as a mixed-integer convex), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3.1.1 Convex decomposition)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment model to efficiently ...
- **p. 1 / 1 Introduction - extractive body cue:** As participants in the DARPA Robotics Challenge (DRC), we are particularly interested in tasks related to disaster relief, such as walking outdoors over irregular terrain ...
- **p. 2 / 1 Introduction - extractive body cue:** However, for complex humanoid systems like Atlas, solving trajectory optimization problems using the full dynamics can be computationally prohibitive.
- **p. 2 / 1 Introduction - extractive body cue:** Despite significant kinematic sensor limitations due to backlash and actuator deflection, our experiments demonstrate a measurable improvement in our ability to estimate the robot's state ...
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will hit a step edge and fall.
- **p. 22 / 6.4.1 Running - extractive body cue:** 13), require at least 3cm of clearance between links to avoid self-collisions, and constrain the gaze of the robot's head cameras to be no more ...
- **Boundary to test:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain consists of the top surface of every ... | p. 4 (3.1 Footstep planning as a mixed-integer convex), p. 1 (1 Introduction) |
| Reported outcome | To characterize the state estimator we evaluate its performance in a variety of experiments. | p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation) |
| Failure/limitation | The robot's trailing foot eventually collided with the front of the step resulting in a fall. | p. 20 (6.3 Closed-loop walking with LIDAR feedback), p. 20 (6.3 Closed-loop walking with LIDAR feedback) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Note that inputs computed by solving this QP are, in general, not equal to those computed by thresholding the output of the closed-form LQR policy.를 Given the current robot state, q, v, we can compute the equations of motion, H(q)˙v + C(q, v) = Bτ + JT λ, (25) H f Ha  ˙v + C f ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The robot's trailing foot eventually collided with the front of the step resulting in a fall.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain consists of the top surface of every ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, locomotion planning, optimization, state estimation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We describe several experiments performed on the robot and in simulation..
3. Compare against the body-reported baseline or a matched simpler baseline: baseline not recovered.
4. Report the body metric and its denominator/aggregation: Orientation estimation performance is comparable between different estimators.Notethattheprecisionofthegroundtruthorientation determined using VICON measurements is on the order of 1◦, so we were unable to differentiate yaw drift on a f ....
5. Re-run the body-reported ablation/failure condition: The robot's trailing foot eventually collided with the front of the step resulting in a fall..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.1.1 Convex decomposition), p. 8 (3.2 Dynamic motion planning), p. 11 (4.4 Additional costs and constraints); the primary result is directionally consistent at p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Unfortunately, safe, terrain mechanism이 a matched simpler baseline 대비 Orientation estimation performance is comparable between different estimators.Notethattheprecisionofthegroundtruthorientation determined using VICON measurements is on the order of 1◦, ...을 개선하고, The robot's trailing foot eventually collided with the front of the step resulting in a fall. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
