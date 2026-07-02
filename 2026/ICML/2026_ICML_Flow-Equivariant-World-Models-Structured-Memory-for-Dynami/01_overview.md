# Flow Equivariant World Models: Structured Memory for Dynamic Environments

- Year/Venue: 2026 / ICML
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Flow-Equivariant-World-Models-Structured-Memory-for-Dynami/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- These sensory streams and the underlying dynamics of the world obey smooth, timeparameterized symmetries which existing world models ignore.
- Without a memory that respects this structure, partial observability presents a major obstacle to existing methods: each observation reveals only a fraction of the world, while unobserved regions ...
- When an agent observes dynamics, turns away, then turns back to the original viewpoint, flow equivariance asserts dynamics continue even when unobserved; existing work loses track of objects ...

## Core Idea
- In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and accurate dynamics prediction over long horizons.
- We demonstrate the advantage of this framework over state-ofthe-art diffusion, memory-augmented, and recurrent world model architectures on 2D and 3D partially observed video world modeling benchmarks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate the advantage of this framework over state-ofthe-art diffusion, memory-augmented, and recurrent world model architectures on 2D and 3D partially observed video world modeling benchmarks.
- More broadly, our results suggest that predictive representations become more powerful when they are organized in line with the temporal and dynamical structure of the world they model.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We demonstrate the advantage of this framework over state-ofthe-art diffusion, memory-augmented, and recurrent world model architectures on 2D and 3D partially observed video world modeling benchmarks.
- In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and accurate dynamics prediction over long horizons.
- More broadly, our results suggest that predictive representations become more powerful when they are organized in line with the temporal and dynamical structure of the world they model.

## Abstract Cue
- Embodied systems experience the world as ‘a symphony of flows’: a combination of many continuous streams of sensory input coupled to selfmotion, interwoven with the dynamics of external objects.
