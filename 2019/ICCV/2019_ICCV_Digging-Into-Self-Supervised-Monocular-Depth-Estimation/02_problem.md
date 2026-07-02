# Problem

- Year/Venue: 2019 / ICCV
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, self-supervised, geometry
- Paper link: ./2019/ICCV/2019_ICCV_Digging-Into-Self-Supervised-Monocular-Depth-Estimation/paper.pdf
- Code/Project: https://github.com/nianticlabs/monodepth2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, collecting large and varied training datasets with accurate ground truth depth for supervised learning is itself a formidable challenge.
- To overcome this limitation, self-supervised learning has emerged as a promising alternative for training models to perform monocular depth estimation.
- Generating high quality depth-from-color is attractive because it could inexpensively complement LIDAR sensors used in self-driving cars, and enable new single-photo applications such as image-editing and AR-compositing.

## 해결하려는 문제
- We demonstrate the effectiveness of each component in isolation, and show high quality, state-of-the-art results on the KITTI benchmark.
- Research on self-supervised monocular training usually explores increasingly complex architectures, loss functions, and image formation models, all of which have recently helped to close the gap with fully-supervised ...
- In particular, we propose (i) a minimum reprojection loss, designed to robustly handle occlusions, (ii) a full-resolution multi-scale sampling method that reduces visual artifacts, and (iii) an auto-masking ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
