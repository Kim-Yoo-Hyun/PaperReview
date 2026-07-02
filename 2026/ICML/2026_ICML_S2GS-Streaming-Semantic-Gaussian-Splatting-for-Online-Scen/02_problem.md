# Problem

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, 3D reconstruction, semantic, alignment, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_S2GS-Streaming-Semantic-Gaussian-Splatting-for-Online-Scen/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, most existing approaches remain limited to streaming modeling of geometry and appearance, lacking semantic scene understanding and instance-level, decomposable representations, and thus falling short for downstream applications ...
- However, most existing approaches remain offline-global in the sense that, as new frames arrive, they repeatedly recompute cross-frame interactions over the growing history.

## 해결하려는 문제
- As shown in Figure 1, even on an H200 GPU equipped with 140 GB of VRAM, SIU3R (Xu et al., 2025) still encounters an out-ofmemory (OOM) after processing ...
- More fundamentally, in real-world online scenarios, inputs arrive Recently, feed-forward methods (Xu et al., 2025; Sun et al., 2025; Tian et al., 2025) built upon 3D Gaussian Splatting ...
- Introduction Meanwhile, recent advances (Li et al., 2025c; Huang et al., 2025; Wang et al., 2025b; Lan et al., 2025; Zhuo et al., 2025; Yuan et al., 2026) ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
