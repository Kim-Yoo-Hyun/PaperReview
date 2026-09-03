# Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 tactile 문제를 이해하기 위해 읽는다. 본문은 This limitation presents challenges on two fronts.를 문제로 두고, The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to guide the touch location ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion models have made breakthroughs in 3D generation tasks.
- **p. 1 / Abstract - extractive body cue:** Current 3D diffusion models focus on reconstructing target shape from images or a set of partial observations.
- **p. 1 / Abstract - extractive body cue:** While excelling in global context understanding, they struggle to capture the local details of complex shapes and limited to the occlusion and lighting conditions.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we utilize tactile images to capture the local 3D information and propose a Touch2Shape model, which leverages a touch-conditioned diffusion model ...
- **p. 1 / Abstract - extractive body cue:** For shape reconstruction, we have developed a touch embedding module to condition the diffusion model in creating a compact representation and a touch shape fusion ...
- **p. 2 / 1. Introduction - extractive body cue:** This limitation presents challenges on two fronts.
- **p. 2 / 1. Introduction - extractive body cue:** However, acquiring 3D data presents greater challenges and costs compared to 2D image and text data.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments validate the effectiveness of our method, demonstrating significant improvements in both reconstruction performance and the ability to improve reconstruction quality through touch exploration.
- **p. 4 / 3.2. Touch Shape Fusion - extractive body cue:** The touch shape fusion module is designed with two goals.
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive body cue:** The loss function for diffusion model training is as follows: Ldiff(t, n) = //Eω(zt, r(t), C(T0, ..., Tn→1)) ↓ωt//2, (2) where ωt is the added ...
- **p. 4 / 3.1. Touch-conditioned Diffusion Model - extractive body cue:** The implementation involves extracting feature tokens from images using ResNet [16], combining them with touch tokens through a dropout layer, and then inputting them together ...
- **p. 5 / 3.3. Policy Training - extractive body cue:** We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
- **p. 5 / 3.3. Policy Training - extractive body cue:** At each time step, we input the latent vector z of the target object, add noise through the diffusion model, and then use a touchconditioned ...
- **p. 3 / 3. Method - extractive body cue:** In test stage, we gather tactile images (T0, ..., Tn→1) from the target, utilizing the trained diffusion model to obtain a lowdimensional representation for predicting ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy model receives the denoised vector as input and is trained using reinforcement learning (Section 3.2). | tactile image/force, vision과 proprioceptive history | p. 4 (3. Method), p. 2 (1. Introduction) |
| State/latent | policy, model, receives, denoised, vector, input, trained, reinforcement, learning, Section, employ, simulated | contact geometry, force state 또는 latent dynamics | p. 4 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model) |
| Output/action | In this work, we employ a simulated robotic arm guided by a trained policy model to touch the target, enabling the acquisition of tactile images to reconstruct the target through touch interaction. | grasp/contact action, force command 또는 object motion | p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 2 (1. Introduction) |
| Objective/outcome | For reward function setting, since the final output shape is not predicted, we design it to be the difference in the diffusion model's loss values. | slip/contact success, force/pose error와 robustness | p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the ...
- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments validate the effectiveness of our method, demonstrating significant improvements in both reconstruction performance and the ability to improve reconstruction quality through touch exploration.
- **p. 4 / 3.2. Touch Shape Fusion - extractive body cue:** The touch shape fusion module is designed with two goals.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** The evaluation results in different modes validate that our method can effectively integrate visual and tactile information to achieve a better reconstruction performance.
- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive body cue:** The latter method (we called ActiveVT here) proposes an active touch sensing for 3D reconstruction method to improve the reconstruction performance.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** As shown in Table 4, we add our proposed modules one by one to validate that each sub-module succeeds to improve the performance.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Initially, limited information makes determining the overall global shape challenging, but with more grasp actions, our method effectively improves the reconstruction quality.
- **p. 6 / 4.2. Evaluation on Reconstruction Performance - extractive body cue:** The quantitative results are reported in Table 2.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.4. Ablation Study), p. 6 (4.2. Evaluation on Reconstruction Performance) |
| Embodiment/environment | The dataset is devided into three subsets: 1,100 objects for training, 200 for validation and 350 for testing. | hardware/simulator version and reset protocol | p. 6 (4.2. Evaluation on Reconstruction Performance), p. 5 (4.1. Experimental Settings) |
| Dataset/benchmark | The second dataset employed originates from [7], encompassing 1650 ShapeNet [3] objects that span six categories: bowls, bottles, cameras, jars, guitars, and mugs. | role, split, size and leakage | p. 6 (4.2. Evaluation on Reconstruction Performance), p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Metric | Especially on the visual-tactile 3D reconstruction task, we obtain a very low CD error, which validates the multi-modal fusion ability of our model. | definition, denominator, direction and uncertainty | p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study) |
| Baseline/ablation | Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison as the true optimal policy cannot be ... | fair input/data/compute/action matching | p. 7 (4.3. Evaluation on Policy), p. 7 (4.3. Evaluation on Policy), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Evaluation on Policy - extractive body cue:** Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is viewed as an upper-bound point of comparison ...

## Why Read It

Robotics-enabling 3D perception의 tactile 문제를 이해하기 위해 읽는다. 본문은 This limitation presents challenges on two fronts.를 문제로 두고, The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to guide the touch location ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training), p. 5 (3.3. Policy Training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
