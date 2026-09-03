# PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Diffusion, Robotics, 3D action
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, the number of discretized bins needed to approximate a continuous action space grows exponentially with increasing dimensionality, making it difficult to maintain accuracy and scalability as task complexity increases.를 문제로 두고, In this work, we propose PDFactor, a novel multi-task manipulation agent that leverages a tri-perspective view transformer to learn a hybrid action representation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic manipulation based on visual observations and natural language instructions is a long-standing challenge in robotics.
- **p. 1 / Abstract - extractive body cue:** Yet prevailing approaches model action distribution by adopting explicit or implicit representations, which often struggle to achieve a trade-off between accuracy and efficiency.
- **p. 1 / Abstract - extractive body cue:** In response, we propose PDFactor, a novel framework that models action distribution with a hybrid triplane representation.
- **p. 1 / Abstract - extractive body cue:** In particular, PDFactor decomposes 3D point cloud into three orthogonal feature planes and leverages a tri-perspective view transformer to produce dense cubic features as a ...
- **p. 1 / Abstract - extractive body cue:** We employ a small denoising network conceptually as both a parameterized loss function measuring the quality of the learned latent features and an action gradient ...
- **p. 2 / 1. Introduction - extractive body cue:** However, the number of discretized bins needed to approximate a continuous action space grows exponentially with increasing dimensionality, making it difficult to maintain accuracy and ...
- **p. 2 / 1. Introduction - extractive body cue:** To avoid the computational difficulty of approximating the continuous action distribution, we further propose score matching loss, which leverages the principles of diffusion models to ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose PDFactor, a novel multi-task manipulation agent that leverages a tri-perspective view transformer to learn a hybrid action representation.
- **p. 2 / 1. Introduction - extractive body cue:** To summarise, our work presents the following three contributions: • We formulate a hybrid action representation termed Policy Diffusion Field to ground continuous and multimodal ...
- **p. 3 / 3. Method - extractive body cue:** In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a ...
- **p. 5 / 3.4. Score Matching Loss - extractive body cue:** After obtaining three 2D feature planes, we introduce score matching loss.
- **p. 5 / Model - extractive body cue:** We show detailed model configurations in Tab.
- **p. 5 / 3. We aim to model their joint dis - extractive body cue:** Notably, since our denoising network is small, we can sample t multiple times given latent triplane features \protect \mathbf {T}, which helps model convergence and ...
- **p. 4 / 3.2. Tri-Perspective View Projection - extractive body cue:** Specifically, given a set of multi-view RGB-D images captured by sensor cameras, we first pass images, which consist of 6 channels including RGB and coordinates ...
- **p. 4 / 3. Method - extractive body cue:** Then the triplane tokens are fed into a multi-view transformer along with the instruction and robot proprioception to produce triplane features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a multi-task policy \pi (\ ma thbf {a}/\mathbf ... | RGB-D/point cloud, object state와 contact/task observation | p. 3 (3. Method), p. 2 (1. Introduction) |
| State/latent | particular, given, RGB-D, observations, protect, mathbf, language, instruction, robot, proprioception, goal, learn | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (3. Method), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | Thus the action space is aligned and translationally anchored to the visual features observed from input images, which simplifies the mapping from states to actions and avoids training and inferencing with a ... | grasp, pose, force 또는 end-effector trajectory | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | For the gripper open state and collision state, we simply pass latent vector \protect \mathbf {z} through an MLP to predict a binary label optimized via binary cross entropy loss: &\m a ... | task completion, contact success, pose/force error와 generalization | p. 5 (3. We aim to model their joint dis), p. 3 (3. Method), p. 5 (3.4. Score Matching Loss) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose PDFactor, a novel multi-task manipulation agent that leverages a tri-perspective view transformer to learn a hybrid action representation.
- **p. 2 / 1. Introduction - extractive body cue:** To summarise, our work presents the following three contributions: • We formulate a hybrid action representation termed Policy Diffusion Field to ground continuous and multimodal ...
- **p. 3 / 3. Method - extractive body cue:** In particular, given RGB-D observations \protect \mathbf {o}, language instruction \protect \mathbf {l} and robot proprioception \protect \mathbf {c}, our goal is to learn a ...
- **p. 5 / 3.4. Score Matching Loss - extractive body cue:** After obtaining three 2D feature planes, we introduce score matching loss.
- **p. 5 / Model - extractive body cue:** We show detailed model configurations in Tab.
- **p. 6 / 4.2. Comparison with State-of-the-Art Methods - extractive body cue:** Our method achieves the best performance with an average success rate of 87.3% among all 18 tasks, an absolute improvement of 5.9% over RVT-2, the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous state-of-the-art ...
- **p. 6 / 4.1. Experiment Setup - extractive body cue:** We evaluate policies by task completion success rate, which is the proportion of execution trajectories that achieve the goal conditions specified in the language instructions.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 8 (Figure/Table caption) |
| Embodiment/environment | We collect 15 demonstrations per task and train PDFactor-B with the collected dataset for 10k steps with the same hyperparameters as the simulation data. | hardware/simulator version and reset protocol | p. 8 (4.4. Evaluation in the Real World), p. 6 (4.1. Experiment Setup) |
| Dataset/benchmark | We train and evaluate PDFactor with the same dataset as PerAct, with 100 demonstrations for training and 25 unseen demonstrations for testing. | role, split, size and leakage | p. 8 (4.4. Evaluation in the Real World), p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 8 (4.4. Evaluation in the Real World) |
| Metric | Figure 5. (a) Learning efficiency. We show the learning curves of PDFactor and RVT-2. PDFactor demonstrates faster convergence with a higher performance than previous state-of-the-art RVT-2. (b) & (c) Accuracy and inference ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Study & Model Analysis), p. 6 (4.2. Comparison with State-of-the-Art Methods) |
| Baseline/ablation | For example, in place cups task, the agent is required to have comprehensive spatial understanding and long-horizon reasoning abilities to hang mugs on the cup holder, where our method achieves a sizable ... | fair input/data/compute/action matching | p. 6 (4.2. Comparison with State-of-the-Art Methods), p. 6 (4.3. Ablation Study & Model Analysis), p. 8 (4.3. Ablation Study & Model Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future works could explore recent techniques on reducing diffusive sampling steps while maintaining optimal accuracy.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Policy Representations. (a) Explicit policy predicts a specific action distribution along the 3D space. (b) Implicit pol- icy, e.g., energy-based and diffusion-based models, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. PDFactor Overview. The 3D point cloud reconstructed from the multi-view RGB-D images is first featurized and projected to three orthogonal views, which are ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. A subset of the evaluated 18 tasks in RLBench simulation and 6 tasks in the real world. where \ d elta \sim \mathcal ...
- **p. 7 / 4.3. Ablation Study & Model Analysis - extractive body cue:** We observe that the average success rate drops by 9%, indicating the importance of feature projection to avoid visual occlusions.
- **p. 8 / 4.3. Ablation Study & Model Analysis - extractive body cue:** Variants Planning Tools Long Rotation Motion Multimodal Precision Occlusion Avg.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, the number of discretized bins needed to approximate a continuous action space grows exponentially with increasing dimensionality, making it difficult to maintain accuracy and scalability as task complexity increases.를 문제로 두고, In this work, we propose PDFactor, a novel multi-task manipulation agent that leverages a tri-perspective view transformer to learn a hybrid action representation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Method), p. 5 (3. We aim to model their joint dis) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
