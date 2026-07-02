# Method

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_DreamScene360-Unconstrained-Text-to-3D-Scene-Generation-wi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present a text-to-3D 360◦ scene generation pipeline that facilitates the creation of comprehensive 360◦ scenes for in-the-wild environments in a matter of minutes.
- Our approach utilizes the generative power of a 2D diffusion model and prompt self-refinement to create a high-quality and globally coherent panoramic image.
- This image acts as a preliminary “flat” ⋆ In this section, we detail the proposed DreamScene360 architecture (Fig.2).

## 원리적 동기
- The vast potential applications of text-to-3D to VR/MR platforms, industrial design, and gaming sectors have significantly propelled research efforts aimed at developing a reliable method for immersive scene ...
- Recent developments in the 2D domain have seen the successful generation or editing of high-quality and adaptable images/videos using large-scale pre-trained diffusion models on large-scale datasets, allowing users ...
- We present a text-to-3D 360◦ scene generation pipeline that facilitates the creation of comprehensive 360◦ scenes for in-the-wild environments in a matter of minutes.

## 핵심 방법론
- In this section, we detail the proposed DreamScene360 architecture (Fig.2).
- We utilize the diffusion process from MultiDiffuser to generate a DreamScene360 Input Text Text2Panorama “Yosemite National Park with a waterfall” Diffusion Model Self-refinement (round += 1) Draft Image ...
- 3.2), followed by employing semantic alignment and geometric correspondences as regularizations for the deformation of the 3D Gaussians (Sec.
