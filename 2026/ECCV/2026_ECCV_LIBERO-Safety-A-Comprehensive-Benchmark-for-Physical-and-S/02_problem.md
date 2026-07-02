# Problem

- Year/Venue: 2026 / ECCV
- Category: Benchmarks and Datasets
- Tags: VLA, Vision-Language Model, Benchmark, semantic
- Paper link: ./2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/paper.pdf
- Code/Project: https://libero-safety.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. – Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and scalability bottlenecks of ...
- First, their exclusive reliance on human teleoperation is prohibitively time-consuming, severely bottlenecking the scalability required to train robust foundation models.
- By coupling sparse human intent with an optimization-based motion planner , we ensure the rapid synthesis of large-scale, kinematically feasible, and collision-free expert demonstrations. – Large-Scale Safety Dataset: ...

## 해결하려는 문제
- To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity.
- To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline.
- Our analysis reveals a critical generalization-safety tension: although high-diversity training fosters safer trajectories, task success remains fundamentally bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.

## 선행 연구 / 배경 단서
- This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. – Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and scalability bottlenecks of ...
- Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.
- Unlike existing benchmarks, our framework systematically evaluates the physical and semantic safety boundaries of VLA models through parameterized task specifications and multi-dimensional hazard scenarios.
