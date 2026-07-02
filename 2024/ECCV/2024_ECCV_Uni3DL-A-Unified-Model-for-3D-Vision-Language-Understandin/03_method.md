# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Uni3DL-A-Unified-Model-for-3D-Vision-Language-Understandin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present Uni3DL, a unified model for 3D Vision-Language understanding.
- On the BLEU-1 and ROUGE-L scores, our method beats precious STOA methods by a large margin (more than 20%).
- With a unified architecture, our Uni3DL model enjoys seamless task decomposition and substantial parameter sharing across tasks.

## 원리적 동기
- Extending these successes of unified vision-language modeling in the 2D domain to 3D perception tasks remains a formidable challenge.
- This difficulty primarily stems from the substantial architectural differences between 2D and 3D models, along with the limited availability of extensive 3D datasets for pre-training purposes.
- We present Uni3DL, a unified model for 3D Vision-Language understanding.

## 핵심 방법론
- On the BLEU-1 and ROUGE-L scores, our method beats precious STOA methods by a large margin (more than 20%).
- Note that Swin3D† uses extra training data (Structure3D ). localization because minor boundary inaccuracies in segmentation masks minimally impact segmentation IOU, but can significantly alter bounding box locations.
