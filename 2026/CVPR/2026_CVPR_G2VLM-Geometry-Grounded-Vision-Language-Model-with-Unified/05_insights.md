# Insights — G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive body cue:** We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and ...
- **p. 4 / 3. Unified Spatial Vision-Language Model - extractive body cue:** We introduce G2VLM, a unified geometry-grounded VLM that integrates spatial 3D reconstruction and spatial understanding.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** Our model's input is a sequence (Ii)N i=1 of N RGB images Ii ∈R3×H×W , we present the detailed design for each expert as follows.
- **p. 4 / 3.1. Model Architecture - extractive body cue:** As illustrated in Figure 3, G2VLM adopts a Mixture-ofTransformer-Experts (MoT) architecture [16] that consists of two transformer experts-one geometry perception expert dedicated to visual geometry ...
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive body cue:** For joint-training, we use AdamW optimizer for 16K iterations with a lr of 2e-5 on 64 A800 GPUs over 3 days.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3. Unified Spatial Vision-Language Model), p. 4 (3.1. Model Architecture), p. 4 (3.1. Model Architecture)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** We argue that this limitation stems from how current VLMs acquire their physical world knowledge.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this limitation, we propose to integrate visual geometry learning into the VLM.
- **p. 3 / 1. Introduction - extractive body cue:** Then turn right, go straight pass the boxes to get to the black monitor.
- **p. 8 / 5. Conclusion - extractive body cue:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive body cue:** We leave the scaling of our model to future work, as this is a promising direction to unlock even stronger performance.
- **p. 7 / 4.1. Visual Geometry Results - extractive body cue:** These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior or ...
- **Boundary to test:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in a single vision-language model. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over the baselines. Notably, it con- firms a ... | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results) |
| Failure/limitation | While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models. | p. 8 (5. Conclusion), p. 7 (4.2. Spatial Understanding & Reasoning Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 (1) where Ti ∈SE(3) ⊂R4×4 is the camera pose, Xi ∈ RH×W ×3 is the associated pixel-aligned 3D point map represented in its own camera coordinate system, each corresponding to the input ...를 On visual geometry tasks, G2VLM achieves competitive results against state-of-theart (SOTA) feed-forward 3D reconstruction models, such as VGGT [52], across depth estimation, point estimation, and camera pose estimation tasks.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding in a single vision-language model.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `VLM, 3D reconstruction, spatial reasoning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D [44] datasets..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over the baselines. Notably, it con- firms a ....
4. Report the body metric and its denominator/aggregation: These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy..
5. Re-run the body-reported ablation/failure condition: Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over the baselines. Notably, it con- firms a ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Model Architecture), p. 5 (3.3. Spatial Reasoning Learning), p. 4 (3.1. Model Architecture); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. ... 대비 These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy.을 개선하고, While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
