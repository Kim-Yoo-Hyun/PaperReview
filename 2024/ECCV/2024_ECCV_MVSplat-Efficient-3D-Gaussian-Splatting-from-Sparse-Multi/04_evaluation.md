# Evaluation - MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03187.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments), p. 11 (4 Experiments)): Note that the MVSplat significantly outperforms pixelSplat in terms of LPIPS, and the gain is larger when the domain gap between source and target datasets becomes larger.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive PDF cue:** On the DTU dataset, we report results on 16 validation scenes, with 4 novel views for each scene.
- **p. 8 / 4 Experiments - extractive PDF cue:** Furthermore, to further assess the cross-dataset generalization ability, we also directly evaluate all models on the multi-view DTU [16] dataset, which contains object-centric scenes with ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Models trained on the source dataset RealEstate10K (indoor scenes) are used to conduct zero-shot test on scenes from target datasets ACID (outdoor scenes) and DTU ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Models are trained with a collection of training scenes from each indicated dataset, and tested on novel scenes from the same dataset.
- **p. 11 / 4 Experiments - extractive PDF cue:** 5, MVSplat renders competitive novel views, despite scenes of the targeted datasets containing significantly different camera distributions and image appearance from those of the source ...
- **p. 7 / 4 Experiments - extractive PDF cue:** RealEstate10K contains real estate videos downloaded from YouTube, which are split into 67,477 training scenes and 7,289 testing scenes, while ACID contains nature scenes captured ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We assess our model on the large-scale RealEstate10K [51] and ACID [20] datasets.
- **p. 9 / 4 Experiments - extractive PDF cue:** The first three rows are from RealEstate10K (indoor scenes), while the last one is from ACID (outdoor scenes).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that the MVSplat significantly outperforms pixelSplat in terms of LPIPS, and the gain is larger when the domain gap between source and target ... | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | MVSplat achieves the highest quality on novel view results even under challenging conditions, such as these regions with repeated patterns ("window frames" in 1st ... | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4. pixelSplat requires an extra 50,000 steps to fine-tune the Gaussians with an additional depth regularization to achieve reasonable geometry reconstruction results. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2), MVSplat achieves better performance with more input views. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | MVSplat surpasses all previous state-of-theart models in terms of all metrics on visual quality, with more obvious improve | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive PDF cue:** On the DTU dataset, we report results on 16 validation scenes, with 4 novel views for each scene.
- **p. 8 / 4 Experiments - extractive PDF cue:** Furthermore, to further assess the cross-dataset generalization ability, we also directly evaluate all models on the multi-view DTU [16] dataset, which contains object-centric scenes with ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Models trained on the source dataset RealEstate10K (indoor scenes) are used to conduct zero-shot test on scenes from target datasets ACID (outdoor scenes) and DTU ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Models are trained with a collection of training scenes from each indicated dataset, and tested on novel scenes from the same dataset.
- **p. 11 / 4 Experiments - extractive PDF cue:** 5, MVSplat renders competitive novel views, despite scenes of the targeted datasets containing significantly different camera distributions and image appearance from those of the source ...
- **p. 7 / 4 Experiments - extractive PDF cue:** RealEstate10K contains real estate videos downloaded from YouTube, which are split into 67,477 training scenes and 7,289 testing scenes, while ACID contains nature scenes captured ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We assess our model on the large-scale RealEstate10K [51] and ACID [20] datasets.
- **p. 9 / 4 Experiments - extractive PDF cue:** The first three rows are from RealEstate10K (indoor scenes), while the last one is from ACID (outdoor scenes).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Our MVSplat outperforms pixelSplat [1] in terms of both appearance and geometry quality with 10× fewer parameters and more than 2× faster inference ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of MVSplat. Given multiple posed images as input, MVSplat first extracts multi-view image features with a Transformer. Then, the per-view cost volumes ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Comparisons with the state of the art. Running time includes both encoder and render, note that 3DGS-based methods (pixelSplat and MVSplat) render dramatically ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 3: Comparisons with the state of the art. The first three rows are from RealEstate10K (indoor scenes), while the last one is from ACID ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4: Comparisons of 3D Gaussians (top) and depth maps (bottom). We compare the reconstructed geometry quality by visualizing zoom-out views of 3D Gaus- sians ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 5: Cross-dataset generalization. Models trained on the source dataset RealEstate10K (indoor scenes) are used to conduct zero-shot test on scenes from target datasets ACID ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 2: Cross-dataset generalization. Models trained on RE10K (indoor scenes) are directly used to test on scenes from ACID (outdoor scenes) and DTU (object- centric ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 3: Ablations on RealEstate10K. The "base + refine" is our final model, where "refine" refers to the "depth refinement" detailed in Sec. 3.1. All ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | On the DTU dataset, we report results on 16 validation scenes, with 4 novel views for each scene. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | Furthermore, to further assess the cross-dataset generalization ability, we also directly evaluate all models on the multi-view DTU [16] dataset, which contains object-centric scenes ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 11 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (3 Method), p. 6 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The inference time and model parameters are also reported to enable thorough comparisons of speed and accuracy trade-offs. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 6 ("w/o cross-attn") showcase higher error intensity. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Colored error maps obtained by calculating the differences between the rendered images and the ground truth are attached for better comparison. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Performances are averaged over thousands of test scenes in each dataset. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| This includes pixelNeRF [46], GPNR [33], AttnRend [10] and pixelSplat [1], with results taken directly from the pixelSplat [1] paper, and the recent state-of-the-art ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Our MVSplat instead generates high-quality geometries by training solely with photometric supervision. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| 4 demonstrates the feed-forward geometry reconstruction results of MVSplat, without any extra fine-tuning. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| To demonstrate this advantage, we conduct two cross-dataset evaluations. | definition/direction/unit from same section | p. 11 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| MVSplat also produces significantly higher-quality 3D Gaussian primitives compared to the latest state-of-the-art pixelSplat [1], as demonstrated in Fig. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Fig. 6: Ablations on RealEstate10K. Colored error maps obtained by calculating the differences between the rendered images and the ground truth are attached for ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| We compare MVSplat with several representative feed-forward methods that focus on scene-level novel view synthesis from sparse views, including i) Light Field Network-based GPNR ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| The baseline methods exhibit obvious artifacts for these regions, while MVSplat shows no such artifacts due to our cost volume-based geometry representation. | comparison identity and matched condition | p. 9 (4 Experiments) |
| This includes pixelNeRF [46], GPNR [33], AttnRend [10] and pixelSplat [1], with results taken directly from the pixelSplat [1] paper, and the recent state-of-the-art ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| 1, apart from attaining superior image quality, MVSplat also shows the fastest inference time among all the compared models, accompanied by a lightweight model ... | comparison identity and matched condition | p. 10 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Models trained on the source dataset RealEstate10K (indoor scenes) are used to conduct zero-shot test on scenes from target datasets ACID (outdoor scenes) and ... | component/input/data sensitivity | p. 11 (4 Experiments) |
| 4 demonstrates the feed-forward geometry reconstruction results of MVSplat, without any extra fine-tuning. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Models trained on RE10K (indoor scenes) are directly used to test on scenes from ACID (outdoor scenes) and DTU (objectcentric scenes), without any further ... | component/input/data sensitivity | p. 11 (4 Experiments) |
| All other ablations are conducted on the "base" model w/o depth refinement. | component/input/data sensitivity | p. 12 (4 Experiments) |
| Setup PSNR↑SSIM↑LPIPS↓ base + refine 26.39 0.869 0.128 base 26.12 0.864 0.133 w/o cost volume 22.83 0.753 0.197 w/o cross-view attention 25.19 0.852 0.152 ... | component/input/data sensitivity | p. 12 (4 Experiments) |
| Our full model without "depth refinement" (Sec. | component/input/data sensitivity | p. 13 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present MVSplat, a Gaussian-based feed-forward model for novel view synthesis. | Note that the MVSplat significantly outperforms pixelSplat in terms of LPIPS, and the gain is larger when the domain gap between source and target ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments), p. 11 (4 Experiments) |
| Primary metric/result | MVSplat achieves the highest quality on novel view results even under challenging conditions, such as these regions with repeated patterns ("window frames" in 1st ... | numeric claim only at cited anchor | p. 9 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive PDF cue:** Running time includes both encoder and render, note that 3DGS-based methods (pixelSplat and MVSplat) render dramatically faster (∼500FPS for the render).
- **p. 10 / 4 Experiments - extractive PDF cue:** For an in-depth time comparison with pixelSplat [1], our encoder runs at 0.043s, which is more than 2× faster than pixelSplat (0.102s).
- **p. 10 / 4 Experiments - extractive PDF cue:** Besides, pixelSplat predicts 3 Gaussians perpixel, while our MVSplat predicts 1 single Gaussian, which also contributes to our faster rendering speed (0.0015s vs.
- **p. 10 / 4 Experiments - extractive PDF cue:** 0.0025s) due to the threefold reduction in the number of Gaussians.
- **p. 10 / 4 Experiments - extractive PDF cue:** 4. pixelSplat requires an extra 50,000 steps to fine-tune the Gaussians with an additional depth regularization to achieve reasonable geometry reconstruction results.
- **p. 5 / 3 Method - extractive PDF cue:** After this operation, we obtain cross-view aware Transformer features {F i}K i=1 (F i ∈R H 4 × W 4 ×C), where C denotes the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This limitation is analogous to the reason why pixelSplat performs inferior in cross-dataset generalization tests discussed earlier. | p. 12 (4 Experiments) |
| body limitation/failure cue | This is because our cost volume cannot find any matches in these regions, leading to poorer geometry cues. | p. 14 (4 Experiments) |
| body limitation/failure cue | Besides, our model is currently trained on the RealEstate10K dataset, where its diversity is not sufficient enough to generalize robustly to in-the-wild real-world scenarios ... | p. 14 (5 Conclusion) |
| body limitation/failure cue | MVSplat is inherently superior in generalizing to out-of-distribution novel scenes, primarily due to the fact that the cost volume captures the relative similarity between ... | p. 11 (4 Experiments) |
| body limitation/failure cue | This discrepancy is attributed to the reliance of pixelSplat on pure feature aggregation, which lacks robustness to changes in feature distribution. | p. 12 (4 Experiments) |
| body limitation/failure cue | When removing it from the "base" model, the quantitative results drop significantly: it decreases the PSNR by more than 3dB, and increases LPIPS by ... | p. 13 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The inference time and model parameters are also reported to enable thorough comparisons of speed and accuracy trade-offs. | p. 8 (4 Experiments) |
| 1, apart from attaining superior image quality, MVSplat also shows the fastest inference time among all the compared models, accompanied by a lightweight model ... | p. 10 (4 Experiments) |
| All models are trained on a single A100 GPU for 300,000 iterations with the Adam [19] optimizer. | p. 8 (4 Experiments) |
| This includes pixelNeRF [46], GPNR [33], AttnRend [10] and pixelSplat [1], with results taken directly from the pixelSplat [1] paper, and the recent state-of-the-art ... | p. 9 (4 Experiments) |
| For an in-depth time comparison with pixelSplat [1], our encoder runs at 0.043s, which is more than 2× faster than pixelSplat (0.102s). | p. 10 (4 Experiments) |
| The cost volume serves as a cornerstone to the success of MVSplat, which plays the most important role in our encoder to provide better ... | p. 13 (4 Experiments) |
| (2) and compute their correlations via Eq. | p. 6 (3 Method) |
| We then compute the dot product [43,44] between F i and F j→i dm to obtain the correlation | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / 4 Experiments - extractive PDF cue:** This limitation is analogous to the reason why pixelSplat performs inferior in cross-dataset generalization tests discussed earlier.
- **p. 14 / 4 Experiments - extractive PDF cue:** This is because our cost volume cannot find any matches in these regions, leading to poorer geometry cues.
- **p. 14 / 5 Conclusion - extractive PDF cue:** Besides, our model is currently trained on the RealEstate10K dataset, where its diversity is not sufficient enough to generalize robustly to in-the-wild real-world scenarios despite ...
- **p. 11 / 4 Experiments - extractive PDF cue:** MVSplat is inherently superior in generalizing to out-of-distribution novel scenes, primarily due to the fact that the cost volume captures the relative similarity between features, ...
- **p. 12 / 4 Experiments - extractive PDF cue:** This discrepancy is attributed to the reliance of pixelSplat on pure feature aggregation, which lacks robustness to changes in feature distribution.
- **p. 13 / 4 Experiments - extractive PDF cue:** When removing it from the "base" model, the quantitative results drop significantly: it decreases the PSNR by more than 3dB, and increases LPIPS by 0.064 ...

- **PDF anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 7 (4 Experiments), metrics p. 8 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), baselines p. 10 (4 Experiments), p. 13 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), results p. 12 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 8 (4 Experiments), p. 11 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
