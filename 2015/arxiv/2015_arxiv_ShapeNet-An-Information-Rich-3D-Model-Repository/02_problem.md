# Problem - ShapeNet: An Information-Rich 3D Model Repository

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1512.03012; PDF retrieval source: https://arxiv.org/pdf/1512.03012. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, a critical bottleneck facing the adoption of data-driven methods for 3D content is the lack of large-scale, curated datasets of 3D models that are available to the community.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects.
- **p. 1 / Abstract - extractive PDF cue:** ShapeNet contains 3D models from a multitude of semantic categories and organizes them under the WordNet taxonomy.
- **p. 1 / Abstract - extractive PDF cue:** It is a collection of datasets providing many semantic annotations for each 3D model such as consistent rigid alignments, parts and bilateral symmetry planes, physical ...
- **p. 1 / Abstract - extractive PDF cue:** Annotations are made available through a public web-based interface to enable data visualization of object attributes, promote data-driven geometric analysis, and provide a large-scale quantitative ...
- **p. 1 / Abstract - extractive PDF cue:** At the time of this technical report, ShapeNet has indexed more than 3,000,000 models, 220,000 models out of which are classified into 3,135 categories (WordNet ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, a critical bottleneck facing the adoption of data-driven methods for 3D content is the lack of large-scale, curated datasets of 3D models that are ...
- **p. 1 / 1. Introduction - extractive PDF cue:** At the same time, there are many open research problems due to fundamental challenges in using 3D content.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a critical bottleneck facing the adoption of data-driven methods for 3D content is the lack of large-scale, curated datasets of 3D ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | These goals imply several desiderata for ShapeNet: • Broad and deep coverage of objects observed in the real world, with thousands of ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | goals, imply, several, desiderata, ShapeNet, Broad, deep, coverage, objects, observed | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Motivated, far-reaching, impact, dataset, efforts, Penn, Treebank, WordNet | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: goals, imply, several, desiderata, ShapeNet, Broad, deep, coverage, objects, observed | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Decision / output variable | method trajectory/action; body terms: Motivated, far-reaching, impact, dataset, efforts, Penn, Treebank, WordNet | p. 1 (1. Introduction), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Recently, data-driven, methods, machine, learning, community, have, been | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1. Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.1. Category Annotation), p. 5 (4. Annotation Acquisition and Validation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** At the same time, there are many open research problems due to fundamental challenges in using 3D content.
- **p. 2 / 1. Introduction - extractive PDF cue:** We then describe the acquisition and validation of annotations collected so far (Section 4), summarize the current state of all available ShapeNet datasets, and provide ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 1 (Abstract)): Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands of citations, we propose establishing ...

- **p. 1 / Abstract - extractive PDF cue:** We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
