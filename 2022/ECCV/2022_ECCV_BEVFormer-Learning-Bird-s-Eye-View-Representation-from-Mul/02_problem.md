# Problem

- Year/Venue: 2022 / ECCV
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: sensor fusion, 3D perception, Planning
- Paper link: ./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/paper.pdf
- Code/Project: https://github.com/fundamentalvision/BEVFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- The significant challenges are that autonomous driving is time-critical and objects in the scene change rapidly, and thus simply stacking BEV features of cross timestamps brings extra computational ...
- Apart from the low cost for deployment, cameras own the desirable advantages to detect long-range distance objects and identify vision-based road elements (e.g., traffic lights, stoplines), compared to ...

## 해결하려는 문제
- Our approach achieves the new state-of-the-art 56.9% in terms of NDS metric on the nuScenes test set, which is 9.0 points higher than previous best arts and on ...
- For temporal information, we propose temporal selfattention to recurrently fuse the history BEV information.
- We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions.

## 선행 연구 / 배경 단서
- The significant challenges are that autonomous driving is time-critical and objects in the scene change rapidly, and thus simply stacking BEV features of cross timestamps brings extra computational ...
- However, the existing state-of-the-art multi-camera 3D detection methods rarely exploit temporal information.
- Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.
