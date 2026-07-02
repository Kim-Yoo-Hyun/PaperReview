# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Object-X-Learning-to-Reconstruct-Multi-Modal-3D-Object-Rep/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The 3RScan dataset (9) consists of 1,335 annotated indoor scenes covering 432 distinct spaces, with 1,178 scenes (385 rooms) used for training and 157 scenes (47 rooms) reserved ...
- In this paper, we propose Object-X, a versatile multi-modal object representation framework capable of encoding rich object embeddings (e.g., images, point cloud, text) and decoding them back into ...
- We use 77 test scenes from the split defined in (15).

## 원리적 동기
- However, a critical limitation persists: existing object embeddings are generally learned for specific tasks and cannot be decoded to reconstruct the explicit, high-fidelity appearance and geometry of the ...
- As a consequence, they inherently lack object-level modularity, making it difficult to reason about individual objects, efficiently incorporate other modalities (e.g., text, semantics), or easily use the representation ...
- The 3RScan dataset (9) consists of 1,335 annotated indoor scenes covering 432 distinct spaces, with 1,178 scenes (385 rooms) used for training and 157 scenes (47 rooms) reserved ...

## 핵심 방법론
- The 3RScan dataset (9) consists of 1,335 annotated indoor scenes covering 432 distinct spaces, with 1,178 scenes (385 rooms) used for training and 157 scenes (47 rooms) reserved ...
- We use 77 test scenes from the split defined in (15).
- First, we evaluate the Object-X decoder in terms of storage efficiency, geometric fidelity, and visual quality on the object reconstruction task.
- 3DGS (11) serves as a high-fidelity baseline, representing each object as a set of 3D Gaussians.
