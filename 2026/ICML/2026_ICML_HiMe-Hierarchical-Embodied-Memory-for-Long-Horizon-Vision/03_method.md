# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_HiMe-Hierarchical-Embodied-Memory-for-Long-Horizon-Vision/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, ...
- Most existing architectures rely on the Markov assumption, where the policy is conditioned only on the transient observation at the current time step.
- HiMe addresses this challenge by organizing embodied intelligence into a hierarchical structure that separates fast execution from memory-driven reasoning over long time scales. tion with large-scale internet-level pretraining.

## 원리적 동기
- Existing solutions face a “frequency-competence paradox,” where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities.
- HiMe addresses this challenge by organizing embodied intelligence into a hierarchical structure that separates fast execution from memory-driven reasoning over long time scales. tion with large-scale internet-level pretraining.
- To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, ...

## 핵심 방법론
- HiMe (Ours) Flat Memory Components Object Search Counting Rearrangement Sentry Memory Management Memory Size API Calls (↓) Memory Hit (↑) Avg.
- Progress (↑) API Calls (↓) Memory Hit (↑) Avg.
- Progress (↑) API Calls (↓) Memory Hit (↑) Avg.
- Progress (↑) ✓ × ✓ × inf inite recent 8 1.8 5.4 94% 68% 92% 64% 2.6 4.8 98% 61% 92% 58% 1.4 6.2 92% 76% 87% 73% ...
- In Flat memory methods, the Planner is often queried every step to interpret the visual buffer, placing the expensive LLM in a high-frequency control loop.
