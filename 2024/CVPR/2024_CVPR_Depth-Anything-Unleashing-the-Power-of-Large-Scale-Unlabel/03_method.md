# Method

- Year/Venue: 2024 / CVPR
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_Depth-Anything-Unleashing-the-Power-of-Large-Scale-Unlabel/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision.
- Following MiDaS , we use the DPT decoder for
- We use the AdamW optimizer and decay the learning rate with a linear schedule.

## 원리적 동기
- Monocular Depth Estimation (MDE), which is a fundamental problem with broad applications in robotics , autonomous driving , virtual reality , etc., also requires a foundation model to ...
- This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision.

## 핵심 방법론
- This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision.
- Following MiDaS , we use the DPT decoder for
- We use the AdamW optimizer and decay the learning rate with a linear schedule.
- In the second stage of joint training, we train a student model to sweep across all unlabeled images for one time.
- Note that MiDaS does not strictly follow the zero-shot evaluation on KITTI and NYUv2, because it uses their training images.
