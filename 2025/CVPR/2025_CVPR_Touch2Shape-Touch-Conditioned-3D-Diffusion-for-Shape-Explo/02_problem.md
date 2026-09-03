# Problem - Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): This limitation presents challenges on two fronts.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Diffusion models have made breakthroughs in 3D generation tasks.
- **p. 1 / Abstract - extractive body cue:** Current 3D diffusion models focus on reconstructing target shape from images or a set of partial observations.
- **p. 1 / Abstract - extractive body cue:** While excelling in global context understanding, they struggle to capture the local details of complex shapes and limited to the occlusion and lighting conditions.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we utilize tactile images to capture the local 3D information and propose a Touch2Shape model, which leverages a touch-conditioned diffusion model ...
- **p. 1 / Abstract - extractive body cue:** For shape reconstruction, we have developed a touch embedding module to condition the diffusion model in creating a compact representation and a touch shape fusion ...
- **p. 2 / 1. Introduction - extractive body cue:** This limitation presents challenges on two fronts.
- **p. 2 / 1. Introduction - extractive body cue:** However, acquiring 3D data presents greater challenges and costs compared to 2D image and text data.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation presents challenges on two fronts. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | The policy model receives the denoised vector as input and is trained using reinforcement learning (Section 3.2). | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | policy, model, receives, denoised, vector, input, trained, reinforcement, learning, Section | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | loss, function, diffusion, model, training, follows, Ldiff, t//2 | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: policy, model, receives, denoised, vector, input, trained, reinforcement, learning, Section | p. 4 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model) |
| Decision / output variable | contact-aware action/force; body terms: main, contributions, article, follows, Touch2Shape, touch-conditioned, diffusion, model | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Touch Shape Fusion) |
| Objective / loss / cost | contact prediction/control error; cue terms: reward, function, setting, since, final, output, shape, predicted | p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model) |
| Success / guarantee | slip/contact success and safe interaction | p. 6 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.2. Evaluation on Reconstruction Performance), p. 7 (4.4. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, acquiring 3D data presents greater challenges and costs compared to 2D image and text data.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Touch Shape Fusion)): The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to guide the ...

- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments validate the effectiveness of our method, demonstrating significant improvements in both reconstruction performance and the ability to improve reconstruction quality through touch exploration.
- **p. 4 / 3.2. Touch Shape Fusion - extractive body cue:** The touch shape fusion module is designed with two goals.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Furthermore, the Oracle policy is used to select the action which resulted in the best improvement, which is ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 2 (1. Introduction), objective p. 5 (3.3. Policy Training), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 4 (3.1. Touch-conditioned Diffusion Model), p. 5 (3.3. Policy Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
