# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_GaussFusion-Improving-3D-Reconstruction-in-the-Wild-with-A/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Introduction We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
- Unlike prior RGB-based approaches limited to a single reconstruction pipeline, our method introduces a geometryinformed video-to-video generator that refines 3DGS renderings across both optimization-based and feed-forward methods.
- MVSplat360 is on par to our method in terms of consistency within its specialized domain, but still lacks in visual quality.

## 원리적 동기
- We plan to release our code and model. [Project Page] Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous ...
- Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames.
- Introduction We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.

## 핵심 방법론
- MVSplat360 is on par to our method in terms of consistency within its specialized domain, but still lacks in visual quality.
- We use Gemini-Flash-2.5 to generate the text description of each video.
- For DL3DV and RE10K, we randomly downsample 5% of the original video frames as training views and optimize Gaussian splats for 7K iterations following the standard Splatfacto setup.
- We randomly drop out geometry modalities and text input during training.
- Training uses the AdamW optimizer with a linear learning rate (LR) warm-up over the first 1K steps, followed by a constant LR of 1×10−5 .
