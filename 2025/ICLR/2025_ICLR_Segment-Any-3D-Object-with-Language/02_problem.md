# Problem - Segment Any 3D Object with Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ENv1CeTwxc; PDF retrieval source: https://openreview.net/pdf/49d9ee59e578038d8529a39c19e31d4c61cdc5fe.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): Failure to segment such instances drastically narrows the scope of application. ∗Equal Contribution 1

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** In this paper, we investigate Open-Vocabulary 3D Instance Segmentation (OV3DIS) with free-form language instructions.
- **p. 1 / ABSTRACT - extractive PDF cue:** Earlier works mainly rely on annotated base categories for training which leads to limited generalization to unseen novel categories.
- **p. 1 / ABSTRACT - extractive PDF cue:** To mitigate the poor generalizability to novel categories, recent works generate class-agnostic masks or projecting generalized masks from 2D to 3D, subsequently classifying them with ...
- **p. 1 / ABSTRACT - extractive PDF cue:** However, these works often disregard semantic information in the mask generation, leading to sub-optimal performance.
- **p. 1 / ABSTRACT - extractive PDF cue:** Instead, generating generalizable but semantic-aware masks directly from 3D point clouds would result in superior outcomes.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Failure to segment such instances drastically narrows the scope of application. ∗Equal Contribution 1
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Due to the lack of novel classes during training, these methods easily overfit to the base categories and thus yielding sub-optimal performance on novel categories.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Failure to segment such instances drastically narrows the scope of application. ∗Equal Contribution 1 | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The goal of open-vocabulary 3D instance segmentation (OV-3DIS) with free-form language instructions is defined as follows: Given a 3D point cloud P ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | goal, open-vocabulary, instance, segmentation, OV-3DIS, free-form, language, instructions, defined, follows | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | segmentation, network, required, aligned, language, instructions, directly, segment | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: goal, open-vocabulary, instance, segmentation, OV-3DIS, free-form, language, instructions, defined, follows | p. 4 (3 METHOD), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: circumvent, issue, introduce, Cross, Modality, Decoder, CMD, incorporate | p. 5 (3 METHOD), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: overall, training, loss, combination, mask, semantic, multimodal, association | p. 7 (3 METHOD), p. 7 (3 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 METHOD), p. 7 (3 METHOD) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Due to the lack of novel classes during training, these methods easily overfit to the base categories and thus yielding sub-optimal performance on novel categories.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In view of the strong limitations of closed-set setting, open-set 3D instance segmentation (OS-3DIS) that aims at detecting and segmenting unseen classes based on instructions ...

## What the Paper Changes

PDF contribution framing (p. 5 (3 METHOD), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework.

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In summary, our contributions are as follows: • We propose a visual-language learning framework for OV-3DIS, SOLE.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** A multimodal fusion network is designed for SOLE, which can directly predict semantic-related masks from 3D point clouds with multimodal information, leading to high-quality and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In this paper, we propose SOLE: Segment any 3D Object with LanguagE to circumvent the abovementioned issues for OV-3DIS.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We propose the semantic-aware mask generator to obtain semantic-related masks from 3D point clouds, yielding better and more generalizable 3D masks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 2: Left (a) : Previous works train class-agnostic mask proposal module with only using mask annotations. In ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | In contrast, solely using 3D instance backbone feature f b (second row) cannot inherit the generalizable semantic information, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Given a free-form language instruction instead of category name, e.g., "I wanna see outside", the model only using ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 4, our method further shows superior robustness on more out-of-distribution data from Replica, achieving +9.8% improvement in AP ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 METHOD), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 4 (3 METHOD), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective p. 7 (3 METHOD), p. 7 (3 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
