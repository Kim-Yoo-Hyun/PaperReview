# Dexterous World Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Byungjun Kim, Taeksoo Kim, Junyoung Lee, Hanbyul Joo
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, world model, dexterous manipulation, video prediction
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 safety 문제를 이해하기 위해 읽는다. 본문은 However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial for modeling realistic human manipulations.를 문제로 두고, Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent progress in 3D reconstruction has made it easy to create realistic digital twins from everyday environments.
- **p. 1 / Abstract - extractive body cue:** However, current digital twins remain largely static, limited to navigation and view synthesis without embodied interactivity.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we introduce Dexterous World Model (DWM), a scene-action-conditioned video diffusion framework that models how dexterous human actions induce dynamic changes in ...
- **p. 1 / Abstract - extractive body cue:** Given a static 3D scene rendering and an egocentric hand motion sequence, DWM generates temporally coherent videos depicting plausible human-scene interactions.
- **p. 1 / Abstract - extractive body cue:** Our approach conditions video generation on (1) static scene renderings following a specified camera trajectory to ensure spatial consistency, and (2) egocentric hand mesh renderings ...
- **p. 2 / 1. Introduction - extractive body cue:** However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial ...
- **p. 2 / 1. Introduction - extractive body cue:** Many existing world models often treat camera motion as the action input [6, 63].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion.
- **p. 2 / 1. Introduction - extractive body cue:** (2) We propose a conditioning scheme that leverages static scene videos and egocentric hand motions to model interaction-induced residual dynamics.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** 2 for the overview of our framework.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** (3), we instantiate our framework as an egocentric, scene-action-conditioned video diffusion model.
- **p. 1 / 1. Introduction - extractive body cue:** Modeling dynamic consequences and causal relationships is central to world modeling, which enables the prediction of environmental changes This CVPR paper is the Open Access ...
- **p. 3 / 3.1. Formulation of Dexterous World Models - extractive body cue:** (2) Here, pd θ is the dynamics model that samples the scene and action-induced changes (S0, ∆S1:F ) given the actions A1:F = {C, H}1:F ...
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** The model then simulates the resulting environment states induced by the hand action inputs under the same camera views, V1:F = Π(S0 + ∆S1:F ; ...
- **p. 5 / 3.3. Paired Interaction Video Dataset Construction - extractive body cue:** For each prerecorded action sequence in TRUMANS, we render three synchronized outputs: (1) the interaction video captures the full human-scene interaction from the moving egocentric ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Conditional-independence assumption | 원문 대조: 초기 static scene S_0, interaction-induced changes ΔS_{1:F}, camera sequence C_{1:F}가 주어지면 observation model에서 hand-action input과 initial frame에 대한 직접 조건을 제거할 수 있다는 conditional-independence 설명이다. Action이 world dynamics에 필요 없다는 주장은 아니다. ([PDF p. 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=3), §3.1 Formulation of Dexterous World Models, Eq. (2)) | Latent S_0, ΔS, C 조건; 실제 관측 입력과 동일시하지 않음 | [PDF p. 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=3), §3.1 Formulation of Dexterous World Models, Eq. (2) |
| State/latent | observation, model, simplified, visual, outcome, conditionally, independent, action, input, image, given, known | safe set, recovery state 또는 constraint margin | p. 3 (3.1. Formulation of Dexterous World Models), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 2 (1. Introduction) |
| Output/action | For each prerecorded action sequence in TRUMANS, we render three synchronized outputs: (1) the interaction video captures the full human-scene interaction from the moving egocentric camera; (2) the static-scene video is rendered ... | shielded, recovery 또는 safe action | p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The training objective follows the standard latent diffusion loss [36]: LLDM = Ez0,t,ϵ h ∥ϵ -ϵθ(zt, t / cs, ch)∥2 2 i . | task return과 violation/failure probability | p. 5 (3.2. Scene-Action-Conditioned Video Diffusion), p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.1. Formulation of Dexterous World Models) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion.
- **p. 2 / 1. Introduction - extractive body cue:** (2) We propose a conditioning scheme that leverages static scene videos and egocentric hand motions to model interaction-induced residual dynamics.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** 2 for the overview of our framework.
- **p. 4 / 3.2. Scene-Action-Conditioned Video Diffusion - extractive body cue:** (3), we instantiate our framework as an egocentric, scene-action-conditioned video diffusion model.
- **p. 1 / 1. Introduction - extractive body cue:** Modeling dynamic consequences and causal relationships is central to world modeling, which enables the prediction of environmental changes This CVPR paper is the Open Access ...
- **p. 8 / 4.2. Qualitative Results - extractive body cue:** Including real-world data for training significantly improves both perceptual and pixel-level metrics across synthetic and real-world test sets, demonstrating that static-camera real-world interactions enhance generalization.
- **p. 6 / 4.1. Comparison - extractive body cue:** 1, where our method achieves superior performance across all metrics.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** 2, incorporating real-world data consistently improves performance on most metrics, not only on synthetic test sequences but also on Aria-captured real-world data, which includes both ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.2. Qualitative Results), p. 6 (4.1. Comparison) |
| Embodiment/environment | Despite real-world scenes with dynamic view being completely unseen during training, and the absence of any training samples involving opening a window, DWM successfully generates coherent simulations, demonstrating strong generalization. | hardware/simulator version and reset protocol | p. 6 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction) |
| Dataset/benchmark | Notably, our method generalizes well to completely unseen real-world scenes, producing coherent action-conditioned dynamics such as opening a sliding window. | role, split, size and leakage | p. 6 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction), p. 7 (4.1. Comparison), p. 5 (3.3. Paired Interaction Video Dataset Construction) |
| Metric | Specifically, we report LPIPS [57] and DreamSim [12] scores for perceptual similarity, and PSNR and SSIM for pixel-level quality. | definition, denominator, direction and uncertainty | p. 6 (4. Experiments), p. 6 (3.4. Action Evaluation with DWM), p. 7 (4.2. Qualitative Results) |
| Baseline/ablation | Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. | fair input/data/compute/action matching | p. 6 (4.1. Comparison), p. 6 (4.1. Comparison), p. 7 (4.1. Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Comparison - extractive body cue:** CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest.
- **p. 6 / 4.1. Comparison - extractive body cue:** InterDyn [2] produces spatially aligned hands with the input masks but fails to model resulting object dynamics.
- **p. 7 / 4.1. Comparison - extractive body cue:** Baselines fail to perform meaningful actions or hallucinate incorrect interactions.

## Why Read It

Manipulation, contact, tactile, and dexterity의 safety 문제를 이해하기 위해 읽는다. 본문은 However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial for modeling realistic human manipulations.를 문제로 두고, Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 5 (3.3. Paired Interaction Video Dataset Construction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial for modeling realistic human manipulations. (p. 2, 1. Introduction).
- **Actual contribution:** Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion. (p. 2, 1. Introduction).
- **Evaluation boundary:** Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. (p. 6, 4.1. Comparison).
- **Explicit failure boundary:** CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest. (p. 6, 4.1. Comparison).
