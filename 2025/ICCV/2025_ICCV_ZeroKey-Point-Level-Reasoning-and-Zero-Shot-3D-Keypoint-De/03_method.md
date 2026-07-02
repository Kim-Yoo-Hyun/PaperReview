# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ZeroKey-Point-Level-Reasoning-and-Zero-Shot-3D-Keypoint-De/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a novel zero-shot approach for keypoint detection on 3D shapes.
- We then select the area overlapped with the bounding box prediction as the detected points and lift these 2D points to 3D using our method.
- We then lift these 2D keypoints to 3D using the same backprojection technique described in our method.

## 원리적 동기
- Point-level reasoning on visual data is challenging as it requires precise localization capability, posing problems even for powerful models like DINO or CLIP.
- This work opens new avenues for cross-modal learning and underscores the effectiveness of MLLMs in contributing to 3D computer vision challenges.
- We propose a novel zero-shot approach for keypoint detection on 3D shapes.

## 핵심 방법론
- We then select the area overlapped with the bounding box prediction as the detected points and lift these 2D points to 3D using our method.
- We then lift these 2D keypoints to 3D using the same backprojection technique described in our method.
- We lift the prediction of this method to 3D using the same lifting procedure used in our method to compare 3D Zero-shot keypoint detection.
- In contrast, our method precisely locates keypoints.
- Unlike our approach, this baseline does not retrieve keypoint according to a text prompt and operates fully unsupervised.
