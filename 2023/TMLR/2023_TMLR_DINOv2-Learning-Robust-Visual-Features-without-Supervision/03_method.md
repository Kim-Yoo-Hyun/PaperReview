# Method

- Year/Venue: 2023 / TMLR
- Category: Foundations: Vision Foundation Models
- Tags: self-supervised, representation
- Paper link: ./2023/TMLR/2023_TMLR_DINOv2-Learning-Robust-Visual-Features-without-Supervision/paper.pdf
- Code/Project: https://github.com/facebookresearch/dinov2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised ...
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision.

## 원리적 동기
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.
- In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised ...

## 핵심 방법론
- ViT-g/14 ViT-L/14 ViT-L/14 Scratch Scratch Distill 86.5 84.5 86.3 73.4 72.2 73.3 1.00 1.10 1.08 92.1 90.2 91.2 Arch Method Finegr.
- ARSketch Video ViT-g/14 ViT-L/14 ViT-L/14 Scratch Scratch Distill 78.3 75.8 77.6 75.2 71.3 76.3 77.0 69.5 74.5 69.3 67.3 67.5 (a) Comparison on individual metrics (b) Averaged metrics ...
- Comparison between a ViT-L trained from scratch or distilled from DINOv2 using ViT-g/14.
- For reference, we also report the performance of the ViT-g/14 teacher.
- We show that a ViT-L model distilled from a frozen ViT-g outperforms a the same model trained from scratch on all benchmarks, sometimes even outperforming the distillation target.
