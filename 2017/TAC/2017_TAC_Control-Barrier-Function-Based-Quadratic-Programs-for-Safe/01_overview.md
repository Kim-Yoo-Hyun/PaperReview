# Control Barrier Function Based Quadratic Programs for Safety Critical Systems

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1609.06408.
> PDF retrieval source: https://arxiv.org/pdf/1609.06408. Reading tracker status/evidence was not changed.

- Year/Venue: 2017 / TAC
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: CORE
- Tags: Robotics, control barrier function, safety-critical control, quadratic programming
- Official paper: https://arxiv.org/abs/1609.06408
- Full-text retrieval: https://arxiv.org/pdf/1609.06408
- Code/Project: https://coogan.ece.gatech.edu/papers/pdf/ames2017control.pdf
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly designing controllers.를 문제로 두고, Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in the relationships shown in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints.
- **p. 1 / Abstract - extractive body cue:** As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a ...
- **p. 1 / Abstract - extractive body cue:** Safety conditions are specified in terms of forward invariance of a set, and are verified via two novel generalizations of barrier functions; in each case, ...
- **p. 1 / Abstract - extractive body cue:** In addition, each of these formulations yields a notion of control barrier function (CBF), providing inequality constraints in the control input that, when satisfied, again ...
- **p. 1 / Abstract - extractive body cue:** Through these constructions, CBFs can naturally be unified with control Lyapunov functions (CLFs) in the context of a quadratic program (QP); this allows for the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly designing controllers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by the use of Lyapunov functions to certify stability properties of a set without calculating the exact solution of a system, the underlying concept ...

## Core Idea

- **p. 2 / B. Contributions - extractive body cue:** Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in ...
- **p. 2 / B. Contributions - extractive body cue:** The first contribution of this paper is to formulate conditions on the derivative of a (reciprocal or zeroing) barrier function that are minimally restrictive on ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, barrier functions were used in the paper [4] to develop an interior penalty method for converting constrained optimal control methods into unconstrained ones1.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, the approach developed here will pose a feedback design problem that mediates the safety and stabilization requirements, in the sense that safety is ...
- **p. 3 / C. Organization and Notation - extractive body cue:** The theory developed in the paper is illustrated on the adaptive cruise control and lane keeping problems in Sect.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While it is tempting to decompose the problem into the design of a controller for each individual objective and then integrate the resulting controllers via ...
- **p. 2 / B. Contributions - extractive body cue:** The relations established for barrier functions then extend to control barrier functions. perspective allows for the consideration of multiple control objectives (expressed via multiple CLFs) ...
- **p. 1 / Abstract - extractive body cue:** As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (43) Here, x = (x1, x2, x3) := (vf, vl, D) where vf and vl are the velocity of the following and leading vehicle (in m/s), respectively, D is the distance between ... | observation, uncertainty/risk estimate와 task command | p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS) |
| State/latent | Here, where, velocity, following, leading, vehicle, respectively, distance, between, vehicles, mass, f1vf | safe set, recovery state 또는 constraint margin | p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS) |
| Output/action | The model parameters a, b, Cr, Iz and v0 are all positive, and hence the system is exponentially stable, and therefore input-to-state stable [41]. | shielded, recovery 또는 safe action | p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 2 (B. Contributions) |
| Objective/outcome | Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints. | task return과 violation/failure probability | p. 1 (Abstract), p. 2 (B. Contributions), p. 2 (B. Contributions) |

## Main Claims and Actual Contribution

- **p. 2 / B. Contributions - extractive body cue:** Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in ...
- **p. 2 / B. Contributions - extractive body cue:** The first contribution of this paper is to formulate conditions on the derivative of a (reciprocal or zeroing) barrier function that are minimally restrictive on ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, barrier functions were used in the paper [4] to develop an interior penalty method for converting constrained optimal control methods into unconstrained ones1.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, the approach developed here will pose a feedback design problem that mediates the safety and stabilization requirements, in the sense that safety is ...
- **p. 3 / C. Organization and Notation - extractive body cue:** The theory developed in the paper is illustrated on the adaptive cruise control and lane keeping problems in Sect.
- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** A video of the results is available on YouTube [57].
- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** Simulation results for ACC Various problem formulations are compared here.
- **p. 14 / 0.1 N - extractive body cue:** Simulation results for lane keeping are shown in Fig.6.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Embodiment/environment | The parameters used for the simulation are given in Table I. | hardware/simulator version and reset protocol | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Dataset/benchmark | 14 ZCBFs generate a smoother input trajectory (see Fig. | role, split, size and leakage | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (VI. SIMULATION RESULTS), p. 14 (0.1 N) |
| Metric | The feedforward term xff = [0, 0, 0, rd]⊤reduces tracking error. | definition, denominator, direction and uncertainty | p. 14 (0.1 N), p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Baseline/ablation | Simulation results for ACC Various problem formulations are compared here. | fair input/data/compute/action matching | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (VI. SIMULATION RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 14 / VII. CONCLUSIONS - extractive body cue:** Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 One of the difficulties in designing cyber-physical systems is the need to meet a large and diverse set of objectives by properly designing controllers.를 문제로 두고, Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result in the relationships shown in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 11 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 1 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
