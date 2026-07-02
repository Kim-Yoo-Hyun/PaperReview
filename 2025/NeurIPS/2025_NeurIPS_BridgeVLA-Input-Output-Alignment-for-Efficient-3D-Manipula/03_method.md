# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BridgeVLA-Input-Output-Alignment-for-Efficient-3D-Manipula/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we introduce a new paradigm for constructing 3D VLAs.
- Even when the data are increased to 50 trajectories per task, its success rate is still much lower than BridgeVLA, which indicates only adding 3D information is not ...
- That is, while the objects (e.g., red block and green plate) and skill (e.g., place A in B) are seen during training, the instruction that pairs them together ...

## 원리적 동기
- Another significant challenge in developing 3D VLA models lies in the misalignment between the 3D inputs used in action fine-tuning and the 2D image inputs used in original ...
- To tackle the challenges mentioned above, as inllustrated in Fig.
- In this paper, we introduce a new paradigm for constructing 3D VLAs.

## 핵심 방법론
- Even when the data are increased to 50 trajectories per task, its success rate is still much lower than BridgeVLA, which indicates only adding 3D information is not ...
- That is, while the objects (e.g., red block and green plate) and skill (e.g., place A in B) are seen during training, the instruction that pairs them together ...
- 3) ACT : A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
