# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, depth, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fin3R-Fine-tuning-Feed-forward-3D-Reconstruction-Models-vi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing non-synthetic depth labels are noisy and predominantly biased toward indoor environments. (2) Long-sequence pointmap degradation: Inherent ambiguities in multi-view pointmap regression impede the network’s ability to capture ...
- Fine structures are frequently over-smoothed, object boundaries become blurred, and transparent or glossy surfaces are reconstructed with significant inaccuracies, yielding point clouds that lack crisp geometry.

## 해결하려는 문제
- We freeze the decoder, which handles view matching, and fine-tune only the image encoder—the component dedicated to feature extraction.
- We present Fin3R, a simple, effective, and general fine-tuning method for feedforward 3D reconstruction models.
- We validate our method on a wide range of models, including DUSt3R, MASt3R, CUT3R, and VGGT.

## 선행 연구 / 배경 단서
- Motivated by these challenges, we investigate whether extensive unlabelled single-view data can be used to fine-tune pre-trained models to improve fine geometry recovery and robustness without sacrificing multi-view ...
- Existing non-synthetic depth labels are noisy and predominantly biased toward indoor environments. (2) Long-sequence pointmap degradation: Inherent ambiguities in multi-view pointmap regression impede the network’s ability to capture ...
- Fine structures are frequently over-smoothed, object boundaries become blurred, and transparent or glossy surfaces are reconstructed with significant inaccuracies, yielding point clouds that lack crisp geometry.
