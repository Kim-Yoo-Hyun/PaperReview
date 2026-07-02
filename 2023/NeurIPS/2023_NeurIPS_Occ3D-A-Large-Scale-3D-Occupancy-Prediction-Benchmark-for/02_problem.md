# Problem

- Year/Venue: 2023 / NeurIPS
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: 3D Vision, occupancy, sensor fusion, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Occ3D-A-Large-Scale-3D-Occupancy-Prediction-Benchmark-for/paper.pdf
- Code/Project: https://tsinghua-mars-lab.github.io/Occ3D/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- These limitations call for a general and coherent representation that can model the detailed geometry and semantics of objects both within and outside of the ontology tree.
- 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations.
- Existing methods typically focus on estimating 3D bounding boxes, neglecting finer geometric details and struggling to handle general, out-of-vocabulary objects.

## 해결하려는 문제
- Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- To support 3D occupancy prediction, we develop a label generation pipeline that produces dense, visibility-aware labels for any given scene.
- We establish two benchmarks, derived from the Waymo Open Dataset and the nuScenes Dataset, namely Occ3D-Waymo and Occ3D-nuScenes benchmarks.

## 선행 연구 / 배경 단서
- The contributions of this work are as follows: (1) We introduce Occ3D, a high-quality 3D occupancy prediction benchmark to facilitate research in this emerging area; (2) We put ...
- These limitations call for a general and coherent representation that can model the detailed geometry and semantics of objects both within and outside of the ontology tree.
- Additionally, we propose CTF-Occ, a transformer-based Coarse-To-Fine 3D Occupancy prediction network.
