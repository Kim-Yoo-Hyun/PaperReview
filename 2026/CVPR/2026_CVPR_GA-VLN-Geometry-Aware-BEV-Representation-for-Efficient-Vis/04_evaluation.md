# Evaluation

## Dataset
ScanQA, Matterport3D, HM3D, Habitat, R2R, RxR, VLN-CE

## Benchmark
- 주요 benchmark는 task family `embodied navigation and spatial planning`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
SR, SPL, nDTW, goal distance, collision rate, IoU, AP, mAP

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: Together, these complementary cues--explicit depth-based projection and implicit learned priors--yield compact yet spatially expressive representations that substantially improve navigation efficiency and performance.
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: not identified from primary page
- PDF status: downloaded
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
