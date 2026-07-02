# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, calibration, geometry
- Paper link: ./2024/CVPR/2024_CVPR_DUSt3R-Geometric-3D-Vision-Made-Easy/paper.pdf
- Code/Project: https://github.com/naver/dust3r
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We base our network architecture on standard Transformer encoders and decoders, allowing us to leverage powerful pretrained models.
- Conclusion We presented a novel paradigm to solve not only 3D reconstruction in-the-wild without prior information about scene nor cameras, but a whole variety of 3D vision tasks ...
- We again emphasize that our method is the first one to enable global unconstrained MVS, in the sense that we have no prior knowledge regarding the camera intrinsic ...

## 원리적 동기
- We cast the pairwise reconstruction problem as a regression of pointmaps, relaxing the hard constraints of usual projective camera models.
- This is possible because our network jointly processes the input images and the resulting 3D pointmaps, thus learning to associate 2D structures with 3D shapes, and having the ...
- We base our network architecture on standard Transformer encoders and decoders, allowing us to leverage powerful pretrained models.

## 핵심 방법론
- Conclusion We presented a novel paradigm to solve not only 3D reconstruction in-the-wild without prior information about scene nor cameras, but a whole variety of 3D vision tasks ...
- We again emphasize that our method is the first one to enable global unconstrained MVS, in the sense that we have no prior knowledge regarding the camera intrinsic ...
- Our method does not reach the accuracy levels of the best methods.
- We believe this level of accuracy to be of great use in practice, considering the plug-and-play nature of our approach.
- Timewise, our approach is also much faster than the traditional COLMAP pipeline .
