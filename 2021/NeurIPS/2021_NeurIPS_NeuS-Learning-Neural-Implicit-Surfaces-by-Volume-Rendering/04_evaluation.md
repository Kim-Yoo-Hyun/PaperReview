# Evaluation - NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.10689; PDF retrieval source: https://arxiv.org/pdf/2106.10689. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 5. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 8 (4 Experiments), p. 20 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments)): COLMAP results are achieved by trim=0.

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** We further tested on 7 challenging scenes from the low-res set of the BlendedMVS dataset [48] (CC-4 License).
- **p. 7 / 4 Experiments - extractive body cue:** To evaluate our approach and baseline methods, we use 15 scenes from the DTU dataset [11], same as those used in IDR [49], with a ...
- **p. 10 / 4 Experiments - extractive body cue:** (b) COLMAP𝑡𝑟𝑖𝑚= 10 (c) COLMAP𝑡𝑟𝑖𝑚= 7 (a) Ours Reference Image Figure 8: Comparison on scenes with thin structure objects.
- **p. 10 / 4 Experiments - extractive body cue:** Furthermore, different from the methods [41, 20, 45, 21] which only target at high-quality thin structure reconstruction, our method can handle the scenes which have ...
- **p. 8 / 4 Experiments - extractive body cue:** The results show that our approach outperforms the baseline methods on the DTU dataset in both settings - w/ and w/o mask in terms of ...
- **p. 8 / 4 Experiments - extractive body cue:** We conduct the qualitative comparisons on the DTU dataset and the BlendedMVS dataset in both settings, w/ mask and w/o mask, in Figure 4 and ...
- **p. 9 / 4 Experiments - extractive body cue:** Our method works better for the objects with abrupt depth changes.
- **p. 8 / 4 Experiments - extractive body cue:** We measure the reconstruction quality with the Chamfer distances in the same way as UNISURF [31] and IDR [49] and report the scores in Table ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | COLMAP results are achieved by trim=0. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that our approach outperforms the baseline methods on the DTU dataset in both settings - w/ and w/o mask in terms ... | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: Quantitative comparisons with NeRF on the task of novel view synthesis without mask supervision. E.2 Novel View Synthesis In this experiment, we ... | p. 20 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the ... | p. 2 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that we use the qualitative results of UNISURF reported their paper for comparison. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** We further tested on 7 challenging scenes from the low-res set of the BlendedMVS dataset [48] (CC-4 License).
- **p. 7 / 4 Experiments - extractive body cue:** To evaluate our approach and baseline methods, we use 15 scenes from the DTU dataset [11], same as those used in IDR [49], with a ...
- **p. 10 / 4 Experiments - extractive body cue:** (b) COLMAP𝑡𝑟𝑖𝑚= 10 (c) COLMAP𝑡𝑟𝑖𝑚= 7 (a) Ours Reference Image Figure 8: Comparison on scenes with thin structure objects.
- **p. 10 / 4 Experiments - extractive body cue:** Furthermore, different from the methods [41, 20, 45, 21] which only target at high-quality thin structure reconstruction, our method can handle the scenes which have ...
- **p. 8 / 4 Experiments - extractive body cue:** The results show that our approach outperforms the baseline methods on the DTU dataset in both settings - w/ and w/o mask in terms of ...
- **p. 8 / 4 Experiments - extractive body cue:** We conduct the qualitative comparisons on the DTU dataset and the BlendedMVS dataset in both settings, w/ mask and w/o mask, in Figure 4 and ...
- **p. 9 / 4 Experiments - extractive body cue:** Our method works better for the objects with abrupt depth changes.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the top ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of (a) weight bias of naive solution, and (b) the weight function defined in our solution, which is unbiased in the first-order ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Illustration of weight distribution in case of multiple surface intersection. This is the formula of the opaque density ρ(t) in the ideal case ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Quantitative evaluation on DTU dataset. COLMAP results are achieved by trim=0.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Comparions on surface reconstruction with mask supervision. 8
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Comparions on surface reconstruction without mask supervision. with UNISURF [31] on two examples in the w/o mask setting. Note that we use the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Ablation studies. We show the qualitative results and report the quantitative metrics in Chamfer distance and MAE (mean absolute error) between the ground-truth ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7: Visual comparisons with UNISURF. We also studied the effect of Eikonal regulariza- tion [10] and geometric initialization [1]. With- out Eikonal regularization or ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We further tested on 7 challenging scenes from the low-res set of the BlendedMVS dataset [48] (CC-4 License). | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | To evaluate our approach and baseline methods, we use 15 scenes from the DTU dataset [11], same as those used in IDR [49], with ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3 Method), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We measure the reconstruction quality with the Chamfer distances in the same way as UNISURF [31] and IDR [49] and report the scores in ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We show the qualitative results and report the quantitative metrics in Chamfer distance and MAE (mean absolute error) between the ground-truth and predicted SDF ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Note that the reported scores of IDR in the setting of w/ mask and NeRF and UNISURF in the w/o mask setting are from ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| This is indicated by the MAE(mean absolute error) between the SDF predictions and corresponding ground-truth SDF, as shown in the bottom line of Figure ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Figure 11: The visualization of the level-set surfaces extracted from the NeRF results using different threshold values. NeRF[29]. To implement NeRF, we use the ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| (1) The state-of-the-art surface rendering approach - IDR [49]: IDR can reconstruct surface with high quality but requires foreground masks as supervision; Since IDR ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| As shown in Figure 6, the quantitative result of naive solution is worse than our weight choice (e) in terms of the Chamfer distance. | definition/direction/unit from same section | p. 9 (4 Experiments) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (1) The state-of-the-art surface rendering approach - IDR [49]: IDR can reconstruct surface with high quality but requires foreground masks as supervision; Since IDR ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| The results show that our approach outperforms the baseline methods on the DTU dataset in both settings - w/ and w/o mask in terms ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| More details of the baseline methods are included in the supplementary material. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Regarding the w/o mask setting, we visually compare our method with NeRF and COLMAP in the setting of w/o mask in Figure 5, which ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Figure 10: The section points and mid-points defined on a ray. D.2 Baselines IDR[49]. To implement IDR, we use their officially released codes2 and ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To evaluate the effect of the weight calculation, we test three different kinds of weight constructions described in Sec. | component/input/data sensitivity | p. 9 (4 Experiments) |
| We also studied the effect of Eikonal regularization [10] and geometric initialization [1]. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Each scene was tested with and without foreground masks provided by IDR [49]. | component/input/data sensitivity | p. 7 (4 Experiments) |
| 4.2 Comparisons We conducted the comparisons in two settings, with mask supervision (w/ mask) and without mask supervision (w/o mask). | component/input/data sensitivity | p. 8 (4 Experiments) |
| (e) Full Model Reference Image Chamfer Distance 0.59 0.62 1.49 (a) Naive Solution (b) Direct Solution 4.45 (c) w/o Eikonal 0.64 MAE 6.19 0.93 ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Without Eikonal regularization or geometric initialization, the result on Chamfer distance is on par with that of the full model. | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Therefore we propose a novel volume rendering scheme to ensure unbiased surface reconstruction in the first-order approximation of SDF. | COLMAP results are achieved by trim=0. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 20 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | The results show that our approach outperforms the baseline methods on the DTU dataset in both settings - w/ and w/o mask in terms ... | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** To evaluate our approach and baseline methods, we use 15 scenes from the DTU dataset [11], same as those used in IDR [49], with a ...
- **p. 8 / 4 Experiments - extractive body cue:** We sample 512 rays per batch and train our model for 300k iterations for 14 hours (for the ‘w/ mask' setting) and 16 hours (for ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation of our method is that although our method does not heavily rely on correspondence matching of texture features, the performance would still ... | p. 10 (5 Conclusion) |
| body limitation/failure cue | Figure 16: A failure reconstruction case containing textureless regions. Figure 16 shows a failure case where our method fails to correctly reconstruct the texutreless ... | p. 21 (Figure/Table caption) |
| body limitation/failure cue | As shown in Figure 4 for the setting of w/ mask, IDR shows limited performance for reconstructing thin metals parts in Scan 37 (DTU), ... | p. 8 (4 Experiments) |
| body limitation/failure cue | NeuS produces high-quality reconstruction and successfully reconstructs objects with severe occlusions and complex structures. | p. 10 (5 Conclusion) |
| body limitation/failure cue | Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: Illustration of (a) weight bias of naive solution, and (b) the weight function defined in our solution, which is unbiased in the ... | p. 4 (Figure/Table caption) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We sample 512 rays per batch and train our model for 300k iterations for 14 hours (for the ‘w/ mask' setting) and 16 hours ... | p. 8 (4 Experiments) |
| The MAE is computed on uniformly-sampled points in the object's bounding sphere. | p. 10 (4 Experiments) |
| We assume the point sampling size is n and the batch size is m. | p. 7 (3 Method) |
| Both functions are encoded by Multi-layer Perceptrons (MLP). | p. 3 (3 Method) |
| With NeuS, the scene of an object to be reconstructed is represented by two functions: f : R3 →R that maps a spatial position ... | p. 3 (3 Method) |
| The occlusion-aware property ensures that when a ray sequentially passes multiple surfaces, the rendering procedure will correctly use the color of the surface nearest ... | p. 4 (3 Method) |
| Upon successful minimization of a loss function based on this supervision, the zero-level set of the network-encoded SDF is expected to represent an accurately ... | p. 4 (3 Method) |
| Volume-rendering weight w(t)=T(t)ρ(t), accumulated transmittance T(t)=exp(−∫₀ᵗρ(u)du). | PDF p. 5 §3; rendering definition이며 metric 결과가 아님 |

## Limitations and Verification Questions

- **p. 10 / 5 Conclusion - extractive body cue:** One limitation of our method is that although our method does not heavily rely on correspondence matching of texture features, the performance would still degrade ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 16: A failure reconstruction case containing textureless regions. Figure 16 shows a failure case where our method fails to correctly reconstruct the texutreless region ...
- **p. 8 / 4 Experiments - extractive body cue:** As shown in Figure 4 for the setting of w/ mask, IDR shows limited performance for reconstructing thin metals parts in Scan 37 (DTU), and ...
- **p. 10 / 5 Conclusion - extractive body cue:** NeuS produces high-quality reconstruction and successfully reconstructs objects with severe occlusions and complex structures.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Illustration of the surface rendering and volume rendering. (b) A toy example of bamboo planter, where there are occlusions on the top ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of (a) weight bias of naive solution, and (b) the weight function defined in our solution, which is unbiased in the first-order ...

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), metrics p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 10 (4 Experiments), p. 19 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 18 (Figure/Table caption), results p. 8 (4 Experiments), p. 8 (4 Experiments), p. 20 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 9 (4 Experiments).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
