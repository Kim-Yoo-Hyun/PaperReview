# Problem - Detecting Twenty-thousand Classes using Image-level Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.02605; PDF retrieval source: https://arxiv.org/pdf/2201.02605. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 5 (3 Preliminaries), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries)): In our experiments, the proposal network and the bounding box regressors are not the current performance bottleneck, as modern detectors use an over-sufficient number of proposals in testing (1K proposals ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- **p. 1 / 1 Introduction - extractive body cue:** Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
- **p. 1 / 1 Introduction - extractive body cue:** Despite many data collection efforts, detection datasets [18, 28, 34, 49] are much smaller in overall size and vocabularies than classification datasets [10].
- **p. 1 / 1 Introduction - extractive body cue:** For example, the recent LVIS detection dataset [18] has 1000+ classes with 120K images; OpenImages [28] has 500 classes in 1.8M images.
- **p. 1 / 1 Introduction - extractive body cue:** Moreover, not all classes contain sufficient annotations to train a robust detector (see Figure 1 Top).
- **p. 5 / 3 Preliminaries - extractive body cue:** In our experiments, the proposal network and the bounding box regressors are not the current performance bottleneck, as modern detectors use an over-sufficient number of ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that the localization and classification sub-problems can be decoupled.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In our experiments, the proposal network and the bounding box regressors are not the current performance bottleneck, as modern detectors use an ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | We propose a simple classification loss that applies the image-level supervision to the proposal with the largest size, and do not supervise ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | simple, classification, loss, applies, image-level, supervision, proposal, largest, size, supervise | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | simple, leverage, image, supervision, learn, object, detectors, including | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: simple, classification, loss, applies, image-level, supervision, proposal, largest, size, supervise | p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Decision / output variable | path/waypoint/velocity; body terms: enables, learn, detectors, classes, would, have, been, impossible | p. 2 (X. Zhou et al), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Equalization, losses, SeeSaw, loss, reweights, per-class, balancing, gradients | p. 6 (X. Zhou et al), p. 4 (X. Zhou et al), p. 6 (X. Zhou et al), p. 2 (X. Zhou et al), p. 3 (X. Zhou et al), p. 3 (X. Zhou et al) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (X. Zhou et al), p. 3 (X. Zhou et al), p. 3 (X. Zhou et al) |
| Success / guarantee | goal reach with collision-free execution | p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 11 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** We observe that the localization and classification sub-problems can be decoupled.
- **p. 1 / 1 Introduction - extractive body cue:** Traditional methods tightly couple these two subproblems and thus rely on box labels for all classes.
- **p. 4 / 3 Preliminaries - extractive body cue:** We first describe the object detection problem and then detail our approach.
- **p. 4 / 3 Preliminaries - extractive body cue:** Given an image I ∈R3×h×w, object detection solves the two subproblems of (1) localization: find all objects with their location, represented as a box bj ...

## What the Paper Changes

PDF body contribution framing (p. 2 (X. Zhou et al), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (X. Zhou et al), p. 3 (X. Zhou et al)): This also enables our method to learn detectors for new classes which would have been impossible to predict and assign.

- **p. 1 / 1 Introduction - extractive body cue:** Object detection consists of two sub-problems - finding the object (localization) and naming it (classification).
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose Detector with image classes (Detic) that uses image-level supervision in addition to detection supervision.
- **p. 2 / X. Zhou et al - extractive body cue:** Experiments on the open-vocabulary LVIS [17, 18] and the open-vocabulary COCO [2] benchmarks show that our method can significantly improve over a strong box-supervised baseline, ...
- **p. 3 / X. Zhou et al - extractive body cue:** Our contributions are summarized below: - We identify issues and propose a simpler alternative to existing weaklysupervised detection techniques in the open-vocabulary setting. - Our ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | By default, a trained classifier cannot recognize novel classes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | 6 Limitations and Conclusions We present Detic which is a simple way to use image supervision in largevocabulary ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | We leave incorporating such information for future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 5 (3 Preliminaries), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), interface p. 2 (X. Zhou et al), p. 5 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), objective p. 6 (X. Zhou et al), p. 4 (X. Zhou et al), p. 6 (X. Zhou et al), p. 2 (X. Zhou et al), p. 3 (X. Zhou et al), p. 3 (X. Zhou et al).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
