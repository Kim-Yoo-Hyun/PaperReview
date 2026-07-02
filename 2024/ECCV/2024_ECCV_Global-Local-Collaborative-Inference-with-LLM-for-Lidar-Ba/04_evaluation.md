# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: semantic
- Paper link: ./2024/ECCV/2024_ECCV_Global-Local-Collaborative-Inference-with-LLM-for-Lidar-Ba/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- IoU
- mAP

## Evaluation Protocol and Results
- 1, our proposed GLIS greatly improves the open-vocabulary detection performance on ScanNetV2.
- Our methods also significantly improve the detection precision of many classes, e.g., chair is improved by 10.79%, toilet is improved by 5.81%, and table is improved by 5.15%.
- We also report the results on top-10 classes for 20cls comparison with methods like .
- 4.1 Datasets and Metrics We conduct experiments on two datasets: ScanNetV2 and SUN RGB-D .
- Extensive experiments on ScanNetV2 and SUN RGB-D demonstrate the superiority of our methods.
- 1, our proposed GLIS greatly improves the open-vocabulary detection performance on ScanNetV2.

## Baselines
- Compared to previous 10cls 20cls sota method CoDA , mAP25 is raised from 28.76% to 30.94% and mAP25 is raised from 19.32% to 20.83%.
- For a fair comparison, we evaluate our GLIS on the top-20 object classes in ScanNetV2 and SUN RGB-D respectively, following OV-3DET .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
