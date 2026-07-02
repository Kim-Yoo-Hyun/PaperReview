# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VLA-OS-Structuring-and-Dissecting-Planning-Representations/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture ...
- First, to avoid biases introduced by specific neural network choices, we develop VLA-OS1 model series: 1 “OS” stands for “Operating System” and designates that our model family provides ...
- However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of ...

## 원리적 동기
- 3) Bottleneck: Between task planning and policy learning, which presents a greater challenge for current manipulation tasks?
- Among these challenges, five core questions stand out: 1) Representation: What representation should we adopt for task planning and policy learning?
- To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture ...

## 핵심 방법론
- First, to avoid biases introduced by specific neural network choices, we develop VLA-OS1 model series: 1 “OS” stands for “Operating System” and designates that our model family provides ...
- However, current task-planning approaches in VLA are mainly based on intuitive designs and lack fair and systematic comparisons, as these methods vary along multiple dimensions, including network architectures, ...
- Recent studies have increasingly emphasized the development of foundational models for robot manipulation tasks by training large Vision-Language-Action models (VLAs) on extensive datasets .
- Hierarchical-VLA exhibits a generally better performance than ActionOnly-VLA and Integrated-VLA, while it incurs larger training and inference costs.
- 4) Scalability and Pretraining: Do VLAs that incorporate task planning preserve the advantageous properties of end-to-end foundation models, such as model and data scalability, as well as benefits ...
