# PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=AnofTirXgv.
> PDF retrieval source: https://openreview.net/pdf/9655ce373e592ae3473dc14dddd5cc2be47a3b47.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, depth, 3D Vision
- Official paper: https://openreview.net/forum?id=AnofTirXgv
- Full-text retrieval: https://openreview.net/pdf/9655ce373e592ae3473dc14dddd5cc2be47a3b47.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the deployment of simulation-trained policies remains fundamentally bottlenecked by the sim-to-real gap(Jia et al., 2025).를 문제로 두고, To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Real-world physical sensing exhibits complex, heterogeneous noise patterns that deviate significantly from idealized simulation, posing a fundamental bottleneck for sim-to-real transfer.
- **p. 1 / Abstract - extractive body cue:** Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a physics-grounded paradigm that disentangles monolithic noise into two complementary modalities: sensing invalidation and measurement inaccuracy, enabling a tailored treatment ...
- **p. 1 / Abstract - extractive body cue:** Building on this insight, we propose PRISM, a tripartite framework that distills 3D Visual Foundation Model features as rich spatialsemantic priors for physics-based reasoning.
- **p. 1 / Abstract - extractive body cue:** To address the inherent sparsity and class imbalance of invalidation regions, we develop Hierarchical Positive-Prioritized Supervision, integrating multi-scale positive-weighted objectives with a positive-preserving dynamic hard ...
- **p. 1 / 1. Introduction - extractive body cue:** However, the deployment of simulation-trained policies remains fundamentally bottlenecked by the sim-to-real gap(Jia et al., 2025).
- **p. 1 / 1. Introduction - extractive body cue:** (a) The Reality Gap: Unlike pristine simulation, real-world physical sensing exhibits a bimodal noise distribution: black voids and gray residuals.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.
- **p. 2 / 1. Introduction - extractive body cue:** 2) Semantic-Geometric Collaboration: We propose PRISM, a unified framework that distills the rich physical common sense of 3D Visual Foundation Model to drive noise synthesis.
- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive body cue:** The architecture consists of three sequential modules.
- **p. 3 / 3. Methodology - extractive body cue:** We present PRISM, a tripartite framework that synthesizes realistic depth by disentangling sensor noise into physically grounded modalities.
- **p. 5 / 3.4. Hierarchical Positive-Prioritized Supervision - extractive body cue:** To address the extreme class imbalance and ensure precise boundary detection, we propose a supervision strategy comprised of three coupled mechanisms.
- **p. 3 / 2.3. Visual Foundation Models as Semantic Priors - extractive body cue:** State-of-theart architectures like Metric3Dv2 (Hu et al., 2024) and MoGe (Wang et al., 2025b) employ ViT-based encoders to distill invariant geometric representations.
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive body cue:** Stage I: Noise Disentanglement Learning.In addition to the pixel-wise classification, we introduce a Dice Loss to enforce shape compactness and prevent trivial solutions.
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive body cue:** During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Simulation) Task Language (Optional) <Enhanced Triplet> Enhanced Depth Simulated RGB Simulated State Large-scale Dataset from Simulation Simulated State Simulated RGB Simulated Depth Joint Gripper + (a) Large-scale Simulated Demonstrati ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 4 (3.2. Bimodal Noise Disentangler) |
| State/latent | Simulation, Task, Language, Optional, Enhanced, Triplet, Depth, Simulated, RGB, State, Large-scale, Dataset | geometry, map, object/relationship state | p. 5 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 4 (3.2. Bimodal Noise Disentangler), p. 3 (3.1. Semantic-Physics Reasoner) |
| Output/action | The BND maps the concatenated RGB-Depth input X = [I; Dsim] ∈R4×H×W to a pixel-wise sensing invalidation probability map ˆ M ∈[0, 1]H×W . | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. Bimodal Noise Disentangler), p. 3 (3.1. Semantic-Physics Reasoner), p. 5 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |
| Objective/outcome | The BND is optimized to minimize the weighted sum of these objectives over the mined sets: LBND = 4 X l=0 λl X x∈Ωl ℓ(l) bce(x) + λdiceLdice( ˆ Ml, Mgt) ! ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.
- **p. 2 / 1. Introduction - extractive body cue:** 2) Semantic-Geometric Collaboration: We propose PRISM, a unified framework that distills the rich physical common sense of 3D Visual Foundation Model to drive noise synthesis.
- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive body cue:** The architecture consists of three sequential modules.
- **p. 3 / 3. Methodology - extractive body cue:** We present PRISM, a tripartite framework that synthesizes realistic depth by disentangling sensor noise into physically grounded modalities.
- **p. 5 / 3.4. Hierarchical Positive-Prioritized Supervision - extractive body cue:** To address the extreme class imbalance and ensure precise boundary detection, we propose a supervision strategy comprised of three coupled mechanisms.
- **p. 8 / 5.3. Downstream Application Evaluation - extractive body cue:** By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an average ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Cross-policy Sim2Real generalization. We report the average success rate (%) across all 6 tasks using three different policy architectures. PRISM consistently outperforms baselines. ...
- **p. 7 / 5.2. Depth Fidelity Evaluation - extractive body cue:** Specifically, our Hierarchical PositivePrioritized Supervision yields high Invalidation IoU/F1 by overcoming mask sparsity, while the disentangled NRG achieves the lowest valid-region MAE/RMSE, effectively preventing the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption) |
| Embodiment/environment | We establish a benchmark of 6 diverse manipulation tasks (Tab.3) across two robotic platforms to evaluate challenging physical properties. | hardware/simulator version and reset protocol | p. 8 (5.3. Downstream Application Evaluation), p. 6 (5.1. Experimental Settings) |
| Dataset/benchmark | Assessing the impact of removing SPR and BND on Invalidation IoU and Robot SR. | role, split, size and leakage | p. 8 (5.3. Downstream Application Evaluation), p. 6 (5.1. Experimental Settings), p. 8 (5.3. Downstream Application Evaluation), p. 7 (5.2. Depth Fidelity Evaluation) |
| Metric | NRG Only w/o SPR w/o BND PRISM Full 0.08 0.10 0.12 0.14 Overall MAE 0.118 0.095 0.098 0.076 -36% (i) Overall MAE NRG Only w/o SPR w/o BND PRISM Full 0.4 0.6 ... | definition, denominator, direction and uncertainty | p. 8 (5.3. Downstream Application Evaluation), p. 24 (Figure/Table caption), p. 7 (5.1. Experimental Settings) |
| Baseline/ablation | Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when compared to overfitting-prone baselines. | fair input/data/compute/action matching | p. 7 (5.2. Depth Fidelity Evaluation), p. 8 (5.2. Depth Fidelity Evaluation), p. 8 (5.3. Downstream Application Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation ...
- **p. 9 / 7. Limitations - extractive body cue:** While PRISM demonstrates strong capabilities in simulateddepth enhancement, it possesses certain limitations.
- **p. 9 / 7. Limitations - extractive body cue:** Second, the current per-frame generation pipeline does not explicitly enforce temporal consistency for highly dynamic scenes, leaving flickering noise across frames as a key open ...
- **p. 6 / 5.1. Experimental Settings - extractive body cue:** We utilize the provided models to construct aligned sim-real pairs and define the ground-truth invalidation mask by identifying native sensor failures (zeros or NaNs) in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) to ...
- **p. 8 / 5.3. Downstream Application Evaluation - extractive body cue:** Articulated tasks on a Realman RM75 arm test robustness against translucent refraction, transparent obstacles, and severe occlusions during long-horizon behaviors like interacting with a drawer ...
- **p. 8 / 5.3. Downstream Application Evaluation - extractive body cue:** By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an average ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the deployment of simulation-trained policies remains fundamentally bottlenecked by the sim-to-real gap(Jia et al., 2025).를 문제로 두고, To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (2.3. Visual Foundation Models as Semantic Priors) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
