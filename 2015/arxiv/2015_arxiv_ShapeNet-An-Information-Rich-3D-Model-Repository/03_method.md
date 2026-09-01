# Method - ShapeNet: An Information-Rich 3D Model Repository

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1512.03012; PDF retrieval source: https://arxiv.org/pdf/1512.03012. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4.2. Hierarchical Rigid Alignment), p. 1 (1. Introduction), p. 6 (4.1. Category Annotation), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): For the alignment at each level, we first use a geometric algorithm described in the Appendix A.1, and then ask human experts to check and correct possible misalignments.

## Method Body Digest

- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive PDF cue:** For the alignment at each level, we first use a geometric algorithm described in the Appendix A.1, and then ask human experts to check and ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands ...
- **p. 6 / 4.1. Category Annotation - extractive PDF cue:** After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to verify ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We then describe the acquisition and validation of annotations collected so far (Section 4), summarize the current state of all available ShapeNet datasets, and provide ...
- **p. 1 / 1. Introduction - extractive PDF cue:** RGB-D sensors and other technology for scanning and reconstruction are providing increasingly higher fidelity geometric representations of objects and real environments that can eventually become ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We end with a discussion of ShapeNet's future trajectory and connect it with several research directions (Section 7).
- **p. 5 / 4.1. Category Annotation - extractive PDF cue:** As described in Section 3.2, we assign each 3D model to one or more synsets in the WordNet taxonomy.
- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, data-driven methods from the machine learning community have been exploited by researchers in vision and NLP (natural language processing). "Big data" in the visual ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands ...
- **p. 1 / Abstract - extractive PDF cue:** We present ShapeNet: a richly-annotated, large-scale repository of shapes represented by 3D CAD models of objects.

## Source Evidence Cues

- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive PDF cue:** For the alignment at each level, we first use a geometric algorithm described in the Appendix A.1, and then ask human experts to check and ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands ...
- **p. 6 / 4.1. Category Annotation - extractive PDF cue:** After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human workers to verify ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We then describe the acquisition and validation of annotations collected so far (Section 4), summarize the current state of all available ShapeNet datasets, and provide ...
- **p. 1 / 1. Introduction - extractive PDF cue:** RGB-D sensors and other technology for scanning and reconstruction are providing increasingly higher fidelity geometric representations of objects and real environments that can eventually become ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We end with a discussion of ShapeNet's future trajectory and connect it with several research directions (Section 7).
- **p. 5 / 4.1. Category Annotation - extractive PDF cue:** As described in Section 3.2, we assign each 3D model to one or more synsets in the WordNet taxonomy.
- **Detected method headings:** 3.3. Annotation Methodology (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | For the alignment at each level, we first use a geometric algorithm described in the Appendix A.1, and then ask human experts ... | p. 6 (4.2. Hierarchical Rigid Alignment), p. 1 (1. Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have ... | p. 1 (1. Introduction), p. 6 (4.1. Category Annotation) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | After we retrieve these models we use the popularity score of each model on the repository to sort models and ask human ... | p. 6 (4.1. Category Annotation), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1. Introduction - extractive PDF cue:** Recently, data-driven methods from the machine learning community have been exploited by researchers in vision and NLP (natural language processing). "Big data" in the visual ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goals, imply, several, desiderata, ShapeNet, Broad, deep, coverage, objects, observed, real, world, thousands, object | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | goals, imply, several, desiderata, ShapeNet, Broad, deep, coverage, objects, observed | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | Motivated, far-reaching, impact, dataset, efforts, Penn, Treebank, WordNet, ImageNet, collectively | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Recently, data-driven, methods, machine, learning, community, have, been, exploited, researchers | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** These goals imply several desiderata for ShapeNet: • Broad and deep coverage of objects observed in the real world, with thousands of object categories and ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We then describe the acquisition and validation of annotations collected so far (Section 4), summarize the current state of all available ShapeNet datasets, and provide ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Motivated by the far-reaching impact of dataset efforts such as the Penn Treebank [20], WordNet [21] and ImageNet [4], which collectively have tens of thousands ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Scene understanding from 2D images is a grand challenge in vision that has recently benefited tremendously from 3D CAD models [28, 34].
- **p. 5 / 4. Annotation Acquisition and Validation - extractive PDF cue:** Our goal is to provide all annotations with high accuracy.
- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive PDF cue:** The goal of this step is to establish a consistent canonical orientation for models within each category.
- **p. 6 / 4.2. Hierarchical Rigid Alignment - extractive PDF cue:** Following the above discussion, it is natural for us to propose a hierarchical alignment method, with a small amount of human supervision.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Meaningful textual descriptions are rarely provided for individual models, and online repositories are usually either unorganized or grouped into gross categories (e.g., ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | There has been substantial growth in the number of of 3D models available online over the last decade, with repositories like the ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** alignment, level, first, geometric, algorithm, described, Appendix, then, human, experts, check, correct, possible, misalignments, Motivated, far-reaching, impact, dataset, efforts, Penn.
- **Relevant PDF headings:** 3.3. Annotation Methodology (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | The 12 object categories of PASCAL 3D+[35], a popular computer vision 3D benchmark dataset, are all covered by ShapeNetCore. | p. 7 (5.1. ShapeNetCore), p. 6 (4.1. Category Annotation) |
| Baseline harness | We estimate the absolute dimensions of models using prior work in size estimation [25], followed by manual verification. | p. 7 (4.5. Physical Property Estimation), p. 6 (4.1. Category Annotation) |
| Metric / failure reporting | Table 3. Total number of models for the top 100 ShapeNetSem categories (out of 270 categories). Each category is also linked to ... | p. 9 (Figure/Table caption), p. 5 (4. Annotation Acquisition and Validation) |

## Failure and Ablation Link

- **p. 6 / 4.1. Category Annotation - extractive PDF cue:** Although we do not currently use these models, the plane can easily be identified and removed through simple geometric analysis.
- **p. 6 / 4.1. Category Annotation - extractive PDF cue:** Through inspection, we identify and group 3D models into the following categories: single 3D models, 3D scenes, billboards, and big ground plane. • Single 3D ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4.2. Hierarchical Rigid Alignment), p. 1 (1. Introduction), p. 6 (4.1. Category Annotation), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), objective p. 1 (1. Introduction), temporal p. 2 (2. Background and Related Work), p. 2 (2. Background and Related Work), p. 3 (3.1. Data Collection), p. 3 (3.1. Data Collection), p. 5 (3.4. Annotation Schema and Web API), p. 6 (4.2. Hierarchical Rigid Alignment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
