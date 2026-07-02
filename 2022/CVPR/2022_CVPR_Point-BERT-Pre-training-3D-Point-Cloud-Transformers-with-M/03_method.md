# Method

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2022/CVPR/2022_CVPR_Point-BERT-Pre-training-3D-Point-Cloud-Transformers-with-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Equipped with our pretraining strategy, we show that a pure Transformer architecture attains 93.8% accuracy on ModelNet40 and 83.1% accuracy on the hardest setting of ScanObjectNN, surpassing carefully ...
- Tokenizer We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT to 3D point cloud.
- The pre-training objective is to recover the original point tokens at the masked locations under the supervision of point tokens obtained by the Tokenizer.

## 원리적 동기
- Tokenizer We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT to 3D point cloud.
- Inspired by BERT, we devise a Masked Point Modeling (MPM) task to pre-train point cloud Transformers.
- Equipped with our pretraining strategy, we show that a pure Transformer architecture attains 93.8% accuracy on ModelNet40 and 83.1% accuracy on the hardest setting of ScanObjectNN, surpassing carefully ...

## 핵심 방법론
- During MPM pre-training, we fix the weights of Tokenizer learned by dVAE.
- The stochastic depth with a 0.1 rate is applied in our transformer encoder.
- PointNet PointNet++ SO-Net PointCNN DGCNN DensePoint RSCNN KPConv 1k 1k 1k 1k 1k 1k 1k ∼6.8k 89.2 90.5 92.5 92.2 92.9 92.8 92.9 92.9 [T] PCT [T] PointTransformer ...
