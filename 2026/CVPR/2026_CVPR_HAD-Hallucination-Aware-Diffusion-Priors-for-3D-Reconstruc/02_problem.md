# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_HAD-Hallucination-Aware-Diffusion-Priors-for-3D-Reconstruc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- This dependency severely limits performance in data-sparse scenarios, such as sparse-view settings and extreme novelview extrapolation tasks where the quality of rendered images degrades dramatically, as illustrated in ...
- These hallucination scores enable selective masking of unreliable pixels during the progressive 3D reconstruction procedure, preventing the introduction of nonexistent artifacts into the 3D model.

## 해결하려는 문제
- We show that our method substantially reduces hallucination artifacts in diffusion-assisted 3D reconstruction, thereby achieving state-of-the-art performance across mul- 1.
- To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel ...
- Diffusion priors have recently demonstrated strong capability in enhancing the quality of sparse-view 3D reconstruction by augmenting training views at novel viewpoints, but they inevitably introduce hallucinated content ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
