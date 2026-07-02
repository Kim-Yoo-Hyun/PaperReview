# Method

- Year/Venue: 2024 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: LLM, Robotics, Vision-Language
- Paper link: ./2024/CVPR/2024_CVPR_ManipLLM-Embodied-Multimodal-Large-Language-Model-for-Obje/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Therefore, we introduce an innovative approach for robot manipulation that leverages the robust reasoning capabilities of Multimodal Large Language Models (MLLMs) to enhance the stability and generalization of ...
- During inference, our approach utilizes an RGB image and text prompt to predict the end effector’s pose in chain of thoughts.
- Specifically, we randomly select n positive pixels with an affordance score higher than 0.8 and select n negative pixels with an affordance score lower than 0.2 as training ...

## 원리적 동기
- Robot manipulation relies on accurately predicting contact points and end-effector directions to ensure successful operation.
- However, learning-based robot manipulation, trained on a limited category within a simulator, often struggles to achieve generalizability, especially when confronted with extensive categories.
- Therefore, we introduce an innovative approach for robot manipulation that leverages the robust reasoning capabilities of Multimodal Large Language Models (MLLMs) to enhance the stability and generalization of ...

## 핵심 방법론
- Specifically, we randomly select n positive pixels with an affordance score higher than 0.8 and select n negative pixels with an affordance score lower than 0.2 as training ...
- In the simulator, when pre-collecting training data, if the manipulation is successful, we record the RGB image and the corresponding end-effector pose, which are used as model input ...
- 3.1.2 Fine-tuning Tasks Formulation We design a training paradigm to fine-tune the MLLM and stimulate the model to generate interpretable pose predictions for object-centric manipulation.
- Since we only have a language decoder (LLaMa) instead of a visual decoder, the model is not able to generate an affordance map directly.
