# ShapeNet: An Information-Rich 3D Model Repository

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1512.03012.
> PDF retrieval source: https://arxiv.org/pdf/1512.03012. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2015 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Dataset, shape, representation
- Official paper: https://arxiv.org/abs/1512.03012
- Full-text retrieval: https://arxiv.org/pdf/1512.03012
- Code/Project: https://shapenet.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, a critical bottleneck facing the adoption of data-driven methods for 3D content is the lack of large-scale, curated datasets of 3D models that are available to the community.를 문제로 두고, Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands of citations, we propose establishing ShapeNet: a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects.
- **p. 1 / Abstract - extractive body cue:** ShapeNet contains 3D models from a multitude of semantic categories and organizes them under the WordNet taxonomy.
- **p. 1 / Abstract - extractive body cue:** It is a collection of datasets providing many semantic annotations for each 3D model such as consistent rigid alignments, parts and bilateral symmetry planes, physical ...
- **p. 1 / Abstract - extractive body cue:** Annotations are made available through a public web-based interface to enable data visualization of object attributes, promote data-driven geometric analysis, and provide a large-scale quantitative ...
- **p. 1 / Abstract - extractive body cue:** At the time of this technical report, ShapeNet has indexed more than 3,000,000 models, 220,000 models out of which are classified into 3,135 categories (WordNet ...
- **p. 1 / 1. Introduction - extractive body cue:** However, a critical bottleneck facing the adoption of data-driven methods for 3D content is the lack of large-scale, curated datasets of 3D models that are ...
- **p. 1 / 1. Introduction - extractive body cue:** At the same time, there are many open research problems due to fundamental challenges in using 3D content.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands ...
- **p. 1 / Abstract - extractive body cue:** We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects.
- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive body cue:** For the alignment at each level, we first use a geometric algorithm described in the Appendix A.1, and then ask human experts to check and ...
- **p. 6 / 4.1. Category Annotation - extractive body cue:** After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to verify ...
- **p. 2 / 1. Introduction - extractive body cue:** We then describe the acquisition and validation of annotations collected so far (Section 4), summarize the current state of all available ShapeNet datasets, and provide ...
- **p. 1 / 1. Introduction - extractive body cue:** RGB-D sensors and other technology for scanning and reconstruction are providing increasingly higher fidelity geometric representations of objects and real environments that can eventually become ...
- **p. 2 / 1. Introduction - extractive body cue:** We end with a discussion of ShapeNet's future trajectory and connect it with several research directions (Section 7).
- **p. 5 / 4.1. Category Annotation - extractive body cue:** As described in Section 3.2, we assign each 3D model to one or more synsets in the WordNet taxonomy.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | These goals imply several desiderata for ShapeNet: • Broad and deep coverage of objects observed in the real world, with thousands of object categories and millions of total instances. • Categorization scheme ... | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | goals, imply, several, desiderata, ShapeNet, Broad, deep, coverage, objects, observed, real, world | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | We then describe the acquisition and validation of annotations collected so far (Section 4), summarize the current state of all available ShapeNet datasets, and provide basic statistics on the collected annotations (Section ... | policy/controller trajectory 또는 measured result | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | Recently, data-driven methods from the machine learning community have been exploited by researchers in vision and NLP (natural language processing). "Big data" in the visual and textual domains has led to tremendous ... | success metric, robustness, generalization과 reproducibility | p. 1 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands ...
- **p. 1 / Abstract - extractive body cue:** We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3. Total number of models for the top 100 ShapeNetSem categories (out of 270 categories). Each category is also linked to the corresponding WordNet ...
- **p. 5 / 4. Annotation Acquisition and Validation - extractive body cue:** Our goal is to provide all annotations with high accuracy.
- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive body cue:** We explain by an example. "armchair", "chair" and "seat" are three categories in our taxonomy, each being a subcategory of its successor.
- **p. 6 / 4.1. Category Annotation - extractive body cue:** After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to verify ...
- **p. 7 / 4.3. Parts and Keypoints - extractive body cue:** models where further human annotation would be most informative, generate a new set of crowd-sourced annotation tasks, algorithmically propagate their results, and so on.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 5 (4. Annotation Acquisition and Validation) |
| Embodiment/environment | The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore. | hardware/simulator version and reset protocol | p. 7 (5.1. ShapeNetCore), p. 6 (4.1. Category Annotation) |
| Dataset/benchmark | We manually verify these detections and mark scenes for future analysis. • Billboards: planes with a painted texture. | role, split, size and leakage | p. 7 (5.1. ShapeNetCore), p. 6 (4.1. Category Annotation), p. 6 (4.1. Category Annotation), p. 7 (5.1. ShapeNetCore) |
| Metric | Our goal is to provide all annotations with high accuracy. | definition, denominator, direction and uncertainty | p. 5 (4. Annotation Acquisition and Validation), p. 6 (4.1. Category Annotation), p. 5 (4. Annotation Acquisition and Validation) |
| Baseline/ablation | We estimate the absolute dimensions of models using prior work in size estimation [25], followed by manual verification. | fair input/data/compute/action matching | p. 7 (4.5. Physical Property Estimation), p. 6 (4.1. Category Annotation), p. 6 (4.1. Category Annotation) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6. Discussion and Future Work - extractive body cue:** The construction of ShapeNet is a continuous, ongoing effort.
- **p. 7 / 6. Discussion and Future Work - extractive body cue:** Here we have just described the initial steps we have taken in defining ShapeNet and populating a core subset of model annotations that we hope ...
- **p. 7 / 6. Discussion and Future Work - extractive body cue:** We plan to grow ShapeNet in four distinct directions: Additional annotation types We will introduce several additional types of annotations that have strong connections to ...

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, a critical bottleneck facing the adoption of data-driven methods for 3D content is the lack of large-scale, curated datasets of 3D models that are available to the community.를 문제로 두고, Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands of citations, we propose establishing ShapeNet: a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.2. Hierarchical Rigid Alignment), p. 1 (1. Introduction), p. 6 (4.1. Category Annotation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
