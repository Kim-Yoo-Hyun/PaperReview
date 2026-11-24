# Insights — Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html; PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도를 입력받아 모터 위치 목표를 낸다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...
- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **Contribution anchor:** p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In particular, an expressive RNN controller may learn to exploit details of the simulation dynamics that are maladaptive in the real world, leading to failure.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Memory-based controllers, such as recurrent neural networks (RNN), are a potentially powerful choice for solving highly dynamic nonlinear control problems due to their ability to ...
- **p. 6 / V. CONCLUSION - extractive body cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive body cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.
- **Boundary to test:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal robot, Cassie. RNNs trained without dynamics randomization ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 같은 입력·관절 제어에서 순환 기억의 역할을 비교한다. | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4) |
| Reported outcome | As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best. | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Failure/limitation | Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal robot, Cassie. RNNs trained without dynamics randomization ... | p. 1 (Figure/Table caption), p. 6 (V. CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- 정책 입력은 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도다. 순환 정책은 모터 위치 목표를 내고 PD 제어기가 토크를 계산한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- 같은 로봇·속도 지령에서 기억 구조와 학습 중 동역학 무작위화를 각각 바꿔 실물 전이의 차이를 확인할 수 있다. [PDF 6쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=6)
- 재현할 때 보행 위상과 관절 PD 목표의 기준 자세를 동일하게 둔다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, bipedal locomotion, recurrent policy, sim-to-real, online adaptation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal robot, Cassie. RNNs trained without dynamics randomization ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware..
3. Compare against the body-reported baseline or a matched simpler baseline: Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each with separate random seeds..
4. Report the body metric and its denominator/aggregation: Feedforward networks obtain a notably lower reward, with high variance..
5. Re-run the body-reported ablation/failure condition: Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal robot, Cassie. RNNs trained without dynamics randomization ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 1 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 State, Space, Action mechanism이 Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM ... 대비 Feedforward networks obtain a notably lower reward, with high variance.을 개선하고, Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
