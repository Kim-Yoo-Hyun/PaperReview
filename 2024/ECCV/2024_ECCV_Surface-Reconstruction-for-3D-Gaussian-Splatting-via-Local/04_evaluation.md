# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Surface-Reconstruction-for-3D-Gaussian-Splatting-via-Local/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Replica

## Metrics
- accuracy
- Chamfer
- F-score

## Evaluation Protocol and Results
- Following the setting , 4 scenes are selected from ScanNet for experiments and compared ours with both the GSrec 11 Table 1: The quantitative results of the scene ...
- 1 where our method outperforms both of SuGaR’s variants with a clear margin.
- Although SuGaR (SDF) achieves better quality, the inaccurate depth in the texture-less region such as walls in Fig.
- Chamfer distance↓ room0 room1 room2 office0 office1 office2 office3 office4 average SuGaR (density) 8.84 SuGaR (SDF) 7.28 GSrec (Ours) 6.08 F-score ↑ 9.79 8.10 6.08 12.59 10.85 9.97 ...
- Extensive experimental results demonstrate the effectiveness of our method in achieving superior mesh quality compared with the SoTA surface reconstruction for 3DGS.
- Following the setting , 4 scenes are selected from ScanNet for experiments and compared ours with both the GSrec 11 Table 1: The quantitative results of the scene ...

## Baselines
- Since we have the Gaussian means and the normals for this baseline, we can also apply to extract a mesh from it.
- We compare our method against the SoTA surface reconstruction method for 3D Gaussian Splatting in terms of Chamfer distance and F-score.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
