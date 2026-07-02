# GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model

- Year/Venue: 2025 / ICML poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_GAPrompt-Geometry-Aware-Point-Cloud-Prompt-for-3D-Vision-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.
- Our GAPrompt compares to full fine-tuning and existing PEFT methods.
- However, fully fine-tuning these models for downstream tasks is computationally expensive and storage-intensive.

## Core Idea
- To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.
- Additionally, we present a Point Shift Prompter designed to extract global shape information from the point cloud, enabling instance-specific geometric adjustments at the input level.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that GAPrompt significantly outperforms state-ofthe-art PEFT methods and achieves competitive results compared to full fine-tuning on various benchmarks, while utilizing only 2.19% of trainable parameters.
- Existing parameter-efficient fine-tuning (PEFT) approaches, which focus primarily on input token prompting, struggle to achieve competitive performance due to their limited ability to capture the geometric information inherent ...
- Recently, pre-trained 3D vision models (Yu et al., 2022; Zhang et al., 2022; Zha et al., 2024) have shown remarkable performance in processing point cloud data, enabling their ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that GAPrompt significantly outperforms state-ofthe-art PEFT methods and achieves competitive results compared to full fine-tuning on various benchmarks, while utilizing only 2.19% of trainable parameters.
- To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.
- Additionally, we present a Point Shift Prompter designed to extract global shape information from the point cloud, enabling instance-specific geometric adjustments at the input level.

## Abstract Cue
- Overall Accuracy (%) Pre-trained 3D vision models have gained significant attention for their promising performance on point cloud data.
