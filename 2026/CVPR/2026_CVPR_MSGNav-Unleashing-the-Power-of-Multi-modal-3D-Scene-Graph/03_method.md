# Method

- Year/Venue: 2026 / CVPR
- Category: Navigation and Embodied AI
- Tags: 3D Scene Graph, Navigation, zero-shot
- Paper link: ./2026/CVPR/2026_CVPR_MSGNav-Unleashing-the-Power-of-Multi-modal-3D-Scene-Graph/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Built on M3DSG, we propose MSGNav, a zero-shot navigation system that includes a Key Subgraph Selection module for efficient reasoning, an Adaptive Vocabulary Update module for open vocabulary ...
- To address these limitations, we introduce the Multi-modal 3D Scene Graph (M3DSG), which preserves visual cues by replacing textual relational edges with dynamically assigned images.
- Real-world deployment requires open vocabulary generalization and low training overhead, motivating zero-shot methods rather than task-specific RL training.

## 원리적 동기
- Additionally, we further identify the “last mile” problem in zero-shot navigation — determining the feasible target location with a suitable final viewpoint, and propose a Visibility-based Viewpoint Decision ...
- However, existing zero-shot methods that build explicit 3D scene graphs often compress rich visual observations into text-only relations, leading to high construction cost, irreversible loss of visual evidence, ...
- Built on M3DSG, we propose MSGNav, a zero-shot navigation system that includes a Key Subgraph Selection module for efficient reasoning, an Adaptive Vocabulary Update module for open vocabulary ...

## 핵심 방법론
- SenseAct-NN Monolitic Modular CLIP on Wheels Modular GOAT SenseAct-NN Skill Chain VLMnav DyNaVLM 3D-Mem† TANGO MTU3D Training-free × ✓ ✓ × ✓ ✓ ✓ ✓ × SR ↑ ...
