# Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Planning, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Therefore, solving the skill chaining problem in long-horizon tasks while preserving the scalability and data efficiency of VLA models remains a fundamental and open challenge.
- However, most existing VLA frameworks are tailored for short-horizon tasks, leaving the challenge of long-horizon task execution largely unresolved.
- Although this strategy reduces the complexity of learning individual behaviors, it does not adequately account for the transitions and dependencies between subtasks, commonly referred to as the skill ...

## Core Idea
- This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models.
- In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- RQ2: How does our Long-VLA compare with state-of-the-art (SOTA) methods?
- We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation.
- 4.1 Experiments Setup Simulation & Real-world Experiment.

## Limitation
- In conclusion, Long-VLA advances the field of generalist robotics by introducing a unified, end-toend approach to long-horizon manipulation, effectively addressing the persistent challenge of skill chaining through a ...

## Contribution
- This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models.
- In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks.
- Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues ...

## Abstract Cue
- : Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control.
