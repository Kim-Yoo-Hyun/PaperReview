# Insights — DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / 3.5. Method extensions - extractive body cue:** Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive body cue:** In the following, we present our method in three parts.
- **p. 2 / 1. Introduction - extractive body cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce 3D OV-SD, a new 3D semantic segmentation task providing adaptive segmentations based on scene context and user-defined queries.
- **p. 8 / 4.3.1. Open-Vocabulary Segmentation - extractive body cue:** We present quantitative outcomes in Table 3, first analyzing results for classes, followed by concepts.
- **p. 5 / 3.5. Method extensions - extractive body cue:** First, the projector requires at least one spatially precise feature field to perform segmentation (e.g., dense encoders).
- **p. 8 / 4.3.2. Unsupervised Semantic Segmentation - extractive body cue:** Since SmooSeg only produces 2D segmentations, we recover a 3D segmentation by training a Semantic-NeRF [39] on its outputs.
- **Contribution anchor:** p. 5 (3.5. Method extensions), p. 3 (3.1. Problem Statement and Overview), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 8 (4.3.1. Open-Vocabulary Segmentation), p. 5 (3.5. Method extensions)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** As illustrated in Figure 1, DiSCO-3D not only addresses OV-SD but also generalizes to its edge cases: 3D OV-Seg (when queries target a single sub-concept) ...
- **p. 2 / 1. Introduction - extractive body cue:** We present DiSCO-3D, the first method designed to solve the 3D OV-SD problem, combining Unsupervised Semantic Segmentation with Open-Vocabulary Segmentation guidance to serve as a ...
- **p. 3 / 3.1. Problem Statement and Overview - extractive body cue:** Discovery problem, specialized to the case of Neural Field [25] representations.
- **p. 5 / 4. Experimental evaluations - extractive body cue:** Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** The last column refers to the main experiment where the number of prototypes is fixed and does not depend on NGT .
- **Boundary to test:** Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as long as two conditions are met. | p. 5 (3.5. Method extensions), p. 3 (3.1. Problem Statement and Overview) |
| Reported outcome | Notice that the only difference between DiSCO-3D and those baselines relies on the fact that DiSCO-3D achieves USS and OVSeg jointly whereas the latters achieve it successively. | p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies) |
| Failure/limitation | Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations. | p. 5 (4. Experimental evaluations), p. 7 (4.2.3. Ablations studies) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Regarding GrowSP, although it succeeds in performing accurate segmentation, the global performances are lower, probably due to the input data modalities, as the discrete nature of point clouds may limit their expressiveness ...를 We evaluate DiSCO-3D on both real and synthetic data, demonstrating better performance than hand-designed naive baselines on the proposed OV-SD task and experimentally show that our solution produces state-of-the-art performances on the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) as long as two conditions are met.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We also display some qualitative examples in Figure 3 across various scenes (both indoor and outdoor from various datasets [12, 21, 33]), feature fields (LeRF and OpenNeRF), types of queries (textual, visual ....
3. Compare against the body-reported baseline or a matched simpler baseline: All quantitative experiments, including DiSCO3D and the comparative baselines, use the same pre-trained Nerfacto models and feature fields as input..
4. Report the body metric and its denominator/aggregation: First, we observe that the complete model's performance remains stable in both segmentation accuracy and the numFF Method PCLIP Hungarian PQ ↑ mIoU ↑ mAcc ↑ PQ ↑ mIoU ↑ mAcc ↑ ....
5. Re-run the body-reported ablation/failure condition: Sensitivity to Number of Prototypes and influence of Lproto..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.5. Method extensions), p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 5 (3.5. Method extensions); the primary result is directionally consistent at p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies), p. 5 (4.1. Implementation and evaluation details); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Although, present, pre-trained mechanism이 All quantitative experiments, including DiSCO3D and the comparative baselines, use the same pre-trained Nerfacto models and ... 대비 First, we observe that the complete model's performance remains stable in both segmentation accuracy and the numFF Method ...을 개선하고, Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
