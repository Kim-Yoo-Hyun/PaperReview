# GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Kai Zhang, Sai Bi, Hao Tan, Yuanbo Xiangli, Nanxuan Zhao, Kalyan Sunkavalli, Zexiang Xu
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf)

## Why This Paper Is Here

GS-LRM은 알려진 카메라 자세와 소수의 입력 뷰에서 픽셀별 가우시안 속성을 직접 예측해 물체나 장면을 복원한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=1) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=5)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Reconstructing a 3D scene from image captures is both a central problem and a long-standing challenge in computer vision.
- **p. 1 / 1 Introduction - extractive body cue:** Traditionally, high-quality 3D reconstruction relies on complex photogrammetry systems [23, 48,50] and requires a dense set of multi-view images.
- **p. 1 / 1 Introduction - extractive body cue:** Recent advancements in neural representations and differentiable rendering [9, 30, 40, 41] have shown superior reconstruction and rendering quality, by optimizing renderings on a per-scene ...
- **p. 1 / 1 Introduction - extractive body cue:** However, these methods are slow and still require a large number of input views.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, transformer-based 3D large reconstruction models (LRMs) have been proposed, learning general 3D reconstruction priors from vast collections of 3D objects and achieving sparse-view 3D ...
- **p. 1 / 1 Introduction - extractive body cue:** This leads to challenges in training and rendering speeds, preserving fine details, and scaling to large scenes beyond object-centric inputs. *

## Core Idea

- **p. 4 / 3 Method - extractive body cue:** In this section, we present the technical details of our method, including the architecture of our transformer-based model (Sec.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose GS-LRM, a novel transformer-based large reconstruction model that predicts 3D Gaussian primitives [30] from sparse input images, enabling fast and ...
- **p. 5 / 3 Method - extractive body cue:** 2) and consists of Pre-LayerNorm [3], multi-head Self-Attention [60] and MLP.
- **p. 2 / 1 Introduction - extractive body cue:** The core of our approach is a simple and scalable transformer-based network architecture that predicts per-pixel Gaussians.
- **p. 6 / 3 Method - extractive body cue:** This property allows us to better handle high-frequency details in the inputs and large-scale scene captures.
- **p. 6 / 3 Method - extractive body cue:** We empirically find that the perceptual loss in [14] based on VGG-19 network [53] provides a more stable training than LPIPS [73] used in [27,32,61,66], ...
- **p. 4 / 3 Method - extractive body cue:** Multi-view image tokens are then concatenated and passed through a sequence of transformer blocks consisting of self-attention and MLP layers.
- **p. 5 / 3 Method - extractive body cue:** GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting 5 Per-pixel Gaussians Transformer Block (×𝐿) MLP + Self-Att + Linear & Unpatchify Merged Gaussians Image + ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Unlike previous LRMs that require careful designs of additional (triplane) NeRF tokens for reconstruction, we align input (2D images) and output (3D Gaussians) in the same pixel space, predicting one Gaussian per ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 6 (3 Method) |
| State/latent | Unlike, previous, LRMs, require, careful, designs, additional, triplane, NeRF, tokens, reconstruction, align | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method) |
| Output/action | The final output of our model is simply the merge of 3D Gaussians from all N input views. | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | 3.2 Loss Functions During training, we render the images at the M supervision views using the predicted Gaussian splats, and minimize the image reconstruction loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- 여러 뷰의 영상 패치를 하나의 트랜스포머 입력으로 결합하고 디코딩한 가우시안을 미분 가능하게 렌더링해 학습한다. [PDF 4쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=4) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=6)
- Objaverse 물체와 RealEstate10K 장면에 맞춘 모델을 따로 학습해 희소 뷰 복원 성능과 추론 비용을 비교했다. [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=7) · [PDF 9쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=9) · [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=10)

## Evaluation Scope

약 0.23초는 카메라 자세를 아는 2~4개 입력 뷰에서 A100 한 장으로 가우시안을 예측하는 추론 시간이다. 물체 복원과 장면 복원은 별도로 학습한 모델로 비교했다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=1) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=7) · [PDF 14쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03212.pdf#page=14)

## Explicit Limitations and Failure Boundary

- **p. 13 / 4 Experiments - extractive body cue:** 4.6 Limitations Although our method shows high-quality reconstruction results from posed sparse images, there are still a few limitations to be addressed in future work.
- **p. 14 / 5 Conclusion - extractive body cue:** We hope that our work can inspire more future work in the space of data-driven feed-forward 3D reconstruction.
- **p. 8 / 4 Experiments - extractive body cue:** The Triplane-LRM cannot reconstruct high-frequency details (top left and top right) and thin structures (bottom left) well.
- **p. 14 / 4 Experiments - extractive body cue:** Please refer to our project page for the video and interactive rendering results. the view frustum, which means that unseen regions cannot be reconstructed.
- **p. 9 / 4 Experiments - extractive body cue:** We also tried to compare against another baseline SparseNeuS [36]; however, we found that it failed to produce plausible reconstructions given 4 highly sparse inputs; ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method)이다.
