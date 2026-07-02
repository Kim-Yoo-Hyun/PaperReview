# Method

- Year/Venue: 2024 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, Vision-Language, grounding
- Paper link: ./2024/CVPR/2024_CVPR_LangSplat-3D-Language-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.
- Instead of directly learning CLIP embeddings, LangSplat first trains a scene-wise language autoencoder and then learns language features on the scene-specific latent space, bed bench room sofa lawn ...
- Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled ...

## 원리적 동기
- Unlike existing methods that ground CLIP language embeddings in a NeRF model, LangSplat advances the field by utilizing a collection of 3D Gaussians, each encoding language features distilled ...
- By employing a tile-based splatting technique for rendering language features, we circumvent the costly rendering process inherent in NeRF.
- Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recently.

## 핵심 방법론
- bed bench room sofa lawn overall further demonstrates the effectiveness of our LangSplat.
- LSeg ODISE OV-Seg 56.0 52.6 79.8 6.0 24.1 88.9 19.2 4.5 17.5 52.5 48.3 39.8 71.4 66.1 81.2 20.6 43.5 77.5 5.
- Conclusion FFD 56.6 LERF 73.5 3D-OVS 89.5 6.1 53.2 89.3 25.1 46.6 92.8 42.9 73.7 88.2 26.9 54.8 86.8 92.5 94.2 94.1 90.0 96.1 93.4 LangSplat 3.7 27
