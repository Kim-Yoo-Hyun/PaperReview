# Problem

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, monocular geometry
- Paper link: ./2022/CVPR/2022_CVPR_MonoScene-Monocular-3D-Semantic-Scene-Completion/paper.pdf
- Code/Project: https://github.com/cv-rits/MonoScene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Different from the SSC literature, relying on 2.5 or 3D input, we solve the complex problem of 2D to 3D scene reconstruction while jointly inferring its semantics.
- To solve this challenging problem, we project 2D features along their line of sight, inspired by optics, bridging 2D and 3D networks while letting the 3D network self-discover ...
- Introduction Estimating 3D from an image is a problem that goes back to the roots of computer vision .

## 해결하려는 문제
- Experiments show we outperform the literature on all metrics and datasets while hallucinating plausible scenery even beyond the camera field of view.
- Along with architectural contributions, we introduce novel global scene and local frustums losses.
- 1, where it outperformed all comparable baselines and even some 3D input baselines.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
