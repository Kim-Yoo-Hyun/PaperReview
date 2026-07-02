# Method

- Year/Venue: 2022 / ECCV
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: sensor fusion, 3D perception, Planning
- Paper link: ./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/paper.pdf
- Code/Project: https://github.com/fundamentalvision/BEVFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- For temporal information, we propose temporal selfattention to recurrently fuse the history BEV information.
- Compared with training tasks individually, multi-task learning saves computational cost and reduces the inference time by sharing more modules,
- To aggregate spatial information, we design spatial cross-attention that each BEV query extracts the spatial features from the regions of interest across camera views.

## 원리적 동기
- The significant challenges are that autonomous driving is time-critical and objects in the scene change rapidly, and thus simply stacking BEV features of cross timestamps brings extra computational ...
- Apart from the low cost for deployment, cameras own the desirable advantages to detect long-range distance objects and identify vision-based road elements (e.g., traffic lights, stoplines), compared to ...
- For temporal information, we propose temporal selfattention to recurrently fuse the history BEV information.

## 핵심 방법론
- Compared with training tasks individually, multi-task learning saves computational cost and reduces the inference time by sharing more modules,
- While comparing different BEV encoders under same settings, BEVFormer achieves higher performances of all tasks except for road segmentation results is comparable with BEVFormer-S.
