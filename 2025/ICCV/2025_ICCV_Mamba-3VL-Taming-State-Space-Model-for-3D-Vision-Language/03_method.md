# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Mamba-3VL-Taming-State-Space-Model-for-3D-Vision-Language/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose Mamba-3VL, a pioneering 3D-VL framework to model complex intra- and inter-modality correlations and enhance spatial relation reasoning, while guaranteeing top-tier performance, high efficiency, ...
- To further provide precise spatial encoding for mamba, we develop Instance-aware Dynamic Position Adapter (IDPA) to dynamically adjust instance-specific positional embeddings and enhance local spatial relation of 3D ...
- ScanRefer Nr3D Inference Time Training Time 0.6 Sr3D 0.5 0.4 0.3 0.2 Second (s) Accuracy (%) 0.1 BUTD-DETR EDA MCLN G3-LQ LIBA PQ3D Mamba-3VL Figure 2.

## 원리적 동기
- The primary challenge of these tasks lies i
- State Space Models (SSM) have emerged as promising linear-complexity alternatives for sequential data processing, while inherent selection mechanism offers notable capability for spatial modeling.
- In this paper, we propose Mamba-3VL, a pioneering 3D-VL framework to model complex intra- and inter-modality correlations and enhance spatial relation reasoning, while guaranteeing top-tier performance, high efficiency, ...

## 핵심 방법론
- The hidden dimension and query decoder layer is set to d = 768, L = 4. (5) The instance-specific positional embeddings x′i encodes rich object-centric attributes.
- Implementation Details x′i = Warping(ri , xi ) = Linear (concat (ri , xi )) , 22.4 31.5 34.0 25.1 23.0 36.0 31.8 39.5 The output x̄i of ...
