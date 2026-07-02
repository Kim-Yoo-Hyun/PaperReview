# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BeliefMapNav-3D-Voxel-Based-Belief-Map-for-Zero-Shot-Objec/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Habitat
- HM3D

## Metrics
- accuracy
- mAP
- SPL
- SR
- success rate

## Evaluation Protocol and Results
- We conduct experiments on its validation set, consisting of 11 environments, 21 object categories, and 2,195 object-goal navigation episodes.
- 4.1 Benchmarks and Implementation details Dataset: We evaluate our method on three standard benchmarks: HM3D , MP3D and HSSD .
- Ablation studies assess each component’s contribution.
- Experiments on HM3D and HSSD benchmarks show that BeliefMapNav achieves state-of-the-art (SOTA) Success Rate (SR) and Success weighted by Path Length (SPL), with a notable 9.7 SPL improvement ...
- We conduct experiments on its validation set, consisting of 11 environments, 21 object categories, and 2,195 object-goal navigation episodes.

## Baselines
- In this section, we outline datasets and key implementation details, then compare BeliefMapNav’s performance against SOTA baselines on HM3D , MP3D , and HSSD .
- Baseline summaries and HM3D failure analyses appear in Appendix A.6 and A.7, respectively.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
