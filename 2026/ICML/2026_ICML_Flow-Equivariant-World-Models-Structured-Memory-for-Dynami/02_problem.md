# Problem

- Year/Venue: 2026 / ICML
- Category: 3D Equivariance, Calibration, and Registration
- Tags: equivariant, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Flow-Equivariant-World-Models-Structured-Memory-for-Dynami/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- These sensory streams and the underlying dynamics of the world obey smooth, timeparameterized symmetries which existing world models ignore.
- Without a memory that respects this structure, partial observability presents a major obstacle to existing methods: each observation reveals only a fraction of the world, while unobserved regions ...
- When an agent observes dynamics, turns away, then turns back to the original viewpoint, flow equivariance asserts dynamics continue even when unobserved; existing work loses track of objects ...

## 해결하려는 문제
- We demonstrate the advantage of this framework over state-ofthe-art diffusion, memory-augmented, and recurrent world model architectures on 2D and 3D partially observed video world modeling benchmarks.
- In this work, we introduce Flow Equivariant World Modeling, a framework that leverages time-parameterized symmetries within a latent memory for stable and accurate dynamics prediction over long horizons.
- More broadly, our results suggest that predictive representations become more powerful when they are organized in line with the temporal and dynamical structure of the world they model.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
