# Method

- Year/Venue: 2026 / CVPR
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, VLA, tactile sensing, contact-rich manipulation, real-time control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- To overcome these challenges, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which introduces a novel Adaptive Tactile Injection mechanism.
- Compared to Ex0, we introduce tactile input but in a direct manner, consistent with the experiments discussed in the intuition analysis in Sec.
- We found that training them on the full sequence often leads to failures during the grasping stage, which makes it difficult to reveal their core capability—namely, reacting to ...

## 원리적 동기
- To overcome these challenges, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which introduces a novel Adaptive Tactile Injection mechanism.
- Vision-Language-Action (VLA) models have significantly advanced the capabilities of robotic agents in executing diverse tasks; however, they still face challenges in contactrich manipulation scenarios that require precise physical ...
- To overcome these challenges, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which introduces a novel Adaptive Tactile Injection mechanism.

## 핵심 방법론
- Compared to Ex0, we introduce tactile input but in a direct manner, consistent with the experiments discussed in the intuition analysis in Sec.
- We found that training them on the full sequence often leads to failures during the grasping stage, which makes it difficult to reveal their core capability—namely, reacting to ...
- Consequently, it has implicitly learned richer contact dynamics and cross-modal correlations during training, allowing it to infer approximate tactile cues from visual features at test time.
- Specifically, since there is no gating mechanism, the queries in the Adaptive Cross Attention module are conditioned on the tactile features extracted from the tactile encoder throughout the ...
- Together with Adaptive Cross Attention, it enables the attention query to switch to tactile tokens only when the gate is activated; otherwise, the attention query remains identical to ...
