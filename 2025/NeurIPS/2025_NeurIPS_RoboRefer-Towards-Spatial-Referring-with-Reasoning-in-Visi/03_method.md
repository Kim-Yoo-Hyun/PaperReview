# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To support SFT and RFT training, we introduce RefSpatial , a large-scale dataset of 20M QA pairs (2× prior), covering 31 spatial relations (vs.
- To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via supervised fine-tuning (SFT).
- Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.

## 원리적 동기
- Specifically, existing vision-language models (VLMs) [8–11]-based methods mainly attempt to enhance the first level, i.e., single-step spatial understanding by integrating 3D inputs.
- However, they either demand costly 3D reconstruction of multi-view images , causing modality gaps , or treat depth as RGB-like inputs via a shared image encoder, risking modality ...
- To support SFT and RFT training, we introduce RefSpatial , a large-scale dataset of 20M QA pairs (2× prior), covering 31 spatial relations (vs.

## 핵심 방법론
- Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- 3.3) and necessary training details about RoboRefer (Sec.
