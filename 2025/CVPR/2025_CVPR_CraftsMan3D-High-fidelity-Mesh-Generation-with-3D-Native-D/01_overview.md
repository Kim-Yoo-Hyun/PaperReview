# CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_CraftsMan3D-High-fidelity-Mesh-Generation-with-3D-Native-D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite the significant advancements in 3D generation, existing methods still struggle with lengthy optimization processes, self-occlusion, irregular mesh topologies, and difficulties in accommodating user editing, consequently impeding their ...
- Specifically, we first introduce a robust data preprocessing pipeline that utilizes visibility check and winding mumber to maximize the use of existing 3D data.

## Core Idea
- We present the qualitative and quantitative evaluation of our method as described in Section 4.2 and Section 3.3, as well as comparison results against other baseline methods, showing ...
- The shape auto-encoder is based on a perceiver-based transformer architecture with 185M parameters, while the latent set diffusion model is based on a DiT, comprising 500 million parameters.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that our method achieves high efficacy in producing superior quality 3D meshes compared to existing methods.
- While these methods significantly improve generation efficiency and robustness, the resulting 3D assets tend to have artifacts and struggle to generate assets of complex geometric structures. iii) 3D ...
- However, existing methods still struggle to produce results that are ready to use.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that our method achieves high efficacy in producing superior quality 3D meshes compared to existing methods.
- While these methods significantly improve generation efficiency and robustness, the resulting 3D assets tend to have artifacts and struggle to generate assets of complex geometric structures. iii) 3D ...
- We present a novel generative 3D modeling system, coined CraftsMan3D, which can generate high-fidelity 3D geometries with highly varied shapes, detailed surfaces, and, notably, allows for refining the ...

## Abstract Cue
- ing this data, we employ a 3D-native DiT model that directly models the distribution of 3D data in latent space, generating coarse geometries in seconds.
