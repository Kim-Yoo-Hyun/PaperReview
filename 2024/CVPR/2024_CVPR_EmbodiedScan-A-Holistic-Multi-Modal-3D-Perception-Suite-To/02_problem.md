# Problem - EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small [12, 45] or lack comprehensive annotations [6, 51] to support the aforemenThis CVPR paper is the Open Access ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In the realm of computer vision and robotics, embodied agents are expected to explore their environment and carry out human instructions.
- **p. 1 / Abstract - extractive body cue:** This necessitates the ability to fully understand 3D scenes given their first-person observations and contextualize them into language for interaction.
- **p. 1 / Abstract - extractive body cue:** However, traditional research focuses more on scene-level input and output setups from a global view.
- **p. 1 / Abstract - extractive body cue:** To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** It encompasses over 5k scans encapsulating 1M ego-centric RGB-D views, 1M language prompts, 160k 3D-oriented boxes spanning over 760 categories, some of which partially align ...
- **p. 1 / 1. Introduction - extractive body cue:** Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small [12, 45] or lack comprehensive annotations [6, 51] to support the aforemenThis CVPR ...
- **p. 1 / 1. Introduction - extractive body cue:** It commences its journey devoid of any prior knowledge about the scene, guided only by an initial instruction.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Regarding data, earlier datasets targeting egocentric RGB-D inputs are either too small [12, 45] or lack comprehensive annotations [6, 51] to support ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Given this dataset, we can take multi-modality input, including RGB images, point clouds derived from depth maps as well as language prompts, ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, dataset, take, multi-modality, input, including, RGB, images, point, clouds | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | necessitates, ability, fully, understand, scenes, given, first-person, observations | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Given, dataset, take, multi-modality, input, including, RGB, images, point, clouds | p. 4 (4. Embodied Perceptron), p. 1 (1. Introduction), p. 1 (Abstract) |
| Decision / output variable | method trajectory/action; body terms: Building, upon, database, introduce, baseline, framework, named, Embodied | p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Training, objectives, include, original, classification, loss, centerness, disentangled | p. 6 (4.2. Sparse & Dense Decoder), p. 5 (4. Embodied Perceptron), p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder), p. 4 (3.2. Annotation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4. Embodied Perceptron), p. 5 (4.1. Multi-Modal 3D Encoder), p. 4 (3.2. Annotation) |
| Success / guarantee | comparable score and protocol validity | p. 6 (5. Benchmark), p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** It commences its journey devoid of any prior knowledge about the scene, guided only by an initial instruction.

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 1 (Abstract)): Building upon this database, we introduce a baseline framework named Embodied Perceptron.

- **p. 1 / Abstract - extractive body cue:** To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | On the other hand, since we cannot trivially obtain the reconstruction of a new environment, models trained with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Figure 2. Dataset composition. Embodied- Scan is composed of three data sources and has similar scans, images, objects, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | 3a) to address limitations in existing 3D box annotations, i.e., lack of orientation and small object annotations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Generated language prompts following SR3D fall into five types of spatial object-to-object relations: Horizontal Proximity, Vertical Proximity, Support, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4. Embodied Perceptron), p. 1 (1. Introduction), p. 1 (Abstract), p. 4 (3.1. Data Collection & Processing). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (4. Embodied Perceptron), p. 1 (1. Introduction), p. 1 (Abstract), p. 4 (3.1. Data Collection & Processing), objective p. 6 (4.2. Sparse & Dense Decoder), p. 5 (4. Embodied Perceptron), p. 5 (4.1. Multi-Modal 3D Encoder), p. 6 (4.2. Sparse & Dense Decoder), p. 4 (3.2. Annotation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
