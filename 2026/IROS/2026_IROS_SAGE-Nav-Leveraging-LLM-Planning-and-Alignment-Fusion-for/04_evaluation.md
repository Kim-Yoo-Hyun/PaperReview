# Evaluation

## Dataset
PDF/abstract 자동 추출에서 명확한 dataset 명칭을 찾지 못함. 본문의 experiment section 확인 필요.

## Benchmark
- 주요 benchmark는 task family `structured 3D scene graph reasoning`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
Recall@K, mean Recall@K, relationship accuracy, zero-shot relation accuracy, IoU, AP, mAP, success rate

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: Extensive evaluations in the i-THOR and RoboTHOR environments demonstrate that SAGE-Nav achieves state-of-the-art performance, delivering substantial gains in navigation efficiency and zero-shot generalization while ...
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: not identified
- PDF status: downloaded
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
