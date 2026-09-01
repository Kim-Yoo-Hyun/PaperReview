# Evaluation - SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (4.4. Ablation Study), p. 7 (4.3. Zero-Shot Generalization), p. 7 (4.1. Experimental Setup), p. 6 (Figure/Table caption), p. 6 (4.1. Experimental Setup)): Table 3. Component-wise ablation on RE10K (4× 3DSR). Modules are added cumulatively to the NoPoSplat baseline. Each component improves performance, and Gaussian Offset Learning yields the largest gain with fewer ...

## Evaluation Body Digest

- **p. 7 / 4.3. Zero-Shot Generalization - extractive PDF cue:** We further evaluate the zero-shot generalization ability of SR3R on the DTU dataset, a challenging object-centric benchmark with unseen geometries and illumination conditions.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** To further assess generalization, we perform zero-shot 3DSR experiments on the DTU dataset, which features object-centric scenes with different camera motion and scene types from ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** RE10K and ACID are two large-scale datasets, containing indoor real estate walkthrough videos and outdoor natural scenes captured by aerial drones, respectively.
- **p. 8 / 4.3. Zero-Shot Generalization - extractive PDF cue:** This indicates that SR3R effectively preserves geometric and photometric fidelity even on completely unseen scenes.
- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive PDF cue:** We evaluate SR3R through 4× 3DSR experiments on the large-scale RE10K and ACID datasets, and compare it against the SOTA feed-forward 3DGS reconstruction models NoPoSplat ...
- **p. 8 / 4.3. Zero-Shot Generalization - extractive PDF cue:** SRGS and FSGS+SRGS use per-scene optimization.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Adding PointTransformerV3 further boosts accuracy through multi-scale spatial reasoning, producing the full SR3R model with the best performance.
- **p. 7 / 4.3. Zero-Shot Generalization - extractive PDF cue:** As shown in Table 2, SR3R achieves substantially higher accuracy than all feed-forward baselines in the zero-shot 33390

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental Results (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. Component-wise ablation on RE10K (4× 3DSR). Modules are added cumulatively to the NoPoSplat baseline. Each component improves performance, and Gaussian Offset Learning ... | p. 8 (Figure/Table caption) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Offset w/o PTv3), it significantly improves reconstruction quality while reducing the number of learnable Gaussian parameters, demonstrating its efficiency. | p. 8 (4.4. Ablation Study) |
| 4.3. Zero-Shot Generalization | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, SR3R achieves substantially higher accuracy than all feed-forward baselines in the zero-shot 33390 | p. 7 (4.3. Zero-Shot Generalization) |
| 4.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | Each component of SR3R progressively improves reconstruction quality, with upsampling reducing coarse blur, cross-attention improving feature alignment, Gaussian offset learning enhancing local geometry, and ... | p. 7 (4.1. Experimental Setup) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1. Quantitative comparison of 4× 3DSR on the large-scale RE10K and ACID datasets. SR3R consistently and substantially outperforms all baselines and their upscaled-input ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Zero-Shot Generalization - extractive PDF cue:** We further evaluate the zero-shot generalization ability of SR3R on the DTU dataset, a challenging object-centric benchmark with unseen geometries and illumination conditions.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** To further assess generalization, we perform zero-shot 3DSR experiments on the DTU dataset, which features object-centric scenes with different camera motion and scene types from ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** RE10K and ACID are two large-scale datasets, containing indoor real estate walkthrough videos and outdoor natural scenes captured by aerial drones, respectively.
- **p. 8 / 4.3. Zero-Shot Generalization - extractive PDF cue:** This indicates that SR3R effectively preserves geometric and photometric fidelity even on completely unseen scenes.
- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive PDF cue:** We evaluate SR3R through 4× 3DSR experiments on the large-scale RE10K and ACID datasets, and compare it against the SOTA feed-forward 3DGS reconstruction models NoPoSplat ...
- **p. 8 / 4.3. Zero-Shot Generalization - extractive PDF cue:** SRGS and FSGS+SRGS use per-scene optimization.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We reformulate 3DGS-based 3DSR as a feed-forward mapping problem from sparse LR views to HR 3DGS representation. (a) Unlike existing methods that rely ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the SR3R framework. Given two LR input views, a feed-forward 3DGS backbone produces an LR 3DGS, which is then densified via ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison with SOTA feed-forward 3DGS reconstruction methods on Re10k (top three) and ACID (bottom three) datasets. SR3R delivers significantly sharper details and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison of 4× 3DSR on the large-scale RE10K and ACID datasets. SR3R consistently and substantially outperforms all baselines and their upscaled-input versions ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative ablation results of SR3R components. Each component of SR3R progressively improves reconstruction quality, with upsampling reducing coarse blur, cross-attention improving feature alignment, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Zero-shot generalization results from RE10K to DTU. Feed-forward models are trained on RE10K and tested on DTU without fine-tuning. SRGS and FSGS+SRGS use ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Component-wise ablation on RE10K (4× 3DSR). Modules are added cumulatively to the NoPoSplat baseline. Each component improves performance, and Gaussian Offset Learning yields ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation on upsampling strategies on RE10K (4× 3DSR). SR3R maintains consistently strong performance across all interpolation and learning-based upsampling methods. Upsampling RE10K (64 ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We further evaluate the zero-shot generalization ability of SR3R on the DTU dataset, a challenging object-centric benchmark with unseen geometries and illumination conditions. | embodiment, simulator version and control stack | p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup) |
| Task/environment | To further assess generalization, we perform zero-shot 3DSR experiments on the DTU dataset, which features object-centric scenes with different camera motion and scene types ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Problem Formulation), p. 4 (3.4. LR Image to HR 3DGS Mapping) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Adding PointTransformerV3 further boosts accuracy through multi-scale spatial reasoning, producing the full SR3R model with the best performance. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| As shown in Table 2, SR3R achieves substantially higher accuracy than all feed-forward baselines in the zero-shot 33390 | definition/direction/unit from same section | p. 7 (4.3. Zero-Shot Generalization) |
| This setup allows us to evaluate large-scale 3DSR performance and demonstrate SR3R's superior zero-shot capability without scene-specific optimization. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| We evaluate the robustness of SR3R to different upsampling strategies used before the ViT encoder. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| The MSE and LPIPS loss weights follow [37] and are set to 1 and 0.05. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| Figure 1. We reformulate 3DGS-based 3DSR as a feed-forward mapping problem from sparse LR views to HR 3DGS representation. (a) Unlike existing methods that ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Overview of the SR3R framework. Given two LR input views, a feed-forward 3DGS backbone produces an LR 3DGS, which is then densified ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3. Qualitative comparison with SOTA feed-forward 3DGS reconstruction methods on Re10k (top three) and ACID (bottom three) datasets. SR3R delivers significantly sharper details ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1. Quantitative comparison of 4× 3DSR on the large-scale RE10K and ACID datasets. SR3R consistently and substantially outperforms all baselines and their upscaled-input ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| All feed-forward models, including SR3R and baselines, are trained on RE10K and directly tested on DTU without any fine-tuning. | comparison identity and matched condition | p. 7 (4.3. Zero-Shot Generalization) |
| We additionally include two SOTA per-scene optimization methods, SRGS [9] and FSGS [47], a sparse-view-specific model that we combine with SRGS (denoted as FSGS+SRGS) ... | comparison identity and matched condition | p. 7 (4.3. Zero-Shot Generalization) |
| To assess the contribution of each component in SR3R, we perform a component-wise ablation using NoPoSplat as the baseline and evaluate 4× 3DSR performance ... | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| We compare SR3R with two state-of-the-art feed-forward 3DGS reconstruction models, NoPoSplat [37] and DepthSplat [33], as well as the perscene optimization methods SRGS [9] ... | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| Modules are added cumulatively to the NoPoSplat baseline. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Qualitative ablation results of SR3R components. | component/input/data sensitivity | p. 7 (4.1. Experimental Setup) |
| All feed-forward models, including SR3R and baselines, are trained on RE10K and directly tested on DTU without any fine-tuning. | component/input/data sensitivity | p. 7 (4.3. Zero-Shot Generalization) |
| Component-wise ablation on RE10K (4× 3DSR). | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| This setup allows us to evaluate large-scale 3DSR performance and demonstrate SR3R's superior zero-shot capability without scene-specific optimization. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| Ablation on upsampling strategies on RE10K (4× 3DSR). | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Figure 2. Overview of the SR3R framework. Given two LR input views, a feed-forward 3DGS backbone produces an LR 3DGS, which is then densified ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions are as follows. • A novel formulation of 3DSR. | Table 3. Component-wise ablation on RE10K (4× 3DSR). Modules are added cumulatively to the NoPoSplat baseline. Each component improves performance, and Gaussian Offset Learning ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (4.4. Ablation Study), p. 7 (4.3. Zero-Shot Generalization), p. 7 (4.1. Experimental Setup), p. 6 (Figure/Table caption), p. 6 (4.1. Experimental Setup) |
| Primary metric/result | Offset w/o PTv3), it significantly improves reconstruction quality while reducing the number of learnable Gaussian parameters, demonstrating its efficiency. | numeric claim only at cited anchor | p. 8 (4.4. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 7 / 4.1. Experimental Setup - extractive PDF cue:** Both the backbone and our mapping network are trained for 75,000 iterations with a batch size of 8 and a learning rate of 2.5×10-5.
- **p. 7 / 4.1. Experimental Setup - extractive PDF cue:** All experiments are conducted on four NVIDIA RTX 5090 GPUs.
- **p. 8 / 4.3. Zero-Shot Generalization - extractive PDF cue:** Time ↓ SRGS [9] 12.420 0.327 0.598 300s FSGS+SRGS [47] 13.720 0.444 0.481 420s NopoSplat [38] 12.628 0.343 0.581 0.01s Up-Noposplat 16.643 0.598 0.369 0.16s ...
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Time ↓ Bilinear 24.586 0.795 0.204 1.59s Bicubic 24.663 0.817 0.193 1.53s SwinIR [18] 24.794 0.827 0.188 1.69s HAT [3] 24.782 0.819 0.183 1.75s
- **p. 4 / 3.3. LR 3DGS Reconstruction and Densification - extractive PDF cue:** The final densified 3DGS is obtained by aggregating all sub-Gaussians: \mat h c a l { G} ^{\ text { Den s e}} = \bi ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These improvements hold for both 3DGS backbones, confirming that our offsetbased refinement and cross-view fusion effectively restore 3D-specific high-frequency structures that 2D upsampling and ... | p. 7 (4.2. Comparison with State-of-the-Art) |
| body limitation/failure cue | Applying 2D upsampling reduces excessive softness but still fails to recover reliable high-frequency structures, often introducing ambiguous or hallucinated textures. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | Notably, even Bilinear interpolation already surpasses all feed-forward baselines (Table 1), indicating that SR3R does not depend on a particular upsampling design. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | These results highlight the advantage of learning Gaussian offsets over direct parameter regression, enabling more accurate high-frequency recovery under sparse LR inputs. | p. 7 (4.2. Comparison with State-of-the-Art) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Both the backbone and our mapping network are trained for 75,000 iterations with a batch size of 8 and a learning rate of 2.5×10-5. | p. 7 (4.1. Experimental Setup) |
| The ViT encoder-decoder follows a vanilla configuration with a patch size of 16 and 8 attention heads. | p. 7 (4.1. Experimental Setup) |
| We evaluate the robustness of SR3R to different upsampling strategies used before the ViT encoder. | p. 8 (4.4. Ablation Study) |
| Incorporating bidirectional cross-attention further enhances structural consistency by injecting geometric priors from the pretrained 3DGS encoder. | p. 8 (4.4. Ablation Study) |
| Two crossattentions are computed in opposite directions: \b e gin {al i gned} \mathbf { U}_ { o \ leftar r o w p} ... | p. 4 (3.4. LR Image to HR 3DGS Mapping) |
| The encoder learns locally contextualized representations capturing essential texture and geometric cues. | p. 4 (3.4. LR Image to HR 3DGS Mapping) |
| This produces the decoded features tde ∈RN×C, which integrate multi-view geometry and reduce inconsistencies caused by pose inaccuracy or limited view overlap. | p. 5 (3.4. LR Image to HR 3DGS Mapping) |
| The decoded features are then provided to the Gaussian offset learning module (Section 3.5) to estimate residual corrections from the densified representation GDense to ... | p. 5 (3.4. LR Image to HR 3DGS Mapping) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive PDF cue:** These improvements hold for both 3DGS backbones, confirming that our offsetbased refinement and cross-view fusion effectively restore 3D-specific high-frequency structures that 2D upsampling and direct ...
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Applying 2D upsampling reduces excessive softness but still fails to recover reliable high-frequency structures, often introducing ambiguous or hallucinated textures.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Notably, even Bilinear interpolation already surpasses all feed-forward baselines (Table 1), indicating that SR3R does not depend on a particular upsampling design.
- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive PDF cue:** These results highlight the advantage of learning Gaussian offsets over direct parameter regression, enabling more accurate high-frequency recovery under sparse LR inputs.

- **PDF anchors reviewed:** datasets p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Zero-Shot Generalization), p. 7 (4.2. Comparison with State-of-the-Art), p. 8 (4.3. Zero-Shot Generalization), metrics p. 8 (4.4. Ablation Study), p. 7 (4.3. Zero-Shot Generalization), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 7 (4.1. Experimental Setup), p. 1 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 7 (4.3. Zero-Shot Generalization), p. 7 (4.3. Zero-Shot Generalization), p. 8 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), results p. 8 (Figure/Table caption), p. 8 (4.4. Ablation Study), p. 7 (4.3. Zero-Shot Generalization), p. 7 (4.1. Experimental Setup), p. 6 (Figure/Table caption), p. 6 (4.1. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
