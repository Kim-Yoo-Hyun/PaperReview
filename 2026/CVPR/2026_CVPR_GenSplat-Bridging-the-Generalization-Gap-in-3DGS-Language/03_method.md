# Method

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language, generalization
- Paper link: ./2026/CVPR/2026_CVPR_GenSplat-Bridging-the-Generalization-Gap-in-3DGS-Language/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose GenSplat, a novel approach for language comprehension in 3D Gaussian Splatting (3DGS).
- Following , we use diverse datasets for training, including ScanRefer , Nr3D , Sr3D , Multi3DRefer , ScanQA , SQA3D , Scan2Cap and Nr3DCaptioning .
- To further improve spatial alignment and computational efficiency, we introduce a Geometry-Aware Frame Selector (GAFS), which adaptively selects the most informative views based on Gaussian and textural cues.

## 원리적 동기
- Our key insight for this problem is to formulate a structured learning process to progressively align linguistic concepts with 3D Gaussians.
- However, they inherently lack cross-scene generalization (as they require per-scene optimization) and do not support comprehensive spatial reasoning beyond segmentation, e.g., for visual question answering (VQA) or captioning ...
- In this paper, we propose GenSplat, a novel approach for language comprehension in 3D Gaussian Splatting (3DGS).

## 핵심 방법론
- Following , we use diverse datasets for training, including ScanRefer , Nr3D , Sr3D , Multi3DRefer , ScanQA , SQA3D , Scan2Cap and Nr3DCaptioning .
- Note that our method does not require test-time per-scene optimization beyond 3DGS reconstruction.
- We use AdamW optimizer with a learning rate initialized as 2 × 10−4 and updated using the cosine annealing schedule.
- In the instruction-tuning stage, we use ground-truth selected views to train the MLLM.
- In both stages, we use the AdamW optimizer with a learning rate of 1 × 10−4 (weight decay of 0.01) and a batch size of 2 per GPU.
