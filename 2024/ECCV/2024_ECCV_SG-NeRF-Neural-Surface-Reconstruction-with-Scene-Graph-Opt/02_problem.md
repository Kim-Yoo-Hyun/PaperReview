# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: NeRF, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_SG-NeRF-Neural-Surface-Reconstruction-with-Scene-Graph-Opt/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To tackle this challenge, we present a novel approach that optimizes radiance fields with scene graphs to mitigate the influence of outlier poses.
- Experimental results on various datasets consistently demonstrate the effectiveness and superiority of our method over existing approaches, showcasing its robustness in handling outliers and producing high-quality 3D reconstructions.
- However, NeRFs require accurate camera poses as input, and existing methods struggle to handle significantly noisy pose estimates (i.e., outliers), which are commonly encountered in real-world scenarios.

## 해결하려는 문제
- Experimental results on various datasets consistently demonstrate the effectiveness and superiority of our method over existing approaches, showcasing its robustness in handling outliers and producing high-quality 3D reconstructions.
- To tackle this challenge, we present a novel approach that optimizes radiance fields with scene graphs to mitigate the influence of outlier poses.
- Furthermore, we propose a new dataset containing typical outlier poses for a detailed evaluation.

## 선행 연구 / 배경 단서
- 3D mapping and reconstruction from multi-view images is crucial for a wide range of applications, such as virtual and augmented reality.
- Given a set of unorganized images captured around an object, most pipelines proceed in two stages for obtaining the reconstruction.
