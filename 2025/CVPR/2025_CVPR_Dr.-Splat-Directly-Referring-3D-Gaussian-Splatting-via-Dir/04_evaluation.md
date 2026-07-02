# Evaluation

- Year/Venue: 2025 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, language embedding, grounding
- Paper link: ./2025/CVPR/2025_CVPR_Dr.-Splat-Directly-Referring-3D-Gaussian-Splatting-via-Dir/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- LERF

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- Experiments demonstrate that our approach significantly outperforms existing approaches in 3D perception benchmarks, such as openvocabulary 3D semantic segmentation, 3D object localization, and 3D object selection tasks.
- For video results, please visit : https://drsplat.github.io/ 3D search scheme (ours) Chair Render 2D images ‘Direct’ 3D Search Search all images: B×H×W → Slow #Gaussians → Fast W ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
