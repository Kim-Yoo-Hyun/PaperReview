# Method

- Year/Venue: 2026 / ICRA
- Category: Navigation and Embodied AI
- Tags: VLA, Vision-Language Model, Robotics, Navigation
- Paper link: ./2026/ICRA/2026_ICRA_OmniVLA-An-Omni-Modal-Vision-Language-Action-Model-for-Rob/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present videos showcasing OmniVLA’s performance and will release its checkpoints and training code on our project page1 .
- In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation.
- We conduct an ablation study to highlight the benefits of training OmniVLA with a larger and more diverse data mixture while keeping the model architecture fixed.

## 원리적 동기
- In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and ...
- However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.
- We present videos showcasing OmniVLA’s performance and will release its checkpoints and training code on our project page1 .

## 핵심 방법론
- We conduct an ablation study to highlight the benefits of training OmniVLA with a larger and more diverse data mixture while keeping the model architecture fixed.
- Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the 1B MiniVLA and the 500M SmolVLA ...
- Additionally, we observe that the choice of pre-trained VLA architecture and pre-training data has a significant impact on the performance.
- Our method successfully follows the language instructions and reaches the target object, whereas the baselines LeLaN and CoW fail, navigating instead toward the incorrect object.
- To ensure fair comparison with our approach, which relies solely on a single RGB camera without depth or LiDAR, we estimate depth using Depth360 and project it to ...
