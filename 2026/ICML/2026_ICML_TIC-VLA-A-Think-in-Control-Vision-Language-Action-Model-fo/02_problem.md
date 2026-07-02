# Problem

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: VLA, Vision-Language Model, Robotics, Navigation, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_TIC-VLA-A-Think-in-Control-Vision-Language-Action-Model-fo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control.
- Vision-languageaction (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action.
- We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation.

## 해결하려는 문제
- Extensive experiments in simulation and on a real robot show that TICVLA consistently outperforms prior VLA models while maintaining robust real-time control under multi-second reasoning latency.
- A latencyconsistent training strategy improves robustness under variable reasoning delays.
- To support realistic evaluation, we present DynaNav, a physics-accurate, photo-realistic simulation suite for language-guided navigation in dynamic environments.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
