# Method

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2021/ICCV/2021_ICCV_Point-Transformer/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- We use the sampled point sets produced by Qi et al. for a fair comparison with prior work.
- For evaluation metrics, we use the mean accuracy within each category (mAcc) and the overall accuracy (OA) over all classes.

## 원리적 동기
- part segmentation tic ion an ntat semgme se arXiv:2012.09164v2 [cs.CV] 26 Sep 2021 Hengshuang Zhao1,2 Li Jiang3 Jiaya Jia3 Philip Torr1 Vladlen Koltun4 University of Oxford 2 The ...
- The Point Transformer can serve as the backbone for various 3D point cloud understanding tasks such as object classification, object part segmentation, and semantic scene segmentation. analysis .
- It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.

## 핵심 방법론
- It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing.
- We use the sampled point sets produced by Qi et al. for a fair comparison with prior work.
- For evaluation metrics, we use the mean accuracy within each category (mAcc) and the overall accuracy (OA) over all classes.
- They are split into 9,843 models for training and 2,468 for testing.
- To probe the representation learned by the Point Transformer, we conduct shape retrieval by retrieving nearest neighbors in the space of the output features produced by the Point ...
