# Insights — Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting, together with a joint optimization scheme, to further steer the student toward accurate surfaces from ...
- **p. 3 / 3. Method - extractive body cue:** Our framework integrates Gaussian Splatting with UDF learning via a band-limited distillation scheme: a frozen local-shape UDF teacher ut provides supervision in a narrow nearsurface ...
- **p. 3 / 3. Method - extractive body cue:** Rendering proceeds by projecting each Gaussian onto the image plane and compositing its contribution in frontto-back order.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** Furthermore, the overall distillation formulation offers several advantages: it simplifies the learning task by limiting the geometric complexity within each patch, enables effective reuse of ...
- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model for distillation, denoted ...
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** To integrate this patch-based UDF prior into the 3DGS optimization, we use it to regularize the student UDF model fs.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.3. Band-limited Knowledge Distillation), p. 3 (3.2. Learning Patch-based UDF Priors)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with ...
- **p. 1 / 1. Introduction - extractive body cue:** Surface reconstruction from multi-view images is a fundamental problem in computer vision and graphics.
- **p. 2 / 1. Introduction - extractive body cue:** First, the teacher is supervised by real geometric ground-truth rather than relying only on photometric cues, which provide accurate UDF targets for Gaussian primitives and ...
- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further ...
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** It is well known that learning unsigned distance functions (UDFs) is intrinsically more challenging than learning signed distance fields (SDFs), due to sign ambiguity and ...
- **Boundary to test:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further enforce structural coherence and enhance reconstruction completeness.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Among UDF-based approaches, our model further achieves competitive runtime 4897 | p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset) |
| Failure/limitation | In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further enforce structural coherence and enhance reconstruction completeness. | p. 8 (5. Conclusion), p. 8 (4.3. DTU Dataset) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ...를 Our goal is to reconstruct accurate, geometrically consistent open surfaces from calibrated multi-view images.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further enforce structural coherence and enhance reconstruction completeness.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further enforce structural coherence and enhance reconstruction completeness.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction..
3. Compare against the body-reported baseline or a matched simpler baseline: As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), Gaussian-based methods without explicit distance fields (3DGS [24], ....
4. Report the body metric and its denominator/aggregation: Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3)..
5. Re-run the body-reported ablation/failure condition: Figure 4. Ablation study on the DTU [51]. report the numbers from the original papers [29, 32, 45, 61]. Our experiments follow [29] for surface extraction. To en- sure fairness, all other ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.3. Band-limited Knowledge Distillation); the primary result is directionally consistent at p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset), p. 8 (4.3. DTU Dataset); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, follows mechanism이 As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared ... 대비 Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ...을 개선하고, In future work, we plan to extend the framework to handle sparse setting and dynamic scenes ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
