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

- **Closed-loop position:** `joint/task state, reference와 sensor feedback → state estimate, task-space error와 control decision → torque, force, velocity 또는 position command`.
- 이 논문의 재사용 가능한 지점은 (5a) This is a locally-linear feedback policy with k ≜-Q-1 uuQu and K ≜-Q-1 uuQux (5b) the feed-forward modification and feedback gain matrix, respectively.를 Although indirect methods automatically take into account state constraints, control limits pose a difficulty.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 state estimate, task-space error와 control decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 As reported below, in our experiments the average number of factorizations was never larger than 2.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Finally, Section IV describes the results, illustrating the usefulness of our approach.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, optimal control, trajectory optimization, control limits`.
- **Reading predecessor in the generated track queue:** DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** In-Hand Manipulation via Motion Cones (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As reported below, in our experiments the average number of factorizations was never larger than 2.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2..
3. Compare against the body-reported baseline or a matched simpler baseline: The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm..
4. Report the body metric and its denominator/aggregation: We generated random LQ problems as follows..
5. Re-run the body-reported ablation/failure condition: ablation/failure condition not recovered.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING); the primary result is directionally consistent at p. 6 (IV. RESULTS), p. 5 (IV. RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Finally, Section, describes mechanism이 The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and ... 대비 We generated random LQ problems as follows.을 개선하고, the paper's strongest untested assumption 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
