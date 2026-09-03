# Insights — Benchmarking Safe Exploration in Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openai.com/index/benchmarking-safe-exploration-in-deep-reinforcement-learning/; PDF retrieval source: https://cdn.openai.com/safexp-short.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- **p. 2 / 1 Introduction - extractive body cue:** Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating ...
- **p. 1 / Abstract - extractive body cue:** First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe ...
- **p. 1 / Abstract - extractive body cue:** Second, we present the Safety Gym benchmark suite, a new slate of high-dimensional continuous control environments for measuring research progress on constrained RL.
- **p. 2 / 1 Introduction - extractive body cue:** While "sim-to-real" transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building ...
- **p. 2 / 1 Introduction - extractive body cue:** We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction ...
- **p. 3 / 1 Introduction - extractive body cue:** Our baseline algorithms include Trust Region Policy Optimization (TRPO) [Schulman et al., 2015] and Proximal Policy Optimization (PPO) [Schulman et al., 2017] in their original ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** While RL is not yet fully mature or ready to serve as an "off-the-shelf" solution, it appears to offer a viable path to solving hard ...
- **p. 2 / 1 Introduction - extractive body cue:** However, there is not yet a standard set of environments for making progress on safe exploration specifically.2 Different papers use different environments and evaluation procedures, ...
- **p. 2 / 1 Introduction - extractive body cue:** There is a gradient of difficulty across benchmark environments.
- **p. 1 / 1 Introduction - extractive body cue:** However, for many problems simulators will either not be available or high-enough fidelity for RL to learn behaviors that succeed in the real environment.
- **p. 3 / 1 Introduction - extractive body cue:** Towards providing useful baselines: To make Safety Gym relevant out-of-the-box and to partially clarify state-of-the-art in safe exploration, we benchmark several existing constrained and unconstrained ...
- **p. 16 / 5 Experiments - extractive body cue:** [2017], we omit the learned failure predictor they used for cost shaping.
- **p. 21 / 5.3 Results - extractive body cue:** There are a number of avenues we consider promising for future work.
- **Boundary to test:** [2017], we omit the learned failure predictor they used for cost shaping.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | By success, we mean attaining improvements simultaneously along both the episodic return axis and the constraint regret axis, while still producing a constraint-satisfying policy at the conclusion of training. | p. 21 (5.3 Results), p. 14 (5 Experiments) |
| Failure/limitation | [2017], we omit the learned failure predictor they used for cost shaping. | p. 16 (5 Experiments), p. 21 (5.3 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 We recommend a protocol for evaluating constrained RL algorithms on Safety Gym environments based on three metrics: task performance of the final policy, constraint satisfaction of the final policy, and average regret ...를 While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating the complexities of the real world (such ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 [2017], we omit the learned failure predictor they used for cost shaping.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address the gap, we present Safety Gym: a set of tools for accelerating safe exploration research.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, safe reinforcement learning, Safety Gym, Benchmark, constraints`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** [2017], we omit the learned failure predictor they used for cost shaping.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: SG6 has at least one environment for each task, robot, and level..
3. Compare against the body-reported baseline or a matched simpler baseline: Advancing SOTA on Safety Gym: Our baseline results for constrained RL indicate a need for stronger and/or better-tuned algorithms to succeed on Safety Gym environments..
4. Report the body metric and its denominator/aggregation: We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero (or within noise of zero), and among approximately constraint-satisfying algorithms, one algorithm dominates an ....
5. Re-run the body-reported ablation/failure condition: These learning curves depict the metrics Jr(θ), Jc(θ), and ρc(θ) without normalization, and show the absolute performance of each algorithm..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction); the primary result is directionally consistent at p. 21 (5.3 Results), p. 14 (5 Experiments), p. 10 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, present, Safety mechanism이 Advancing SOTA on Safety Gym: Our baseline results for constrained RL indicate a need for stronger ... 대비 We compare normalized scores like we would compare individual training runs: the average constraint violation should be zero ...을 개선하고, [2017], we omit the learned failure predictor they used for cost shaping. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
