# Method

- Year/Venue: 2026 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2026/ICRA/2026_ICRA_Semantically-Consistent-Language-Gaussian-Splatting-for-3D/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, (i) we present a novel point-level querying framework that performs tracking on segmentation masks to establish a semantically consistent groundtruth for distilling the language Gaussians; ...
- We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. • With this ...
- To address this, we propose a tracking-based Existing works address (a) by distilling language embeddings distillation process and aggregate the language embedding from foundation 2D vision-language models (VLMs) ...

## 원리적 동기
- Existing methods for querying 3D Gaussian Splatting often struggle with inconsistent 2D mask supervision and lack a robust 3D point-level retrieval mechanism.
- To address this, we propose a tracking-based Existing works address (a) by distilling language embeddings distillation process and aggregate the language embedding from foundation 2D vision-language models (VLMs)
- In this work, (i) we present a novel point-level querying framework that performs tracking on segmentation masks to establish a semantically consistent groundtruth for distilling the language Gaussians; ...

## 핵심 방법론
- We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. • With this ...
- Differently, our approach does not rely on new loss functions.
- III, a tracking module takes a sequence of images and Differently, we propose a novel method for constructing regions of interest as input to track masks of the ...
- IV-A, we present a masklet extraction algorithm (Alg.
- Paper website: https : //evelinyin.github.io/seconGS/ • We introduce tracking for generating semantic and 3D- Standard Query 0.12 wood dressing doll pebbled wall Avg IOU Score 0.10 0.08 0.06 ...
