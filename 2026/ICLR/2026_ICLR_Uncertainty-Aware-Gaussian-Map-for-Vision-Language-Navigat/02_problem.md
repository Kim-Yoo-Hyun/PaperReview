# Problem - Uncertainty-Aware Gaussian Map for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LPv59noPAy; PDF retrieval source: https://openreview.net/pdf/465d0779d3489df4f9f1afa9b725d78970007e26.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Despite these advances, existing agents typically ignore uncertainty in perception when making decisions.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Vision-Language Navigation (VLN) requires an agent to navigate 3D environments following natural language instructions.
- **p. 1 / ABSTRACT - extractive PDF cue:** During navigation, existing agents commonly encounter perceptual uncertainty, such as insufficient evidence for reliable grounding or ambiguity in interpreting spatial cues, yet they typically ignore ...
- **p. 1 / ABSTRACT - extractive PDF cue:** In this work, we explicitly model three forms of perceptual uncertainty (i.e., geometric, semantic, and appearance uncertainty) and integrate them into the agent's observation space ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Concretely, our agent first constructs a Semantic Gaussian Map (SGM), composed of differentiable 3D Gaussian primitives initialized from panoramic observations, that encodes both the geometric ...
- **p. 1 / ABSTRACT - extractive PDF cue:** On top of SGM, geometric uncertainty is estimated through variational perturbations of Gaussian position and scale to assess structural reliability; semantic uncertainty is captured by ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Despite these advances, existing agents typically ignore uncertainty in perception when making decisions.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Their training recipes discourage expressing uncertainty or recognizing unreliable situations, instead incentivizing them to predict actions regardless of confidence [17].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite these advances, existing agents typically ignore uncertainty in perception when making decisions. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | observations, agent, learns, navigation, policy, at/X, predicts, actions, includes, navigable | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | navigable, viewpoint, agent, constructs, SGM, panoramic, observations, extends | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: observations, agent, learns, navigation, policy, at/X, predicts, actions, includes, navigable | p. 3 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: approximate, like, introduce, variational, distributions, optimize, them, minimizing | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Published, conference, ICLR, Since, constant, respect, minimizing, divergence | p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Their training recipes discourage expressing uncertainty or recognizing unreliable situations, instead incentivizing them to predict actions regardless of confidence [17].
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Brighter colors indicate higher uncertainty.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** High uncertainty in the distance; safer to detour right.

## What the Paper Changes

PDF contribution framing (p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 2 (1 INTRODUCTION)): To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing the Kullback-Leibler (KL) divergence to ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Extensive ablation studies confirm the contribution of each component (§4.4).
- **p. 6 / 3 METHOD - extractive PDF cue:** This fusion enables the agent to jointly reason about geometric structure and perceptual confidence, thereby promoting reliable and uncertainty-aware decision-making.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In the same manner, semantic uncertainty is estimated by perturbing the semantic attributes of Gaussians, which reveals ambiguous interpretations and allows the agent to down-weight ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 22 | Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 5 illustrates our diverse perceptual forms. i) SGM preserves detailed geometric structures while maintaining high-fidelity rendering of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 1: Motivation. Previous VLN agents typically ignore perceptual uncertainty when making decisions. As a result, they often ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 21 | Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 3 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD), p. 1 (1 INTRODUCTION), objective p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
