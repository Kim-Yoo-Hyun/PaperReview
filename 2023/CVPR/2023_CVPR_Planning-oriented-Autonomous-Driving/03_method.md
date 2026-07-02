# Method

- Year/Venue: 2023 / CVPR
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: Planning, sensor fusion, 3D perception
- Paper link: ./2023/CVPR/2023_CVPR_Planning-oriented-Autonomous-Driving/paper.pdf
- Code/Project: https://github.com/OpenDriveLab/UniAD
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce Unified Autonomous Driving (UniAD), a comprehensive framework up-to-date that incorporates full-stack driving tasks in one network.
- Mask” represent cross-attention and the attention mask in the pixel-agent interaction respectively. “Mask Feat.” denotes the reuse of the mask feature for instance-level occupancy.
- Mask ✓ ✓ Mask Feat. ✓ IoU-n.↑ IoU-f.↑ VPQ-n.↑ VPQ-f.↑ 61.2 61.3 62.3 62.6 39.7 39.4 39.7 39.5 51.5 51.0 52.4 53.2 31.8 31.8 32.5 32.8 guided attention ...

## 원리적 동기
- Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due to the isolation ...
- Modern autonomous driving system is characterized as modular tasks in sequential order, i.e., perception, prediction, and planning.
- We introduce Unified Autonomous Driving (UniAD), a comprehensive framework up-to-date that incorporates full-stack driving tasks in one network.

## 핵심 방법론
- Mask” represent cross-attention and the attention mask in the pixel-agent interaction respectively. “Mask Feat.” denotes the reuse of the mask feature for instance-level occupancy.
- Mask ✓ ✓ Mask Feat. ✓ IoU-n.↑ IoU-f.↑ VPQ-n.↑ VPQ-f.↑ 61.2 61.3 62.3 62.6 39.7 39.4 39.7 39.5 51.5 51.0 52.4 53.2 31.8 31.8 32.5 32.8 guided attention ...
- Cross-attention with masks and the reuse of mask feature helps improve the prediction. “Cross.
- As illustrated in Table 9, attending each pixel to all agents without locality constraints (Exp.2) results in slightly worse performance compared to an attention-free baseline (Exp.1).
