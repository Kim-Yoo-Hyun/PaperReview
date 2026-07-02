# Method

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, Vision-Language, semantic
- Paper link: ./2025/ICCV/2025_ICCV_SceneSplat-Gaussian-Splatting-based-Scene-Understanding-wi/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Furthermore, we propose a self-supervised 1.
- To address these limitations, we introduce SceneSplat in Fig.
- We adopt the pretraining on the SceneSplat-7K dataset and report fine-tuning mIoU and mAcc on indoor semantic segmentation tasks.

## 원리적 동기
- To address these limitations, we introduce SceneSplat in Fig.
- However, effectively integrating semantic reasoning into 3DGS in a generalizable manner remains an open challenge.
- Furthermore, we propose a self-supervised 1.

## 핵심 방법론
- We adopt the pretraining on the SceneSplat-7K dataset and report fine-tuning mIoU and mAcc on indoor semantic segmentation tasks.
- Training Source OpenScene† PLA RegionPLC OV3D Mosaic3D SceneSplat (Ours) SN SN SN SN SN SN Mosaic3D SceneSplat (Ours) SceneSplat (Ours) SN, SN++, ARKitS, MP3D, S3D SN++ SN, SN++, ...
- One may assume that the collected language labels cap the upper bound zero-shot performance since they provide the supervision signal during vision-language pretraining.
- Method ScanNet20 (20) mIoU mAcc ScanNet200 (200) mIoU mAcc ScanNet++ (100) mIoU mAcc No-Pre MGM +DINO +iBOT +LA 77.1 76.7 77.0 77.2 77.2 35.4 35.5 35.9 35.2 34.7 ...
- Although the collected labels are not perfect, large-scale pretraining can filter noise and learn meaningful patterns.
