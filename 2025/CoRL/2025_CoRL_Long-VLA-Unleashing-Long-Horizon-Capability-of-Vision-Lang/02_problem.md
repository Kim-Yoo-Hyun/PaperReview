# Problem

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Planning, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Therefore, solving the skill chaining problem in long-horizon tasks while preserving the scalability and data efficiency of VLA models remains a fundamental and open challenge.
- However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.
- Although this strategy reduces the complexity of learning individual behaviors, it does not adequately account for the transitions and dependencies between subtasks, commonly referred to as the skill ...

## 해결하려는 문제
- This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models.
- In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks.
- Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues ...

## 선행 연구 / 배경 단서
- Therefore, solving the skill chaining problem in long-horizon tasks while preserving the scalability and data efficiency of VLA models remains a fundamental and open challenge.
- However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.
- For example, reward-driven online methods are difficult to reconcile with the large-scale offline training regime typical of VLA models, while modular architectures hinder joint end-to-end learning and contradict ...
