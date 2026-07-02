# Evaluation

- Year/Venue: 2025 / ICML Oral
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICML/2025_ICML_ReferSplat-Referring-Segmentation-in-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanRefer
- LERF

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- When integrating all components (index 3), referred to as ReferSplat, we achieve a substantial performance gain, reaching a new state-of-the-art.
- 2 show that our method significantly outperforms all baselines, demonstrating that the proposed 3D Referring Feature Fields effectively models the relationship between 3D Gaussians and text.
- 3, our method achieves about 50% mIoU against ground truth, validating the effectiveness of our pseudo mask generation.
- We conduct ablation experiments to evaluate the effectiveness of different components.
- Extensive experiments demonstrate that ReferSplat achieves state-of-the-art performance on both open-vocabulary 3DGS segmentation and the newly proposed referring 3DGS segmentation tasks. ⨂ Rendered Feature Output Mask Pseudo GT ...
- When integrating all components (index 3), referred to as ReferSplat, we achieve a substantial performance gain, reaching a new state-of-the-art.

## Baselines
- 1, incorporating PCMI (index 1) improves mIoU by 5.1% and 4.3%, respectively compared to the baseline, which is our constructed Referring Feature Fields.
- We set several baselines for comparison: 1) LangSplat Adaptation: we modify LangSplat (Qin et al., 2024) from open-vocabulary segmentation to referring segmentation by replacing phrase inputs with referring ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
