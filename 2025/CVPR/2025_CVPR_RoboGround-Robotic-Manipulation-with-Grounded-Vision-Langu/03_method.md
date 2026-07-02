# Method

- Year/Venue: 2025 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, grounding, Robotics
- Paper link: ./2025/CVPR/2025_CVPR_RoboGround-Robotic-Manipulation-with-Grounded-Vision-Langu/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To further explore and enhance generalization, we propose an automated pipeline for generating large-scale, simulated data with a diverse set of objects and instructions.
- We introduce ROBO G ROUND, a groundingaware robotic manipulation policy that leverages grounding masks as an intermediate representation to guide policy networks in object manipulation tasks.
- Since the pre-trained model is unavailable, we reproduce it here without large-scale pre-training or image prediction.

## 원리적 동기
- Previous Work Recent advancements in robotic manipulation have highlighted the potential of intermediate representations for improving policy generalization.
- To further explore and enhance generalization, we propose an automated pipeline for generating large-scale, simulated data with a diverse set of objects and instructions.

## 핵심 방법론
- Since the pre-trained model is unavailable, we reproduce it here without large-scale pre-training or image prediction.
- Unseen instances refer to evaluation on new objects within classes present in the training data, while unseen classes involve evaluation on objects from entirely new classes not included ...
- Unseen instance denotes evaluation on new objects belonging to classes present in the training data.
- In contrast, unseen class refers to evaluation on objects from entirely new classes that were not included in the training data.
- While BC-Transformer and GR-1 benefit from language input, their performance on more challenging tasks remains relatively low.
