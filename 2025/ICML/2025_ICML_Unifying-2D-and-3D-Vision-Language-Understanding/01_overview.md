# Unifying 2D and 3D Vision-Language Understanding

- Year/Venue: 2025 / ICML Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Unifying-2D-and-3D-Vision-Language-Understanding/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The key limitation, however, is dataset availability: while 2D datasets are vast and well-curated, 3D datasets remain scarce and expensive to annotate (Dai et al., 2017; Yeshwanth et ...
- Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models more effective?
- We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory data available in ...

## Core Idea
- We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory data available in ...
- We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGBD images, outperforming box-based approaches.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With these innovations, our model achieves state-of-the-art performance across multiple 3D vision-language grounding tasks, demonstrating the potential of transferring advances from 2D vision-language learning to the dataconstrained 3D ...
- At first glance, this reliance on 2D models appears counterintuitive, as prior research has consistently shown that 3D models outperform their 2D counterparts when trained on comparable amounts ...
- We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGBD images, outperforming box-based approaches.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGBD images, outperforming box-based approaches.
- We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory data available in ...
- With these innovations, our model achieves state-of-the-art performance across multiple 3D vision-language grounding tasks, demonstrating the potential of transferring advances from 2D vision-language learning to the dataconstrained 3D ...

## Abstract Cue
- rich 3D information, these systems predominantly use 2D vision-language models to interpret their sensory video input, rather than leveraging 3D models that incorporate depth and egomotion.
