# Insights — A Realtime Pattern Generator for Biped Walking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2002.1013335; PDF retrieval source: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a robot with limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.
- **p. 3 / 1 Introduction - extractive body cue:** Since the 3DLIPM is a dynamics under the central force field, the motion along Y ′ and X′ is also governed by the identical equations ...
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, it mainly relies on the accuracy of the model data [3, 5, 10, 14].
- **p. 2 / 1 Introduction - extractive body cue:** (11) Therefore, we have the same dynamics of Eq.
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing ...
- **p. 4 / 1 Introduction - extractive body cue:** 3.2 Pattern generation along a local axis Now the problem becomes a control of the motion along X or Y -axis for each step.
- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...
- **Boundary to test:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint angles and it must avoid collision between ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal. | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | From the experimental results, the effectiveness of the proposed realtime walk generation method was confirmed. | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Failure/limitation | Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint angles and it must avoid collision between ... | p. 6 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).를 Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint angles and it must avoid collision between ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, bipedal locomotion, 3D linear inverted pendulum, real-time control`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint angles and it must avoid collision between ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for the experiments..
3. Compare against the body-reported baseline or a matched simpler baseline: baseline not recovered.
4. Report the body metric and its denominator/aggregation: In order to reduce the error between the desired ZMP trajectory and the actual ZMP, the horizontal position of the torso is adjusted..
5. Re-run the body-reported ablation/failure condition: Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint angles and it must avoid collision between ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction); the primary result is directionally consistent at p. 6 (4 Experiments), p. 6 (4 Experiments), p. 4 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 allows, separate, controller mechanism이 a matched simpler baseline 대비 In order to reduce the error between the desired ZMP trajectory and the actual ZMP, the horizontal position ...을 개선하고, Although we assume an ideal robot, which can step towards any direction at all time, in ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
