# Method

- Year/Venue: 2019 / ICCV
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, self-supervised, geometry
- Paper link: ./2019/ICCV/2019_ICCV_Digging-Into-Self-Supervised-Monocular-Depth-Estimation/paper.pdf
- Code/Project: https://github.com/nianticlabs/monodepth2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In particular, we propose (i) a minimum reprojection loss, designed to robustly handle occlusions, (ii) a full-resolution multi-scale sampling method that reduces visual artifacts, and (iii) an auto-masking ...
- Research on self-supervised monocular training usually explores increasingly complex architectures, loss functions, and image formation models, all of which have recently helped to close the gap with fully-supervised ...
- In this paper, we propose a set of improvements, which together result in both quantitatively and qualitatively improved depth maps compared to competing self-supervised methods.

## 원리적 동기
- However, collecting large and varied training datasets with accurate ground truth depth for supervised learning is itself a formidable challenge.
- To overcome this limitation, self-supervised learning has emerged as a promising alternative for training models to perform monocular depth estimation.
- In particular, we propose (i) a minimum reprojection loss, designed to robustly handle occlusions, (ii) a full-resolution multi-scale sampling method that reduces visual artifacts, and (iii) an auto-masking ...

## 핵심 방법론
- We introduced three contributions: (i) a minimum reprojection loss, computed for each pixel, to deal Input Zhou et al.
- Comparison of our method to existing methods on KITTI 2015 using the Eigen split.
- Effect of ImageNet pretraining We follow previous work in initializing our encoders with weights pretrained on ImageNet .
- While our contributions are designed for monocular training, we still gain high accuracy in the stereo-only category.
- We train these ‘w/o pretraining’ models for 30 epochs to ensure convergence.
