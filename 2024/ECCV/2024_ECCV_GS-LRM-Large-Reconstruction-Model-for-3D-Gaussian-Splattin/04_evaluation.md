# Evaluation - GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 10 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments)): Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost column), has fewer floaters (mid-right and ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive PDF cue:** We follow the standard training/testing split for the dataset, which is also used in pixelSplat [8].
- **p. 7 / 4 Experiments - extractive PDF cue:** We use the RealEstate10K [74] dataset to train our scenelevel model.
- **p. 6 / 4 Experiments - extractive PDF cue:** In this section, we first describe the training and testing datasets (Sec.
- **p. 10 / 4 Experiments - extractive PDF cue:** We can observe that our model is better in sharpness (leftmost column), has fewer floaters (mid-right and rightmost), and is more faithful to the original ...
- **p. 12 / 4 Experiments - extractive PDF cue:** Our current model is limited to static scenes only, and we thus pick the generated videos from relevant
- **p. 12 / 4 Experiments - extractive PDF cue:** 6: We show high-res novel-view renderings from our predicted GS given highres input images (4 512×512 images for objects, and 2 512×904 images for a ...
- **p. 8 / 4 Experiments - extractive PDF cue:** For scene-level, we adopt two input views for a fair comparison with pixelSplat [8].
- **p. 8 / 4 Experiments - extractive PDF cue:** We normalize the camera poses for scene-level input images following common practices in previous forward-facing reconstructions as done in [9,39].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost ... | p. 10 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, our approach achieves the best quantitative results on the RealEstate10k | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We outperform relevant baselines by a large margin in both scenarios. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, we improve the PSNR for novel-view rendering by 3.98dB on GSO data, and by 1.59dB on ABO data. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We outperform this baseline by a large margin across all view synthesis metrics; for example, as shown in Tab. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive PDF cue:** We follow the standard training/testing split for the dataset, which is also used in pixelSplat [8].
- **p. 7 / 4 Experiments - extractive PDF cue:** We use the RealEstate10K [74] dataset to train our scenelevel model.
- **p. 6 / 4 Experiments - extractive PDF cue:** In this section, we first describe the training and testing datasets (Sec.
- **p. 10 / 4 Experiments - extractive PDF cue:** We can observe that our model is better in sharpness (leftmost column), has fewer floaters (mid-right and rightmost), and is more faithful to the original ...
- **p. 12 / 4 Experiments - extractive PDF cue:** Our current model is limited to static scenes only, and we thus pick the generated videos from relevant
- **p. 12 / 4 Experiments - extractive PDF cue:** 6: We show high-res novel-view renderings from our predicted GS given highres input images (4 512×512 images for objects, and 2 512×904 images for a ...
- **p. 8 / 4 Experiments - extractive PDF cue:** For scene-level, we adopt two input views for a fair comparison with pixelSplat [8].
- **p. 8 / 4 Experiments - extractive PDF cue:** We normalize the camera poses for scene-level input images following common practices in previous forward-facing reconstructions as done in [9,39].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Novel-view renderings of our predicted Gaussians from object captures (top left), text-conditioned generated object images (top right), scene captures (bottom left) and text-conditioned ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our simple transformer-based GS-LRM predicts 3D Gaussian parameters from sparse posed images. Images are patchified and the concatenated patch tokens are sent to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison against baselines on object-level (left) and scene-level (right) reconstructions. We matched the baseline settings by comparing with Instant3D's Triplane-LRM [32] and LGM ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 3: Visual comparisons to Instant3D's Triplane-LRM [32]. The 4-view input images are shown in the leftmost column, and we compare novel view renderings on ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visual comparisons to LGM [59]. The LGM renderings have obvious distorted textures (top) and broken geometries (bottom) and are inferior in recovering accurate ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost column), ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 6: We show high-res novel-view renderings from our predicted GS given high- res input images (4 512×512 images for objects, and 2 512×904 images ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Fig. 7: Text-to-3D (top two rows) and image-to-3D (bottom two rows) results by chaining Instant3D's [32] text-conditioned and Zero123++'s [52] image-conditioned multi-view generators to our ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We follow the standard training/testing split for the dataset, which is also used in pixelSplat [8]. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We use the RealEstate10K [74] dataset to train our scenelevel model. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 6 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The dataset contains 80K video clips curated from 10K YouTube videos. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Following [27], we center and scale each 3D object to a bounding box of [-1, 1]3, and render 32 views randomly placed around the ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| This sampling strategy encourages more overlap between input views and rendering views than directly sampling from 32 rendering views, which helps the model's convergence. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| To enable efficient training and inference, we adopt FlashAttention-v2 [18] in the xFormers [31] library, gradient checkpointing [15], and mixed-precision training [37] with BF16 ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| The LGM renderings have obvious distorted textures (top) and broken geometries (bottom) and are inferior in recovering accurate surface opacity (top left; bottom left; ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We attribute this to our pixel-aligned Gaussian prediction scheme which creates a shortcut for learning accurate per-Gaussian colors from input RGB images; this is ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We qualitatively show some results to demonstrate such a workflow for applying our models in this downstream 3D generation task. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| For the image-to-3D application, we use the imageconditioned multi-view diffusion model in Zero123++ [52], which generates 6 structured views at fixed viewpoints. | definition/direction/unit from same section | p. 11 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We outperform relevant baselines by a large margin in both scenarios. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We outperform this baseline by a large margin across all view synthesis metrics; for example, as shown in Tab. | comparison identity and matched condition | p. 9 (4 Experiments) |
| In particular, when compared to pixelSplat, the top-performing baseline, our model leads to significant improvements of 2.2db in PSNR, 0.034 in SSIM, and 0.028 ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| We also made necessary changes for fair comparisons with baseline methods (Sec. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse ... | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We only leverage the multi-view renderings of the objects without accessing explicit 3D information (such as depths). | component/input/data sensitivity | p. 7 (4 Experiments) |
| We further fine-tune a model that takes 2 -4 input images of 512 × 512 for generating visual results. | component/input/data sensitivity | p. 8 (4 Experiments) |
| We pre-train the model with a resolution of 256 × 256 and fine-tune the trained model with a resolution of 512 × 512 for ... | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec. | Fig. 5: We compare scene-level GS-LRM with the best-performing baseline pixel- Splat [8]. We can observe that our model is better in sharpness (leftmost ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 10 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments) |
| Primary metric/result | 1, our approach achieves the best quantitative results on the RealEstate10k | numeric claim only at cited anchor | p. 10 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** GSO ABO PSNR \delimiter "3222378 SSIM \delimiter "3222378 LPIPS \delimiter "3223379 PSNR \delimiter "3222378 SSIM \delimiter "3222378 LPIPS \delimiter "3223379 Triplane-LRM [32] 26.54 0.893 0.064 ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We evaluate our model on two 3D object datasets including the full Google Scanned Objects (GSO) [21] that contains 1009 objects and the Amazon Berkeley ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Our transformer consists of 24 layers, and the hidden dimension of the transformer is 1024.
- **p. 9 / 4 Experiments - extractive PDF cue:** The official LGM is trained with a special setting using 256×256 resolution input and 512×512 resolution output supervision.
- **p. 9 / 4 Experiments - extractive PDF cue:** Since their model only accepts 256×256 input, we compare with LGM using our low-res model, trained with 256×256 images only from our 256-res pre-training stage.
- **p. 9 / 4 Experiments - extractive PDF cue:** We evaluate both models with 256×256 renderings for comparison.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future ... | p. 13 (4 Experiments) |
| body limitation/failure cue | We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction. | p. 14 (5 Conclusion) |
| body limitation/failure cue | The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well. | p. 8 (4 Experiments) |
| body limitation/failure cue | Please refer to our project page for the video and interactive rendering results. the view frustum, which means that unseen regions cannot be reconstructed. | p. 14 (4 Experiments) |
| body limitation/failure cue | We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse ... | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.1), then introduce the implementation and training details (Sec. | p. 6 (4 Experiments) |
| 4.2 Implementation Details We have two models trained independently in this paper: object-level GS-LRM and scene-level GS-LRM. | p. 7 (4 Experiments) |
| We also apply deferred backpropagation [71] for rendering the GS to save GPU memory. | p. 8 (4 Experiments) |
| We pre-train the model with a resolution of 256 × 256 and fine-tune the trained model with a resolution of 512 × 512 for ... | p. 8 (4 Experiments) |
| We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse ... | p. 9 (4 Experiments) |
| This further highlights the method-wise advantage of our GS-LRM - a transformer model predicting per-pixel Gaussians that scales up easily with data and compute. | p. 10 (4 Experiments) |
| It's worth noting that this is an almost equal-compute comparison: LGM is trained on 32 A100 (80G VRAM) for 4 days, while our lowres ... | p. 10 (4 Experiments) |
| From each output token, we decode the attributes of pixel-aligned Gaussians in the corresponding patch with a linear layer. | p. 4 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 4 Experiments - extractive PDF cue:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.
- **p. 14 / 5 Conclusion - extractive PDF cue:** We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction.
- **p. 8 / 4 Experiments - extractive PDF cue:** The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well.
- **p. 14 / 4 Experiments - extractive PDF cue:** Please refer to our project page for the video and interactive rendering results. the view frustum, which means that unseen regions cannot be reconstructed.
- **p. 9 / 4 Experiments - extractive PDF cue:** We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse inputs; ...

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), metrics p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), baselines p. 7 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 10 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), results p. 10 (Figure/Table caption), p. 10 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
