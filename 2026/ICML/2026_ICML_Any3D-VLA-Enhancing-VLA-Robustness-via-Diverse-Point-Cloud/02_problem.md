# Problem - Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=zyMvoKYWMZ; PDF retrieval source: https://openreview.net/pdf/01fd7931fc7be08bf369b6a34264822e6d1de9b9.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): (2) To address the scaling bottlenecks of 3D VLA training and the cross-environment domain gap, we introduce a hybrid point-cloud training strategy and construct a large-scale RGBD dataset for VLA ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Existing Vision-Language-Action (VLA) models typically take 2D images as visual input, which limits their spatial understanding in complex scenes.
- **p. 1 / Abstract - extractive body cue:** How can we incorporate 3D information to enhance VLA capabilities?
- **p. 1 / Abstract - extractive body cue:** We conduct a pilot study across different observation spaces and visual representations.
- **p. 1 / Abstract - extractive body cue:** The results show that explicitly lifting visual input into point clouds yields representations that better complement their corresponding 2D representations.
- **p. 1 / Abstract - extractive body cue:** To address the challenges of (1) scarce 3D data and (2) the domain gap induced by cross-environment differences and 1School of Computing and Data Science, ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) To address the scaling bottlenecks of 3D VLA training and the cross-environment domain gap, we introduce a hybrid point-cloud training strategy and construct a ...
- **p. 2 / 1. Introduction - extractive body cue:** However, 3D VLAs still face bottlenecks in scalable training and real deployment: (1) compared to the massive amount of 2D image data, 3D data is ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (2) To address the scaling bottlenecks of 3D VLA training and the cross-environment domain gap, we introduce a hybrid point-cloud training strategy ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | model, takes, input, image, observations, corresponding, point, clouds, language, instruction | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Given, RGB, images, optional, depth, first, lift, visual | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: model, takes, input, image, observations, corresponding, point, clouds, language, instruction | p. 5 (5.3. Training Strategy), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, summarized, follows, ANY3D-VLA, plug-in, pipeline, existing, VLA | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: full, form, loss, function, provided, Appendix, incorporate, explicit | p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy), p. 4 (5.1. Overall Architecture) |
| Success / guarantee | instruction-conditioned task success | p. 6 (6.1.1. REAL-WORLD SETUP), p. 7 (6.1.3. REAL-WORLD POST-TRAINING), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, 3D VLAs still face bottlenecks in scalable training and real deployment: (1) compared to the massive amount of 2D image data, 3D data is ...
- **p. 1 / 1. Introduction - extractive body cue:** Vision-Language-Action (VLA) models, trained on massive collections of action trajectories paired with language instructions, hold great promise for achieving general-purpose embodied intelligence (Kim et al., ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA.

- **p. 2 / 1. Introduction - extractive body cue:** We propose ANY3D-VLA, a plug-in pipeline for existing VLA backbones (Figure 1).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We also conduct a qualitative analysis to highlight the robustness of our method compared to baselines and to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Future work could extend to additional robot platforms and environments, and evaluate more complex, long-horizon tasks. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Expert trajectories are produced by generating candidate grasp poses with BoDex (Chen et al., 2025b), performing oneshot collision-avoidance ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (5.3. Training Strategy), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 5 (5.3. Training Strategy), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
