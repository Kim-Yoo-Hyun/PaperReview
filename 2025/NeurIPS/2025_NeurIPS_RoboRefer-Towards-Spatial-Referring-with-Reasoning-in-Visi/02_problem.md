# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Specifically, existing vision-language models (VLMs) [8–11]-based methods mainly attempt to enhance the first level, i.e., single-step spatial understanding by integrating 3D inputs.
- However, they either demand costly 3D reconstruction of multi-view images , causing modality gaps , or treat depth as RGB-like inputs via a shared image encoder, risking modality ...
- This level, where most current research [1–7] concentrates, provides the essential perceptual basis for complex spatial referring. (2) Multi-step spatial reasoning, which transcends basic understanding through compositional reasoning ...

## 해결하려는 문제
- To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via supervised fine-tuning (SFT).
- To support SFT and RFT training, we introduce RefSpatial , a large-scale dataset of 20M QA pairs (2× prior), covering 31 spatial relations (vs.
- In addition, we present RefSpatial-Bench , a challenging benchmark filling the gap

## 선행 연구 / 배경 단서
- However, they either demand costly 3D reconstruction of multi-view images , causing modality gaps , or treat depth as RGB-like inputs via a shared image encoder, risking modality ...
- Specifically, existing vision-language models (VLMs) [8–11]-based methods mainly attempt to enhance the first level, i.e., single-step spatial understanding by integrating 3D inputs.
- This level, where most current research [1–7] concentrates, provides the essential perceptual basis for complex spatial referring. (2) Multi-step spatial reasoning, which transcends basic understanding through compositional reasoning ...
