# Problem

- Year/Venue: 2026 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2026/ICRA/2026_ICRA_Semantically-Consistent-Language-Gaussian-Splatting-for-3D/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing methods for querying 3D Gaussian Splatting often struggle with inconsistent 2D mask supervision and lack a robust 3D point-level retrieval mechanism.
- To address this, we propose a tracking-based Existing works address (a) by distilling language embeddings distillation process and aggregate the language embedding from foundation 2D vision-language models (VLMs)

## 해결하려는 문제
- In this work, (i) we present a novel point-level querying framework that performs tracking on segmentation masks to establish a semantically consistent groundtruth for distilling the language Gaussians; ...
- Extensive experiments on three benchmark datasets demonstrate that the proposed method outperforms state-of-the-art performance.
- Our method achieves an mIoU improvement of +4.14, +20.42, and +1.7 on the LERF, 3D-OVS, and Replica datasets.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
