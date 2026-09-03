# Evaluation - Dexterous World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. Qualitative Results), p. 6 (4.1. Comparison), p. 8 (4.3. Ablation Study), p. 6 (4.1. Comparison), p. 7 (4.2. Qualitative Results), p. 7 (4.1. Comparison)): Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world interactions enhance generalization.

## Evaluation Body Digest

- **p. 6 / 4.1. Comparison - extractive body cue:** Despite real-world scenes with dynamic view being completely unseen during training, and the absence of any training samples involving opening a window, DWM successfully generates ...
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** Collecting such triplets in real-world environments is challenging in practice, as it would require capturing both a static scene and a dynamic human-object interaction under ...
- **p. 7 / 4.1. Comparison - extractive body cue:** Notably, our method generalizes well to completely unseen real-world scenes, producing coherent action-conditioned dynamics such as opening a sliding window.
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** To this end, we develop a dedicated data construction protocol to collect a real-world dataset for evaluation under dynamic viewpoints.
- **p. 6 / 4.1. Comparison - extractive body cue:** 3 shows comparisons on synthetic and real-world scenes captured in dynamic views.
- **p. 7 / 4.1. Comparison - extractive body cue:** Quantitative comparisons on synthetic and real-world datasets.
- **p. 8 / 4.2. Qualitative Results - extractive body cue:** Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world interactions enhance generalization.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This is notable given that the real-world training data includes only static-camera interactions, demonstrating strong generalization to more complex real-world scenarios.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 3.3. Paired Interaction Video Dataset Construction (p. 5); 3.4. Action Evaluation with DWM (p. 6); 4. Experiments (p. 6); 4.2. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Qualitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world interactions enhance ... | p. 8 (4.2. Qualitative Results) |
| 4.1. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, where our method achieves superior performance across all metrics. | p. 6 (4.1. Comparison) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, incorporating real-world data consistently improves performance on most metrics, not only on synthetic test sequences but also on Aria-captured real-world data, which includes ... | p. 8 (4.3. Ablation Study) |
| 4.1. Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. | p. 6 (4.1. Comparison) |
| 4.2. Qualitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The model simulates outcomes for multiple action candidates and scores each based on its proximity to the desired goal. | p. 7 (4.2. Qualitative Results) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Comparison - extractive body cue:** Despite real-world scenes with dynamic view being completely unseen during training, and the absence of any training samples involving opening a window, DWM successfully generates ...
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** Collecting such triplets in real-world environments is challenging in practice, as it would require capturing both a static scene and a dynamic human-object interaction under ...
- **p. 7 / 4.1. Comparison - extractive body cue:** Notably, our method generalizes well to completely unseen real-world scenes, producing coherent action-conditioned dynamics such as opening a sliding window.
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** To this end, we develop a dedicated data construction protocol to collect a real-world dataset for evaluation under dynamic viewpoints.
- **p. 6 / 4.1. Comparison - extractive body cue:** 3 shows comparisons on synthetic and real-world scenes captured in dynamic views.
- **p. 7 / 4.1. Comparison - extractive body cue:** Quantitative comparisons on synthetic and real-world datasets.
- **p. 8 / 4.2. Qualitative Results - extractive body cue:** Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world interactions enhance generalization.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This is notable given that the real-world training data includes only static-camera interactions, demonstrating strong generalization to more complex real-world scenarios.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Dexterous World Models predict egocentric visual dynamics of static 3D scenes, driven by dexterous hand manipulations.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview. DWM simulates egocentric visual dynamics induced by embodied actions within a given static 3D scene. We instantiate it as a video diffusion ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparisons on synthetic and real-world datasets. Our method consistently achieves the best performance across all metrics and settings, demonstrating superior realism and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison on synthetic and real-world scenes with dynamic view. DWM successfully generates physically plausible simulations with dynamic view changes corresponding to the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparison on real-world scenes with static camera. Our method produces realistic interactions with consistent scene dynamics. Baselines fail to perform meaningful actions ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Navigation-manipulation disentanglement. Without hand-motion input, DWM simulates navigation only. Conditioning on hand motion enables the model to generate action-induced visual dynamics, highlighting navigation-manipulation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation on training data composition. Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation on hand-motion conditioning. We demonstrate the effectiveness of spatially aligned hand-mesh conditioning.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Despite real-world scenes with dynamic view being completely unseen during training, and the absence of any training samples involving opening a window, DWM successfully ... | embodiment, simulator version and control stack | p. 6 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction) |
| Task/environment | Collecting such triplets in real-world environments is challenging in practice, as it would require capturing both a static scene and a dynamic human-object interaction ... | reset, timeout, object/scene variation | p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 7 (4.1. Comparison) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.3. Paired Interaction Video Dataset Construction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Specifically, we report LPIPS [57] and DreamSim [12] scores for perceptual similarity, and PSNR and SSIM for pixel-level quality. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| This formulation enables goal-driven action selection via simulation, without requiring explicit reward functions or real-world trials. | definition/direction/unit from same section | p. 6 (3.4. Action Evaluation with DWM) |
| The model simulates outcomes for multiple action candidates and scores each based on its proximity to the desired goal. | definition/direction/unit from same section | p. 7 (4.2. Qualitative Results) |
| DWM successfully generates physically plausible simulations with dynamic view changes corresponding to the input hand actions. | definition/direction/unit from same section | p. 7 (4.1. Comparison) |
| We demonstrate the effectiveness of spatially aligned hand-mesh conditioning. | definition/direction/unit from same section | p. 8 (4.2. Qualitative Results) |
| DWM accurately manipulates the intended target object based on variations in hand-action condition. | definition/direction/unit from same section | p. 8 (4.2. Qualitative Results) |
| To incorporate such effects, we additionally use real-world human-object interaction videos recorded from fixed cameras [58], where Ct = C0 for all t ∈1, ... | definition/direction/unit from same section | p. 5 (3.3. Paired Interaction Video Dataset Construction) |
| Our construction leverages fixed-camera setups to approximate this pairing, enabling supervision without requiring separate static captures or 3D scene reconstruction. | definition/direction/unit from same section | p. 5 (3.3. Paired Interaction Video Dataset Construction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. | comparison identity and matched condition | p. 6 (4.1. Comparison) |
| 4 compares our method with baselines in a real-world scene with a static camera. | comparison identity and matched condition | p. 6 (4.1. Comparison) |
| Baselines fail to perform meaningful actions or hallucinate incorrect interactions. | comparison identity and matched condition | p. 7 (4.1. Comparison) |
| Without hand-motion input, DWM simulates navigation only. | comparison identity and matched condition | p. 7 (4.2. Qualitative Results) |
| Ablation on hand-motion conditioning. | comparison identity and matched condition | p. 8 (4.2. Qualitative Results) |
| Ablation on training data composition. | comparison identity and matched condition | p. 8 (4.2. Qualitative Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablation on hand-motion conditioning. We demonstrate the effectiveness of spatially aligned hand-mesh conditioning. | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We set the mask as ones and finetune the model with our dataset without the hand-mesh video condition. | component/input/data sensitivity | p. 6 (4. Experiments) |
| This formulation enables goal-driven action selection via simulation, without requiring explicit reward functions or real-world trials. | component/input/data sensitivity | p. 6 (3.4. Action Evaluation with DWM) |
| Without hand-motion input, DWM simulates navigation only. | component/input/data sensitivity | p. 7 (4.2. Qualitative Results) |
| Without hand motion conditioning, DWM operates as a pure navigator. | component/input/data sensitivity | p. 7 (4.2. Qualitative Results) |
| Ablation on training data composition. | component/input/data sensitivity | p. 8 (4.2. Qualitative Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video ... | Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world interactions enhance ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. Qualitative Results), p. 6 (4.1. Comparison), p. 8 (4.3. Ablation Study), p. 6 (4.1. Comparison), p. 7 (4.2. Qualitative Results), p. 7 (4.1. Comparison) |
| Primary metric/result | 1, where our method achieves superior performance across all metrics. | numeric claim only at cited anchor | p. 6 (4.1. Comparison) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive body cue:** We construct a benchmark of 144 samples, each consisting of a static scene video, a hand-mesh video, a ground-truth interaction video.
- **p. 6 / 4. Experiments - extractive body cue:** In the static camera setting (Real-World Static), we use 48 samples unseen during training from TASTE-Rob [58].
- **p. 6 / 4. Experiments - extractive body cue:** For the dynamic camera setting (Real-World Dynamic), we use 48 samples from our custom captured dataset by Aria Glasses.
- **p. 8 / 4.2. Qualitative Results - extractive body cue:** Rollout #1 Rollout #2 Rollout #3 Rollout #4 Goal Image Text Prompt "I close the microwave." CLIP: 21.096 LPIPS : 0.298 CLIP: 21.288 LPIPS: 0.309 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest. | p. 6 (4.1. Comparison) |
| body limitation/failure cue | InterDyn [2] produces spatially aligned hands with the input masks but fails to model resulting object dynamics. | p. 6 (4.1. Comparison) |
| body limitation/failure cue | Baselines fail to perform meaningful actions or hallucinate incorrect interactions. | p. 7 (4.1. Comparison) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use CogVideoX [52] for denoising and set the noise strength to 0.75 with 50 inference steps. | p. 6 (4. Experiments) |
| For each sample in our benchmark, we generate three videos with random seeds and report the averaged results. | p. 6 (4. Experiments) |
| Hand mask instead provides pixel-level alignment by encoding binary hand segmentation videos via the same VAE encoder. | p. 8 (4.3. Ablation Study) |
| VAE Encoder Hand Video Latents Static Video Latents Text Encoder Noisy Video Latents Patch Embedding VAE Decoder "The person extends the right arm and ... | p. 4 (3.1. Formulation of Dexterous World Models) |
| Importantly, we instantiate the generative process as a latent video diffusion model [36] conditioned on two egocentric signals: (1) a static-scene video, Π(S0; C1:F ... | p. 4 (3.2. Scene-Action-Conditioned Video Diffusion) |
| During inference, the model iteratively denoises zt to obtain ˆz0, which is decoded by VAE into a realistic interaction video. | p. 5 (3.2. Scene-Action-Conditioned Video Diffusion) |
| The model operates in the latent space of a pretrained video variational autoencoder (VAE) [22, 52], which encodes an input video into latent tensors ... | p. 5 (3.2. Scene-Action-Conditioned Video Diffusion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Comparison - extractive body cue:** CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest.
- **p. 6 / 4.1. Comparison - extractive body cue:** InterDyn [2] produces spatially aligned hands with the input masks but fails to model resulting object dynamics.
- **p. 7 / 4.1. Comparison - extractive body cue:** Baselines fail to perform meaningful actions or hallucinate incorrect interactions.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 7 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 6 (4.1. Comparison), p. 7 (4.1. Comparison), metrics p. 6 (4. Experiments), p. 6 (3.4. Action Evaluation with DWM), p. 7 (4.2. Qualitative Results), p. 7 (4.1. Comparison), p. 8 (4.2. Qualitative Results), p. 8 (4.2. Qualitative Results), baselines p. 6 (4.1. Comparison), p. 6 (4.1. Comparison), p. 7 (4.1. Comparison), p. 7 (4.2. Qualitative Results), p. 8 (4.2. Qualitative Results), p. 8 (4.2. Qualitative Results), results p. 8 (4.2. Qualitative Results), p. 6 (4.1. Comparison), p. 8 (4.3. Ablation Study), p. 6 (4.1. Comparison), p. 7 (4.2. Qualitative Results), p. 7 (4.1. Comparison).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. (p. 6, 4.1. Comparison).
- **Metric evidence:** 1, where our method achieves superior performance across all metrics. (p. 6, 4.1. Comparison).
- **Baseline/ablation evidence:** Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. (p. 6, 4.1. Comparison).
- **Failure/negative evidence:** CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest. (p. 6, 4.1. Comparison).
