# Problem

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2021/ICCV/2021_ICCV_Self-Supervised-Pretraining-of-3D-Features-on-any-Point-Cl/paper.pdf
- Code/Project: https://github.com/facebookresearch/DepthContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- A primary reason is the lack of large annotated datasets because 3D data is both difficult to acquire and time consuming to label.
- Pretraining on depth maps faces several challenges: first, the absence of any supervision at scale requires
- Thus, 3D data acquisition and annotation both require significantly more effort than images or videos, and there is no existing weak supervision, like image tags, to shortcut the ...

## 해결하려는 문제
- We evaluate our models on 9 benchmarks for object detection, semantic segmentation, and object classification, where they achieve stateof-the-art results and can outperform supervised pretraining.
- We pretrain standard point cloud and voxel based model architectures, and show that joint pretraining further improves performance.
- Our pretraining which uses unlabeled single-view 3D data, outperforms training from scratch, and achieves the same detection performance with about half the detection labels. points that need to ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
