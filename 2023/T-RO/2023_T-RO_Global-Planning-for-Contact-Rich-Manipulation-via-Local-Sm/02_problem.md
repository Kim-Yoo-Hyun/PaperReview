# Problem - Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2206.10787; PDF retrieval source: https://arxiv.org/pdf/2206.10787. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Faced with such challenges, many existing works have sought to explicitly consider contact modes by either enumerating or sampling them.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The empirical success of Reinforcement Learning (RL) in contact-rich manipulation leaves much to be understood from a model-based perspective, where the key difficulties are often ...
- **p. 1 / Abstract - extractive body cue:** The stochastic nature of RL addresses (i) and (ii) by effectively sampling and averaging the contact modes.
- **p. 1 / Abstract - extractive body cue:** On the other hand, model-based methods have tackled the same challenges by smoothing contact dynamics analytically.
- **p. 1 / Abstract - extractive body cue:** Our first contribution is to establish the theoretical equivalence of the two smoothing schemes for simple systems, and provide qualitative and empirical equivalence on several ...
- **p. 1 / Abstract - extractive body cue:** In order to further alleviate (ii), our second contribution is a convex, differentiable and quasi-dynamic formulation of contact dynamics, which is amenable to both smoothing ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Faced with such challenges, many existing works have sought to explicitly consider contact modes by either enumerating or sampling them.
- **p. 2 / I. INTRODUCTION - extractive body cue:** (iii) We combine contact mode smoothing with sampling-based motion planning, filling in a gap in the spectrum of existing methods and achieving efficient global planning ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Faced with such challenges, many existing works have sought to explicitly consider contact modes by either enumerating or sampling them. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | We overload the notation on the variables for convention, and say the system has state x ∈Rn, input u ∈Rm, and map ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | overload, notation, variables, convention, system, state, input, Moreover, derivatives, dynamics | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | derivatives, discontinuous, functions, they, good, local, approximation, CQDC | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: overload, notation, variables, convention, system, state, input, Moreover, derivatives, dynamics | p. 5 (II. LOCAL THEORY OF SMOOTHING), p. 2 (I. INTRODUCTION), p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: first, contribution, establish, theoretical, equivalence, smoothing, schemes, simple | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: Letting, denote, objective, function, gradients, Remarkably, implies, quasi-dynamic | p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE), p. 4 (II. LOCAL THEORY OF SMOOTHING), p. 5 (II. LOCAL THEORY OF SMOOTHING), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS), p. 1 (I. INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. LOCAL THEORY OF SMOOTHING) |
| Success / guarantee | completion, contact success and robustness | p. 17 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS), p. 18 (IX. SIM2REAL TRANSFER & HARDWARE RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** (iii) We combine contact mode smoothing with sampling-based motion planning, filling in a gap in the spectrum of existing methods and achieving efficient global planning ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This invalidity of the local model presents significant challenges for both *These authors contributed equally to this work.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our final contribution is to fill in this gap by combining smoothing-based contact mode abstraction and the global search capabilities of RRT.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (II. LOCAL THEORY OF SMOOTHING)): Our first contribution is to establish the theoretical equivalence of the two smoothing schemes for simple systems under our framework (Sec.II,IV-C).

- **p. 2 / I. INTRODUCTION - extractive body cue:** (ii) We present a convex, differentiable formulation of quasi-dynamic contact dynamics and its analytic smoothing, which we show to be highly effective for contact-rich manipulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Examples of contact-rich plans generated by our method.
- **p. 1 / Abstract - extractive body cue:** Our final contribution resolves (iii), where we show that classical sampling-based motion planning algorithms can be effective in global planning when contact modes are abstracted ...
- **p. 3 / II. LOCAL THEORY OF SMOOTHING - extractive body cue:** (1) which consists of the sensitivity term J(¯x) ∈Rm×n, and a bias term µ(¯x) ∈Rm, which we refer to as model parameters (J (¯x) , ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 17 | These experiments further shed light on the efficacy and the limitations of our proposed method. | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | The collision geometries, robot controller stiffness and coefficients of friction are kept consistent between the CQDC dynamics and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | However, the necessary damping to uphold the quasidynamic assumption does not always exist on 3D systems. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (II. LOCAL THEORY OF SMOOTHING), p. 2 (I. INTRODUCTION), p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 5 (II. LOCAL THEORY OF SMOOTHING), p. 2 (I. INTRODUCTION), p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS), objective p. 7 (III. CONVEX QUASI-DYNAMIC DIFFERENTIABLE), p. 4 (II. LOCAL THEORY OF SMOOTHING), p. 5 (II. LOCAL THEORY OF SMOOTHING), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS), p. 8 (IV. SMOOTHING OF CONTACT DYNAMICS), p. 1 (I. INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
