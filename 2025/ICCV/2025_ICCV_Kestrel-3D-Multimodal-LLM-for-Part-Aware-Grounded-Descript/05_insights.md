# Insights — Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed ...
- **p. 2 / 1. Introduction - extractive body cue:** To tackle the challenges posed by PaPGD, we propose Kestrel, a novel part-aware 3D MLLM designed to capture the intricate spatial and compositional details required ...
- **p. 3 / 4. Method - extractive body cue:** To bridge this gap, we propose Kestrel, which combines a 3D MLLM with a query refinement mechanism to enable fine-grained part segmentation along with detailed ...
- **p. 4 / 4.1. Kestrel - extractive body cue:** We introduce projector P1 to align the latent space of language and 3D vision.
- **p. 6 / Model - extractive body cue:** In addition, we propose a new evaluation for the 3D CompositionAware Language Comprehension (3D-CALC) capabilities of 3D MLLMs.
- **p. 4 / 4.1. Kestrel - extractive body cue:** As shown in Figure 2, Kestrel is composed of a point encoder, an LLM, a point feature propagation module (PFPM), and a segmentation decoder.
- **p. 4 / 4.1. Kestrel - extractive body cue:** Each upsampled feature is combined with intermediate segmentation decoder queries, qi(i ↑{1, 2}), which will be projected through an MLP and then combined by a ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method), p. 4 (4.1. Kestrel), p. 6 (Model), p. 4 (4.1. Kestrel)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, a critical limitation persists: existing 3D MLLMs often fail to capture the fine-grained details of object parts and their material properties, which are essential ...
- **p. 1 / 1. Introduction - extractive body cue:** Both armrests are also leather with a sleek black finish, matching the seat support, which is made of leather in brown.
- **p. 2 / 1. Introduction - extractive body cue:** These breakthroughs have spurred a growing trend to adapt MLLMs for 3D applications [22-24, 46, 56, 64] to bridge the gap between human and machine ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model ...
- **p. 8 / 6. Conclusion - extractive body cue:** Our work establishes a robust benchmark for part-aware 3D vision-language understanding, paving the way for future research in finegrained 3D object interaction and grounding.
- **p. 5 / 5. Experiments - extractive body cue:** 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Real-Word Demos. Kestrel shows a certain degree of robustness to noisy and incomplete real-world inputs. # Refinement Levels Grounded Desc. Direct Segmentation Reasoning ...
- **Boundary to test:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model cannot be evaluated. Models marked with * ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed object understanding through materialaware, part-level segmentation an ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | 5.2 investigates the performance of Kestrel in single-part grounding from both direct segmentation (3DCoMPaT-GrIn and PartNetMobility [63]) and reasoning segmentation perspectives (3DCoMPaT-GrIn and RPSeg3D [26]). | p. 5 (5. Experiments), p. 5 (Figure/Table caption) |
| Failure/limitation | Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model cannot be evaluated. Models marked with * ... | p. 6 (Figure/Table caption), p. 8 (6. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The point encoder and LLM take a point-aware instruction and point cloud as input, generating a detailed part-level description of the point cloud.를 The 3D Segmentation Decoder extracts the output embedding of the [SEG] token from the output hidden states of the 3D MLLM.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model cannot be evaluated. Models marked with * ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We introduce Part-Aware Point Grounded Description (PaPGD), a novel task that challenges 3D MLLMs to achieve detailed object understanding through materialaware, part-level segmentation an ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. Results marked with ! indicate metrics for the model cannot be evaluated. Models marked with * ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 5.4, we showcase the robustness and potential applications of Kestrel when the point cloud distribution deviates from the training data, including scenarios where the point clouds are collected from noisy real-world environments..
3. Compare against the body-reported baseline or a matched simpler baseline: We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design choices, as detailed in Sec..
4. Report the body metric and its denominator/aggregation: Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on 3DCoMPaT-GrIn. ing. We pretrain Kestrel on PointLLM's dataset[64] and 3DCoMPaT-GrIn's point c ....
5. Re-run the body-reported ablation/failure condition: Table 5. Ablation on the query refinement levels. Evaluates the effect of changing the number of query refinement stages on the mIoU performance of each task segments parts such as the pulling ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. Kestrel), p. 4 (4.1. Kestrel), p. 3 (4. Method); the primary result is directionally consistent at p. 5 (5. Experiments), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 We conduct ablation experiments on our training strategy and Kestrel to explore the effects of design ... 대비 Table 2. 3D Composition-Aware Language Comprehension (3D-CALC). Part, material, and composition understanding eval- uated based on accuracy on ...을 개선하고, Table 1. Part-Aware Point Grounded Description Results. Comparison of models on language understanding and multi-part grounding. ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
