# Insights — ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.
- **p. 2 / 1. Introduction - extractive body cue:** To achieve open-vocabulary 3D visual grounding and reasoning, this paper proposes ReasonGrounder, a novel LVLM-Guided Hierarchical Feature Splatting method that enables implicit instruction comprehension and ...
- **p. 6 / Method - extractive body cue:** To extract language features from each image, we use the OpenCLIP ViT-B/16 model.
- **p. 6 / Method - extractive body cue:** We then train the hierarchical feature Gaussian field by fixing all other parameters of the 3D Gaussians.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (Method), p. 6 (Method)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Existing 3D visual grounding (3DVG) methods [7, 12, 13, 36] face challenges in open-vocabulary grounding and reasoning, primarily due to reliance on 3D annotations [37, ...
- **p. 2 / 1. Introduction - extractive body cue:** However, challenges remain in interpreting user intent and handling occlusions during object localization.
- **p. 1 / 1. Introduction - extractive body cue:** In a given scene, the user observes from a perspective with occlusions and asks questions such as: "Can you localize the red, round, sweet fruit ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is ...
- **p. 5 / 4. Experiments - extractive body cue:** The dataset features multiple object instances with varying levels of occlusion, making it ideal for evaluating the ability in open-vocabulary 3D reasoning, grounding, and amodal ...
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** Existing openvocabulary 3D visual grounding methods struggle with localizing complete objects in novel views with occlusion, limiting their real-world applicability.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive body cue:** To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from ...
- **Boundary to test:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Our results show that ReasonGrounder outperforms 2D-based methods like ODISE [35] and OV-Seg [25], and significantly surpasses 3D-based methods, including Method bed bench room sofa lawn overall LSeg [22] 56.0 6.0 19.2 ... | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning) |
| Failure/limitation | Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the ... | p. 6 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 LVLM aids in interpreting complex instructions and locating objects even when partially or fully occluded. • (4) Dataset Contributions: A new ReasoningGD dataset offers over 10K complex scenes with 2 million annotations, ...를 For instance, simple commands like apple can be directly interpreted, while more complex instructions, such as Can you localize the red, round, sweet fruit on the table that is partially occluded by ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, grounding, LVLM`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This paper introduces a novel dataset, ReasoningGD, which includes over 10K scenes of varying complexity and more than 263 types of common objects, with around 2 million annotations..
3. Compare against the body-reported baseline or a matched simpler baseline: Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods..
4. Report the body metric and its denominator/aggregation: Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is deemed successful if the pixel with the ....
5. Re-run the body-reported ablation/failure condition: Table 7. Ablation studies. The results are presented for two dif- ferent scenes: the Figurines scene from the LERF dataset and the 001 scene from the proposed ReasoningGD dataset. tion with implicit ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (Method), p. 6 (Method); the primary result is directionally consistent at p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Furthermore, introduce, novel mechanism이 Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods. 대비 Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same ...을 개선하고, Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
