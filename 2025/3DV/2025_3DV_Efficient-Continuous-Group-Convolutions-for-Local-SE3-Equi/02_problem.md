# Problem - Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=c6RR0bqNVI&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): The relative orientations of different objects in the scene cannot be captured by global equivariance as obtained by existing architectures or by data augmentation techniques.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Extending the translation equivariance property of convolutional neural networks to larger symmetry groups has been shown to reduce sample complexity and enable more discriminative feature ...
- **p. 1 / Abstract - extractive body cue:** Further, exploiting additional symmetries facilitates greater weight sharing than standard convolutions, leading to an enhanced network expressivity without an increase in parameter count.
- **p. 1 / Abstract - extractive body cue:** However, extending the equivariant properties of a convolution layer comes at a computational cost.
- **p. 1 / Abstract - extractive body cue:** In particular, for 3D data, expanding equivariance to the SE(3) group (rotation and translation) results in a 6D convolution operation, which is not tractable for ...
- **p. 1 / Abstract - extractive body cue:** While efforts have been made to develop efficient SE(3) equivariant networks, existing approaches rely on discretization or only introduce global rotation equivariance.
- **p. 2 / 1. Introduction - extractive body cue:** The relative orientations of different objects in the scene cannot be captured by global equivariance as obtained by existing architectures or by data augmentation techniques.
- **p. 1 / 1. Introduction - extractive body cue:** Approaches learning directly from 3D data often take inspiration from the success in 2D vision and address two of the main challenges in such data ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The relative orientations of different objects in the scene cannot be captured by global equivariance as obtained by existing architectures or by ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (Note that the definition given is cross-correlation instead of convolution since this aligns better with template-matching.) It is well known that convolution ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Note, definition, given, cross-correlation, instead, convolution, since, aligns, better, template-matching | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | during, training, only, sampling, subset, elements, input, output | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Note, definition, given, cross-correlation, instead, convolution, since, aligns, better, template-matching | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution) |
| Decision / output variable | geometry/map/query r; body terms: finite, subset, referred, frame, solve, group, equivariant, integral | p. 2 (1. Introduction), p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: One, solution, input, kernel, cost, losing, capacity, capture | p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.2. Shape classification), p. 6 (4.2. Shape classification), p. 6 (4.2. Shape classification) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Approaches learning directly from 3D data often take inspiration from the success in 2D vision and address two of the main challenges in such data ...
- **p. 2 / 1. Introduction - extractive body cue:** Group convolution is an operation that is, per definition, equivariant to a specific group and, hence, capable of coping with such problems.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution), p. 4 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution)): In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which allows for exact equivariance (as opposed ...

- **p. 3 / 3.1. Group equivariant convolution - extractive body cue:** Further, considering Y = G/H as quotient space with H = {g ∈G/gy0 = y0} as the stabilizer subgroup StabG(y0), which consists of group elements ...
- **p. 4 / 3.2. Efficient group convolution - extractive body cue:** To achieve exact equivariance with tractable computational load, we propose a carefully constructed grid F(xj) ⊂SE(3) specific to each point xj ∈R3.
- **p. 4 / 3.1. Group equivariant convolution - extractive body cue:** equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial ...
- **p. 5 / 3.2. Efficient group convolution - extractive body cue:** Therefore, we propose to perform a stochastic approximation of Eq.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 4. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models, especially ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | Figure 5. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | When compared to global equivariant networks, our method falls behind in the I / SO(3) setup and achieves ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution), p. 1 (1. Introduction), objective p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
