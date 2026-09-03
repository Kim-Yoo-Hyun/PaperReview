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

- **Paper-specific interface:** The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that the input path be Fig. (p. 1, I. INTRODUCTION).
- **Paper-specific mechanism:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is This section presents experimental results for our implementation of CHOMP on Barrett Technology's WAM arm shown in figure 1. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM); the relevant task/metric cue is Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from collision. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still falls prey to local minima ... (p. 3, II. THE CHOMP ALGORITHM).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, motion planning, trajectory optimization, manipulation`.
- **Reading predecessor in the generated track queue:** Rapidly-Exploring Random Trees: A New Tool for Path Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a na¨ıve initial guess into a trajectory suitable ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that the input path be Fig. (p. 1, I. INTRODUCTION); preserve the objective/update rule: Setting the gradient of the right hand side of equation 3 to zero and solving for the minimizer results in the following more succinct update rule: ξk+1 = ξk -1 ... (p. 2, II. THE CHOMP ALGORITHM).
2. Use the paper-reported task/data/environment cue: Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from collision. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM).
3. Compare against the reported or matched baseline: However, we made little effort to make our code efficient; we stress that our algorithm is performing essentially the same amount of work as the smoother of a two stage ... (p. 6, III. EXPERIMENTS ON A ROBOTIC ARM).
4. Report the body metric with its denominator and aggregation: Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from collision. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM).
5. Re-run the reported ablation or stress/failure condition: Experimental results Our first experiment was designed to evaluate the efficacy of CHOMP and its probabilistic variants as a replacement for planning on a variety of everyday household manipulation problems. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM); if none is reported, design one around: However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still falls prey to local minima ... (p. 3, II. THE CHOMP ALGORITHM).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (Abstract), match the reported outcome at p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), and measure the boundary at p. 3 (II. THE CHOMP ALGORITHM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM).

## Falsifiable research question

Under the paper's stated interface (The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that ...), does the paper-specific mechanism (In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic ...) retain the reported evaluation outcome (Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how ...) when tested against the paper's strongest explicit boundary (However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** This section presents experimental results for our implementation of CHOMP on Barrett Technology's WAM arm shown in figure 1. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM).
- **Strongest explicit boundary:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still falls prey to local minima ... (p. 3, II. THE CHOMP ALGORITHM).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
