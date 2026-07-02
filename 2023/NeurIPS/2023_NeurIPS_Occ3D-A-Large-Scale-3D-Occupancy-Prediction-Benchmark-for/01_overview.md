# Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving

- Year/Venue: 2023 / NeurIPS
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: 3D Vision, occupancy, sensor fusion, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Occ3D-A-Large-Scale-3D-Occupancy-Prediction-Benchmark-for/paper.pdf
- Code/Project: https://tsinghua-mars-lab.github.io/Occ3D/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- These limitations call for a general and coherent representation that can model the detailed geometry and semantics of objects both within and outside of the ontology tree.
- 3D occupancy prediction, which estimates the detailed occupancy states and semantics of a scene, is an emerging task to overcome these limitations.
- Existing methods typically focus on estimating 3D bounding boxes, neglecting finer geometric details and struggling to handle general, out-of-vocabulary objects.

## Core Idea
- To optimize the occupancy prediction, we use the OHEM loss for model training P Locc = W L(gk , pk ), where Wk , gk , and pk ...
- Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- To benchmark our proposed Occ3D datasets and our CTF-Occ model, we evaluate existing 3D occupancy prediction methods on Occ3D-nuScenes and Occ3D-Waymo.
- We establish two benchmarks, derived from the Waymo Open Dataset and the nuScenes Dataset, namely Occ3D-Waymo and Occ3D-nuScenes benchmarks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Lastly, we propose a new model, dubbed Coarse-to-Fine Occupancy (CTF-Occ) network, which demonstrates superior performance on the Occ3D benchmarks.
- To support 3D occupancy prediction, we develop a label generation pipeline that produces dense, visibility-aware labels for any given scene.
- We establish two benchmarks, derived from the Waymo Open Dataset and the nuScenes Dataset, namely Occ3D-Waymo and Occ3D-nuScenes benchmarks.

## Abstract Cue
- Robotic perception requires the modeling of both 3D geometry and semantics.
