# Evaluation - PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=AnofTirXgv; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/331054. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption), p. 7 (5.2. Depth Fidelity Evaluation), p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 24 (Figure/Table caption)): By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an average success rate of 92.5% and ...

## Evaluation Body Digest

- **p. 8 / 5.3. Downstream Application Evaluation - extractive PDF cue:** We establish a benchmark of 6 diverse manipulation tasks (Tab.3) across two robotic platforms to evaluate challenging physical properties.
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** We train on ByteCameraDepth (Liu et al., 2025), comprising real-world raw depth captured from 7 cameras across 10 modes in 7 diverse scene categories.
- **p. 8 / 5.3. Downstream Application Evaluation - extractive PDF cue:** Assessing the impact of removing SPR and BND on Invalidation IoU and Robot SR.
- **p. 7 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when compared to overfitting-prone baselines.
- **p. 7 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** By leveraging generic VFM priors rather than fitting specific dataset statistics, PRISM effectively reasons about noise generation through materialcorrelated visual patterns rather than superficial domain ...
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** We utilize the provided models to construct aligned sim-real pairs and define the ground-truth invalidation mask by identifying native sensor failures (zeros or NaNs) in ...
- **p. 8 / 5.3. Downstream Application Evaluation - extractive PDF cue:** NRG Only w/o SPR w/o BND PRISM Full 0.08 0.10 0.12 0.14 Overall MAE 0.118 0.095 0.098 0.076 -36% (i) Overall MAE NRG Only w/o ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 15. Component Ablation Study. We evaluate the contribution of Semantic-Physics Reasoner (SPR) and Bimodal Noise Disentangler (BND) against the pure Noise Residual Generator (NRG) ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 6); 5.1. Experimental Settings (p. 6); 5.2. Depth Fidelity Evaluation (p. 7); 5.3. Downstream Application Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Downstream Application Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an ... | p. 8 (5.3. Downstream Application Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Cross-policy Sim2Real generalization. We report the average success rate (%) across all 6 tasks using three different policy architectures. PRISM consistently outperforms ... | p. 8 (Figure/Table caption) |
| 5.2. Depth Fidelity Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Specifically, our Hierarchical PositivePrioritized Supervision yields high Invalidation IoU/F1 by overcoming mask sparsity, while the disentangled NRG achieves the lowest valid-region MAE/RMSE, effectively preventing ... | p. 7 (5.2. Depth Fidelity Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7. Semantics Efficacy. Comparing generic vs. geometric priors. 3D VFMs show superior material awareness. Impact of Causal Architecture. We treat the diffusion-based NRG ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 16. VFM Backbone Comparison in SPR. We compare CNNs, Generic ViTs, and 3D VFMs. Robot SR refers to the average success rate across ... | p. 24 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 5.3. Downstream Application Evaluation - extractive PDF cue:** We establish a benchmark of 6 diverse manipulation tasks (Tab.3) across two robotic platforms to evaluate challenging physical properties.
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** We train on ByteCameraDepth (Liu et al., 2025), comprising real-world raw depth captured from 7 cameras across 10 modes in 7 diverse scene categories.
- **p. 8 / 5.3. Downstream Application Evaluation - extractive PDF cue:** Assessing the impact of removing SPR and BND on Invalidation IoU and Robot SR.
- **p. 7 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when compared to overfitting-prone baselines.
- **p. 7 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** By leveraging generic VFM priors rather than fitting specific dataset statistics, PRISM effectively reasons about noise generation through materialcorrelated visual patterns rather than superficial domain ...
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** We utilize the provided models to construct aligned sim-real pairs and define the ground-truth invalidation mask by identifying native sensor failures (zeros or NaNs) in ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The Anatomy of Depth Perception and Modeling. (a) The Reality Gap: Unlike pristine simulation, real-world physical sensing exhibits a bimodal noise distribution: black ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The overview of PRISM framework. The PRISM orchestrates three synergistic modules: the SPR extracts material-aware priors, the BND predicts sensing invalidation, and the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of the PRISM-enabled Sim-to-Real Pipeline. (a) Simulation Data Collection: Large-scale expert demonstrations are collected in a simulator. (b) Offline Depth Enhancement: PRISM ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Hardware Requirement of Downstream Evaluation. The real-world setup consists of two platforms: Franka Research 3 for specular and deformable manipulation tasks, and Realman ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Cross-camera synthesis generalization. Models trained on ByteCameraDepth are directly tested on NYU-Depth-v2 (Zero- shot in Kinect Camera) to assess robustness.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Multi-task manipulation success rates with RISE policy. We evaluate 6 tasks with diverse properties: Specular (☼), Deformable (<), Articulated (), and Long-Horizon (7). ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We establish a benchmark of 6 diverse manipulation tasks (Tab.3) across two robotic platforms to evaluate challenging physical properties. | embodiment, simulator version and control stack | p. 8 (5.3. Downstream Application Evaluation), p. 6 (5.1. Experimental Settings) |
| Task/environment | We train on ByteCameraDepth (Liu et al., 2025), comprising real-world raw depth captured from 7 cameras across 10 modes in 7 diverse scene categories. | reset, timeout, object/scene variation | p. 6 (5.1. Experimental Settings), p. 8 (5.3. Downstream Application Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 4 (3.2. Bimodal Noise Disentangler) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Semantic-Physics Reasoner), p. 5 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| NRG Only w/o SPR w/o BND PRISM Full 0.08 0.10 0.12 0.14 Overall MAE 0.118 0.095 0.098 0.076 -36% (i) Overall MAE NRG Only ... | definition/direction/unit from same section | p. 8 (5.3. Downstream Application Evaluation) |
| Table 15. Component Ablation Study. We evaluate the contribution of Semantic-Physics Reasoner (SPR) and Bimodal Noise Disentangler (BND) against the pure Noise Residual Generator ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Inaccuracy MAE ↓ RMSE ↓AbsRel ↓δ < 1.25 ↑ IoU ↑ F1 ↑ Recall ↑MAE ↓RMSE ↓Acc-δ ↑ GazeboDR 0.203 0.258 0.167 0.724 - ... | definition/direction/unit from same section | p. 7 (5.1. Experimental Settings) |
| Multi-task manipulation success rates with RISE policy. | definition/direction/unit from same section | p. 8 (5.2. Depth Fidelity Evaluation) |
| Figure 7. Semantics Efficacy. Comparing generic vs. geometric priors. 3D VFMs show superior material awareness. Impact of Causal Architecture. We treat the diffusion-based NRG ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 16. VFM Backbone Comparison in SPR. We compare CNNs, Generic ViTs, and 3D VFMs. Robot SR refers to the average success rate across ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation (detection of sensor failures), and Measurement Inaccuracy (precision in valid regions). | definition/direction/unit from same section | p. 7 (5.1. Experimental Settings) |
| Figure 9. Hardware Requirement of Downstream Evaluation. The real-world setup consists of two platforms: Franka Research 3 for precision tasks, and Realman RM75 for ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when compared to overfitting-prone baselines. | comparison identity and matched condition | p. 7 (5.2. Depth Fidelity Evaluation) |
| PRISM consistently outperforms baselines. | comparison identity and matched condition | p. 8 (5.2. Depth Fidelity Evaluation) |
| By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an ... | comparison identity and matched condition | p. 8 (5.3. Downstream Application Evaluation) |
| Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Note: Baselines marked with ‘-' do not support separate invalidation masks from continuous noise. | comparison identity and matched condition | p. 7 (5.1. Experimental Settings) |
| Table 17. Progressive Ablation of H-PPS. We add components sequentially to the standard BCE baseline. Boundary-IoU evaluates the precision of artifact edges (within 5px). ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 7. Semantics Efficacy. Comparing generic vs. geometric priors. 3D VFMs show superior material awareness. Impact of Causal Architecture. We treat the diffusion-based NRG ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 17. Progressive Ablation of H-PPS. We add components sequentially to the standard BCE baseline. Boundary-IoU evaluates the precision of artifact edges (within 5px). ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 15. Component Ablation Study. We evaluate the contribution of Semantic-Physics Reasoner (SPR) and Bimodal Noise Disentangler (BND) against the pure Noise Residual Generator ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Figure 3. Overview of the PRISM-enabled Sim-to-Real Pipeline. (a) Simulation Data Collection: Large-scale expert demonstrations are collected in a simulator. (b) Offline Depth Enhancement: ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 18. Sensitivity Analysis. We analyze the trade-offs for Positive Weight wpos (Left) and Initial Mining Ratio γstart (Right). The optimal configurations (wpos = ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated ... | By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption), p. 7 (5.2. Depth Fidelity Evaluation), p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Primary metric/result | Table 4. Cross-policy Sim2Real generalization. We report the average success rate (%) across all 6 tasks using three different policy architectures. PRISM consistently outperforms ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Training proceeds in two phases totaling 100 epochs: first freezing the VAE and U-Net to optimize only the ControlNet, followed by joint fine-tuning where the ...
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Inference utilizes DDIM sampling (50 steps, 9.0 scale).
- **p. 7 / 5.1. Experimental Settings - extractive PDF cue:** Inaccuracy MAE ↓ RMSE ↓AbsRel ↓δ < 1.25 ↑ IoU ↑ F1 ↑ Recall ↑MAE ↓RMSE ↓Acc-δ ↑ GazeboDR 0.203 0.258 0.167 0.724 - - ...
- **p. 8 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** We evaluate 6 tasks with diverse properties: Specular (☼), Deformable (<), Articulated (), and Long-Horizon (7).
- **p. 8 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** Results are reported as mean ± std across 3 random seeds (/20 trials).
- **p. 8 / 5.2. Depth Fidelity Evaluation - extractive PDF cue:** Task Properties Explicit Analytical Modeling Implicit Data-Driven Modeling ☼<  7 GazeboDR DepthSynth ActiveStereo DCL-Depth Stable-S2R PRISM Can-to-Plate ✓ 18.7±0.6 20.0±0.0 20.0±0.0 20.0±0.0 20.0±0.0 20.0±0.0 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | While PRISM demonstrates strong capabilities in simulateddepth enhancement, it possesses certain limitations. | p. 9 (7. Limitations) |
| body limitation/failure cue | Second, the current per-frame generation pipeline does not explicitly enforce temporal consistency for highly dynamic scenes, leaving flickering noise across frames as a key ... | p. 9 (7. Limitations) |
| body limitation/failure cue | We utilize the provided models to construct aligned sim-real pairs and define the ground-truth invalidation mask by identifying native sensor failures (zeros or NaNs) ... | p. 6 (5.1. Experimental Settings) |
| body limitation/failure cue | Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Articulated tasks on a Realman RM75 arm test robustness against translucent refraction, transparent obstacles, and severe occlusions during long-horizon behaviors like interacting with a ... | p. 8 (5.3. Downstream Application Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training proceeds in two phases totaling 100 epochs: first freezing the VAE and U-Net to optimize only the ControlNet, followed by joint fine-tuning where ... | p. 6 (5.1. Experimental Settings) |
| Results are reported as mean ± std across 3 random seeds (/20 trials). | p. 8 (5.2. Depth Fidelity Evaluation) |
| Implemented in PyTorch on 8 NVIDIA H200 GPUs, PRISM trains on 5122 images with a batch size of 32. | p. 6 (5.1. Experimental Settings) |
| First, a Frozen 3DVFM Backbone extracts patch tokens ΦVFM(I) that encode implicit semantic-physical properties. | p. 3 (3.1. Semantic-Physics Reasoner) |
| Modern VFMs implicitly encode richer semantic-physical correspondences, learning to associate visual contexts with intrinsic physical behaviors (Lin et al., 2025). | p. 3 (2.3. Visual Foundation Models as Semantic Priors) |
| During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim ... | p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |
| The training objective is masked to compute gradients strictly within valid sensor regions: LNRG = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t, cctl)∥2 2 ⊙(1 -ˆ ... | p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |
| (c) Depth-Aware Policy Learning: A modified robotic policy, equipped with a dedicated depth encoder, is trained on the enhanced dataset to learn robustness against ... | p. 5 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation ...
- **p. 9 / 7. Limitations - extractive PDF cue:** While PRISM demonstrates strong capabilities in simulateddepth enhancement, it possesses certain limitations.
- **p. 9 / 7. Limitations - extractive PDF cue:** Second, the current per-frame generation pipeline does not explicitly enforce temporal consistency for highly dynamic scenes, leaving flickering noise across frames as a key open ...
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** We utilize the provided models to construct aligned sim-real pairs and define the ground-truth invalidation mask by identifying native sensor failures (zeros or NaNs) in ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) to ...
- **p. 8 / 5.3. Downstream Application Evaluation - extractive PDF cue:** Articulated tasks on a Realman RM75 arm test robustness against translucent refraction, transparent obstacles, and severe occlusions during long-horizon behaviors like interacting with a drawer ...

- **PDF anchors reviewed:** datasets p. 8 (5.3. Downstream Application Evaluation), p. 6 (5.1. Experimental Settings), p. 8 (5.3. Downstream Application Evaluation), p. 7 (5.2. Depth Fidelity Evaluation), p. 7 (5.2. Depth Fidelity Evaluation), p. 6 (5.1. Experimental Settings), metrics p. 8 (5.3. Downstream Application Evaluation), p. 24 (Figure/Table caption), p. 7 (5.1. Experimental Settings), p. 8 (5.2. Depth Fidelity Evaluation), p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), baselines p. 7 (5.2. Depth Fidelity Evaluation), p. 8 (5.2. Depth Fidelity Evaluation), p. 8 (5.3. Downstream Application Evaluation), p. 6 (Figure/Table caption), p. 7 (5.1. Experimental Settings), p. 24 (Figure/Table caption), results p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption), p. 7 (5.2. Depth Fidelity Evaluation), p. 9 (Figure/Table caption), p. 24 (Figure/Table caption), p. 24 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
