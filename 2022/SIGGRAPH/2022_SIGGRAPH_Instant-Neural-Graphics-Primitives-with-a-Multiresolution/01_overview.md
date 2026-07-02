# Instant Neural Graphics Primitives with a Multiresolution Hash Encoding

- Year/Venue: 2022 / SIGGRAPH
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, efficiency
- Paper link: ./2022/SIGGRAPH/2022_SIGGRAPH_Instant-Neural-Graphics-Primitives-with-a-Multiresolution/paper.pdf
- Code/Project: https://nvlabs.github.io/instant-ngp/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Unlike prior work, no structural updates to the data structure are needed at any point during training. • Efficiency: our hash table lookups are O (1) and do ...
- However, such data structures rely on heuristics and structural modifications (such as pruning, splitting, or merging) that may complicate the training process, limit the method to a specific ...
- The hash tables thus automatically prioritize the sparse areas with the most important fine scale detail.

## Core Idea
- Such hash collisions cause the colliding training gradients to average, meaning that the largest gradients—those most relevant to the loss function—will dominate.
- Unlike prior work, no structural updates to the data structure are needed at any point during training. • Efficiency: our hash table lookups are O (1) and do ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 2021], which achieves state-of-the-art results in both quality and speed by prefixing its small MLP with a lookup from an octree of trainable feature vectors.
- With a similar number of parameters (𝑇 = 224 ), our method achieves the same PSNR after 2.5 minutes of training, peaking at 41.9 dB after 4 min.
- 2021] have shown impressive results when fitting very large images—up to a billion pixels—with high fidelity at even the smallest scales.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Abstract Cue
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
