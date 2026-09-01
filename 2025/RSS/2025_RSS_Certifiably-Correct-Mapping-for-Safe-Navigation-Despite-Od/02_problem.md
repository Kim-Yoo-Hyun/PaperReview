# Problem - Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p007.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p007.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)): Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions.
- **p. 1 / Abstract - extractive body cue:** However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle maps and therefore collisions.
- **p. 1 / Abstract - extractive body cue:** This paper introduces a framework for certifiably-correct mapping that ensures that the obstacle map correctly classifies obstacle-ree regions despite the ‘odometry drift in vision-based localization ...
- **p. 1 / Abstract - extractive body cue:** By deflating the safe region based on the incremental odometry error at each timestep, we ensure that the map remains accurate and reliable locally around ...
- **p. 1 / Abstract - extractive body cue:** ur contributions include two approaches to modify popular obstacle mapping paradigms, (I) Safe Flight Corridors, and (Ud) Signed Distance Fields.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | Accurate, state, estimation, mapping, essential, safe, robotic, navigation, planners, controllers | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | prove, correctness, applicability, ofthis, frame, popular, state-of-the-art, mapping | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Accurate, state, estimation, mapping, essential, safe, robotic, navigation, planners, controllers | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: Section, introduce, deflation, mechanism, representations, methods, certified, maps | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Overview, notation, objectives, Various, methods, have, been, developed | p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Success / guarantee | goal reach with collision-free execution | p. 1 (1. INTRODUCTION), p. 1 (Abstract), p. 2 (1. INTRODUCTION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** As exemplified by the DARPA SubT Challenge, teams have developed perception systems capable of navigating subterranean environments [21, 22, 23].
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In contrast, the method proposed in this paper introduces a different strategy: regions where correctness cannot be assured are "forgotten," ensuring that only reliable, consistent ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 1 (Abstract)): In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps to acheive safe navigation, Finally ...

- **p. 2 / 1. INTRODUCTION - extractive body cue:** In contrast to [27], this paper assumes that the incremental pose estimate is bounded in a Lie-algebraic sense, which allows ‘our methods to be applied ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Our main contributions are as follows:
- **p. 1 / Abstract - extractive body cue:** Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | The rover uses an onboard safety filter to prevent collisions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Unlike baseline methods which result in collisions, our approach prevents crashes by deflating the safe regions appropriately. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), interface p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), objective p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
