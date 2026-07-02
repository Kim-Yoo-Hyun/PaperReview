# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_LangScene-X-Reconstruct-Generalizable-3D-Language-Embedded/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To reduce the memory cost and enhance scalability for large-scale data, we propose a generalizable Language Quantized Compressor (LQC) trained on largescale datasets, which encodes high-dimensional language features ...
- Powered by the generative capability of creating more consistent novel observations, we can build generalizable 3D languageembedded scenes from only sparse views.
- Specifically, we first train a TriMap video diffusion model that can generate appearance (RGBs), geometry (normals), and semantics (segmentation maps) from sparse inputs through progressive knowledge integration.

## 해결하려는 문제
- Furthermore, we propose a Language Quantized Compressor (LQC), trained on largescale image datasets, to efficiently encode language embeddings, enabling cross-scene generalization without perscene retraining.
- Extensive experiments on real-world data demonstrate the superiority of our LangScene-X over state-of-the-art methods in terms of quality and generalizability.
- This approach eliminates the need for per-scene retraining, reduces memory overhead, and enables rapid rendering of language-embedded Gaussians.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
