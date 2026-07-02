# Method

- Year/Venue: 2025 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, prompting, Robotics
- Paper link: ./2025/CVPR/2025_CVPR_Object-Centric-Prompt-Driven-Vision-Language-Action-Model/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space.
- To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.
- To avoid a collision, we introduce a “pre-move” waypoint before reaching the predicted contact pose.

## 원리적 동기
- To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner.
- To address these challenges, several works propose using visual prompts as a convenient yet expressive modality for goal specification.
- We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space.

## 핵심 방법론
- To avoid a collision, we introduce a “pre-move” waypoint before reaching the predicted contact pose.
- Comparison of our method against baseline methods. (s) and (f) denote suction gripper and finger gripper, respectively.
