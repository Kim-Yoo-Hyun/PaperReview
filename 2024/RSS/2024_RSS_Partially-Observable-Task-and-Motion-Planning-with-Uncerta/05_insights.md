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

- **Paper-specific interface:** Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, the time horizons to perform meaningful tasks can ... (p. 3, III. BACKGROUND).
- **Paper-specific mechanism:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the construction of a non-deterministic Markov ... (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is We applied TAMPURA to five simulated and two realworld robotics problems, illustrated in Figure 2 and Figure 1, (p. 7, VI. SIMULATED EXPERIMENTS & ANALYSIS); the relevant task/metric cue is See the supplementary material for videos of successful completions under various initializations of these tasks. (p. 9, VII. REAL-WORLD IMPLEMENTATION). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 20:⃗ s ←[D[x] : x ∈zip(⃗Ψpre,⃗c,⃗Ψeff)] 21: ▷Compute f, num "failures" where c in Ψpre did not cause Ψeff. (p. 6, V. LEARNING THE SPARSE ABSTRACT MDP).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, TAMP, POMDP, uncertainty, risk-aware planning, closed-loop control`.
- **Reading predecessor in the generated track queue:** FOCI: Trajectory Optimization on Gaussian Splats (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite these novelties, TAMPURA, and TAMP in general, have several limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, the time horizons to perform meaningful tasks can ... (p. 3, III. BACKGROUND); preserve the objective/update rule: In this paper, we focus on planning problems with objectives modeled as goals in belief space (e.g., the goal may be to believe that with high probability the world is ... (p. 4, IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP).
2. Use the paper-reported task/data/environment cue: In this task, the robot is equipped with a single RGBD camera mounted to the gripper, and must find and pick up a small cube hidden in the environment. (p. 9, VII. REAL-WORLD IMPLEMENTATION).
3. Compare against the reported or matched baseline: The robot's task is to move these cubes into the bowl without colliding with a human's hand moving around in the workspace. (p. 9, VII. REAL-WORLD IMPLEMENTATION).
4. Report the body metric with its denominator and aggregation: See the supplementary material for videos of successful completions under various initializations of these tasks. (p. 9, VII. REAL-WORLD IMPLEMENTATION).
5. Re-run the reported ablation or stress/failure condition: The robot's task is to move these cubes into the bowl without colliding with a human's hand moving around in the workspace. (p. 9, VII. REAL-WORLD IMPLEMENTATION); if none is reported, design one around: 20:⃗ s ←[D[x] : x ∈zip(⃗Ψpre,⃗c,⃗Ψeff)] 21: ▷Compute f, num "failures" where c in Ψpre did not cause Ψeff. (p. 6, V. LEARNING THE SPARSE ABSTRACT MDP).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION), and measure the boundary at p. 6 (V. LEARNING THE SPARSE ABSTRACT MDP), p. 8 (C D).

## Falsifiable research question

Under the paper's stated interface (Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, ...), does the paper-specific mechanism (Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems ...) retain the reported evaluation outcome (See the supplementary material for videos of successful completions under various initializations of these tasks.) when tested against the paper's strongest explicit boundary (20:⃗ s ←[D[x] : x ∈zip(⃗Ψpre,⃗c,⃗Ψeff)] 21: ▷Compute f, num "failures" where c in Ψpre did not cause ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (See the supplementary material for videos of successful completions under various initializations of these tasks.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the construction of a non-deterministic Markov ... (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** We applied TAMPURA to five simulated and two realworld robotics problems, illustrated in Figure 2 and Figure 1, (p. 7, VI. SIMULATED EXPERIMENTS & ANALYSIS).
- **Strongest explicit boundary:** 20:⃗ s ←[D[x] : x ∈zip(⃗Ψpre,⃗c,⃗Ψeff)] 21: ▷Compute f, num "failures" where c in Ψpre did not cause Ψeff. (p. 6, V. LEARNING THE SPARSE ABSTRACT MDP).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
