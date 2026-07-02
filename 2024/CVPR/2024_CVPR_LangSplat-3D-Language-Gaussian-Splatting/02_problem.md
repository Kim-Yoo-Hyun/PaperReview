# Problem

- Year/Venue: 2024 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, Vision-Language, grounding
- Paper link: ./2024/CVPR/2024_CVPR_LangSplat-3D-Language-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled ...
- By employing a tile-based splatting technique for rendering language features, we circumvent the costly rendering process inherent in NeRF.

## 해결하려는 문제
- Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled ...
- Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.
- Instead of directly learning CLIP embeddings, LangSplat first trains a scene-wise language autoencoder and then learns language features on the scene-specific latent space,

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
