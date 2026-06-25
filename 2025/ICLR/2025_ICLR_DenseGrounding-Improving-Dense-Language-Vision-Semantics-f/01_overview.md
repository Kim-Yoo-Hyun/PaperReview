# DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding

- Year/Venue: 2025 / ICLR Poster
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision, semantic
- Authors: Henry Zheng, Hao Shi, Qihang Peng, Yong Xien Chng, Rui Huang, Yepeng Weng, zhongchao shi, Gao Huang
- Paper: https://openreview.net/forum?id=iGafR0hSln
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Enabling intelligent agents to comprehend and interact with 3D environments through natural language is crucial for advancing robotics and human-computer interaction.
- Method cue: We propose DenseGrounding, a novel approach designed to address these issues by enhancing both visual and textual semantics.
- Result cue: Extensive experiments show that DenseGrounding significantly outperforms existing methods in overall accuracy, achieving improvements of **5.81%** and **7.56%** when trained on the comprehensive full ...

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, semantic.
- 초록에서 확인되는 주요 cue: Enabling, However, DenseGrounding, For, Hierarchical, Scene, Semantic, Enhancer.
