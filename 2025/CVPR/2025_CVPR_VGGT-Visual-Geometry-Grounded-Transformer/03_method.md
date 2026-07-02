# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, geometry, Transformer
- Paper link: ./2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/paper.pdf
- Code/Project: https://github.com/facebookresearch/vggt
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.
- Recent contributions like DUSt3R and its evolution We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point ...
- We compare our alternating-attention architecture against two variants: one using only global self-attention and another employing cross-attention. well, excelling on challenging out-of-domain examples, such as oil paintings, non-overlapping ...

## 원리적 동기
- Introduction We consider the problem of estimating the 3D attributes of a scene, captured in a set of images, utilizing a feedforward neural network.
- Even so, visual geometry still plays a major role in 3D reconstruction, which increases complexity and computational cost.
- We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.

## 핵심 방법론
- We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.
- We compare our alternating-attention architecture against two variants: one using only global self-attention and another employing cross-attention. well, excelling on challenging out-of-domain examples, such as oil paintings, non-overlapping ...
- Note that our method directly predicts close-to-accurate point/depth maps, which can serve as a good initialization for BA.
- This eliminates the need for triangulation and iterative refinement in BA as done by , making our approach significantly faster (only around 2 seconds even with BA).
- For evaluation, we use ALIKED to detect keypoints, treating them as query points yq .
