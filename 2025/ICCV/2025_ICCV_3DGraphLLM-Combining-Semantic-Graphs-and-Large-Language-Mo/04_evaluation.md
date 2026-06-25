# Evaluation

## Dataset
ScanNet, ScanRefer, Nr3D, ReferIt3D, ScanQA, OXE

## Benchmark
- 주요 benchmark는 task family `structured 3D scene graph reasoning`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
Recall@K, mean Recall@K, relationship accuracy, zero-shot relation accuracy, Acc@0.25, Acc@0.5, IoU, AP

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: Recent methods for learning scene representations have shown that adapting these representations to the 3D world can significantly improve the quality of LLM responses.
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: not identified from primary page
- PDF status: downloaded
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
