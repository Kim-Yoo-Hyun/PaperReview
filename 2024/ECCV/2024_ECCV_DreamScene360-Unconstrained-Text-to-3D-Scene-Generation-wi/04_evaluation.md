# Evaluation - DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/996_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00996.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments)): These functionalities are otherwise hard to achieve in previous baselines that do not have global 2D representations, and as a result, our results provide a much better visual appearance than ...

## Evaluation Body Digest

- **p. 11 / 4 Experiments - extractive PDF cue:** QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets.
- **p. 11 / 4 Experiments - extractive PDF cue:** Specifically, for each method, we render images with camera rotations and translations to mimic the immersive trajectory inside the 3D scenes.
- **p. 12 / 4 Experiments - extractive PDF cue:** Their pipeline, which inpaints each patch separately based on the same text prompt, tends to produce repetitive results especially when generating complex scenes.
- **p. 12 / 4 Experiments - extractive PDF cue:** 3, our method can generate diverse 3D scenes in different styles with distinct contents, while preserving high-fidelity novel-view rendering ability and realistic scene geometry.
- **p. 13 / 4 Experiments - extractive PDF cue:** DreamScene360 13 (a) ℒ!"# (b) ℒ!"# + ℒ$%& (c) ℒ!"# + ℒ'%( (d) ℒ!"# + ℒ$%& + ℒ'%( Fig.
- **p. 13 / 4 Experiments - extractive PDF cue:** In this part, we mainly focus on the generated panorama since panorama provides a holistic view of the 3D scene and provides an upper bound ...
- **p. 14 / 4 Experiments - extractive PDF cue:** In the absence of geometric priors of the scene (a), the optimized 3D Gaussian rendering yields plausible results in panoramic camera views.
- **p. 11 / 4 Experiments - extractive PDF cue:** However, the works utilizing a bounded NeRF representation using score distillation do not work very well in this case.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 11).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | These functionalities are otherwise hard to achieve in previous baselines that do not have global 2D representations, and as a result, our results provide ... | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, the works utilizing a bounded NeRF representation using score distillation do not work very well in this case. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4.2 Main Results 360◦Scene Generation. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In comparison, our method delivers consistent results thanks to the intermediate panorama as a global 2D representation. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5, we observe that using a simple text prompt usually delivers minimalist results with fewer details. | p. 13 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 11 / 4 Experiments - extractive PDF cue:** QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets.
- **p. 11 / 4 Experiments - extractive PDF cue:** Specifically, for each method, we render images with camera rotations and translations to mimic the immersive trajectory inside the 3D scenes.
- **p. 12 / 4 Experiments - extractive PDF cue:** Their pipeline, which inpaints each patch separately based on the same text prompt, tends to produce repetitive results especially when generating complex scenes.
- **p. 12 / 4 Experiments - extractive PDF cue:** 3, our method can generate diverse 3D scenes in different styles with distinct contents, while preserving high-fidelity novel-view rendering ability and realistic scene geometry.
- **p. 13 / 4 Experiments - extractive PDF cue:** DreamScene360 13 (a) ℒ!"# (b) ℒ!"# + ℒ$%& (c) ℒ!"# + ℒ'%( (d) ℒ!"# + ℒ$%& + ℒ'%( Fig.
- **p. 13 / 4 Experiments - extractive PDF cue:** In this part, we mainly focus on the generated panorama since panorama provides a holistic view of the 3D scene and provides an upper bound ...
- **p. 14 / 4 Experiments - extractive PDF cue:** In the absence of geometric priors of the scene (a), the optimized 3D Gaussian rendering yields plausible results in panoramic camera views.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: DreamScene360. We introduce a 3D scene generation pipeline that creates immersive scenes with full 360◦coverage from text prompts of any level of specificity. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overall Architecture. Beginning with a concise text prompt, we employ a diffusion model to generate a 360◦panoramic image. A self-refinement process is em- ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 3: Diverse Generation. We demonstrate that our generated 3D scenes are di- verse in style, consistent in geometry, and highly matched with the simple ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visual Comparisons. We showcase 360◦3D scene generation. In each row, from left to right, displays novel views as the camera undergoes clockwise rotation ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparisons between LucidDreamer and ours. CLIP Distance↓ Q-Align↑ NIQE↓ BRISQUE↓ Runtime LucidDreamer [7] 0.8900
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 5: Ablation of Self-Refinement. We demonstrate that the self-refinement pro- cess greatly enhances the image quality by improving the text prompt. As shown in ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Fig. 6: Ablation of Optimization Loss. We demonstrate the impact of Semantic and Geometric losses on the synthesized virtual cameras. (a) Utilizing photometric loss on ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 7: Ablation Study on 3D Initialization. We present a comparative visual- ization of various initialization methods for 3D Panoramic Gaussian Splatting. In the absence ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets. | embodiment, simulator version and control stack | p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Task/environment | Specifically, for each method, we render images with camera rotations and translations to mimic the immersive trajectory inside the 3D scenes. | reset, timeout, object/scene variation | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| However, the works utilizing a bounded NeRF representation using score distillation do not work very well in this case. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Since there is no ground truth in the generated 3D scenes, we utilize CLIP [47] embedding distance, following previous works [58,68], to measure the ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| We demonstrate the impact of Semantic and Geometric losses on the synthesized virtual cameras. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| We demonstrate that the self-refinement process greatly enhances the image quality by improving the text prompt. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| In conclusion, our results demonstrate global semantic, stylized, and geometric consistency, offering complete 360◦coverage without any blind spots. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Loss Function We investigate the importance of multiple loss functions we adopted in Fig. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Fig. 2: Overall Architecture. Beginning with a concise text prompt, we employ a diffusion model to generate a 360◦panoramic image. A self-refinement process is ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 3: Diverse Generation. We demonstrate that our generated 3D scenes are di- verse in style, consistent in geometry, and highly matched with the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer [7]. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Fig. 4: Visual Comparisons. We showcase 360◦3D scene generation. In each row, from left to right, displays novel views as the camera undergoes clockwise ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets. | comparison identity and matched condition | p. 11 (4 Experiments) |
| These functionalities are otherwise hard to achieve in previous baselines that do not have global 2D representations, and as a result, our results provide ... | comparison identity and matched condition | p. 13 (4 Experiments) |
| We provide quantitative comparisons in Tab. | comparison identity and matched condition | p. 12 (4 Experiments) |
| We show visual comparisons against LucidDreamer [7] in Fig. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 6: Ablation of Optimization Loss. We demonstrate the impact of Semantic and Geometric losses on the synthesized virtual cameras. (a) Utilizing photometric loss ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| In conclusion, our results demonstrate global semantic, stylized, and geometric consistency, offering complete 360◦coverage without any blind spots. | component/input/data sensitivity | p. 12 (4 Experiments) |
| 4.3 Ablation Study Self-refinement Process We further evaluate the importance of the selfrefinement process. | component/input/data sensitivity | p. 13 (4 Experiments) |
| 7: Ablation Study on 3D Initialization. | component/input/data sensitivity | p. 14 (4 Experiments) |
| Fig. 5: Ablation of Self-Refinement. We demonstrate that the self-refinement pro- cess greatly enhances the image quality by improving the text prompt. As shown ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| QAlign [65] is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets. | component/input/data sensitivity | p. 11 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Collectively, our framework, DreamScene360, enables the creation of immersive and realistic 3D environments from a simple user command, offering a novel solution to the ... | These functionalities are otherwise hard to achieve in previous baselines that do not have global 2D representations, and as a result, our results provide ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments) |
| Primary metric/result | However, the works utilizing a bounded NeRF representation using score distillation do not work very well in this case. | numeric claim only at cited anchor | p. 11 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 1 Introduction - extractive PDF cue:** 3.2 Lifting in-the-wild Panorama to 360 Scene Transforming a single image, specifically an in-the-wild 360◦panoramic image, into a 3D model poses significant challenges due to ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the case of the Yosemite text prompt, LucidDreamer merely replicates the waterfall seen in the initial view throughout. | p. 12 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.1 Experiment Setting Implementation. | p. 11 (4 Experiments) |
| We use the opensource codebase of LucidDreamer, which starts from a single image and a text prompt. | p. 11 (4 Experiments) |
| The vast potential applications of text-to-3D to VR/MR platforms, industrial design, and gaming sectors have significantly propelled research efforts aimed at developing a reliable ... | p. 2 (1 Introduction) |
| Moreover, the issue of prompt engineering in text-to-image generation [51, 52], becomes more pronounced in text-to-3D generation frameworks [1, 7, 46] that rely on ... | p. 2 (1 Introduction) |
| Upon projecting the 3D Gaussians into a 2D space, the color C of a pixel is computed by volumetric rendering, which is performed using ... | p. 7 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 4 Experiments - extractive PDF cue:** In the case of the Yosemite text prompt, LucidDreamer merely replicates the waterfall seen in the initial view throughout.

- **PDF anchors reviewed:** datasets p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), metrics p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), baselines p. 11 (4 Experiments), p. 10 (Figure/Table caption), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), results p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 14 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
