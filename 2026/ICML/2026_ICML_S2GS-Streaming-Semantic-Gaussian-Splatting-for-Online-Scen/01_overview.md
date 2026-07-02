# S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, 3D reconstruction, semantic, alignment, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_S2GS-Streaming-Semantic-Gaussian-Splatting-for-Online-Scen/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short for downstream applications ...
- However, most existing approaches remain offline-global in the sense that, as new frames arrive, they repeatedly recompute cross-frame interactions over the growing history.

## Core Idea
- Our method maintains low per-frame runtime with only mild growth as the stream length increases, while
- More fundamentally, in real-world online scenarios, inputs arrive Recently, feed-forward methods (Xu et al., 2025; Sun et al., 2025; Tian et al., 2025) built upon 3D Gaussian Splatting ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Introduction Meanwhile, recent advances (Li et al., 2025c; Huang et al., 2025; Wang et al., 2025b; Lan et al., 2025; Zhuo et al., 2025; Yuan et al., 2026) ...
- As shown in Figure 1, even on an H200 GPU equipped with 140 GB of VRAM, SIU3R (Xu et al., 2025) still encounters an out-ofmemory (OOM) after processing ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- As shown in Figure 1, even on an H200 GPU equipped with 140 GB of VRAM, SIU3R (Xu et al., 2025) still encounters an out-ofmemory (OOM) after processing ...
- More fundamentally, in real-world online scenarios, inputs arrive Recently, feed-forward methods (Xu et al., 2025; Sun et al., 2025; Tian et al., 2025) built upon 3D Gaussian Splatting ...
- Introduction Meanwhile, recent advances (Li et al., 2025c; Huang et al., 2025; Wang et al., 2025b; Lan et al., 2025; Zhuo et al., 2025; Yuan et al., 2026) ...

## Abstract Cue
- SIU3R Ours OOM 16 32 64 128 256 512 1024 16 32 64 128 256 512 1024 Number of views Number of views Figure 1.
