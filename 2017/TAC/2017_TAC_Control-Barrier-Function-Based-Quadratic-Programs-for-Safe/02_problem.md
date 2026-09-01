# Problem - Control Barrier Function Based Quadratic Programs for Safety Critical Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1609.06408; PDF retrieval source: https://arxiv.org/pdf/1609.06408. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 11 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS)): One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly designing controllers.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints.
- **p. 1 / Abstract - extractive body cue:** As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a ...
- **p. 1 / Abstract - extractive body cue:** Safety conditions are specified in terms of forward invariance of a set, and are verified via two novel generalizations of barrier functions; in each case, ...
- **p. 1 / Abstract - extractive body cue:** In addition, each of these formulations yields a notion of control barrier function (CBF), providing inequality constraints in the control input that, when satisfied, again ...
- **p. 1 / Abstract - extractive body cue:** Through these constructions, CBFs can naturally be unified with control Lyapunov functions (CLFs) in the context of a quadratic program (QP); this allows for the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly designing controllers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by the use of Lyapunov functions to certify stability properties of a set without calculating the exact solution of a system, the underlying concept ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | (43) Here, x = (x1, x2, x3) := (vf, vl, D) where vf and vl are the velocity of the following and ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | Here, where, velocity, following, leading, vehicle, respectively, distance, between, vehicles | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Initially, will, suppose, control, input, unbounded, later, address | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: Here, where, velocity, following, leading, vehicle, respectively, distance, between, vehicles | p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Importantly, under, mild, conditions, demonstrated, necessary, sufficient, forward | p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: Safety, critical, systems, involve, tight, coupling, between, potentially | p. 1 (Abstract), p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), p. 3 (B. Contributions), p. 7 (III. CONTROL BARRIER FUNCTIONS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (I. INTRODUCTION), p. 3 (B. Contributions), p. 7 (III. CONTROL BARRIER FUNCTIONS) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 14 (0.1 N), p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by the use of Lyapunov functions to certify stability properties of a set without calculating the exact solution of a system, the underlying concept ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In the case of reciprocal barrier functions, existing formulations impose invariant level sets of B [5], via, ˙B ≤0, as was done in earlier work ...
- **p. 10 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** 10 1) ACC problem setup: We begin by setting up the dynamics of the problem based upon [34] and [36], which assume that the lead ...
- **p. 11 / V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS - extractive body cue:** Simulation results of the ACC problem based on (ACC QP) (left) speed of the lead car and the controlled car with the desired speed vd ...

## What the Paper Changes

PDF contribution framing (p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (C. Organization and Notation)): Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in the relationships shown in Fig.

- **p. 2 / B. Contributions - extractive body cue:** The first contribution of this paper is to formulate conditions on the derivative of a (reciprocal or zeroing) barrier function that are minimally restrictive on ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, barrier functions were used in the paper [4] to develop an interior penalty method for converting constrained optimal control methods into unconstrained ones1.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, the approach developed here will pose a feedback design problem that mediates the safety and stabilization requirements, in the sense that safety is ...
- **p. 3 / C. Organization and Notation - extractive body cue:** The theory developed in the paper is illustrated on the adaptive cruise control and lane keeping problems in Sect.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | Future work will be devoted to building upon the foundations presented in this paper in the context of ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 2 (B. Contributions). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 11 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), interface p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 2 (B. Contributions), objective p. 1 (Abstract), p. 2 (B. Contributions), p. 2 (B. Contributions), p. 1 (I. INTRODUCTION), p. 3 (B. Contributions), p. 7 (III. CONTROL BARRIER FUNCTIONS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
