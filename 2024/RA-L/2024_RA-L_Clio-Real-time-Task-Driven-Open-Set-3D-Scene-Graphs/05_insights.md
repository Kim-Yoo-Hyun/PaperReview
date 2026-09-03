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

- **Paper-specific interface:** To obtain semantic features for the places, we compute a CLIP embedding vector for each input image provided to Clio. (p. 5, IV. TASK-DRIVEN CLUSTERING).
- **Paper-specific mechanism:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once on entire graph takes approximately 30 ... (p. 7, VI. EXPERIMENTS); the relevant task/metric cue is We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated objects, total number of estimated objects ... (p. 6, VI. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the "Wrong Object" failure category). (p. 8, VI. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `3D Vision, Graph Reasoning`.
- **Reading predecessor in the generated track queue:** Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite the encouraging experimental results, our approach has multiple limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: To obtain semantic features for the places, we compute a CLIP embedding vector for each input image provided to Clio. (p. 5, IV. TASK-DRIVEN CLUSTERING); preserve the objective/update rule: As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) as a measure of the ... (p. 4, IV. TASK-DRIVEN CLUSTERING).
2. Use the paper-reported task/data/environment cue: For the Office, Apartment, and Cubicle datasets we manually annotate ground truth 3D bounding boxes for objects associated to the given set of tasks. (p. 6, VI. EXPERIMENTS).
3. Compare against the reported or matched baseline: In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, which is essentially Clio without ... (p. 6, VI. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated objects, total number of estimated objects ... (p. 6, VI. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, which is essentially Clio without ... (p. 6, VI. EXPERIMENTS); if none is reported, design one around: Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the "Wrong Object" failure category). (p. 8, VI. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), and measure the boundary at p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (To obtain semantic features for the places, we compute a CLIP embedding vector for each input image provided to Clio.), does the paper-specific mechanism (We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.) retain the reported evaluation outcome (We report the F1 score as the harmonic mean of osR and osP and include average IOU of ...) when tested against the paper's strongest explicit boundary (Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We report the F1 score as the harmonic mean of osR and osP and include average IOU of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once on entire graph takes approximately 30 ... (p. 7, VI. EXPERIMENTS).
- **Strongest explicit boundary:** Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the "Wrong Object" failure category). (p. 8, VI. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
