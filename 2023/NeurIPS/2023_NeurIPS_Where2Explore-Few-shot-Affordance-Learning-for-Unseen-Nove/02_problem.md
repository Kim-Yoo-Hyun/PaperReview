# Problem - Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.07473; PDF retrieval source: https://arxiv.org/pdf/2309.07473. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): This limitation hinders the efficiency and safety of real-world applications of robots.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Articulated object manipulation is a fundamental yet challenging task in robotics.
- **p. 1 / Abstract - extractive body cue:** Due to significant geometric and semantic variations across object categories, previous manipulation models struggle to generalize to novel categories.
- **p. 1 / Abstract - extractive body cue:** Few-shot learning is a promising solution for alleviating this issue by allowing robots to perform a few interactions with unseen objects.
- **p. 1 / Abstract - extractive body cue:** However, extant approaches often necessitate costly and inefficient test-time interactions with each unseen instance.
- **p. 1 / Abstract - extractive body cue:** Recognizing this limitation, we observe that despite their distinct shapes, different categories often share similar local geometries essential for manipulation, such as pullable handles and ...
- **p. 1 / 1 Introduction - extractive body cue:** This limitation hinders the efficiency and safety of real-world applications of robots.
- **p. 1 / 1 Introduction - extractive body cue:** However, due to the significant variance in the objects' structure, 3D geometry, and articulation types across categories, developing efficient perception and manipulation systems that can ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation hinders the efficiency and safety of real-world applications of robots. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | similarity, module, designed, take, partial, point, cloud, object, action, directions | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Thanks, property, similarity, conditioned, action, directions, gripper, orientations | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: similarity, module, designed, take, partial, point, cloud, object, action, directions | p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method) |
| Decision / output variable | geometry/map/query r; body terms: demonstrate, framework, capability, efficiently, explore, novel, categories, exploiting | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: train, similarity, module, loss, measure, distance, between, prediction | p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** However, due to the significant variance in the objects' structure, 3D geometry, and articulation types across categories, developing efficient perception and manipulation systems that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering the substantial semantic and geometric gap between known shapes and novel categories, forming an efficient exploration strategy for out-of-distribution objects is challenging.
- **p. 2 / 1 Introduction - extractive body cue:** Via fine-tuning our network with the interactions on novel objects, the model could generalize to unseen objects within this novel category (Bottom Right).
- **p. 3 / 1 Introduction - extractive body cue:** • Exploring the challenging task of cross-category few-shot learning for articulated object manipulation, requiring the model to capture fine-grained geometric information from an entirely new ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method), p. 3 (4 Method), p. 3 (4 Method)): The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.

- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our framework by training our model on constrained object categories and applying few-shot learning to novel categories with limited shapes.
- **p. 5 / 4 Method - extractive body cue:** As shown in the right part of figure 2, when faced with a novel category, our framework will first predict the similarity of the objects.
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 3 / 4 Method - extractive body cue:** As shown in Figure 2, we propose the ‘Where2Explore' framework to explicitly leverage the similar semantics on local geometries shared across different categories for cross-category ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | While affordance fails to directly generalize to novel objects (Left), the similarity module can still discover areas that ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Table 4: Few-shot learning on novel categories using different interaction budget (1, 2, 5). B More Experimental Results ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 5 (4 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 5 (4 Method), objective p. 6 (4 Method), p. 6 (4 Method), p. 5 (4 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** This limitation hinders the efficiency and safety of real-world applications of robots. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. (p. 8, 5 Experiments).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
