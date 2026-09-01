# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2303.04137.
> PDF retrieval source: https://arxiv.org/pdf/2303.04137. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: Diffusion, Imitation Learning, Robotics
- Official paper: https://arxiv.org/abs/2303.04137
- Full-text retrieval: https://arxiv.org/pdf/2303.04137
- Code/Project: https://github.com/real-stanford/diffusion_policy
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 (2022) fails to commit to a single mode due to its lack of temporal action consistency.를 문제로 두고, To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: • Closed-loop ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process.
- **p. 1 / Abstract - extractive body cue:** We benchmark Diffusion Policy across 15 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods ...
- **p. 1 / Abstract - extractive body cue:** Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of ...
- **p. 1 / Abstract - extractive body cue:** We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action ...
- **p. 1 / Abstract - extractive body cue:** To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including ...
- **p. 5 / 1 Introduction - extractive body cue:** (2022) fails to commit to a single mode due to its lack of temporal action consistency.
- **p. 1 / 1 Introduction - extractive body cue:** Prior work attempts to address this challenge by exploring different action representations (Fig 1 a) - using mixtures of Gaussians Mandlekar et al.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its ...
- **p. 4 / 1 Introduction - extractive body cue:** (2020), we introduce a novel transformer-based DDPM which adopts the transformer architecture from minGPT Shafiullah et al.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a visionconditioned diffusion policy, where the visual observations are treated as conditioning instead of a part of the joint data distribution.
- **p. 4 / 1 Introduction - extractive body cue:** Third, we removed inpainting-based goal state conditioning due to incompatibility with our framework utilizing a receding prediction horizon.
- **p. 1 / 1 Introduction - extractive body cue:** This formulation allows robot policies to inherit several key properties from diffusion models - significantly improving performance. • Expressing multimodal action distributions.
- **p. 16 / A.4 Hyperparameters - extractive body cue:** On simulation benchmarks, we used the iDDPM algorithm Nichol and Dhariwal (2021) with the same 100 denoising diffusion iterations for both training and inference.
- **p. 16 / A.4 Hyperparameters - extractive body cue:** For CNN-based Diffusion Policy, We found using FiLM conditioning to pass-in observations is better than impainting on all tasks 1 2 3 4 5 6 ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Diffusion Policy 3 b) CNN-based c) Transformer-based Conv1D Conv1D Conv1D Conv1D Conv1D Input: Image Observation Sequence Output: Action Sequence … Cross Attention Cross Attention ×K Obs Emb Action Emb Action Emb A ... | observation history와 expert trajectory/action | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | Diffusion, Policy, CNN-based, Transformer-based, Conv1D, Input, Image, Observation, Sequence, Output, Action, Cross | behavior policy와 temporal action context | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | At time step t, the policy takes the latest To steps of observation data Ot as input and outputs Ta steps of actions At. b) In the CNN-based Diffusion Policy, FiLM (Feature-wise ... | predicted action 또는 action chunk | p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | imitation error, task success, robustness와 compounding error | imitation error, task success, robustness와 compounding error | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its ...
- **p. 4 / 1 Introduction - extractive body cue:** (2020), we introduce a novel transformer-based DDPM which adopts the transformer architecture from minGPT Shafiullah et al.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a visionconditioned diffusion policy, where the visual observations are treated as conditioning instead of a part of the joint data distribution.
- **p. 4 / 1 Introduction - extractive body cue:** Third, we removed inpainting-based goal state conditioning due to incompatibility with our framework utilizing a receding prediction horizon.
- **p. 1 / 1 Introduction - extractive body cue:** This formulation allows robot policies to inherit several key properties from diffusion models - significantly improving performance. • Expressing multimodal action distributions.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Behavior Cloning Benchmark (State Policy) We present success rates with different checkpoint selection methods in the format of (max performance) / (average of ...
- **p. 9 / Figure/Table caption - extractive body cue:** Tab. 6. Diffusion Policy with R3M achieves an 80% success rate but predicts jittery actions and is more likely to get stuck compared to the ...
- **p. 6 / 5 Evaluation - extractive body cue:** We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for 4 of the tasks (9 variants in total). | hardware/simulator version and reset protocol | p. 6 (5 Evaluation), p. 7 (5 Evaluation) |
| Dataset/benchmark | This evaluation suite includes both simulated and real environments, single and multiple task benchmarks, fully actuated and under-actuated systems, and rigid and fluid objects. | role, split, size and leakage | p. 6 (5 Evaluation), p. 7 (5 Evaluation), p. 6 (5 Evaluation), p. 7 (5 Evaluation) |
| Metric | We threshold success rate by the minimum achieved IoU metric from the human demonstration dataset. | definition, denominator, direction and uncertainty | p. 9 (5 Evaluation), p. 9 (5 Evaluation), p. 6 (Figure/Table caption) |
| Baseline/ablation | We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%. | fair input/data/compute/action matching | p. 6 (5 Evaluation), p. 8 (5 Evaluation), p. 9 (5 Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 Evaluation - extractive body cue:** We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7. Realworld Push-T Comparisons. Columns 1-4 show action trajectories based on key events. The last column shows averaged images of the end state. A: ...
- **p. 11 / A C - extractive body cue:** The primary failure modes for these were out-of-domain initial positioning of the egg beater, or missing the egg beater crank handle or losing grasp of ...
- **p. 12 / A C - extractive body cue:** The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting ...
- **p. 12 / A C - extractive body cue:** The primary failure modes for these were missed grasps during initial grasp of the mat, where the policy struggled to correct itself and thus got ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Multimodal behavior. At the given state, the end-effector (blue) can either go left or right to push the block. Diffusion Policy learns both ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Training Stability. Left: IBC fails to infer training actions with increasing accuracy despite smoothly decreasing training loss for energy function. Right: IBC's evaluation ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 (2022) fails to commit to a single mode due to its lack of temporal action consistency.를 문제로 두고, To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: • Closed-loop ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 5 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), p. 16 (A.4 Hyperparameters) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
