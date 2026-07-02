# Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model
- Paper link: ./2025/ICCV/2025_ICCV_Egocentric-Action-aware-Inertial-Localization-in-Point-Clo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Localization: Acceleration This paper presents a novel inertial localization framework named Egocentric Action-aware Inertial Localization (EAIL), which leverages egocentric action cues from headmounted IMU signals to localize the ...
- Human inertial localization is challenging due to IMU sensor noise that causes trajectory drift over time.
- The diversity of human actions further complicates IMU signal processing by introducing various motion patterns.

## Core Idea
- The learned encoders are then used in reasoning the IMU data and the point cloud over time and space to perform inertial localization.
- Interestingly, these encoders can further be utilized to recognize the corresponding sequence of actions as a by-product.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate the effectiveness of the proposed framework over state-of-the-art inertial localization and inertial action recognition baselines.
- The learning process is enhanced using concurrently collected vision and language signals to improve multimodal alignment.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate the effectiveness of the proposed framework over state-of-the-art inertial localization and inertial action recognition baselines.
- By assuming that the 3D point cloud of the environment is available, it contrastively learns modality encoders that align short-term egocentric action cues in IMU signals with local ...
- The learned encoders are then used in reasoning the IMU data and the point cloud over time and space to perform inertial localization.

## Abstract Cue
- Localization: Acceleration This paper presents a novel inertial localization framework named Egocentric Action-aware Inertial Localization (EAIL), which leverages egocentric action cues from headmounted IMU signals to localize the target individual within a 3D point cloud.
