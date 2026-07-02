# Method

- Year/Venue: 2026 / ICRA
- Category: Navigation and Embodied AI
- Tags: Robotics, Navigation
- Paper link: ./2026/ICRA/2026_ICRA_LaViRA-Language-Vision-Robot-Actions-Translation-for-Zero/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce LaViRA, a simple yet effective zero-shot framework that addresses this dilemma by decomposing action into a coarse-to-fine hierarchy: Language Action for high-level planning, Vision Action for ...
- — Zero-shot Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an agent to navigate unseen environments based on natural language instructions without any prior training.

## 원리적 동기
- I NTRODUCTION Vision-and-Language Navigation (VLN) presents the challenge of grounding natural language instructions within visual observations to enable an embodied agent to navigate through previously unseen environments .
- LaViRA significantly outperforms existing state-of-the-art methods on the VLN-CE benchmark, demonstrating superior generalization capabilities in unseen environments, while maintaining transparency and efficiency for real-world deployment.
- We introduce LaViRA, a simple yet effective zero-shot framework that addresses this dilemma by decomposing action into a coarse-to-fine hierarchy: Language Action for high-level planning, Vision Action for ...

## 핵심 방법론
- CMA RecBERT ETPNav BEVBert Random NavGPT-CE DiscussNav-CE MapGPT-CE Open-Nav SmartWay InstructNav CA-Nav GC-VLN LaViRA(GPT-4o) LaViRA(Gemini-2.5-Pro) OSR↑ SR↑ SPL↑ Supervised Learning 6.92 45 5.80 57 5.15 58 5.13
