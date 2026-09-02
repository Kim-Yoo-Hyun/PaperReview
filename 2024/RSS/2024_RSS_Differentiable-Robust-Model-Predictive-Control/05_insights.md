# Insights — Differentiable Robust Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p003.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p003.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of ...
- **p. 1 / Abstract - extractive body cue:** Drawing parallels with differential dynamic programming, the IFT enables the derivation of an efficient differentiable optimal control framework.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This motivates the development of control algorithms that explicitly account for unknown disturbances in the dynamics and guarantee robustness.
- **p. 4 / II. MATHEMATICAL BACKGROUND - extractive body cue:** From the safe MPC via barrier methods perspective, the proposed work provides a novel expansion of the works [3], [14] and [19] to a tube-based ...
- **p. 5 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization of an appropriately ...
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** In order to optimize both the nominal and ancillary controller, we propose to use a loss function of the form L(τ ∗(θ), ¯τ(¯θ)) =
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 4 (II. MATHEMATICAL BACKGROUND), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when applied to autonomous systems acting in the real-world, deterministic MPC is often unable to respond to large disturbances that occur due to environmental ...
- **p. 2 / II. MATHEMATICAL BACKGROUND - extractive body cue:** However, in practice, the system under study is subject to large dynamical uncertainty through effects such as unmodeled physics, random noise, etc., that results in ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** A potential failure mode of nominal MPC when applied for the control of the true system is safety violations caused by this large predictive error ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** This approach is inherently robust to small uncertainty providing one explanation for the success of nominal MPC in practice, even when Problem 1 is not ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** The results in Table I show that, while NT-MPC fails to reach the target in the majority of the cases and occasionally violates the safety ...
- **Boundary to test:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number of failures even when controlled using NTMPC.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC in real-time, drastically increasing the success rate to ... | p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Failure/limitation | For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number of failures even when controlled using NTMPC. | p. 10 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 Safety is enforced through the use of discrete barrier states [3], which enables scalable constraint satisfaction such that safe planning and control can be executed in real-time.를 This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of the problem [43].로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number of failures even when controlled using NTMPC.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, MPC, robust control, differentiable optimization, uncertainty, Robotarium`.
- **Reading predecessor in the generated track queue:** Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number of failures even when controlled using NTMPC.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The generality of the proposed DT-MPC is established through benchmarks on five nonlinear robotics systems subject to highly non-convex constraints such as dense obstacle fields..
3. Compare against the body-reported baseline or a matched simpler baseline: 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]..
4. Report the body metric and its denominator/aggregation: On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC in real-time, drastically increasing the success rate to ....
5. Re-run the body-reported ablation/failure condition: In the experiments that follow, the nominal MPC is tuned to perform the task successfully and then the algorithms are deployed on the true system, without further tuning..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC); the primary result is directionally consistent at p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contribution, development mechanism이 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]. 대비 On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal ...을 개선하고, For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
