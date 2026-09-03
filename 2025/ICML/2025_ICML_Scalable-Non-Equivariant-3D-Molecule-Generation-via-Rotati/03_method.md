# Method - Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=l5KpQ5MmaD; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/165283. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 5 (3.1. Aligned Latent Space), p. 5 (3.1. Aligned Latent Space), p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models)): Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ←Eη(Rθx, h) Subtract center of ...

## Method Body Digest

- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** We use the same noise prediction parametrization in our model, and xϕ(zt, t) in (8) is further rewritten as: xϕ(zt, t) = zt αt -σt ...
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** Regarding the specific architectural choices for Eη and Dψ, we use the same encoder architecture as GeoLDM (Xu et al., 2023) for the purpose of ...
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** The reconstruction loss L(θ, η, ψ) is defined as: L = -Eqθ,η(zx,zh/x,h) [log pψ(Rθx, h/zx, zh)] (20) We write down the entire training algorithm for ...
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Let Eη denote the encoder parameterized by η and Dψ denote the decoder parameterized by ψ, then the 4
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** Note that Lprior is a constant irrelevant of optimization and p(x/z0) can be parameterized by a separate Gaussian distribution to make L0 have a similar ...
- **p. 2 / 2.2. Diffusion Models - extractive body cue:** The forward process of the diffusion model starts with a generic data point x and adds increasing levels of Gaussian noise to it.
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** The above rotation representation is good for gradient-based optimization in the sense that SVD+(M) is smooth where det(M)̸ = 0 (Levinson et al., 2020).

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose to construct aligned representations in an unsupervised manner with an autoencoder.
- **p. 2 / 1. Introduction - extractive body cue:** Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment Driven by the interest in further investigating the capacity of non-equivariant diffusion models and motivated by the ...
- **p. 4 / 3. Method - extractive body cue:** In Section 3.1, we introduce how we learn alignment with an autoencoder.

## Source Evidence Cues

- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** We use the same noise prediction parametrization in our model, and xϕ(zt, t) in (8) is further rewritten as: xϕ(zt, t) = zt αt -σt ...
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** Regarding the specific architectural choices for Eη and Dψ, we use the same encoder architecture as GeoLDM (Xu et al., 2023) for the purpose of ...
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** The reconstruction loss L(θ, η, ψ) is defined as: L = -Eqθ,η(zx,zh/x,h) [log pψ(Rθx, h/zx, zh)] (20) We write down the entire training algorithm for ...
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Let Eη denote the encoder parameterized by η and Dψ denote the decoder parameterized by ψ, then the 4
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** Note that Lprior is a constant irrelevant of optimization and p(x/z0) can be parameterized by a separate Gaussian distribution to make L0 have a similar ...
- **p. 2 / 2.2. Diffusion Models - extractive body cue:** The forward process of the diffusion model starts with a generic data point x and adds increasing levels of Gaussian noise to it.
- **Detected method headings:** 2.2. Diffusion Models (p. 2); 3. Method (p. 4); 3.2. Non-Equivariant Latent Diffusion Model (p. 5); 5.1. Diffusion Models (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, ... | p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We use the same noise prediction parametrization in our model, and xϕ(zt, t) in (8) is further rewritten as: xϕ(zt, t) = ... | p. 3 (2.2. Diffusion Models), p. 5 (3.1. Aligned Latent Space) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Regarding the specific architectural choices for Eη and Dψ, we use the same encoder architecture as GeoLDM (Xu et al., 2023) for ... | p. 5 (3.1. Aligned Latent Space), p. 5 (3.1. Aligned Latent Space) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** The above rotation representation is good for gradient-based optimization in the sense that SVD+(M) is smooth where det(M)̸ = 0 (Levinson et al., 2020).
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ...
- **p. 5 / 3.2. Non-Equivariant Latent Diffusion Model - extractive body cue:** The reconstruction loss reduces to L2 loss ∥ˆx -x∥2
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** The reconstruction loss L(θ, η, ψ) is defined as: L = -Eqθ,η(zx,zh/x,h) [log pψ(Rθx, h/zx, zh)] (20) We write down the entire training algorithm for ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** Note that Lprior is a constant irrelevant of optimization and p(x/z0) can be parameterized by a separate Gaussian distribution to make L0 have a similar ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** To obtain the training objective, we follow the practice of DDPM (Ho et al., 2020) and discard the weighting in (11).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models), p. 4 (3. Method), p. 5 (3.2. Non-Equivariant Latent Diffusion Model), p. 5 (3.1. Aligned Latent Space).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | One, EGNN, layer, takes, inputs, outputs, defined, eijmij, atomic, coordinates, atom, features, Learnable, parameters | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | One, EGNN, layer, takes, inputs, outputs, defined, eijmij, atomic, coordinates | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, challenge, construct, aligned, representations, unsupervised, manner, autoencoder, Scalable, Non-Equivariant | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | above, rotation, representation, good, gradient-based, optimization, sense, SVD, smooth, where | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2.3. Equivariance - extractive body cue:** One EGNN layer that takes xl, hl as inputs and outputs xl+1, hl+1 is defined as: mij = ϕe(hl i, hl j, d2 ij, aij), ...
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ...
- **p. 2 / 2.2. Diffusion Models - extractive body cue:** Given the distributions above and using Bayes' rule, we can derive the true posterior distribution of the forward transition (4), conditioned on x: q(zs/zt, x) ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** 2 (11) where ϵϕ denotes ϵϕ(αtx + σtϵ, t), the predicted noise that is output by the denoising network ϕ.
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Furthermore, there is no restriction on the input M, making it suitable for building on top of a neural network.
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** Note that both the input to the encoder E and the target of the reconstruction are the rotated molecule (Rθx, h).
- **p. 2 / 1. Introduction - extractive body cue:** Autoencoders have been widely used to reduce input dimensions and improve efficiency for latent diffusion models (Rombach et al., 2022).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The time step t is treated as a scalar feature and is appended to the feature vector of every atom. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | As for the diffusion model, we use the same noise schedule and number of time steps as EDM/GeoLDM. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The sampling speed is measured by the average time used to generate 100 samples as one mini-batch, and we use 1000 sampling ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** The reconstruction loss L(θ, η, ψ) is defined as: L = -Eqθ,η(zx,zh/x,h) [log pψ(Rθx, h/zx, zh)] (20) We write down the entire training algorithm for ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** Note that Lprior is a constant irrelevant of optimization and p(x/z0) can be parameterized by a separate Gaussian distribution to make L0 have a similar ...
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** On QM9, we train the autoencoder for 200 epochs using a batch size of 64.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We adopt a batch size of 256 as used in the DiT paper, and train both RADMDiT-S and RADMDiT-B for around 5500 epochs.
- **p. 7 / 4.5. Efficiency Comparison - extractive body cue:** We add the number of parameters of the autoencoder but exclude its training time, since training the 7
- **p. 7 / 4.5. Efficiency Comparison - extractive body cue:** We list the parameter counts, average training time per epoch and sampling speed in Table 3.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Inputs, atomic, coordinates, atom, features, Learnable, parameters, rotation, network, encoder, decoder, while, converged, Subtract, center, gravity, Calculate, reconstruction, loss, Update.
- **Relevant PDF headings:** 2.2. Diffusion Models (p. 2); 3. Method (p. 4); 3.2. Non-Equivariant Latent Diffusion Model (p. 5); 5.1. Diffusion Models (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Datasets We first evaluate our approach using the QM9 dataset (Ramakrishnan et al., 2014) which is a standard molecule generation benchmark widely ... | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Semantic / temporal fusion | As we can see from the table, diffusion models perform much better than ENF and G-SchNet, and equivariant baselines significantly outperform non-equivariant ... | p. 6 (4.1. Experimental Setup), p. 7 (4.4. Ablation Study) |
| Robot query / planning handoff | Figure 1: Molecules generated by RADMDiT-B on QM9 (the three on the left) and GEOM-Drugs (the three on the right). non-equivariant models. ... | p. 7 (Figure/Table caption), p. 6 (4.1. Experimental Setup) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablation Study - extractive body cue:** The nonequivariant baselines GraphLDM and GraphLDM-aug used the same GNN architecture as the noise prediction network, but were trained in a latent space without learned ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** To validate the effectiveness of the alignment itself, we conduct an ablation study using the same architecture for the diffusion model.
- **p. 5 / 4. Experiments - extractive body cue:** In Section 4.4, we show the results of ablation studies.
- **p. 5 / 4. Experiments - extractive body cue:** Finally in Section 4.5, we demonstrate the efficiency and scalability of our non-equivariant model.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Among them, EDM and GeoLDM are state-of-the-art equivariant diffusion models.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Similarly, we compare with GeoLDM's non-equivariant versions GraphLDM and GraphLDM-aug.
- **p. 8 / 4.5. Efficiency Comparison - extractive body cue:** From the table we can see that in general our nonequivariant model RADM is significantly more efficient than EDM and GeoLDM.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 5 (3.1. Aligned Latent Space), p. 5 (3.1. Aligned Latent Space), p. 4 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), objective p. 4 (3.1. Aligned Latent Space), p. 4 (3.1. Aligned Latent Space), p. 5 (3.2. Non-Equivariant Latent Diffusion Model), p. 5 (3.1. Aligned Latent Space), p. 3 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models), temporal p. 5 (3.2. Non-Equivariant Latent Diffusion Model), p. 6 (4.1. Experimental Setup), p. 3 (2.3. Equivariance), p. 5 (2. If E and D were), p. 8 (4.5. Efficiency Comparison), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
