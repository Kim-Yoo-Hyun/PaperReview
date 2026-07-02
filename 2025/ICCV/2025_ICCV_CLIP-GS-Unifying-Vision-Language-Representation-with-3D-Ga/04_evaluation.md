# Evaluation

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICCV/2025_ICCV_CLIP-GS-Unifying-Vision-Language-Representation-with-3D-Ga/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ModelNet40
- ShapeNet
- Objaverse

## Metrics
- accuracy
- PSNR
- SSIM

## Evaluation Protocol and Results
- Leveraging the well-aligned multimodal representations, CLIP-GS demonstrates versatility and outperforms point cloud-based models on various 3D tasks, including multimodal retrieval, zero-shot, and few-shot classification.
- How- ever, the emphasis predominantly remains on point cloud, which, as a sparse spatial representation, offers limited 3D reconstruction capabilities compared to the emerging 3D modeling method 3D ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
