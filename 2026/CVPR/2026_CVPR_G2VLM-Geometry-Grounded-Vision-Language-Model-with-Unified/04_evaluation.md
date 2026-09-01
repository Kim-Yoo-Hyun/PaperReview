# Evaluation - G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 5 (Figure/Table caption)): Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over the baselines. Notably, it con- ...

## Evaluation Body Digest

- **p. 6 / 4.1. Visual Geometry Results - extractive PDF cue:** Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D [44] datasets.
- **p. 6 / 4.1. Visual Geometry Results - extractive PDF cue:** Following the methodology of [55, 57, 62], we evaluate our method on monocular depth estimation task using the Sintel [7] and NYU-V2 [46] datasets.
- **p. 7 / 4.1. Visual Geometry Results - extractive PDF cue:** G2VLM effectively reconstructs a diverse set of open-domain images, spanning object-level, structure-level, indoor, and outdoor scenes, including both dynamic and static content.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive PDF cue:** We evaluate our model on comprehensive spatial understanding and reasoning benchmarks, including SPARBench [79], OmniSpatial [24], MindCube [73] (spatial mental modeling), and OST-Bench [33] (online ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate our method across a wide range of spatial tasks.
- **p. 7 / 4.1. Visual Geometry Results - extractive PDF cue:** These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy.
- **p. 6 / 4.1. Visual Geometry Results - extractive PDF cue:** We report the Absolute Relative Error (Abs Rel) and the prediction accuracy at a threshold of δ < 1.25.
- **p. 7 / 4.1. Visual Geometry Results - extractive PDF cue:** Consistent with prior works [4, 51, 55, 57], we report Accuracy (Acc.) and Completion (Comp.) in Table 1a.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Visual Geometry Results (p. 6); 4.2. Spatial Understanding & Reasoning Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach ... | p. 8 (Figure/Table caption) |
| 4.1. Visual Geometry Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy. | p. 7 (4.1. Visual Geometry Results) |
| 4.1. Visual Geometry Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 1a, our method achieves on-par performance on the RRA and RTA metrics and comparable results on the AUC metric when ... | p. 7 (4.1. Visual Geometry Results) |
| 4.1. Visual Geometry Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As demonstrated in Table 1a, our method achieves on-par performance with SOTA multi-frame feed-forward reconstruction approaches, such as VGGT and π3. | p. 6 (4.1. Visual Geometry Results) |
| 4.1. Visual Geometry Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report the Absolute Relative Error (Abs Rel) and the prediction accuracy at a threshold of δ < 1.25. | p. 6 (4.1. Visual Geometry Results) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Visual Geometry Results - extractive PDF cue:** Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D [44] datasets.
- **p. 6 / 4.1. Visual Geometry Results - extractive PDF cue:** Following the methodology of [55, 57, 62], we evaluate our method on monocular depth estimation task using the Sintel [7] and NYU-V2 [46] datasets.
- **p. 7 / 4.1. Visual Geometry Results - extractive PDF cue:** G2VLM effectively reconstructs a diverse set of open-domain images, spanning object-level, structure-level, indoor, and outdoor scenes, including both dynamic and static content.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive PDF cue:** We evaluate our model on comprehensive spatial understanding and reasoning benchmarks, including SPARBench [79], OmniSpatial [24], MindCube [73] (spatial mental modeling), and OST-Bench [33] (online ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate our method across a wide range of spatial tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present G2VLM, a geometry grounded vision-language model proficient in both spatial 3D reconstruction and spatial understanding tasks. For spatial reasoning questions, G2VLM ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Our model, G2VLM, employs an architecture inspired by the two-streams hypothesis. It features two experts: a geomet- ric perception expert (our "where pathway") ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of three different loss supervision mecha- nisms for the joint-training stage. Note that for visual geometry scores, lower is better. The VG ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison with mainstream feed-forward 3D reconstruction methods on visual geometry tasks and with representative VLMs on spatial understanding and reasoning tasks. Our model ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative results of our model. G2VLM effectively reconstructs a diverse set of open-domain images, spanning object-level, structure-level, indoor, and outdoor scenes, including both ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Experimental study results. (a) The dual encoder design, with both a semantic-rich CLIP encoder and a low-level vision DINO encoder, yields the best ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach over ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following the evaluation settings in [55, 62], we evaluate the quality of reconstructed multiview point maps on the 7-Scenes [45] and ETH3D [44] datasets. | embodiment, simulator version and control stack | p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results) |
| Task/environment | Following the methodology of [55, 57, 62], we evaluate our method on monocular depth estimation task using the Sintel [7] and NYU-V2 [46] datasets. | reset, timeout, object/scene variation | p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.1. Model Architecture), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3.1. Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy. | definition/direction/unit from same section | p. 7 (4.1. Visual Geometry Results) |
| We report the Absolute Relative Error (Abs Rel) and the prediction accuracy at a threshold of δ < 1.25. | definition/direction/unit from same section | p. 6 (4.1. Visual Geometry Results) |
| Consistent with prior works [4, 51, 55, 57], we report Accuracy (Acc.) and Completion (Comp.) in Table 1a. | definition/direction/unit from same section | p. 7 (4.1. Visual Geometry Results) |
| Figure 4. Comparison of three different loss supervision mecha- nisms for the joint-training stage. Note that for visual geometry scores, lower is better. The ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| As demonstrated in Table 1a, our method achieves on-par performance with SOTA multi-frame feed-forward reconstruction approaches, such as VGGT and π3. | definition/direction/unit from same section | p. 6 (4.1. Visual Geometry Results) |
| For visual geometry, we evaluate on monocular depth estimation, point map estimation, and camera pose estimation 9539 | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Figure 6. Experimental study results. (a) The dual encoder design, with both a semantic-rich CLIP encoder and a low-level vision DINO encoder, yields the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 3. We present G2VLM, a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| As shown in Table 1a, our method achieves on-par performance on the RRA and RTA metrics and comparable results on the AUC metric when ... | comparison identity and matched condition | p. 7 (4.1. Visual Geometry Results) |
| When compared with spatial expert models, G2VLM-SR also achieves the best results on all four spatial benchmarks, despite its relatively small 2B size. | comparison identity and matched condition | p. 7 (4.2. Spatial Understanding & Reasoning Results) |
| As demonstrated in Table 1a, our method achieves on-par performance with SOTA multi-frame feed-forward reconstruction approaches, such as VGGT and π3. | comparison identity and matched condition | p. 6 (4.1. Visual Geometry Results) |
| Figure 4. Comparison of three different loss supervision mecha- nisms for the joint-training stage. Note that for visual geometry scores, lower is better. The ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 1. Comparison with mainstream feed-forward 3D reconstruction methods on visual geometry tasks and with representative VLMs on spatial understanding and reasoning tasks. Our ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6. Experimental study results. (a) The dual encoder design, with both a semantic-rich CLIP encoder and a low-level vision DINO encoder, yields the ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior ... | component/input/data sensitivity | p. 7 (4.1. Visual Geometry Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We introduce G2VLM, the first unified model that bridges spatial 3D reconstruction and high-level spatial understanding ... | Table 2. Ablation study on the design choices for G2VLM. GP denotes the geometric perception expert. Our results validate the superiority of our approach ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 5 (Figure/Table caption) |
| Primary metric/result | These results demonstrate that our method achieves on-par performance with VGGT in completion and comparable results in accuracy. | numeric claim only at cited anchor | p. 7 (4.1. Visual Geometry Results) |

- Numeric sentences retained from the body:
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive PDF cue:** Notably, G2VLM-SR achieves the best results among all existing works, surpassing the proprietary GPT4o by 18.48 points on SPAR-Bench.
- **p. 5 / 3.3. Spatial Reasoning Learning - extractive PDF cue:** Similar to VGGT, for every batch, we randomly sample 2-24 frames from a random training scene.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models. | p. 8 (5. Conclusion) |
| body limitation/failure cue | We leave the scaling of our model to future work, as this is a promising direction to unlock even stronger performance. | p. 7 (4.2. Spatial Understanding & Reasoning Results) |
| body limitation/failure cue | These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior ... | p. 7 (4.1. Visual Geometry Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Across all training, we employ gradient norm clipping with a threshold of 1.0 to ensure training stability and leverage bfloat16 precision and gradient checkpointing ... | p. 5 (3.3. Spatial Reasoning Learning) |
| We first fix image resolution to 224x224 and use AdamW optimizer for 100K iterations with a learning rate (lr) of 2e-4 using cosine scheduler. | p. 5 (3.3. Spatial Reasoning Learning) |
| All heads are designed as lightweight transformer decoders. | p. 4 (3.1. Model Architecture) |
| We adopt the Qwen2 vision encoder which supports native dynamic resolution, along with the design of Multimodal Rotary Position Embedding (MRoPE). | p. 4 (3.1. Model Architecture) |
| For each sequence, we randomly sample 10 images, form all possible pairs, and compute the angular errors of the relative rotation and translation vectors. | p. 7 (4.1. Visual Geometry Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** While our model exhibits strong generalization abilities in both visual geometry and spatial reasoning, one potential limitation is training instability with large-scale models.
- **p. 7 / 4.2. Spatial Understanding & Reasoning Results - extractive PDF cue:** We leave the scaling of our model to future work, as this is a promising direction to unlock even stronger performance.
- **p. 7 / 4.1. Visual Geometry Results - extractive PDF cue:** These results underscore our model's strong capabilities, particularly since it does not use camera tokens (like VGGT) which provides a strong camera pose prior or ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 7 (4.2. Spatial Understanding & Reasoning Results), p. 5 (4. Experiments), metrics p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 5 (Figure/Table caption), p. 6 (4.1. Visual Geometry Results), p. 5 (4. Experiments), baselines p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.2. Spatial Understanding & Reasoning Results), p. 6 (4.1. Visual Geometry Results), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (4.1. Visual Geometry Results), p. 7 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 6 (4.1. Visual Geometry Results), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
