# Problem - Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data [37,62,79].

## PDF Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** 3D semantic scene understanding, with the task of assigning semantics to every 3D point, plays a fundamental role in many computer vision applications, such as ...
- **p. 2 / 1 Introduction - extractive body cue:** Traditional studies in this field usually target solving this problem in a closed-set fashion [16,73], resulting in models that can only be used to make ...
- **p. 2 / 1 Introduction - extractive body cue:** Recent progress in computer vision have witnessed the emerging interests in solving semantic understanding tasks in open-vocabulary settings [35,62,67,78, 94].
- **p. 2 / 1 Introduction - extractive body cue:** In contrast to closed-set setting, models targeting open-vocabulary tasks must make predictions for any semantics described in text, including object category and fine-grained attributes (e.g., ...
- **p. 2 / 1 Introduction - extractive body cue:** However, this is a challenging task due to the wide diversity and complexity of possible queries.
- **p. 2 / 1 Introduction - extractive body cue:** Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale ...
- **p. 2 / 1 Introduction - extractive body cue:** Motivated by the advance of aligning text and image embeddings with large-scale foundation models [2, 39,48,65], existing methods mitigate this challenge by lifting the image ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | It takes posed RGB images and the reconstructed 3D point cloud as model inputs. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | takes, posed, RGB, images, reconstructed, point, cloud, model, inputs, Open-Vocabulary | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | summary, make, following, contributions, best, knowledge, first, leverage | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: takes, posed, RGB, images, reconstructed, point, cloud, model, inputs, Open-Vocabulary | p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 3 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, make, following, contributions, best, knowledge, first, leverage | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (4 HKUST) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: frozen, features, extracted, decoder, U-Net, diffusion, model, trained | p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 4 (X. Zhu et al), p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 8 (X. Zhu et al) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (X. Zhu et al), p. 7 (X. Zhu et al), p. 8 (X. Zhu et al) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 4 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Motivated by the advance of aligning text and image embeddings with large-scale foundation models [2, 39,48,65], existing methods mitigate this challenge by lifting the image ...
- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, directly distilling knowledge from these features as normally done in prior art [54,56,62] is infeasible.

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (4 HKUST), p. 1 (4 HKUST), p. 2 (1 Introduction)): In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary 3D semantic segmentation. - We ...

- **p. 3 / 1 Introduction - extractive body cue:** To mitigate these issues, we propose a novel mask distillation method tailored to distill knowledge from the Mask2Former style 2D branch [10, 87] to the ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks given novel text prompts, without relying on any annotated 3D ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite these achievements, contrastively trained CLIP-based models exhibit limitations in handling fine-grained classes [66] and novel compositional text queries [58], restricting their performance in open-vocabulary ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | There are several limitations of the proposed model. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | As Replica does not provide the training data, we perform training on ScanNet and perform evaluation on Replica, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 3 (1 Introduction), p. 5 (X. Zhu et al). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 3 (1 Introduction), p. 5 (X. Zhu et al), objective p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 4 (X. Zhu et al), p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 8 (X. Zhu et al).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
