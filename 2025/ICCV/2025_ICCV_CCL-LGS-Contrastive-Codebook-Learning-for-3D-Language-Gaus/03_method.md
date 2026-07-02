# Method

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICCV/2025_ICCV_CCL-LGS-Contrastive-Codebook-Learning-for-3D-Language-Gaus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues.
- We first compare our method with existing SOTA methods on LERF dataset.
- Specifically, our approach first employs a zero-shot tracker to 1.

## 원리적 동기
- To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues.
- However, methods that rely on 2D priors are prone to a critical challenge: cross-view semantic inconsistencies induced by occlusion, image blur, and view-dependent variations.
- To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues.

## 핵심 방법론
- We first compare our method with existing SOTA methods on LERF dataset.
- The second dataset, 3D-OVS , consists of long-tail objects set against diverse backgrounds.
- The training is performed over 30,000 iterations using the Adam optimizer , with a learning rate of 0.001 and beta parameters set to (0.9, 0.999). “tea in glass” ...
- For each scene, we jointly train the 3D Gaussians for both color and semantic features by setting dc = 3 and df = 8.
- For a fair comparison, we select the latest works on open-vocabulary 3D scene understanding: Feature-3DGS, LEGaussians, LangSplat, GSGrouping, GOI, and 3D VL-GS.
