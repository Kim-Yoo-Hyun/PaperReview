# Problem - Matterport3D: Learning from RGB-D Data in Indoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1709.06158; PDF retrieval source: https://arxiv.org/pdf/1709.06158. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models can be trained.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Access to large, diverse RGB-D datasets is critical for training RGB-D scene understanding algorithms.
- **p. 1 / Abstract - extractive body cue:** However, existing datasets still cover only a limited number of views or a restricted scale of spaces.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.
- **p. 1 / Abstract - extractive body cue:** Annotations are provided with surface reconstructions, camera poses, and 2D and 3D semantic segmentations.
- **p. 1 / Abstract - extractive body cue:** The precise global alignment and comprehensive, diverse panoramic set of views over entire buildings enable a variety of supervised and self-supervised computer vision tasks, including ...
- **p. 1 / 1. Introduction - extractive body cue:** Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models can be trained.
- **p. 1 / 1. Introduction - extractive body cue:** Unfortunately, current RGB-D datasets have small numbers of images [33], limited scene coverage [17], limited viewpoints [35], and/or motion blurred imagery.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | More specifically, we train a convolutional neural network (ResNet-50 [18]) to map an input image patch to a 512 dimensional descriptor. | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | More, specifically, train, convolutional, neural, network, ResNet-50, input, image, patch | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Similar, state, train, ConvNet, triplet, Siamese, fashion, where | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: More, specifically, train, convolutional, neural, network, ResNet-50, input, image, patch | p. 5 (4.1. Keypoint Matching), p. 4 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching) |
| Decision / output variable | method trajectory/action; body terms: introduce, Matterport3D, large-scale, RGB-D, dataset, containing, panoramic, views | p. 1 (Abstract), p. 4 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Although, have, ground-truth, camera, poses, dataset, cannot, measure | p. 3 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 6 (4.2. View Overlap Prediction), p. 6 (4.2. View Overlap Prediction), p. 7 (4.3. Surface Normal Estimation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4.2. View Overlap Prediction), p. 6 (4.2. View Overlap Prediction), p. 1 (1. Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Unfortunately, current RGB-D datasets have small numbers of images [33], limited scene coverage [17], limited viewpoints [35], and/or motion blurred imagery.
- **p. 2 / 1. Introduction - extractive body cue:** For each of these tasks, we provide baseline results using variants of existing state-of-the-art algorithms demonstrating the benefits of the Matterport3D data; we hope that ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 4 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), p. 2 (1. Introduction), p. 2 (1. Introduction)): In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.

- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Providing scans of homes in their entirety enables opportunities for learning about long-range context, which is critical for holistic scene understanding and autonomous navigation.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** This multiplicity and diversity of views enables opportunities for learning to predict view-dependent surface properties, such as material reflectance [4, 26], and for learning to ...
- **p. 2 / 1. Introduction - extractive body cue:** The surface normals estimated from highquality depths in diverse scenes allows training models for normal estimation from color images that outperform previous ones.
- **p. 2 / 1. Introduction - extractive body cue:** The precise global alignment over building scale allows training for state-of-the-art keypoint descriptors that can robustly match keypoints from drastically varying camera views.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (4.1. Keypoint Matching), p. 4 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 8 (4.4. Region-Type Classification). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (4.1. Keypoint Matching), p. 4 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 8 (4.4. Region-Type Classification), objective p. 3 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 6 (4.2. View Overlap Prediction), p. 6 (4.2. View Overlap Prediction), p. 7 (4.3. Surface Normal Estimation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
