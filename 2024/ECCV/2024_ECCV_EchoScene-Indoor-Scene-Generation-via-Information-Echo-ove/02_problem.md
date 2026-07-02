# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Graph Reasoning, Diffusion
- Paper link: ./2024/ECCV/2024_ECCV_EchoScene-Indoor-Scene-Generation-via-Information-Echo-ove/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing methods struggle to handle scene graphs due to varying numbers of nodes, multiple edge combinations, and manipulatorinduced node-edge operations.

## 해결하려는 문제
- Extensive experiments validate our approach, which maintains scene controllability and surpasses previous methods in generation fidelity.
- We present EchoScene, an interactive and controllable generative model that generates 3D indoor scenes on scene graphs.
- This is achieved through an information echo scheme in both shape and layout branches.

## 선행 연구 / 배경 단서
- Controllable Scene Generation (CSG) refers to synthesizing realistic 3D scenes according to input prompts while enabling specific entities within the scene to be user-interactive .
- It has successfully been applied in robotics , Virtual Reality / Augmented Reality , and autonomous driving .
- Recently, combining CSG with scene graph diﬀusion models has attracted significant research interest , since on the one hand, diﬀusion models empower more realistic and diverse 3D content ...
