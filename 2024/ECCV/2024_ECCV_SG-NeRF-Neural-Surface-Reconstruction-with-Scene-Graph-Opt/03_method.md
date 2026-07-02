# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: NeRF, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_SG-NeRF-Neural-Surface-Reconstruction-with-Scene-Graph-Opt/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.
- The byproduct of our method is the optimized camera pose Pi = (Ri , ti ) for each training image, where Ri ∈ SO(3) and ti ∈ R3 ...

## 원리적 동기
- To tackle this challenge, we present a novel approach that optimizes radiance fields with scene graphs to mitigate the influence of outlier poses.
- Experimental results on various datasets consistently demonstrate the effectiveness and superiority of our method over existing approaches, showcasing its robustness in handling outliers and producing high-quality 3D reconstructions.
- Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.

## 핵심 방법론
- Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.
- The byproduct of our method is the optimized camera pose Pi = (Ri , ti ) for each training image, where Ri ∈ SO(3) and ti ∈ R3 ...
- Given the training images, we first apply a widely used Structure-from-Motion (SfM) algorithm, i.e., COLMAP , to construct an initial scene graph of the images, where the keypoint ...
- After training, we extract the 3D scene mesh from the density of the optimized radiance field.
