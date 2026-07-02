# Problem

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2026/ICML/2026_ICML_MapDream-Task-Driven-Map-Learning-for-Vision-Language-Navi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, most existing approaches rely on hand-crafted maps constructed independently of the navigation policy.
- A central difficulty of VLN is partial observability.
- Agents perceive the environment only through local, sequential observations, which limits their understanding of the space.

## 해결하려는 문제
- Experiments on R2RCE and RxR-CE achieve state-of-the-art monocular performance, validating task-driven generative map learning.
- Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird’seye-view (BEV) image synthesis.
- Supervised pretraining bootstraps a reliable mapping-to-control interface, while the autoregressive design enables end-to-end joint optimization through reinforcement fine-tuning.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
