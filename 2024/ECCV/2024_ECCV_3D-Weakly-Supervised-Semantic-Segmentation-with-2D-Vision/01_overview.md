# 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_3D-Weakly-Supervised-Semantic-Segmentation-with-2D-Vision/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- 3D point cloud semantic segmentation [13, 16, 27–29, 43] can provide valuable geometric and semantic data about the 3D environment and has gained considerable attention over the past ...

## Core Idea
- Subsequently, we introduce semantic segmentation methods supervised by scene-level labels or subcloud-level labels and compare them with our method.
- In this paper, we propose 3DSS-VLG, a weakly supervised approach for 3D Semantic Segmentation with 2D Vision-Language Guidance, an alternative approach that a 3D model predicts denseembedding for ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Moreover, with extensive quantitative and qualitative experiments, we present that our 3DSS-VLG is able not only to achieve the state-ofthe-art performance on both S3DIS and ScanNet datasets, but ...
- Finally, ablation studies are provided to further demonstrate the necessity and effectiveness of each component of our framework.
- 4.1 Datasets and Evaluation Metrics We evaluate our 3DSS-VLG on two publicly and widely-used large-scale point cloud datasets with multi-view images, S3DIS and ScanNet .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Moreover, with extensive quantitative and qualitative experiments, we present that our 3DSS-VLG is able not only to achieve the state-ofthe-art performance on both S3DIS and ScanNet datasets, but ...
- In this paper, we propose 3DSS-VLG, a weakly supervised approach for 3D Semantic Segmentation with 2D Vision-Language Guidance, an alternative approach that a 3D model predicts denseembedding for ...
- Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised by the corresponding ...

## Abstract Cue
- In this paper, we propose 3DSS-VLG, a weakly supervised approach for 3D Semantic Segmentation with 2D Vision-Language Guidance, an alternative approach that a 3D model predicts denseembedding for each point which is co-embedded with both the aligned image and text spaces from the 2D vision-language ...
