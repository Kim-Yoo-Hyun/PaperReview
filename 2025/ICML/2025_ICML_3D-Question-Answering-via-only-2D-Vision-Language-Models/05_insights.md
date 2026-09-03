# Insights — 3D Question Answering via only 2D Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=IkhJApkJQ3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168051. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views ...
- **p. 1 / 1. Introduction - extractive body cue:** All of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning. a4 is our method that leverages pre-trained LVLMs operating ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) We introduce cdViews that integrates a viewSelector with a viewNMS to capture critical and diverse views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...
- **p. 3 / 3. Preliminaries - extractive body cue:** Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D ...
- **p. 2 / 1. Introduction - extractive body cue:** To train this module, we design a viewAnnotator that automatically generates training data in two steps. viewAnnotator firstly converts question-answer pairs into descriptive captions.
- **p. 6 / 3. Preliminaries - extractive body cue:** Views are classified as "uncertain" when the model chooses the option of "Uncertain, insufficient or unclear information" or outputs none of the given options, and ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 2 (1. Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, both approaches have significant limitations, either being inefficient or failing to capture critical views.
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges, we introduce a new framework cdViews to select critical and diverse Views <Question>: What is the black couch facing? <Answer>: Coffee ...
- **p. 5 / 3. Preliminaries - extractive body cue:** It relies on the semantic similarity between questions and views, which introduces two key limitations: 1) Missing Critical Views.
- **p. 5 / 3. Preliminaries - extractive body cue:** This limitation stems from the fundamental difference between object identification and relationship comprehension, and the latter requiring stronger understanding capabilities.
- **p. 4 / 3. Preliminaries - extractive body cue:** In the following, we first present a problem formulation for zero-shot 3D-QA, followed by experiments using two intuitive view selection methods: uniform sampling and image ...
- **p. 7 / 5.1. Comparisons with the State-of-the-Arts - extractive body cue:** The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy ...
- **Boundary to test:** The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy views.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views based on their potential to provide answer-specific ... | p. 1 (Abstract), p. 1 (1. Introduction) |
| Reported outcome | Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In Step 1, LVLMs processes question-answer pairs to ... | p. 5 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Failure/limitation | The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy views. | p. 7 (5.1. Comparisons with the State-of-the-Arts) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 It takes the question embedding Q and the visual embedding set {Vi}N i=1 as input and outputs a binary label ˆSi (0 or 1) for each visual embedding.를 Since 2D LVLMs are fundamentally designed to process 2D images as input, we propose cdViews to efficiently select the most informative 2D views of 3D scenes.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy views.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views based on their potential to provide answer-specific ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The reason is that the uniform sampling method ignores the question and the image retrieval method often fails to capture critical views or introduces redundancy views.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects)..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by light green boxes indicating outputs at each step). In Step 1, LVLMs processes question-answer pairs to ....
4. Report the body metric and its denominator/aggregation: Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) and SQA (Ma et al., 2022). For ScanQA, scores are presented in the format ....
5. Re-run the body-reported ablation/failure condition: ScanQA contains over 41K question-answer annotations across 800 indoor 3D scenes, which are divided into train, val, and test sets (with or without objects)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1. Introduction), p. 6 (3. Preliminaries), p. 2 (1. Introduction); the primary result is directionally consistent at p. 5 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 cdViews, novel, automatically mechanism이 Figure 5: Our viewAnnotator module operates in two steps: Caption Generation and View Matching (illustrated by ... 대비 Table 1: Performance comparisons with the state-of-the-art methods on the test set of ScanQA (Azuma et al., 2022) ...을 개선하고, The reason is that the uniform sampling method ignores the question and the image retrieval method ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
