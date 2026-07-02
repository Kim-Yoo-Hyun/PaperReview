# Evaluation

- Year/Venue: 2023 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: NeRF, Vision-Language, grounding
- Paper link: ./2023/ICCV/2023_ICCV_LERF-Language-Embedded-Radiance-Fields/paper.pdf
- Code/Project: https://www.lerf.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- COCO
- LERF

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- queries like “Electricity”, visual properties like “Yellow”, long-tail objects such as “Waldo”, and even reading text like “Boops” on the mug.
- For each prompt, an RGB image and relevancy map are rendered focusing on the location with maximum relevancy activation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
