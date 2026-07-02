# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model
- Paper link: ./2025/ICCV/2025_ICCV_Egocentric-Action-aware-Inertial-Localization-in-Point-Clo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The learned encoders are then used in reasoning the IMU data and the point cloud over time and space to perform inertial localization.
- Interestingly, these encoders can further be utilized to recognize the corresponding sequence of actions as a by-product.
- By assuming that the 3D point cloud of the environment is available, it contrastively learns modality encoders that align short-term egocentric action cues in IMU signals with local ...

## 원리적 동기
- Localization: Acceleration This paper presents a novel inertial localization framework named Egocentric Action-aware Inertial Localization (EAIL), which leverages egocentric action cues from headmounted IMU signals to localize the ...
- Human inertial localization is challenging due to IMU sensor noise that causes trajectory drift over time.
- The learned encoders are then used in reasoning the IMU data and the point cloud over time and space to perform inertial localization.

## 핵심 방법론
- 0.4m 0.6m RS 0.2m 0.4m 0.6m RS MnasNet 2.95 7.57 12.75 / 2.16 5.45 9.86 / EfficientNet 3.10 7.77 12.71 / 2.54 6.68 10.84 / IMUNet 3.74 10.15 ...
- Inertial Action Recognition Results.
- We evaluate performance using top1 and top5 accuracy metrics.
- Higher values indicate better performance.
- EfficientNet IMUNet MnasNet RoNIN NiLoc+ Ours 2.5 2.0 1.5 Method 0.0 0 2 4
