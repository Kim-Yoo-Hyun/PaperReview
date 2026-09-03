# Problem - Gaussian Splatting Visual MPC for Granular Media Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2410.09740v3. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, these models often underperform compared to linear dynamics models due to a lack of inductive biases.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects.
- **p. 1 / Abstract - extractive body cue:** However, manipulating granular materials such as beans, nuts, and rice remains challenging due to the intricate physics of particle interactions, high-dimensional and partially observable state, ...
- **p. 1 / Abstract - extractive body cue:** Current deep latent dynamics models often struggle to generalize in granular material manipulation due to a lack of inductive biases.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose a novel approach that learns a visual dynamics model over Gaussian splatting representations of scenes and leverages this model for ...
- **p. 1 / Abstract - extractive body cue:** Our method enables efficient optimization for complex manipulation tasks on piles of granular media.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these models often underperform compared to linear dynamics models due to a lack of inductive biases.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Several factors contribute to the difficulty of granular material manipulation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these models often underperform compared to linear dynamics models due to a lack of inductive biases. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (b) The dynamics model f predicts the temporal evolution of the Gaussian Splatting representation Zt with input action ut. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | dynamics, model, predicts, temporal, evolution, Gaussian, Splatting, representation, input, action | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Second, accounting, particles, planning, requires, high-dimensional, state, creates | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: dynamics, model, predicts, temporal, evolution, Gaussian, Splatting, representation, input, action | p. 3 (III. PRELIMINARIES), p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: form, node, features, GNN, consists, encoder, fenc, representation | p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: optimization, process, aims, acquire, sequence, actions, minimize, cost | p. 4 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Several factors contribute to the difficulty of granular material manipulation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This representation enables robots to optimize their actions, anticipate challenges, and adapt to dynamic environments.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Furthermore, we highlight its generalization capability by transferring a trained model to new environments with varying object shapes in a zero-shot setting.

## What the Paper Changes

PDF body contribution framing (p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder fenc with node representation ¯vi ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contribution: We use the Gaussian splats representing the scene at each time as a state vector that can be manipulated via MPC, effectively lowering ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our model successfully enables solutions of complex planning tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This representation enables robots to optimize their actions, anticipate challenges, and adapt to dynamic environments.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Future work could extend this framework to other non-rigid materials, further enhancing the capabilities of robotic systems in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PRELIMINARIES), p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. PRELIMINARIES), p. 3 (IV. OUR APPROACH), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective p. 4 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, these models often underperform compared to linear dynamics models due to a lack of inductive biases. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting representation, (b) learns a dynamics ... (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales. (p. 6, VI. LIMITATIONS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
