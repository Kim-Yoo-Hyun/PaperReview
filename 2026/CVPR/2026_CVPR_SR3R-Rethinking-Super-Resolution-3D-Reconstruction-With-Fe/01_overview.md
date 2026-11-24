# SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Xiang Feng, Xiangbo Wang, Tieshi Zhong, Chengkai Wang, Yiting Zhao, Tianxiang Xu, Zhenzhong Kuang, Feiwei Qin, Xuefei Yin, Yanming Zhu
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf)

## Why This Paper Is Here

SR3R은 몇 장의 저해상도 입력 영상에서 고해상도 3D 가우시안을 직접 예측하도록 여러 장면에 걸쳐 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=1) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D super-resolution (3DSR) aims to reconstruct highresolution (HR) 3D scenes from low-resolution (LR) multiview images.
- **p. 1 / Abstract - extractive body cue:** Existing methods rely on dense LR inputs and per-scene optimization, which restricts the highfrequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited ...
- **p. 1 / Abstract - extractive body cue:** This severely limits reconstruction fidelity, cross-scene generalization, and real-time usability.
- **p. 1 / Abstract - extractive body cue:** We propose to reformulate 3DSR as a direct feedforward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific ...
- **p. 1 / Abstract - extractive body cue:** This fundamentally changes how 3DSR acquires high-frequency knowledge and enables robust generalization to unseen scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Although this strategy injects high-frequency cues into the HR 3DGS reconstruction, it suffers from several fundamental limitations.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows. • A novel formulation of 3DSR.
- **p. 2 / 1. Introduction - extractive body cue:** We propose SR3R, a feed-forward framework that directly reconstructs HR 3DGS from as few as two LR views through a learned mapping network.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** This removes the reliance on 2DSR pseudo-supervision, allows learning from large-scale multiscene data, and enables cross-scene generalization, substantially improving scalability and efficiency.
- **p. 4 / 3.2. Overall Framework - extractive body cue:** The LR input images are upsampled to the target resolution and processed by our mapping network, which consists of a ViT encoder, a feature refinement ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** To correct these unreliable 2D features, we introduce a feature refinement module that aligns the encoder tokens ten ∈RN×C with geometry-aware tokens tpre ∈RN×C extracted ...
- **p. 4 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** It adopts a transformer-based architecture composed of a ViT encoder, a feature refinement module, a ViT decoder, and a Gaussian offset learning module.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The two attention outputs Uo←p and Up←o are then concatenated and fused through a fully connected layer to generate the refined feature token tca.
- **p. 5 / 3.4. LR Image to HR 3DGS Mapping - extractive body cue:** The decoded features are then provided to the Gaussian offset learning module (Section 3.5) to estimate residual corrections from the densified representation GDense to the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This task has become increasingly critical because state-of-the-art 3D Gaussian Splatting (3DGS)-based reconstruction methods [14, 25] typically require dense and high-resolution input views to recover fine geometric and appearance details. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | task, become, increasingly, critical, because, state-of-the-art, Gaussian, Splatting, DGS, reconstruction, methods, typically | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| Output/action | Current 3DSR methods [9, 15, 24, 40] typically employ pretrained 2D image or video super-resolution (2DSR) models to generate pseudo-HR images from dense multiview LR inputs, which are then used as supervision ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.4. LR Image to HR 3DGS Mapping) |
| Objective/outcome | Following [38], we adopt a combination of pixel-wise reconstruction loss (MSE) and perceptual consistency loss (LPIPS) to jointly preserve geometric accuracy and visual fidelity. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.6. Training Objective), p. 3 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- 영상 특징을 정제하고 가우시안의 위치 오프셋을 학습해 고주파 외관과 기하를 복원한다. [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=5)
- 입력에 없던 시점의 고해상도 렌더링을 평가하고, 학습에 포함되지 않은 장면에서 장면별 최적화 방법과 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

4배 초해상도는 RE10K와 ACID의 새 시점에서 평가했다(표 1). 표 2는 RE10K에서 학습한 모델을 물체 중심 DTU에 추가 학습 없이 적용한 별도 전이 실험이다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=6) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.pdf#page=8)

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive body cue:** These improvements hold for both 3DGS backbones, confirming that our offsetbased refinement and cross-view fusion effectively restore 3D-specific high-frequency structures that 2D upsampling and direct ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Applying 2D upsampling reduces excessive softness but still fails to recover reliable high-frequency structures, often introducing ambiguous or hallucinated textures.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Notably, even Bilinear interpolation already surpasses all feed-forward baselines (Table 1), indicating that SR3R does not depend on a particular upsampling design.
- **p. 7 / 4.2. Comparison with State-of-the-Art - extractive body cue:** These results highlight the advantage of learning Gaussian offsets over direct parameter regression, enabling more accurate high-frequency recovery under sparse LR inputs.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Overall Framework), p. 4 (3.4. LR Image to HR 3DGS Mapping)이다.
