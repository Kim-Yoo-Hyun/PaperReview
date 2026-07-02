# Problem

- Year/Venue: 2024 / RA-L
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, semantic
- Paper link: ./2024/RA-L/2024_RA-L_FM-Fusion-Instance-aware-Semantic-Mapping-Boosted-by-Visio/paper.pdf
- Code/Project: https://github.com/HKUST-Aerial-Robotics/FM-Fusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- —Semantic mapping based on the supervised object detectors is sensitive to image distribution.
- In real-world environments, the object detection and segmentation performance can lead to a major drop, preventing the use of semantic mapping in a wider domain.
- On the other hand, the development of vision-language foundation models demonstrates a strong zero-shot transferability across data distribution.

## 해결하려는 문제
- Our method achieves 40.3 mean average precision (mAP) on the ScanNet semantic instance segmentation task.
- We evaluate the zero-shot performance of our method in ScanNet and SceneNN datasets.
- We propose a probabilistic label fusion method to predict close-set semantic classes from open-set label measurements.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
