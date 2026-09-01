# Insights — CHOMP: Gradient Optimization Techniques for Efficient Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ri.cmu.edu/publications/chomp-gradient-optimization-techniques-for-efficient-motion-planning/; PDF retrieval source: https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.
- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Given suitable finite differencing matrices Kd for d = 1, . . . , D, we can represent fprior as a sum of terms fprior(ξ) ...
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** As we show in the next section, we could also derive the objective over a prespecified discretization, but we find that the properties of the ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** We gain additional insight into the computational benefits of the covariant gradient based update by considering the analysis tools developed in the online learning/optimization literature, ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of an optimization problem ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 4 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Few current approaches to optimal control are equipped to handle obstacle avoidance, though.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many optimal controllers which do handle obstacles are framed in terms of mixed integer programming, which is known to be an NP-hard problem [24], [9], ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Intuitively, this heuristic suggests simply that the workspace gradients encountered after then first collision of a given configuration are invalid and should therefore be ignored.
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall into a suboptimal local minimum. from the ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory through ...
- **Boundary to test:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a na¨ıve initial guess into a trajectory suitable ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems. | p. 1 (I. INTRODUCTION), p. 1 (II. THE CHOMP ALGORITHM) |
| Reported outcome | Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of A improved performance by avoiding situations where preferring smooth trajectories ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Failure/limitation | Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a na¨ıve initial guess into a trajectory suitable ... | p. 1 (Figure/Table caption), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that the input path be Fig.를 Perhaps the most prevalent method of path optimization is the so-called "shortcut" heuristic, which picks pairs of configurations along the path and invokes a local planner to attempt to replace the intervening ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a na¨ıve initial guess into a trajectory suitable ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, motion planning, trajectory optimization, manipulation`.
- **Reading predecessor in the generated track queue:** Rapidly-Exploring Random Trees: A New Tool for Path Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a na¨ıve initial guess into a trajectory suitable ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We chose 15 different configurations in a given scene representing various tasks such as picking up an object 3The last degree of freedom simply rotates the hand in place..
3. Compare against the body-reported baseline or a matched simpler baseline: CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory through configuration space to its performance when initia ....
4. Report the body metric and its denominator/aggregation: Because the amount of rotation over a footstep is generally quite small (under 30◦), the error between the inner product on exponential map vectors and the true quaternion distance metric is negligible..
5. Re-run the body-reported ablation/failure condition: Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a na¨ıve initial guess into a trajectory suitable ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM); the primary result is directionally consistent at p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, Covariant, Hamiltonian mechanism이 CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance ... 대비 Because the amount of rotation over a footstep is generally quite small (under 30◦), the error between the ...을 개선하고, Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
