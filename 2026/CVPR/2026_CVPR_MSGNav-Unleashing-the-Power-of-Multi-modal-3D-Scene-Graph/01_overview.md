# MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Scene Graph, Navigation, zero-shot
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Previous RL-based embodied navigation methods suffer from poor generalization and a large sim-to-real gap [44].를 문제로 두고, Our contributions can be summarized as follows: • M3DSG: We propose a multi-modal 3D scene graph that incorporates visual information, overcoming pure-text limitations and enhancing open-vocabulary scene representation for embodied navi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • M3DSG: We propose a multi-modal 3D scene graph that incorporates visual information, overcoming pure-text limitations and enhancing ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we introduce a visibility-based viewpoint decision module in our MSGNav.
- **p. 2 / 1. Introduction - extractive body cue:** 1, we introduce the Multi-modal 3D Scene Graph (M3DSG), which replaces the pure-text relational edges with dynamically assigned images to incorporate visual cues, and facilitates ...
- **p. 3 / 3.1.2. Overview - extractive body cue:** Unlike traditional 3D scene graph [9] which uses textual relation edges, our method stores images to describe detailed object relations directly.
- **p. 5 / 3.3. MSGNav Embodied Navigation System - extractive body cue:** To fully exploit this, we propose the navigation system MSGNav.
- **p. 7 / 4.2.2. HM3D-ObjNav Benchmark - extractive body cue:** As shown in Table 2, MSGNav achieves a state-of-the-art Success Rate (SR) of 74.1%, which is 1.9% higher than that of the previous best-performing method ...
- **p. 6 / 4.1. Experimental Setting - extractive body cue:** Following standard practice, we assess navigation performance using Success Rate (SR = Nsuccess Ntotal ) and Success weighted by Path Length (SPL = 1 Ntotal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Experiments on the HM3D-ObjNav benchmark. gains 12.5% in SR and 6.7% in SPL (row 3). Notably, in- troducing either AVU (row 4) or ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Previous RL-based embodied navigation methods suffer from poor generalization and a large sim-to-real gap [44].를 문제로 두고, Our contributions can be summarized as follows: • M3DSG: We propose a multi-modal 3D scene graph that incorporates visual information, overcoming pure-text limitations and enhancing open-vocabulary scene representation for embodied navi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (3.1.1. Problem definition), p. 6 (3.3.4. Visibility-based Viewpoint Decision (VVD)), p. 8 (4.3.3. Decision-making for "Last-mile") to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
