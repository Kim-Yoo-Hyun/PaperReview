# Method

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICRA/2026_ICRA_Scalable-Vision-Language-Action-Model-Pretraining-for-Robo/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our model consists of a VLM backbone and a diffusion action expert.
- We use PaliGemma-2 as the VLM, which combines a SigLIP vision encoder with linear projection for alignment and a Gemma-2 language model for multi-modal token processing.
- We use the 3B-parameter model with an input image resolution of 2242 as the default setting.

## 원리적 동기
- Existing Vision-Language-Action data for robotic manipulation are typically collected in laboratory settings through human teleoperations .
- Although such robot action data is invaluable, its high acquisition cost significantly limits both the scale of the collected data and its diversity in skills, object categories, and ...
- Our model consists of a VLM backbone and a diffusion action expert.

## 핵심 방법론
- Our model consists of a VLM backbone and a diffusion action expert.
- We use PaliGemma-2 as the VLM, which combines a SigLIP vision encoder with linear projection for alignment and a Gemma-2 language model for multi-modal token processing.
- We use the 3B-parameter model with an input image resolution of 2242 as the default setting.
- An overview of our model architecture is presented in Fig.
- For the action expert, we apply a Diffusion Transformer (DiT) and the DiT-Base model is used by default.
