# Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Object-X-Learning-to-Reconstruct-Multi-Modal-3D-Object-Rep/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, a critical limitation persists: existing object embeddings are generally learned for specific tasks and cannot be decoded to reconstruct the explicit, high-fidelity appearance and geometry of the ...
- As a consequence, they inherently lack object-level modularity, making it difficult to reason about individual objects, efficiently incorporate other modalities (e.g., text, semantics), or easily use the representation ...
- Traditional 3D representations, often relying on explicit geometry such as dense point clouds (4; 20) or meshes (18), alongside collections of images, tend to incur prohibitive storage and ...

## Core Idea
- The 3RScan dataset (9) consists of 1,335 annotated indoor scenes covering 432 distinct spaces, with 1,178 scenes (385 rooms) used for training and 157 scenes (47 rooms) reserved ...
- In this paper, we propose Object-X, a versatile multi-modal object representation framework capable of encoding rich object embeddings (e.g., images, point cloud, text) and decoding them back into ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Evaluations on two challenging real-world datasets demonstrate that Object-X achieves high-fidelity novel-view synthesis comparable to standard 3D Gaussian Splatting, while significantly improving geometric accuracy.
- Moreover, Object-X achieves competitive performance with specialized methods in scene alignment and localization.
- Next, we will provide experiments on various tasks benefiting from Object-X.

## Limitation
- Despite these advances, Object-X has limitations.
- Furthermore, while promising in zero-shot scenarios for tasks like single-image object reconstruction, performance does not yet consistently match that of optimized task-specific methods.

## Contribution
- Evaluations on two challenging real-world datasets demonstrate that Object-X achieves high-fidelity novel-view synthesis comparable to standard 3D Gaussian Splatting, while significantly improving geometric accuracy.
- In this paper, we propose Object-X, a versatile multi-modal object representation framework capable of encoding rich object embeddings (e.g., images, point cloud, text) and decoding them back into ...
- The learned embedding enables 3D Gaussian Splatting-based object reconstruction, while also supporting a range of downstream tasks, including scene alignment, single-image 3D object reconstruction, and localization.

## Abstract Cue
- Learning effective multi-modal 3D representations of objects is essential for numerous applications, such as augmented reality and robotics.
