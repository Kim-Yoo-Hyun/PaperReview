# Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation

- Year/Venue: 2025 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, prompting, Robotics
- Paper link: ./2025/CVPR/2025_CVPR_Object-Centric-Prompt-Driven-Vision-Language-Action-Model/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.
- To address these challenges, several works propose using visual prompts as a convenient yet expressive modality for goal specification.
- Language instructions can be ambiguous and brief, making it challenging for the robot to understand the tasks, or they can be overly detailed, increasing the difficulty for the ...

## Core Idea
- We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space.
- To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Various approaches exist to convey the goals that robots should achieve, such as language descriptions, goal images, or goal videos.
- We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space.
- We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.
- To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.

## Abstract Cue
- In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos.
