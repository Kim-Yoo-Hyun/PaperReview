# Insights — SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2504.18684; PDF retrieval source: https://arxiv.org/pdf/2504.18684. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As a result, our method only requires a single in-context example of the toolbox usage and no other training data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** This component is the only pipeine change required for our method to be deployed in the real-world.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D bounding boxes to ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. nightstand and bed), ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, training end-to-end learning-based methods on 3D referential grounding requires a large amount of annotated data aligning language references to a 3D scene, which the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also deploy our full pipeline on two robotic ground vehicles for real-time indoor navigation, demonstrating our method's ability to further generalize to previously unseen ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that the sentence implies choosing a pillow on ...
- **Boundary to test:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable model failure points by analyzing its chain ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | On Sr3D, SORT3D surpasses SOTA supervised training methods and achieves close overall performance to Transcrib3D while surpassing it in view-dependent accuracy. | p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION) |
| Failure/limitation | We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable model failure points by analyzing its chain ... | p. 6 (V. RESULTS AND DISCUSSION), p. 6 (V. RESULTS AND DISCUSSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 3D referential grounding additionally acts as a precursor to downstream tasks such as object-goal navigation, multi-action instruction-following, and scene visual question answering (VQA).를 The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable model failure points by analyzing its chain ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable model failure points by analyzing its chain ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to SOTA baselines..
3. Compare against the body-reported baseline or a matched simpler baseline: Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset of IRef-VLA using ScanNet scenes and compare to SOTA baselines..
4. Report the body metric and its denominator/aggregation: For our methods, we conduct multiple trials on each data split to measure variance in LLMs, reported with standard deviation values on the grounding accuracy, which we note that other LLM-based methods ....
5. Re-run the body-reported ablation/failure condition: Ablation of Captioning Module We evaluate the effect on grounding accuracy of adding open-vocabulary captions generated from 2D images of objects in the scene..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY); the primary result is directionally consistent at p. 6 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION), p. 5 (V. RESULTS AND DISCUSSION); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 SORT3D, Spatial, Object-centric mechanism이 Referential Grounding on Benchmark Datasets We test our model on both ReferIt3D subsets and the subset ... 대비 For our methods, we conduct multiple trials on each data split to measure variance in LLMs, reported with ...을 개선하고, We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
