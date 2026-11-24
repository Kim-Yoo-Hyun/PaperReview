# DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Kaizhao Zhang, Tian Niu, Tianyu Liu, Chenen Guo, Zijun Xu, Qingda Hu, Wenchao Ding
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Diffusion, 3D manipulation, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

DiffuView는 한 시점에서 다른 시점의 영상을 합성하는 확산 사전학습으로 로봇 모방 정책에 쓸 시각 표현을 얻는다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation from visual observations remains challenging due to the lack of 3D consistent representations that can generalize across diverse viewpoints and sensor configurations.
- **p. 1 / Abstract - extractive body cue:** Existing methods, primarily based on masked autoencoders or neural scene representations, struggle to capture robust view correspondences due to a lack of global 3D consistency ...
- **p. 1 / Abstract - extractive body cue:** Crucially, while multi-view diffusion models have recently shown tremendous success in 3D aware generative synthesis, their powerful representations offer a promising direction for achieving viewpoint ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce DiffuView, a novel framework that learns unified 3D aware representations through multi-view diffusion pretraining and deploys them for imitation learning.
- **p. 1 / Abstract - extractive body cue:** Specifically, DiffuView models the conditional generation of target views given source observations within a diffusion framework, enabling the network to implicitly recover scene geometry and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most of these approaches rely solely on 2D imagery, lacking awareness of This CVPR paper is the Open Access version, provided by the Computer ...
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this data bottleneck, recent studies have turned to leveraging advances in computer vision, particularly selfsupervised and large-scale visual pretraining, to obtain transferable representations ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We propose DiffuView, a novel diffusion-based representation learning framework for robotic manipulation that learns 3D consistent visual ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method consists of two stages, as illustrated in Fig.
- **p. 1 / 1. Introduction - extractive body cue:** (c) Our method leverages a multi view diffusion model that learns 3D consistent and geometry aware representations by generating novel target views conditioned on source ...
- **p. 4 / 3. Method - extractive body cue:** In this section, we present our two stage framework for learning 3D consistent visuomotor in details.
- **p. 5 / 3.2. Policy Learning - extractive body cue:** In addition, we introduce an action causal self-attention mechanism to model temporal dependencies among consecutive action tokens.
- **p. 4 / 3.2. Policy Learning - extractive body cue:** Thanks to our flexible view inference design, the pretrained model can serve two complementary roles during downstream learning: (i) as a feature extractor for action ...
- **p. 5 / 3.2. Policy Learning - extractive body cue:** = \ma th bb {E }_{( \math bf {a}_0,\mathbf {z}_{\text {obs}},\mathbf {l}),\,t,\,\boldsymbol {\varepsilon }} \Big [ \big \/ \boldsymbol {\varepsilon } - \boldsymbol {\varepsilon }_{\psi ...
- **p. 4 / 3. Method - extractive body cue:** 2, DiffuView first pretrains a multi-view diffusion model to infer geometric correspondences across different camera views, enabling the encoder to capture cross view aligned representations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | After the FiLM conditioned QFormer aggregates the visual features into a compact observation embedding zobs, a diffusion policy is employed as the action head to generate the robot action a0 conditioned on ... | RGB-D/point cloud, object state와 contact/task observation | p. 4 (3.2. Policy Learning), p. 5 (3.2. Policy Learning) |
| State/latent | After, FiLM, conditioned, QFormer, aggregates, visual, features, compact, observation, embedding, zobs, diffusion | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning) |
| Output/action | At each timestep t, the policy network εψ learns to predict the noise component based on the noisy action a(t), the timestep t, the observation embedding zobs, and the language token l: ... | grasp, pose, force 또는 end-effector trajectory | p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning), p. 4 (3. Method) |
| Objective/outcome | Unlike vanilla self-attention, causal masking enforces an autoregressive constraint such that each action token can only attend to its preceding tokens. | task completion, contact success, pose/force error와 generalization | p. 5 (3.2. Policy Learning), p. 5 (3.2. Policy Learning) |

## Main Claims and Actual Contribution

- 목표 시점 생성에 쓰인 확산 네트워크의 특징을 행동 정책에 전달해 시점 사이 대응이 제어 학습에 반영되게 한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=4)
- LIBERO와 실물 조작에서 관측 시점을 바꿔 정책을 평가하고 사전학습 표현에 따른 차이를 측정했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.4. Real World Experiments), p. 7 (4.3. View Generalization Experiments) |
| Embodiment/environment | To enable our pretraining model to generalize effectively to the visual and geometric characteristics of robotic manipulation scenes, we construct a pretraining dataset composed of diverse multi view observations tailored to manipulatio ... | hardware/simulator version and reset protocol | p. 5 (4.1. Pretraining Setups), p. 5 (4.1. Pretraining Setups) |
| Dataset/benchmark | We collect 50 trajectories for each task in the Meta-World benchmark as our training dataset. | role, split, size and leakage | p. 5 (4.1. Pretraining Setups), p. 5 (4.1. Pretraining Setups), p. 6 (4.2. Simulation Experiments), p. 7 (4.4. Real World Experiments) |
| Metric | Ablation Types Success Rate DiffuView 89.2 DiffuView w/o Robotics Data Pretraining 63.3 DiffuView w/o Pl¨ucker Embedding 76.2 DiffuView w/o FiLM Conditioning in Q-Former 73.3 DiffuView Noise Conditioned Activated Experts Top K = ... | definition, denominator, direction and uncertainty | p. 7 (4.4. Real World Experiments), p. 7 (4.3. View Generalization Experiments), p. 8 (4.5. Ablation Studies) |
| Baseline/ablation | 3, the pretrained module enables the policy to maintain stable manipulation performance under large viewpoint shifts, whereas the baseline 23606 | fair input/data/compute/action matching | p. 6 (4.3. View Generalization Experiments), p. 7 (4.4. Real World Experiments), p. 6 (4.2. Simulation Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** In future work, we plan to extend DiffuView toward a joint flexible view and time pretraining framework, enabling unified spatial temporal representation learning.
- **p. 8 / 5. Conclusion and Limitation - extractive body cue:** Furthermore, we evaluated the viewpoint generalization metrics on proposed MV-bench, confirming that our work can robustly handle large viewpoint shifts.
- **p. 7 / 4.3. View Generalization Experiments - extractive body cue:** However, when the viewpoint shift becomes excessively large, spatial geometric occlusions occur, leading to a noticeable degradation in the performance of the pretrained model.
- **p. 7 / 4.4. Real World Experiments - extractive body cue:** Ablation Types Success Rate DiffuView 89.2 DiffuView w/o Robotics Data Pretraining 63.3 DiffuView w/o Pl¨ucker Embedding 76.2 DiffuView w/o FiLM Conditioning in Q-Former 73.3 DiffuView ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (Left) Stage 1: Multi-view diffusion pretraining reconstructs target views from source observations using Pl¨ucker rays, depth, and warped RGB depth pairs to learn ...
- **p. 6 / 4.2. Simulation Experiments - extractive body cue:** For the noise-level conditioning module, we employ a MoE design within each transformer Table 3.
- **p. 6 / 4.3. View Generalization Experiments - extractive body cue:** Following [59], we also render multi-view data in the LIBERO Spatial environment to evaluate the robustness of our method under viewpoint variations.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Policy Learning), p. 5 (3.2. Policy Learning)이다.
