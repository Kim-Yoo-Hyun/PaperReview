# Method

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, consistency, 4D reasoning
- Paper link: ./2026/CVPR/2026_CVPR_ConsisVLA-4D-Advancing-Spatiotemporal-Consistency-in-Effic/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We introduce CV-Aligner and ...
- To achieve explicit semantic object selection, we retain only the Top-K tokens most relevant to the instruction: (5) On the other hand, we use the aggregated geometric relation ...
- To this end, we propose ConsisVLA-4D, a unified and efficient framework that enhances spatiotemporal consistency in 3D-perception and 4D-reasoning, as shown in Fig.

## 원리적 동기
- Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often rely on additional ...
- Due to the lack of a comprehensive understanding of current spatial states and insufficient knowledge of evolving scene dynamics, existing methods struggle to build consistent correlations with predicted ...
- Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We introduce CV-Aligner and ...

## 핵심 방법론
- The overall training objective is formulated as: \small \mathcal {L}_{\text {total}} = \mathcal {L}_{\text {action}} + \mathcal {L}_{\text {dyn-4D}} + \mathcal {L}_{\text {dep-4D}}.
- In real-world, we reproduce three representative models, including OpenVLA (base model), and OpenVLAOFT (the best 7B baseline in performance and efficiency), with training and deployment settings identical.
- During training, CS-Thinker learns the complete processes from Eq.
- D. represent the training-only dynamic objects and global depth representations in 4D-Reasoning, respectively.
- Compared to simulation, the real-world setup adds a new viewpoint input, increases the action chunk size from 8 to 25, and reduces the training batch size from 64 ...
