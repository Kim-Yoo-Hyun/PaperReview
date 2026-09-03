# Method - Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.14365; PDF retrieval source: https://arxiv.org/pdf/2304.14365. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract)): Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network.
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; ...
- **p. 1 / Abstract - extractive body cue:** Robotic perception requires the modeling of both 3D geometry and semantics.
- **p. 2 / 1 Introduction - extractive body cue:** We formalize the 3D occupancy prediction task as follows: a model needs to jointly estimate the occupancy state and semantic label of every voxel in ...
- **p. 1 / Abstract - extractive body cue:** 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations.
- **p. 2 / 1 Introduction - extractive body cue:** The occupancy state of each voxel can be categorized as free, occupied, or unobserved.
- **p. 1 / Abstract - extractive body cue:** Furthermore, we provide an extensive analysis of the proposed dataset with various baseline models.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; ...
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network.
- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network.
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; ...
- **p. 1 / Abstract - extractive body cue:** Robotic perception requires the modeling of both 3D geometry and semantics.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in ... | p. 2 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | formalize, occupancy, prediction, task, follows, model, needs, jointly, estimate, state, semantic, label, every, voxel | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | formalize, occupancy, prediction, task, follows, model, needs, jointly, estimate, state | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | contributions, follows, introduce, Occ3D, high-quality, occupancy, prediction, benchmark, facilitate, research | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** We formalize the 3D occupancy prediction task as follows: a model needs to jointly estimate the occupancy state and semantic label of every voxel in ...
- **p. 1 / Abstract - extractive body cue:** 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations.
- **p. 2 / 1 Introduction - extractive body cue:** The occupancy state of each voxel can be categorized as free, occupied, or unobserved.
- **p. 1 / Abstract - extractive body cue:** Furthermore, we provide an extensive analysis of the proposed dataset with various baseline models.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Occ3D-Waymo contains 1,000 publicly available sequences in total, where 798 scenes are for training and 202 scenes are for validation. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Additionally, we conduct experiments using LiDAR as an input on the Waymo dataset. "LiDAR-Onl" refers to adopting single frame LiDAR as input. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Occ3D-Waymo contains 1,000 publicly available sequences in total, where 798 scenes are for training and 202 scenes are for validation. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Lastly, model, dubbed, Coarse-to-Fine, Occupancy, CTF-Occ, network, demonstrates, superior, performance, Occ3D, benchmarks, Additionally, transformer-based, prediction, contributions, follows, introduce, high-quality, benchmark.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo. | p. 8 (6 Experiments), p. 9 (6 Experiments) |
| Baseline harness | Our method outperforms previous methods by remarkable margins, increasing the mIoU by 1.97. | p. 10 (6 Experiments), p. 10 (6 Experiments) |
| Metric / failure reporting | For token selection, uncertain selection and top-k selection are on par and they significantly outperform the random selection as expected. | p. 10 (6 Experiments), p. 10 (6 Experiments) |

## Failure and Ablation Link

- **p. 9 / 6 Experiments - extractive body cue:** The voxel embedding will first pass through four encoder layers without token selection.
- **p. 10 / 6 Experiments - extractive body cue:** Without the OHEM loss, we only get 14.06 mIoU.
- **p. 10 / 6 Experiments - extractive body cue:** 6.3 Ablation study In this section, we ablate the choices of incremental token selection and OHEM loss.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: The architecture of CTF-Occ network. CTF-Occ consists of an image backbone, a coarse-to-fine voxel encoder, and an implicit occupancy decoder. in a scene ...
- **p. 9 / 6 Experiments - extractive body cue:** We replace their original detection decoders with the occupancy decoder adopted in our CTF-Occ network and remain their BEV feature encoders.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (1) 3D bounding box representation erases the geometric details of objects, a construction vehicle has a mechanical arm that protrudes from the main ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Our Occ3D dataset demonstrates rich semantic and geometric expressiveness. (a) Diversity of scenes in the Occ3D dataset; (b) Out-of-vocabulary objects, also known as ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), objective 본문 anchor 없음, temporal p. 8 (6 Experiments), p. 9 (6 Experiments), p. 3 (2 Related Work), p. 3 (2 Related Work), p. 4 (2 Related Work), p. 4 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
