# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Distilling-Unsigned-Distance-Function-for-Surface-Reconstr/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We compare our method against both SDF-based and UDFbased surface reconstruction approaches across all scenes.
- This mismatch produces noisy or biased gradients and leads to unstable training, over-smoothing, and the loss of fine surface details.
- First, there is no ground-truth surface for supervision; training must rely primarily on multi-view photometric consistency, which is indirect and sensitive to occlusion, view-dependence, and illumination changes.

## 원리적 동기
- To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting ...
- Existing methods for UDF learning generally fall into two families: NeRF-based frameworks and 3D Gaussian Splatting (3DGS) based methods .
- We compare our method against both SDF-based and UDFbased surface reconstruction approaches across all scenes.

## 핵심 방법론
- We compare our method against both SDF-based and UDFbased surface reconstruction approaches across all scenes.
- Visual comparison with 2DGS , GaussianUDF , NeuralUDF , VRPrior and ours on the DF3D dataset.
- UDF-based baselines include NeuralUDF , 2SUDF , VRPrior , and GaussianUDF , which are specifically designed for open and incomplete surfaces.
- 30 92 117 133 164 204 300 320 448 522 591 598 Mean Time NeuS 2DGS GOF 3.18 4.82 4.78 4.99 3.73 5.71 5.89 2.21 5.89 3.60 2.44 ...
