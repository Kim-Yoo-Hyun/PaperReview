# DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_DreamScene360-Unconstrained-Text-to-3D-Scene-Generation-wi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The vast potential applications of text-to-3D to VR/MR platforms, industrial design, and gaming sectors have significantly propelled research efforts aimed at developing a reliable method for immersive scene ...
- Recent developments in the 2D domain have seen the successful generation or editing of high-quality and adaptable images/videos using large-scale pre-trained diffusion models on large-scale datasets, allowing users ...
- Moving beyond 2D, the generation of 3D content, particularly 3D scenes, is constrained by the limited availability of annotated 3D image-text data pairs.

## Core Idea
- We present a text-to-3D 360◦ scene generation pipeline that facilitates the creation of comprehensive 360◦ scenes for in-the-wild environments in a matter of minutes.
- Our approach utilizes the generative power of a 2D diffusion model and prompt self-refinement to create a high-quality and globally coherent panoramic image.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- QAlign is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets.
- Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer .
- In our experiments, we set the input image for the LucidDreamer to be generated from Stable Diffusion v1.5 using the input text for a fair comparison.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach utilizes the generative power of a 2D diffusion model and prompt self-refinement to create a high-quality and globally coherent panoramic image.
- We present a text-to-3D 360◦ scene generation pipeline that facilitates the creation of comprehensive 360◦ scenes for in-the-wild environments in a matter of minutes.

## Abstract Cue
- The increasing demand for virtual reality applications has highlighted the significance of crafting immersive 3D assets.
