# Method

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_SGS-SLAM-Semantic-Gaussian-Splatting-For-Neural-Dense-SLAM/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting.
- We introduce a unique semantic feature loss that effectively compensates for the shortcomings of traditional depth and color losses in object optimization.
- Like previous SLAM techniques, our method can be split into two processes: tracking and mapping.

## 원리적 동기
- Dense Visual Simultaneous Localization and Mapping (SLAM) is a crucial problem in the field of computer vision.
- However, NeRF-based SLAM methods employ multi-layer perceptrons (MLPs) as the implicit neural representation of scenes, which introduces several challenging limitations.
- We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting.

## 핵심 방법론
- Like previous SLAM techniques, our method can be split into two processes: tracking and mapping.
- SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM 3.1
- SGS-SLAM is a Gaussian-based semantic visual SLAM system.
- 3.1 introduces its multi-channel Gaussian representation for joint parameter optimization.
