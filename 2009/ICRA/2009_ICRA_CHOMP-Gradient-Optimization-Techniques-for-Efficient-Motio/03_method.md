# Method - CHOMP: Gradient Optimization Techniques for Efficient Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ri.cmu.edu/publications/chomp-gradient-optimization-techniques-for-efficient-motion-planning/; PDF retrieval source: https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 1 (II. THE CHOMP ALGORITHM), p. 4 (II. THE CHOMP ALGORITHM)): This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of an optimization problem [1] that attempts to maximize ...

## Method Body Digest

- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of an optimization problem ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still ...
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** For instance, the first term (d = 1) represents the total squared velocity along the trajectory.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** At iteration k, within a region of our current hypothesis ξk, we can approximate our objective using a first-order Taylor expansion: U(ξ) ≈U(ξk) + gT ...
- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** Such an objective will have no motivation to alter the velocity profile along the trajectory since such operations do not change the trajectory's length.
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** Defining an obstacle potential We will switch for a moment to discussing optimization of a continuous trajectory q(t) by defining our obstacle potential as a ...
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Setting the gradient of the right hand side of equation 3 to zero and solving for the minimizer results in the following more succinct update ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.
- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Given suitable finite differencing matrices Kd for d = 1, . . . , D, we can represent fprior as a sum of terms fprior(ξ) ...

## Source Evidence Cues

- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of an optimization problem ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still ...
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** For instance, the first term (d = 1) represents the total squared velocity along the trajectory.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** At iteration k, within a region of our current hypothesis ξk, we can approximate our objective using a first-order Taylor expansion: U(ξ) ≈U(ξk) + gT ...
- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** Such an objective will have no motivation to alter the velocity profile along the trajectory since such operations do not change the trajectory's length.
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** Defining an obstacle potential We will switch for a moment to discussing optimization of a continuous trajectory q(t) by defining our obstacle potential as a ...
- **Detected method headings:** II. THE CHOMP ALGORITHM (p. 1)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of ... | p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization ... | p. 3 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | For instance, the first term (d = 1) represents the total squared velocity along the trajectory. | p. 2 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Setting the gradient of the right hand side of equation 3 to zero and solving for the minimizer results in the following more succinct update ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of an optimization problem ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** The authors of [12] show how gradient-style updates can be understood as sequentially minimizing a local quadratic approximation to the objective function.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Understanding the update rule This update rule is a special case of a more general rule known as covariant gradient descent [2], [29], in which ...
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Penalties from the additional objective function terms are also multiplied through A-1 when applying the gradient, just as the workspace potential is.
- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 2 (II. THE CHOMP ALGORITHM), p. 1 (II. THE CHOMP ALGORITHM).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | shares, much, common, elastic, bands, planning, however, unlike, many, previous, path, optimization, techniques, drop | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | shares, much, common, elastic, bands, planning, however, unlike, many, previous | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | present, Covariant, Hamiltonian, Optimization, Motion, Planning, CHOMP, novel, generating, optimizing | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | Setting, gradient, right, hand, side, equation, zero, solving, minimizer, following | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that the input path ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Perhaps the most prevalent method of path optimization is the so-called "shortcut" heuristic, which picks pairs of configurations along the path and invokes a local ...
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Understanding the update rule This update rule is a special case of a more general rule known as covariant gradient descent [2], [29], in which ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** This variant is a Monte Carlo sampling technique that utilizes gradient information and energy conservation concepts to efficiently navigate equiprobability curves of an augmented state-space.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Unlike many of the other teams who seemed to focus on feedback control, operational control, and other reactive behaviors, our strategy has been to strongly ...
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** For instance, the first term (d = 1) represents the total squared velocity along the trajectory.
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** We start with a boolean-valued voxel representation of the environment, and compute the Euclidean Distance Transform (EDT) for both the voxel map and its logical ...
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | This indicator factor can be written mathematically as I(minj≤i d(xj(q)), although implementationally it is implemented simply by ignoring all terms after the ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | We discretize the trajectories at the LittleDog host computer control cycle frequency, which is 100 Hz. | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | We discretize the trajectories at the LittleDog host computer control cycle frequency, which is 100 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** normative, makes, easy, derive, CHOMP, update, rule, understand, equation, Lagrangian, form, optimization, problem, attempts, maximize, decrease, objective, function, subject, making.
- **Relevant PDF headings:** II. THE CHOMP ALGORITHM (p. 1).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | We chose 15 different configurations in a given scene representing various tasks such as picking up an object 3The last degree of ... | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Search / trajectory decision | CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Execution interface | Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Experimental results Our first experiment was designed to evaluate the efficacy of CHOMP and its probabilistic variants as a replacement for planning on a variety ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** However, we made little effort to make our code efficient; we stress that our algorithm is performing essentially the same amount of work as the ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall into a suboptimal local minimum. from the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Left: A simple two-dimensional trajectory traveling through an obstacle potential (with large potentials are in red and small potentials in blue). The gradient ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 1 (II. THE CHOMP ALGORITHM), p. 4 (II. THE CHOMP ALGORITHM), objective p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 1 (II. THE CHOMP ALGORITHM), temporal p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 6 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 6 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
