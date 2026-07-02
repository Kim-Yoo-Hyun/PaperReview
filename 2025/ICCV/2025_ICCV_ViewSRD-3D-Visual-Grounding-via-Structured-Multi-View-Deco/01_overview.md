# ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ViewSRD-3D-Visual-Grounding-via-Structured-Multi-View-Deco/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- However, existing methods struggle with disentangling targets from anchors in complex multi-anchor queries and resolving inconsistencies in spatial descriptions caused by perspective variations.

## Core Idea
- To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- Our SRD module is inherently model-agnostic, operating independently of the training process by focusing exclusively on decoupling complex multi-anchor queries into simpler single-anchor queries.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on 3D visual grounding datasets show that ViewSRD significantly outperforms state-of-the-art methods, particularly in complex queries requiring precise spatial differentiation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on 3D visual grounding datasets show that ViewSRD significantly outperforms state-of-the-art methods, particularly in complex queries requiring precise spatial differentiation.
- To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- However, existing methods struggle with disentangling targets from anchors in complex multi-anchor queries and resolving inconsistencies in spatial descriptions caused by perspective variations.

## Abstract Cue
- (a) Regular 3D visual grounding Multi-anchor Query Sentence 3D visual grounding aims to identify and localize objects in a 3D space based on textual descriptions.
