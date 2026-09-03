# SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=U5nRMOs8Ed.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167962. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Diffusion, Imitation Learning, equivariant
- Official paper: https://openreview.net/forum?id=U5nRMOs8Ed
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/167962
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements of the scene.를 문제로 두고, The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling generalization to unseen scenes, 2. a novel ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion Policies are effective at learning closed-loop manipulation policies from human demonstrations but generalize poorly to novel arrangements of objects in 3D space, hurting real-world ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene.
- **p. 1 / Abstract - extractive body cue:** Such equivariance is achieved by embedding the states, actions, and the denoising process in spherical Fourier space.
- **p. 1 / Abstract - extractive body cue:** Additionally, we employ novel spherical FiLM layers to condition the action denoising process equivariantly on the scene embeddings.
- **p. 1 / Abstract - extractive body cue:** Lastly, we propose a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.
- **p. 1 / 1. Introduction - extractive body cue:** Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements ...
- **p. 2 / 1. Introduction - extractive body cue:** The equivariance constraints lead to provable SE(3) generalization to transformed scenes.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method is light and SE(3) equivariant across multiple objects, allowing it to perform more complicated tasks with less engineering.
- **p. 4 / 4.1. Method Overview - extractive body cue:** Additionally, we propose bi-manual relative action representation.
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.
- **p. 4 / 4.1. Method Overview - extractive body cue:** We model ϵθ using three components as shown in Figure 2: i) the spherical encoder embeds the state into a multichannel spherical scene feature enc(S) ...
- **p. 5 / 4.4. Spherical FiLM Conditioning Layer - extractive body cue:** We propose equivariant spherical FiLM (SFiLM) layers to extend the Feature-wise Linear Modulation (FiLM) layer (Perez et al., 2018) used by Diffuser (Janner et al., ...
- **p. 5 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** The robot state e is concatenated to the output of the encoder yielding C.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this section, we propose a spherical representation of the state and action for the policy. | image/video, language instruction, proprioception과 history | p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview) |
| State/latent | section, spherical, representation, state, action, policy, Diffusion, model, maps, observations, actions, states | language-grounded task state와 action-policy context | p. 4 (4.2. Representing State and Action by Spherical Signal), p. 4 (4.1. Method Overview), p. 2 (2. Background) |
| Output/action | The Spherical Diffusion Policy model maps observations to actions π(S) = A. | continuous action, pose 또는 action chunk | p. 4 (4.1. Method Overview), p. 2 (2. Background), p. 2 (2. Background) |
| Objective/outcome | The mixing channel temporal convolution in Equation. | instruction following, task success, generalization과 latency | p. 5 (4.3. Spherical Denoising Temporal U-net), p. 4 (4.2. Representing State and Action by Spherical Signal) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose Spherical Diffusion Policy (SDP), a Fourier space SE(3) equivariant method that automatically adapts to changes in the scene.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, our method is light and SE(3) equivariant across multiple objects, allowing it to perform more complicated tasks with less engineering.
- **p. 4 / 4.1. Method Overview - extractive body cue:** Additionally, we propose bi-manual relative action representation.
- **p. 4 / 4.2. Representing State and Action by Spherical Signal - extractive body cue:** In this section, we propose a spherical representation of the state and action for the policy.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** Notably, as the tilting range increases, SDP achieves a more significant relative performance improvement over the baselines.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6. Impact of training dataset size on task success rates: in- creasing the number of demonstrations from 100 to 316 (a 3× increase) yields ...
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.1. Simulation Experiments), p. 9 (Figure/Table caption) |
| Embodiment/environment | To evaluate robustness, we modify four MimicGen tasks with SE(3) initialization by randomly tilting the table within a defined range and randomly placing objects on the tabletop while keeping the robot base ... | hardware/simulator version and reset protocol | p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments) |
| Dataset/benchmark | Experimental Settings We conduct simulation experiments using the MimicGen (Mandlekar et al., 2023) environment, built on the Mujoco simulator (Todorov et al., 2012), which features diverse tasks that are contact-rich, precise, and ... | role, split, size and leakage | p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments) |
| Metric | We report the maximum test success rate throughout training, averaging results over 50 rollouts for each of the three seeds. | definition, denominator, direction and uncertainty | p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments), p. 8 (5.2. Physical Experiments) |
| Baseline/ablation | Results on Tasks with SE(2) Initialization Table 2 shows that SDP outperforms all baselines across 10 tasks, except for Coffee and Coffee Preparation. | fair input/data/compute/action matching | p. 6 (5.1. Simulation Experiments), p. 6 (5.1. Simulation Experiments), p. 7 (5.2. Physical Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** One limitation of the proposed method is that it operates in position control, ignoring contact forces, which leads to protective stops in the Flip Book ...
- **p. 9 / 6. Conclusion and Limitations - extractive body cue:** Another limitation is the lowresolution point cloud processing in the observation encoder, which struggles to capture fine details, such as these in the Push Eraser ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method overview. During inference, SDP first embeds state St into a spherical scene feature Ct by the encoder enc. Then, SDTU ϵθ estimates ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Spherical denoising temporal U-net (SDTU). Left: The SDTU ϵθ estimates the noise ϵ, based on the noisy actions Ak t , denoising step ...
- **p. 6 / 5.2. Physical Experiments - extractive body cue:** The observations are captured by two stationary RGBD cameras positioned above the workspace to minimize occlusion.
- **p. 6 / 5.1. Simulation Experiments - extractive body cue:** We hypothesize that this drop is caused by pointcloud occlusion and object instability due to gravity, both of which disrupt SE(3) equivariance.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Diffusion Policy may struggle to attain robust 3D generalization without training on a large amount of costly human demonstrations to exhaust the possible 3D arrangements of the scene.를 문제로 두고, The contributions of this work are: 1. a novel method, Spherical Diffusion Policy, which is equivariant to 3D rotations and invariant to 3D translations enabling generalization to unseen scenes, 2. a novel ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4.1. Method Overview), p. 4 (4.2. Representing State and Action by Spherical Signal), p. 5 (4.4. Spherical FiLM Conditioning Layer) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
