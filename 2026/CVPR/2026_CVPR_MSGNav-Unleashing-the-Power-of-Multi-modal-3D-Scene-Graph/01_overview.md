# MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Xun Huang, Shijia Zhao, Yunxiang Wang, Xin Lu, Wanfa Zhang, Rongsheng Qu, Weixin Li, Yunhong Wang, Chenglu Wen
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Scene Graph, Navigation, zero-shot
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

MSGNav는 탐색하며 본 RGB-D 영상으로 물체 사이 관계를 보존하는 3차원 장면 그래프를 만들고 목표를 관측할 위치를 고른다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Embodied navigation is a fundamental capability for robotic agents operating.
- **p. 1 / Abstract - extractive body cue:** Real-world deployment requires open vocabulary generalization and low training overhead, motivating zero-shot methods rather than task-specific RL training.
- **p. 1 / Abstract - extractive body cue:** However, existing zero-shot methods that build explicit 3D scene graphs often compress rich visual observations into text-only relations, leading to high construction cost, irreversible loss ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce the Multi-modal 3D Scene Graph (M3DSG), which preserves visual cues by replacing textual relational edges with dynamically assigned images.
- **p. 1 / Abstract - extractive body cue:** Built on M3DSG, we propose MSGNav, a zero-shot navigation system that includes a Key Subgraph Selection module for efficient reasoning, an Adaptive Vocabulary Update module ...
- **p. 2 / 1. Introduction - extractive body cue:** Previous RL-based embodied navigation methods suffer from poor generalization and a large sim-to-real gap [44].
- **p. 2 / 1. Introduction - extractive body cue:** Novel categories beyond a preset vocabulary cannot be represented, limiting generalization in 3D scene graph-based methods.

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • M3DSG: We propose a multi-modal 3D scene graph that incorporates visual information, overcoming pure-text limitations and enhancing ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we introduce a visibility-based viewpoint decision module in our MSGNav.
- **p. 2 / 1. Introduction - extractive body cue:** 1, we introduce the Multi-modal 3D Scene Graph (M3DSG), which replaces the pure-text relational edges with dynamically assigned images to incorporate visual cues, and facilitates ...
- **p. 3 / 3.1.2. Overview - extractive body cue:** Unlike traditional 3D scene graph [9] which uses textual relation edges, our method stores images to describe detailed object relations directly.
- **p. 5 / 3.3. MSGNav Embodied Navigation System - extractive body cue:** To fully exploit this, we propose the navigation system MSGNav.
- **p. 6 / 3.3.4. Visibility-based Viewpoint Decision (VVD) - extractive body cue:** To achieve this goal, we propose a Visibility-based Viewpoint Decision (VVD) module (in Algorithm 2).
- **p. 8 / 4.3.3. Decision-making for "Last-mile" - extractive body cue:** The first row without any module, which represents our baseline model 3D-Mem [43] results. "VVD", "AVU", and "CRV" represent the Visibility-based Viewpoint Decision module, Adaptive ...
- **p. 6 / 3.3.3. Closed-Loop Reasoning (CLR) - extractive body cue:** In addition to modeling the scene as perception memory, we introduce the decision memory M for closed-loop reasoning.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each time step t, it obtains an RGB-D observation It and executes an action At (camera rotation or ego-motion) to actively explore until locating the target. | camera/depth stream, pose, map와 language goal | p. 3 (3.1.1. Problem definition), p. 4 (3.1.2. Overview) |
| State/latent | time, step, obtains, RGB-D, observation, executes, action, camera, rotation, ego-motion, actively, explore | robot pose, free-space/semantic map와 local goal | p. 3 (3.1.1. Problem definition), p. 4 (3.1.2. Overview), p. 4 (3.1.2. Overview) |
| Output/action | At time step t, the agent incrementally constructs the scene graph St based on received observation It and its own pose. | collision-free trajectory 또는 velocity command | p. 4 (3.1.2. Overview), p. 4 (3.1.2. Overview), p. 7 (4.3.2. Advantage of M3DSG) |
| Objective/outcome | (4) This edge update process is efficient, eliminating the need for costly VLM queries. | goal reach, safety, localization error와 replanning latency | p. 4 (3.2.2. Incremental Construction of M3DSG), p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 3 (3.1.2. Overview) |

## Main Claims and Actual Contribution

- 물체 쌍을 함께 관측한 영상을 그래프 간선에 저장하고 관련 부분 그래프의 추론 및 가시성 평가로 마지막 접근 시점을 선택한다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=6)
- GOAT-Bench와 HM3D-ObjNav에서 성공률과 경로 효율을 측정하고 그래프 처리 및 최종 시점 선택의 효과를 비교했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 6 (4.1. Experimental Setting) |
| Embodiment/environment | We evaluate our proposed approach on two established goal-oriented navigation benchmarks: 1) GOAT-Bench [19] (Multi-modal lifelong open-vocabulary dataset, 360 episodes, 36 scenes, 2669 total subtasks, 36 novel goal categories). | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting) |
| Dataset/benchmark | These results highlight the effectiveness of our multi-modal scene graph in tackling multi-modal lifelong navigation tasks. | role, split, size and leakage | p. 6 (4.1. Experimental Setting), p. 6 (4.1. Experimental Setting), p. 7 (4.2.1. Goat-Bench Benchmark), p. 7 (4.2.1. Goat-Bench Benchmark) |
| Metric | Following standard practice, we assess navigation performance using Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 Ntotal PNtotal i=1 Si ls i max(ls i ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setting), p. 8 (Figure/Table caption), p. 7 (4.2.2. HM3D-ObjNav Benchmark) |
| Baseline/ablation | As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing method WMNav [31], and significantly outperforms other prior ... | fair input/data/compute/action matching | p. 7 (4.2.2. HM3D-ObjNav Benchmark), p. 8 (Figure/Table caption), p. 7 (4.2.1. Goat-Bench Benchmark) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Statistical box plot of candidate viewpoint scores com- puted by the VVD module and distances from GT viewpoints. representations in embodied navigation. Limitations ...
- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we propose the MSGNav, a zero-shot embodied navigation framework built upon a Multi-modal 3D Scene Graph (M3DSG) that preserves visual information for ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Demonstration of the "last-mile" problem. (a) Previ- ous methods select the nearest traversable position after target lo- calization, and often fail due to ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (3.1.1. Problem definition), p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 8 (4.3.3. Decision-making for "Last-mile")이다.
