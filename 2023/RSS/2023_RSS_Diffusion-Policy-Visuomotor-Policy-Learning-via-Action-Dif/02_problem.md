# Problem - Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.04137; PDF retrieval source: https://arxiv.org/pdf/2303.04137. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 5 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction)): (2022) fails to commit to a single mode due to its lack of temporal action consistency.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process.
- **p. 1 / Abstract - extractive body cue:** We benchmark Diffusion Policy across 15 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods ...
- **p. 1 / Abstract - extractive body cue:** Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of ...
- **p. 1 / Abstract - extractive body cue:** We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action ...
- **p. 1 / Abstract - extractive body cue:** To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including ...
- **p. 5 / 1 Introduction - extractive body cue:** (2022) fails to commit to a single mode due to its lack of temporal action consistency.
- **p. 1 / 1 Introduction - extractive body cue:** Prior work attempts to address this challenge by exploring different action representations (Fig 1 a) - using mixtures of Gaussians Mandlekar et al.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (2022) fails to commit to a single mode due to its lack of temporal action consistency. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | Diffusion Policy 3 b) CNN-based c) Transformer-based Conv1D Conv1D Conv1D Conv1D Conv1D Input: Image Observation Sequence Output: Action Sequence … Cross Attention ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | Diffusion, Policy, CNN-based, Transformer-based, Conv1D, Input, Image, Observation, Sequence, Output | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | formulation, instead, directly, outputting, action, policy, infers, action-score | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: Diffusion, Policy, CNN-based, Transformer-based, Conv1D, Input, Image, Observation, Sequence, Output | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: successfully, employ, diffusion, models, visuomotor, policy, learning, present | p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: Scaling, action, dimension, independently, works, well, most, tasks | p. 16 (A.1 Normalization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | closed-loop task success and robustness | p. 9 (5 Evaluation), p. 9 (5 Evaluation), p. 6 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Prior work attempts to address this challenge by exploring different action representations (Fig 1 a) - using mixtures of Gaussians Mandlekar et al.
- **p. 4 / 1 Introduction - extractive body cue:** The difficulty of transformer training Liu et al.
- **p. 5 / 1 Introduction - extractive body cue:** Similarly, BCRNN and BET would have difficulty specifying the number of modes that exist in the action distribution (needed for GMM or k-means steps).
- **p. 1 / 1 Introduction - extractive body cue:** (2011), which includes multimodal action distributions, a well-known challenge for policy learning. arXiv:2303.04137v5 [cs.RO] 14 Mar 2024

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction)): To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: ...

- **p. 4 / 1 Introduction - extractive body cue:** (2020), we introduce a novel transformer-based DDPM which adopts the transformer architecture from minGPT Shafiullah et al.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a visionconditioned diffusion policy, where the visual observations are treated as conditioning instead of a part of the joint data distribution.
- **p. 4 / 1 Introduction - extractive body cue:** Third, we removed inpainting-based goal state conditioning due to incompatibility with our framework utilizing a receding prediction horizon.
- **p. 1 / 1 Introduction - extractive body cue:** This formulation allows robot policies to inherit several key properties from diffusion models - significantly improving performance. • Expressing multimodal action distributions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | We observed that poor performance during the transition between stages is the most common failure case for the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Figure 7. Realworld Push-T Comparisons. Columns 1-4 show action trajectories based on key events. The last column shows ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | The primary failure modes for these were out-of-domain initial positioning of the egg beater, or missing the egg ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 5 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), interface p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 16 (A.1 Normalization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
