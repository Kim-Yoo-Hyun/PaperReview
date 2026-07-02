# Method

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D reconstruction, representation
- Paper link: ./2020/ECCV/2020_ECCV_NeRF-Representing-Scenes-as-Neural-Radiance-Fields-for-Vie/paper.pdf
- Code/Project: https://github.com/bmild/nerf
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of ...
- This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 to 62 images, ...
- Our realistic synthetic dataset consists of pathtraced renderings of 8 geometrically complex objects with complex non-Lambertian materials.

## 원리적 동기
- In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation to minimize the ...
- We describe how to effectively optimize neural radiance fields to render photorealistic novel views of scenes with complicated geometry and appearance, and demonstrate results that outperform prior work ...
- We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of ...

## 핵심 방법론
- This dataset consists of 8 scenes captured with a handheld cellphone (5 taken from the LLFF paper and 3 that we capture), captured with 20 to 62 images, ...
- Our realistic synthetic dataset consists of pathtraced renderings of 8 geometrically complex objects with complex non-Lambertian materials.
- The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this data because it only reconstructs objects inside a bounded volume).
- The DeepVoxels dataset consists of 4 diffuse objects with simple geometry.
