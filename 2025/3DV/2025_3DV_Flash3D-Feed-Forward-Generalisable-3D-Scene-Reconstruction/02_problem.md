# Problem

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_Flash3D-Feed-Forward-Generalisable-3D-Scene-Reconstruction/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Introduction We consider the problem of reconstructing photorealistic 3D scenes from a single image in just one forward pass of a network.
- This problem is closely related to monocular depth estimation , which is a mature area.
- Unambiguous geometric cues, such as triangulation, are unavailable in the monocular setting, and there is no direct evidence of the occluded parts of the scene.

## 해결하려는 문제
- It achieves state-of-the-art results when trained and tested on RealEstate10k.
- We propose Flash3D, a method for scene reconstruction and novel view synthesis from a single image which is both very generalisable and efficient.
- For efficiency, we base this extension on feed-forward Gaussian Splatting.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
