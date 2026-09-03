# GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Gaussian Splatting, world model, Robotics
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, since these methods primarily rely on offline per-scene reconstruction, their computational demands pose significant challenges [49, 91] on applying them in robotic manipulation, especially for Model-based Reinforcement Learnin ...를 문제로 두고, In summary, our main contributions are threefold. • We introduce GWM, a novel 3D world model that is instantiated with a Gaussian diffusion transformer and a Gaussian VAE for efficient dynamic modeling.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Training robot policies within a learned world model is trending due to the inefficiency of real-world interactions.
- **p. 1 / Abstract - extractive body cue:** The established image-based world models and policies have shown prior success, but lack robust geometric information that requires consistent spatial and physical understanding of the ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by ...
- **p. 1 / Abstract - extractive body cue:** At its core is a latent Diffusion Transformer (DiT) combined with a 3D variational autoencoder, enabling fine-grained scenelevel future state reconstruction with Gaussian Splatting.
- **p. 1 / Abstract - extractive body cue:** GWM can not only enhance the visual representation for imitation learning agent by self-supervised future prediction training, but can serve as a neural simulator that ...
- **p. 2 / 1. Introduction - extractive body cue:** However, since these methods primarily rely on offline per-scene reconstruction, their computational demands pose significant challenges [49, 91] on applying them in robotic manipulation, especially ...
- **p. 2 / 1. Introduction - extractive body cue:** However, their reliance on image inputs makes them susceptible to unseen visual variations (e.g., lighting, camera pose, textures, etc.) [40], as they lack 3D geometric ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are threefold. • We introduce GWM, a novel 3D world model that is instantiated with a Gaussian diffusion transformer and ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose Gaussian World Model (GWM), a novel 3D world model that integrates 3D-GS with high-capacity generative models for robotic manipulation.
- **p. 4 / 3.1. World State Encoding - extractive body cue:** The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer.
- **p. 5 / 2. Does Gaussian world model benefits downstream imita - extractive body cue:** Specifically, we leverage the following three testing environments and four tasks in our experiments: Environments To provide a comprehensive analysis of GWM's capability, we evaluate ...
- **p. 6 / 4.1. Action-conditioned Scene Prediction - extractive body cue:** Results and Analyses We provide quantitative comparison between our method and iVideoGPT in Tab.
- **p. 4 / 3.1. World State Encoding - extractive body cue:** The 3D variational encoder embeds the Gaussian Splats estimated by a foundational reconstruction model to a compact latent space, and the diffusion transformer operates on ...
- **p. 5 / 3.3. GWM for Policy Learning - extractive body cue:** Specifically, we use the feature vector after the first denoising step in the diffusion process as the input for downstream policy models like BCtransformer [59] ...
- **p. 3 / 3.1. World State Encoding - extractive body cue:** Next, we use these sampled Gaussians GN as queries to attend and aggregate information from all Gaussians G to latent embedding x using a L ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Feed-forward 3D Gaussian Splatting Given single or two-view image inputs I = {I}i={1,2} of a world state, our goal is to first encode the scene into 3D Gaussian representations for dynamics learning ... | image/video, language instruction, proprioception과 history | p. 3 (3.1. World State Encoding), p. 3 (3.1. World State Encoding) |
| State/latent | Feed-forward, Gaussian, Splatting, Given, single, two-view, image, inputs, world, state, goal, first | language-grounded task state와 action-policy context | p. 3 (3.1. World State Encoding), p. 3 (3.1. World State Encoding), p. 6 (4.2. GWM-based Imitation Learning) |
| Output/action | Specifically, we obtain the 3D Gaussian world state G using Splatt3R [70], which first employs the stereo reconstruction model Mast3R [37] to generate 3D point maps from input images and then predicts ... | continuous action, pose 또는 action chunk | p. 3 (3.1. World State Encoding), p. 6 (4.2. GWM-based Imitation Learning), p. 2 (1. Introduction) |
| Objective/outcome | The goal of model-based RL [31] is to learn a policy π that maximizes the expected sum of discounted rewards π∗ = arg maxπ Eπ [P∞ t=0 γtrt] while constructing a model ... | instruction following, task success, generalization과 latency | p. 5 (3.3. GWM for Policy Learning), p. 4 (3.2. Diffusion-based Dynamics Modeling), p. 5 (3.2. Diffusion-based Dynamics Modeling) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are threefold. • We introduce GWM, a novel 3D world model that is instantiated with a Gaussian diffusion transformer and ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose Gaussian World Model (GWM), a novel 3D world model that integrates 3D-GS with high-capacity generative models for robotic manipulation.
- **p. 4 / 3.1. World State Encoding - extractive body cue:** The overall pipeline of GWM, which primarily consists of a 3D variational encoder and a latent diffusion transformer.
- **p. 5 / 2. Does Gaussian world model benefits downstream imita - extractive body cue:** Specifically, we leverage the following three testing environments and four tasks in our experiments: Environments To provide a comprehensive analysis of GWM's capability, we evaluate ...
- **p. 6 / 4.1. Action-conditioned Scene Prediction - extractive body cue:** Results and Analyses We provide quantitative comparison between our method and iVideoGPT in Tab.
- **p. 8 / 4.5. Ablation Analysis - extractive body cue:** Choice of Gaussian Splatting As shown in Table 4, compared to directly building image-based world model with diffusion transformer on par with [1], introducing Gaussian ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations per ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. Each ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4.5. Ablation Analysis), p. 7 (Figure/Table caption) |
| Embodiment/environment | This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches. | hardware/simulator version and reset protocol | p. 8 (4.5. Ablation Analysis), p. 8 (4.5. Ablation Analysis) |
| Dataset/benchmark | This validates our hypothesis that explicit 3D representation enhances spatial understanding for robot learning compared to pure 2D approaches. | role, split, size and leakage | p. 8 (4.5. Ablation Analysis), p. 8 (4.5. Ablation Analysis) |
| Metric | Table 2. Multi-Task Imitation Learning Results in Robocasa. Average success rates (%) of multi-task agents trained with 50 human demonstrations or 3000 generated demonstrations per task. Results are evaluated over 50 episodes ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (4.5. Ablation Analysis), p. 6 (Figure/Table caption) |
| Baseline/ablation | Figure 5. Model-based RL Results of GWM and ivideogpt [82] on METAWORLD. The shadow area represents 95% confidence interval (CI) across three random seeds. Each data point is evaluated over 20 episodes. ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (4.5. Ablation Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In this paper, we introduce a novel Gaussian World Model (GWM) for robotic manipulation that addresses limitations of image-based world models by incorporating robust geometric ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Gaussian World Model (GWM) is a novel branch of world model that predicts dynamic future states and enables robotic manipulation based on the ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, since these methods primarily rely on offline per-scene reconstruction, their computational demands pose significant challenges [49, 91] on applying them in robotic manipulation, especially for Model-based Reinforcement Learnin ...를 문제로 두고, In summary, our main contributions are threefold. • We introduce GWM, a novel 3D world model that is instantiated with a Gaussian diffusion transformer and a Gaussian VAE for efficient dynamic modeling.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. World State Encoding), p. 5 (3.3. GWM for Policy Learning), p. 3 (3.1. World State Encoding), p. 4 (3.1. World State Encoding) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
