# Problem - ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OheAR2xrtb; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114743. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): However, previous trajectory-level diffusion models for robotic manipulation have two key limitations.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Imitation learning, e.g., diffusion policy, has been proven effective in various robotic manipulation tasks.
- **p. 1 / ABSTRACT - extractive body cue:** However, extensive demonstrations are required for policy robustness and generalization.
- **p. 1 / ABSTRACT - extractive body cue:** To reduce the demonstration reliance, we leverage spatial symmetry and propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion model for generating action sequences in complex ...
- **p. 1 / ABSTRACT - extractive body cue:** Further, previous equivariant diffusion models require the per-step equivariance in the Markov process, making it difficult to learn policy under such strong constraints.
- **p. 1 / ABSTRACT - extractive body cue:** We theoretically extend equivariant Markov kernels and simplify the condition of equivariant diffusion process, thereby significantly improving training efficiency for trajectory-level SE(3) equivariant diffusion policy.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, previous trajectory-level diffusion models for robotic manipulation have two key limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** ET-SEED improves the sample efficiency and decreases the training difficulty by restricting the equivariant operations during the diffusion denoising process.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, previous trajectory-level diffusion models for robotic manipulation have two key limitations. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | ET-SEED can theoretically guarantee the output actions are equivariant to any SE(3) transformation applied on the input observation, while only involving one ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | ET-SEED, theoretically, guarantee, output, actions, equivariant, transformation, applied, input, observation | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | denoising, step, input, network, consists, observation, noisy, action | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: ET-SEED, theoretically, guarantee, output, actions, equivariant, transformation, applied, input, observation | p. 4 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, mainly, followed, ET-SEED, efficient, trajectory-level, equivariant | p. 2 (1 INTRODUCTION), p. 7 (4 METHOD), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: practice, observe, training, neural, networks, approximate, properties, much | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (4 METHOD), p. 4 (4 METHOD), p. 6 (4 METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 8 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** ET-SEED improves the sample efficiency and decreases the training difficulty by restricting the equivariant operations during the diffusion denoising process.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Though, one of the main challenges of imitation learning is that it requires extensive demonstrations to learn a robust manipulation policy (Brohan et al., 2022; ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Although some works seek to tackle these issues through data augmentation (Yu et al., 2023) or contrastive learning (Ma et al., 2024), they usually require ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 7 (4 METHOD), p. 2 (1 INTRODUCTION), p. 4 (4 METHOD), p. 5 (4 METHOD)): In summary, our contributions are mainly as followed: • We propose ET-SEED, an efficient trajectory-level SE(3) equivariant diffusion policy defined on SE(3) manifold, which achieves a proficient and generalizable manipulation ...

- **p. 7 / 4 METHOD - extractive body cue:** Formally, we have ˆAk→0 = sθ(O, Ak; k) (8) To ensure the overall SE(3) equivariance of our pipeline, we propose a novel design of denoising ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Further, in real-world experiments, with only 20 demonstration trajectories, our method is able to generalize to unseen scenarios.
- **p. 4 / 4 METHOD - extractive body cue:** In this paper, we propose ET-SEED, a trajectorylevel end-to-end SE(3) equivariant diffusion model for robotic manipulation.
- **p. 5 / 4 METHOD - extractive body cue:** This key design choice significantly reduces the training complexity, thereby enhancing the overall performance of our method.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | However, the proposed method has certain limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Figure 3: Overview of our pipeline. A colored point cloud and a random sampled action sequence are first ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The standard deviation of the Gaussian noise is set to 10% of the workspace size. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In this variant, we use a standard PointNet++ to predict noise at each step. • Ours w/o Eqv-Diff: ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 4 (4 METHOD), p. 7 (4 METHOD), p. 7 (4 METHOD), p. 4 (4 METHOD), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
