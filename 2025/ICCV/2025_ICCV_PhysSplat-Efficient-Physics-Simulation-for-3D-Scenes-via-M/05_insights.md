# Insights — PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (5 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/supplemental/Zhao_PhysSplat_Efficient_Physics_ICCV_2025_supplemental.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. 3D Open-vocabulary Segmentation - extractive body cue:** By leveraging the capabilities of these robust expert models, our method enables the automatic labeling of an entire image.
- **p. 3 / 7. More Details about Material Point Method - extractive body cue:** MPM consists of two primary phases: 1) Particle-to-Grid (P2G) Transfer: Particles transfer their properties to the grid, enabling the computation of global quantities such as ...
- **p. 4 / 7. More Details about Material Point Method - extractive body cue:** More visual results of our method. \m a t hb f {F}_p ^ {n+ 1} = (\mathbf {I} + \Delta t \mathbf {C}_p^{n+1}) \mathbf {F}_p^n.
- **p. 2 / 1. 3D Open-vocabulary Segmentation - extractive body cue:** In addition to the existing Gaussian properties, we introduce a new parameter, semantic attribute, to each Gaussian.
- **p. 3 / 7. More Details about Material Point Method - extractive body cue:** This dual transfer mechanism allows MPM to efficiently handle large deformations and complex interactions in continuum materials.
- **p. 2 / 2. Implementation Details for Baselines - extractive body cue:** For PhysDreamer, we used the pre-trained models provided in the official code repository1, as the training code is not made available.
- **p. 2 / 2. Implementation Details for Baselines - extractive body cue:** The trained models are then used for qualitative evaluation.
- **Contribution anchor:** p. 2 (1. 3D Open-vocabulary Segmentation), p. 3 (7. More Details about Material Point Method), p. 4 (7. More Details about Material Point Method), p. 2 (1. 3D Open-vocabulary Segmentation), p. 3 (7. More Details about Material Point Method), p. 2 (2. Implementation Details for Baselines)

### Strongest assumption and failure boundary

- **p. 2 / 1. 3D Open-vocabulary Segmentation - extractive body cue:** In addition to the existing Gaussian properties, we introduce a new parameter, semantic attribute, to each Gaussian.
- **p. 2 / 1. 3D Open-vocabulary Segmentation - extractive body cue:** Inspired by prior successful works, we innovatively introduce the integration of 2D open-vocabulary detector models, such as Grounding DINO, promptable 2D segmentation models, such as ...
- **p. 5 / 8. Analysis of Failure Cases - extractive body cue:** As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with occluded objects.
- **p. 3 / 6. More Analysis about Material Property Dis - extractive body cue:** This approach has the potential to further enhance the performance of our model and represents a direction for our future work.
- **Boundary to test:** As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with occluded objects.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | By leveraging the capabilities of these robust expert models, our method enables the automatic labeling of an entire image. | p. 2 (1. 3D Open-vocabulary Segmentation), p. 3 (7. More Details about Material Point Method) |
| Reported outcome | This approach has the potential to further enhance the performance of our model and represents a direction for our future work. | p. 3 (6. More Analysis about Material Property Dis), p. 3 (Figure/Table caption) |
| Failure/limitation | As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with occluded objects. | p. 5 (8. Analysis of Failure Cases), p. 3 (6. More Analysis about Material Property Dis) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Specifically, given an input image, we first employ an image tagging model, RAM to get the tags of the image.를 The integrated 2D openvocabulary model can automatically segment objects within images without the need for any textual input.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with occluded objects.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: By leveraging the capabilities of these robust expert models, our method enables the automatic labeling of an entire image.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `3D Vision, Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with occluded objects.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Sim Anything may struggle to segment the entire object, resulting in unnatural simulations..
3. Compare against the body-reported baseline or a matched simpler baseline: In this section, we elaborate on the implementation details of baselines used for comparison to our proposed method..
4. Report the body metric and its denominator/aggregation: Figure 1. The whole pipeline for 3D Open-vocabulary Segmentation. mentioned in our Supp.Mat, we provided video clips and asked the participants to give each video a score (RS) by anonymous questionnaire. A ....
5. Re-run the body-reported ablation/failure condition: As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with occluded objects..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (2. Implementation Details for Baselines), p. 3 (7. More Details about Material Point Method), p. 2 (2. Implementation Details for Baselines); the primary result is directionally consistent at p. 3 (6. More Analysis about Material Property Dis), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 leveraging, capabilities, robust mechanism이 In this section, we elaborate on the implementation details of baselines used for comparison to our ... 대비 Figure 1. The whole pipeline for 3D Open-vocabulary Segmentation. mentioned in our Supp.Mat, we provided video clips and ...을 개선하고, As noted in our limitation, segmentation failure can be a bottleneck, especially in complex environments with ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
