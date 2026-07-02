# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2025/ICCV/2025_ICCV_Details-Matter-for-Indoor-Open-vocabulary-3D-Instance-Segm/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose a new state-of-the-art solution for OV-3DIS by carefully designing a recipe to combine the concepts together and refining them to address key challenges.
- Additionally, we introduce the standardized maximum similarity (SMS) score to normalize text-to-proposal similarity, effectively filtering out false positives and boosting precision.
- Our method effectively retrieves instances based on functional descriptions (e.g., drink water, heat mac & cheese) and object attributes (e.g., red chair). dicted proposals into open-vocabulary queries.

## 원리적 동기
- While various concepts have been proposed from existing research, we observe that these individual concepts are not mutually exclusive but complementary.
- This paper carefully combines the concepts and refines each step to address key challenges, achieving state-of-theart
- In this paper, we propose a new state-of-the-art solution for OV-3DIS by carefully designing a recipe to combine the concepts together and refining them to address key challenges.

## 핵심 방법론
- However, we note that our method with CLIP still surpasses existing baselines by a large margin (i.e., 3.8% over Open3DIS and 2.8% over OpenYOLO3D).
