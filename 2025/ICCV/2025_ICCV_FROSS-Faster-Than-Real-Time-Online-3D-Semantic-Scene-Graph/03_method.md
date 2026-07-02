# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Vision, Graph Reasoning, semantic
- Paper link: ./2025/ICCV/2025_ICCV_FROSS-Faster-Than-Real-Time-Online-3D-Semantic-Scene-Graph/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this issue, we propose FROSS (Faster-thanReal-Time Online 3D Semantic Scene Graph Generation), an innovative approach for online and faster-than-realtime 3D SSG generation that leverages the direct ...
- We introduce FROSS, an online real-time 3D semantic scene graph generation method that leverages and integrates 2D scene graphs.
- RGB-D heres to the training protocol established in EGTR, which initiates with pre-training the object detector for standard object detection tasks.

## 원리적 동기
- Existing methods for 3D SSG generation, however, face significant challenges, including high computational demands and non-incremental processing that hinder their suitability for real-time open-world applications.
- Real-world applications, however, present open-world challenges where environments often exceed known spatial boundaries and contain previously unseen spaces .
- To address this issue, we propose FROSS (Faster-thanReal-Time Online 3D Semantic Scene Graph Generation), an innovative approach for online and faster-than-realtime 3D SSG generation that leverages the direct ...

## 핵심 방법론
- RGB-D heres to the training protocol established in EGTR, which initiates with pre-training the object detector for standard object detection tasks.
- The superior performance compared to the other image-based methods can be attributed to our Gaussian-based merging strategy.
- For Gaussian merging operations, the Hellinger distance threshold δd is established at 0.85.
