# Method

- Year/Venue: 2024 / CVPR
- Category: Benchmarks and Datasets
- Tags: 3D Vision, Embodied AI, dataset
- Paper link: ./2024/CVPR/2024_CVPR_EmbodiedScan-A-Holistic-Multi-Modal-3D-Perception-Suite-To/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We use cross-entropy loss and sceneclass affinity loss for training.
- Given the multi-level sparse visual features FkS and text features from the text encoder, we use a multi-modal fusion transformer model for vision-language information interactions.
- To address the gap, we introduce EmbodiedScan, a multi-modal, ego-centric 3D perception dataset and benchmark for holistic 3D scene understanding.

## 원리적 동기
- Nonetheless, subtle but significant discrepancies exist between this expectation and research problems examined within the computer vision community.
- Most previous studies have primarily revolved around scene-level input and output problems from a global view , i.e., taking reconstructed 3D point clouds or meshes as inputs and ...
- We use cross-entropy loss and sceneclass affinity loss for training.

## 핵심 방법론
- We use cross-entropy loss and sceneclass affinity loss for training.
- Given the multi-level sparse visual features FkS and text features from the text encoder, we use a multi-modal fusion transformer model for vision-language information interactions.
- Training objectives include the original classification loss, centerness loss, and a disentangled Chamfer Distance (CD) loss for eight corners .
- Grounding features F G updated after each transformer layer are fed into the prediction heads sharing the same architecture as those used for 3D detection.
- With the dense feature F D , we use a 3D FPN to aggregate multilevel features and produce multi-scale occupancy predictions.
