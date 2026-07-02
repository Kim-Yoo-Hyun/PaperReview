# Method

- Year/Venue: 2024 / ECCV
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, grounding, open-vocabulary
- Paper link: ./2024/ECCV/2024_ECCV_Grounding-DINO-Marrying-DINO-with-Grounded-Pre-Training-fo/paper.pdf
- Code/Project: https://github.com/IDEA-Research/GroundingDINO
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we develop an open-set object detector, called Grounding DINO, by marrying Transformer-based detector DINO with grounded pre-training, which can detect arbitrary objects with human inputs ...
- We use the notations “CC”, “SBU”, “VG”, “OI”, “O365”, and “YFCC” for Conceptual Captions , SBU Captions , Visual Genome , OpenImage , Objects365 , YFCC100M respectively.
- 4.4 Effects of RefC and COCO Data We add the RefCOCO/+/g (we note it as “RefC” in tables) and COCO into training in some settings.

## 원리적 동기
- Most existing open-set detectors are developed by extending closed-set detectors to open-set scenarios with language information.
- In this paper, we develop an open-set object detector, called Grounding DINO, by marrying Transformer-based detector DINO with grounded pre-training, which can detect arbitrary objects with human inputs ...

## 핵심 방법론
- We use the notations “CC”, “SBU”, “VG”, “OI”, “O365”, and “YFCC” for Conceptual Captions , SBU Captions , Visual Genome , OpenImage , Objects365 , YFCC100M respectively.
- 4.4 Effects of RefC and COCO Data We add the RefCOCO/+/g (we note it as “RefC” in tables) and COCO into training in some settings.
- Backbone Pre-Training Data Fine-tuning MAttNet VGTR TransVG VILLA_L∗ RefTR MDETR DQ-DETR R101 R101 R101 R101 R101 R101 R101 None None None CC, SBU, COCO, VG VG GoldG,RefC GoldG,RefC ...
