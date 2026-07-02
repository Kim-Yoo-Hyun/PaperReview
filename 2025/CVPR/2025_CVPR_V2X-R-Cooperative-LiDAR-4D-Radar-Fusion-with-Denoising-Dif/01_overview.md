# V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection

- Year/Venue: 2025 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_V2X-R-Cooperative-LiDAR-4D-Radar-Fusion-with-Denoising-Dif/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Weather-robust 4D radar, with Doppler velocity and additional geometric information, offers a promising solution to this challenge.
- Introduction Outdoor environments, however, present complex and dynamic challenges, including various occlusions and weather conditions .

## Core Idea
- Experimental Details and Metrics We used 8,084/829/3,166 frames for training/ validation/ testing in our V2X-R dataset, ensuring there is no overlap in the intersection of the training/validation/testing sets.
- Subsequently, we propose a novel cooperative LiDAR-4D radar fusion pipeline for 3D object detection and implement it with multiple fusion strategies.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that our LiDAR-4D radar fusion pipeline demonstrates superior performance in the V2X-R dataset.
- To achieve weather-robust detection, we additionally propose a Multi-modal Denoising Diffusion (MDD) module in our fusion pipeline.
- Over and above this, our MDD module further improved the foggy/snowy performance of the basic fusion model by up to 5.73%/6.70% and barely disrupting normal performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that our LiDAR-4D radar fusion pipeline demonstrates superior performance in the V2X-R dataset.
- To achieve weather-robust detection, we additionally propose a Multi-modal Denoising Diffusion (MDD) module in our fusion pipeline.
- Subsequently, we propose a novel cooperative LiDAR-4D radar fusion pipeline for 3D object detection and implement it with multiple fusion strategies.

## Abstract Cue
- 4D Radar in Multi-Agent View Instance Weather robustness 4D radar in Agent3 Current Vehicle-to-Everything (V2X) systems have significantly enhanced 3D object detection using LiDAR and camera data.
