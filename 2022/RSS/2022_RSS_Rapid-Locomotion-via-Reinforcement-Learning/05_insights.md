# Insights — Rapid Locomotion via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss18/p022.html; PDF retrieval source: https://arxiv.org/pdf/2205.02824. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter sprint ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The same policy can spin the robot at 5.7 rad/s on flat ground and also enables the robot to spin on the more challenging icy ...
- **p. 3 / III. METHOD - extractive body cue:** Teacher-student training enables the agent to specialize its behavior to the current dynamics dt, instead of learning a single behavior that works across different dt.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that reinforcement learning can be used to learn locomotion controllers that simultaneously achieve linear and angular high-speed behaviors and operate on diverse natural ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One possibility is to resolve these issues by making targeted improvements to the hand-designed models used in modelbased control.
- **p. 2 / III. METHOD - extractive body cue:** As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ...
- **p. 3 / III. METHOD - extractive body cue:** (hθa) x[t-h:t-1] (42 × 15) [256, 32] zt (8) Body (πθb) xt (42), zt (8) [512, 256, 128] at (12) TABLE II: Network architecture for ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Task difficulty is a function of both the system dynamics and the optimization algorithm, making manual curriculum design tedious and problem-dependent.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, increasing the range of commanded velocities to include high speeds results in training failure.
- **p. 1 / I. INTRODUCTION - extractive body cue:** How can we perform real-time control in complex environments where efficient reduced-order models may not exist or are currently unknown?
- **p. 1 / I. INTRODUCTION - extractive body cue:** The problem is that trajectory optimization with a full model is not possible in real-time for a complex task such as fast running on natural ...
- **p. 8 / VI. DISCUSSION - extractive body cue:** Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or ...
- **p. 8 / VI. DISCUSSION - extractive body cue:** We cannot use motion capture to record the robot's state outdoors as we do in the lab.
- **p. 7 / IV. RESULTS - extractive body cue:** Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline made ...
- **Boundary to test:** Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or avoiding pitfalls.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter sprint at 3.4 m/s; (c) high-speed spinning indoors; ... | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | The performance of the system is improved substantially by implementing the Box Curriculum. | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Failure/limitation | Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or avoiding pitfalls. | p. 8 (VI. DISCUSSION), p. 8 (VI. DISCUSSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 Our goal is to learn a policy πθ(.) with parameters θ that takes as input sensory data and velocity commands and gives as output joint position commands (see Figure 2), which are ...를 As detailed in Section III-C, the policy πθ(·) takes as input a history of previous observations and actions denoted by ot-H:t where ot = [qt, ˙qt, gori t , at-1].로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or avoiding pitfalls.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter sprint at 3.4 m/s; (c) high-speed spinning indoors; ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, Reinforcement Learning, high-speed locomotion`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or avoiding pitfalls.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length..
3. Compare against the body-reported baseline or a matched simpler baseline: Unlike our learned controller, the baseline did not recover from (1) slipping down the gravelly incline and (4) tripping over the barrier..
4. Report the body metric and its denominator/aggregation: Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum for all error thresholds. (b) Velocity tracking error ....
5. Re-run the body-reported ablation/failure condition: We observe that the policy trained without any curriculum fails to learn..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD); the primary result is directionally consistent at p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 end-to-end, learned, controller mechanism이 Unlike our learned controller, the baseline did not recover from (1) slipping down the gravelly incline ... 대비 Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of ...을 개선하고, Our system also does not use vision, so in general, it cannot perform tasks that require ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
