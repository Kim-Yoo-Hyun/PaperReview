# Method - PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=AnofTirXgv; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/331054. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (2.3. Visual Foundation Models as Semantic Priors), p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 4 (3.2. Bimodal Noise Disentangler), p. 5 (3) Sequential Optimization Objectives. Since PRISM is)): The architecture consists of three sequential modules.

## Method Body Digest

- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive PDF cue:** The architecture consists of three sequential modules.
- **p. 3 / 2.3. Visual Foundation Models as Semantic Priors - extractive PDF cue:** State-of-theart architectures like Metric3Dv2 (Hu et al., 2024) and MoGe (Wang et al., 2025b) employ ViT-based encoders to distill invariant geometric representations.
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** Stage I: Noise Disentanglement Learning.In addition to the pixel-wise classification, we introduce a Dice Loss to enforce shape compactness and prevent trivial solutions.
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim to ...
- **p. 4 / 3.2. Bimodal Noise Disentangler - extractive PDF cue:** The architecture is structured into three processing stages:
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** Its objective is the mask-constrained loss restricted to valid regions, shown in Eq.(7).
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** The BND is optimized to minimize the weighted sum of these objectives over the mined sets: LBND = 4 X l=0 λl X x∈Ωl ℓ(l) ...
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** The training objective is masked to compute gradients strictly within valid sensor regions: LNRG = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t, cctl)∥2 2 ⊙(1 -ˆ M) ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.
- **p. 2 / 1. Introduction - extractive PDF cue:** 2) Semantic-Geometric Collaboration: We propose PRISM, a unified framework that distills the rich physical common sense of 3D Visual Foundation Model to drive noise synthesis.
- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive PDF cue:** The architecture consists of three sequential modules.

## Source Evidence Cues

- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive PDF cue:** The architecture consists of three sequential modules.
- **p. 3 / 2.3. Visual Foundation Models as Semantic Priors - extractive PDF cue:** State-of-theart architectures like Metric3Dv2 (Hu et al., 2024) and MoGe (Wang et al., 2025b) employ ViT-based encoders to distill invariant geometric representations.
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** Stage I: Noise Disentanglement Learning.In addition to the pixel-wise classification, we introduce a Dice Loss to enforce shape compactness and prevent trivial solutions.
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim to ...
- **p. 4 / 3.2. Bimodal Noise Disentangler - extractive PDF cue:** The architecture is structured into three processing stages:
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** Its objective is the mask-constrained loss restricted to valid regions, shown in Eq.(7).
- **Detected method headings:** 2.2. Paradigms of Depth Noise Modeling (p. 2); 1) Explicit Analytical Modeling reconstructs noise via (p. 3); 2) Implicit Data-Driven Modeling leverages generative (p. 3); 2.3. Visual Foundation Models as Semantic Priors (p. 3); 3. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The architecture consists of three sequential modules. | p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (2.3. Visual Foundation Models as Semantic Priors) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | State-of-theart architectures like Metric3Dv2 (Hu et al., 2024) and MoGe (Wang et al., 2025b) employ ViT-based encoders to distill invariant geometric representations. | p. 3 (2.3. Visual Foundation Models as Semantic Priors), p. 5 (3) Sequential Optimization Objectives. Since PRISM is) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Stage I: Noise Disentanglement Learning.In addition to the pixel-wise classification, we introduce a Dice Loss to enforce shape compactness and prevent trivial ... | p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** The BND is optimized to minimize the weighted sum of these objectives over the mined sets: LBND = 4 X l=0 λl X x∈Ωl ℓ(l) ...
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** Its objective is the mask-constrained loss restricted to valid regions, shown in Eq.(7).
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** The training objective is masked to compute gradients strictly within valid sensor regions: LNRG = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t, cctl)∥2 2 ⊙(1 -ˆ M) ...
- **p. 3 / 3. Methodology - extractive PDF cue:** Our objective is to learn the conditional distributions P(M/I, Dsim) and P(R/Dsim, M) via physicsgrounded disentanglement.
- **p. 3 / 2) Implicit Data-Driven Modeling leverages generative - extractive PDF cue:** By indiscriminately conflating distinct error sources-such as specular signal loss versus transparent measurement bias-into a unified stochastic variable, they risk hallucinating geometric artifacts that contradict ...
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** To prevent the model from hallucinating artifacts in invalid regions (holes), we utilize the invalidation mask ˆ M predicted by the BND module as a ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 3 (3. Methodology), p. 3 (2) Implicit Data-Driven Modeling leverages generative), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 5 (3) Sequential Optimization Objectives. Since PRISM is).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Simulation, Task, Language, Optional, Enhanced, Triplet, Depth, Simulated, RGB, State, Large-scale, Dataset, Joint, Gripper | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Simulation, Task, Language, Optional, Enhanced, Triplet, Depth, Simulated, RGB, State | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | operationalize, insight, PRISM, PhysicsReasoned, Implicit, Sensor, Modeling, semantic-geometric, collaborative, framework | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | BND, optimized, minimize, weighted, objectives, over, mined, sets, LBND, diceLdice | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** Simulation) Task Language (Optional) <Enhanced Triplet> Enhanced Depth Simulated RGB Simulated State Large-scale Dataset from Simulation Simulated State Simulated RGB Simulated Depth Joint Gripper + ...
- **p. 4 / 3.2. Bimodal Noise Disentangler - extractive PDF cue:** The BND maps the concatenated RGB-Depth input X = [I; Dsim] ∈R4×H×W to a pixel-wise sensing invalidation probability map ˆ M ∈[0, 1]H×W .
- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive PDF cue:** Formally, given an input RGB image I ∈R3×H×W , SPR maps its semantics to a set of multi-scale channel attention vectors S = {Sl}L l=1, ...
- **p. 5 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** (c) Depth-Aware Policy Learning: A modified robotic policy, equipped with a dedicated depth encoder, is trained on the enhanced dataset to learn robustness against sensor ...
- **p. 2 / 1. Introduction - extractive PDF cue:** 4) SOTA Fidelity and Sim2Real Transfer: Extensive benchmarks demonstrate that PRISM achieves state-of-theart fidelity in noisy depth synthesis.
- **p. 2 / 1. Introduction - extractive PDF cue:** Real-world depth corruption follows structured physical regularities: specular surfaces (e.g., metal, mirror) cause regular reflection resulting in Sensing Invalidation, whereas transparent or translucent materials (e.g., ...
- **p. 3 / 3. Methodology - extractive PDF cue:** The goal of sensor simulation is to learn a mapping M : Dsim →Dreal such that policies trained on M(Dsim) generalize to Dr.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We present PRISM, a tripartite framework that synthesizes realistic depth by disentangling sensor noise into physically grounded modalities. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Inference utilizes DDIM sampling (50 steps, 9.0 scale). | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Inference utilizes DDIM sampling (50 steps, 9.0 scale). | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim to ...
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive PDF cue:** Its objective is the mask-constrained loss restricted to valid regions, shown in Eq.(7).
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Training proceeds in two phases totaling 100 epochs: first freezing the VAE and U-Net to optimize only the ControlNet, followed by joint fine-tuning where the ...
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Implemented in PyTorch on 8 NVIDIA H200 GPUs, PRISM trains on 5122 images with a batch size of 32.
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim to ...
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive PDF cue:** The training objective is masked to compute gradients strictly within valid sensor regions: LNRG = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t, cctl)∥2 2 ⊙(1 -ˆ M) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** architecture, consists, three, sequential, modules, State-of-theart, architectures, like, Metric3Dv2, MoGe, Wang, employ, ViT-based, encoders, distill, invariant, geometric, representations, Stage, Noise.
- **Relevant PDF headings:** 2.2. Paradigms of Depth Noise Modeling (p. 2); 1) Explicit Analytical Modeling reconstructs noise via (p. 3); 2) Implicit Data-Driven Modeling leverages generative (p. 3); 2.3. Visual Foundation Models as Semantic Priors (p. 3); 3. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We establish a benchmark of 6 diverse manipulation tasks (Tab.3) across two robotic platforms to evaluate challenging physical properties. | p. 8 (5.3. Downstream Application Evaluation), p. 6 (5.1. Experimental Settings) |
| Semantic / temporal fusion | Zero-shot evaluation on the NYU-Depth-v2 dataset (Tab.2) demonstrates PRISM's superior robustness under noisy domain shifts when compared to overfitting-prone baselines. | p. 7 (5.2. Depth Fidelity Evaluation), p. 8 (5.2. Depth Fidelity Evaluation) |
| Robot query / planning handoff | By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), ... | p. 8 (5.3. Downstream Application Evaluation), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7. Semantics Efficacy. Comparing generic vs. geometric priors. 3D VFMs show superior material awareness. Impact of Causal Architecture. We treat the diffusion-based NRG as ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 17. Progressive Ablation of H-PPS. We add components sequentially to the standard BCE baseline. Boundary-IoU evaluates the precision of artifact edges (within 5px). Config ...
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 15. Component Ablation Study. We evaluate the contribution of Semantic-Physics Reasoner (SPR) and Bimodal Noise Disentangler (BND) against the pure Noise Residual Generator (NRG) ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Overview of the PRISM-enabled Sim-to-Real Pipeline. (a) Simulation Data Collection: Large-scale expert demonstrations are collected in a simulator. (b) Offline Depth Enhancement: PRISM ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) to ...
- **p. 25 / Figure/Table caption - extractive PDF cue:** Table 18. Sensitivity Analysis. We analyze the trade-offs for Positive Weight wpos (Left) and Initial Mining Ratio γstart (Right). The optimal configurations (wpos = 3.0 ...
- **p. 6 / 5.1. Experimental Settings - extractive PDF cue:** Training proceeds in two phases totaling 100 epochs: first freezing the VAE and U-Net to optimize only the ControlNet, followed by joint fine-tuning where the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (2.3. Visual Foundation Models as Semantic Priors), p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 4 (3.2. Bimodal Noise Disentangler), p. 5 (3) Sequential Optimization Objectives. Since PRISM is), objective p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 5 (3) Sequential Optimization Objectives. Since PRISM is), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), p. 3 (3. Methodology), p. 3 (2) Implicit Data-Driven Modeling leverages generative), p. 4 (2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ), temporal p. 3 (3. Methodology), p. 6 (5.1. Experimental Settings), p. 8 (5.2. Depth Fidelity Evaluation), p. 8 (5.3. Downstream Application Evaluation), p. 9 (7. Limitations), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
