# Method

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, referring segmentation, language
- Paper link: ./2026/CVPR/2026_CVPR_LangRef3DGS-Natural-Language-Guided-3D-Referential-Segment/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To overcome this, we present a real-time framework that leverages 3D Gaussian Splatting (3DGS) to build a semantically continuous and differentiable embedding field from partial observations.
- Despite significant missing data (e.g., the stuffed bear, plate, and cookies are partially unobserved), our method accurately segments objects of varying scales—from the large tea glass to the ...
- Our approach integrates two key components: a Dirichlet Process (DP) for the adaptive discovery of novel object categories, and a gradient low-rank mechanism that enhances class separability by ...

## 원리적 동기
- Despite significant progress in 3D semantic segmentation, existing methods remain constrained by several inherent limitations.
- These limitations originate from two intertwined factors.
- To overcome this, we present a real-time framework that leverages 3D Gaussian Splatting (3DGS) to build a semantically continuous and differentiable embedding field from partial observations.

## 핵심 방법론
- figurines Venue LERF LangSplat Gaussian Grouping CGC Feature-3DGS ILGS OpenSplat3D LangRef3DGS teatime ramen mean mIoU mBIoU mIoU mBIoU mIoU mBIoU mIoU mBIoU 33.5 52.8 69.7 91.6 58.8 75.9 ...
- These observations, supported by extensive examples in Appendix F.2, suggest that combining Gaussian-based semantic embeddings with Dirichlet Process (DP) clustering ensures stable reasoning even under partial observations.
- Method LangSplat LEGaussians OpenGaussian OpenInsGaussian OpenSplat3D LangRef3DGS Venue CVPR2024 CVPR2024 NeurIPS2024 ICCV2025 CVPR2025 Ours figurines teatime ramen waldo kitchen mean mIoU mAcc. mIoU mAcc. mIoU mAcc. mIoU mAcc. ...
- Method LERF LangSplat Gaussian Grouping CGC LEGaussians OpenGaussian Feature-3DGS OpenInsGaussian ILGS LangRef3DGS Venue CVPR2023 CVPR2024 ECCV2024 ICPR2024 CVPR2024 NeurIPS2024 CVPR2024 ICCV2025 ICCV2025 Ours LERF-Mask LERF-OVS mIoU mBloU mIoU ...
