# Problem - Dexterous World Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial for modeling realistic human manipulations.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent progress in 3D reconstruction has made it easy to create realistic digital twins from everyday environments.
- **p. 1 / Abstract - extractive body cue:** However, current digital twins remain largely static, limited to navigation and view synthesis without embodied interactivity.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce Dexterous World Model (DWM), a scene-action-conditioned video diffusion framework that models how dexterous human actions induce dynamic changes in ...
- **p. 1 / Abstract - extractive body cue:** Given a static 3D scene rendering and an egocentric hand motion sequence, DWM generates temporally coherent videos depicting plausible human-scene interactions.
- **p. 1 / Abstract - extractive body cue:** Our approach conditions video generation on (1) static scene renderings following a specified camera trajectory to ensure spatial consistency, and (2) egocentric hand mesh renderings ...
- **p. 2 / 1. Introduction - extractive body cue:** However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial ...
- **p. 2 / 1. Introduction - extractive body cue:** Many existing world models often treat camera motion as the action input [6, 63].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Conditional-independence assumption | 원문 대조: 초기 static scene S_0, interaction-induced changes ΔS_{1:F}, camera sequence C_{1:F}가 주어지면 observation model에서 hand-action input과 initial frame에 대한 직접 조건을 제거할 수 있다는 conditional-independence 설명이다. Action이 world dynamics에 필요 없다는 주장은 아니다. ([PDF p. 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=3), §3.1 Formulation of Dexterous World Models, Eq. (2)) | Latent S_0, ΔS, C 조건 | 이 식은 sensor/preprocessing 계약이 아님 |
| State / latent | observation, model, simplified, visual, outcome, conditionally, independent, action, input, image | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | Furthermore, most, video, models, accept, only, textual, instruction | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: observation, model, simplified, visual, outcome, conditionally, independent, action, input, image | p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 2 (1. Introduction) |
| Decision / output variable | filtered/recovery action u_safe; body terms: main, contributions, summarized, follows, introduce, Dexterous, World, Models | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: training, objective, follows, standard, latent, diffusion, loss, LLDM | p. 5 (3.2. Scene-Action-Conditioned Video Diffusion) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 6 (4. Experiments), p. 6 (3.4. Action Evaluation with DWM), p. 7 (4.2. Qualitative Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Many existing world models often treat camera motion as the action input [6, 63].

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 1 (1. Introduction)): Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion.

- **p. 2 / 1. Introduction - extractive body cue:** (2) We propose a conditioning scheme that leverages static scene videos and egocentric hand motions to model interaction-induced residual dynamics.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** 2 for the overview of our framework.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** (3), we instantiate our framework as an egocentric, scene-action-conditioned video diffusion model.
- **p. 1 / 1. Introduction - extractive body cue:** Modeling dynamic consequences and causal relationships is central to world modeling, which enables the prediction of environmental changes This CVPR paper is the Open Access ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | InterDyn [2] produces spatially aligned hands with the input masks but fails to model resulting object dynamics. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Baselines fail to perform meaningful actions or hallucinate incorrect interactions. | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 5 (3.2. Scene-Action-Conditioned Video Diffusion).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial for modeling realistic human manipulations. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest. (p. 6, 4.1. Comparison).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
