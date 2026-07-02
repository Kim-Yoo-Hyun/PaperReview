# Method

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2026/ICML/2026_ICML_MapDream-Task-Driven-Map-Learning-for-Vision-Language-Navi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird’seye-view (BEV) image synthesis.
- Supervised pretraining bootstraps a reliable mapping-to-control interface, while the autoregressive design enables end-to-end joint optimization through reinforcement fine-tuning.
- RxR Val-Unseen SR ↑ SR ↑ Table 2 further reports zero-shot generalization to RxR-CE when training only on R2R-CE.

## 원리적 동기
- However, most existing approaches rely on hand-crafted maps constructed independently of the navigation policy.
- A central difficulty of VLN is partial observability.
- Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird’seye-view (BEV) image synthesis.

## 핵심 방법론
- RxR Val-Unseen SR ↑ SR ↑ Table 2 further reports zero-shot generalization to RxR-CE when training only on R2R-CE.
