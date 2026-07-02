# Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying

- Year/Venue: 2026 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2026/ICRA/2026_ICRA_Semantically-Consistent-Language-Gaussian-Splatting-for-3D/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods for querying 3D Gaussian Splatting often struggle with inconsistent 2D mask supervision and lack a robust 3D point-level retrieval mechanism.
- To address this, we propose a tracking-based Existing works address (a) by distilling language embeddings distillation process and aggregate the language embedding from foundation 2D vision-language models (VLMs)

## Core Idea
- In this work, (i) we present a novel point-level querying framework that performs tracking on segmentation masks to establish a semantically consistent groundtruth for distilling the language Gaussians; ...
- We observe that it does not have a consistent optimal threshold for all queries. consistent ground-truth to train language-aware Gaussians, which improves the distillation quality. • With this ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on three benchmark datasets demonstrate that the proposed method outperforms state-of-the-art performance.
- Our method achieves an mIoU improvement of +4.14, +20.42, and +1.7 on the LERF, 3D-OVS, and Replica datasets.
- In the case of 3D LERF , 3D-OVS , and Replica , demonstrating Gaussian Splatting , this involves retrieving the relevant that our method outperforms the state-of-the-art method ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, (i) we present a novel point-level querying framework that performs tracking on segmentation masks to establish a semantically consistent groundtruth for distilling the language Gaussians; ...
- Extensive experiments on three benchmark datasets demonstrate that the proposed method outperforms state-of-the-art performance.
- Our method achieves an mIoU improvement of +4.14, +20.42, and +1.7 on the LERF, 3D-OVS, and Replica datasets.

## Abstract Cue
- —Open-vocabulary 3D scene understanding is crucial for robotics applications, such as natural language-driven manipulation, human-robot interaction, and autonomous navigation.
