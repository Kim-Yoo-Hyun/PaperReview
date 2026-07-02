# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_HAD-Hallucination-Aware-Diffusion-Priors-for-3D-Reconstruc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- For each scene, we first train a 3DGS model using 9 input training views, then generate 100 augmented novel views via diffusion priors at a resolution of 960×540.
- For 3DGS training, we set the learning rates to 8e−5 for Gaussian means, 5e−2 for opacity, 1e−3 for rotation, 5e−4 for the 0-th order spherical harmonics (SH0 ), ...

## 원리적 동기
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- This dependency severely limits performance in data-sparse scenarios, such as sparse-view settings and extreme novelview extrapolation tasks where the quality of rendered images degrades dramatically, as illustrated in ...
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...

## 핵심 방법론
- For each scene, we first train a 3DGS model using 9 input training views, then generate 100 augmented novel views via diffusion priors at a resolution of 960×540.
- For 3DGS training, we set the learning rates to 8e−5 for Gaussian means, 5e−2 for opacity, 1e−3 for rotation, 5e−4 for the 0-th order spherical harmonics (SH0 ), ...
- The poses for these augmented views are sampled from views excluded from the 3DGS training set, providing ground-truth images that enable computation of the ground-truth hallucination score map ...
- To construct the hallucination score network, we utilize the pretrained multiview encoder Quantitative results – Tab.
