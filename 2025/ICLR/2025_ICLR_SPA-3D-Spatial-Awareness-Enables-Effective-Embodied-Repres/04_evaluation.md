# Evaluation

- Year/Venue: 2025 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_SPA-3D-Spatial-Awareness-Enables-Effective-Embodied-Repres/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- ScanNet
- S3DIS
- RLBench
- LIBERO

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- The results on each benchmark are shown in Tab.
- While no method ranks first across all individual benchmarks, consistent with the findings by Majumdar et al. (2023), SPA achieves the best or second-best mean success rate in ...
- Moreover, despite being based on MAE, previous SOTA embodied representations like MVP and VC-1 do not consistently outperform the original ImageNet version.
- For detailed results on each task and each random seed, please refer to Appendix D.
- The results on each benchmark are shown in Tab.
- While no method ranks first across all individual benchmarks, consistent with the findings by Majumdar et al. (2023), SPA achieves the best or second-best mean success rate in ...

## Baselines
- VC-1 AD (2) MW (5) DMC (5) TF (2) RLBench Group 1 (35) Group 2 (36) Meta-World (48) Object (10) Spatial (10) LIBERO Goal (10) 10 (10) 90 ...
- Furthermore, InternViT-6B, despite having significantly more model parameters, does not demonstrate superiority and even performs worse on some benchmarks compared to InternViT-300M.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
