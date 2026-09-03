# Insights — From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fzmittHfq3; PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection ...
- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 4 / 3 Methodology - extractive body cue:** We introduce a lightweight fusion mechanism that aligns and combines these complementary representations (see Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 6 / 3 Methodology - extractive body cue:** These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM for extracting 3D ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 6 (3 Methodology)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.
- **p. 2 / 1 Introduction - extractive body cue:** These limitations now form a major bottleneck in developing reliable generalist robot policies.
- **p. 3 / 1 Introduction - extractive body cue:** To overcome limitation (3) of alignment challenges, we draw inspiration from the brain's division of labor.
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 9 / 4 Experiments - extractive body cue:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.
- **p. 11 / 5 Conclusion - extractive body cue:** In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial understanding.
- **p. 11 / 5 Conclusion - extractive body cue:** Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance and robustness on spatially demanding tasks.
- **Boundary to test:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | 3, FALCON achieves the highest average success rate of 70.0% across all nine task suites, outperforming the advanced method SpatialVLA [31] (44.4%) by 25.6%. | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Failure/limitation | For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. | p. 9 (4 Experiments), p. 11 (5 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t , . . . , In t } ... (p. 4, 3 Methodology).
- **Paper-specific mechanism:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. (p. 8, 4 Experiments); the relevant task/metric cue is FALCON achieves an overall success rate of 62.9%, surpassing all baseline methods. (p. 8, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. (p. 9, 4 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t , . . . , In t } ... (p. 4, 3 Methodology); preserve the objective/update rule: 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function over the predicted action horizon. (p. 5, 3 Methodology).
2. Use the paper-reported task/data/environment cue: All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data. (p. 8, 4 Experiments).
3. Compare against the reported or matched baseline: 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. (p. 8, 4 Experiments).
4. Report the body metric with its denominator and aggregation: FALCON achieves an overall success rate of 62.9%, surpassing all baseline methods. (p. 8, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: Kosmos-VLA (w/ rgb-d) is a point cloud-based variant where the ESM is replaced by a lightweight point cloud encoder [46] while retaining other parts. (p. 11, 4 Experiments); if none is reported, design one around: For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. (p. 9, 4 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 8 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), and measure the boundary at p. 9 (4 Experiments), p. 1 (Abstract).

## Falsifiable research question

Under the paper's stated interface (3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t ...), does the paper-specific mechanism (We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through ...) retain the reported evaluation outcome (FALCON achieves an overall success rate of 62.9%, surpassing all baseline methods.) when tested against the paper's strongest explicit boundary (For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (FALCON achieves an overall success rate of 62.9%, surpassing all baseline methods.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme. (p. 2, 1 Introduction).
- **Paper-supported outcome:** 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. (p. 8, 4 Experiments).
- **Strongest explicit boundary:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. (p. 9, 4 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
