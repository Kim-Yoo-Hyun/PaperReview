# Problem - CHOMP: Gradient Optimization Techniques for Efficient Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ri.cmu.edu/publications/chomp-gradient-optimization-techniques-for-efficient-motion-planning/; PDF retrieval source: https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Few current approaches to optimal control are equipped to handle obstacle avoidance, though.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Existing high-dimensional motion planning algorithms are simultaneously overpowered and underpowered.
- **p. 1 / Abstract - extractive body cue:** In domains sparsely populated by obstacles, the heuristics used by sampling-based planners to navigate "narrow passages" can be needlessly complex; furthermore, additional post-processing is required ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present CHOMP, a novel method for continuous path refinement that uses covariant gradient techniques to improve the quality of sampled trajectories.
- **p. 1 / Abstract - extractive body cue:** Our optimization technique converges over a wider range of input paths and is able to optimize higherorder dynamics of trajectories than previous path optimization strategies.
- **p. 1 / Abstract - extractive body cue:** As a result, CHOMP can be used as a standalone motion planner in many real-world planning queries.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Few current approaches to optimal control are equipped to handle obstacle avoidance, though.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many optimal controllers which do handle obstacles are framed in terms of mixed integer programming, which is known to be an NP-hard problem [24], [9], ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Few current approaches to optimal control are equipped to handle obstacle avoidance, though. | graph, configuration space 또는 task-and-motion planning domain | body wording is the source claim |
| Observation / input | The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that ... | start/goal, map, dynamics와 successor/operator description | exact sensor/frame/preprocessing from PDF body |
| State / latent | shares, much, common, elastic, bands, planning, however, unlike, many, previous | path, trajectory, symbolic state 또는 task-motion decision | notation and tensor shape require body check |
| Output / action | Understanding, update, rule, special, case, more, general, known | feasible action sequence 또는 minimum-cost plan | exact unit/frame/decoder require body check |
| Target outcome | success/reachability and constraint satisfaction | path cost, goal reachability, feasibility와 computation | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | s/q; body terms: shares, much, common, elastic, bands, planning, however, unlike, many, previous | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. THE CHOMP ALGORITHM) |
| Decision / output variable | a/ξ ∈ feasible decisions; body terms: present, Covariant, Hamiltonian, Optimization, Motion, Planning, CHOMP, novel | p. 1 (I. INTRODUCTION), p. 1 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM) |
| Objective / loss / cost | path/task cost or expected utility; cue terms: Setting, gradient, right, hand, side, equation, zero, solving | p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 2 (II. THE CHOMP ALGORITHM), p. 1 (II. THE CHOMP ALGORITHM) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (II. THE CHOMP ALGORITHM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 1 (II. THE CHOMP ALGORITHM) |
| Success / guarantee | success/reachability and constraint satisfaction | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Many optimal controllers which do handle obstacles are framed in terms of mixed integer programming, which is known to be an NP-hard problem [24], [9], ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 4 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM)): In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.

- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Given suitable finite differencing matrices Kd for d = 1, . . . , D, we can represent fprior as a sum of terms fprior(ξ) ...
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** As we show in the next section, we could also derive the objective over a prespecified discretization, but we find that the properties of the ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** We gain additional insight into the computational benefits of the covariant gradient based update by considering the analysis tools developed in the online learning/optimization literature, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Intuitively, this heuristic suggests simply that the workspace gradients encountered after then first collision of a given configuration ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

planning writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), objective p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 2 (II. THE CHOMP ALGORITHM), p. 1 (II. THE CHOMP ALGORITHM).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Many optimal controllers which do handle obstacles are framed in terms of mixed integer programming, which is known to be an NP-hard problem [24], [9], [17], [27]. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still falls prey to local minima ... (p. 3, II. THE CHOMP ALGORITHM).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
