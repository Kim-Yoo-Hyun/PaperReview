# Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Kestrel-3D-Multimodal-LLM-for-Part-Aware-Grounded-Descript/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing 3D datasets largely focus on either vision-only part segmentation or vision-language scene segmentation, lacking the fine-grained multimodal segmentation needed for robotic navigation and interaction in real-world environments.
- To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language model that integrates ...
- Both armrests are also leather with a sleek black finish, matching the seat support, which is made of leather in brown.

## Core Idea
- To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language model that integrates ...
- To address this gap, we present the 3DCoMPaT Grounded Instructions (3DCoMPaT-GrIn) Dataset, a comprehensive resource that pairs rich point cloud descriptions with corresponding part-level segmentation masks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The extensive experiments demonstrate that Kestrel effectively bridges the gap between part-aware language understanding and 3D segmentation grounding, paving the way for more robust and interpretable 3D object ...
- Each part-level phrase in this generated text (e.g., “backrest” and “seat support”) is linked to a point-wise segmentation mask, challenging the model’s capability for part-aware language understanding and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language model that integrates ...
- To address this gap, we present the 3DCoMPaT Grounded Instructions (3DCoMPaT-GrIn) Dataset, a comprehensive resource that pairs rich point cloud descriptions with corresponding part-level segmentation masks.
- armrests In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, partaware segmentation grounding and detailed explanation ...

## Abstract Cue
- armrests In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, partaware segmentation grounding and detailed explanation of 3D objects.
