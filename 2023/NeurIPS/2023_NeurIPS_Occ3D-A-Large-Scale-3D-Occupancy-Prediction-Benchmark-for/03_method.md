# Method

- Year/Venue: 2023 / NeurIPS
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: 3D Vision, occupancy, sensor fusion, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Occ3D-A-Large-Scale-3D-Occupancy-Prediction-Benchmark-for/paper.pdf
- Code/Project: https://tsinghua-mars-lab.github.io/Occ3D/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To optimize the occupancy prediction, we use the OHEM loss for model training P Locc = W L(gk , pk ), where Wk , gk , and pk ...
- Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- To support 3D occupancy prediction, we develop a label generation pipeline that produces dense, visibility-aware labels for any given scene.

## 원리적 동기
- These limitations call for a general and coherent representation that can model the detailed geometry and semantics of objects both within and outside of the ontology tree.
- 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations.
- To optimize the occupancy prediction, we use the OHEM loss for model training P Locc = W L(gk , pk ), where Wk , gk , and pk ...

## 핵심 방법론
- To optimize the occupancy prediction, we use the OHEM loss for model training P Locc = W L(gk , pk ), where Wk , gk , and pk ...
- It can be observed that our method performs better in all classes than previous baseline methods under the IoU metric.
- Especially for some objects such as traffic cone and vehicle, our method surpasses the baseline method by 2.88 and 10.23 IoU respectively.
- BEVDet TPVFormer BEVFormer CTF-Occ (Ours) 0.13 13.06 2.17 10.15 7.80 5.85 4.62 0.94 1.49 0.0 7.27 10.06 2.35 48.15 34.12 9.88 3.89 17.86 12.03 5.67 13.64 8.49 8.90 ...
- We replace their original detection decoders with the occupancy decoder adopted in our CTF-Occ network and remain their BEV feature encoders.
