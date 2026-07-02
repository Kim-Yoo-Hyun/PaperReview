# Evaluation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_DreamScene360-Unconstrained-Text-to-3D-Scene-Generation-wi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP
- SSIM

## Evaluation Protocol and Results
- QAlign is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets.
- Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer .
- In our experiments, we set the input image for the LucidDreamer to be generated from Stable Diffusion v1.5 using the input text for a fair comparison.
- QAlign is the state-of-the-art method in quality assessment benchmarks, which adopts a large multi-modal model fine-tuned on available image quality assessment datasets.
- Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer .

## Baselines
- In our experiments, we set the input image for the LucidDreamer to be generated from Stable Diffusion v1.5 using the input text for a fair comparison.
- Thus, the comparisons are conducted between DreamScene360 (ours) and the state-of-the-art LucidDreamer .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
