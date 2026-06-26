# Evaluation

## Dataset
ScanNet, LAION

## Benchmark
- 주요 benchmark는 task family `open-vocabulary 3D semantic understanding`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
mIoU, AP, mAP, open-vocabulary accuracy, long-tail performance, IoU, SR, SPL

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: We propose **Rh-3DGS**, a robust semantic 3DGS framework that uses reliability-aware distillation and manifold-consistent aggregation. **Visibility-Calibrated Distillation (VCD)** computes per-pixel reliability weights from rasterization ...
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: not identified
- PDF status: downloaded
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
