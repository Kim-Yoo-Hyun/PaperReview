# Insights — Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p125.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p125.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** First, we introduce the Un= supervised Actuator Net (UAN), which leverages real-world data {o bridge the sim-to-real gap for complex actuation mechanisms without requiring access ...
- **p. 2 / A. Unsupervised Actuator Net - extractive body cue:** Alternatively, we propose a method for matching the transition dynamics of the actuator such that
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Each training episode consists of a 20s rollout executing the torque sequence from the hardware data from 3, t0 8744.20 Through taining on rollouts, the ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's ...
- **p. 5 / A. Comparing System Identification Approaches - extractive body cue:** We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen ...
- **p. 3 / B. Whole-body Controller Pre-training - extractive body cue:** 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets ...
- **Contribution anchor:** p. 2 (1. Iyrropucrion), p. 1 (Body text (section not recovered)), p. 2 (A. Unsupervised Actuator Net), p. 3 (A. Unsupervised Actuator Net), p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches)

### Strongest assumption and failure boundary

- **p. 1 / Body text (section not recovered) - extractive body cue:** However, training solely with task rewards introduces two major challenges: these rewards are prone (o exploitation (reward hacking), and the exploration process can lack sufficient ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** However, these task rewards pose two major challenges: (i) they are prone 10 reward hacking, where the policy exploits imperfections in the simulation, and (i) ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Building on this enhanced simulation environment, we audress the challenge of guided exploration for athletic behaviors.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** The real-to-sim calibration phase involves collecting data on the real robot and training a UAN to close the sim-to-real gap for non-ideal actuation mechanisms.
- **p. 3 / A. Unsupervised Actuator Net - extractive body cue:** Our training pipeline involves three steps: 1) Train a UAN to close the sim-to-real gap for actuators with complex transmission mechanisms by mapping a history ...
- **p. 5 / A. Arm Modifications - extractive body cue:** During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5.
- **p. 6 / A. Comparing System Identification Approaches - extractive body cue:** Meanwhile, the Default, DR, and ROA policies produced unstable behaviors-the Default policy, for instance, strayed excessively and failed to throw the bull at all.
- **Boundary to test:** During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is frst pre-trained on random base velocities and ... | p. 2 (1. Iyrropucrion), p. 1 (Body text (section not recovered)) |
| Reported outcome | Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, resulting in a better real throw distance. For ... | p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches) |
| Failure/limitation | During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5. | p. 5 (A. Arm Modifications), p. 6 (A. Comparing System Identification Approaches) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 2) Observation Space: ‘The policy's observation space consists of proprioceptive readings from the robot's onboard sen= sors including the gravity vector projected in the robot's body frame g, a base velocity command ...를 1) Policy Architecture: "The WBC is a control policy, a, = ro(Or-yc4)e Where the action at time f, ay, is a vector of position targets for each ofthe robots joints and oy ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Rather than enforcing strict adherence to a reference trajectory, we propose treating it as a hint to guide exploration, In our approach, « WBC is frst pre-trained on random base velocities and ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, loco-manipulation, sim-to-real`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with minor deformations at Tink 5.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: On hardware, the ball was thrown approximately 20m, with the real robot throwing slightly further than in simulation - possibly due to inaccuracies in the ball-bucket contact modeling..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference in throw distance as compared to standard baselines, resulting in a better real throw distance. For ....
4. Report the body metric and its denominator/aggregation: We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both the training data and on an unseen test trajectory (see Figure 6) ur results ....
5. Re-run the body-reported ablation/failure condition: In this section, we report ablations that identify the contribution of key system components and present results for the athletic tasks..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (B. Whole-body Controller Pre-training), p. 5 (A. Comparing System Identification Approaches), p. 3 (B. Whole-body Controller Pre-training); the primary result is directionally consistent at p. 5 (Figure/Table caption), p. 5 (A. Comparing System Identification Approaches), p. 6 (B. Finetuning Foundational WBC); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Rather, enforcing, strict mechanism이 Fig. 4: UAN improves simulator accuracy and real throwing performance. UAN (Ours) achieves lower sim-to-real difference ... 대비 We first evaluate the modeling accuracy of these approaches by reporting the mean-square joint position error on both ...을 개선하고, During development, the Unitree ZI Pro arm experienced structural failures at inks 2 and 4, with ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
