# Evaluation

## Dataset
ScanNet, OXE

## Benchmark
- 주요 benchmark는 task family `diffusion-based generation or policy learning`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
PSNR, SSIM, LPIPS, ATE, RPE, Chamfer, F-score, pose AUC

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: To achieve this, we introduce Match-ControlNet, a matching-specific, controllable 2D generative model.
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: not identified
- PDF status: downloaded
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
