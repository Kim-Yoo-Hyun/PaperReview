# ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=OheAR2xrtb.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114743. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Diffusion, equivariant
- Official paper: https://openreview.net/forum?id=OheAR2xrtb
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114743
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, previous trajectory-level diffusion models for robotic manipulation have two key limitations.를 문제로 두고, In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves a proficient and generalizable manipulation policy wi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Imitation learning, e.g., diffusion policy, has been proven effective in various robotic manipulation tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, extensive demonstrations are required for policy robustness and generalization.
- **p. 1 / ABSTRACT - extractive body cue:** To reduce the demonstration reliance, we leverage spatial symmetry and propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion model for generating action sequences in complex ...
- **p. 1 / ABSTRACT - extractive body cue:** Further, previous equivariant diffusion models require the per-step equivariance in the Markov process, making it difficult to learn policy under such strong constraints.
- **p. 1 / ABSTRACT - extractive body cue:** We theoretically extend equivariant Markov kernels and simplify the condition of equivariant diffusion process, thereby significantly improving training efficiency for trajectory-level SE(3) equivariant diffusion policy.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, previous trajectory-level diffusion models for robotic manipulation have two key limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ET-SEED improves the sample efficiency and decreases the training difficulty by restricting the equivariant operations during the diffusion denoising process.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, we have ˆAk→0 = sθ(O, Ak; k) (8) To ensure the overall SE(3) equivariance of our pipeline, we propose a novel design of denoising ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Further, in real-world experiments, with only 20 demonstration trajectories, our method is able to generalize to unseen scenarios.
- **p. 4 / 4 METHOD - extractive body cue:** In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation.
- **p. 5 / 4 METHOD - extractive body cue:** This key design choice significantly reduces the training complexity, thereby enhancing the overall performance of our method.
- **p. 7 / 4 METHOD - extractive body cue:** In each denoising step, the input of our denoising network sθ consists of observation O, noisy action sequence Ak, and scalar condition k, outputs the ...
- **p. 4 / 4 METHOD - extractive body cue:** 2 is a general example to show how it works, given an observation and a noisy action sequence, our model first implement K -1 invariant ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, sθ is defined as sθ(O, Ak; k) =  Einv(O, Ak; k), k > 1 Eequiv(O, Ak; k), k = 1 (9) As illustrated ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | ET-SEED can theoretically guarantee the output actions are equivariant to any SE(3) transformation applied on the input observation, while only involving one equivariant denoising step. | image/video, language instruction, proprioception과 history | p. 4 (4 METHOD), p. 7 (4 METHOD) |
| State/latent | ET-SEED, theoretically, guarantee, output, actions, equivariant, transformation, applied, input, observation, while, only | language-grounded task state와 action-policy context | p. 4 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD) |
| Output/action | When the input observation O is transformed by any SE(3) element T, the output denoised action sequence A0 will be equivariantly transformed. | continuous action, pose 또는 action chunk | p. 7 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD) |
| Objective/outcome | In practice, we observe that training neural networks to approximate the properties of p2 and p3 is much more challenging compared to p1, both in terms of performance and training cost. | instruction following, task success, generalization과 latency | p. 5 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves ...
- **p. 7 / 4 METHOD - extractive body cue:** Formally, we have ˆAk→0 = sθ(O, Ak; k) (8) To ensure the overall SE(3) equivariance of our pipeline, we propose a novel design of denoising ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Further, in real-world experiments, with only 20 demonstration trajectories, our method is able to generalize to unseen scenarios.
- **p. 4 / 4 METHOD - extractive body cue:** In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation.
- **p. 5 / 4 METHOD - extractive body cue:** This key design choice significantly reduces the training complexity, thereby enhancing the overall performance of our method.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Design Average Ours w/o SE(3) 24±4.48 Ours w/o Eqv-Diff 57±6.52 Ours 76±2.24 While EquiBot achieves commendable results in both success rate and Dgeo, it struggles ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** (2) Can our method achieve comparable performance with fewer demonstrations?
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, ET-SEED consistently outperforms across all six tasks, with minimal performance drop when facing unseen object poses.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Embodiment/environment | (3) Is our method applicable to real-world robotic manipulation tasks? | hardware/simulator version and reset protocol | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Dataset/benchmark | We design six representative robot manipulation tasks: Open Bottle Cap, Open Door, Rotate Triangle, Calligraphy, Cloth Folding, and Cloth Fling. | role, split, size and leakage | p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (0.6 Results) |
| Metric | Table 1: Success rates (↑) and standard deviation of different tasks in simulation. Open Bottle Cap Open Door Rotate Triangle T NP T NP | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Baseline/ablation | DP3 and DP3+Aug are used to compare ET-SEED with baseline methods that utilize data augmentation to achieve spatial generalization, while EquiBot allows for a comparison between different architectures of equivariant diffusion process. | fair input/data/compute/action matching | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 CONCLUSION - extractive body cue:** However, the proposed method has certain limitations.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first passed through K -1 SE(3) invariant denoising ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** The standard deviation of the Gaussian noise is set to 10% of the workspace size.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: Our method without the SE(3) equivariant denoising ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, previous trajectory-level diffusion models for robotic manipulation have two key limitations.를 문제로 두고, In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves a proficient and generalizable manipulation policy wi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 7 (4 METHOD), p. 4 (4 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
