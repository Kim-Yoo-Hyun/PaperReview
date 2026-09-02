# Insights — Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p118.html; PDF retrieval source: https://arxiv.org/pdf/2403.10454.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / III. BACKGROUND - extractive body cue:** To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended ...
- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that in tasks requiring risk sensitivity, information gathering, and robustness to uncertainty, TAMPURA significantly outperforms reinforcement learning, Monte Carlo tree search, and determinized ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Advances in techniques like behavior cloning (BC) [1, 2], reinforcement learning (RL) [3, 4], and model-based control [5, 6] have made it possible to develop ...
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** The first action recommended by this policy is the next controller to execute on the robot.
- **p. 4 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** 3: while abs(b) /∈G do 4: if abs(b) /∈Bsparse then 5: args ←(b0, G, O, s) 6: s, ˆT , Bsparse ←Model-Learning(args) 7: ▷Solve the ...
- **Contribution anchor:** p. 3 (III. BACKGROUND), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP)

### Strongest assumption and failure boundary

- **p. 3 / III. BACKGROUND - extractive body cue:** However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these methods typically do not generalize to solving arbitrary complex goals over long time horizons.
- **p. 3 / III. BACKGROUND - extractive body cue:** Fortunately, in cases where exact belief updates cannot be computed, it can suffice to compute approximate belief states using approximate Bayesian inference methods like particle ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This paper shows how to extend TAMP to settings with partial observability, uncertainty, and imperfect symbolic descriptions of controllers.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The resulting MDP is sparse enough that high-quality uncertainty-aware solvers like LAO* [10] can be applied.
- **p. 9 / VIII. DISCUSSION - extractive body cue:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.
- **p. 9 / VII. REAL-WORLD IMPLEMENTATION - extractive body cue:** The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), and (2) issues with tension in the ...
- **Boundary to test:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended time horizons. | p. 3 (III. BACKGROUND), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP) |
| Reported outcome | Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. Red intensity corresponds to p, the probability ... | p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Failure/limitation | Despite these novelties, TAMPURA, and TAMP in general, have several limitations. | p. 9 (VIII. DISCUSSION), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, the time horizons to perform meaningful tasks can be enormous, ...를 A POMDP is a tuple M = ⟨S, O, A, T , Z, r, b0, γ⟩.1 S, O, and A are the state, observation, and action spaces.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Despite these novelties, TAMPURA, and TAMP in general, have several limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended time horizons.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, TAMP, POMDP, uncertainty, risk-aware planning, closed-loop control`.
- **Reading predecessor in the generated track queue:** FOCI: Trajectory Optimization on Gaussian Splats (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Searching for Objects in Clutter This task is the real-world counterpart to the PARTIAL OBSERVABILITY simulated experiment..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. Red intensity corresponds to p, the probability ....
4. Report the body metric and its denominator/aggregation: Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from the blue cell to the green cell. Red intensity corresponds to p, the probability ....
5. Re-run the body-reported ablation/failure condition: The robot's task is to move these cubes into the bowl without colliding with a human's hand moving around in the workspace..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 9 (VII. REAL-WORLD IMPLEMENTATION); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 mitigate, introduce, concept mechanism이 Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must ... 대비 Fig. 4: Comparisons of model-learning strategies on a simplified grid-world environment in which an agent must navigate from ...을 개선하고, Despite these novelties, TAMPURA, and TAMP in general, have several limitations. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
