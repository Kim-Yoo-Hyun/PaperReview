# Method

- Year/Venue: 2019 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, semantic, geometry, Graph Reasoning
- Paper link: ./2019/ICCV/2019_ICCV_3D-Scene-Graph-A-Structure-for-Unified-Semantics-3D-Space/paper.pdf
- Code/Project: https://3dscenegraph.stanford.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.

## 원리적 동기
- obj1 obj1 obj2 (0.8, 0.3, - 0.1) obj2 0.85 obj2 class: bed color: blue, brown material: wood, fabric area: 2.2 m2 shape: prism rectangular action affordance: sit on, ...
- Introduction B1 Where should semantic information be grounded and what structure should it have to be most useful and invariant?
- 3D Scene Graph: It consists of 4 layers, that represent semantics, 3D space and camera.

## 핵심 방법론
- Mask R-CNN 0.079 0.166 0.070 0.151 AP AP.50 AP.75 AR 2D Ours Mask R-CNN w/ Framing 0.160 (+0.081) 0.316 (+0.150) 0.147 (+0.077) 0.256 (+0.105) Ours Mask R-CNN w/ ...
- Mask R-CNN with framing and multi-view consistency (d) further removed the painted vase and bed reflection, achieving results very close to the ground truth.
- Similar improvements can be seen in the case of 3D (Figure 7).
- Even though they might not appear as large quantitatively, they are crucial for getting consistent 3D results with most changes relating to consistent local regions and better object ...
- Human Labor: We perform a user study to associate detection performance with human labor (hours spent).
