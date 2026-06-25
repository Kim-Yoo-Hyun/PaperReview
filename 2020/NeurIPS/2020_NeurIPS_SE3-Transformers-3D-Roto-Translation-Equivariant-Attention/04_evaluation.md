# Evaluation

## Dataset
Replica, OXE, ShapeNet

## Benchmark
- 주요 benchmark는 task family `sequence/representation learning`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
PSNR, SSIM, LPIPS, ATE, RPE, Chamfer, F-score, pose AUC

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: We evaluate our model on a toy N-body particle simulation dataset, showcasing the robustness of the predictions under rotations of the input.
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: https://github.com/FabianFuchsML/se3-transformer-public
- PDF status: downloaded
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
