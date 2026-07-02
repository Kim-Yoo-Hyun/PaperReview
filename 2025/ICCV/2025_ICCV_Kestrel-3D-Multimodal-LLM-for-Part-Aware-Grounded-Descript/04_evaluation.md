# Evaluation

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Kestrel-3D-Multimodal-LLM-for-Part-Aware-Grounded-Descript/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Objaverse
- PartNet
- PartNet-Mobility
- ScanRefer

## Metrics
- BLEU
- accuracy
- mIoU
- mAP

## Evaluation Protocol and Results
- The extensive experiments demonstrate that Kestrel effectively bridges the gap between part-aware language understanding and 3D segmentation grounding, paving the way for more robust and interpretable 3D object ...
- Each part-level phrase in this generated text (e.g., “backrest” and “seat support”) is linked to a point-wise segmentation mask, challenging the model’s capability for part-aware language understanding and ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
