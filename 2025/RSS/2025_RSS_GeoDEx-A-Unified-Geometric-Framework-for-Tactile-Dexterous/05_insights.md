# Insights — GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p057.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p057.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** We will end by describing the control architecture of our framework.
- **p. 3 / B. Force Estimation - extractive body cue:** Our projection allows changes to normal force magnitude and practically gives similar results as we will show in the experimental section,
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 5 / B. Force Estimation - extractive body cue:** We use MwoCo to simulate the arm, hand, and objects' kinematics, dynamics, and contact interactions.
- **Contribution anchor:** p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings)

### Strongest assumption and failure boundary

- **p. 1 / 1. Iyrropucrion - extractive body cue:** While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution ...
- **p. 1 / Abstract - extractive body cue:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise.
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Most Of the existing works focus on contact force and position planning and validate the method in simulation only [23, 25, 26], [27] performed hardware ...
- **p. 3 / B. Utilizing Tactile Readings - extractive body cue:** When extrinsic contacts are present, we can also assume there is a virtual sensor attached to the contact point that can measure force in the ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 10 / V. Discussion - extractive body cue:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.
- **p. 10 / V. Discussion - extractive body cue:** We can use this contact location, along with the object parameters to compute the ‘optimal force needed to grasp the object in force equilibrium, such ...
- **Boundary to test:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping and extrinsic ... | p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings) |
| Reported outcome | According to the results, we can see an improvement | p. 7 (B. Simulation Results), p. 8 (C. Hardware Results) |
| Failure/limitation | For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips. | p. 10 (V. Discussion), p. 10 (V. Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 The interaction between the fingertips and the objects is measured using the tactile fingertips which output normal forces at the contact location. ‘The hardware setup and experiment objects are shown in Fig.를 the finger-object contacts with consideration of sensor error; a force estimator that uses tactile sensor reading, the robot state and the object pose to estimates all contact forces that would achieve force ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping and extrinsic ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, force uncertainty, dexterous manipulation, extrinsic manipulation, geometric planning`.
- **Reading predecessor in the generated track queue:** PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The goal is for the objects to rotate about a pivot axis on the table, To this, using the distance between the pivot point and the contacts, the algorithm precomputes a trajectory ....
3. Compare against the body-reported baseline or a matched simpler baseline: We compared the controller when using the estimated force values against the raw measurements, with the results shown in Fig..
4. Report the body metric and its denominator/aggregation: ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it was successful and when it failed.
5. Re-run the body-reported ablation/failure condition: 1) without over-pressuring it (following constraint in eq..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 5 (B. Force Estimation); the primary result is directionally consistent at p. 7 (B. Simulation Results), p. 8 (C. Hardware Results), p. 8 (C. Hardware Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Through, various, experimental mechanism이 We compared the controller when using the estimated force values against the raw measurements, with the ... 대비 ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force ...을 개선하고, For these failure cases, the main element at fault was the saturation of the tactile sensors ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
