# Problem - Contact-Invariant Optimization for Hand Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://homes.cs.washington.edu/~zoran/behavior-discovery.html; PDF retrieval source: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should change from one phase to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a motion synthesis framework capable of producing a wide variety of important human behaviors that have rarely been studied, including getting up from ...
- **p. 1 / Abstract - extractive body cue:** Our framework is not specific to humans, but applies to characters of arbitrary morphology and limb configuration.
- **p. 1 / Abstract - extractive body cue:** The approach is fully automatic and does not require domain knowledge specific to each behavior.
- **p. 1 / Abstract - extractive body cue:** It also does not require pre-existing examples or motion capture data.
- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 2 / 1 Introduction - extractive body cue:** In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should ...
- **p. 1 / 1 Introduction - extractive body cue:** Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, biomechanics, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Instead, movement details and complexity should emerge from an automated procedure whose only inputs are intuitive high-level goals that are easy to ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | Instead, movement, details, complexity, should, emerge, automated, procedure, whose, only | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | include, getting, ground, crawling, climbing, moving, heavy, objects | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Instead, movement, details, complexity, should, emerge, automated, procedure, whose, only | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: core, framework, contact-invariant, optimization, CIO, introduce, here, present | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | task/contact/pose objective; cue terms: auxiliary, variables, affect, only, cost, function, dynamics, enabling | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | completion, contact success and robustness | p. 6 (5 Results), p. 6 (5 Results), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, biomechanics, ...
- **p. 1 / 1 Introduction - extractive body cue:** With the current state-of-the-art in automated motion synthesis, any additional complex behavior would require a new movement model carefully crafted by experts from scratch.
- **p. 2 / 1 Introduction - extractive body cue:** 1.1 The key idea: Contact-Invariant Optimization (CIO) As with prior methods for automated behavior synthesis, our CIO method also comes down to exploiting domain-specific knowledge.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.

- **p. 1 / 1 Introduction - extractive body cue:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc
- **p. 2 / 1 Introduction - extractive body cue:** The important difference is that the domain to which our method is tailored is much larger, and includes any behavior of any articulated character where ...
- **p. 2 / 1 Introduction - extractive body cue:** Intuitively, CIO is a way of reshaping a highly discontinuous and local-minima-prone search space of movements and contacts, into a slightly larger but much better-behaved ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | One way to remove this limitation is to simply increase the number of potential contacts and cover the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Exactly the same continuation scheme was successful in all of the diverse behaviors we studied, and so our ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
