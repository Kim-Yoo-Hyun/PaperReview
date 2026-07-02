# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Robust-and-Efficient-3D-Gaussian-Splatting-for-Urban-Scene/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address these challenges, we propose a novel, efficient, and robust 3DGS method specifically designed for urban scene reconstruction.
- The source code is available at: https://yzslab.github.io/REUrbanGS. explicit representation introduces scalability challenges, as spatial complexity increases with scene size.

## 해결하려는 문제
- Experimental results demonstrate that our method effectively reconstructs urban-scale scenes and outperforms previous approaches in both efficiency and quality.
- Our approach begins with scene partitioning for parallel training, employing a visibility-based image selection strategy to optimize training efficiency.
- A controllable level-of-detail (LOD) strategy explicitly regulates Gaussian density under a user-defined budget, enabling efficient training and rendering while maintaining high visual fidelity.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
