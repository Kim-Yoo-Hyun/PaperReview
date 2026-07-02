# LangScene-X: Reconstruct Generalizable 3D Language-Embedded Scenes with TriMap Video Diffusion

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_LangScene-X-Reconstruct-Generalizable-3D-Language-Embedded/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To reduce the memory cost and enhance scalability for large-scale data, we propose a generalizable Language Quantized Compressor (LQC) trained on largescale datasets, which encodes high-dimensional language features ...
- Powered by the generative capability of creating more consistent novel observations, we can build generalizable 3D languageembedded scenes from only sparse views.
- Specifically, we first train a TriMap video diffusion model that can generate appearance (RGBs), geometry (normals), and semantics (segmentation maps) from sparse inputs through progressive knowledge integration.

## Core Idea
- Furthermore, we propose a Language Quantized Compressor (LQC), trained on largescale image datasets, to efficiently encode language embeddings, enabling cross-scene generalization without perscene retraining.
- We visualize the training curve of our method and traditional autoencoder.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on real-world data demonstrate the superiority of our LangScene-X over state-of-the-art methods in terms of quality and generalizability.
- Recent developments have achieved this by performing per-scene optimization with embedded language information.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Furthermore, we propose a Language Quantized Compressor (LQC), trained on largescale image datasets, to efficiently encode language embeddings, enabling cross-scene generalization without perscene retraining.
- Extensive experiments on real-world data demonstrate the superiority of our LangScene-X over state-of-the-art methods in terms of quality and generalizability.
- This approach eliminates the need for per-scene retraining, reduces memory overhead, and enables rapid rendering of language-embedded Gaussians.

## Abstract Cue
- Recovering 3D structures with open-vocabulary scene understanding from 2D images is a fundamental but daunting task.
