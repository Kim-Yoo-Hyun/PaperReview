# Insights — Control-Limited Differential Dynamic Programming

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2014.6907001; PDF retrieval source: https://roboti.us/lab/papers/TassaICRA14.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, Section IV describes the results, illustrating the usefulness of our approach.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show experimentally in simulation that simplistic ways of handling them are inefficient and detrimental to convergence.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Because the dynamics are folded into the optimization, state-control trajectories are always strictly feasible and "dynamic constraints" are unnecessary.
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** The dynamics is modeled by the generic function f xi+1 = f(xi,ui), (1) which describes the evolution from time i to i+1 of the state ...
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Na¨ıve Clamping A first attempt to enforce box constraints is to clamp the controls in the forward-pass.
- **p. 3 / C. Line Search - extractive body cue:** Once the backward pass is completed, the proposed locally-linear policy is evaluated with a forward pass: ˆx0 = x0 (7a) ˆui = ui + αki ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Ad-hoc task trajectories can be learned [9], which enlarge the convergence basin with a-priori knowledge and provide a consistent way to define complex task trajectories, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In that context the problem is transcribed into a generic sequential quadratic programming (SQP) which easily admits both equality and inequality constraints.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we consider the solution of controlconstrained problems using indirect methods.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We characterize the boxconstrained control problem in Section III, along with the proposed original solution.
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** As reported below, in our experiments the average number of factorizations was never larger than 2.
- **p. 4 / IV. RESULTS - extractive body cue:** We begin with an initial comparison of the three solution types on a set of simple linear systems randomly selected in Sec.
- **p. 4 / IV. RESULTS - extractive body cue:** We then compare the behavior of squashing and quadratic programming on a nonholonomic car problem in Sec.
- **Boundary to test:** As reported below, in our experiments the average number of factorizations was never larger than 2.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Finally, Section IV describes the results, illustrating the usefulness of our approach. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | However, despite some recent work in this direction [34], direct feed-forward current control is not yet a functional option, while the lack of joint torque sensor on most of hu0 50 100 ... | p. 6 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Failure/limitation | As reported below, in our experiments the average number of factorizations was never larger than 2. | p. 4 (III. CONTROL LIMITS), p. 4 (IV. RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Although indirect methods automatically take into account state constraints, control limits pose a difficulty. (p. 1, Abstract).
- **Paper-specific mechanism:** Finally, Section IV describes the results, illustrating the usefulness of our approach. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm. (p. 4, IV. RESULTS); the relevant task/metric cue is Distance was measured using the Hubertype function z(x,p) = √ x2 + p2-p. (p. 5, IV. RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** A running cost is added to penalize cartesian distance from the origin ℓ(x) = 0.01(z(x,px) + z(y,py)) This term encourages parking maneuvers which do not take the car far from ... (p. 5, IV. RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, optimal control, trajectory optimization, control limits`.
- **Reading predecessor in the generated track queue:** DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** In-Hand Manipulation via Motion Cones (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As reported below, in our experiments the average number of factorizations was never larger than 2.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Although indirect methods automatically take into account state constraints, control limits pose a difficulty. (p. 1, Abstract); preserve the objective/update rule: Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function. (p. 1, I. INTRODUCTION).
2. Use the paper-reported task/data/environment cue: Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2. (p. 4, IV. RESULTS).
3. Compare against the reported or matched baseline: The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm. (p. 4, IV. RESULTS).
4. Report the body metric with its denominator and aggregation: Distance was measured using the Hubertype function z(x,p) = √ x2 + p2-p. (p. 5, IV. RESULTS).
5. Re-run the reported ablation or stress/failure condition: 3 compares the results obtained with the two solvers. (p. 5, IV. RESULTS); if none is reported, design one around: A running cost is added to penalize cartesian distance from the origin ℓ(x) = 0.01(z(x,px) + z(y,py)) This term encourages parking maneuvers which do not take the car far from ... (p. 5, IV. RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS), and measure the boundary at p. 5 (IV. RESULTS), p. 6 (IV. RESULTS).

## Falsifiable research question

Under the paper's stated interface (Although indirect methods automatically take into account state constraints, control limits pose a difficulty.), does the paper-specific mechanism (Finally, Section IV describes the results, illustrating the usefulness of our approach.) retain the reported evaluation outcome (Distance was measured using the Hubertype function z(x,p) = √ x2 + p2-p.) when tested against the paper's strongest explicit boundary (A running cost is added to penalize cartesian distance from the origin ℓ(x) = 0.01(z(x,px) + z(y,py)) This ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Distance was measured using the Hubertype function z(x,p) = √ x2 + p2-p.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Finally, Section IV describes the results, illustrating the usefulness of our approach. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm. (p. 4, IV. RESULTS).
- **Strongest explicit boundary:** A running cost is added to penalize cartesian distance from the origin ℓ(x) = 0.01(z(x,px) + z(y,py)) This term encourages parking maneuvers which do not take the car far from ... (p. 5, IV. RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
