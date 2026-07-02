# Problem

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, open-vocabulary, efficiency
- Paper link: ./2026/CVPR/2026_CVPR_LightSplat-Fast-and-Memory-Efficient-Open-Vocabulary-3D-Sc/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, existing approaches remain slow, memory-intensive, and overly complex due to iterative optimization and dense per-Gaussian feature assignments.
- Despite recent advances, existing methods still suffer from three major
- By assigning semantic indices only to salient regions and managing them with a lightweight index-feature mapping, LightSplat eliminates costly feature optimization and storage overhead.

## 해결하려는 문제
- To address this, we propose LightSplat, a fast and memory-efficient training-free framework that injects compact 2-byte semantic indices into 3D representations from multi-view images.
- We evaluate our method on LERF-OVS, ScanNet, and DL3DV-OVS across complex indoor-outdoor scenes.
- As a result, LightSplat achieves state-of-the-art performance with up to 50-400× speedup and 64× lower memory, enabling scalable language-driven 3D understanding.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
