# Evaluation

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, 3D geometry, Transformer
- Paper link: ./2020/NeurIPS/2020_NeurIPS_SE3-Transformers-3D-Roto-Translation-Equivariant-Attention/paper.pdf
- Code/Project: https://github.com/FabianFuchsML/se3-transformer-public
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ModelNet40

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- We compare to publicly available, state-of-the-art results as well as a set of our own baselines.
- Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field).
- This task sets itself apart from the other two experiments by not being invariant but equivariant: When the input is rotated or translated, the output changes respectively (see ...
- The equivariance error shows that our approach is indeed fully rotation equivariant up to the precision of the computations. input label Set Transf. input label SE(3) Transf. original ...
- We compare to publicly available, state-of-the-art results as well as a set of our own baselines.
- We further achieve competitive performance on two real-world datasets, ScanObjectNN and QM9.

## Baselines
- We compare to publicly available, state-of-the-art results as well as a set of our own baselines.
- Specifically, we compare to the Set-Transformer , a non-equivariant attention model, and Tensor Field Networks , which is similar to SE(3)-Transformer but does not leverage attention.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
