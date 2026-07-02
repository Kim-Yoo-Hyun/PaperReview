# Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion, semantic
- Paper link: ./2024/ECCV/2024_ECCV_Open-Vocabulary-3D-Semantic-Segmentation-with-Text-to-Imag/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Motivated by the advance of aligning text and image embeddings with large-scale foundation models , existing methods mitigate this challenge by lifting the image features from foundation models ...
- Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data .
- Traditional studies in this field usually target solving this problem in a closed-set fashion , resulting in models that can only be used to make predictions within the ...

## Core Idea
- We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic segmentation and visual ...
- We provide qualitative analysis of our approach and OpenScene for the zero-shot visual grounding task in Fig.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We show that it outperforms competitive baselines and achieves significant improvements over state-of-the-art methods.
- In particular, Diff2Scene improves the state-of-the-art method on ScanNet200 by 12%.
- We conduct a series of experiments to demonstrate the effectiveness of Diff2Scene on a variety of zero-shot 3D scene understanding benchmarks.

## Limitation
- There are several limitations of the proposed model.

## Contribution
- We show that it outperforms competitive baselines and achieves significant improvements over state-of-the-art methods.
- In particular, Diff2Scene improves the state-of-the-art method on ScanNet200 by 12%.
- We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic segmentation and visual ...

## Abstract Cue
- In this paper, we investigate the use of diffusion models which are pre-trained on large-scale image-caption pairs for open-vocabulary 3D semantic understanding.
