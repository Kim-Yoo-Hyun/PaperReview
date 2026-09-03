# Problem - OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2112.12143; PDF retrieval source: https://arxiv.org/pdf/2112.12143. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction)): Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data.

## PDF Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Image segmentation is an important step to organize an image into a small number of regions in order to understand "what" and "where" are in ...
- **p. 2 / 1 Introduction - extractive body cue:** Each region represents a semantically meaningful entity, which can be a thing (e.g., a chair) or stuff(e.g., floor).
- **p. 2 / 1 Introduction - extractive body cue:** Language is a natural interface to describe what is in an image.
- **p. 2 / 1 Introduction - extractive body cue:** However, semantic segmentation algorithms often only learn with closed-set categories, and thus are unable to recognize concepts outside labeled datasets.
- **p. 2 / 1 Introduction - extractive body cue:** The segmentation model takes text queries as inputs and produces segmented regions accordingly.
- **p. 3 / 1 Introduction - extractive body cue:** Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data.
- **p. 3 / 1 Introduction - extractive body cue:** We show that the model can generalize well to other datasets, reaching superior performances compared with prior works on segmentation proposals [3,33].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | We argue that what is missing in these state-of-the-art open-vocabulary classification models are mid-level representations from visual groupings [48], which organize an ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | argue, what, missing, state-of-the-art, open-vocabulary, classification, models, mid-level, representations, visual | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Learning, Segmentation, Masks, design, model, architecture, consists, feature | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: argue, what, missing, state-of-the-art, open-vocabulary, classification, models, mid-level, representations, visual | p. 2 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method) |
| Decision / output variable | path/waypoint/velocity; body terms: call, OpenSeg, standing, open-vocabulary, image, segmentation, evaluate, measure | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: grounding, loss, aims, maximizing, normalized, score, labeled, image-caption | p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 7 (3 Method), p. 6 (3 Method) |
| Success / guarantee | goal reach with collision-free execution | p. 9 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** We show that the model can generalize well to other datasets, reaching superior performances compared with prior works on segmentation proposals [3,33].

## What the Paper Changes

PDF body contribution framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method)): We call our method OpenSeg, standing for open-vocabulary image segmentation.

- **p. 3 / 1 Introduction - extractive body cue:** To evaluate our method, we measure performances on holdout image segmentation datasets.
- **p. 6 / 3 Method - extractive body cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | We hope to encourage future works to learn a generalist segmentation model that can transfer across datasets using ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | The small performance differences across different ways of text filtering show OpenSeg is robust to the noise in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Notably, OpenSeg is trained on COCO which does not include underwater scenes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | We find that predictions in the mIoU and Grounding mIoU settings can look quite differently and sometimes mIoU ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction), objective p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
