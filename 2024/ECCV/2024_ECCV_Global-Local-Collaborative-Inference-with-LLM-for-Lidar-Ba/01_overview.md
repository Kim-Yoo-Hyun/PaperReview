# Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: semantic
- Paper link: ./2024/ECCV/2024_ECCV_Global-Local-Collaborative-Inference-with-LLM-for-Lidar-Ba/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In this way, the detection model fails to detect objects not belonging to the training object classes.

## Core Idea
- In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result and a global ...
- We use LLaMA as the LLM backbone, which is initialized by the checkpoint vicuna-7b-v1.5-16k .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on ScanNetV2 and SUN RGB-D demonstrate the superiority of our methods.
- 1, our proposed GLIS greatly improves the open-vocabulary detection performance on ScanNetV2.
- Our methods also significantly improve the detection precision of many classes, e.g., chair is improved by 10.79%, toilet is improved by 5.81%, and table is improved by 5.15%.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on ScanNetV2 and SUN RGB-D demonstrate the superiority of our methods.
- In this paper, we propose a Global-Local Collaborative Scheme (GLIS) for the lidar-based OVD task, which contains a local branch to generate object-level detection result and a global ...
- Intuitively, lidar point clouds provide 3D information, both object level and scene level, to generate trustful detection results.

## Abstract Cue
- Open-Vocabulary Detection (OVD) is the task of detecting all interesting objects in a given scene without predefined object classes.
