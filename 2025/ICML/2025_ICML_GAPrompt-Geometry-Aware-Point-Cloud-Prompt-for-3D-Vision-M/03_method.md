# Method

- Year/Venue: 2025 / ICML poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_GAPrompt-Geometry-Aware-Point-Cloud-Prompt-for-3D-Vision-M/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.
- Additionally, we present a Point Shift Prompter designed to extract global shape information from the point cloud, enabling instance-specific geometric adjustments at the input level.
- First, we introduce a Point Prompt that serves as an auxiliary input alongside the original point cloud, explicitly guiding the model to capture fine-grained geometric details.

## 원리적 동기
- To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.
- Our GAPrompt compares to full fine-tuning and existing PEFT methods.
- To address this challenge, we propose a novel Geometry-Aware Point Cloud Prompt (GAPrompt) that leverages geometric cues to enhance the adaptability of 3D vision models.

## 핵심 방법론
- Reference Param.(M) ↓ ScanObjectNN FLOPs(G) ↓ OBJ BG ModelNet40 OBJ ONLY PB T50 RS Acc. (%) ↑ 85.54 88.12 89.30 88.29 88.81 93.12 96.60 93.29 78.79 83.07 84.60 ...
- While existing methods often struggle to capture fine-grained geometric features due to their token-level adaptation constraints, our Point Prompt and Point Shift Prompter mechanisms directly modulate hi in ...
- 18, enabling precise latent space adjustments at the point level.
- This fundamental difference in operational granularity contributes to enhanced geometric feature representation and more effective model adaptation for point cloud models.
- FEMAE (Zha et al., 2024) as baselines.
