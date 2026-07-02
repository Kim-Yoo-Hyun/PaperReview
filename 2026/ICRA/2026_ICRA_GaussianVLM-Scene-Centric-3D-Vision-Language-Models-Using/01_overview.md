# GaussianVLM: Scene-Centric 3D Vision-Language Models Using Language-Aligned Gaussian Splats for Embodied Reasoning and Beyond

- Year/Venue: 2026 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting
- Paper link: ./2026/ICRA/2026_ICRA_GaussianVLM-Scene-Centric-3D-Vision-Language-Models-Using/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these limitations, we propose a scenecentric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations.
- To process the resulting dense representations, we introduce a dual sparsifier that distills them into compact, task-relevant tokens via taskguided and location-guided pathways, producing sparse, taskaware global and ...
- Current methods show strong dependence on object detectors, introducing processing bottlenecks and limitations in taxonomic flexibility.

## Core Idea
- To address these limitations, we propose a scenecentric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations.
- Notably, we present the first Gaussian splatting-based VLM, leveraging photorealistic 3D representations derived from standard RGB images, demonstrating strong generalization: it improves performance of prior 3D VLM (LL3DA ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Notably, we present the first Gaussian splatting-based VLM, leveraging photorealistic 3D representations derived from standard RGB images, demonstrating strong generalization: it improves performance of prior 3D VLM (LL3DA ...
- Current methods show strong dependence on object detectors, introducing processing bottlenecks and limitations in taxonomic flexibility.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Notably, we present the first Gaussian splatting-based VLM, leveraging photorealistic 3D representations derived from standard RGB images, demonstrating strong generalization: it improves performance of prior 3D VLM (LL3DA ...
- To address these limitations, we propose a scenecentric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations.
- Our approach directly embeds rich linguistic features into the 3D scene representation by associating language with each Gaussian primitive, achieving early modality alignment.

## Abstract Cue
- — As multimodal language models advance, their application to 3D scene understanding is a fast-growing frontier, driving the development of 3D Vision-Language Models (VLMs).
