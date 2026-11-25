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
- Code/Project: https://snuvclab.github.io/dwm/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

Dexterous World Models는 3차원 장면과 일인칭 사람 손 움직임을 조건으로 손이 물체와 상호작용할 때의 영상을 생성한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=1)

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

- 지정된 카메라 경로에서 렌더링한 정적 장면과 손 메시 영상을 분리된 조건으로 비디오 확산 모델에 제공한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=3) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=5)
- 장면과 손 동작에 맞춰 생성한 영상의 시간적·시각적 일관성을 평가하고, 각 조건을 제거했을 때 생성 결과가 어떻게 달라지는지 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.1. Formulation of Dexterous World Models), p. 4 (3.2. Scene-Action-Conditioned Video Diffusion), p. 5 (3.3. Paired Interaction Video Dataset Construction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, textual descriptions are inherently imprecise, as they cannot accurately specify human actions such as hand configurations, fine-grained temporal control, both of which are crucial for modeling realistic human manipulations. (p. 2, 1. Introduction).
- **Actual contribution:** Our main contributions can be summarized as follows: (1) We introduce Dexterous World Models (DWM), a new formulation of world modeling via scene-action-conditioned video diffusion. (p. 2, 1. Introduction).
- **Evaluation boundary:** Quantitatively, ours outperforms baselines across all metrics on real-world static camera videos. (p. 6, 4.1. Comparison).
- **Explicit failure boundary:** CVX-Fun Fine-tuned often fails to interact with the correct target and hallucinates the object of interest. (p. 6, 4.1. Comparison).

## 원문과 공개 자료

- 코드 · 영상 세계 모델의 추론과 훈련 구현 · training/cogvideox/inference.py [배포 파일](https://raw.githubusercontent.com/snuvclab/dwm/19de79b879e662a133761e9f9afb60d4d92a618c/training/cogvideox/inference.py)
- 데이터 · 저자 공개 Real-World Dynamic 평가 분할의 실측 일인칭 영상 · realworld/videos/00001.mp4 [배포 파일](https://huggingface.co/datasets/byungjun-kim/DWM-RealWorld-Dynamic/blob/b9e6da6b85707f7402bc61ea0dae100860db14f9/realworld/videos/00001.mp4)
