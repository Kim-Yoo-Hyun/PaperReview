# Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1712.02889.
> PDF retrieval source: https://arxiv.org/pdf/1712.02889. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, whole-body control, model predictive control, quadruped
- Official paper: https://arxiv.org/abs/1712.02889
- Full-text retrieval: https://arxiv.org/pdf/1712.02889
- Code/Project: https://github.com/ethz-adrl/towr
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness of the plans.를 문제로 두고, In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this work we present a whole-body Nonlinear Model Predictive Control approach for Rigid Body Systems subject to contacts.
- **p. 1 / Abstract - extractive body cue:** We use a full dynamic system model which also includes explicit contact dynamics.
- **p. 1 / Abstract - extractive body cue:** Therefore, contact locations, sequences and timings are not prespecified but optimized by the solver.
- **p. 1 / Abstract - extractive body cue:** Yet, thorough numerical and software engineering allows for running the nonlinear Optimal Control solver at rates up to 190 Hz on a quadruped for a ...
- **p. 1 / Abstract - extractive body cue:** This outperforms the state of the art by at least one order of magnitude.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness of the plans.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this field, centroidal dynamics approaches [5]-[9] become increasingly popular as they capture the core dynamics of the problem.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Contributions In this work, we demonstrate whole-body, contact invariant nonlinear MPC for highly dynamic motions that require explicit reasoning about the full dynamics of the ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Since our code mostly consists of matrix and vector manipulations and register sizes of AVX are doubled over SSE, we obtained an additional speedup of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section III we describe our approach of solving the problem.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** While the development of processors with faster clock speed has stalled in recent years, processing power instead foremost grows due to higher computation core counts ...
- **p. 3 / III. NMPC APPROACH - extractive body cue:** In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy.
- **p. 3 / III. NMPC APPROACH - extractive body cue:** It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Integration and Sensitivity Computation Our system dynamics include a contact model that needs to be chosen stiff enough to approximate the real physics of contact ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control action and Kn a linear feedback controller ... | proprioception, reference pose/motion, visual or language command | p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| State/latent | designs, time-varying, state-feedback, controllers, form, xref, where, feedforward, control, action, linear, feedback | whole-body pose, balance/contact state와 skill/mode | p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH) |
| Output/action | The optimized control input obtained from the NMPC solver is then augmented with the output of two tracking controllers. instructions. | joint/whole-body action, motion target 또는 task trajectory | p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Objective/outcome | AN-1, B1, . . . , BN-1. - quadratize cost function (1) around X, U for multiple-shooting intervals 1 to N. policy update. | tracking, balance, skill/task success와 recovery | p. 3 (III. NMPC APPROACH), p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Contributions In this work, we demonstrate whole-body, contact invariant nonlinear MPC for highly dynamic motions that require explicit reasoning about the full dynamics of the ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Since our code mostly consists of matrix and vector manipulations and register sizes of AVX are doubled over SSE, we obtained an additional speedup of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Section III we describe our approach of solving the problem.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** While the development of processors with faster clock speed has stalled in recent years, processing power instead foremost grows due to higher computation core counts ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, GNMS reaches almost ...
- **p. 5 / VI. RESULTS - extractive body cue:** Also, we add a strong cost penalty on the base orientation to improve stability.
- **p. 7 / VI. RESULTS - extractive body cue:** As a result, the controller achieves a constant apex height but drifts slightly in x and y directions.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 5 (VI. RESULTS) |
| Embodiment/environment | While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get back as close as possible to the nominal state. | hardware/simulator version and reset protocol | p. 6 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Dataset/benchmark | We test a periodic trotting gait on both robots and disturb them during the tests. | role, split, size and leakage | p. 6 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 5 (VI. RESULTS), p. 5 (VI. RESULTS) |
| Metric | Even placing planks under single feet does not deteriorate performance. | definition, denominator, direction and uncertainty | p. 5 (VI. RESULTS), p. 7 (VI. RESULTS), p. 7 (VI. RESULTS) |
| Baseline/ablation | Compared to ANYmal the magnitude of the deviations is slightly larger. | fair input/data/compute/action matching | p. 6 (VI. RESULTS), p. 6 (VI. RESULTS), p. 7 (VI. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot be parallelized easily.
- **p. 7 / VII. SUMMARY AND OUTLOOK - extractive body cue:** Furthermore, while most tasks by design stayed within the physical limitations of the platforms, GNMS would allow us to handle constraints such as torque limitations ...
- **p. 5 / VI. RESULTS - extractive body cue:** The resulting overall controller is stable and can robustly handle aforementioned disturbances.
- **p. 6 / VI. RESULTS - extractive body cue:** Also here we observe that the controller is robust to disturbances.
- **p. 7 / VII. SUMMARY AND OUTLOOK - extractive body cue:** We expect that a longer time horizon could show more elaborate disturbance rejection and recovery behavior since it offers more flexibility and predictive capabilities to ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** In contrast, iLQR requires to compute a single, continuous forward simulation and thus does not benefit from a multi-core processor in this step.

## Why Read It

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Also, especially interesting tasks such as periodic gaits could not be transferred to hardware due to model mismatches and lack of robustness of the plans.를 문제로 두고, In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. NMPC APPROACH), p. 3 (III. NMPC APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** In this field, centroidal dynamics approaches [5]-[9] become increasingly popular as they capture the core dynamics of the problem. (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Note that running only a single solver iteration before updating the state measurement results in better overall performance than running multiple iterations and letting the solver converge. (p. 5, VI. RESULTS).
- **Explicit failure boundary:** Even placing planks under single feet does not deteriorate performance. (p. 5, VI. RESULTS).
