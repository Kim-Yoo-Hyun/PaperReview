# Problem

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_DreamScene360-Unconstrained-Text-to-3D-Scene-Generation-wi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- The vast potential applications of text-to-3D to VR/MR platforms, industrial design, and gaming sectors have significantly propelled research efforts aimed at developing a reliable method for immersive scene ...
- Recent developments in the 2D domain have seen the successful generation or editing of high-quality and adaptable images/videos using large-scale pre-trained diffusion models on large-scale datasets, allowing users ...
- Moving beyond 2D, the generation of 3D content, particularly 3D scenes, is constrained by the limited availability of annotated 3D image-text data pairs.

## 해결하려는 문제
- Our approach utilizes the generative power of a 2D diffusion model and prompt self-refinement to create a high-quality and globally coherent panoramic image.
- We present a text-to-3D 360◦ scene generation pipeline that facilitates the creation of comprehensive 360◦ scenes for in-the-wild environments in a matter of minutes.

## 선행 연구 / 배경 단서
- Recent developments in the 2D domain have seen the successful generation or editing of high-quality and adaptable images/videos using large-scale pre-trained diffusion models on large-scale datasets, allowing users ...
- An example of this is DreamFusion , which seeks to distill the object-wise 2D priors from diffusion models into a 3D neural radiance field (NeRF) .
