# Insights — Clio: Real-time Task-Driven Open-Set 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2404.13696; PDF retrieval source: https://arxiv.org/pdf/2404.13696. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.
- **p. 2 / Abstract - extractive body cue:** Our final contribution is an extensive experimental campaign showing that Clio not only allows real-time construction of compact open-set 3D scene graphs, but also improves ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our third contribution (Section V) is to include the proposed task-driven clustering algorithm into a real-time system, named Clio (Fig.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our second contribution (Section IV) is to apply the Agglomerative IB algorithm from [14] to the problem of taskdriven 3D scene understanding.
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** In this section, we first provide relevant background on the Agglomerative IB, then present an incremental version of the Agglomerative IB algorithm to support real-time ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches use a class-agnostic segmentation network [10] (SegmentAnything or SAM) to generate fine-grained segments of the image and then apply a foundation model [11] ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (Abstract), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 4 (IV. TASK-DRIVEN CLUSTERING)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** This problem can be naturally formulated using the classical Information Bottleneck (IB) [13] theory, which also provides algorithmic approaches for task-driven clustering.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In order to overcome these limitations, a new set of approaches [8, 9] has begun to leverage vision-language foundation models for open-set semantic understanding.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Contrary to current approaches for open-set 3D scene graph construction (e.g., [9]) which are restricted to off-line operation when querying large vision-language models (VLMs) [15] ...
- **p. 8 / VII. LIMITATIONS - extractive body cue:** Despite the encouraging experimental results, our approach has multiple limitations.
- **p. 8 / VII. LIMITATIONS - extractive body cue:** First, while our method is zero-shot and is not bound to any particular foundation model, it does inherit some limitations from the foundation models used ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-Set Object Evaluation While Clio is designed for open-set detection, we include results on the closed-set Replica [17] dataset using the evaluation method performed by ...
- **Boundary to test:** Despite the encouraging experimental results, our approach has multiple limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. | p. 2 (I. INTRODUCTION), p. 2 (Abstract) |
| Reported outcome | Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot failed to actually grasp a correctly identified object. | p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Failure/limitation | Despite the encouraging experimental results, our approach has multiple limitations. | p. 8 (VII. LIMITATIONS), p. 8 (VII. LIMITATIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 Our key observation is that if the graph of primitives in input to the algorithm has multiple connected components (e.g., 3D object segments in different rooms), then the clustering can we performed ...를 Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of tasks, specified in natural language, and is required to build ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Despite the encouraging experimental results, our approach has multiple limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `3D Vision, Graph Reasoning`.
- **Reading predecessor in the generated track queue:** Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite the encouraging experimental results, our approach has multiple limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: During the experiments, the robot constructs a map with Clio in real-time while exploring a scene, and then is tasked to navigate to and pick up objects matching a provided natural language ....
3. Compare against the body-reported baseline or a matched simpler baseline: In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, which is essentially Clio without the Information ....
4. Report the body metric and its denominator/aggregation: We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated objects, total number of estimated objects (Objs), and ....
5. Re-run the body-reported ablation/failure condition: In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, which is essentially Clio without the Information ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION); the primary result is directionally consistent at p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Clio, novel, building mechanism이 In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic ... 대비 We report the F1 score as the harmonic mean of osR and osP and include average IOU of ...을 개선하고, Despite the encouraging experimental results, our approach has multiple limitations. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
