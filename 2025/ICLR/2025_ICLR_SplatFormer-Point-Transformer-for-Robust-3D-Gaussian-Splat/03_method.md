# Method

- Year/Venue: 2025 / ICLR Spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_SplatFormer-Point-Transformer-for-Robust-3D-Gaussian-Splat/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The dataset and training approach we introduce allow SplatFormer to learn rich data-driven priors from a diverse range of 3D objects and view configurations.
- This hierarchical architecture models contextual relationships among neighboring primitives.
- This hierarchical architecture models contextual relationships among ne Standard Regularized External Prior Feed Forward MipNeRF360 (Barron et al., 2022) InstantNGP (Müller et al., 2022) 3DGS (Kerbl et al., ...

## 원리적 동기
- V-dimensional feature vectors vk ∈ RV : K {vk }K k=1 = fθ ({Gk }k=1 ), (4) which encapsulate key details of the 3D primitives.
- The feature decoder gθ then transforms this latent representation into splat attribute residuals K {∆Gk = (∆pk , ∆sk , ∆αk , ∆qk , ∆ak )}K k=1 = ...
- The dataset and training approach we introduce allow SplatFormer to learn rich data-driven priors from a diverse range of 3D objects and view configurations.

## 핵심 방법론
- The dataset and training approach we introduce allow SplatFormer to learn rich data-driven priors from a diverse range of 3D objects and view configurations.
- This hierarchical architecture models contextual relationships among neighboring primitives.
- To implement attention efficiently based on spatial proximity, we adopt PTv3’s serialization and grid pooling strategy.
- Then another 4 stages of attention blocks and upsampling grid pooling layers are used to restore the resolution.
- Each stage comprises attention blocks with layer normalization, multi-head attention, and MLPs.
