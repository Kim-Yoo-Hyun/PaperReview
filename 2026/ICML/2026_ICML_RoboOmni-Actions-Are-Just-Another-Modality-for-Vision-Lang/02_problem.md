# Problem

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_RoboOmni-Actions-Are-Just-Another-Modality-for-Vision-Lang/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in their parent models.
- However, unified discrete frameworks lag behind decoupled continuous designs due to limitations in action chunking and temporal modeling.
- Instead, they often overfit significantly to the specific robotic datasets and environments seen during training (Li et al., 2026; Kim et al., 2024), losing the zero-shot or few-shot ...

## 해결하려는 문제
- Extensive evaluations on the CALVIN, SimplerEnv, and realworld platforms confirm that RoboOmni establishes new state-of-the-art performance, significantly outperforming diffusion-based baselines such as π0 .
- To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.
- At the core of our method is Multi-Token Action Prediction (MTAP), which integrates action chunking directly into the discrete tokenizer.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
