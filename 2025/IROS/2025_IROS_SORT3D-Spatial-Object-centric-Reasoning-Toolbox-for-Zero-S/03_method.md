# Method - SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2504.18684; PDF retrieval source: https://arxiv.org/pdf/2504.18684. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D bounding boxes to be input into the LLM ...

## Method Body Digest

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D bounding boxes to ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. nightstand and bed), ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The usage of open-vocabulary 2D foundation models allows our semantic mapping module to generalize to new environments as we show in our real-world experiments (section ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The LLM is prompted with an in-context example to decompose a referential statement into a series of search calls and choose a single object ID ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** We use Qwen2-VL-7B [27] as our VLM as we found it to perform best in generating accurate and concise descriptions following our template, and the ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** For example, given the query "Find the computer near the desk with a printer on it", the LLM first calls find_below(desk, printer) returning [2], then ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 3D referential grounding additionally acts as a precursor to downstream tasks such as object-goal navigation, multi-action instruction-following, and scene visual question answering (VQA).
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown arXiv:2504.18684v2 [cs.CV] 15 Aug 2025
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** As a result, our method only requires a single in-context example of the toolbox usage and no other training data.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...

## Source Evidence Cues

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D bounding boxes to ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. nightstand and bed), ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The usage of open-vocabulary 2D foundation models allows our semantic mapping module to generalize to new environments as we show in our real-world experiments (section ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The LLM is prompted with an in-context example to decompose a referential statement into a series of search calls and choose a single object ID ...
- **Detected method headings:** III. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D ... | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. ... | p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The usage of open-vocabulary 2D foundation models allows our semantic mapping module to generalize to new environments as we show in our ... | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** We use Qwen2-VL-7B [27] as our VLM as we found it to perform best in generating accurate and concise descriptions following our template, and the ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The LLM is prompted with an in-context example to decompose a referential statement into a series of search calls and choose a single object ID ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** For example, given the query "Find the computer near the desk with a printer on it", the LLM first calls find_below(desk, printer) returning [2], then ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | referential, grounding, additionally, acts, precursor, downstream, tasks, object-goal, navigation, multi-action, instruction-following, scene, visual, question | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | referential, grounding, additionally, acts, precursor, downstream, tasks, object-goal, navigation, multi-action | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | SORT3D, Spatial, Object-centric, Reasoning, Toolbox, Grounding, LLMs, arXiv, Aug, result | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Qwen2-VL-7B, VLM, found, perform, best, generating, accurate, concise, descriptions, following | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 3D referential grounding additionally acts as a precursor to downstream tasks such as object-goal navigation, multi-action instruction-following, and scene visual question answering (VQA).
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The LLM is prompted with an in-context example to decompose a referential statement into a series of search calls and choose a single object ID ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. nightstand and bed), ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We finally leverage the strong semantic language and sequential reasoning priors of LLMs using chain-of-thought prompting [16] to parse a complex referential statement into a ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** For example, understanding statements such as "the chair closest to the closet door", is a task trivial for humans [1] but still challenging for robots.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** While humans are usually able to identify objects from referring expressions by filtering out irrelevant objects, reasoning about spatial relationships, and utilizing semantic object attributes, ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | As the robot moves and produces new observations, we associate per-frame object instance pointclouds using a 2D tracking module and 3D proximity ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We also deploy our full pipeline on two robotic ground vehicles for real-time indoor navigation, demonstrating our method's ability to further generalize ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Instance-level, Semantic, Mapping, real-world, experiments, object, instancelevel, module, running, real-time, obtain, bounding, boxes, input, LLM, spatial, reasoning, toolbox, Given, command.
- **Relevant PDF headings:** III. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and ... | p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (V. RESULTS AND DISCUSSION) |
| Semantic / temporal fusion | Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and ... | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (V. RESULTS AND DISCUSSION) |
| Robot query / planning handoff | On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy. | p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION) |

## Failure and Ablation Link

- **p. 6 / V. RESULTS AND DISCUSSION - extractive PDF cue:** Ablation of Captioning Module We evaluate the effect on grounding accuracy of adding open-vocabulary captions generated from 2D images of objects in the scene.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive PDF cue:** toolbox, which does not have to be from a particular dataset, and we employed no dataset-specific training or fine-tuning.
- **p. 6 / V. RESULTS AND DISCUSSION - extractive PDF cue:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive PDF cue:** In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that the sentence implies choosing a pillow on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), temporal p. 3 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
