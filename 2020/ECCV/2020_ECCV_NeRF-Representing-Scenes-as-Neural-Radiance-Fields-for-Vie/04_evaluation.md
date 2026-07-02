# Evaluation

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D reconstruction, representation
- Paper link: ./2020/ECCV/2020_ECCV_NeRF-Representing-Scenes-as-Neural-Radiance-Fields-for-Vie/paper.pdf
- Code/Project: https://github.com/bmild/nerf
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ShapeNet

## Metrics
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- 8 and 6) show that our method outperforms prior work, and provide extensive ablation studies to validate our design choices (Table 2).
- 6.1 Datasets Synthetic renderings of objects We first show experimental results on two datasets of synthetic renderings of objects (Table 1, “Diffuse Synthetic 360◦ ” and “Realistic Synthetic ...
- We urge the reader to view our supplementary video to better appreciate our method’s significant improvement over baseline methods when rendering smooth paths of novel views.
- We present a method that achieves state-of-the-art results for synthesizing novel views of complex scenes by optimizing an underlying continuous volumetric scene function using a sparse set of ...
- We describe how to effectively optimize neural radiance fields to render photorealistic novel views of scenes with complicated geometry and appearance, and demonstrate results that outperform prior work ...

## Baselines
- We urge the reader to view our supplementary video to better appreciate our method’s significant improvement over baseline methods when rendering smooth paths of novel views.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
