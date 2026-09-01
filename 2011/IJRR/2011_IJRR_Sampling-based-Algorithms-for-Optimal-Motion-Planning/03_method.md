# Method - Sampling-based Algorithms for Optimal Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (76 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1105.1186; PDF retrieval source: https://arxiv.org/pdf/1105.1186. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 2 (1 Introduction), p. 7 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): 1.3 Statement of Contributions To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties of the major paradigms for ...

## Method Body Digest

- **p. 4 / 1 Introduction - extractive PDF cue:** 1.3 Statement of Contributions To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Instead of using an explicit representation of the environment, samplingbased algorithms rely on a collision checking module, providing information about feasibility of candidate trajectories, and ...
- **p. 7 / 1 Introduction - extractive PDF cue:** On the application side, in recent years, random geometric graphs have attracted significant attention as models of ad hoc wireless networks (Gupta and Kumar, 1998, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The PRM algorithm and its variants are multiple-query methods that first construct a graph 2
- **p. 3 / 1 Introduction - extractive PDF cue:** (the roadmap), which represents a rich set of collision-free trajectories, and then answer queries by computing a shortest path that connects the initial state with ...
- **p. 4 / 1 Introduction - extractive PDF cue:** As a first set of results, it is proven that the standard PRM and RRT algorithms are not asymptotically optimal, and that the "simplified" PRM ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Then, the new proposed algorithms are presented and motivated.
- **p. 3 / 1 Introduction - extractive PDF cue:** For example, one may be interested in solution paths of minimum cost, with respect to a given cost functional, such as the length of a ...

## Design Rationale

- **p. 4 / 1 Introduction - extractive PDF cue:** As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the ...
- **p. 11 / 1 Introduction - extractive PDF cue:** In its basic version, it consists of a pre-processing phase, in which a roadmap is constructed by attempting connections among n randomly-sampled points in Xfree, ...
- **p. 13 / 1 Introduction - extractive PDF cue:** Algorithm 3: RRT 1 V ←{xinit}; E ←∅; 2 for i = 1, . . . , n do 3 xrand ←SampleFreei; 4 xnearest ←Nearest(G ...

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive PDF cue:** 1.3 Statement of Contributions To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Instead of using an explicit representation of the environment, samplingbased algorithms rely on a collision checking module, providing information about feasibility of candidate trajectories, and ...
- **p. 7 / 1 Introduction - extractive PDF cue:** On the application side, in recent years, random geometric graphs have attracted significant attention as models of ad hoc wireless networks (Gupta and Kumar, 1998, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The PRM algorithm and its variants are multiple-query methods that first construct a graph 2
- **p. 3 / 1 Introduction - extractive PDF cue:** (the roadmap), which represents a rich set of collision-free trajectories, and then answer queries by computing a shortest path that connects the initial state with ...
- **p. 4 / 1 Introduction - extractive PDF cue:** As a first set of results, it is proven that the standard PRM and RRT algorithms are not asymptotically optimal, and that the "simplified" PRM ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Then, the new proposed algorithms are presented and motivated.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | 1.3 Statement of Contributions To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality ... | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | Instead of using an explicit representation of the environment, samplingbased algorithms rely on a collision checking module, providing information about feasibility of ... | p. 2 (1 Introduction), p. 7 (1 Introduction) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | On the application side, in recent years, random geometric graphs have attracted significant attention as models of ad hoc wireless networks (Gupta ... | p. 7 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive PDF cue:** For example, one may be interested in solution paths of minimum cost, with respect to a given cost functional, such as the length of a ...
- **p. 6 / 1 Introduction - extractive PDF cue:** The cost function is assumed to be monotonic, in the sense that for all σ1, σ2 ∈Σ, c(σ1) ≤c(σ1/σ2), and bounded, in the sense that ...
- **p. 6 / 1 Introduction - extractive PDF cue:** Let c : Σ →R≥0 be a function, called the cost function, which assigns a strictly positive cost to all non-trivial collision-free paths (i.e., c(σ) ...
- **p. 7 / 1 Introduction - extractive PDF cue:** Problem 3 (Optimal path planning) Given a path planning problem (Xfree, xinit, Xgoal) and a cost function c : Σ →R≥0, find a feasible path ...
- **p. 1 / Abstract - extractive PDF cue:** The purpose of this paper is to fill this gap, by rigorously analyzing the asymptotic behavior of the cost of the solution returned by stochastic ...
- **p. 1 / Abstract - extractive PDF cue:** The main contribution of the paper is the introduction of new algorithms, namely, PRM∗and RRT∗, which are provably asymptotically optimal, i.e., such that the cost ...
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 7 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Informally, speaking, given, robot, description, dynamics, environment, initial, state, goal, states, motion, planning, problem | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | Informally, speaking, given, robot, description, dynamics, environment, initial, state, goal | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | early, seminal, papers, incremental, samplingbased, motion, planning, algorithms, Kuffner, LaValle | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | example, interested, solution, paths, minimum, cost, respect, given, functional, length | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive PDF cue:** Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set of goal states, ...
- **p. 11 / 1 Introduction - extractive PDF cue:** For convenience, inputs and outputs of the algorithms are not shown explicitly, but are as follows.
- **p. 13 / 1 Introduction - extractive PDF cue:** Input and output data are the same as in the algorithms introduced in Section 3.2.
- **p. 2 / 1 Introduction - extractive PDF cue:** Informally speaking, sampling-based methods provide large amounts of computational savings by avoiding explicit construction of obstacles in the state space, as opposed to most complete ...
- **p. 11 / 1 Introduction - extractive PDF cue:** All algorithms take as input a path planning problem (Xfree, xinit, Xgoal), an integer n ∈N, and a cost function c : Σ →R≥0, if ...
- **p. 13 / 1 Introduction - extractive PDF cue:** Algorithm 3: RRT 1 V ←{xinit}; E ←∅; 2 for i = 1, . . . , n do 3 xrand ←SampleFreei; 4 xnearest ←Nearest(G ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Even though the idea of connecting points sampled randomly from the state space is essential in both approaches, these two algorithms differ in the way ...
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | The RRT∗algorithm is a variant of RRG that incrementally builds a tree, providing anytime solutions, provably converging to an optimal solution, with ... | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 1 Introduction - extractive PDF cue:** In particular, they were extended to run in an anytime fashion (Likhachev et al., 2004, 2008), deal with dynamic environments (Stentz, 1995; Likhachev et al., ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Statement, Contributions, best, author, knowledge, provides, first, systematic, thorough, analysis, optimality, complexity, properties, major, paradigms, sampling-based, path, planning, algorithms, multiple-.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under ... | p. 31 (V RRT∗), p. 25 (V RRT∗) |
| Dynamics / constraint solve | Using these results, a thorough analysis of the computational complexity of the all the algorithms is given in terms of the number ... | p. 29 (V RRT∗), p. 32 (V RRT∗) |
| Feedback / actuation | An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves O(cd,ε log n) query time using O(d n) ... | p. 31 (V RRT∗), p. 33 (V RRT∗) |

## Failure and Ablation Link

- **p. 36 / Figure/Table caption - extractive PDF cue:** Figure 11: Cost of the best path in the PRM∗algorithm is shown in up to 2, 3, 4, and 5 dimensional configuration spaces, in Figures ...
- **p. 29 / V RRT∗ - extractive PDF cue:** Moreover, none of these vertices can be in the same connected component with Xn.
- **p. 35 / 6 Conclusion - extractive PDF cue:** In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, ...
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is shown ...
- **p. 29 / V RRT∗ - extractive PDF cue:** First, each algorithm is analyzed in terms of the number of calls to the CollisionFree procedure.
- **p. 29 / V RRT∗ - extractive PDF cue:** Number of calls to the CollisionFree procedure Let MALG n denote the total number of calls to the CollisionFree procedure by algorithm ALG in iteration ...
- **p. 30 / V RRT∗ - extractive PDF cue:** The next lemma upper-bounds the number of calls to the CollisionFree procedure in the proposed algorithms.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 Introduction), p. 2 (1 Introduction), p. 7 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), objective p. 3 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), temporal p. 31 (V RRT∗), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 9 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
