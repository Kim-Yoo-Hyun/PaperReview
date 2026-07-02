# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: geometry, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Multimodal-LiDAR-Camera-Novel-View-Synthesis-with-Unified/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- nuScenes

## Metrics
- accuracy
- mAP
- Chamfer
- F-score
- PSNR
- SSIM
- LPIPS
- ATE
- RPE

## Evaluation Protocol and Results
- Thus, compared to single-modality methods and i-NGP that with and without point clouds for depth supervision, we achieve highquality NVS and the best results across both modalities.
- The results indicate that relying solely on NeRF’s implicit pose optimization fails to achieve accurate pose estimates and leads to convergence at local optima.
- Therefore, we exclude the MMG and conduct ablation experiments with GT pose to further demonstrate the advantages of our Uniﬁed NeRF with the multimodal-speciﬁc coarseto-ﬁne training strategy (MSC2F) ...
- We conducted experiments unsetting(bottom).P2IR: Point2Image Regular- der GT-poses to demonstrate the effectiveness of our method in modal fusion. ization.
- Thus, compared to single-modality methods and i-NGP that with and without point clouds for depth supervision, we achieve highquality NVS and the best results across both modalities.
- The results indicate that relying solely on NeRF’s implicit pose optimization fails to achieve accurate pose estimates and leads to convergence at local optima.

## Baselines
- Comparison and Ablation in Pose-free Setting Baselines.
- Thus, compared to single-modality methods and i-NGP that with and without point clouds for depth supervision, we achieve highquality NVS and the best results across both modalities.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
