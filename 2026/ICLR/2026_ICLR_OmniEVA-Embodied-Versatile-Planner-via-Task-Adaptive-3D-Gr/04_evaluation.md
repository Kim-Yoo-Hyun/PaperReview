# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_OmniEVA-Embodied-Versatile-Planner-via-Task-Adaptive-3D-Gr/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Matterport3D
- 3RScan
- Habitat
- HM3D
- BridgeData
- Open X-Embodiment
- ScanRefer
- SQA3D
- ScanQA

## Metrics
- accuracy
- IoU
- ATE
- SPL
- SR
- success rate
- collision

## Evaluation Protocol and Results
- These two reward components reflect distinct optimization objectives: ritask emphasizes performance on offline evaluation benchmarks, while riembod targets end-to-end execution success in real-world robotic deployments.
- These two reward components reflect distinct optimization objectives: ritask emphasizes performance on offline evaluation benchmarks, while riembod targets end-to-end execution success in real-world robotic deployments.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
