# Evaluation - PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=hQWwTWGAyu; PDF retrieval source: https://openreview.net/pdf/859969c4505c940b506d06cb01ee1bce1e5d07d0.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (4.4. Evaluation Results), p. 8 (4.4. Evaluation Results), p. 9 (4.5. Ablation and Analysis), p. 9 (4.5. Ablation and Analysis), p. 10 (4.5. Ablation and Analysis)): Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances reconstruction details (see the zoomed-in region). The improveme ...

## Evaluation Body Digest

- **p. 8 / 4.5. Ablation and Analysis - extractive body cue:** By default we train on the 256 × 256 SceneNet-RGBD dataset and report the average metrics on the seven unseen test sets with single-step inference.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Average results on 7 real-world evaluation datasets with 3,444 samples.
- **p. 6 / 4.3. Evaluation Setup and Metrics - extractive body cue:** To assess the zero-shot generalization of our model, we evaluate on seven commonly used real-world datasets: DIODE (Vasiljevic et al., 2019), KITTI (Geiger et al., ...
- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** To save compute, the 512 × 512 models in this part are fine-tuned on a 6dataset subset (Hypersim, VKITTI2, UrbanSyn, Synscapes, TartanAir, and OmniWorldGame; 1.48M ...
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** These span diverse environments, from indoor rooms to complex outdoor driving scenes.
- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** Trained on 256 × 256 SceneNet RGB-D and averaged over the seven unseen test sets with singlestep inference (PointDiT-L).
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** For a fair comparison, we benchmark against several state-of-the-art baselines, evaluating their publicly available pre-trained weights under the same preprocessing and cropping protocol.
- **p. 8 / 4.4. Evaluation Results - extractive body cue:** Our PointDiT is significantly better in terms of reconstructing thin structures (1st row), transparent objects (2nd rows), and maintaining a more accurate relative scale across ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Datasets (p. 6); 4.2. Implementation Details (p. 6); 4.3. Evaluation Setup and Metrics (p. 6); 4.4. Evaluation Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances reconstruction details ... | p. 7 (Figure/Table caption) |
| 4.4. Evaluation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our largest model, PointDiT-H, achieves the best depth accuracy (Reld and δd 1) and the best point map δp 1, while PointDiT achieves the ... | p. 7 (4.4. Evaluation Results) |
| 4.4. Evaluation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, more steps steadily improve the boundary metric BF1, while Rel and δ1 remain stable, since a single step already ... | p. 8 (4.4. Evaluation Results) |
| 4.5. Ablation and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Even without any pretrained image backbone (i.e., with plain linear embeddings), our model already achieves decent results. | p. 9 (4.5. Ablation and Analysis) |
| 4.5. Ablation and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | They further improve the accuracy metrics (Rel and δ1), confirming that our model readily benefits from geometry-aware features. | p. 9 (4.5. Ablation and Analysis) |

## Dataset / Benchmark Role

- **p. 8 / 4.5. Ablation and Analysis - extractive body cue:** By default we train on the 256 × 256 SceneNet-RGBD dataset and report the average metrics on the seven unseen test sets with single-step inference.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Average results on 7 real-world evaluation datasets with 3,444 samples.
- **p. 6 / 4.3. Evaluation Setup and Metrics - extractive body cue:** To assess the zero-shot generalization of our model, we evaluate on seven commonly used real-world datasets: DIODE (Vasiljevic et al., 2019), KITTI (Geiger et al., ...
- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** To save compute, the 512 × 512 models in this part are fine-tuned on a 6dataset subset (Hypersim, VKITTI2, UrbanSyn, Synscapes, TartanAir, and OmniWorldGame; 1.48M ...
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** These span diverse environments, from indoor rooms to complex outdoor driving scenes.
- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** Trained on 256 × 256 SceneNet RGB-D and averaged over the seven unseen test sets with singlestep inference (PointDiT-L).
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** For a fair comparison, we benchmark against several state-of-the-art baselines, evaluating their publicly available pre-trained weights under the same preprocessing and cropping protocol.
- **p. 8 / 4.4. Evaluation Results - extractive body cue:** Our PointDiT is significantly better in terms of reconstructing thin structures (1st row), transparent objects (2nd rows), and maintaining a more accurate relative scale across ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. PointDiT. A minimalist pixel-space Diffusion Trans- former operating directly on raw point map patches, conditioned on image tokens from a pre-trained DINOv3. The ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison with latent diffusion and regression. The two dominant paradigms each have an inherent limitation: (a) the VAE in latent diffusion models introduces ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparisons. Average results on 7 real-world evaluation datasets with 3,444 samples. The image resolution is 512 × 512. Relp and δp 1 are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Single-step feed-forward inference. Single-step results of PointDiT-H from random noise (three seeds) or an all-zeros input. Performance is nearly invariant to the noise, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances reconstruction details (see ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Point map comparisons. Our PointDiT is significantly better in terms of reconstructing thin structures (1st row), transparent objects (2nd rows), and maintaining a ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5. Generative flow matching vs. deterministic regression. (a) The deterministic regressor converges faster at first but soon overfits, while the generative model trains stably ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3. Ablation experiments. Trained on 256 × 256 SceneNet RGB-D and averaged over the seven unseen test sets with single- step inference (PointDiT-L). Our ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | By default we train on the 256 × 256 SceneNet-RGBD dataset and report the average metrics on the seven unseen test sets with single-step ... | embodiment, simulator version and control stack | p. 8 (4.5. Ablation and Analysis), p. 6 (4.2. Implementation Details) |
| Task/environment | Average results on 7 real-world evaluation datasets with 3,444 samples. | reset, timeout, object/scene variation | p. 6 (4.2. Implementation Details), p. 6 (4.3. Evaluation Setup and Metrics) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3. Approach), p. 4 (3.2. Architecture) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.1. Point Map Generation with Flow Matching), p. 5 (3.4. Inference) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We assess prediction quality in both the point map and depth domains using standard metrics (Wang et al., 2025b): • Accuracy (δ1): the percentage ... | definition/direction/unit from same section | p. 7 (4.3. Evaluation Setup and Metrics) |
| Our largest model, PointDiT-H, achieves the best depth accuracy (Reld and δd 1) and the best point map δp 1, while PointDiT achieves the ... | definition/direction/unit from same section | p. 7 (4.4. Evaluation Results) |
| However, we find that this alone yields unsatisfactory results for point map generation, where we measure per-point accuracy. | definition/direction/unit from same section | p. 9 (4.5. Ablation and Analysis) |
| This is expected, since point map prediction requires pixel-perfect accuracy, and a larger patch size tends to discard more high-frequency detail. | definition/direction/unit from same section | p. 10 (4.5. Ablation and Analysis) |
| PointDiT-H attains the best depth accuracy (Reld and δd 1) and PointDiT the sharpest boundaries (BF1) among all methods, while being far more efficient ... | definition/direction/unit from same section | p. 6 (4.2. Implementation Details) |
| Supporting a variable number of inference steps with one network underscores the flexibility of our approach. | definition/direction/unit from same section | p. 8 (4.4. Evaluation Results) |
| They further improve the accuracy metrics (Rel and δ1), confirming that our model readily benefits from geometry-aware features. | definition/direction/unit from same section | p. 9 (4.5. Ablation and Analysis) |
| Table 1. Comparisons. Average results on 7 real-world evaluation datasets with 3,444 samples. The image resolution is 512 × 512. Relp and δp 1 ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For a fair comparison, we benchmark against several state-of-the-art baselines, evaluating their publicly available pre-trained weights under the same preprocessing and cropping protocol. | comparison identity and matched condition | p. 7 (4.3. Evaluation Setup and Metrics) |
| Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances reconstruction details ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Remarkably, even with a single step, PointDiT-H already outperforms prior methods (Table 1), at a fraction of the inference cost of latent diffusion models. | comparison identity and matched condition | p. 8 (4.4. Evaluation Results) |
| We show additional depth comparisons in the appendix (Figure 7). | comparison identity and matched condition | p. 8 (4.4. Evaluation Results) |
| Even without any pretrained image backbone (i.e., with plain linear embeddings), our model already achieves decent results. | comparison identity and matched condition | p. 9 (4.5. Ablation and Analysis) |
| Overall, the generative formulation improves the boundary metric BF1 from 10.90 to 13.92 under this controlled comparison. of the two models. | comparison identity and matched condition | p. 9 (4.5. Ablation and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The ablation results discussed so far use only the flow matching loss (Equation (5)), which is already highly effective at recovering high-quality geometry. | component/input/data sensitivity | p. 10 (4.5. Ablation and Analysis) |
| All variants are pre-trained at 256 × 256 for 30 epochs (including a 5-epoch warmup) and then fine-tuned at 512×512, scaling the number of ... | component/input/data sensitivity | p. 6 (4.2. Implementation Details) |
| Our model predicts affine-invariant point maps, from which affine-invariant depth maps are obtained by extracting the z-component of each point. | component/input/data sensitivity | p. 7 (4.3. Evaluation Setup and Metrics) |
| Even without any pretrained image backbone (i.e., with plain linear embeddings), our model already achieves decent results. | component/input/data sensitivity | p. 9 (4.5. Ablation and Analysis) |
| We use the same patch size of 16 for all variants. | component/input/data sensitivity | p. 6 (4.2. Implementation Details) |
| PointDiTL attains comparable boundary quality at lower cost, and our smallest variant, PointDiT-B, stays competitive with fewer parameters. | component/input/data sensitivity | p. 7 (4.4. Evaluation Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Inspired by JiT (Li & He, 2026), we introduce a minimalist pixel-space diffusion framework that trains directly on the raw point map space. | Figure 3. Different diffusion sampling steps. Our single-step diffusion already significantly outperforms prior works, and in- creasing the sampling steps further enhances reconstruction details ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (4.4. Evaluation Results), p. 8 (4.4. Evaluation Results), p. 9 (4.5. Ablation and Analysis), p. 9 (4.5. Ablation and Analysis), p. 10 (4.5. Ablation and Analysis) |
| Primary metric/result | Our largest model, PointDiT-H, achieves the best depth accuracy (Reld and δd 1) and the best point map δp 1, while PointDiT achieves the ... | numeric claim only at cited anchor | p. 7 (4.4. Evaluation Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Implementation Details - extractive body cue:** Average results on 7 real-world evaluation datasets with 3,444 samples.
- **p. 6 / 4.2. Implementation Details - extractive body cue:** All variants are pre-trained at 256 × 256 for 30 epochs (including a 5-epoch warmup) and then fine-tuned at 512×512, scaling the number of GPUs ...
- **p. 7 / 4.4. Evaluation Results - extractive body cue:** Input MoGe-2 GT GeometryCrafter PointDiT (1 step) PointDiT (2 steps) PointDiT (3 steps) PointDiT (4 steps) Figure 3.
- **p. 9 / 4.5. Ablation and Analysis - extractive body cue:** PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 Epoch 10 12 ...
- **p. 10 / 4.5. Ablation and Analysis - extractive body cue:** Setting Relp ↓ δp 1 ↑ Reld ↓ δd 1 ↑ BF1 ↑ (a) Prediction target v-pred 35.44 30.03 24.07 58.21 0.46 x-pred 9.29 91.18 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Comparison with latent diffusion and regression. The two dominant paradigms each have an inherent limitation: (a) the VAE in latent diffusion models ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. PointDiT. A minimalist pixel-space Diffusion Trans- former operating directly on raw point map patches, conditioned on image tokens from a pre-trained DINOv3. ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | The same flexibility makes it natural to explore multi-view generation, alternative 3D representations, and richer conditioning signals (e.g., camera parameters), which we view as ... | p. 10 (5. Conclusion) |
| body limitation/failure cue | While our framework delivers robust geometric estimation, it is currently trained at fixed resolutions (256 × 256 and 512 × 512); mixed-resolution training is ... | p. 10 (5. Conclusion) |
| body limitation/failure cue | In Table 2, we study the model's sensitivity to noise sampling in single-step inference, and find it highly robust across stochastic initializations. | p. 7 (4.4. Evaluation Results) |
| body limitation/failure cue | Performance is nearly invariant to the noise, with all-zeros matching or slightly exceeding stochastic sampling, indicating the model learns to be robust to different ... | p. 7 (4.3. Evaluation Setup and Metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the AdamW optimizer (Loshchilov & Hutter, 2019), with a learning rate schedule and hyperparameters consistent with JiT (Li & He, 2026). | p. 6 (4.2. Implementation Details) |
| More implementation details are provided in the appendix (Section A.3). | p. 6 (4.2. Implementation Details) |
| Different diffusion sampling steps. | p. 7 (4.4. Evaluation Results) |
| Across different random noise seeds, performance fluctuations are negligible, with 7 | p. 7 (4.4. Evaluation Results) |
| Supporting a variable number of inference steps with one network underscores the flexibility of our approach. | p. 8 (4.4. Evaluation Results) |
| Thanks to its flow matching formulation, PointDiT can also benefit from additional inference steps using the same model. | p. 8 (4.4. Evaluation Results) |
| To save compute, the 512 × 512 models in this part are fine-tuned on a 6dataset subset (Hypersim, VKITTI2, UrbanSyn, Synscapes, TartanAir, and OmniWorldGame; ... | p. 10 (4.5. Ablation and Analysis) |
| Formally, given an input image c ∈RH×W ×3, our goal is to estimate the corresponding point map x ∈ RH×W ×3, in which each ... | p. 3 (3. Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison with latent diffusion and regression. The two dominant paradigms each have an inherent limitation: (a) the VAE in latent diffusion models introduces ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. PointDiT. A minimalist pixel-space Diffusion Trans- former operating directly on raw point map patches, conditioned on image tokens from a pre-trained DINOv3. The ...
- **p. 10 / 5. Conclusion - extractive body cue:** The same flexibility makes it natural to explore multi-view generation, alternative 3D representations, and richer conditioning signals (e.g., camera parameters), which we view as exciting ...
- **p. 10 / 5. Conclusion - extractive body cue:** While our framework delivers robust geometric estimation, it is currently trained at fixed resolutions (256 × 256 and 512 × 512); mixed-resolution training is a ...
- **p. 7 / 4.4. Evaluation Results - extractive body cue:** In Table 2, we study the model's sensitivity to noise sampling in single-step inference, and find it highly robust across stochastic initializations.
- **p. 7 / 4.3. Evaluation Setup and Metrics - extractive body cue:** Performance is nearly invariant to the noise, with all-zeros matching or slightly exceeding stochastic sampling, indicating the model learns to be robust to different noise ...

- **Evidence anchors reviewed:** datasets p. 8 (4.5. Ablation and Analysis), p. 6 (4.2. Implementation Details), p. 6 (4.3. Evaluation Setup and Metrics), p. 10 (4.5. Ablation and Analysis), p. 7 (4.3. Evaluation Setup and Metrics), p. 10 (4.5. Ablation and Analysis), metrics p. 7 (4.3. Evaluation Setup and Metrics), p. 7 (4.4. Evaluation Results), p. 9 (4.5. Ablation and Analysis), p. 10 (4.5. Ablation and Analysis), p. 6 (4.2. Implementation Details), p. 8 (4.4. Evaluation Results), baselines p. 7 (4.3. Evaluation Setup and Metrics), p. 7 (Figure/Table caption), p. 8 (4.4. Evaluation Results), p. 8 (4.4. Evaluation Results), p. 9 (4.5. Ablation and Analysis), p. 9 (4.5. Ablation and Analysis), results p. 7 (Figure/Table caption), p. 7 (4.4. Evaluation Results), p. 8 (4.4. Evaluation Results), p. 9 (4.5. Ablation and Analysis), p. 9 (4.5. Ablation and Analysis), p. 10 (4.5. Ablation and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
