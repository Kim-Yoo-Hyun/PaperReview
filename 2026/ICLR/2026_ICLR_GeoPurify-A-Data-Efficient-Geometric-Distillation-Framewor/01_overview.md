# GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Authors: Weijia Dou, Xu Zhang, Yi Bin, Jian Liu, Bo Peng, Guoqing Wang, Yang Yang, Heng Tao Shen
- Paper: https://openreview.net/forum?id=mN49LupE8l
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Recent attempts to transfer features from 2D Vision–Language Models (VLMs) to 3D semantic segmentation expose a persistent trade-off.
- Method cue: To exploit this property, we propose \textbf{GeoPurify} that applies a small Student Affinity Network to purify 2D VLM-generated 3D point features using geometric priors ...
- Result cue: Benefiting from latent geometric information and the learned affinity network, GeoPurify effectively mitigates the trade-off and achieves superior data efficiency.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: semantic, alignment, 3D Vision.
- 초록에서 확인되는 주요 cue: Recent, Vision, Language, Models, VLMs, Directly, The, GeoPurify.
