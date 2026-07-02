# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_Bring-My-Cup-Personalizing-Vision-Language-Action-Models-w/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with topdown selective attention.
- We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images.
- Since user-specific instances and the personalized instructions used to refer to them (e.g., “my cup”) are rarely covered during training, these models frequently collapse to category-level recognition and ...

## 원리적 동기
- To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with topdown selective attention.
- However, general-purpose policies, such as VisionLanguage-Action (VLA) models, typically fail to meet this requirement.
- To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with topdown selective attention.

## 핵심 방법론
- We provide further analysis of the tokenlearning baseline and attention visualizations in Appendices B and B.3.
- This optimized setup achieves > 95% accuracy on VQA recognition probes, and we further verify that the learned token transfers to the VLA with minimal embedding shift and ...
- For each personal object, we optimize a specific token embedding within the VLA’s language encoder using the reference images.
