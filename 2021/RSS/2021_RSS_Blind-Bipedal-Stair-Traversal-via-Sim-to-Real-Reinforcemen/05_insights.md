# Insights — Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss17/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss17/p061.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These policies learn proprioceptive reflexes to reject significant disturbances in ground height, resulting in highly robust behavior to many realworld environments. start location or the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Learning on this distribution allows for blind locomotion up and down unknown stairs as well as handling more general stair-like terrain characteristics, e.g. logs, curbs, ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Intuitively, this allows the controller to choose an appropriate stepping frequency for a particular gait, command, and terrain.
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Training is done completely in a simulation environment, with dynamics randomization (see below), and the resulting policy is then used in the realworld.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** On stair-like environments, this is especially apparent due to the difficulty of recovery from missteps with only two legs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, integrating a state-ofthe-art computer vision system into a high-speed controller is technically difficult, especially on a computationally limited platform like a mobile robot.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the limits of this approach are unclear and prior work has not been demonstrated on the scale and variety of disturbances involved in stair-like ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...
- **p. 7 / V. CONCLUSION - extractive body cue:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training pipeline which produces policies capable of blindly ...
- **Boundary to test:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind bipedal robot.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs of typical dimensions found in human environments. ... | p. 4 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Failure/limitation | In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind bipedal robot. | p. 7 (V. CONCLUSION), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 State Space The state st that is input to the control policy at each time step includes three main components.를 In the general RL setting, at each discrete time step t the robot control policy π receives the current state st and returns an action at, which is applied and results in ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind bipedal robot.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, bipedal locomotion, Reinforcement Learning, sim-to-real, proprioception`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind bipedal robot.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22]..
3. Compare against the body-reported baseline or a matched simpler baseline: We also trained a group of policies without stair terrain randomization, and denote these Flat Ground LSTM, to investigate the importance of the terrain randomization introduced in this work..
4. Report the body metric and its denominator/aggregation: Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend and descend stairs of typical dimensions found in human environments. ....
5. Re-run the body-reported ablation/failure condition: Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 m/s over 150 trials. For Stair LSTM ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION); the primary result is directionally consistent at p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, training, pipeline mechanism이 We also trained a group of policies without stair terrain randomization, and denote these Flat Ground ... 대비 Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, ...을 개선하고, In future work, it will be interesting to investigate how vision can be most effectively used ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
