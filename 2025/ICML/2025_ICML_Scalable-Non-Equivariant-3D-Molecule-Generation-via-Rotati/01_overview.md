# Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/ding25a.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/165283. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Yuhui Ding, Thomas Hofmann
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, Diffusion, Generation, equivariant, 3D Vision
- Official paper: https://proceedings.mlr.press/v267/ding25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/ding25a/ding25a.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf)

## Why This Paper Is Here

RADM은 분자마다 회전 좌표계를 추정해 정렬된 잠재 공간에서 3차원 분자 구조를 생성한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf#page=1) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Equivariant diffusion models have achieved impressive performance in 3D molecule generation.
- **p. 1 / Abstract - extractive body cue:** These models incorporate Euclidean symmetries of 3D molecules by utilizing an SE(3)-equivariant denoising network.
- **p. 1 / Abstract - extractive body cue:** However, specialized equivariant architectures limit the scalability and efficiency of diffusion models.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose an approach that relaxes such equivariance constraints.
- **p. 1 / Abstract - extractive body cue:** Specifically, our approach learns a sample-dependent SO(3) transformation for each molecule to construct an aligned latent space.
- **p. 1 / 1. Introduction - extractive body cue:** Compared with their non-equivariant counterparts, they have more complex parametrization and lack standardized implementations.
- **p. 1 / 1. Introduction - extractive body cue:** Different from data with grid-like structures (e.g., images and text sequences), 3D molecules pose unique challenges to generative modeling due to the Euclidean symmetry group ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To address this challenge, we propose to construct aligned representations in an unsupervised manner with an autoencoder.
- **p. 2 / 1. Introduction - extractive body cue:** Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment Driven by the interest in further investigating the capacity of non-equivariant diffusion models and motivated by the ...
- **p. 4 / 3. Method - extractive body cue:** In Section 3.1, we introduce how we learn alignment with an autoencoder.
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** To overcome this, we propose to learn rotations in an unsupervised manner through an autoencoder.
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** In (18) we parameterize the joint distribution of zx, zh as an isotropic Gaussian with a fixed variance σ2, which allows qθ,η(zx, zh/x, h) to ...
- **p. 4 / 3.1. Aligned Latent Space - extractive body cue:** Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ...
- **p. 3 / 2.2. Diffusion Models - extractive body cue:** We use the same noise prediction parametrization in our model, and xϕ(zt, t) in (8) is further rewritten as: xϕ(zt, t) = zt αt -σt ...
- **p. 5 / 3.1. Aligned Latent Space - extractive body cue:** Regarding the specific architectural choices for Eη and Dψ, we use the same encoder architecture as GeoLDM (Xu et al., 2023) for the purpose of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | One EGNN layer that takes xl, hl as inputs and outputs xl+1, hl+1 is defined as: mij = ϕe(hl i, hl j, d2 ij, aij), hl+1 i = ϕh(hl i, X j̸=i ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (2.3. Equivariance), p. 4 (3.1. Aligned Latent Space) |
| State/latent | One, EGNN, layer, takes, inputs, outputs, defined, eijmij, atomic, coordinates, atom, features | geometry, map, object/relationship state | p. 3 (2.3. Equivariance), p. 4 (3.1. Aligned Latent Space), p. 2 (2.2. Diffusion Models) |
| Output/action | Inputs: atomic coordinates x, atom features h Learnable parameters: rotation network Rθ, encoder Eη, decoder Dψ while not converged do Rθ ←Rθ(x, h) µx, µh ←Eη(Rθx, h) Subtract center of gravity from ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. Aligned Latent Space), p. 2 (2.2. Diffusion Models), p. 3 (2.2. Diffusion Models) |
| Objective/outcome | The above rotation representation is good for gradient-based optimization in the sense that SVD+(M) is smooth where det(M)̸ = 0 (Levinson et al., 2020). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.1. Aligned Latent Space), p. 4 (3.1. Aligned Latent Space), p. 5 (3.2. Non-Equivariant Latent Diffusion Model) |

## Main Claims and Actual Contribution

- 분자별 회전 변환으로 정렬한 뒤 회전 등변성이 내장되지 않은 확산 네트워크에서도 좌표 분포를 학습할 수 있게 한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf#page=5)
- QM9과 GEOM-Drugs에서 분자 생성 품질과 계산 비용을 측정해 등변 확산 모델과 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/ding25a/ding25a.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (4.1. Experimental Setup) |
| Embodiment/environment | Datasets We first evaluate our approach using the QM9 dataset (Ramakrishnan et al., 2014) which is a standard molecule generation benchmark widely used by related works. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Dataset/benchmark | We use the same hidden dimension and number of layers for the autoencoder as GeoLDM, and the number of layers of the rotation network is 2 on both datasets. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.3. GEOM-Drugs) |
| Metric | We report the average performance and standard deviation across three runs, each sampling 10000 molecules. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setup), p. 5 (4. Experiments), p. 6 (4.1. Experimental Setup) |
| Baseline/ablation | As we can see from the table, diffusion models perform much better than ENF and G-SchNet, and equivariant baselines significantly outperform non-equivariant baselines. | fair input/data/compute/action matching | p. 6 (4.1. Experimental Setup), p. 7 (4.4. Ablation Study), p. 5 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Experimental Setup - extractive body cue:** As for the diffusion model, we use the same noise schedule and number of time steps as EDM/GeoLDM.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** To implement DiT as the noise prediction network, we follow the official code base6 and make necessary modifications as explained in Section 3.2.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Specifically, we use a basic non-equivariant GNN (17) as the noise prediction network and train the diffusion model based on the same trained autoencoder as ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** The nonequivariant baselines GraphLDM and GraphLDM-aug used the same GNN architecture as the noise prediction network, but were trained in a latent space without learned ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (2.3. Equivariance), p. 4 (3.1. Aligned Latent Space)이다.
