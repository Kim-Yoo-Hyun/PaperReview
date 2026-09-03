# Insights — STOMP: Stochastic Trajectory Optimization for Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980280; PDF retrieval source: https://whiteoak.umd.edu/roswiki/attachments/Papers%282f%29ICRA2011_Kalakrishnan/kalakrishnan_icra2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a new approach to motion planning that can deal with general constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach involves stochastic trajectory optimization using a series of noisy trajectories.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** This allows us to optimize arbitrary costs q(˜θ) for which derivatives are not available, or are non-differentiable or non-smooth.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We address the design of a cost function that allows planning for obstacle avoidance, optimization of task constraints, and minimization of joint torques.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** In order to keep the notation simple, we first derive the algorithm for a 1-dimensional trajectory; this naturally extends later to multiple dimensions.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 3) Torque costs: Given a suitable dynamics model of the robot, we can compute the feed-forward torque required at each joint to track the desired ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 2 (III. THE STOMP ALGORITHM)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** We present a new approach to motion planning using a stochastic trajectory optimization framework.
- **p. 1 / Abstract - extractive body cue:** The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** (c) Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of the gripper.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** STOMP produced a collision-free trajectory in all (a) (b) (c) Fig.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Success in this scenario implies the generation of a collision-free trajectory.
- **p. 3 / 5) Update θ ←θ + δθ - extractive body cue:** An additional advantage is that no gradient step-size parameter is required; the only open parameter in this algorithm is the magnitude of the exploration noise.
- **Boundary to test:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a torque-optimal fashion. to minimize collision costs using ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present a new approach to motion planning that can deal with general constraints. | p. 1 (I. INTRODUCTION), p. 2 (III. THE STOMP ALGORITHM) |
| Reported outcome | The execution times are comparable, even though CHOMP usually requires more iterations to achieve success. | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Failure/limitation | Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a torque-optimal fashion. to minimize collision costs using ... | p. 1 (Figure/Table caption), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we propose an estimated gradient formulated as follows: ...를 Domestic and retail scenarios, in particular, will have lots of cases where constraint satisfaction may be a prime goal, e.g. carrying a glass of water.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a torque-optimal fashion. to minimize collision costs using ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we present a new approach to motion planning that can deal with general constraints.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Robotics, motion planning, trajectory optimization, stochastic optimization`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a torque-optimal fashion. to minimize collision costs using ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We conduct experiments on a simulation of the Willow Garage PR2 robot in a simulated world, followed by a demonstration of performance on the real robot..
3. Compare against the body-reported baseline or a matched simpler baseline: (a) Plan obtained without torque minimization: arm is stretched..
4. Report the body metric and its denominator/aggregation: Success in this scenario implies the generation of a collision-free trajectory..
5. Re-run the body-reported ablation/failure condition: (a) Plan obtained without torque minimization: arm is stretched..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM); the primary result is directionally consistent at p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, motion, planning mechanism이 (a) Plan obtained without torque minimization: arm is stretched. 대비 Success in this scenario implies the generation of a collision-free trajectory.을 개선하고, Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
