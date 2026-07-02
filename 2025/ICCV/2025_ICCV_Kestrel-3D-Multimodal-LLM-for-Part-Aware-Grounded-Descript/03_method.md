# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Kestrel-3D-Multimodal-LLM-for-Part-Aware-Grounded-Descript/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language model that integrates ...
- To address this gap, we present the 3DCoMPaT Grounded Instructions (3DCoMPaT-GrIn) Dataset, a comprehensive resource that pairs rich point cloud descriptions with corresponding part-level segmentation masks.
- armrests In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, partaware segmentation grounding and detailed explanation ...

## 원리적 동기
- Existing 3D datasets largely focus on either vision-only part segmentation or vision-language scene segmentation, lacking the fine-grained multimodal segmentation needed for robotic navigation and interaction in real-world environments.
- To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language model that integrates ...
- To tackle the inherent challenges of grounding objects and generating grounded descriptions at the part level, we propose Kestrel, a part-aware 3D multimodal large language model that integrates ...

## 핵심 방법론
- PARIS3D Kestrel mIoU 56.77 72.54 Table 4.
- Application Domain Shift Generalizability.
- We evaluate Kestrel’s ability to generalize to new domains by testing it on Objaverse using a checkpoint trained only on 3DCoMPaT-GrIn.
- As shown in the first two images of Fig.
- Evaluates model performance on implicit grounding and grounded reasoning tasks.
