# Method

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, monocular geometry
- Paper link: ./2022/CVPR/2022_CVPR_MonoScene-Monocular-3D-Semantic-Scene-Completion/paper.pdf
- Code/Project: https://github.com/cv-rits/MonoScene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Along with architectural contributions, we introduce novel global scene and local frustums losses.
- We report the performance on semantic scene completion (SSC mIoU) and scene completion (SC - IoU) for RGB-inferred baselines and our method.
- Despite the unfair setup since we use only RGB, in NYUv2 (Tab.

## 원리적 동기
- Different from the SSC literature, relying on 2.5 or 3D input, we solve the complex problem of 2D to 3D scene reconstruction while jointly inferring its semantics.
- To solve this challenging problem, we project 2D features along their line of sight, inspired by optics, bridging 2D and 3D networks while letting the 3D network self-discover ...
- Along with architectural contributions, we introduce novel global scene and local frustums losses.

## 핵심 방법론
- We report the performance on semantic scene completion (SSC mIoU) and scene completion (SC - IoU) for RGB-inferred baselines and our method.
- Despite the unfair setup since we use only RGB, in NYUv2 (Tab.
