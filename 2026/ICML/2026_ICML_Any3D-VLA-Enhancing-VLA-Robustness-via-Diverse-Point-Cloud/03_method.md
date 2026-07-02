# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- A NY 3D-VLA We propose A NY 3D-VLA, which adopts a point cloud–2D patch fusion approach (inspired by §4) along with a hybrid point cloud training strategy.
- depth-scale biases, we propose A NY 3D-VLA.
- We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions.

## 원리적 동기
- To address the challenges of (1) scarce 3D data and (2) the domain gap induced by cross-environment differences and 1.
- Existing Vision-Language-Action (VLA) models typically take 2D images as visual input, which limits their spatial understanding in complex scenes.
- A NY 3D-VLA We propose A NY 3D-VLA, which adopts a point cloud–2D patch fusion approach (inspired by §4) along with a hybrid point cloud training strategy.

## 핵심 방법론
- A NY 3D-VLA We propose A NY 3D-VLA, which adopts a point cloud–2D patch fusion approach (inspired by §4) along with a hybrid point cloud training strategy.
- We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions.
- Overall Architecture A NY 3D-VLA integrates a Vision-Language Model (VLM) with an action expert (Black et al., 2025b), and connects them via a Progressive Action Generation (PAG) mechanism ...
- To avoid the computational cost of feeding all points directly into the encoder, we perform in (x, y, z) space the same grid sampling as Sonata (Wu et ...
- The potential reason for this is that implicit methods (such as VGGT or depth-pretrained encoders) rely on reconstruction objectives to learn spatial features; consequently, they often lack precise ...
