# Problem - RVT: Robotic View Transformer for 3D Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14896; PDF retrieval source: https://arxiv.org/pdf/2306.14896. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images.
- **p. 1 / Abstract - extractive body cue:** But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.
- **p. 1 / Abstract - extractive body cue:** Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the ...
- **p. 1 / Abstract - extractive body cue:** In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than ...
- **p. 1 / 1 Introduction - extractive body cue:** C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Hence, a key question is - can we build a manipulation network that not only performs well but also inherits the scalability of view-based methods?

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | model, outputs, dimensional, action, including, DoF, target, effector, pose, translation | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | model, should, predict, action, specified, target, end-effector, pose | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: model, outputs, dimensional, action, including, DoF, target, effector, pose, translation | p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method) |
| Decision / output variable | action, pose, option or chunk a; body terms: summarize, contributions, threefold, first, RVT, multi-view, transformer, object | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: heatmaps, cross-entropy, loss, image, rotation, Euler, angles, train | p. 5 (3 Method), p. 5 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 Method), p. 5 (3 Method) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4 Experiments), p. 5 (Figure/Table caption), p. 8 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Hence, a key question is - can we build a manipulation network that not only performs well but also inherits the scalability of view-based methods?
- **p. 2 / 1 Introduction - extractive body cue:** Another key innovation is that, unlike prior view-based methods, we decouple the camera images from the images fed to the transformer, by re-rendering the images ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method), p. 1 (1 Introduction)): To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the ...

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose RVT (Robotic View Transformer) that significantly outperforms the SOTA voxel-based method both in terms of success rate and training time, ...
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 1 / 1 Introduction - extractive body cue:** This hinders fast development and prototyping.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Although we found RVT to achieve state-of-the-art results, we identify some limitations that present exciting directions for future ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | 6.2 RVT Overview Insert peg in the blue spoke Virtual Image 1 Virtual Image 2 Virtual Image 5 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Hence, the reported performance does not reflect a single multi-task model. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 3 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method), p. 3 (3 Method), objective p. 5 (3 Method), p. 5 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. (p. 8, 4 Experiments).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
