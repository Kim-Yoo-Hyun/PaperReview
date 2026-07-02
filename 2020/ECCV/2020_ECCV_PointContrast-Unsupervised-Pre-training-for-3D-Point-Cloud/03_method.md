# Method

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2020/ECCV/2020_ECCV_PointContrast-Unsupervised-Pre-training-for-3D-Point-Cloud/paper.pdf
- Code/Project: https://github.com/facebookresearch/PointContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best results in segmentation and ...
- Notably, using SR-UNet backbone architecture already boosts performance; yet, pre-training is able to provide further gains, especially when training data is scarce.
- To this end, we select a suite of diverse datasets and tasks to measure the effect of unsupervised pre-training on a large source set of 3D scenes.

## 원리적 동기
- Different from previous works, we focus on high-level scene understanding tasks.
- Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best results in segmentation and ...

## 핵심 방법론
- Notably, using SR-UNet backbone architecture already boosts performance; yet, pre-training is able to provide further gains, especially when training data is scarce.
- Replacing the backbone architecture with SR-UNet already boosts performance.
- When using 100% of the training data, pre-training provides a class-balancing effect, as it boosts performance more on underrepresented (tail) classes.
- PointContrast pre-training further adds a significant gain, and outshines where labels are most limited. from each model for classification and 2048 points for part segmentation.
- 1%-10%) of training data to fine-tune the pre-trained model.
