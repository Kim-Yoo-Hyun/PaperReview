# Problem

- Year/Venue: 2026 / ICML Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_LaST-0-Latent-Spatio-Temporal-Chain-of-Thought-for-Robotic/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- propose LaST0 , a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to ...
- Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes.

## 해결하려는 문제
- Furthermore, LaST0 adopts a dualsystem architecture implemented via a Mixtureof-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on ...
- Across 10 real-world tasks spanning tabletop, mobile, and dexterous hand manipulation, LaST0 improves mean success rates by 13%, 14% and 14% over prior state-of-the-art VLA methods, respectively.
- Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
